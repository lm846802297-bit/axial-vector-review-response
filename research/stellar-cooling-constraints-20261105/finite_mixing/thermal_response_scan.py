"""Reproducible local thermal-response scan; no stellar transport is performed."""

from __future__ import annotations
import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from moving_muon_compton import thermal_compton_emissivity
from thermal_dimuon import thermal_dimuon_emissivity
import rates


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def profile_at_radius(profile, radius_km):
    rows = np.genfromtxt(profile, delimiter=",", names=True)
    i = int(np.argmin(np.abs(rows["r_km"]-radius_km)))
    row = rows[i]
    return {
        "r_km": float(row["r_km"]),
        "temperature_MeV": float(row["T_MeV"]),
        "mu_mu_MeV": float(row["mu_mu_MeV"]),
        "mu_numu_MeV": float(row["mu_numu_MeV"]),
        "lapse": float(row["lapse"]),
    }


def compton_case(mass, point, couplings, energy_order=12, orders=(12,8,8,8)):
    results = {}
    for name, (gv, ga) in couplings.items():
        results[name] = thermal_compton_emissivity(
            mass, point["temperature_MeV"], point["mu_mu_MeV"],
            gv, ga, energy_order=energy_order, orders=orders
        )
    qv = np.asarray(results["vector"]["emissivity_by_mode_MeV5"])
    qa = np.asarray(results["axial"]["emissivity_by_mode_MeV5"])
    qm = np.asarray(results["uv_theta_1e-2"]["emissivity_by_mode_MeV5"])
    gv, ga = couplings["uv_theta_1e-2"]
    incoherent = gv*gv*qv+ga*ga*qa
    return {
        "mass_MeV": mass,
        "profile_point": point,
        "Q_vector_by_mode_MeV5": qv.tolist(),
        "Q_axial_by_mode_MeV5": qa.tolist(),
        "Q_mixed_by_mode_MeV5": qm.tolist(),
        "Q_vector_total_MeV5": float(np.sum(qv)),
        "Q_axial_total_MeV5": float(np.sum(qa)),
        "Q_mixed_total_MeV5": float(np.sum(qm)),
        "Q_axial_over_vector_by_mode": (qa/qv).tolist(),
        "Q_axial_over_vector_total": float(np.sum(qa)/np.sum(qv)),
        "Q_mixed_over_axial_total": float(np.sum(qm)/np.sum(qa)),
        "mixed_interference_fraction_by_mode": (
            (qm-incoherent)/np.maximum(np.abs(qm),1e-300)
        ).tolist(),
        "charge_resolved_mixed_Q_by_mode_MeV5":
            results["uv_theta_1e-2"]["emissivity_by_charge_and_mode_MeV5"],
        "mode_order": ["L", "+", "-"],
        "polarization_basis": "medium rest frame; A' momentum along +z",
        "max_detailed_balance_relative_error": max(
            r["max_detailed_balance_relative_error"] for r in results.values()
        ),
        "max_Eq_5_12_relative_residual": max(
            r["max_Eq_5_12_relative_residual"] for r in results.values()
        ),
        "max_final_muon_shell_relative_error": max(
            r["max_final_muon_shell_relative_error"] for r in results.values()
        ),
        "quadrature": {"energy_order": energy_order, "inner_orders": list(orders)},
    }


def dimuon_case(mass, point, couplings, energy_order=24, angular_order=64):
    results = {
        name: thermal_dimuon_emissivity(
            mass, point["temperature_MeV"], point["mu_mu_MeV"],
            gv, ga, energy_order=energy_order, angular_order=angular_order
        )
        for name, (gv, ga) in couplings.items()
    }
    v = results["vector"]
    a = results["axial"]
    mixed = results["uv_theta_1e-2"]
    threshold = 2.0*rates.M_MU
    beta2 = max(0.0, 1.0-threshold**2/mass**2)
    expected = beta2/(1.0+2.0*rates.M_MU**2/mass**2) if mass>threshold else 0.0
    qv = np.asarray(v["emissivity_by_mode_MeV5"])
    qa = np.asarray(a["emissivity_by_mode_MeV5"])
    qm = np.asarray(mixed["emissivity_by_mode_MeV5"])
    gv, ga = couplings["uv_theta_1e-2"]
    incoherent = gv*gv*qv+ga*ga*qa
    return {
        "mass_MeV": mass,
        "mass_over_threshold": mass/threshold,
        "open": v["open"],
        "Q_vector_by_mode_MeV5": qv.tolist(),
        "Q_axial_by_mode_MeV5": qa.tolist(),
        "Q_mixed_by_mode_MeV5": qm.tolist(),
        "Q_vector_total_MeV5": v["emissivity_total_MeV5"],
        "Q_axial_total_MeV5": a["emissivity_total_MeV5"],
        "Q_mixed_total_MeV5": mixed["emissivity_total_MeV5"],
        "Q_axial_over_vector_total": (
            a["emissivity_total_MeV5"]/v["emissivity_total_MeV5"]
            if v["emissivity_total_MeV5"] else None
        ),
        "analytic_vacuum_width_ratio": expected,
        "integrated_ratio_minus_analytic": (
            a["emissivity_total_MeV5"]/v["emissivity_total_MeV5"]-expected
            if v["emissivity_total_MeV5"] else None
        ),
        "mixed_interference_fraction_by_mode": (
            (qm-incoherent)/np.maximum(np.abs(qm),1e-300)
        ).tolist(),
        "max_detailed_balance_relative_error": max(
            r["max_detailed_balance_relative_error"] for r in results.values()
        ),
        "quadrature": {"energy_order": energy_order, "angular_order": angular_order},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(HERE/"outputs"/"thermal_response_scan.json"))
    args = parser.parse_args()

    profile = ROOT/"data"/"sfho188_digitized.csv"
    center = profile_at_radius(profile, 0.0)
    mid = profile_at_radius(profile, 12.5)
    theta = 1.0e-2
    couplings = {
        "vector": (1.0,0.0),
        "axial": (0.0,-1.0),
        "uv_theta_1e-2": (math.sin(theta)**2,-math.cos(theta)**2),
    }

    # Same local profile point and current endpoints across the mass grid.
    compton_masses = [0.01,0.1,1.0,10.0,100.0,220.0]
    compton_center = [
        compton_case(m,center,couplings,energy_order=12,orders=(12,8,8,8))
        for m in compton_masses
    ]
    # A second radius isolates the local thermodynamic dependence at 10 MeV.
    compton_mid_10 = compton_case(
        10.0,mid,couplings,energy_order=12,orders=(12,8,8,8)
    )

    # Explicit inner/outer quadrature refinement at the central 10 MeV point.
    q12 = thermal_compton_emissivity(
        10.0,center["temperature_MeV"],center["mu_mu_MeV"],
        0.0,-1.0,energy_order=12,orders=(14,10,10,10)
    )["emissivity_total_MeV5"]
    q16 = thermal_compton_emissivity(
        10.0,center["temperature_MeV"],center["mu_mu_MeV"],
        0.0,-1.0,energy_order=16,orders=(14,10,10,10)
    )["emissivity_total_MeV5"]
    compton_convergence = {
        "benchmark_mass_MeV": 10.0,
        "current": "pure axial",
        "profile_radius_km": center["r_km"],
        "inner_orders": [14,10,10,10],
        "energy_order_12_Q_MeV5": q12,
        "energy_order_16_Q_MeV5": q16,
        "relative_change_12_to_16": q16/q12-1.0,
    }

    threshold = 2.0*rates.M_MU
    dimuon_factors = [1.0001,1.001,1.01,1.05,1.2,1.5,2.0,3.0,5.0]
    dimuon_scan = [
        dimuon_case(threshold*f,center,couplings,energy_order=24,angular_order=64)
        for f in dimuon_factors
    ]
    # Independent energy-quadrature convergence check just above threshold.
    test_mass = 1.05*threshold
    d16 = thermal_dimuon_emissivity(
        test_mass,center["temperature_MeV"],center["mu_mu_MeV"],
        0.0,-1.0,energy_order=16,angular_order=64
    )["emissivity_total_MeV5"]
    d32 = thermal_dimuon_emissivity(
        test_mass,center["temperature_MeV"],center["mu_mu_MeV"],
        0.0,-1.0,energy_order=32,angular_order=64
    )["emissivity_total_MeV5"]
    dimuon_convergence = {
        "mass_over_threshold": 1.05,
        "energy_order_16_Q_MeV5": d16,
        "energy_order_32_Q_MeV5": d32,
        "relative_change_16_to_32": d32/d16-1.0,
    }

    output = {
        "title": "Local thermal vector/axial response; no stellar transport",
        "mode_order": ["L", "+", "-"],
        "polarization_basis": (
            "Medium rest frame; A' momentum along +z; L is the longitudinal "
            "polarization and +/- are circular transverse polarizations."
        ),
        "profile": {
            "source": "reconstructed SFHo-18.8 t_pb=1s digitized profile",
            "sha256": sha256(profile),
            "center": center,
            "mid_radius": mid,
            "chemical_potential_convention": "mu_mu is the mu- chemical potential; mu+ uses -mu_mu",
        },
        "couplings_normalized_to_gX": {
            k: {"g_vector": v[0], "g_axial": v[1]}
            for k,v in couplings.items()
        },
        "compton": {
            "process": "mu^+/- + gamma <-> mu^+/- + A'",
            "mass_scan_at_center": compton_center,
            "10MeV_mid_radius_comparison": compton_mid_10,
            "quadrature_convergence": compton_convergence,
        },
        "dimuon": {
            "process": "mu+ + mu- <-> A'",
            "threshold_MeV": threshold,
            "mass_scan": dimuon_scan,
            "quadrature_convergence": dimuon_convergence,
        },
        "scope": {
            "includes": [
                "moving thermal muon momentum integral",
                "both muon charges",
                "exact 2-to-2 recoil in semi-Compton scattering",
                "Fermi blocking of the final muon",
                "Bose enhancement of the final photon",
                "amplitude-level vector-axial interference",
                "mode-resolved production and absorption",
                "full on-shell A' momentum integral for local emissivities",
                "full A' energy integral for dimuon inverse decay/decay",
            ],
            "not_included": [
                "active-neutrino emissivity",
                "radial stellar integration",
                "opacity and escape probability",
                "gravitational redshift",
                "hydrodynamic backreaction",
                "SN1987A exclusion contour",
            ],
        },
        "code_sha256": {
            "rates.py": sha256(ROOT/"rates.py"),
            "moving_muon_compton.py": sha256(HERE/"moving_muon_compton.py"),
            "thermal_dimuon.py": sha256(HERE/"thermal_dimuon.py"),
            "thermal_response_scan.py": sha256(Path(__file__)),
        },
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")
    print(json.dumps({
        "output": str(out),
        "compton_mass_points": len(compton_center),
        "dimuon_mass_points": len(dimuon_scan),
        "compton_10MeV_center_QA_over_QV":
            compton_center[3]["Q_axial_over_vector_total"],
        "dimuon_max_abs_ratio_residual": max(
            abs(x["integrated_ratio_minus_analytic"] or 0.0) for x in dimuon_scan
        ),
        "compton_12_to_16_change": compton_convergence["relative_change_12_to_16"],
        "dimuon_16_to_32_change": dimuon_convergence["relative_change_16_to_32"],
    },indent=2))


if __name__ == "__main__":
    main()
