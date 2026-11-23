#!/usr/bin/env python3
"""Reproducible runner for the current UV-EFT matching audit suite.

Run from any directory with Python 3 and SymPy installed:
    python /mnt/data/run_uv_eft_audit_suite.py

The runner executes only the listed audit programs, stores their stdout/stderr
and exit status in /mnt/data/uv_eft_audit_suite_output.txt, and prints a summary.
It does not perform UV-EFT subtraction or certify a physical Wilson coefficient.
"""
from pathlib import Path
import subprocess
import sys
import hashlib

ROOT = Path('/mnt/data')
SCRIPTS = [
    ('audit_chiral_path_structure.py', 'exact symbolic enumeration of 16 chiral projector patterns and H/C_ij/M'),
    ('audit_dirac_trace_numerator.py', 'explicit 4x4 gamma-matrix checks of four-/two-/zero-slash traces'),
    ('verify_numerator_to_B_kernel.py', 'symbolic reconstruction of f_ij, g, d_alpha and algebraic I-to-B conversion'),
    ('audit_minkowski_wick_signs.py', 'term-wise Wick factors and candidate B-kernel comparison'),
    ('audit_raw_minkowski_phase.py', 'common vertex/propagator/closed-loop phase ledger and conditional Wick ledger'),
    ('derive_raw_minkowski_numerator.py', 'explicit symbolic Dirac-matrix expansion of all 16 slash/mass numerator masks'),
    ('audit_model_vertex_trace_mapping.py', 'exact-rational direct trace vs H/C/M decomposition for all 16 paths in hshs and hhss, retaining epsilon term'),
]

out = []
out.append('UV-EFT AUDIT SUITE')
out.append(f'Python: {sys.version.split()[0]}')
out.append('Scope: bookkeeping/algebra audits only; not a complete amplitude or matching calculation.')
out.append('')
all_ok = True
for filename, purpose in SCRIPTS:
    path = ROOT / filename
    out.append(f'[{filename}]')
    out.append(f'Purpose: {purpose}')
    if not path.exists():
        all_ok = False
        out.append('STATUS: MISSING')
        out.append('')
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    proc = subprocess.run([sys.executable, str(path)], text=True, capture_output=True, cwd=str(ROOT))
    out.append(f'SHA256: {digest}')
    out.append(f'EXIT_CODE: {proc.returncode}')
    out.append('STDOUT:')
    out.append(proc.stdout.rstrip() or '(empty)')
    if proc.stderr.strip():
        out.append('STDERR:')
        out.append(proc.stderr.rstrip())
    if proc.returncode != 0:
        all_ok = False
    out.append('')
out.append(f'SUITE_STATUS: {"PASS" if all_ok else "FAIL"}')
out.append('Interpretation: PASS means all listed scripts ran successfully, not that their physical assumptions are all established.')
output = '\n'.join(out) + '\n'
report = ROOT / 'uv_eft_audit_suite_output.txt'
report.write_text(output, encoding='utf-8')
print(output)
print(f'WROTE: {report}')
if not all_ok:
    raise SystemExit(1)
