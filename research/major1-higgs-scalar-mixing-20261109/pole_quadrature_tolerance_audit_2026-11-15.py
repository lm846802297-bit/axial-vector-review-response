#!/usr/bin/env python3
"""Reproduce the pre-repair SciPy tolerance scan from its immutable source.

This is a historical diagnostic. It intentionally retrieves the archived
QUADPACK-based driver from SOURCE_COMMIT rather than the current repaired
composite Gauss-Legendre implementation.
"""
from __future__ import annotations
import hashlib, importlib.util, json, platform, subprocess, tempfile, warnings
from pathlib import Path
import numpy, scipy
from scipy.integrate import IntegrationWarning

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE_RELATIVE = Path("research/major1-higgs-scalar-mixing-20261109/exact_momentum_fermion_pole_audit.py")
SOURCE_COMMIT = "5522ae1081f61a711fc846168370542efdef9a35"
EXPECTED_SOURCE_SHA256 = "e391afbc3b2f75305a3f31209aac209b3aa4f1104cd0f13c68f0159064b08246"
OUTPUT = HERE / "pole_quadrature_tolerance_audit_2026-11-15.json"
TOLERANCES = ("2e-8", "2e-9", "2e-10")
BENCHMARKS = (("A", 70.886458, 10.0), ("B", 315.0, 63.0))
SINGLET_MASSES = (100.0, 125.25, 150.0)

source_text = subprocess.check_output(
    ["git", "show", f"{SOURCE_COMMIT}:{SOURCE_RELATIVE.as_posix()}"],
    cwd=ROOT, text=True, encoding="utf-8")
source_sha256 = hashlib.sha256(source_text.encode("utf-8")).hexdigest()
if source_sha256 != EXPECTED_SOURCE_SHA256:
    raise RuntimeError(f"Archived source checksum mismatch: {source_sha256}")
all_runs = []
for tolerance in TOLERANCES:
    old = "epsabs=2e-9,epsrel=2e-9"
    if source_text.count(old) != 2:
        raise RuntimeError("Expected exactly two archived quadrature settings")
    variant = source_text.replace(old, f"epsabs={tolerance},epsrel={tolerance}")
    with tempfile.TemporaryDirectory(prefix="pole-tolerance-") as temp_dir:
        module_path = Path(temp_dir) / "pole_driver_variant.py"
        module_path.write_text(variant, encoding="utf-8")
        spec = importlib.util.spec_from_file_location(f"pole_variant_{tolerance}", module_path)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        poles = []
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always", IntegrationWarning)
            for benchmark, vs, ma in BENCHMARKS:
                for ms in SINGLET_MASSES:
                    for index, row in enumerate(module.poles_and_residues(ms, vs, ma), start=1):
                        poles.append({
                            "benchmark": benchmark, "vs_GeV": vs, "mA_GeV": ma,
                            "ms_input_GeV": ms, "pole_index": index,
                            "mass_GeV": float(row["mass"]), "width_GeV": float(row["width"]),
                            "R_hh_re": float(row["R_hh"].real), "R_hh_im": float(row["R_hh"].imag),
                            "determinant_residual_GeV4": float(row["residual"]),
                        })
        messages = [str(w.message).splitlines()[0] for w in caught]
        all_runs.append({"epsabs": tolerance, "epsrel": tolerance,
                         "integration_warning_count": len(messages),
                         "warning_messages": messages, "poles": poles})

base = all_runs[1]["poles"]
for run in (all_runs[0], all_runs[2]):
    other = run["poles"]
    run["max_abs_delta_vs_2e-9"] = {
        "mass_GeV": max(abs(a["mass_GeV"] - b["mass_GeV"]) for a, b in zip(base, other)),
        "width_GeV": max(abs(a["width_GeV"] - b["width_GeV"]) for a, b in zip(base, other)),
        "R_hh_complex": max(abs(complex(a["R_hh_re"], a["R_hh_im"]) - complex(b["R_hh_re"], b["R_hh_im"])) for a, b in zip(base, other)),
    }

result = {
    "purpose": "Historical pre-repair SciPy tolerance diagnostic; not current production code or pole-physics validation.",
    "command": "python research/major1-higgs-scalar-mixing-20261109/pole_quadrature_tolerance_audit_2026-11-15.py",
    "input_source": f"{SOURCE_COMMIT}:{SOURCE_RELATIVE.as_posix()}",
    "input_source_sha256": source_sha256,
    "runtime": {"python": platform.python_version(), "numpy": numpy.__version__, "scipy": scipy.__version__},
    "benchmarks": [{"name": name, "vs_GeV": vs, "mA_GeV": ma} for name, vs, ma in BENCHMARKS],
    "singlet_masses_GeV": SINGLET_MASSES,
    "runs": all_runs,
    "interpretation": "The archived QUADPACK driver emits four IntegrationWarnings at all three requested tolerances. This historical result motivated the independent composite Gauss-Legendre and mpmath tanh-sinh repair recorded in pole_quadrature_independent_audit_2026-11-16.md/json. Do not treat this scan as the current production calculation.",
}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"output": str(OUTPUT), "source_commit": SOURCE_COMMIT,
                  "source_sha256": source_sha256,
                  "runs": [{"tolerance": r["epsabs"], "warnings": r["integration_warning_count"],
                            "max_delta_vs_2e-9": r.get("max_abs_delta_vs_2e-9")} for r in all_runs]}, indent=2))
