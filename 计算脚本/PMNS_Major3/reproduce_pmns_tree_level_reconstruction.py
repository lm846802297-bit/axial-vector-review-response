#!/usr/bin/env python3
"""Re-run the Major 3 tree-level seesaw construction and save provenance.

This wrapper runs the existing pmns_tree_level_reconstruction.py calculation,
preserves its complete JSON result, and records the source and runtime versions.
It performs no likelihood fit, parameter scan, or experimental-constraint check.

Run from any working directory with Python 3 and NumPy installed:
    python 计算脚本/PMNS_Major3/reproduce_pmns_tree_level_reconstruction.py
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
CALCULATION = HERE / "pmns_tree_level_reconstruction.py"
OUTPUT = HERE / "outputs" / "pmns_tree_level_reconstruction_2026-11-04.json"


def main() -> None:
    completed = subprocess.run(
        [sys.executable, str(CALCULATION)],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    result = json.loads(completed.stdout)
    result["reproducibility"] = {
        "calculation_script": CALCULATION.relative_to(REPO_ROOT).as_posix(),
        "calculation_script_sha256": hashlib.sha256(
            CALCULATION.read_bytes()
        ).hexdigest(),
        "runner_script": Path(__file__).resolve().relative_to(REPO_ROOT).as_posix(),
        "python_version": sys.version.split()[0],
        "numpy_version": np.__version__,
        "invocation": (
            "python 计算脚本/PMNS_Major3/"
            "reproduce_pmns_tree_level_reconstruction.py"
        ),
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(OUTPUT.relative_to(REPO_ROOT).as_posix())


if __name__ == "__main__":
    main()
