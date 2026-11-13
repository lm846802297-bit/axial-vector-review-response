#!/usr/bin/env python3
"""Run explicit software/reference checks for the stellar-cooling review package.

This script validates code and saved outputs only. It does not regenerate scans,
modify figures, or change any physical input.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

CALC = Path(__file__).resolve().parent
REPO = CALC.parents[1]
LITERATURE = REPO / "research" / "stellar-cooling-eft-literature-20261105"
BLINOV = CALC / "blinov_reproduction"
FINITE = CALC / "finite_mixing"
THERMAL = FINITE / "thermal_integrals"
OUT = CALC / "outputs" / "review_package_validation_2026-11-13"
OUT.mkdir(parents=True, exist_ok=True)


def make_env(paths: list[Path]) -> dict[str, str]:
    env = os.environ.copy()
    entries = [str(p.resolve()) for p in paths]
    if env.get("PYTHONPATH"):
        entries.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(entries)
    return env


def run_tests(name: str, modules: list[str], cwd: Path, paths: list[Path]) -> dict:
    proc = subprocess.run(
        [sys.executable, "-m", "unittest", *modules, "-v"],
        cwd=cwd,
        env=make_env(paths),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    log_name = f"{name}.log"
    (OUT / log_name).write_text(proc.stdout, encoding="utf-8")
    match = re.search(r"Ran (\d+) tests? in ([0-9.]+)s", proc.stdout)
    count = int(match.group(1)) if match else None
    seconds = float(match.group(2)) if match else None
    return {
        "name": name,
        "return_code": proc.returncode,
        "tests": count,
        "seconds": seconds,
        "passed": proc.returncode == 0 and count is not None and "OK" in proc.stdout,
        "log": f"research/stellar-cooling-constraints-20261105/outputs/review_package_validation_2026-11-13/{log_name}",
    }


core_modules = [
    "test_rates", "test_stage1_detailed_balance", "test_transport",
    "test_vector_reference", "test_direct_collision_integrals",
    "test_fig7_digitization_geometry", "test_profile_12_15km",
]
blinov_modules = [
    "test_reference", "test_b13_global_transport", "test_b13_nonrelativistic_muon",
    "test_b16_b1_independent", "test_b16_b1b2_full_independent",
    "test_b16_dense_local_kernel", "test_b16_directional_escape_8_15",
    "test_b16_emission_radius_escape", "test_b16_escape_phase_space",
    "test_b16_flavour_redshift_comparison", "test_b16_global_redshift",
    "test_b16_inner_path_channel_directional", "test_b16_local_absorption",
    "test_b16_neutrino_flavour_opacity", "test_b16_neutrino_inverse_decay",
    "test_b16_numu_profile_sensitivity", "test_b16_outer_escape_angular_distribution",
    "test_b16_outer_profile_inputs", "test_b16_outer_shell_polarization_resolved",
]
moving_modules = [
    "test_b13_b16_comparison", "test_b13_b16_mass_scan", "test_mixed_rates",
    "test_model", "test_response_scan", "test_thermal_rates",
    "thermal_integrals.test_dimuon", "thermal_integrals.test_moving_compton",
    "thermal_integrals.test_vector_longitudinal_projector",
    "thermal_integrals.test_vector_semicompton_polarization",
]

suites = [
    run_tests("core_production_profile_tests", core_modules, CALC,
              [CALC, BLINOV, FINITE, THERMAL, LITERATURE]),
    run_tests("independent_blinov_b13_b16_tests", blinov_modules, BLINOV,
              [BLINOV, FINITE, THERMAL, LITERATURE]),
    run_tests("moving_muon_finite_mixing_tests", moving_modules, FINITE,
              [CALC, FINITE, THERMAL, LITERATURE]),
]

validate = subprocess.run(
    [sys.executable, str(CALC / "validate_outputs.py")],
    cwd=REPO,
    env=make_env([CALC, BLINOV, FINITE, THERMAL, LITERATURE]),
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    check=False,
)
(OUT / "validate_outputs.log").write_text(validate.stdout, encoding="utf-8")
validate_payload = None
try:
    start = validate.stdout.index("{")
    end = validate.stdout.index("}\n", start) + 1
    validate_payload = json.loads(validate.stdout[start:end])
except Exception:
    pass

literature_output = OUT / "literature_kernel_validation_reproduced_2026-11-13.json"
literature = subprocess.run(
    [
        sys.executable,
        str(LITERATURE / "check_literature_kernels.py"),
        "--matrix-script", str(LITERATURE / "reference_matrix_element.py"),
        "--output", str(literature_output),
    ],
    cwd=REPO,
    env=make_env([CALC, BLINOV, FINITE, THERMAL, LITERATURE]),
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    check=False,
)
(OUT / "literature_kernel_validation.log").write_text(literature.stdout, encoding="utf-8")
literature_payload = json.loads(literature_output.read_text(encoding="utf-8")) if literature_output.exists() else None

def current_git_head() -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=REPO, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True,
        )
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


summary = {
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "purpose": "Independent software and saved-output validation; no scan or figure regeneration",
    "package_source_baseline": "81d9b2faf16eb39879b759b05afce46732c925d7",
    "execution_tree_commit": current_git_head(),
    "execution_tree_matches_package_baseline": current_git_head() == "81d9b2faf16eb39879b759b05afce46732c925d7",
    "python": sys.version,
    "test_suites": suites,
    "targeted_test_count": sum(s["tests"] or 0 for s in suites),
    "all_targeted_tests_passed": all(s["passed"] for s in suites),
    "validate_outputs_return_code": validate.returncode,
    "validate_outputs_summary": validate_payload,
    "literature_kernel_return_code": literature.returncode,
    "literature_kernel_summary": {
        "comparison_count": literature_payload.get("comparison_count") if literature_payload else None,
        "maximum_relative_error": literature_payload.get("maximum_relative_error") if literature_payload else None,
        "comparison_passed": literature_payload.get("comparison_passed") if literature_payload else False,
        "reference_sha256": literature_payload.get("reference_sha256") if literature_payload else None,
    },
    "known_nonstandard_json_artifact": "research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/p1iii_eos_kernel_self_test_2026-11-11.json; preserved byte-for-byte and flagged in JSON_FORMAT_AUDIT.csv; not consumed by the plotted axial scan",
    "scope_limit": "The complete recursive discovery also enters supplemental EOS/C4 test modules and exceeded a 120-second local execution budget. The three explicit targeted suites above are the acceptance set recorded here.",
    "scientific_gate": "Pure-vector Blinov Fig. 7 10-MeV strong-absorption comparison remains NOT PASSED (about +92.24%); this validation does not promote the plot to a final SN1987A exclusion.",
}
(OUT / "validation_summary.json").write_text(
    json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)

success = (
    summary["all_targeted_tests_passed"]
    and validate.returncode == 0
    and literature.returncode == 0
    and bool(literature_payload and literature_payload.get("comparison_passed"))
)
print(json.dumps({
    "success": success,
    "targeted_test_count": summary["targeted_test_count"],
    "test_suites": [{"name": s["name"], "tests": s["tests"], "passed": s["passed"]} for s in suites],
    "validate_outputs_return_code": validate.returncode,
    "literature_kernel_comparison_count": literature_payload.get("comparison_count") if literature_payload else None,
    "literature_kernel_maximum_relative_error": literature_payload.get("maximum_relative_error") if literature_payload else None,
    "output_directory": str(OUT),
}, indent=2))
if not success:
    raise SystemExit(1)
