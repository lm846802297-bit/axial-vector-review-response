#!/usr/bin/env python3
"""Independent endpoint-quadrature audit for the exact-momentum pole driver.

The archived SciPy/QUADPACK implementation is re-run only to inventory its
four endpoint roundoff warnings. The production composite Gauss-Legendre
implementation is then checked against high-precision mpmath tanh-sinh at
those exact points and against order convergence of all six complex pole pairs.
"""
from __future__ import annotations
import cmath, hashlib, importlib.util, json, math, platform, warnings
from pathlib import Path
import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import IntegrationWarning, quad

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "exact_momentum_fermion_pole_audit.py"
OUTPUT = HERE / "pole_quadrature_independent_audit_2026-11-16.json"
ORDERS = (32, 48, 64, 96, 128)
BENCHMARKS = (("A", 70.886458, 10.0), ("B", 315.0, 63.0))
SINGLET_MASSES = (100.0, 125.25, 150.0)
HARD_REFERENCES = {"A": 0.024030443985870786, "B": 0.005407723994710553}

spec = importlib.util.spec_from_file_location("exact_momentum_driver", SOURCE)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot import {SOURCE}")
driver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver)
production_b0bar = driver.b0bar
source_sha256 = hashlib.sha256(SOURCE.read_bytes()).hexdigest()

def legacy_quad_b0bar(s, mi, mj, second=False):
    """The pre-repair QUADPACK implementation, retained for warning provenance."""
    s = complex(s)
    if abs(s.imag) < 1e-18 and s.real > 0.0:
        s += 1e-8j
    aa, bb, cc = s.real, mi * mi - mj * mj - s.real, mj * mj
    roots, disc = [], bb * bb - 4.0 * aa * cc
    if aa and disc >= 0.0:
        for x in ((-bb - math.sqrt(disc)) / (2.0 * aa), (-bb + math.sqrt(disc)) / (2.0 * aa)):
            if 0.0 < x < 1.0:
                roots.append(x)
    points = [0.0] + sorted(roots) + [1.0]
    def integrand(x):
        den = x * mi * mi + (1.0 - x) * mj * mj - x * (1.0 - x) * s
        return -cmath.log(den / (driver.MU * driver.MU))
    total = 0j
    for lo, hi in zip(points[:-1], points[1:]):
        for component in ("real", "imag"):
            fn = (lambda x: integrand(x).real) if component == "real" else (lambda x: integrand(x).imag)
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always", IntegrationWarning)
                value, error = quad(fn, lo, hi, epsabs=2e-9, epsrel=2e-9, limit=200)
            total += value if component == "real" else 1j * value
            for item in caught:
                warning_records.append({
                    "message": str(item.message).splitlines()[0], "component": component,
                    "s_re_GeV2": s.real, "s_im_GeV2": s.imag,
                    "mi_GeV": mi, "mj_GeV": mj, "second_sheet": bool(second),
                    "panel": [lo, hi], "quad_estimated_abs_error": error,
                })
    if second and s.imag < 0.0 and s.real > (mi + mj) ** 2:
        kallen = (s - (mi + mj) ** 2) * (s - (mi - mj) ** 2)
        total += 2j * math.pi * cmath.sqrt(kallen) / s
    return total

def mpmath_b0bar(s_re, s_im, mi, mj, dps):
    """High-precision tanh-sinh integral with explicit endpoint-layer panels."""
    mp.mp.dps = dps
    s = mp.mpc(repr(s_re), repr(s_im))
    mi_mp, mj_mp, mu_mp = mp.mpf(repr(mi)), mp.mpf(repr(mj)), mp.mpf(repr(driver.MU))
    def f(x):
        den = x * mi_mp**2 + (1 - x) * mj_mp**2 - x * (1 - x) * s
        return -mp.log(den / mu_mp**2)
    points = [mp.mpf("0"), mp.mpf("1")]
    if mi_mp > mj_mp and mi_mp:
        delta = (mj_mp / mi_mp) ** 2
        for k in range(-1, 15):
            x = delta * mp.power(10, k)
            if 0 < x < mp.mpf("0.1"):
                points.append(x)
    elif mj_mp > mi_mp and mj_mp:
        delta = (mi_mp / mj_mp) ** 2
        for k in range(-1, 15):
            x = 1 - delta * mp.power(10, k)
            if mp.mpf("0.9") < x < 1:
                points.append(x)
    points = sorted(set(points))
    total = mp.mpc(0)
    for lo, hi in zip(points[:-1], points[1:]):
        total += mp.quad(f, [lo, hi], method="tanh-sinh", maxdegree=8)
    return total

# Reproduce and locate the archived warning points.
warning_records = []
driver.b0bar = legacy_quad_b0bar
with warnings.catch_warnings():
    warnings.simplefilter("ignore", IntegrationWarning)
    for _name, vs, ma in BENCHMARKS:
        for ms in SINGLET_MASSES:
            driver.poles_and_residues(ms, vs, ma)
if len(warning_records) != 4:
    raise AssertionError(f"Expected four legacy warnings; found {len(warning_records)}")

# Compare each warning integral against mpmath and composite Gauss-Legendre.
warning_checks = []
for item in warning_records:
    mp_values = {str(dps): mpmath_b0bar(item["s_re_GeV2"], item["s_im_GeV2"], item["mi_GeV"], item["mj_GeV"], dps) for dps in (50, 70, 90)}
    driver.B0_GL_ORDER = 64
    driver.b0bar_cached.cache_clear()
    gl64 = production_b0bar(complex(item["s_re_GeV2"], item["s_im_GeV2"]), item["mi_GeV"], item["mj_GeV"], item["second_sheet"])
    driver.B0_GL_ORDER = 96
    driver.b0bar_cached.cache_clear()
    gl96 = production_b0bar(complex(item["s_re_GeV2"], item["s_im_GeV2"]), item["mi_GeV"], item["mj_GeV"], item["second_sheet"])
    ref = mp_values["90"]
    gl64_mp, gl96_mp = mp.mpc(repr(gl64.real), repr(gl64.imag)), mp.mpc(repr(gl96.real), repr(gl96.imag))
    warning_checks.append({
        **item,
        "mpmath_tanh_sinh": {k: {"re": mp.nstr(v.real, 28), "im": mp.nstr(v.imag, 28)} for k, v in mp_values.items()},
        "mpmath_dps_70_vs_90_abs": mp.nstr(abs(mp_values["70"] - ref), 8),
        "mpmath_dps_50_vs_90_abs": mp.nstr(abs(mp_values["50"] - ref), 8),
        "gauss_legendre_64": {"re": gl64.real, "im": gl64.imag},
        "gauss_legendre_96": {"re": gl96.real, "im": gl96.imag},
        "gauss64_vs_mpmath90_abs": float(abs(gl64_mp - ref)),
        "gauss96_vs_mpmath90_abs": float(abs(gl96_mp - ref)),
    })

# Recompute all six pole pairs with composite Gauss-Legendre at several orders.
driver.b0bar = production_b0bar
order_runs = []
for order in ORDERS:
    driver.B0_GL_ORDER = order
    driver.b0bar_cached.cache_clear()
    run = {"order": order, "hard_remainders_GeV2": {}, "pole_pairs": []}
    for name, vs, ma in BENCHMARKS:
        hard = driver.hard_momentum(vs, driver.MH * driver.MH, False)
        run["hard_remainders_GeV2"][name] = {"re": hard.real, "im": hard.imag}
        for ms in SINGLET_MASSES:
            rows = driver.poles_and_residues(ms, vs, ma)
            for index, row in enumerate(rows, start=1):
                run["pole_pairs"].append({
                    "benchmark": name, "vs_GeV": vs, "mA_GeV": ma,
                    "ms_input_GeV": ms, "pole_index": index,
                    "mass_GeV": float(row["mass"]), "width_GeV": float(row["width"]),
                    "R_hh_re": float(row["R_hh"].real), "R_hh_im": float(row["R_hh"].imag),
                    "determinant_residual_GeV4": float(row["residual"]),
                })
    order_runs.append(run)

by_order = {run["order"]: run for run in order_runs}
base = by_order[128]
convergence = {}
for order in ORDERS[:-1]:
    other = by_order[order]
    hard_delta = max(
        abs(other["hard_remainders_GeV2"][name][part] - base["hard_remainders_GeV2"][name][part])
        for name, _vs, _ma in BENCHMARKS for part in ("re", "im"))
    pairs = list(zip(base["pole_pairs"], other["pole_pairs"]))
    convergence[str(order)] = {
        "max_hard_remainder_complex_delta_GeV2_vs_128": hard_delta,
        "max_pole_mass_delta_GeV_vs_128": max(abs(a["mass_GeV"] - b["mass_GeV"]) for a, b in pairs),
        "max_pole_width_delta_GeV_vs_128": max(abs(a["width_GeV"] - b["width_GeV"]) for a, b in pairs),
        "max_R_hh_complex_delta_vs_128": max(abs(complex(a["R_hh_re"], a["R_hh_im"]) - complex(b["R_hh_re"], b["R_hh_im"])) for a, b in pairs),
    }

hard_checks = {}
for name in HARD_REFERENCES:
    value = base["hard_remainders_GeV2"][name]
    hard_checks[name] = {
        "computed_re_GeV2": value["re"], "computed_im_GeV2": value["im"],
        "archived_re_GeV2": HARD_REFERENCES[name],
        "abs_real_delta_GeV2": abs(value["re"] - HARD_REFERENCES[name]),
    }
max_residual = max(p["determinant_residual_GeV4"] for p in base["pole_pairs"])
max_residue_sum_delta = 0.0
for name, _vs, _ma in BENCHMARKS:
    for ms in SINGLET_MASSES:
        subset = [p for p in base["pole_pairs"] if p["benchmark"] == name and p["ms_input_GeV"] == ms]
        sum_r = sum(complex(p["R_hh_re"], p["R_hh_im"]) for p in subset)
        max_residue_sum_delta = max(max_residue_sum_delta, abs(sum_r - 1.0))

assert max_residual < 1e-7
assert max_residue_sum_delta < 3e-5
assert all(v["max_pole_mass_delta_GeV_vs_128"] < 1e-10 for v in convergence.values())
assert all(v["max_pole_width_delta_GeV_vs_128"] < 1e-10 for v in convergence.values())
assert all(v["max_R_hh_complex_delta_vs_128"] < 2e-8 for v in convergence.values())
assert all(v["abs_real_delta_GeV2"] < 2e-12 for v in hard_checks.values())
assert all(v["gauss96_vs_mpmath90_abs"] < 1e-12 for v in warning_checks)

result = {
    "purpose": "Independent numerical quadrature audit; does not complete the physical UV propagator or pole prediction.",
    "source": SOURCE.name, "source_sha256": source_sha256,
    "runtime": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__, "mpmath": mp.__version__},
    "benchmarks": [{"name": name, "vs_GeV": vs, "mA_GeV": ma} for name, vs, ma in BENCHMARKS],
    "singlet_masses_GeV": SINGLET_MASSES,
    "legacy_quad_warning_count": len(warning_records),
    "legacy_warning_integrals": [{
        "mi_GeV": w["mi_GeV"], "mj_GeV": w["mj_GeV"],
        "s_re_GeV2": w["s_re_GeV2"], "s_im_GeV2": w["s_im_GeV2"],
        "quad_estimated_abs_error": w["quad_estimated_abs_error"],
        "mpmath90_re": w["mpmath_tanh_sinh"]["90"]["re"],
        "mpmath90_im": w["mpmath_tanh_sinh"]["90"]["im"],
        "mpmath_dps50_vs90_abs": w["mpmath_dps_50_vs_90_abs"],
        "mpmath_dps70_vs90_abs": w["mpmath_dps_70_vs_90_abs"],
        "gauss64_vs_mpmath90_abs": w["gauss64_vs_mpmath90_abs"],
        "gauss96_vs_mpmath90_abs": w["gauss96_vs_mpmath90_abs"],
    } for w in warning_checks],
    "production_order": 64, "gauss_legendre_orders": ORDERS,
    "order_convergence_vs_128": convergence,
    "production_order_64_pole_pairs": by_order[64]["pole_pairs"],
    "hard_coefficient_checks": hard_checks,
    "n128_max_determinant_residual_GeV4": max_residual,
    "n128_max_h_channel_residue_sum_delta": max_residue_sum_delta,
    "interpretation": "The four archived QUADPACK warnings are reproduced and localized to the 20 TeV--muon heavy-light endpoint layer. Composite Gauss-Legendre with geometric endpoint panels converges across orders 32--128; the four flagged integrals agree with independent high-precision mpmath tanh-sinh. The exact-momentum numerical quadrature warning is closed for this declared fermion-sector benchmark and mass grid. This does not validate the incomplete physical pole model, fixed diagonal widths, missing counterterms/gauge sectors, or collider observables.",
}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "output": str(OUTPUT), "source_sha256": source_sha256,
    "legacy_warnings": len(warning_records),
    "warning_checks": [{"mi": x["mi_GeV"], "mj": x["mj_GeV"], "s_re": x["s_re_GeV2"], "s_im": x["s_im_GeV2"], "gauss96_vs_mpmath90_abs": x["gauss96_vs_mpmath90_abs"]} for x in warning_checks],
    "convergence_vs_128": convergence, "hard_checks": hard_checks,
    "max_residual": max_residual, "max_residue_sum_delta": max_residue_sum_delta,
}, indent=2))
