#!/usr/bin/env python3
"""Quantify scalar-summed, scalar-averaged, and mode-resolved transport outputs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

MASSES = (1e-6, 1e-5, 0.1, 1.0, 10.0, 200.0)


def analyze(path: Path) -> dict:
    source = json.loads(path.read_text(encoding="utf-8"))
    rows = source["comparison"]
    indexed = {}
    for row in rows:
        indexed[(float(row["mass_MeV"]), row["variant"], float(row["g"]))] = float(
            row["calculated_erg_s"]
        )

    def paired(scalar: str, resolved: str) -> dict:
        result = {}
        for mass in MASSES:
            deltas = []
            for row in rows:
                if float(row["mass_MeV"]) != mass or row["variant"] != resolved:
                    continue
                key = (mass, scalar, float(row["g"]))
                denominator = indexed[key]
                if denominator <= 0 or row["calculated_erg_s"] <= 0:
                    raise ValueError("Nonpositive luminosity in a transport comparison")
                deltas.append(float(row["calculated_erg_s"])/denominator-1.0)
            a = np.asarray(deltas, float)
            result[str(mass)] = {
                "points": int(a.size),
                "mean_signed_change": float(np.mean(a)),
                "mean_absolute_change": float(np.mean(np.abs(a))),
                "max_absolute_change": float(np.max(np.abs(a))),
                "minimum_signed_change": float(np.min(a)),
                "maximum_signed_change": float(np.max(a)),
            }
        return result

    residuals = {}
    for mass in MASSES:
        residuals[str(mass)] = {}
        for variant in ("blinov_literal", "blinov_average", "thomson_modes",
                        "exact_recoil_scalar", "exact_modes"):
            errors = np.asarray([
                abs(float(row["relative_error"])) for row in rows
                if float(row["mass_MeV"]) == mass and row["variant"] == variant
            ], float)
            residuals[str(mass)][variant] = {
                "points": int(errors.size),
                "mean_absolute_literature_residual": float(np.mean(errors)),
                "max_absolute_literature_residual": float(np.max(errors)),
            }

    return {
        "input_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "source_pdf_sha256": source["pdf_sha256"],
        "literature_residuals": residuals,
        "controlled_transport_effects": {
            "B14_mode_resolved_over_scalar_sum": paired("blinov_literal", "thomson_modes"),
            "B14_scalar_average_over_scalar_sum": paired("blinov_literal", "blinov_average"),
            "B14_mode_resolved_over_scalar_average": paired("blinov_average", "thomson_modes"),
            "fixed_target_exact_recoil_mode_over_scalar": paired("exact_recoil_scalar", "exact_modes"),
        },
        "interpretation": {
            "B14_mode_resolved_over_scalar_sum": (
                "Changes only the transport prescription: identical B.14 local kernels "
                "and mode-summed production, with per-mode versus scalar-summed attenuation."
            ),
            "B14_scalar_average_over_scalar_sum": (
                "Diagnostic arithmetic-average opacity (sum of mode opacities divided by 3); "
                "not adopted as a physical prescription without source justification."
            ),
            "fixed_target_exact_recoil_mode_over_scalar": (
                "Changes transport polarization treatment at fixed-target exact recoil; "
                "this is not the full moving-muon B.13 thermal integral."
            ),
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n",
                           encoding="utf-8")
    for name, values in result["controlled_transport_effects"].items():
        print(name)
        for mass, stats in values.items():
            print(mass, stats)


if __name__ == "__main__":
    main()
