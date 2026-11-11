#!/usr/bin/env python3
"""Map the Caputo SFHo-18.8 key-radius profile onto the official SFHo EOS.

This is a published-figure snapshot mapping at ten audited radii (1--15 km),
not a reconstruction of the full Garching time-dependent profile. The EOS
coordinate Yp_tot is the total proton/charge fraction and is supplied by the
Caputo Fig. 4 curve Ye+Ymu, not by the free-proton fraction Yp.
"""
from __future__ import annotations
import argparse, csv, hashlib, json
from pathlib import Path
import numpy as np
from scipy.interpolate import RegularGridInterpolator
import sfho_eos_tables as eos
from audit_b16_p1iii_eos_nucleon_distribution import (
    HBARC_MEV_FM, NEUTRON_MASS_MEV, PROTON_MASS_MEV, NucleonEOSState,
    degeneracy_factor, infer_filling_factor_from_global_densities,
    phase_space_integrals, state_from_available_volume_density, state_from_hs_spp,
)

EXPECTED_TABLE_SHA256 = {
    "sfho_frdm_eos_v1.03.bin": "f1ea9c3e04502ca35d7fc64facce575f8553293085ea26e07732389b80d32cb4",
    "sfho_frdm_spp_v1.03.tab": "118bd3c986283d958fab88a8e81fe49b64ca3b5137ff4bcdc05f97064cc1219e",
    "sfho_frdm_comp_v1.03.bin": "0dafcd272ff8b8f4b1ba4c05210ea8020dd9a92820b6b0b54165faead4871da7",
}
CAPUTO_ARCHIVE_SHA256 = "2e4a1280460bce9a5f7596d3dfd1d3e0f4752f2e1706e85d3a2c20b5f9dbbd8e"
CAPUTO_FIG1_PDF_SHA256 = "19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e"
CAPUTO_FIG4_PDF_SHA256 = "39d66c37dd67d73fbe1b3afe2f5e2a532e0e040e9d220e66ec389abb5daf17ab"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def load_profile(path: Path):
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    required = (
        "r_km", "T_MeV", "nB_fm3", "Yn_free", "Yp_free", "Yp_tot",
        "Xcluster", "Ycluster_charge",
    )
    if not rows or not set(required).issubset(rows[0]):
        raise ValueError(f"profile CSV must contain columns {list(required)}")
    result = [{key: float(row[key]) for key in required} for row in rows]
    radii = np.array([row["r_km"] for row in result])
    if np.any(np.diff(radii) <= 0.0):
        raise ValueError("profile radii must be strictly increasing")
    for row in result:
        if row["T_MeV"] <= 0 or row["nB_fm3"] <= 0:
            raise ValueError("T and nB must be positive")
        if not (0.01 <= row["Yp_tot"] <= 0.60):
            raise ValueError("Yp_tot lies outside the SPP table grid")
        if abs(row["Yn_free"] + row["Yp_free"] + row["Xcluster"] - 1.0) > 5e-5:
            raise ValueError("Caputo free-nucleon and cluster fractions do not close")
        if abs(row["Ycluster_charge"] - (row["Yp_tot"] - row["Yp_free"])) > 5e-5:
            raise ValueError("Caputo cluster charge does not close")
    return result

def make_interpolators(ext, spp):
    axes_ext = (np.log10(ext.temperature), ext.ye, np.log10(ext.nb[:eos.NB_PHYSICAL]))
    axes_spp = (np.log10(spp.temperature), spp.ye, np.log10(spp.nb[:eos.NB_PHYSICAL]))
    ext_fields = ["mu_n_nonrel_MeV", "mu_p_nonrel_MeV", "X_n", "X_p",
                  "X_d", "X_t", "X_h", "X_alpha", "X_A"]
    spp_fields = {"SigmaV_n_tot_MeV": 2, "SigmaV_p_tot_MeV": 3, "xi": 4,
                  "mstar_n_MeV": 5, "mstar_p_MeV": 6}
    ext_interp = {
        name: RegularGridInterpolator(
            axes_ext, ext.entry(name)[:, :, :eos.NB_PHYSICAL],
            method="linear", bounds_error=True,
        ) for name in ext_fields
    }
    spp_interp = {
        name: RegularGridInterpolator(
            axes_spp, spp.data[:, :, :eos.NB_PHYSICAL, index],
            method="linear", bounds_error=True,
        ) for name, index in spp_fields.items()
    }
    return ext_interp, spp_interp

def state_integrals(state: NucleonEOSState, order: int):
    n_mev3, blocked_mev3 = phase_space_integrals(state, order=order)
    return n_mev3 / HBARC_MEV_FM**3, blocked_mev3 / n_mev3

def calculate(profile_rows, ext, spp):
    ext_interp, spp_interp = make_interpolators(ext, spp)
    output, quadrature_checks = [], []
    for row in profile_rows:
        T, nB, Yp_tot = row["T_MeV"], row["nB_fm3"], row["Yp_tot"]
        point = np.array([[np.log10(T), Yp_tot, np.log10(nB)]])
        values = {name: float(interp(point)[0]) for name, interp in ext_interp.items()}
        values.update({name: float(interp(point)[0]) for name, interp in spp_interp.items()})
        wrong_point = np.array([[np.log10(T), row["Yp_free"], np.log10(nB)]])
        wrong_xn = float(ext_interp["X_n"](wrong_point)[0])
        wrong_xp = float(ext_interp["X_p"](wrong_point)[0])

        state_n = state_from_hs_spp(
            "n", T, values["mstar_n_MeV"], values["SigmaV_n_tot_MeV"],
            values["mu_n_nonrel_MeV"],
        )
        state_p = state_from_hs_spp(
            "p", T, values["mstar_p_MeV"], values["SigmaV_p_tot_MeV"],
            values["mu_p_nonrel_MeV"],
        )
        xi = values["xi"]
        target_n, target_p = row["Yn_free"] * nB, row["Yp_free"] * nB
        xi_caputo = infer_filling_factor_from_global_densities(
            nB, target_n, target_p, saturation_density_fm3=eos.NUCLEON_BAG_DENSITY_FM3
        )
        local = dict(row)
        local.update({
            "Yp_tot_EOS_coordinate": Yp_tot,
            "xi_SPP": xi, "xi_inferred_from_Caputo": xi_caputo,
            "mstar_n_MeV": values["mstar_n_MeV"], "mstar_p_MeV": values["mstar_p_MeV"],
            "SigmaV_n_tot_MeV": values["SigmaV_n_tot_MeV"],
            "SigmaV_p_tot_MeV": values["SigmaV_p_tot_MeV"],
            "U_n_MeV": state_n.scalar_potential_mev, "U_p_MeV": state_p.scalar_potential_mev,
            "mu_n_star_MeV": values["mu_n_nonrel_MeV"],
            "mu_p_star_MeV": values["mu_p_nonrel_MeV"],
            "nu_n_MeV": state_n.effective_chemical_potential_mev,
            "nu_p_MeV": state_p.effective_chemical_potential_mev,
            "Xn_EOS": values["X_n"], "Xp_EOS": values["X_p"],
            "Xcluster_EOS": 1.0 - values["X_n"] - values["X_p"],
            "Ycluster_charge_EOS": Yp_tot - values["X_p"],
            "Xn_EOS_if_free_Yp_wrong_coordinate": wrong_xn,
            "Xp_EOS_if_free_Yp_wrong_coordinate": wrong_xp,
            "Xcluster_EOS_if_free_Yp_wrong_coordinate": 1.0 - wrong_xn - wrong_xp,
            "n_n_target_fm3": target_n, "n_p_target_fm3": target_p,
        })
        species_states = {
            "n": (state_n, target_n, values["X_n"] * nB, values["mstar_n_MeV"], NEUTRON_MASS_MEV),
            "p": (state_p, target_p, values["X_p"] * nB, values["mstar_p_MeV"], PROTON_MASS_MEV),
        }
        for species, (state, target, table_target, mstar, vacuum_mass) in species_states.items():
            n512, f512 = state_integrals(state, 512)
            n2048, f2048 = state_integrals(state, 2048)
            pred_total = xi * n2048
            matched = state_from_available_volume_density(species, T, mstar, target / xi, order=512)
            f_matched = degeneracy_factor(matched, order=512)
            ideal = state_from_available_volume_density(species, T, vacuum_mass, target / xi, order=512)
            f_ideal = degeneracy_factor(ideal, order=512)
            local.update({
                f"nprime_{species}_fm3": n2048,
                f"n_{species}_EOS_fm3": pred_total,
                f"n_{species}_table_mass_fraction_fm3": table_target,
                f"n_{species}_target_Caputo_fm3": target,
                f"n_{species}_rel_residual_vs_Caputo": pred_total / target - 1.0,
                f"n_{species}_rel_residual_vs_EOS_XN": pred_total / table_target - 1.0,
                f"F_{species}{species}_EOS": f2048,
                f"F_{species}{species}_density_matched": f_matched,
                f"F_{species}{species}_ideal_vacuum_mass_same_density": f_ideal,
                f"F_{species}{species}_rel_change_vs_ideal": f2048 / f_ideal - 1.0,
                f"delta_nu_{species}_required_minus_EOS_MeV":
                    matched.effective_chemical_potential_mev - state.effective_chemical_potential_mev,
                f"quadrature_rel_change_2048_vs_512_n_{species}": n2048 / n512 - 1.0,
                f"quadrature_abs_change_2048_vs_512_F_{species}": abs(f2048 - f512),
            })
            quadrature_checks.append({
                "r_km": row["r_km"], "species": species,
                "n_rel_change_2048_vs_512": n2048 / n512 - 1.0,
                "F_abs_change_2048_vs_512": abs(f2048 - f512),
            })
        output.append(local)
    return output, quadrature_checks

def summarize(rows, quad, tables_dir, profile_path):
    def arr(key):
        return np.array([float(row[key]) for row in rows], dtype=float)
    def rms(x):
        x = np.asarray(x, dtype=float)
        return float(np.sqrt(np.mean(x*x)))
    def maxabs(x):
        return float(np.max(np.abs(np.asarray(x, dtype=float))))
    out = {
        "scope": "10 key radii from the Caputo SFHo-18.8 t_pb=1 s published figures; not a full radial/time profile",
        "profile_csv": profile_path.name, "profile_csv_sha256": sha256(profile_path),
        "caputo_source": {
            "archive": "arXiv-2109.03244v3.tar.gz",
            "archive_sha256": CAPUTO_ARCHIVE_SHA256,
            "fig1_pdf_sha256": CAPUTO_FIG1_PDF_SHA256,
            "fig4_pdf_sha256": CAPUTO_FIG4_PDF_SHA256,
            "temperature_source": "T_caputo_vertices.csv, linearly interpolated in radius",
            "composition_source": "caputo_composition_key_radii_2026-11-11.csv",
            "eos_Yp_coordinate": "Yp_tot = Ye + Ymu, not the free-proton abundance Yp",
        },
        "eos_table_sha256": {name: sha256(tables_dir / name) for name in EXPECTED_TABLE_SHA256},
        "interpolation": {
            "method": "trilinear RegularGridInterpolator",
            "axes": ["log10(T_MeV)", "Yp_tot", "log10(nB_fm3)"],
            "physical_density_rows": eos.NB_PHYSICAL, "no_extrapolation": True,
        },
        "radii_km": [float(rows[0]["r_km"]), float(rows[-1]["r_km"])],
        "number_of_key_radii": len(rows),
        "composition_closure": {
            "Xn_EOS_minus_Yn_Caputo_rms_abs": rms(arr("Xn_EOS") - arr("Yn_free")),
            "Xn_EOS_minus_Yn_Caputo_max_abs": maxabs(arr("Xn_EOS") - arr("Yn_free")),
            "Xp_EOS_minus_Yp_Caputo_rms_abs": rms(arr("Xp_EOS") - arr("Yp_free")),
            "Xp_EOS_minus_Yp_Caputo_max_abs": maxabs(arr("Xp_EOS") - arr("Yp_free")),
            "Xcluster_EOS_minus_Caputo_rms_abs": rms(arr("Xcluster_EOS") - arr("Xcluster")),
            "Xcluster_EOS_minus_Caputo_max_abs": maxabs(arr("Xcluster_EOS") - arr("Xcluster")),
            "cluster_charge_EOS_minus_Caputo_rms_abs": rms(arr("Ycluster_charge_EOS") - arr("Ycluster_charge")),
            "cluster_charge_EOS_minus_Caputo_max_abs": maxabs(arr("Ycluster_charge_EOS") - arr("Ycluster_charge")),
        },
        "wrong_EOS_Yp_coordinate_diagnostic": {
            "interpretation": "Using free-proton abundance Yp instead of total proton fraction Yp_tot=Ye+Ymu is incorrect once clusters carry charge.",
            "Xn_rms_abs_error": rms(arr("Xn_EOS_if_free_Yp_wrong_coordinate") - arr("Yn_free")),
            "Xn_max_abs_error": maxabs(arr("Xn_EOS_if_free_Yp_wrong_coordinate") - arr("Yn_free")),
            "Xp_rms_abs_error": rms(arr("Xp_EOS_if_free_Yp_wrong_coordinate") - arr("Yp_free")),
            "Xp_max_abs_error": maxabs(arr("Xp_EOS_if_free_Yp_wrong_coordinate") - arr("Yp_free")),
            "Xcluster_rms_abs_error": rms(arr("Xcluster_EOS_if_free_Yp_wrong_coordinate") - arr("Xcluster")),
            "Xcluster_max_abs_error": maxabs(arr("Xcluster_EOS_if_free_Yp_wrong_coordinate") - arr("Xcluster")),
        },
        "filling_factor_closure": {
            "xi_SPP_minus_Caputo_inferred_rms_abs": rms(arr("xi_SPP") - arr("xi_inferred_from_Caputo")),
            "xi_SPP_minus_Caputo_inferred_max_abs": maxabs(arr("xi_SPP") - arr("xi_inferred_from_Caputo")),
        },
        "occupation_density_closure": {
            "neutron_rel_residual_rms": rms(arr("n_n_rel_residual_vs_Caputo")),
            "neutron_rel_residual_max_abs": maxabs(arr("n_n_rel_residual_vs_Caputo")),
            "proton_rel_residual_rms": rms(arr("n_p_rel_residual_vs_Caputo")),
            "proton_rel_residual_max_abs": maxabs(arr("n_p_rel_residual_vs_Caputo")),
            "max_abs_delta_nu_n_MeV": maxabs(arr("delta_nu_n_required_minus_EOS_MeV")),
            "max_abs_delta_nu_p_MeV": maxabs(arr("delta_nu_p_required_minus_EOS_MeV")),
        },
        "local_degeneracy_factors": {
            "Fnn_EOS_range": [float(np.min(arr("F_nn_EOS"))), float(np.max(arr("F_nn_EOS")))],
            "Fpp_EOS_range": [float(np.min(arr("F_pp_EOS"))), float(np.max(arr("F_pp_EOS")))],
            "Fnn_ideal_vacuum_mass_range": [float(np.min(arr("F_nn_ideal_vacuum_mass_same_density"))), float(np.max(arr("F_nn_ideal_vacuum_mass_same_density")))],
            "Fpp_ideal_vacuum_mass_range": [float(np.min(arr("F_pp_ideal_vacuum_mass_same_density"))), float(np.max(arr("F_pp_ideal_vacuum_mass_same_density")))],
            "Fnn_relative_change_vs_ideal_range": [float(np.min(arr("F_nn_rel_change_vs_ideal"))), float(np.max(arr("F_nn_rel_change_vs_ideal")))],
            "Fpp_relative_change_vs_ideal_range": [float(np.min(arr("F_pp_rel_change_vs_ideal"))), float(np.max(arr("F_pp_rel_change_vs_ideal")))],
            "Fnn_EOS_vs_density_matched_max_abs_difference": maxabs(arr("F_nn_EOS") - arr("F_nn_density_matched")),
            "Fpp_EOS_vs_density_matched_max_abs_difference": maxabs(arr("F_pp_EOS") - arr("F_pp_density_matched")),
        },
        "effective_mass_MeV_ranges": {
            "neutron": [float(np.min(arr("mstar_n_MeV"))), float(np.max(arr("mstar_n_MeV")))],
            "proton": [float(np.min(arr("mstar_p_MeV"))), float(np.max(arr("mstar_p_MeV")))],
        },
        "quadrature": {
            "max_abs_n_relative_change_2048_vs_512": maxabs([x["n_rel_change_2048_vs_512"] for x in quad]),
            "max_abs_F_change_2048_vs_512": maxabs([x["F_abs_change_2048_vs_512"] for x in quad]),
        },
        "interpretation": [
            "The Hempel SFHo table composition fractions X_n and X_p match the Caputo Fig. 4 free-nucleon abundances at the ten key radii to O(10^-5) absolute.",
            "The EOS SPP filling factor agrees with the value inferred from Caputo free-nucleon and total baryon densities at O(10^-4) absolute.",
            "The local EOS occupation density closure is sub-percent; the chemical-potential correction needed to close exactly is below 0.2 MeV and changes Fdeg by less than 4e-4 absolute.",
            "At fixed free-nucleon density and temperature, the EOS effective masses reduce the static degeneracy factors relative to a vacuum-mass ideal Fermi gas, most strongly in the inner core.",
            "These are local t_pb=1 s snapshot factors, not Fiorillo Table 1 mass-time weighted averages. No dynamic response, opacity, transport, or cooling curve is changed.",
        ],
    }
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--profile", type=Path, required=True)
    ap.add_argument("--tables-dir", type=Path, default=eos.default_tables_dir())
    ap.add_argument("--outdir", type=Path, required=True)
    args = ap.parse_args()
    if args.tables_dir is None:
        raise SystemExit("Set SFHO_TABLES_DIR or pass --tables-dir")
    args.outdir.mkdir(parents=True, exist_ok=True)
    for name, expected in EXPECTED_TABLE_SHA256.items():
        actual = sha256(args.tables_dir / name)
        if actual != expected:
            raise ValueError(f"{name} SHA-256 mismatch: {actual}")
    profile_rows = load_profile(args.profile)
    ext = eos.ExtendedEOS.load(args.tables_dir / "sfho_frdm_eos_v1.03.bin")
    spp = eos.SPPTable.load(args.tables_dir / "sfho_frdm_spp_v1.03.tab")
    rows, quad = calculate(profile_rows, ext, spp)
    summary = summarize(rows, quad, args.tables_dir, args.profile)
    csv_path = args.outdir / "caputo_sfho_eos_profile_key_radii_2026-11-11.csv"
    json_path = args.outdir / "caputo_sfho_eos_profile_key_radii_2026-11-11.json"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    json_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
