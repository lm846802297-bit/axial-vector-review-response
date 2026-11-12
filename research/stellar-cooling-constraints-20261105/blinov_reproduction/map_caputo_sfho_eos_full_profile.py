#!/usr/bin/env python3
"""Interpolate the full digitized Caputo snapshot onto the official SFHo EOS."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import RegularGridInterpolator

import sfho_eos_tables as eos
from audit_b16_p1iii_eos_nucleon_distribution import NEUTRON_MASS_MEV, PROTON_MASS_MEV
from map_caputo_sfho_eos_profile import EXPECTED_TABLE_SHA256, load_profile

EXTENDED_FIELDS = (
    "mu_n_nonrel_MeV", "mu_p_nonrel_MeV",
    "X_n", "X_p", "X_d", "X_t", "X_h", "X_alpha", "X_A",
)
SPP_FIELDS = {
    "SigmaV_n_tot_MeV": 2,
    "SigmaV_p_tot_MeV": 3,
    "xi_SPP": 4,
    "mstar_n_MeV": 5,
    "mstar_p_MeV": 6,
}
CLUSTER_FIELDS = ("X_d", "X_t", "X_h", "X_alpha", "X_A")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def make_interpolators(ext, spp):
    ext_axes = (
        np.log10(ext.temperature),
        ext.ye,
        np.log10(ext.nb[:eos.NB_PHYSICAL]),
    )
    spp_axes = (
        np.log10(spp.temperature),
        spp.ye,
        np.log10(spp.nb[:eos.NB_PHYSICAL]),
    )
    ext_interpolators = {
        name: RegularGridInterpolator(
            ext_axes,
            ext.entry(name)[:, :, :eos.NB_PHYSICAL],
            method="linear",
            bounds_error=True,
        )
        for name in EXTENDED_FIELDS
    }
    spp_interpolators = {
        name: RegularGridInterpolator(
            spp_axes,
            spp.data[:, :, :eos.NB_PHYSICAL, index],
            method="linear",
            bounds_error=True,
        )
        for name, index in SPP_FIELDS.items()
    }
    return ext_axes, spp_axes, ext_interpolators, spp_interpolators


def axis_domain(axis: np.ndarray, values: np.ndarray) -> dict[str, float | bool]:
    axis = np.asarray(axis, dtype=float)
    values = np.asarray(values, dtype=float)
    low_margin = float(np.min(values) - axis[0])
    high_margin = float(axis[-1] - np.max(values))
    return {
        "table_min": float(axis[0]),
        "table_max": float(axis[-1]),
        "profile_min": float(np.min(values)),
        "profile_max": float(np.max(values)),
        "lower_margin": low_margin,
        "upper_margin": high_margin,
        "within_bounds": bool(low_margin >= -1e-12 and high_margin >= -1e-12),
    }


def bracket(axis: np.ndarray, value: float) -> tuple[int, int, float]:
    """Return lower/upper grid indices and the linear interpolation weight."""
    axis = np.asarray(axis, dtype=float)
    if value < axis[0] - 1e-12 or value > axis[-1] + 1e-12:
        raise ValueError(f"coordinate {value} is outside [{axis[0]}, {axis[-1]}]")
    lower = int(np.searchsorted(axis, value, side="right") - 1)
    lower = min(max(lower, 0), len(axis) - 2)
    upper = lower + 1
    weight = float((value - axis[lower]) / (axis[upper] - axis[lower]))
    return lower, upper, weight


def map_rows(profile_rows, ext, spp):
    ext_axes, spp_axes, ext_i, spp_i = make_interpolators(ext, spp)
    radii = np.asarray([row["r_km"] for row in profile_rows], dtype=float)
    temperatures = np.asarray([row["T_MeV"] for row in profile_rows], dtype=float)
    densities = np.asarray([row["nB_fm3"] for row in profile_rows], dtype=float)
    yp_tot = np.asarray([row["Yp_tot"] for row in profile_rows], dtype=float)
    coordinates = (np.log10(temperatures), yp_tot, np.log10(densities))

    domains = {}
    for table_name, axes in (("extended_eos", ext_axes), ("single_particle", spp_axes)):
        domains[table_name] = {
            axis_name: axis_domain(axis, coordinate)
            for axis_name, axis, coordinate in zip(
                ("log10_T_MeV", "Yp_tot", "log10_nB_fm3"), axes, coordinates
            )
        }
        if not all(item["within_bounds"] for item in domains[table_name].values()):
            raise ValueError(f"profile lies outside {table_name} interpolation bounds")

    points = np.column_stack(coordinates)
    output = []
    for index, row in enumerate(profile_rows):
        ext_values = {
            name: float(interpolator(points[index:index + 1])[0])
            for name, interpolator in ext_i.items()
        }
        spp_values = {
            name: float(interpolator(points[index:index + 1])[0])
            for name, interpolator in spp_i.items()
        }
        cluster_sum = sum(ext_values[name] for name in CLUSTER_FIELDS)
        xcluster_complement = 1.0 - ext_values["X_n"] - ext_values["X_p"]
        nn = row["Yn_free"] * row["nB_fm3"]
        np_free = row["Yp_free"] * row["nB_fm3"]
        ncluster = row["Xcluster"] * row["nB_fm3"]
        xi_inferred = 1.0 - (
            row["nB_fm3"] - nn - np_free
        ) / eos.NUCLEON_BAG_DENSITY_FM3

        U_n = spp_values["mstar_n_MeV"] - NEUTRON_MASS_MEV + spp_values["SigmaV_n_tot_MeV"]
        U_p = spp_values["mstar_p_MeV"] - PROTON_MASS_MEV + spp_values["SigmaV_p_tot_MeV"]

        t0, t1, tw = bracket(ext_axes[0], coordinates[0][index])
        y0, y1, yw = bracket(ext_axes[1], coordinates[1][index])
        n0, n1, nw = bracket(ext_axes[2], coordinates[2][index])
        st0, st1, stw = bracket(spp_axes[0], coordinates[0][index])
        sy0, sy1, syw = bracket(spp_axes[1], coordinates[1][index])
        sn0, sn1, snw = bracket(spp_axes[2], coordinates[2][index])

        mapped = dict(row)
        mapped.update({
            "Yp_tot_EOS_coordinate": row["Yp_tot"],
            "ext_T_i0": t0, "ext_T_i1": t1, "ext_T_weight": tw,
            "ext_Yp_i0": y0, "ext_Yp_i1": y1, "ext_Yp_weight": yw,
            "ext_nB_i0": n0, "ext_nB_i1": n1, "ext_nB_weight": nw,
            "spp_T_i0": st0, "spp_T_i1": st1, "spp_T_weight": stw,
            "spp_Yp_i0": sy0, "spp_Yp_i1": sy1, "spp_Yp_weight": syw,
            "spp_nB_i0": sn0, "spp_nB_i1": sn1, "spp_nB_weight": snw,
            **ext_values,
            **spp_values,
            "Xcluster_EOS": xcluster_complement,
            "Xcluster_components_sum_EOS": cluster_sum,
            "Xcluster_component_closure_residual": cluster_sum - xcluster_complement,
            "Ycluster_charge_EOS": row["Yp_tot"] - ext_values["X_p"],
            "Xn_EOS_minus_Caputo": ext_values["X_n"] - row["Yn_free"],
            "Xp_EOS_minus_Caputo": ext_values["X_p"] - row["Yp_free"],
            "Xcluster_EOS_minus_Caputo": xcluster_complement - row["Xcluster"],
            "Ycluster_charge_EOS_minus_Caputo": (
                row["Yp_tot"] - ext_values["X_p"] - row["Ycluster_charge"]
            ),
            "n_n_free_fm3": nn,
            "n_p_free_fm3": np_free,
            "n_cluster_baryon_fm3": ncluster,
            "n_n_EOS_fm3": ext_values["X_n"] * row["nB_fm3"],
            "n_p_EOS_fm3": ext_values["X_p"] * row["nB_fm3"],
            "xi_inferred_from_free_plus_cluster": xi_inferred,
            "xi_SPP_minus_inferred": spp_values["xi_SPP"] - xi_inferred,
            "U_n_MeV": U_n,
            "U_p_MeV": U_p,
        })
        output.append(mapped)
    return output, domains


def summarize(rows, domains, profile_path: Path, tables_dir: Path) -> dict:
    def values(key):
        return np.asarray([float(row[key]) for row in rows], dtype=float)

    def rms_abs(key):
        x = values(key)
        return float(np.sqrt(np.mean(x * x)))

    def max_abs(key):
        return float(np.max(np.abs(values(key))))

    radii = values("r_km")
    dr = np.diff(radii)
    table_sha = {name: sha256(tables_dir / name) for name in EXPECTED_TABLE_SHA256}
    if table_sha != EXPECTED_TABLE_SHA256:
        raise ValueError("SFHo table SHA-256 does not match the pinned v1.03 inputs")

    cluster_min = min(float(np.min(values(name))) for name in CLUSTER_FIELDS)
    composition_max = max(
        max_abs("Xn_EOS_minus_Caputo"),
        max_abs("Xp_EOS_minus_Caputo"),
        max_abs("Xcluster_EOS_minus_Caputo"),
        max_abs("Ycluster_charge_EOS_minus_Caputo"),
    )
    summary = {
        "scope": (
            "full 0.05-km digitized Caputo SFHo-18.8 t_pb=1 s published-figure "
            "snapshot; not raw time-dependent Garching simulation data"
        ),
        "profile_csv": profile_path.name,
        "profile_csv_sha256": sha256(profile_path),
        "number_of_profile_points": len(rows),
        "radial_grid_km": {
            "min": float(radii[0]),
            "max": float(radii[-1]),
            "median_step": float(np.median(dr)),
            "min_step": float(np.min(dr)),
            "max_step": float(np.max(dr)),
            "max_abs_step_deviation_from_0p05": float(np.max(np.abs(dr - 0.05))),
        },
        "source": {
            "paper": "Caputo, Raffelt, Vitagliano, arXiv:2109.03244v3",
            "archive_sha256": "2e4a1280460bce9a5f7596d3dfd1d3e0f4752f2e1706e85d3a2c20b5f9dbbd8e",
            "temperature": "Fig. 1 upper panel native vector path",
            "baryon_density": "Fig. 1 lower panel nB native vector path",
            "composition": "Fig. 4 upper panel Yn, Yp, Ye+Ymu native vector paths",
            "n0_caputo_fm3": 0.181,
            "eos_coordinate": "Yp_tot=Ye+Ymu, not free-proton Yp",
        },
        "eos_tables_sha256": table_sha,
        "interpolation": {
            "method": "trilinear RegularGridInterpolator",
            "axes": ["log10(T_MeV)", "Yp_tot", "log10(nB_fm3)"],
            "physical_density_rows": eos.NB_PHYSICAL,
            "bounds_error": True,
            "extrapolation": False,
            "domain_margins": domains,
        },
        "composition_closure": {
            "Xn_rms_abs": rms_abs("Xn_EOS_minus_Caputo"),
            "Xn_max_abs": max_abs("Xn_EOS_minus_Caputo"),
            "Xp_rms_abs": rms_abs("Xp_EOS_minus_Caputo"),
            "Xp_max_abs": max_abs("Xp_EOS_minus_Caputo"),
            "Xcluster_rms_abs": rms_abs("Xcluster_EOS_minus_Caputo"),
            "Xcluster_max_abs": max_abs("Xcluster_EOS_minus_Caputo"),
            "cluster_charge_rms_abs": rms_abs("Ycluster_charge_EOS_minus_Caputo"),
            "cluster_charge_max_abs": max_abs("Ycluster_charge_EOS_minus_Caputo"),
            "EOS_cluster_components_max_abs_residual": max_abs("Xcluster_component_closure_residual"),
            "minimum_individual_cluster_fraction": cluster_min,
        },
        "filling_factor_closure": {
            "xi_rms_abs": rms_abs("xi_SPP_minus_inferred"),
            "xi_max_abs": max_abs("xi_SPP_minus_inferred"),
            "xi_SPP_range": [float(np.min(values("xi_SPP"))), float(np.max(values("xi_SPP")))],
        },
        "free_nucleon_and_cluster_densities_fm3": {
            "neutron_range": [float(np.min(values("n_n_free_fm3"))), float(np.max(values("n_n_free_fm3")))],
            "proton_range": [float(np.min(values("n_p_free_fm3"))), float(np.max(values("n_p_free_fm3")))],
            "cluster_baryon_range": [float(np.min(values("n_cluster_baryon_fm3"))), float(np.max(values("n_cluster_baryon_fm3")))],
        },
        "acceptance": {
            "all_profile_points_inside_both_table_domains": all(
                item["within_bounds"]
                for table in domains.values()
                for item in table.values()
            ),
            "max_composition_abs_residual_below_5e-3": composition_max < 5e-3,
            "max_xi_abs_residual_below_5e-3": max_abs("xi_SPP_minus_inferred") < 5e-3,
            "EOS_cluster_component_closure_below_1e-8": max_abs("Xcluster_component_closure_residual") < 1e-8,
            "all_cluster_components_nonnegative_with_1e-8_tolerance": cluster_min >= -1e-8,
            "radial_grid_is_0p05_km": float(np.max(np.abs(dr - 0.05))) < 1e-8,
        },
        "handoff_fields": [
            "mstar_n_MeV", "mstar_p_MeV",
            "SigmaV_n_tot_MeV", "SigmaV_p_tot_MeV",
            "mu_n_nonrel_MeV", "mu_p_nonrel_MeV",
            "U_n_MeV", "U_p_MeV", "xi_SPP",
            "X_n", "X_p", "X_d", "X_t", "X_h", "X_alpha", "X_A",
        ],
        "interpretation": [
            "The EOS is evaluated at total proton/charge fraction Ye+Ymu; free Yp is retained only as a composition closure target.",
            "Free neutron, free proton, and cluster baryon densities remain separate; n_n+n_p is not set equal to nB.",
            "This is a radial interpolation of published figure paths at t_pb=1 s, not a raw Garching time-history profile.",
            "No Fermi integral, dynamic response, opacity, luminosity, transport, or cooling curve is calculated or modified in this C1 stage.",
        ],
    }
    return summary


def write_report(summary: dict, path: Path) -> None:
    c = summary["composition_closure"]
    x = summary["filling_factor_closure"]
    grid = summary["radial_grid_km"]
    bounds = summary["interpolation"]["domain_margins"]
    passed = all(summary["acceptance"].values())
    lines = [
        "# P1-IIIe-C: full radial Caputo-to-SFHo EOS mapping",
        "",
        "Date: 2026-11-11  ",
        "PR: #57  ",
        "Branch: research/moving-muon-thermal-rates-20261107",
        "",
        "## Scope",
        "",
        f"This report maps {summary['number_of_profile_points']} points from the 0.05-km Caputo SFHo-18.8 published-figure snapshot at t_pb=1 s onto the official SFHo/FRDM v1.03 tables. The radial interval is {grid['min']:.3f}--{grid['max']:.3f} km. It is not a raw time-dependent Garching simulation profile.",
        "",
        "The EOS coordinate is Yp_tot = Ye + Ymu; the free-proton abundance Yp is not used as the EOS coordinate.",
        "",
        "## Interpolation and boundary checks",
        "",
        "Trilinear interpolation is performed in (log10 T, Yp_tot, log10 nB) with bounds_error=True, using only the 308 physical density rows. No extrapolation is permitted.",
        "",
        "| Table axis | Table range | Profile range | Lower margin | Upper margin |",
        "|---|---:|---:|---:|---:|",
    ]
    for table, axes in bounds.items():
        for axis, item in axes.items():
            lines.append(
                f"| {table}: {axis} | [{item['table_min']:.8g}, {item['table_max']:.8g}] | "
                f"[{item['profile_min']:.8g}, {item['profile_max']:.8g}] | "
                f"{item['lower_margin']:.8g} | {item['upper_margin']:.8g} |"
            )
    lines += [
        "",
        "## Composition closure",
        "",
        "| Quantity | RMS absolute residual | Maximum absolute residual |",
        "|---|---:|---:|",
        f"| Xn_EOS - Yn_Caputo | {c['Xn_rms_abs']:.6g} | {c['Xn_max_abs']:.6g} |",
        f"| Xp_EOS - Yp_Caputo | {c['Xp_rms_abs']:.6g} | {c['Xp_max_abs']:.6g} |",
        f"| Xcluster_EOS - Xcluster_Caputo | {c['Xcluster_rms_abs']:.6g} | {c['Xcluster_max_abs']:.6g} |",
        f"| cluster charge | {c['cluster_charge_rms_abs']:.6g} | {c['cluster_charge_max_abs']:.6g} |",
        "",
        "The SPP filling factor is compared with the value inferred independently from the free-nucleon and total baryon densities:",
        "",
        f"- RMS absolute xi residual: {x['xi_rms_abs']:.6g}",
        f"- Maximum absolute xi residual: {x['xi_max_abs']:.6g}",
        f"- Maximum EOS cluster-component closure residual: {c['EOS_cluster_components_max_abs_residual']:.6g}",
        "",
        "## C2 handoff",
        "",
        "The radial table contains m*_n, m*_p, SigmaV_n, SigmaV_p, mu_n^nonrel, mu_p^nonrel, xi, and the individual cluster fractions. It also records the Hempel scalar potentials U_N = m*_N - m_N + SigmaV_N. No phase-space occupation or degeneracy integral is evaluated in this C1 mapping.",
        "",
        "Free neutron, free proton, and cluster baryon densities are stored separately. The identity n_n + n_p = nB is never imposed.",
        "",
        "## Acceptance",
        "",
        f"Overall C1 acceptance: **{'PASS' if passed else 'FAIL'}**.",
        "",
        "The machine-readable acceptance criteria and full provenance are in the accompanying JSON. No dynamic response, B.2 opacity, pure-vector Fig. 7 result, axial cooling curve, manuscript, or referee response is modified.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--tables-dir", type=Path, default=eos.default_tables_dir())
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()
    if args.tables_dir is None:
        raise SystemExit("Set SFHO_TABLES_DIR or pass --tables-dir")

    for name, expected in EXPECTED_TABLE_SHA256.items():
        actual = sha256(args.tables_dir / name)
        if actual != expected:
            raise ValueError(f"{name} SHA-256 mismatch: {actual}")

    profile_rows = load_profile(args.profile)
    ext = eos.ExtendedEOS.load(args.tables_dir / "sfho_frdm_eos_v1.03.bin")
    spp = eos.SPPTable.load(args.tables_dir / "sfho_frdm_spp_v1.03.tab")
    rows, domains = map_rows(profile_rows, ext, spp)
    summary = summarize(rows, domains, args.profile, args.tables_dir)

    args.outdir.mkdir(parents=True, exist_ok=True)
    csv_path = args.outdir / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
    json_path = args.outdir / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.json"
    report_path = args.outdir / "B16_P1IIIE_C_FULL_RADIAL_SFHO_EOS_MAPPING_2026-11-11.md"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows({
            key: (f"{value:.12g}" if isinstance(value, (int, float, np.floating)) else value)
            for key, value in row.items()
        } for row in rows)
    summary["mapped_csv"] = csv_path.name
    summary["mapped_csv_sha256"] = sha256(csv_path)
    json_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    write_report(summary, report_path)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
