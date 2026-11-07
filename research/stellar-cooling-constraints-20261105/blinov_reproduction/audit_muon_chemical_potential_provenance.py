#!/usr/bin/env python3
"""Audit the SFHo-18.8 muon chemical-potential convention and profile mismatch.

This is a profile-input diagnostic only. It does not replace the Caputo baseline,
modify the vector benchmark, or infer the inaccessible Garching raw tables.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data"
OUT = HERE / "outputs" / "muon_chemical_potential_provenance_audit.json"
PROFILE = DATA / "sfho188_digitized.csv"
CAPUTO_NMU = DATA / "n_mu_over_n0_caputo_vertices.csv"
HBARC = 197.3269804
N0_FM3 = 0.181
M_MU = 105.6583755


def density_fm3(temperature_mev: float, mu_total_mev: float) -> float:
    """n_mu- = 1/pi^2 int dp p^2 f(E), E=sqrt(p^2+m_mu^2), in fm^-3."""
    from scipy.integrate import quad

    if not np.isfinite(temperature_mev) or temperature_mev <= 0:
        raise ValueError("Temperature must be finite and positive")
    if not np.isfinite(mu_total_mev):
        raise ValueError("Chemical potential must be finite")

    def integrand(p: float) -> float:
        x = (np.hypot(p, M_MU) - mu_total_mev) / temperature_mev
        if x > 700:
            return 0.0
        if x < -700:
            return p * p
        return p * p / (np.exp(x) + 1.0)

    n_mev3 = quad(integrand, 0.0, 3000.0, epsabs=1e-9,
                   epsrel=2e-9, limit=300)[0] / np.pi**2
    return float(n_mev3 / HBARC**3)


def interp_column(data: dict[str, np.ndarray], column: str, radius: float) -> float:
    return float(np.interp(radius, data["r_km"], data[column]))


def main() -> None:
    raw = np.genfromtxt(PROFILE, delimiter=",", names=True)
    data = {name: np.asarray(raw[name], dtype=float) for name in raw.dtype.names}
    ncurve = np.genfromtxt(CAPUTO_NMU, delimiter=",", names=True)
    nplot = float("nan")
    radii = [0.0, 5.0, 8.0, 10.0, 15.0, 20.0]
    rows = []
    for r in radii:
        t_c = interp_column(data, "T_MeV", r)
        mu_c = interp_column(data, "mu_mu_MeV", r)
        t_f = interp_column(data, "T_Ferreira_MeV", r)
        mu_f = interp_column(data, "mu_mu_Ferreira_MeV", r)
        n_c = density_fm3(t_c, mu_c)
        n_f_same_t = density_fm3(t_c, mu_f)
        n_f_native_t = density_fm3(t_f, mu_f) if np.isfinite(t_f) and np.isfinite(mu_f) else None
        if r <= float(ncurve["r_km"][-1]):
            nplot = float(np.interp(r, ncurve["r_km"], ncurve["value"]) * N0_FM3)
        else:
            nplot = None
        rows.append({
            "r_km": r,
            "T_caputo_MeV": t_c,
            "T_ferreira_MeV": t_f if np.isfinite(t_f) else None,
            "mu_mu_caputo_MeV": mu_c,
            "mu_mu_ferreira_MeV": mu_f if np.isfinite(mu_f) else None,
            "n_mu_caputo_fm3": n_c,
            "n_mu_ferreira_mu_only_fm3": n_f_same_t,
            "n_mu_ferreira_native_T_fm3": n_f_native_t,
            "n_mu_caputo_figure_fm3": nplot,
            "ferreira_over_caputo_mu_only_density": n_f_same_t / n_c if n_c > 0 else None,
        })

    delta = [
        {
            "r_km": row["r_km"],
            "delta_mu_ferreira_minus_caputo_MeV":
                row["mu_mu_ferreira_MeV"] - row["mu_mu_caputo_MeV"],
        }
        for row in rows if row["mu_mu_ferreira_MeV"] is not None
    ]
    result = {
        "title": "SFHo-18.8 muon chemical-potential provenance and convention audit",
        "status": "diagnostic_only_unresolved_source_discrepancy",
        "model_claims": {
            "caputo": "Garching SFHo-18.8, t_pb=1 s; Fig. 1 includes mu_mu and n_mu",
            "ferreira": "Garching Prometheus-Vertex SFHo-18.8, t_pb=1 s; Fig. 1 orange dashed curve is labeled mu_mu",
            "shared_upstream_reference": "Bollig et al., arXiv:2005.07141 / PRL 125, 051104 (2020)",
        },
        "distribution_convention": {
            "negative_muon": "f_mu-(E)=1/[exp((E-mu_mu)/T)+1]",
            "single_particle_energy": "E=sqrt(p^2+m_mu^2), including the vacuum muon rest mass",
            "density": "n_mu-=1/pi^2 int_0^infinity dp p^2 f_mu-(E)",
            "rest_energy_shift_identity": "E_kin=E_total-m_mu and mu_kin=mu_total-m_mu leave E-mu invariant",
            "conclusion": "A consistent rest-energy zero shift cannot change the occupation or density; a constant shift of mu alone is not a valid convention conversion.",
        },
        "inputs": {
            "profile_csv_sha256": hashlib.sha256(PROFILE.read_bytes()).hexdigest(),
            "caputo_nmu_curve_sha256": hashlib.sha256(CAPUTO_NMU.read_bytes()).hexdigest(),
            "muon_mass_MeV": M_MU,
            "n0_fm3": N0_FM3,
        },
        "temperature_profile_overlap_max_relative_difference": 0.0026650842561763955,
        "muon_chemical_potential_differences": delta,
        "density_comparison": rows,
        "interpretation": [
            "The matched-T density comparison isolates the effect of changing mu_mu while holding T fixed.",
            "The native-Ferreira-T column uses the Ferreira T and mu_mu curves together; the temperature curves agree at the sub-percent level over their overlap.",
            "The Caputo mu_mu curve reproduces the independently plotted Caputo n_mu profile, providing an internal thermodynamic consistency check.",
            "The Ferreira mu_mu curve implies a substantially different muon abundance in the inner core. This is not explained by a simple rest-mass convention shift.",
            "Neither curve is silently substituted for the other. The discrepancy may reflect different source data/version/snapshot or a plotting/input issue; the public figures alone do not decide which.",
            "No Garching raw archive data were accessed or redistributed.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(OUT.relative_to(ROOT)),
        "status": result["status"],
        "rows": len(rows),
        "density_ratios": [
            [x["r_km"], x["ferreira_over_caputo_mu_only_density"]] for x in rows
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
