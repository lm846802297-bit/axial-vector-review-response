"""Diagnose the missing R_nu -> R_far opacity using Croon Fig. 2.

The published solid/dashed 0.1 eV curves differ only by the R_far choice.
The model currently includes the vacuum neutrino-decay tail outside R_nu,
but has no measured outer muon-susceptibility profile. This audit compares
the *integrated luminosity suppression* implied by the paper with the
suppression produced by the current implementation.

The resulting effective suppression is not a local optical depth and does
not uniquely reconstruct an outer opacity profile.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
MODEL = OUT / "croon_fig2_literal_transport_preliminary_2026-11-19.json"
DIGITIZED = OUT / "croon_fig2_digitized_curves_2026-11-19.json"
DEFAULT_OUTPUT = OUT / "croon_fig2_outer_opacity_gap_2026-11-19.json"

SOLID = "0.1 eV"
DASHED = "0.1 eV (Rfar=Rnu)"


def _curve_arrays(curve: dict) -> tuple[np.ndarray, np.ndarray]:
    g = np.asarray(curve.get("g", []), dtype=float)
    luminosity = np.asarray(curve.get("L_erg_s", []), dtype=float)
    if (g.ndim != 1 or luminosity.ndim != 1 or len(g) != len(luminosity)
            or len(g) < 2 or np.any(~np.isfinite(g))
            or np.any(~np.isfinite(luminosity)) or np.any(g <= 0.0)
            or np.any(luminosity <= 0.0) or np.any(np.diff(g) <= 0.0)):
        raise ValueError("Each curve needs finite, positive, strictly increasing g and L")
    return g, luminosity


def _digitized_arrays(curve: dict) -> tuple[np.ndarray, np.ndarray]:
    points = curve.get("points", [])
    g = np.asarray([p["g"] for p in points], dtype=float)
    luminosity = np.asarray([p["L_erg_s"] for p in points], dtype=float)
    if (g.ndim != 1 or luminosity.ndim != 1 or len(g) < 2
            or np.any(~np.isfinite(g)) or np.any(~np.isfinite(luminosity))
            or np.any(g <= 0.0) or np.any(luminosity <= 0.0)
            or np.any(np.diff(g) < 0.0)):
        raise ValueError("Digitized curve points must be finite, positive, and ordered")
    # Remove repeated g values before interpolation, retaining the first
    # centerline point. Repeated PDF vertices are not independent samples.
    unique_g, indices = np.unique(g, return_index=True)
    return unique_g, luminosity[indices]


def _log_interp(g_src: np.ndarray, L_src: np.ndarray, g_eval: np.ndarray) -> np.ndarray:
    if np.any(g_eval < g_src[0]) or np.any(g_eval > g_src[-1]):
        raise ValueError("Interpolation would extrapolate outside a curve's g range")
    return 10.0 ** np.interp(np.log10(g_eval), np.log10(g_src), np.log10(L_src))


def _summary(values: np.ndarray) -> dict:
    x = np.asarray(values, dtype=float)
    return {
        "count": int(len(x)),
        "median": float(np.median(x)),
        "p16": float(np.percentile(x, 16)),
        "p84": float(np.percentile(x, 84)),
        "minimum": float(np.min(x)),
        "maximum": float(np.max(x)),
    }


def analyze_outer_opacity_gap(
    model: dict,
    digitized: dict,
    plateau_g_range: tuple[float, float] = (3.0e-6, 3.0e-2),
    low_g_range: tuple[float, float] = (1.0e-9, 1.0e-7),
) -> dict:
    model_curves = model.get("curves", {})
    digitized_curves = digitized.get("curves", {})
    required_model = (SOLID, DASHED)
    for label in required_model:
        if label not in model_curves or label not in digitized_curves:
            raise ValueError(f"Missing required solid/dashed curve {label!r}")

    gm_s, lm_s = _curve_arrays(model_curves[SOLID])
    gm_d, lm_d = _curve_arrays(model_curves[DASHED])
    gd_s, ld_s = _digitized_arrays(digitized_curves[SOLID])
    gd_d, ld_d = _digitized_arrays(digitized_curves[DASHED])

    lo = max(gd_s[0], gd_d[0], gm_s[0], gm_d[0])
    hi = min(gd_s[-1], gd_d[-1], gm_s[-1], gm_d[-1])
    common = gd_s[(gd_s >= lo) & (gd_s <= hi)]
    if len(common) < 10:
        raise ValueError("Too few common digitized points between the solid and dashed curves")

    paper_solid = _log_interp(gd_s, ld_s, common)
    paper_dashed = _log_interp(gd_d, ld_d, common)
    model_solid = _log_interp(gm_s, lm_s, common)
    model_dashed = _log_interp(gm_d, lm_d, common)

    paper_outer_suppression = paper_dashed / paper_solid
    model_outer_suppression = model_dashed / model_solid
    missing_suppression = paper_outer_suppression / model_outer_suppression
    effective_delta_tau = np.log(missing_suppression)

    def branch(mask: np.ndarray) -> dict:
        if not np.any(mask):
            return {"count": 0}
        return {
            "g_range": [float(np.min(common[mask])), float(np.max(common[mask]))],
            "paper_Rnu_over_Rfar100_luminosity_ratio": _summary(paper_outer_suppression[mask]),
            "model_Rnu_over_Rfar100_luminosity_ratio": _summary(model_outer_suppression[mask]),
            "additional_missing_luminosity_suppression": _summary(missing_suppression[mask]),
            "effective_log_suppression_ln_ratio": _summary(effective_delta_tau[mask]),
            "model_over_paper_solid_Rfar100": _summary((model_solid/paper_solid)[mask]),
            "model_over_paper_dashed_RfarRnu": _summary((model_dashed/paper_dashed)[mask]),
        }

    plateau = (common >= plateau_g_range[0]) & (common <= plateau_g_range[1])
    weak = (common >= low_g_range[0]) & (common <= low_g_range[1])

    rows = []
    for i, g in enumerate(common):
        rows.append({
            "g": float(g),
            "paper_L_Rfar100_erg_s": float(paper_solid[i]),
            "paper_L_Rnu_erg_s": float(paper_dashed[i]),
            "model_L_Rfar100_erg_s": float(model_solid[i]),
            "model_L_Rnu_erg_s": float(model_dashed[i]),
            "paper_outer_luminosity_suppression": float(paper_outer_suppression[i]),
            "model_outer_luminosity_suppression": float(model_outer_suppression[i]),
            "additional_missing_luminosity_suppression": float(missing_suppression[i]),
            "effective_delta_tau_ln_ratio": float(effective_delta_tau[i]),
        })

    return {
        "title": "Croon Fig. 2 outer-opacity gap: solid versus Rfar=Rnu dashed 0.1 eV curves",
        "source_pdf_sha256": digitized.get("source_pdf_sha256"),
        "model_status": model.get("status"),
        "model_profile": model.get("profile"),
        "curve_identity": {
            "solid": SOLID,
            "dashed": DASHED,
            "paper_definition": "The published dashed 0.1 eV curve changes R_far from 100 km to R_nu; the solid curve uses R_far=100 km.",
            "model_outer_medium": "The current implementation has no measured muon-susceptibility profile outside R_nu; only the vacuum neutrino-decay tail is included.",
        },
        "comparison_definition": (
            "S_paper=L_paper(Rfar=Rnu)/L_paper(Rfar=100 km); "
            "S_model=L_model(Rfar=Rnu)/L_model(Rfar=100 km); "
            "missing suppression=S_paper/S_model. "
            "ln(missing suppression) is an effective integrated-luminosity diagnostic, not a local optical depth."
        ),
        "plateau_g_range": list(plateau_g_range),
        "weak_g_range": list(low_g_range),
        "weak_branch": branch(weak),
        "strong_coupling_plateau": branch(plateau),
        "full_common_range": branch(np.ones_like(common, dtype=bool)),
        "pointwise": rows,
        "limitations": [
            "A ratio of volume-integrated luminosities cannot uniquely determine Gamma_abs(r,omega) outside R_nu.",
            "The PDF vector-path centerline has no propagated stroke-width uncertainty.",
            "The public profile does not provide a validated muon-susceptibility profile from R_nu to R_far.",
            "No outer opacity is tuned or inferred as a physical radial profile from this diagnostic.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, default=MODEL)
    parser.add_argument("--digitized", type=Path, default=DIGITIZED)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    model = json.loads(args.model.read_text(encoding="utf-8"))
    digitized = json.loads(args.digitized.read_text(encoding="utf-8"))
    result = analyze_outer_opacity_gap(model, digitized)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({
        "weak_branch": result["weak_branch"],
        "strong_coupling_plateau": result["strong_coupling_plateau"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
