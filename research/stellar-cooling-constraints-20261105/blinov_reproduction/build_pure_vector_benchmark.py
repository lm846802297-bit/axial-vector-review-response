"""Build an auditable 4B summary from the archived literal Blinov vector run.

This does not rerun the costly transport scan. It verifies the SHA-256 links
between the existing scan, its source code, reconstructed profile and
digitized Fig. 7 comparison, then emits a compact acceptance report.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data"
OUT = HERE / "outputs"

SCAN = OUT / "blinov_fig7_refined_scan.json"
COMPARISON = OUT / "fig7_refined_comparison.json"
REFERENCE = HERE / "reference.py"
PROFILE = DATA / "sfho188_digitized.csv"
FIG7_SOURCE = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
FIGURE_PROVENANCE = DATA / "vector_reference" / "provenance.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    scan = json.loads(SCAN.read_text(encoding="utf-8"))
    comparison = json.loads(COMPARISON.read_text(encoding="utf-8"))

    hashes = {
        "reference_py": sha256(REFERENCE),
        "profile_csv": sha256(PROFILE),
        "refined_scan_json": sha256(SCAN),
        "fig7_digitized_source_json": sha256(FIG7_SOURCE),
        "fig7_provenance_json": sha256(FIGURE_PROVENANCE),
        "comparison_json": sha256(COMPARISON),
    }
    linked_hash_checks = {
        "scan_uses_current_reference_code":
            scan["reference_code_sha256"] == hashes["reference_py"],
        "scan_uses_current_reconstructed_profile":
            scan["profile_sha256"] == hashes["profile_csv"],
        "comparison_uses_this_refined_scan":
            comparison["input_sha256"]["scan_json"] == hashes["refined_scan_json"],
        "comparison_uses_current_fig7_digitization":
            comparison["input_sha256"]["fig7_digitized_comparison_source"]
            == hashes["fig7_digitized_source_json"],
        "comparison_uses_current_fig4_digitization":
            comparison["input_sha256"]["fig4_digitized_vertices"]
            == sha256(DATA / "vector_reference" / "blinov_cooling_vertices.csv"),
        "comparison_uses_current_fig4_provenance":
            comparison["input_sha256"]["fig4_provenance"]
            == hashes["fig7_provenance_json"],
    }

    curve_rows = []
    for row in comparison["fig7"]:
        curve_rows.append({
            "mass_MeV": row["mass_MeV"],
            "digitized_points": row["reference_points"],
            "mean_absolute_relative_difference":
                row["mean_abs_relative_difference"],
            "maximum_absolute_relative_difference":
                row["max_abs_relative_difference"],
            "mean_absolute_relative_difference_percent":
                100.0 * row["mean_abs_relative_difference"],
            "maximum_absolute_relative_difference_percent":
                100.0 * row["max_abs_relative_difference"],
            "pointwise_residuals": row["points"],
        })

    # The 10 MeV curve is a required Fig. 7 benchmark point and currently
    # fails badly at the high-absorption end. Do not average this away.
    ten_mev = next(x for x in curve_rows if x["mass_MeV"] == 10.0)
    other_max = max(
        x["maximum_absolute_relative_difference"]
        for x in curve_rows if x["mass_MeV"] != 10.0
    )
    acceptance = {
        "provenance_hash_links_pass": all(linked_hash_checks.values()),
        "fig7_curve_reproduction_pass": (
            all(x["maximum_absolute_relative_difference"] < 0.10
                for x in curve_rows)
        ),
        "ten_MeV_curve_pass": ten_mev["maximum_absolute_relative_difference"] < 0.10,
        "all_other_digitized_curves_within_10_percent":
            other_max < 0.10,
        "overall_4B_status": "NOT_PASSED" if (
            not all(linked_hash_checks.values())
            or ten_mev["maximum_absolute_relative_difference"] >= 0.10
        ) else "PASSED",
    }

    payload = {
        "title": "4B pure-vector Blinov Appendix-B benchmark audit",
        "source": {
            "paper": "Blinov et al., arXiv:2511.09619v2",
            "url": "https://arxiv.org/abs/2511.09619",
            "target": "Fig. 7, s18.8-SFHo-MUONS, 1 s post-bounce",
            "equation_map": {
                "luminosity": "Eq. (17)",
                "direction_averaged_escape_and_path": "Eqs. (18)-(19)",
                "reduced_absorption_and_vector_speed": "Eqs. (20)-(21)",
                "neutrino_production": "Eqs. (22)-(26)",
                "dimuon_production": "Eqs. (27)-(28)",
                "semi_Compton_collision_integral": "Eq. (29)",
                "no_recoil_semi_Compton_cross_section": "Eq. (30)",
                "production_rate": "Eqs. (31)-(32)",
                "muon_degeneracy_factor": "Eq. (33)",
                "forward_reverse_cross_section_ratio": "Eq. (34)",
                "semi_Compton_detailed_balance": "Eq. (35)",
            },
        },
        "implementation": {
            "module": "blinov_reproduction/reference.py",
            "independent_of_production_rates_and_transport": True,
            "prescription": "Literal scalar Appendix-B rate and opacity prescription",
            "muon_distribution": "Single negative-muon distribution as written in Eq. (33)",
            "semi_compton": "Nonrelativistic muon, no recoil, Eq. (30)-(32)",
            "transport": "Full direction-averaged chord optical depth, Eq. (18)-(21)",
            "profile": "Reconstructed SFHo-18.8, 1 s public-figure profile; not original simulation tables",
            "profile_radius_km": 25.0,
            "quadrature": {
                "radial_order": 132,
                "energy_order": 280,
                "angular_order": 40,
                "path_order": 96,
            },
            "coupling_scan_points_per_mass": 501,
            "masses_MeV": [x["mass_MeV"] for x in scan["results"]],
        },
        "hashes_sha256": hashes,
        "linked_hash_checks": linked_hash_checks,
        "fig7_comparison": curve_rows,
        "acceptance": acceptance,
        "interpretation": [
            "This is a literal scalar-opacity reproduction of the published vector-boson calculation; it is not the newer mode-resolved axial calculation.",
            "The vector Fig. 7 reproduction is not passed: the 10 MeV high-absorption tail has a large residual.",
            "The near-agreement at the peak does not validate the full curve because source normalization and attenuation can compensate.",
            "The reconstructed profile and digitized published curves are not author-provided numerical tables; their uncertainty is distinct from numerical quadrature convergence.",
            "No fitted opacity rescaling or manual normalization is applied.",
        ],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "pure_vector_literature_benchmark.json"
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"acceptance": acceptance, "linked_hash_checks": linked_hash_checks,
                      "curves": [{k: x[k] for k in (
                          "mass_MeV", "mean_absolute_relative_difference_percent",
                          "maximum_absolute_relative_difference_percent")}
                                 for x in curve_rows]}, indent=2))
    if not acceptance["provenance_hash_links_pass"]:
        raise SystemExit("4B provenance/hash validation failed")


if __name__ == "__main__":
    main()
