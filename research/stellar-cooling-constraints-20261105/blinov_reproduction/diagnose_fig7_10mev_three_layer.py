"""Three-layer source/opacity/transport decomposition of Blinov Fig. 7 at 10 MeV."""
from __future__ import annotations
import argparse, hashlib, json, os
from pathlib import Path
import numpy as np

try:
    from .reference import DEFAULT_PROFILE, MEV2_TO_ERG_S, KM_TO_MEV_INV, energy_weights, load_profile, local_rates, radial_rule, scalar_optical_depths
except ImportError:
    from reference import DEFAULT_PROFILE, MEV2_TO_ERG_S, KM_TO_MEV_INV, energy_weights, load_profile, local_rates, radial_rule, scalar_optical_depths

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "fig7_10mev_three_layer.json"
CHANNELS = ("neutrino", "compton", "dimuon")
PRODUCTION_KEYS = {"neutrino": "neutrino_production", "compton": "compton_production", "dimuon": "dimuon_production"}


def channel_reduced_absorptions(production_by_channel, omega, temperature):
    """Decompose the reference reduced opacity channel by channel."""
    x = np.asarray(omega, dtype=float) / np.asarray(temperature, dtype=float)
    return {
        channel: -np.expm1(-x) * np.exp(np.minimum(x, 700.0)) * np.asarray(production, dtype=float)
        for channel, production in production_by_channel.items()
    }


def weighted_quantile(values, weights, quantile):
    values, weights = np.asarray(values, float).ravel(), np.asarray(weights, float).ravel()
    if not 0.0 <= quantile <= 1.0:
        raise ValueError("quantile must lie in [0, 1]")
    valid = np.isfinite(values) & np.isfinite(weights) & (weights > 0.0)
    if not np.any(valid):
        return 0.0
    values, weights = values[valid], weights[valid]
    order = np.argsort(values)
    values, weights = values[order], weights[order]
    cumulative = np.cumsum(weights)
    index = min(np.searchsorted(cumulative, quantile * cumulative[-1]), len(values)-1)
    return float(values[index])


def weighted_tau_summary(tau_by_channel, weights):
    total = sum(tau_by_channel.values())
    out = {}
    for channel, tau in tau_by_channel.items():
        out[channel] = {
            "weighted_mean": float(np.average(tau, weights=weights)),
            "weighted_median": weighted_quantile(tau, weights, 0.50),
            "weighted_p90": weighted_quantile(tau, weights, 0.90),
        }
    out["total"] = {
        "weighted_mean": float(np.average(total, weights=weights)),
        "weighted_median": weighted_quantile(total, weights, 0.50),
        "weighted_p90": weighted_quantile(total, weights, 0.90),
    }
    mean_total = out["total"]["weighted_mean"]
    for channel in CHANNELS:
        out[channel]["fraction_of_mean_total"] = out[channel]["weighted_mean"] / mean_total if mean_total > 0 else 0.0
    return out


def decompose(profile_path, fig7_path, radial_order=40, energy_order=100, angular_order=16, path_order=32, radius_km=25.0, energy_offset=1000.0):
    fig7 = json.loads(fig7_path.read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"]["10.0"]
    couplings = np.asarray(vertices["g"], float)
    reference = np.asarray(vertices["luminosity_erg_s"], float)
    if len(couplings) != 25 or len(reference) != 25:
        raise ValueError("Expected the archived 25-point 10 MeV Fig. 7 grid")

    r, rw = radial_rule(radius_km, radial_order)
    radial_grid = np.unique(np.r_[0.0, r, radius_km])
    profile = load_profile(profile_path, radial_grid)
    energies = 10.0 + np.geomspace(1e-5, energy_offset, energy_order)
    energies = np.unique(np.r_[energies, 10.0 / profile["lapse"]])
    energies = energies[energies > 10.0 * (1.0 + 1e-10)]
    energies.sort()
    rates = local_rates(10.0, energies[None, :], profile["T"][:, None], profile["mu_numu"][:, None], profile["mu_mu"][:, None])
    production = {ch: rates[key] for ch, key in PRODUCTION_KEYS.items()}
    reduced = channel_reduced_absorptions(production, energies[None, :], profile["T"][:, None])
    reduced_sum = sum(reduced.values())
    reduced_reference = rates["reduced_absorption"]
    reduced_residual = float(np.max(np.abs(reduced_sum-reduced_reference)/np.maximum(np.abs(reduced_reference),1e-300)))

    columns, angle_weights = {}, None
    for ch in CHANNELS:
        columns[ch], angle_weights = scalar_optical_depths(r, radial_grid, reduced[ch], 10.0, energies, radius_km, angular_order, path_order)
    total_columns = sum(columns.values())
    direct_columns, direct_angle_weights = scalar_optical_depths(r, radial_grid, reduced_reference, 10.0, energies, radius_km, angular_order, path_order)
    column_residual = float(np.max(np.abs(total_columns-direct_columns)/np.maximum(np.abs(direct_columns),1e-300)))
    angle_residual = float(np.max(np.abs(angle_weights-direct_angle_weights)))

    source_index = np.searchsorted(radial_grid, r)
    lapse = profile["lapse"][source_index]
    eweights = energy_weights(energies, 10.0/lapse)
    momentum = np.sqrt(np.maximum(energies**2-10.0**2,0.0))
    geometry = 4.0*np.pi*(r*KM_TO_MEV_INV)**2 * rw*KM_TO_MEV_INV * lapse**2
    phase_space = momentum*energies**2/(2.0*np.pi**2)
    measure = geometry[:,None]*eweights*phase_space[None,:]*MEV2_TO_ERG_S
    source_unit = {ch: measure*production[ch][source_index] for ch in CHANNELS}
    source_total = sum(source_unit.values())
    angular_source_weights = source_total[:,None,:]*angle_weights[None,:,None]

    peak_index = int(np.argmax(reference))
    selected_indices = {"weak_coupling":0, "reference_peak":peak_index, "strong_absorption":len(couplings)-1}
    rows=[]
    for index,g in enumerate(couplings):
        escape = np.exp(-g**2*total_columns)
        escape_average = np.einsum("rae,a->re",escape,angle_weights)
        channel_rows={}
        thin_total=escaped_total=0.0
        for ch in CHANNELS:
            thin=float(g**2*np.sum(source_unit[ch]))
            escaped=float(g**2*np.sum(source_unit[ch]*escape_average))
            thin_total += thin
            escaped_total += escaped
            channel_rows[ch]={
                "optically_thin_luminosity_erg_s":thin,
                "escaped_luminosity_erg_s":escaped,
                "escape_fraction":escaped/thin if thin>0 else 0.0,
                "fraction_of_total_escaped":0.0,
            }
        for ch in CHANNELS:
            channel_rows[ch]["fraction_of_total_escaped"] = channel_rows[ch]["escaped_luminosity_erg_s"]/escaped_total if escaped_total>0 else 0.0
        tau_summary=weighted_tau_summary({ch:g**2*columns[ch] for ch in CHANNELS},angular_source_weights)
        rows.append({
            "index":index,"g":float(g),
            "reference_luminosity_erg_s":float(reference[index]),
            "calculated_luminosity_erg_s":escaped_total,
            "relative_difference":float(escaped_total/reference[index]-1.0),
            "optically_thin_total_luminosity_erg_s":thin_total,
            "total_escape_fraction":escaped_total/thin_total if thin_total>0 else 0.0,
            "channels":channel_rows,
            "source_weighted_optical_depth":tau_summary,
        })

    residuals=np.asarray([row["relative_difference"] for row in rows])
    channel_sum_residual=max(
        abs(sum(row["channels"][ch]["escaped_luminosity_erg_s"] for ch in CHANNELS)/max(row["calculated_luminosity_erg_s"],1e-300)-1.0)
        for row in rows
    )
    return {
        "title":"Three-layer decomposition of Blinov Fig. 7 at 10 MeV",
        "mass_MeV":10.0,
        "scope":"Independent diagnostic using the archived literal scalar Appendix-B reference. Production rates, transport code, axial scan, manuscript and constraint figures are unchanged.",
        "interpretation_limit":"The channel opacities use the same detailed-balance prescription as reference.py. This is not an independent microscopic derivation or direct forward/reverse thermal phase-space integration of B.19.",
        "input_sha256":{
            "profile":hashlib.sha256(profile_path.read_bytes()).hexdigest(),
            "fig7_comparison_json":hashlib.sha256(fig7_path.read_bytes()).hexdigest(),
            "fig7_pdf":fig7.get("pdf_sha256"),
        },
        "run_commit_sha":os.environ.get("GITHUB_SHA"),
        "quadrature":{"radial_order":radial_order,"energy_order":energy_order,"angular_order":angular_order,"path_order":path_order,"radius_km":radius_km,"energy_offset_MeV":energy_offset},
        "channel_definitions":{
            "neutrino":"neutrino-pair coalescence production and inverse neutrino-decay opacity",
            "compton":"semi-Compton muon-photon production and inverse Compton opacity",
            "dimuon":"muon-pair production and inverse dimuon opacity, when open",
        },
        "internal_consistency":{
            "channel_reduced_opacity_sum_vs_reference_max_relative_residual":reduced_residual,
            "sum_channel_columns_vs_direct_total_max_relative_residual":column_residual,
            "angle_weight_max_absolute_residual":angle_residual,
            "escaped_channel_luminosity_sum_max_relative_residual":float(channel_sum_residual),
        },
        "curve_metrics":{
            "n_points":len(rows),
            "mean_absolute_relative_difference":float(np.mean(np.abs(residuals))),
            "maximum_absolute_relative_difference":float(np.max(np.abs(residuals))),
            "weak_coupling_relative_difference":float(residuals[0]),
            "reference_peak_relative_difference":float(residuals[peak_index]),
            "strong_absorption_relative_difference":float(residuals[-1]),
        },
        "selected_points":{name:rows[idx] for name,idx in selected_indices.items()},
        "all_25_curve_points":rows,
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    parser.add_argument("--fig7",type=Path,default=DEFAULT_FIG7)
    parser.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    parser.add_argument("--nr",type=int,default=40)
    parser.add_argument("--ne",type=int,default=100)
    parser.add_argument("--na",type=int,default=16)
    parser.add_argument("--ns",type=int,default=32)
    args=parser.parse_args()
    report=decompose(args.profile,args.fig7,args.nr,args.ne,args.na,args.ns)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({
        "curve_metrics":report["curve_metrics"],
        "internal_consistency":report["internal_consistency"],
        "selected_points":{
            name:{
                "g":row["g"],"relative_difference":row["relative_difference"],
                "thin":row["optically_thin_total_luminosity_erg_s"],
                "escaped":row["calculated_luminosity_erg_s"],
                "channels":row["channels"],"tau":row["source_weighted_optical_depth"],
            } for name,row in report["selected_points"].items()
        },
        "output":str(args.output),
    },indent=2))


if __name__=="__main__":
    main()
