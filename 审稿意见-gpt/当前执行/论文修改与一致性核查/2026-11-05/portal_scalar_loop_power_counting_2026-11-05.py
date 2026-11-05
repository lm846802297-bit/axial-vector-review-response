#!/usr/bin/env python3
"""P2-lite diagnostic: CP-even scalar-potential bubbles induced by the matched UV portal.

Scope:
- Uses the two Plan-C-lite VLL-threshold benchmarks.
- Uses the matched-reference diagonal propagators with m_h and the unmixed m_s.
- Computes only the CP-even radial (h,s) scalar-bubble subset.
- Subtracts each bubble at p^2=0 to remove its local constant.
- Does NOT claim a complete two-loop UV-EFT matching or a gauge-independent pole result.

The overall sign depends on the self-energy convention; the script reports magnitudes.
Only the Python standard library is required.
"""
from __future__ import annotations

from math import atan, log, pi, sqrt

MH = 125.25
VH = 246.22
ME = 20_000.0
THETA_L = 1.0e-2
GAMMA_H = 0.00407  # GeV
M_LEPTON = {"mu": 0.1056583755, "tau": 1.77686}
BENCHMARKS = (
    ("A_open_AA", sqrt(2.0) * M_LEPTON["tau"] / (THETA_L * sqrt(4.0 * pi)), 10.0),
    ("B_closed_AA", 315.0, 63.0),
)
PI_RET = {
    "A_open_AA": complex(-0.413277859, -0.113173709),
    "B_closed_AA": complex(-0.093002551, -0.025468201),
}


def simpson(function, n: int) -> float:
    """Composite Simpson integration on [0,1]."""
    if n <= 0:
        raise ValueError("n must be positive")
    if n % 2:
        n += 1
    h = 1.0 / n
    total = function(0.0) + function(1.0)
    total += 4.0 * sum(function(i * h) for i in range(1, n, 2))
    total += 2.0 * sum(function(i * h) for i in range(2, n, 2))
    return total * h / 3.0


def delta_b0(p2: float, mi: float, mj: float, n: int = 8000) -> float:
    r"""Return B0(p2;mi^2,mj^2)-B0(0;mi^2,mj^2).

    B0 is defined by -int_0^1 dx log([x mi^2+(1-x)mj^2-x(1-x)p2-i0]/mu^2).
    The selected points are below all CP-even two-scalar thresholds, so the
    difference is real and is evaluated as -int log1p[-x(1-x)p2/D0].
    """
    if p2 < 0.0 or mi <= 0.0 or mj <= 0.0:
        raise ValueError("This diagnostic expects p2>=0 and positive scalar masses.")

    def integrand(x: float) -> float:
        d0 = x * mi * mi + (1.0 - x) * mj * mj
        z = x * (1.0 - x) * p2 / d0
        if z >= 1.0:
            raise ValueError("A two-scalar cut is open; use the complex B0 routine.")
        return -log(1.0 - z)

    return simpson(integrand, n)



def delta_b0_closed(p2: float, mi: float, mj: float) -> float:
    r"""Closed form for B0(p2;mi^2,mj^2)-B0(0;mi^2,mj^2).

    The selected benchmark kinematics satisfy the sub-threshold condition
    lambda_K=(p2-mi^2-mj^2)^2-4 mi^2 mj^2 < 0, so the result is real.
    The arbitrary reference scale mu^2 cancels between the two terms.
    """
    if p2 <= 0.0 or mi <= 0.0 or mj <= 0.0:
        raise ValueError("Require p2>0 and positive internal masses.")
    a, b = mi * mi, mj * mj
    scale = max(a, b)

    # Equal-mass limit: a numerically stable elementary expression.
    if abs(a - b) <= 1.0e-12 * scale:
        z = p2 / (4.0 * a)
        if not 0.0 < z < 1.0:
            raise ValueError("Equal-mass point is not below its two-particle threshold.")
        return 2.0 - 2.0 * sqrt((1.0 - z) / z) * atan(
            sqrt(z / (1.0 - z))
        )

    lam_k = (p2 - a - b) ** 2 - 4.0 * a * b
    if lam_k >= 0.0:
        raise ValueError("Closed real branch requires lambda_K<0.")
    q = sqrt(-lam_k) / (2.0 * p2)
    t0 = (a - b - p2) / (2.0 * p2)
    t1 = t0 + 1.0
    mu2 = 1.0  # arbitrary reference scale squared; it cancels exactly

    def primitive(t: float) -> float:
        return (
            t * log(p2 * (t * t + q * q) / mu2)
            - 2.0 * t
            + 2.0 * q * __import__("math").atan(t / q)
        )

    i0 = (a * log(a / mu2) - b * log(b / mu2)) / (a - b) - 1.0
    return i0 - (primitive(t1) - primitive(t0))

def coupling_inputs(vs: float) -> tuple[float, float]:
    """Return lambda_HS^UV=-Delta lambda_HS^E and lambda_H."""
    y = {name: sqrt(2.0) * ME * THETA_L / VH for name in M_LEPTON}
    theta_r = {name: mass / (ME * THETA_L) for name, mass in M_LEPTON.items()}
    lam = {name: sqrt(2.0) * ME * theta_r[name] / vs for name in M_LEPTON}
    products = {name: y[name] * lam[name] for name in M_LEPTON}
    delta_lambda = -sum(value * value for value in products.values()) / (8.0 * pi**2)
    return -delta_lambda, MH**2 / (2.0 * VH**2)


def scalar_width(ms: float, vs: float, ma: float) -> float:
    """Plan-C-lite diagonal width, used only in the isolated-pole diagnostic."""
    width = 0.0
    if ms > 2.0 * ma:
        x = ma * ma / (ms * ms)
        width += (
            ms**3 / (32.0 * pi * vs**2)
            * (1.0 - 4.0 * x + 12.0 * x * x)
            * sqrt(1.0 - 4.0 * x)
        )
    for mass in M_LEPTON.values():
        if ms > 2.0 * mass:
            width += (
                mass**2 * ms / (8.0 * pi * vs**2)
                * (1.0 - 4.0 * mass**2 / ms**2) ** 1.5
            )
    return width


def cp_even_bubble_subset(vs: float, ms: float, lam_hs: float, lam_h: float) -> dict:
    r"""Compute |Delta Pi_hs| from the CP-even radial scalar bubbles.

    Cubic potential derivatives:
      g_hhh = 6 lambda_H v_h
      g_sss = 6 lambda_S v_s
      g_hhs = lambda_HS v_s
      g_hss = lambda_HS v_h

    DeltaPi = 1/(32 pi^2) [
        g_hhh*g_hhs*DeltaB_hh
      + g_hss*g_sss*DeltaB_ss
      + 2*g_hhs*g_hss*DeltaB_hs
    ].
    """
    lam_s = ms**2 / (2.0 * vs**2)
    g_hhh = 6.0 * lam_h * VH
    g_sss = 6.0 * lam_s * vs
    g_hhs = lam_hs * vs
    g_hss = lam_hs * VH

    db_hh = delta_b0_closed(MH**2, MH, MH)
    db_ss = delta_b0_closed(MH**2, ms, ms)
    db_hs = delta_b0_closed(MH**2, MH, ms)

    prefactor = 1.0 / (32.0 * pi**2)
    terms = {
        "hh": prefactor * g_hhh * g_hhs * db_hh,
        "ss": prefactor * g_hss * g_sss * db_ss,
        "hs": prefactor * 2.0 * g_hhs * g_hss * db_hs,
    }
    total = sum(terms.values())
    return {
        "lambda_s": lam_s,
        "g_hhh": g_hhh,
        "g_sss": g_sss,
        "g_hhs": g_hhs,
        "g_hss": g_hss,
        "delta_b0_hh": db_hh,
        "delta_b0_ss": db_ss,
        "delta_b0_hs": db_hs,
        "terms": terms,
        "delta_pi_abs": abs(total),
    }


def main() -> None:
    print("P2-lite CP-even scalar-potential bubble diagnostic")
    print("Convention: magnitudes only; no addition to the retained fermion self-energy.")
    print(f"m_h={MH:.5f} GeV, v_h={VH:.5f} GeV, M_E={ME:.1f} GeV")
    print("The UV portal is fixed by lambda_HS^EFT(M_E)=0 and the leading VLL threshold.")
    print()

    for name, vs, ma in BENCHMARKS:
        lam_hs, lam_h = coupling_inputs(vs)
        print(f"BENCHMARK {name}: v_s={vs:.9f} GeV, m_A'={ma:.6g} GeV")
        print(f"  lambda_HS^UV={lam_hs:.12g}; lambda_H={lam_h:.12g}")
        for ms in (100.0, MH):
            result = cp_even_bubble_subset(vs, ms, lam_hs, lam_h)
            width = scalar_width(ms, vs, ma)
            pi_ret = PI_RET[name]
            ratio_to_ret = result["delta_pi_abs"] / abs(pi_ret)
            a = complex(MH**2, -MH * GAMMA_H)
            b = complex(ms**2, -ms * width)
            eta = result["delta_pi_abs"] / abs(a - b)
            print(f"  m_s={ms:.5f} GeV; lambda_S={result['lambda_s']:.9g}; Gamma_s={width:.9g} GeV")
            print(
                "    DeltaB0(hh,ss,hs)="
                f"({result['delta_b0_hh']:.12g}, "
                f"{result['delta_b0_ss']:.12g}, "
                f"{result['delta_b0_hs']:.12g})"
            )
            print(
                "    |terms(hh,ss,hs)| [GeV^2]="
                f"({result['terms']['hh']:.9g}, "
                f"{result['terms']['ss']:.9g}, "
                f"{result['terms']['hs']:.9g})"
            )
            print(f"    |DeltaPi_CP-even subset|={result['delta_pi_abs']:.9g} GeV^2")
            print(f"    ratio to |Pi_hs^ret|={ratio_to_ret:.9g}")
            print(f"    isolated-pole eta_subset={eta:.9g}; eta^2={eta**2:.9g}")
        print()

    # Cross-check the closed forms against Simpson integration at every
    # benchmark/m_s point and for all hh, ss, and hs bubble topologies.
    max_relative_error = 0.0
    for name, vs, ma in BENCHMARKS:
        for ms in (100.0, MH):
            pairs = (("hh", MH, MH), ("ss", ms, ms), ("hs", MH, ms))
            for label, mi, mj in pairs:
                analytic = delta_b0_closed(MH**2, mi, mj)
                numeric = delta_b0(MH**2, mi, mj, 8000)
                relative_error = abs(analytic - numeric) / abs(analytic)
                max_relative_error = max(max_relative_error, relative_error)
                print(
                    f"CROSS-CHECK {name} m_s={ms:.5f} {label}: "
                    f"closed={analytic:.14g}, Simpson={numeric:.14g}, "
                    f"relative_error={relative_error:.3e}"
                )

    # Simpson convergence at every distinct mass pair.
    checked_pairs = set()
    for _, _, _ in BENCHMARKS:
        for ms in (100.0, MH):
            for mi, mj in ((MH, MH), (ms, ms), (MH, ms)):
                checked_pairs.add((mi, mj))
    for mi, mj in sorted(checked_pairs):
        vals = [delta_b0(MH**2, mi, mj, n) for n in (2000, 4000, 8000, 16000)]
        assert abs(vals[-1] - vals[-2]) < 1.0e-12
    assert max_relative_error < 1.0e-11
    print(f"CHECKS: Simpson convergence passed; max closed-vs-Simpson relative error={max_relative_error:.3e}.")
    print("SCOPE: CP-even radial scalar subset only; not a complete matched two-loop pole result.")


if __name__ == "__main__":
    main()
