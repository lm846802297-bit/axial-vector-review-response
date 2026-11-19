"""Compare baseline/high-order Croon C0 curves and charge-conjugate sensitivity."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
BASE = OUT / "croon_c0_luminosity_10mev_2026-11-19.json"
HIGH = OUT / "croon_c0_luminosity_10mev_highorder_2026-11-19.json"
BOTH = OUT / "croon_c0_luminosity_10mev_antimuons_2026-11-19.json"
LMUTAU = OUT / "croon_c0_luminosity_10mev_lmutau_2026-11-19.json"
DEFAULT_OUTPUT = OUT / "croon_c0_luminosity_convergence_2026-11-19.json"
RAFFELT = 3.0e52
SCENARIOS = ("vacuum_tail", "Rfar_Rnu", "T3_outer_envelope")
CHANNELS = ("L_nu_coalescence_erg_s", "L_semi_compton_erg_s", "L_total_erg_s")


def load(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("mass_MeV") != 10.0:
        raise ValueError(f"{path.name}: expected mV=10 MeV")
    return data


def crossing_couplings(curve: list[dict], scenario: str, threshold: float = RAFFELT) -> list[float]:
    g = np.asarray([x["g_X"] for x in curve], float)
    L = np.asarray([x[scenario]["L_total_erg_s"] for x in curve], float)
    crossings = []
    for i in range(len(g)-1):
        if (L[i]-threshold)*(L[i+1]-threshold) <= 0.0 and L[i] != L[i+1]:
            x0, x1 = np.log10(g[i]), np.log10(g[i+1])
            y0, y1 = np.log10(L[i]), np.log10(L[i+1])
            x = x0 + (np.log10(threshold)-y0)*(x1-x0)/(y1-y0)
            crossings.append(float(10.0**x))
    return crossings


def peak(curve: list[dict], scenario: str) -> dict:
    item = max(curve, key=lambda x: x[scenario]["L_total_erg_s"])
    return {"g_X": item["g_X"], **item[scenario]}


def run(
    base_path: Path = BASE, high_path: Path = HIGH,
    both_path: Path = BOTH, lmutau_path: Path = LMUTAU
) -> dict:
    base, high, both, lmutau = (
        load(base_path), load(high_path), load(both_path), load(lmutau_path)
    )
    if len({x["profile_sha256"] for x in (base, high, both, lmutau)}) != 1:
        raise ValueError("All four runs must use exactly the same profile")
    if base["neutrino_flavour_factor"] != 1.0 or high["neutrino_flavour_factor"] != 1.0:
        raise ValueError("The primary C0 curve is the generic one-neutrino-flavour baseline")
    if lmutau["neutrino_flavour_factor"] != 2.0:
        raise ValueError("The Lmu-Ltau variant must use the Sec. 4.4 factor of two")
    if base["muon_susceptibility"]["charge_conjugate_mu_plus_included"]:
        raise ValueError("Primary baseline must use mu- only")
    if not both["muon_susceptibility"]["charge_conjugate_mu_plus_included"]:
        raise ValueError("Charge-conjugate sensitivity file must include mu+")

    bcurve, hcurve, acurve, lcurve = (
        base["coupling_curve"], high["coupling_curve"],
        both["coupling_curve"], lmutau["coupling_curve"]
    )
    gb = np.asarray([x["g_X"] for x in bcurve])
    gh = np.asarray([x["g_X"] for x in hcurve])
    ga = np.asarray([x["g_X"] for x in acurve])
    gl = np.asarray([x["g_X"] for x in lcurve])
    if not (np.array_equal(gb, gh) and np.array_equal(gb, ga) and np.array_equal(gb, gl)):
        raise ValueError("Coupling grids differ between runs")

    convergence = {}
    anti_sensitivity = {}
    lmutau_sensitivity = {}
    for scenario in SCENARIOS:
        convergence[scenario] = {}
        anti_sensitivity[scenario] = {}
        lmutau_sensitivity[scenario] = {}
        for channel in CHANNELS:
            b = np.asarray([x[scenario][channel] for x in bcurve])
            h = np.asarray([x[scenario][channel] for x in hcurve])
            a = np.asarray([x[scenario][channel] for x in acurve])
            l = np.asarray([x[scenario][channel] for x in lcurve])
            rel = np.abs(h/b-1.0)
            anti = a/b-1.0
            lmutau_rel = l/b-1.0
            convergence[scenario][channel] = {
                "maximum_absolute_relative_change": float(np.max(rel)),
                "mean_absolute_relative_change": float(np.mean(rel)),
            }
            anti_sensitivity[scenario][channel] = {
                "minimum_relative_change": float(np.min(anti)),
                "maximum_relative_change": float(np.max(anti)),
                "relative_change_at_g1e-9": float(
                    a[int(np.argmin(np.abs(gb-1e-9)))] /
                    b[int(np.argmin(np.abs(gb-1e-9)))] - 1.0
                ),
            }
            lmutau_sensitivity[scenario][channel] = {
                "minimum_relative_change_vs_generic": float(np.min(lmutau_rel)),
                "maximum_relative_change_vs_generic": float(np.max(lmutau_rel)),
                "relative_change_at_g1e-9": float(
                    l[int(np.argmin(np.abs(gb-1e-9)))] /
                    b[int(np.argmin(np.abs(gb-1e-9)))] - 1.0
                ),
            }

    ordering_checks = {
        "Rfar_Rnu_not_below_Rfar100": all(
            x["Rfar_Rnu"]["L_total_erg_s"] >= x["vacuum_tail"]["L_total_erg_s"]*(1.0-2e-10)
            for x in bcurve
        ),
        "T3_outer_envelope_not_above_vacuum_tail": all(
            x["T3_outer_envelope"]["L_total_erg_s"] <= x["vacuum_tail"]["L_total_erg_s"]*(1.0+2e-10)
            for x in bcurve
        ),
    }
    if not all(ordering_checks.values()):
        raise AssertionError(f"Unexpected Rfar ordering: {ordering_checks}")

    crossings = {
        scenario: {
            "generic_baseline_gX_crossings_of_Raffelt_3e52": crossing_couplings(bcurve, scenario),
            "generic_high_order_gX_crossings_of_Raffelt_3e52": crossing_couplings(hcurve, scenario),
            "LmuLtau_gX_crossings_of_Raffelt_3e52": crossing_couplings(lcurve, scenario),
            "generic_baseline_peak": peak(bcurve, scenario),
            "generic_high_order_peak": peak(hcurve, scenario),
            "LmuLtau_peak": peak(lcurve, scenario),
        }
        for scenario in SCENARIOS
    }

    return {
        "title": "Croon C0 mV=10 MeV numerical convergence and profile-convention audit",
        "profile_sha256": base["profile_sha256"],
        "profile_rows": base["profile_rows"],
        "mass_MeV": 10.0,
        "generic_neutrino_flavour_factor": 1.0,
        "LmuLtau_neutrino_flavour_factor": 2.0,
        "muon_charge_convention": "mu- only baseline; mu- + mu+ sensitivity reported separately",
        "R_nu_km": base["R_nu_km"],
        "quadrature": {
            "baseline": base["quadrature"],
            "high_order": high["quadrature"],
        },
        "free_streaming_channel_luminosity_baseline": base["free_streaming_channel_luminosity_per_g2_erg_s"],
        "free_streaming_channel_luminosity_high_order": high["free_streaming_channel_luminosity_per_g2_erg_s"],
        "high_order_convergence": convergence,
        "antimuon_charge_conjugate_sensitivity": anti_sensitivity,
        "LmuLtau_two_flavour_sensitivity_vs_generic": lmutau_sensitivity,
        "raffelt_threshold_erg_s": RAFFELT,
        "crossings_and_peaks": crossings,
        "Rfar_ordering_checks": ordering_checks,
        "scope": "public Caputo/Bollig profile reconstruction; generic Croon Fig. 2 baseline compared with the separate Sec. 4.4 Lmu-Ltau factor-two variant; not a raw-Garching reproduction or final cooling bound",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=BASE)
    parser.add_argument("--high-order", type=Path, default=HIGH)
    parser.add_argument("--antimuons", type=Path, default=BOTH)
    parser.add_argument("--lmutau", type=Path, default=LMUTAU)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(args.baseline, args.high_order, args.antimuons, args.lmutau)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({
        "R_nu_km": result["R_nu_km"],
        "high_order_convergence": result["high_order_convergence"],
        "antimuon_charge_conjugate_sensitivity": result["antimuon_charge_conjugate_sensitivity"],
        "LmuLtau_two_flavour_sensitivity_vs_generic": result["LmuLtau_two_flavour_sensitivity_vs_generic"],
        "crossings_and_peaks": result["crossings_and_peaks"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
