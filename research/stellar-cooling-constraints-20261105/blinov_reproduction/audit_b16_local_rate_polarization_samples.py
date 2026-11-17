"""Rebuild a 10 MeV local B.6/B.10/B.14--B.19 polarization sample package.

Local rates only: this script does not integrate global escape probabilities
or alter the scalar B.2 baseline or any axial-vector output.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import os
import platform
from pathlib import Path

import numpy as np
import scipy

import reference
import audit_b16_local_absorption as local

HERE = Path(__file__).resolve().parent
DEFAULT_PROFILE = HERE.parent / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT_DIR = HERE / "outputs"
MASS_MEV = 10.0
RADII_KM = (8.0, 12.0, 15.0, 20.0, 22.0, 25.0)
ENERGIES_MEV = (12.0, 15.0, 20.0, 30.0, 50.0, 100.0, 200.0, 300.0, 500.0)
MODES = ("L", "plus", "minus")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def git_blob_sha1(path):
    raw = Path(path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def rel(a, b):
    return abs(float(a) - float(b)) / max(abs(float(b)), 1.0e-300)


def b14_weights(mass, omega):
    ratio = (mass / omega) ** 2
    den = 2.0 + ratio
    return np.asarray((ratio / den, 1.0 / den, 1.0 / den), float)


def build_rows(profile_path=DEFAULT_PROFILE, mass=MASS_MEV,
               neutrino_order=512, susceptibility_order=256):
    radii = np.asarray(RADII_KM, float)
    energies = np.asarray(ENERGIES_MEV, float)
    profile = reference.load_profile(profile_path, radii)
    scalar = reference.local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    rows = []
    for ir, radius in enumerate(radii):
        temperature = float(profile["T"][ir])
        lapse = float(profile["lapse"][ir])
        mu_mu = float(profile["mu_mu"][ir])
        mu_numu = float(profile["mu_numu"][ir])
        n_minus, chi_minus, fdeg_minus = local.independent_muon_density_susceptibility(
            temperature, mu_mu, susceptibility_order
        )
        n_plus, chi_plus, fdeg_plus = local.independent_muon_density_susceptibility(
            temperature, -mu_mu, susceptibility_order
        )
        plus_fraction = chi_plus / (chi_minus + chi_plus) if chi_minus + chi_plus > 0 else 0.0
        for ie, omega0 in enumerate(energies):
            omega = float(omega0)
            x = omega / temperature
            p_mu, a_mu = local.direct_neutrino_modes(
                mass, omega, temperature, mu_numu, neutrino_order
            )
            p_tau, a_tau = local.direct_neutrino_modes(
                mass, omega, temperature, 0.0, neutrino_order
            )
            comp = local.independent_b14_b16_compton(
                mass, omega, temperature, chi_minus
            )
            weights = b14_weights(mass, omega)
            c_prod = comp["production_B16_MeV_per_g2"] * weights
            c_abs = comp["absorption_B19_MeV_per_g2"] * weights
            c_red = comp["reduced_B4_from_absorption_MeV_per_g2"] * weights
            nu_red = (1.0 - np.exp(-x)) * (a_mu + a_tau)
            total_prod = p_mu + p_tau + c_prod
            total_abs = a_mu + a_tau + c_abs
            total_red = nu_red + c_red
            scalar_prod = float(scalar["production"][ir, ie])
            scalar_abs = float(scalar["absorption"][ir, ie])
            scalar_red = float(scalar["reduced_absorption"][ir, ie])
            checks = {
                "B10_mu_max_relative_residual": max(
                    rel(p_mu[h], np.exp(-x) * a_mu[h]) for h in range(3)
                ),
                "B10_tau_max_relative_residual": max(
                    rel(p_tau[h], np.exp(-x) * a_tau[h]) for h in range(3)
                ),
                "B4_neutrino_relative_residual": rel(
                    float(np.sum(nu_red)),
                    float(np.expm1(x) * np.sum(p_mu + p_tau))
                ),
                "B19_compton_relative_residual": comp["B19_relative_residual"],
                "B4_compton_relative_residual": comp["B4_relative_residual"],
                "B14_B16_velocity_cancellation_residual": comp["B14_B16_velocity_cancellation_residual"],
                "B14_mode_weight_sum_residual": abs(float(np.sum(weights)) - 1.0),
                "mode_production_sum_relative_residual": rel(float(np.sum(total_prod)), scalar_prod),
                "mode_absorption_sum_relative_residual": rel(float(np.sum(total_abs)), scalar_abs),
                "mode_reduced_absorption_sum_relative_residual": rel(float(np.sum(total_red)), scalar_red),
            }
            row = {
                "radius_km": float(radius), "omega_MeV": omega,
                "T_MeV": temperature, "lapse": lapse,
                "mu_mu_MeV": mu_mu, "mu_numu_MeV": mu_numu,
                "n_mu_minus_MeV3": n_minus, "chi_mu_minus_MeV3": chi_minus,
                "Fdeg_mu_minus": fdeg_minus,
                "n_mu_plus_MeV3": n_plus, "chi_mu_plus_MeV3": chi_plus,
                "Fdeg_mu_plus": fdeg_plus,
                "mu_plus_susceptibility_fraction": plus_fraction,
                "compton_prod_scalar_MeV_per_g2": comp["production_B16_MeV_per_g2"],
                "compton_abs_scalar_MeV_per_g2": comp["absorption_B19_MeV_per_g2"],
                "compton_red_abs_scalar_MeV_per_g2": comp["reduced_B4_from_absorption_MeV_per_g2"],
                "total_prod_scalar_MeV_per_g2": scalar_prod,
                "total_abs_scalar_MeV_per_g2": scalar_abs,
                "total_red_abs_scalar_MeV_per_g2": scalar_red,
                **checks,
            }
            for h, mode in enumerate(MODES):
                row["nu_mu_prod_" + mode + "_MeV_per_g2"] = float(p_mu[h])
                row["nu_mu_abs_" + mode + "_MeV_per_g2"] = float(a_mu[h])
                row["nu_tau_prod_" + mode + "_MeV_per_g2"] = float(p_tau[h])
                row["nu_tau_abs_" + mode + "_MeV_per_g2"] = float(a_tau[h])
                row["compton_w_" + mode] = float(weights[h])
                row["compton_prod_" + mode + "_MeV_per_g2"] = float(c_prod[h])
                row["compton_abs_" + mode + "_MeV_per_g2"] = float(c_abs[h])
                row["compton_red_abs_" + mode + "_MeV_per_g2"] = float(c_red[h])
                row["total_prod_" + mode + "_MeV_per_g2"] = float(total_prod[h])
                row["total_abs_" + mode + "_MeV_per_g2"] = float(total_abs[h])
                row["total_red_abs_" + mode + "_MeV_per_g2"] = float(total_red[h])
            rows.append(row)
    rows.sort(key=lambda z: (z["radius_km"], z["omega_MeV"]))
    residual_names = [k for k in rows[0] if k.endswith("_residual")]
    maxima = {k: max(float(r[k]) for r in rows) for k in residual_names}
    return rows, maxima


def make_svg(rows):
    width, height = 1200, 720
    panel_w, panel_h = 370, 300
    colors = {"L": "#1f4e79", "plus": "#c47a12", "minus": "#2f855a"}
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="600" y="28" text-anchor="middle" font-family="sans-serif" font-size="18" font-weight="bold">10 MeV local production by polarization mode</text>',
        '<text x="600" y="48" text-anchor="middle" font-family="sans-serif" font-size="11">B.6 neutrino modes + B.14 no-recoil Compton split; rates per g_X^2</text>',
    ]
    for idx, radius in enumerate(RADII_KM):
        col, row_index = idx % 3, idx // 3
        x0, y0 = 42 + col * 386, 58 + row_index * 320
        subset = [r for r in rows if r["radius_km"] == radius]
        xs = np.log10([r["omega_MeV"] for r in subset])
        ys = {m: np.log10([max(r["total_prod_" + m + "_MeV_per_g2"], 1e-300) for r in subset]) for m in MODES}
        xmin, xmax = float(xs.min()), float(xs.max())
        ymin = min(float(v.min()) for v in ys.values()) - 0.4
        ymax = max(float(v.max()) for v in ys.values()) + 0.4
        px0, py0, pw, ph = x0 + 55, y0 + 35, 290, 205
        out.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="#bbb"/>' % (x0, y0, panel_w, panel_h))
        out.append('<text x="%d" y="%d" font-family="sans-serif" font-size="13" font-weight="bold">r = %g km</text>' % (x0 + 12, y0 + 21, radius))
        out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#333"/>' % (px0, py0 + ph, px0 + pw, py0 + ph))
        out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#333"/>' % (px0, py0, px0, py0 + ph))
        for tick in range(4):
            xx = px0 + tick * pw / 3
            energy = 10 ** (xmin + tick * (xmax - xmin) / 3)
            out.append('<line x1="%.2f" y1="%d" x2="%.2f" y2="%d" stroke="#e5e5e5"/>' % (xx, py0, xx, py0 + ph))
            out.append('<text x="%.2f" y="%d" text-anchor="middle" font-family="sans-serif" font-size="9">%.0f</text>' % (xx, py0 + ph + 15, energy))
        for tick in range(4):
            yy = py0 + tick * ph / 3
            value = ymax - tick * (ymax - ymin) / 3
            out.append('<line x1="%d" y1="%.2f" x2="%d" y2="%.2f" stroke="#e5e5e5"/>' % (px0, yy, px0 + pw, yy))
            out.append('<text x="%d" y="%.2f" text-anchor="end" font-family="sans-serif" font-size="9">10^%.0f</text>' % (px0 - 6, yy + 3, value))
        for mode in MODES:
            points = []
            for xx, yy in zip(xs, ys[mode]):
                xp = px0 + (xx - xmin) / (xmax - xmin) * pw
                yp = py0 + (ymax - yy) / (ymax - ymin) * ph
                points.append("%.2f,%.2f" % (xp, yp))
            out.append('<polyline fill="none" stroke="%s" stroke-width="2" points="%s"/>' % (colors[mode], " ".join(points)))
        out.append('<text x="%d" y="%d" text-anchor="middle" font-family="sans-serif" font-size="10">omega [MeV] (log)</text>' % (px0 + pw // 2, y0 + panel_h - 12))
        legend_x = x0 + panel_w - 150
        for j, mode in enumerate(MODES):
            lx = legend_x + j * 46
            out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (lx, y0 + 20, lx + 14, y0 + 20, colors[mode]))
            out.append('<text x="%d" y="%d" font-family="sans-serif" font-size="9">%s</text>' % (lx + 18, y0 + 23, mode))
    out.append("</svg>")
    return "\n".join(out) + "\n"


def run(profile_path=DEFAULT_PROFILE, output_dir=DEFAULT_OUTPUT_DIR,
        mass=MASS_MEV, neutrino_order=512, susceptibility_order=256):
    profile_path, output_dir = Path(profile_path), Path(output_dir)
    if float(mass) != MASS_MEV:
        raise ValueError("This package is fixed to m_V=10 MeV")
    rows, maxima = build_rows(profile_path, mass, neutrino_order, susceptibility_order)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "b16_local_rate_polarization_samples_10mev_54pt.csv"
    json_path = output_dir / "b16_local_rate_polarization_samples_10mev_54pt.json"
    svg_path = output_dir / "b16_local_rate_polarization_samples_10mev_54pt.svg"
    fields = list(rows[0])
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    svg_path.write_text(make_svg(rows), encoding="utf-8")
    provenance_path = profile_path.parent / "profile_provenance.json"
    provenance = json.loads(provenance_path.read_text()) if provenance_path.exists() else {}
    payload = {
        "title": "10 MeV local B.16 rate and polarization sample package",
        "date": "2026-11-17",
        "benchmark": {
            "mass_MeV": mass,
            "profile_path": str(profile_path),
            "profile_sha256": sha256(profile_path),
            "profile_git_blob_sha1": git_blob_sha1(profile_path),
            "profile_identity": "reconstructed public-figure SFHo-18.8, t_pb=1 s; not raw Garching data",
            "source_pdfs": provenance.get("sources", {}),
        },
        "configuration": {
            "radii_km": list(RADII_KM), "energies_MeV": list(ENERGIES_MEV),
            "point_count": len(rows), "neutrino_angular_order": int(neutrino_order),
            "muon_susceptibility_quadrature_order": int(susceptibility_order),
            "rate_normalization": "per g_X^2",
            "run_commit_sha": os.environ.get("GITHUB_SHA", "local-unset"),
            "run_context": "github_actions" if os.environ.get("GITHUB_ACTIONS") == "true" else "local",
            "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
        },
        "source_sha256": {
            "producer": sha256(Path(__file__)),
            "local_rate_kernel": sha256(HERE / "audit_b16_local_absorption.py"),
            "scalar_reference": sha256(HERE / "reference.py"),
        },
        "equation_conventions": {
            "neutrino": "B.6/B.10 direct two-body angular integral; L,+,- polarization modes sum to the scalar rate",
            "compton": "B.14--B.17; B.17 uses one negative-muon species; mu-plus is reported separately as a diagnostic",
            "compton_mode_split": "B.14 no-recoil Thomson-limit inverse-cross-section weights: w_L=(m_V^2/omega^2)/(2+m_V^2/omega^2), w_+=w_-=1/(2+m_V^2/omega^2)",
            "detailed_balance": "B.10/B.19 and reduced absorption B.4 checked per mode and after summation",
            "escape": "Local rates only; no P_escape is integrated here. Global escape is handled separately by audit_b16_escape_phase_space.py with the fixed-omega B.2 chord prescription.",
            "relativity": "No full GR ray tracing is claimed; the local lapse is retained in the reconstructed profile and source measure.",
        },
        "closure_maxima": maxima,
        "limitations": [
            "The Compton split is the B.14 no-recoil Thomson-limit approximation, not a recoil-resolved three-mode kernel.",
            "This is a local production/absorption package, not the global B.1/B.2 escape integral.",
            "The SFHo-18.8 profile is reconstructed from public figures, not raw Garching simulation data.",
        ],
        "outputs": {
            "csv": {"path": csv_path.name, "sha256": sha256(csv_path), "bytes": csv_path.stat().st_size},
            "svg": {"path": svg_path.name, "sha256": sha256(svg_path), "bytes": svg_path.stat().st_size},
        },
        "rows": rows,
    }
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    payload["outputs"]["json"] = {"path": json_path.name, "sha256": sha256(json_path), "bytes": json_path.stat().st_size}
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--mass", type=float, default=MASS_MEV)
    parser.add_argument("--neutrino-order", type=int, default=512)
    parser.add_argument("--susceptibility-order", type=int, default=256)
    args = parser.parse_args()
    payload = run(args.profile, args.output_dir, args.mass, args.neutrino_order, args.susceptibility_order)
    print(json.dumps({
        "profile_sha256": payload["benchmark"]["profile_sha256"],
        "profile_git_blob_sha1": payload["benchmark"]["profile_git_blob_sha1"],
        "point_count": payload["configuration"]["point_count"],
        "closure_maxima": payload["closure_maxima"],
        "outputs": payload["outputs"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
