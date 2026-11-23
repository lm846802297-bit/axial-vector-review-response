#!/usr/bin/env python3
"""Check on-shell invariant projection and h/s-leg symmetry of the integrated kernels.

Reads the reproducible 576-row CSV emitted by RC-001-six-cycle-simplex-integration.py.
On shell, Q1=Q2=Q3=0, Q4=t_R/2, Q5=s_R/2, Q6=u_R/2. For a physically
consistent exact mass/angle benchmark satisfying M11=0, the complete six-cycle
candidate sum must be symmetric under s1 <-> s2, hence the summed Q5 and Q6
coefficients must agree. This is a finite-mass candidate-kernel consistency test,
not a dimensionally regulated UV-EFT matching test.
Requires Python 3 + SymPy.
"""
import csv, os
from pathlib import Path
import sympy as sp

src=Path(os.environ.get("RC001_INTEGRATED_CSV","/tmp/rc001_run/RC-001-six-cycle-integrated-candidate-kernel-ledger.csv"))
if not src.is_file():
    raise FileNotFoundError(f"Integrated candidate-kernel CSV not found: {src}. Run RC-001-six-cycle-simplex-integration.py first or set RC001_INTEGRATED_CSV.")
with src.open(newline="",encoding="utf-8") as f:
    rows=list(csv.DictReader(f))
if len(rows)!=576: raise AssertionError(f"expected 576 integrated rows, found {len(rows)}")

names=("a","b","c_L","c_R","s_L","s_R","m_1","m_2")
sym={name:sp.Symbol(name) for name in names}
locals_map={"hyper":sp.hyper,**sym}
benchmark={
    sym["a"]:sp.Rational(2,7), sym["b"]:sp.Rational(3,11),
    sym["c_L"]:sp.Rational(12,13), sym["s_L"]:sp.Rational(5,13),
    sym["c_R"]:sp.Rational(12,13), sym["s_R"]:sp.Rational(5,13),
    sym["m_1"]:sp.Integer(1), sym["m_2"]:sp.Rational(144,25),
}
# Exact M11=0 constraint: -cL*cR*m1 + m2*sL*sR = 0.
constraint=sp.simplify(-benchmark[sym["c_L"]]*benchmark[sym["c_R"]]*benchmark[sym["m_1"]]
                       +benchmark[sym["m_2"]]*benchmark[sym["s_L"]]*benchmark[sym["s_R"]])
if constraint!=0: raise AssertionError(f"benchmark violates M11=0: {constraint}")
print("PASS: exact rational benchmark satisfies the triangular mass-matrix M11=0 constraint.")

sums={}
for alpha in (5,6):
    subset=[r for r in rows if int(r["alpha"])==alpha]
    if len(subset)!=96: raise AssertionError(f"alpha={alpha}: expected 96 cycle/path rows, got {len(subset)}")
    total=sp.Integer(0)
    for r in subset:
        total += sp.sympify(r["Gamma4_times_integrated_candidate_kernel"],locals=locals_map)
    sums[alpha]=sp.factor(total.subs(benchmark))
    print(f"PASS: aggregated alpha={alpha} from {len(subset)} rows (6 cycles x 16 paths).")

check=sp.simplify(sums[5]-sums[6])
if check!=0: raise AssertionError(f"on-shell s_R/u_R coefficient mismatch: {check}")
print("PASS: complete six-cycle finite-mass candidate sum has equal Q5/Q6 coefficients at the exact benchmark.")
print(f"BENCHMARK: sum(Q5) = {sp.N(sums[5],18)}")
print(f"BENCHMARK: sum(Q6) = {sp.N(sums[6],18)}")
print("ON-SHELL MAP: Q1=Q2=Q3=0; Q4=t_R/2; Q5=s_R/2; Q6=u_R/2.")
print("LIMIT: this verifies s1<->s2 symmetry of the integrated candidate kernels at one exact physical mass/angle point; it does not compare the finite-mass result to the dimensionally regulated hard Wilson coefficient or EFT soft subtraction.")
