"""Independent Fig. 3 density, Fermi-density, and B.1 source audit.

Uses the archived Bollig Fig. 3/Fig. 4 PDF vector paths and the public Caputo
SFHo-18.8 profile reconstruction. It does not modify production rates,
transport, luminosity, or axial outputs.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import expit

from reference import (
    M_MU,
    negative_muon_density_and_degeneracy,
    compton_production,
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_CAPUTO_N = ROOT / "data" / "n_mu_over_n0_caputo_vertices.csv"
DEFAULT_BOLLIG_PATHS = HERE / "outputs" / "bollig_fig3_fig4_vector_paths_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "bollig_muon_density_b1_source_audit_2026-11-09.json"
HBARC = 197.3269804
N0_FM3 = 0.181  # Caputo et al. Fig. 1 caption: n0 = 0.181 fm^-3.


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fermi_density_fm3(temperature: float, chemical: float) -> tuple[float, float]:
    """Return n(mu-) and n(mu+) in fm^-3, with two spin states each."""
    if temperature <= 0:
        raise ValueError("temperature must be positive")

    def density(mu):
        integral = quad(
            lambda p: p * p * float(expit((mu - np.hypot(p, M_MU)) / temperature)),
            0.0, np.inf, epsabs=0.0, epsrel=2e-9, limit=250,
        )[0] / np.pi**2
        return integral / HBARC**3

    return density(chemical), density(-chemical)


def susceptibility_fm3(temperature: float, chemical: float) -> float:
    """chi_mu = 2 int d^3p/(2pi)^3 f(1-f), for the mu-minus species."""
    integral = quad(
        lambda p: (
            p * p
            * float(expit((chemical - np.hypot(p, M_MU)) / temperature))
            * (1.0 - float(expit((chemical - np.hypot(p, M_MU)) / temperature)))
        ),
        0.0, np.inf, epsabs=0.0, epsrel=2e-9, limit=250,
    )[0] / np.pi**2
    return integral / HBARC**3


def deduplicate(points):
    out = []
    for x, y in sorted(points, key=lambda p: p[0]):
        if not out or abs(x - out[-1][0]) > 1e-8:
            out.append((float(x), float(y)))
        else:
            # Multiple path segments can repeat the same vertex. Keep the
            # last value only if the coordinate is numerically identical.
            out[-1] = (float(x), float(y))
    return np.asarray(out, dtype=float)


def linear_map(points, values):
    """Least-squares affine map coordinate = intercept + slope * physical."""
    p = np.asarray(points, dtype=float)
    v = np.asarray(values, dtype=float)
    slope, intercept = np.polyfit(v, p, 1)
    return float(intercept), float(slope)


def interpolate_curve(points, x):
    return float(np.interp(x, points[:, 0], points[:, 1]))


def rel_summary(values):
    a = np.asarray(values, dtype=float)
    return {
        "count": int(len(a)),
        "mean_abs_relative_difference": float(np.mean(np.abs(a))),
        "rms_relative_difference": float(np.sqrt(np.mean(a * a))),
        "max_abs_relative_difference": float(np.max(np.abs(a))),
        "min_relative_difference": float(np.min(a)),
        "max_relative_difference": float(np.max(a)),
    }


def run(profile_path=DEFAULT_PROFILE, caputo_n_path=DEFAULT_CAPUTO_N,
        bollig_path_path=DEFAULT_BOLLIG_PATHS):
    profile_rows = read_csv(profile_path)
    profile_r = np.asarray([float(x["r_km"]) for x in profile_rows])
    temp = np.asarray([float(x["T_MeV"]) for x in profile_rows])
    mu = np.asarray([float(x["mu_mu_MeV"]) for x in profile_rows])

    caputo_rows = read_csv(caputo_n_path)
    caputo_r = np.asarray([float(x["r_km"]) for x in caputo_rows])
    caputo_n_over_n0 = np.asarray([float(x["value"]) for x in caputo_rows])
    caputo_n = N0_FM3 * caputo_n_over_n0

    archive = json.loads(bollig_path_path.read_text(encoding="utf-8"))
    paths = archive["candidate_vector_paths"]
    fig3 = next(x for x in paths if x["index"] == 33)
    fig4 = next(x for x in paths if x["index"] == 193)
    if fig3["color"] != [0.6999970078468323, 0.6999970078468323, 0.0]:
        raise AssertionError("Fig. 3 path 33 is not the archived yellow SFHo-18.8 curve")
    if fig4["color"] != [0.6999970078468323, 0.6999970078468323, 0.0]:
        raise AssertionError("Fig. 4 path 193 is not the archived yellow SFHo-18.8 curve")

    fig3_points = deduplicate(fig3["points"])
    # Fig. 3 axis tick coordinates read from the PDF vector tick marks:
    # x: 5, 10, 15, 20 km; y: 10^-7 ... 10^-2 fm^-3.
    x0, dx = linear_map(
        [135.52529907226562, 185.83108520507812,
         236.13726806640625, 286.44146728515625],
        [5.0, 10.0, 15.0, 20.0],
    )
    y0, dy = linear_map(
        [285.0899658203125, 265.39776611328125, 245.70758056640625,
         226.0169677734375, 206.32675170898438, 186.6345672607422],
        [-7.0, -6.0, -5.0, -4.0, -3.0, -2.0],
    )
    # y_pdf = y0 + dy*log10(n/fm^-3), with dy < 0.
    def bollig_n(radius):
        y_pdf = interpolate_curve(fig3_points, x0 + dx * radius)
        return float(10.0 ** ((y_pdf - y0) / dy))

    fig4_points = deduplicate(fig4["points"])

    # Fig. 1 provides Bollig's temperature profile for the same SFHo-18.8
    # model and 1 s post-bounce time. Use its actual PDF vector axes to test
    # whether the Fig. 3 density residual can be explained by T(r).
    fig1 = next(x for x in archive["fig1_temperature_vector_paths"] if x["index"] == 0)
    if fig1["color"] != [0.6999970078468323, 0.6999970078468323, 0.0]:
        raise AssertionError("Fig. 1 path 0 is not the archived yellow SFHo-18.8 curve")
    fig1_points = deduplicate(fig1["points"])
    x1, dx1 = linear_map(
        [389.2326354980469, 442.6397399902344,
         496.04840087890625, 549.4555053710938],
        [5.0, 10.0, 15.0, 20.0],
    )
    y1, dy1 = linear_map(
        [177.6042938232422, 158.30784606933594, 139.01141357421875,
         119.71297454833984, 100.41653442382812, 81.12008666992188,
         61.8236],
        [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0],
    )
    def bollig_temperature(radius):
        y_pdf = interpolate_curve(fig1_points, x1 + dx1 * radius)
        return float((y_pdf - y1) / dy1)

    # Fig. 4 axis ticks are taken from the actual black PDF vector tick marks,
    # not text bounding boxes (whose glyph tops/left edges are offset from ticks).
    # x ticks 5,10,15,20 km: drawing paths 248,253,258,263.
    # y ticks -4,-2,0,2,4: drawing paths 225,229,233,237,241.
    x4, dx4 = linear_map(
        [390.42822265625, 443.4383544921875,
         496.4469299316406, 549.4570922851562],
        [5.0, 10.0, 15.0, 20.0],
    )
    y4, dy4 = linear_map(
        [291.43780517578125, 263.7730712890625, 236.10794067382812,
         208.44161987304688, 180.77688598632812],
        [-4.0, -2.0, 0.0, 2.0, 4.0],
    )
    def bollig_eta(radius):
        y_pdf = interpolate_curve(fig4_points, x4 + dx4 * radius)
        return float((y_pdf - y4) / dy4)

    # Step 1: compare absolute density curves on the Caputo profile's nodes.
    overlap = (caputo_r >= 5.0) & (caputo_r <= 15.0)
    common_r = caputo_r[overlap]
    n_bollig = np.asarray([bollig_n(r) for r in common_r])
    n_caputo = caputo_n[overlap]
    bollig_vs_caputo = n_caputo / n_bollig - 1.0

    shell = (common_r >= 12.0) & (common_r <= 15.0)

    # Step 2: independently reconstruct n(mu-) and n(mu+) from the
    # full relativistic Fermi-Dirac distribution on the same radial nodes.
    t_common = np.interp(common_r, profile_r, temp)
    mu_common = np.interp(common_r, profile_r, mu)
    fermi_minus, fermi_plus, fermi_net, fermi_total = [], [], [], []
    susceptibility, fdeg = [], []
    ref_density, ref_fdeg = negative_muon_density_and_degeneracy(
        t_common, mu_common
    )
    for t, m in zip(t_common, mu_common):
        nm, np_ = fermi_density_fm3(float(t), float(m))
        chi = susceptibility_fm3(float(t), float(m))
        fermi_minus.append(nm)
        fermi_plus.append(np_)
        fermi_net.append(nm - np_)
        fermi_total.append(nm + np_)
        susceptibility.append(chi)
        fdeg.append(chi / nm if nm > 0 else 0.0)
    fermi_minus = np.asarray(fermi_minus)
    fermi_plus = np.asarray(fermi_plus)
    fermi_net = np.asarray(fermi_net)
    fermi_total = np.asarray(fermi_total)
    susceptibility = np.asarray(susceptibility)
    fdeg = np.asarray(fdeg)
    fermi_minus_vs_caputo = fermi_minus / n_caputo - 1.0
    fermi_net_vs_caputo = fermi_net / n_caputo - 1.0
    fermi_total_vs_caputo = fermi_total / n_caputo - 1.0
    fermi_minus_vs_bollig = fermi_minus / n_bollig - 1.0
    # Compare Fig. 1 and Fig. 4 on the dense thermodynamic-profile grid,
    # not only on the much sparser n_mu plotting vertices.
    profile_mask = (profile_r >= 5.0) & (profile_r <= 15.0)
    profile_r_common = profile_r[profile_mask]
    profile_shell = (profile_r_common >= 12.0) & (profile_r_common <= 15.0)
    profile_t_common = temp[profile_mask]
    profile_mu_common = mu[profile_mask]
    eta_bollig_profile = np.asarray([bollig_eta(float(r)) for r in profile_r_common])
    eta_caputo_profile = profile_mu_common / profile_t_common
    eta_caputo_vs_bollig = eta_caputo_profile / eta_bollig_profile - 1.0
    t_bollig_profile = np.asarray([bollig_temperature(float(r)) for r in profile_r_common])
    t_caputo_vs_bollig = profile_t_common / t_bollig_profile - 1.0
    # Retain the density-node values for the implied-temperature diagnostic.
    eta_bollig = np.asarray([bollig_eta(float(r)) for r in common_r])
    t_bollig = np.asarray([bollig_temperature(float(r)) for r in common_r])

    # Verify the archived reference.py implementation against the separately
    # integrated n(mu-) and chi_mu; B.17 uses n_mu*Fdeg = chi_mu.
    ref_density_fm3 = ref_density / HBARC**3
    ref_n_rel = ref_density_fm3 / fermi_minus - 1.0
    ref_chi_fm3 = ref_density * ref_fdeg / HBARC**3
    chi_rel = ref_chi_fm3 / susceptibility - 1.0
    nFdeg_rel = (fermi_minus * fdeg) / susceptibility - 1.0

    # Step 3: check the local B.16 Compton source formula used inside B.1.
    # At mV=10 MeV the dimuon channel is closed; this tests the muon-density
    # convention and the n_mu*Fdeg factor, not the neutrino source.
    compton_checks = []
    for r_target in (8.0, 10.0, 12.0, 15.0):
        t = float(np.interp(r_target, profile_r, temp))
        m = float(np.interp(r_target, profile_r, mu))
        nm, _ = fermi_density_fm3(t, m)
        chi = susceptibility_fm3(t, m)
        nm_mev3 = nm * HBARC**3
        chi_mev3 = chi * HBARC**3
        fdeg_here = chi_mev3 / nm_mev3
        for omega in (12.0, 15.0, 20.0, 30.0, 50.0, 100.0):
            mV = 10.0
            v = np.sqrt(1.0 - (mV / omega)**2)
            alpha = 1.0 / 137.035999084
            alpha_v = 1.0 / (4.0 * np.pi)
            bose = 1.0 / np.expm1(omega / t)
            direct = (
                chi_mev3 * (2.0 / v) * bose
                * (8.0 * np.pi * alpha * alpha_v / (3.0 * M_MU**2))
                * (1.0 + mV**2 / (2.0 * omega**2)) * v
            )
            reference = float(compton_production(
                mV, omega, t, nm_mev3, fdeg_here
            ))
            compton_checks.append({
                "radius_km": r_target, "omega_MeV": omega,
                "n_mu_minus_fm3": nm, "n_mu_plus_fm3": fermi_density_fm3(t, m)[1],
                "Fdeg": fdeg_here,
                "n_mu_Fdeg_MeV3": chi_mev3,
                "direct_B16_MeV": direct,
                "reference_py_B16_MeV": reference,
                "relative_residual": reference / direct - 1.0,
            })

    # Step 2 cross-check: infer the temperature needed to reproduce Bollig
    # Fig. 3's density if its Fig. 4 eta=mu/T is retained. This is a diagnostic,
    # not an adopted profile or an assumption that the curves are same snapshot.
    implied_temperature = []
    for r, n_b, t_cap, m_cap in zip(common_r, n_bollig, t_common, mu_common):
        eta = bollig_eta(float(r))
        target = float(n_b)
        def residual(t):
            nm, _ = fermi_density_fm3(t, eta * t)
            return nm - target
        lo, hi = 0.5, 150.0
        if residual(lo) * residual(hi) > 0:
            t_imp = None
        else:
            t_imp = float(brentq(residual, lo, hi, xtol=1e-9, rtol=1e-10))
        implied_temperature.append({
            "radius_km": float(r),
            "eta_Bollig": eta,
            "T_Caputo_MeV": float(t_cap),
            "T_implied_from_Bollig_nmu_MeV": t_imp,
            "T_implied_over_T_Caputo": (t_imp / float(t_cap) if t_imp else None),
        })

    selected = []
    for r in (5.0, 8.0, 10.0, 12.0, 12.5, 13.0, 14.0, 15.0):
        n_b = bollig_n(r)
        n_c = float(np.interp(r, caputo_r, caputo_n))
        t = float(np.interp(r, profile_r, temp))
        m = float(np.interp(r, profile_r, mu))
        n_m, n_p = fermi_density_fm3(t, m)
        selected.append({
            "radius_km": r,
            "Bollig_Fig3_nmu_fm3": n_b,
            "Caputo_plotted_nmu_fm3": n_c,
            "Caputo_FD_nmu_minus_fm3": n_m,
            "Caputo_FD_nmu_plus_fm3": n_p,
            "Caputo_FD_nmu_net_fm3": n_m - n_p,
            "Caputo_FD_over_plotted_minus_1": n_m / n_c - 1.0,
            "Caputo_plotted_over_Bollig_minus_1": n_c / n_b - 1.0,
            "Caputo_T_MeV": t,
            "Caputo_mu_mu_MeV": m,
            "Bollig_mu_mu_over_T": bollig_eta(r),
            "Bollig_Fig1_T_MeV": bollig_temperature(r),
            "Caputo_T_over_Bollig_Fig1_T_minus_1": t / bollig_temperature(r) - 1.0,
        })

    max_b1_closure = max(abs(x["relative_residual"]) for x in compton_checks)
    max_n_rel = float(np.max(np.abs(ref_n_rel)))
    max_chi_rel = float(np.max(np.abs(chi_rel)))
    max_nFdeg_rel = float(np.max(np.abs(nFdeg_rel)))
    if max_b1_closure > 1e-10:
        raise AssertionError(f"B.16 source closure failed: {max_b1_closure}")
    if max_n_rel > 1e-8 or max_chi_rel > 1e-8 or max_nFdeg_rel > 1e-12:
        raise AssertionError("Independent Fermi integral and reference.py disagree")

    return {
        "source": {
            "Bollig": "arXiv:2005.07141v7, Fig. 3 and Fig. 4",
            "Caputo": "arXiv:2109.03244v3, Fig. 1",
            "n0_fm3": N0_FM3,
            "Bollig_pdf_sha256": archive["pdf_sha256"],
            "Caputo_density_source_sha256": sha256(caputo_n_path),
            "Caputo_profile_sha256": sha256(profile_path),
            "vector_path_indices": {"Fig3_SFHo18_8": 33, "Fig4_SFHo18_8": 193},
        },
        "axis_calibration": {
            "Fig3_radius_pdf_x0": x0, "Fig3_radius_pdf_dx_per_km": dx,
            "Fig3_log10_density_pdf_y0": y0, "Fig3_pdf_dy_per_decade": dy,
            "Fig4_radius_pdf_x0": x4, "Fig4_radius_pdf_dx_per_km": dx4,
            "Fig4_eta_pdf_y0": y4, "Fig4_pdf_dy_per_eta": dy4,
        },
        "comparison_summary": {
            "Caputo_plotted_vs_Bollig_Fig3_5_15km": rel_summary(bollig_vs_caputo),
            "Caputo_plotted_vs_Bollig_Fig3_12_15km": rel_summary(bollig_vs_caputo[shell]),
            "Caputo_FD_mu_minus_vs_Caputo_plotted_5_15km": rel_summary(fermi_minus_vs_caputo),
            "Caputo_FD_mu_minus_vs_Caputo_plotted_12_15km": rel_summary(fermi_minus_vs_caputo[shell]),
            "Caputo_FD_net_vs_Caputo_plotted_5_15km": rel_summary(fermi_net_vs_caputo),
            "Caputo_FD_total_vs_Caputo_plotted_5_15km": rel_summary(fermi_total_vs_caputo),
            "Caputo_FD_mu_minus_vs_Bollig_Fig3_5_15km": rel_summary(fermi_minus_vs_bollig),
            "Caputo_FD_mu_minus_vs_Bollig_Fig3_12_15km": rel_summary(fermi_minus_vs_bollig[shell]),
            "Caputo_mu_over_T_vs_Bollig_Fig4_5_15km": rel_summary(eta_caputo_vs_bollig),
            "Caputo_mu_over_T_vs_Bollig_Fig4_12_15km": rel_summary(eta_caputo_vs_bollig[profile_shell]),
            "Caputo_T_vs_Bollig_Fig1_5_15km": rel_summary(t_caputo_vs_bollig),
            "Caputo_T_vs_Bollig_Fig1_12_15km": rel_summary(t_caputo_vs_bollig[profile_shell]),
            "Bollig_Fig1_T_vs_T_implied_from_Fig3_density_and_Fig4_eta_12_15km": rel_summary(
                np.asarray([
                    (x["T_implied_from_Bollig_nmu_MeV"] / bollig_temperature(x["radius_km"]) - 1.0)
                    for x in implied_temperature
                    if 12.0 <= x["radius_km"] <= 15.0
                ], dtype=float)
            ),
            "reference_py_vs_independent_FD_density_max_abs_relative": max_n_rel,
            "reference_py_vs_independent_FD_susceptibility_max_abs_relative": max_chi_rel,
            "n_mu_Fdeg_equals_susceptibility_max_abs_relative": max_nFdeg_rel,
            "B16_direct_vs_reference_py_max_abs_relative": max_b1_closure,
        },
        "selected_radii": selected,
        "implied_temperature_diagnostic": implied_temperature,
        "B16_local_source_checks": compton_checks,
        "interpretation": {
            "B1_muon_density_definition": (
                "One negative-muon species with two spin states, as in Blinov Eq. (B.17); "
                "n_mu*Fdeg equals the negative-muon susceptibility integral."
            ),
            "profile_status": (
                "Caputo plotted n_mu is checked against the independent negative-muon FD integral. "
                "The direct Bollig Fig. 3 density comparison is kept separate and must not be inferred "
                "from the Fig. 4 degeneracy-parameter agreement alone."
            ),
            "no_production_changes": True,
        },
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    p.add_argument("--caputo-density", type=Path, default=DEFAULT_CAPUTO_N)
    p.add_argument("--bollig-paths", type=Path, default=DEFAULT_BOLLIG_PATHS)
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    a = p.parse_args()
    result = run(a.profile, a.caputo_density, a.bollig_paths)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["comparison_summary"], indent=2))
    print(json.dumps(result["selected_radii"], indent=2))
    print(f"Saved {a.output}")


if __name__ == "__main__":
    main()
