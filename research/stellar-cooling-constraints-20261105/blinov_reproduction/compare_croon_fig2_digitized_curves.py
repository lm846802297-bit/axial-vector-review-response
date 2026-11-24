"""Point-by-point, no-fit comparison of Croon Fig. 2 vector paths and C0 curves."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DEFAULT_MODEL = HERE / "outputs" / "croon_fig2_literal_transport_preliminary_2026-11-19.json"
DEFAULT_DIGITIZED = HERE / "outputs" / "croon_fig2_digitized_curves_2026-11-19.json"
DEFAULT_OUTPUT = HERE / "outputs" / "croon_fig2_digitized_comparison_2026-11-19.json"


def _metrics(residual_dex: np.ndarray) -> dict:
    r = np.asarray(residual_dex, dtype=float)
    if r.size == 0:
        return {"point_count": 0}
    return {
        "point_count": int(r.size),
        "median_residual_dex_model_minus_digitized": float(np.median(r)),
        "mean_residual_dex_model_minus_digitized": float(np.mean(r)),
        "rms_residual_dex": float(np.sqrt(np.mean(r*r))),
        "maximum_absolute_residual_dex": float(np.max(np.abs(r))),
        "fraction_within_0p05_dex": float(np.mean(np.abs(r) <= 0.05)),
        "fraction_within_0p10_dex": float(np.mean(np.abs(r) <= 0.10)),
        "median_model_over_digitized": float(10.0**np.median(r)),
    }


def compare_curves(model: dict, digitized: dict) -> dict:
    model_curves = model.get("curves")
    digitized_curves = digitized.get("curves")
    if not isinstance(model_curves, dict) or not isinstance(digitized_curves, dict):
        raise ValueError("Both inputs must contain a curves mapping")

    output = {}
    for label, dcurve in digitized_curves.items():
        if label not in model_curves:
            raise ValueError(f"Digitized curve {label!r} has no model counterpart")
        mcurve = model_curves[label]
        gm = np.asarray(mcurve.get("g", []), dtype=float)
        lm = np.asarray(mcurve.get("L_erg_s", []), dtype=float)
        points = dcurve.get("points", [])
        gd = np.asarray([p["g"] for p in points], dtype=float)
        ld = np.asarray([p["L_erg_s"] for p in points], dtype=float)

        if (gm.ndim != 1 or lm.ndim != 1 or gd.ndim != 1 or ld.ndim != 1
                or len(gm) != len(lm) or len(gd) != len(ld)):
            raise ValueError(f"{label}: malformed curve arrays")
        if (np.any(~np.isfinite(gm)) or np.any(~np.isfinite(lm))
                or np.any(gm <= 0.0) or np.any(np.diff(gm) <= 0.0)):
            raise ValueError(f"{label}: model coupling grid must be finite, positive, and strictly increasing")
        if np.any(np.diff(gd) < 0.0):
            raise ValueError(f"{label}: digitized points must be ordered by increasing g")

        valid_data = np.isfinite(gd) & np.isfinite(ld) & (gd > 0.0) & (ld > 0.0)
        in_range = valid_data & (gd >= gm[0]) & (gd <= gm[-1])
        model_log_g = np.log10(gm)
        model_log_l = np.full(len(gm), np.nan)
        positive_model = lm > 0.0
        model_log_l[positive_model] = np.log10(lm[positive_model])

        interpolable = np.zeros(len(gd), dtype=bool)
        interpolated_log_l = np.full(len(gd), np.nan)
        for j in np.flatnonzero(in_range):
            right = int(np.searchsorted(gm, gd[j], side="left"))
            if right < len(gm) and abs(np.log10(gd[j])-model_log_g[right]) <= 1e-13:
                if positive_model[right]:
                    interpolable[j] = True
                    interpolated_log_l[j] = model_log_l[right]
                continue
            left = right - 1
            if (left >= 0 and right < len(gm)
                    and positive_model[left] and positive_model[right]):
                fraction = (
                    np.log10(gd[j])-model_log_g[left]
                ) / (model_log_g[right]-model_log_g[left])
                interpolated_log_l[j] = (
                    model_log_l[left]
                    + fraction*(model_log_l[right]-model_log_l[left])
                )
                interpolable[j] = True

        used_mask = in_range & interpolable
        used_g = gd[used_mask]
        used_ld = ld[used_mask]
        model_log_l_used = interpolated_log_l[used_mask]
        if len(used_g) == 0:
            raise ValueError(f"{label}: no digitized points overlap positive model segments")

        residual = model_log_l_used - np.log10(used_ld)
        peak_index = int(np.argmax(np.where(positive_model, lm, -np.inf)))
        peak_g = float(gm[peak_index])
        low = used_g <= peak_g
        high = used_g > peak_g

        point_rows = []
        used_indices = np.flatnonzero(used_mask)
        for source_index, g, l_data, log_l_model, res in zip(
            used_indices, used_g, used_ld, model_log_l_used, residual
        ):
            point_rows.append({
                "digitized_point_index": int(source_index),
                "g": float(g),
                "L_digitized_erg_s": float(l_data),
                "L_model_interpolated_erg_s": float(10.0**log_l_model),
                "model_over_digitized": float(10.0**res),
                "residual_dex_model_minus_digitized": float(res),
            })

        output[label] = {
            "mass_MeV": float(mcurve.get("mass_mev", dcurve.get("mass_MeV"))),
            "source_pdf_path_index": dcurve.get("source_path_index"),
            "digitized_point_count": int(len(points)),
            "used_point_count": int(len(used_g)),
            "excluded_outside_model_range_count": int(np.sum(valid_data & ~in_range)),
            "excluded_nonpositive_model_interval_count": int(np.sum(in_range & ~interpolable)),
            "model_peak_g": peak_g,
            "all_points": _metrics(residual),
            "low_g_branch": _metrics(residual[low]),
            "high_g_branch": _metrics(residual[high]),
            "points": point_rows,
        }

    return {
        "title": "No-fit pointwise comparison of Croon Fig. 2 and C0 vector luminosity",
        "source_paper": "Croon et al., JHEP 01 (2021) 107, arXiv:2006.13942",
        "model_status": model.get("status"),
        "model_profile": model.get("profile"),
        "digitized_source_pdf_sha256": digitized.get("source_pdf_sha256"),
        "digitized_source_page_index": digitized.get("source_page_index"),
        "axis_calibration": digitized.get("axis_calibration"),
        "comparison_definition": (
            "Interpolate log10(L_model) linearly in log10(g) at each digitized vector-path point; "
            "residual is log10(L_model/L_digitized). No normalization fit, coupling shift, or curve rescaling."
        ),
        "curve_results": output,
        "interpretation_limits": [
            "The PDF vector-path centerline is used as the digitized reference; line-stroke thickness is not yet propagated as an uncertainty.",
            "The public Caputo-based SFHo-18.8 profile is not the raw Garching profile used by Croon.",
            "A curve mismatch is a diagnostic, not permission to tune a rate or normalization.",
            "The Rfar=Rnu curve is a sensitivity line and is not the conservative Rfar=100 km result.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--digitized", type=Path, default=DEFAULT_DIGITIZED)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    model = json.loads(args.model.read_text(encoding="utf-8"))
    digitized = json.loads(args.digitized.read_text(encoding="utf-8"))
    result = compare_curves(model, digitized)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({
        label: {
            "all_points": values["all_points"],
            "low_g_branch": values["low_g_branch"],
            "high_g_branch": values["high_g_branch"],
        }
        for label, values in result["curve_results"].items()
    }, indent=2))


if __name__ == "__main__":
    main()
