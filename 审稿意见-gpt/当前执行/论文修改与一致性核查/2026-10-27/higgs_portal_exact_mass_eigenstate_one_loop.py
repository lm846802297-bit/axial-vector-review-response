#!/usr/bin/env python3
"""Independent one-loop h-s self-energy check in the exact mass-eigenstate basis.

Dependencies: Python 3, NumPy, SciPy.
Conventions follow RC-001:
  Gamma_inv = p^2 I - M_loc^2 + Pi_RC,
  A0bar(m^2)=m^2[1-ln(m^2/mu^2)],
  B0bar=-int_0^1 dx ln([x m_i^2+(1-x)m_j^2-x(1-x)p^2-i0]/mu^2).
The Plan-B convention is Pi_B=-Pi_RC.
"""
from math import log, pi, sqrt
import numpy as np
from scipy.integrate import quad

MH = 125.25
VH = 246.22
ME = 20_000.0
THETA_L = 1.0e-2
MU_R = ME
LEPTONS = {"mu": 0.1056583755, "tau": 1.77686}
BENCHMARKS = [
    ("A_open_AA", 70.886458, 10.0),
    ("B_closed_AA", 315.0, 63.0),
]


def a0bar(m, mu):
    return m*m*(1.0-log(m*m/(mu*mu))) if m else 0.0


def b0bar(s, mi, mj, mu):
    """Finite B0 with +i*pi*beta absorptive part above a two-particle cut."""
    roots = []
    if s > 0:
        disc = (mi*mi-mj*mj-s)**2 - 4*s*mj*mj
        if disc >= 0:
            for z in np.roots([s, mi*mi-mj*mj-s, mj*mj]):
                if abs(z.imag) < 1e-10 and 0.0 < z.real < 1.0:
                    roots.append(float(z.real))
    points = sorted([0.0, *roots, 1.0])
    real_part = 0.0
    negative_intervals = []

    for lo, hi in zip(points[:-1], points[1:]):
        mid = 0.5*(lo+hi)
        dmid = mid*mi*mi+(1-mid)*mj*mj-mid*(1-mid)*s
        if dmid < 0:
            negative_intervals.append((lo, hi))

        def integrate_segment(a, b, root_left=False, root_right=False):
            if root_left and root_right:
                m = 0.5*(a+b)
                return (integrate_segment(a, m, True, False)
                        + integrate_segment(m, b, False, True))
            if root_left:
                length = b-a
                def f(t):
                    if t == 0.0:
                        return 0.0
                    x = a+length*t*t
                    D = x*mi*mi+(1-x)*mj*mj-x*(1-x)*s
                    return -log(abs(D)/(mu*mu))*2*length*t
                return quad(f, 0.0, 1.0, epsabs=2e-10, epsrel=2e-10, limit=300)[0]
            if root_right:
                length = b-a
                def f(t):
                    if t == 0.0:
                        return 0.0
                    x = b-length*t*t
                    D = x*mi*mi+(1-x)*mj*mj-x*(1-x)*s
                    return -log(abs(D)/(mu*mu))*2*length*t
                return quad(f, 0.0, 1.0, epsabs=2e-10, epsrel=2e-10, limit=300)[0]
            def f(x):
                D = x*mi*mi+(1-x)*mj*mj-x*(1-x)*s
                return -log(abs(D)/(mu*mu))
            return quad(f, a, b, epsabs=2e-10, epsrel=2e-10, limit=300)[0]

        root_left = any(abs(lo-r) < 1e-9 for r in roots)
        root_right = any(abs(hi-r) < 1e-9 for r in roots)
        real_part += integrate_segment(lo, hi, root_left, root_right)

    imag_part = pi*sum(hi-lo for lo, hi in negative_intervals)
    return complex(real_part, imag_part)


def mass_eigenstate_data(vs, ml):
    # Leading-seesaw benchmark inputs, then exact SVD of the full mass matrix.
    theta_r = ml/(ME*THETA_L)
    y = sqrt(2)*ME*THETA_L/VH
    lam = sqrt(2)*ME*theta_r/vs
    M = np.array([[0.0, y*VH/sqrt(2)],
                  [lam*vs/sqrt(2), ME]])
    UL, masses, Vh = np.linalg.svd(M, full_matrices=False)
    UR = Vh.T
    Gamma_h = np.array([[0.0, y/sqrt(2)], [0.0, 0.0]])
    Gamma_s = np.array([[0.0, 0.0], [lam/sqrt(2), 0.0]])
    Gh = UL.T @ Gamma_h @ UR
    Gs = UL.T @ Gamma_s @ UR
    return masses, Gh, Gs, y, lam, theta_r


def pi_rc_one_flavor(vs, ml, s):
    masses, Gh, Gs, y, lam, theta_r = mass_eigenstate_data(vs, ml)
    total = 0j
    uv_p2 = 0j
    uv_const = 0j
    for i in range(2):
        for j in range(2):
            mi, mj = masses[i], masses[j]
            B = b0bar(s, mi, mj, MU_R)
            C = Gh[i,j]*np.conj(Gs[i,j]) + np.conj(Gh[j,i])*Gs[j,i]
            D = Gh[i,j]*Gs[j,i] + np.conj(Gh[j,i])*np.conj(Gs[i,j])
            K = (a0bar(mi,MU_R)+a0bar(mj,MU_R)
                 +(mi*mi+mj*mj-s)*B)
            total += C*K + 2*mi*mj*D*B
            uv_p2 += C
            uv_const += C*2*(mi*mi+mj*mj)+2*mi*mj*D
    return -total/(16*pi*pi), masses, uv_p2, uv_const


def pi_soft_B(s, vs):
    """Leading low-energy EFT soft self-energy in the Plan-C/Plan-B convention."""
    total = 0j
    for ml in LEPTONS.values():
        A = a0bar(ml, MU_R)
        B = b0bar(s, ml, ml, MU_R)
        prod = ml*ml/(VH*vs)
        bubble = prod*(4*A+2*(4*ml*ml-s)*B)/(16*pi*pi)
        contact = (4*ml**4/(VH*vs))*(1-log(ml*ml/(MU_R*MU_R)))/(16*pi*pi)
        total += bubble+contact
    return total


def pi_light_exact_B(s, vs, ml):
    """Light-light term only, using exact mass-eigenstate light Yukawas."""
    masses, Gh, Gs, *_ = mass_eigenstate_data(vs, ml)
    mlight = masses[1]
    gh = Gh[1,1].real
    gs = Gs[1,1].real
    return gh*gs*(4*a0bar(mlight,MU_R)
                  +2*(4*mlight*mlight-s)*b0bar(s,mlight,mlight,MU_R))/(16*pi*pi)


def scalar_width(ms, vs, ma):
    width = 0.0
    if 2*ma < ms:
        x = (ma/ms)**2
        width += ms**3/(32*pi*vs**2)*(1-4*x+12*x*x)*sqrt(1-4*x)
    for ml in LEPTONS.values():
        if 2*ml < ms:
            width += ml**2*ms/(8*pi*vs**2)*(1-4*ml*ml/ms**2)**1.5
    return width


def main():
    print("Exact mass-eigenstate one-loop h-s self-energy check")
    print(f"m_h={MH} GeV; v_h={VH} GeV; M_E(input)={ME} GeV; theta_L(input)={THETA_L}")
    print("All four internal mass-eigenstate pairs are included.")
    print("Pi_RC convention is converted to Plan-B convention by Pi_B=-Pi_RC.")
    print()

    for label, vs, ma in BENCHMARKS:
        full0_rc = 0j
        fullh_rc = 0j
        uv_p2 = 0j
        uv_const = 0j
        light0_B = 0j
        lighth_B = 0j

        print(f"BENCHMARK {label}: v_s={vs:.6f} GeV, m_A'={ma:g} GeV, g_X={ma/(2*vs):.8g}")
        for flavor, ml in LEPTONS.items():
            p0, masses, uvc, uvk = pi_rc_one_flavor(vs, ml, 0.0)
            ph, *_ = pi_rc_one_flavor(vs, ml, MH*MH)
            full0_rc += p0
            fullh_rc += ph
            uv_p2 += uvc
            uv_const += uvk
            light0_B += pi_light_exact_B(0.0, vs, ml)
            lighth_B += pi_light_exact_B(MH*MH, vs, ml)
            print(f"  {flavor}: m_light={masses[1]:.9g} GeV, m_heavy={masses[0]:.9g} GeV")

        full_diff_B = -(fullh_rc-full0_rc)
        light_diff_B = lighth_B-light0_B
        hard_diff_exact = full_diff_B-light_diff_B
        q = sum(2*ml*ml/(VH*vs) for ml in LEPTONS.values())
        hard_derivative_candidate = q*MH*MH/(24*pi*pi)

        delta_lambda = -sum(
            (sqrt(2)*ME*THETA_L/VH * sqrt(2)*ME*(ml/(ME*THETA_L))/vs)**2
            for ml in LEPTONS.values()
        )/(8*pi*pi)
        threshold_pi = -VH*vs*delta_lambda
        hard0_rc = full0_rc+pi_soft_B(0.0,vs)

        matched_pi = pi_soft_B(MH*MH,vs)+hard_diff_exact
        gamma_s = scalar_width(MH,vs,ma)
        a = MH*MH-1j*MH*0.00407
        b = MH*MH-1j*MH*gamma_s
        mixing_ratio = abs(matched_pi)/abs(a-b)

        print(f"  Pi_RC(0) full = {full0_rc.real:.12g} GeV^2")
        print(f"  Pi_RC(m_h^2) full = {fullh_rc.real:.12g} {fullh_rc.imag:+.12g}i GeV^2")
        print(f"  Pi_B(m_h^2)-Pi_B(0) full = {full_diff_B.real:.12g} {full_diff_B.imag:+.12g}i GeV^2")
        print(f"  exact light-light Pi_B(m_h^2)-Pi_B(0) = {light_diff_B.real:.12g} {light_diff_B.imag:+.12g}i GeV^2")
        print(f"  exact hard momentum difference = {hard_diff_exact.real:.12g} {hard_diff_exact.imag:+.12g}i GeV^2")
        print(f"  leading hard-derivative prediction = {hard_derivative_candidate:.12g} GeV^2")
        print(f"  relative difference = {hard_diff_exact.real/hard_derivative_candidate-1:+.6e}")
        print(f"  UV p^2 coefficient sum C = {uv_p2.real:.4e}")
        print(f"  UV local coefficient sum = {uv_const.real:.4e}")
        print(f"  leading-seesaw Delta lambda_HS = {delta_lambda:.12g}")
        print(f"  -v_h v_s Delta lambda_HS = {threshold_pi:.12g} GeV^2")
        print(f"  zero-momentum hard comparator = {hard0_rc.real:.12g} GeV^2")
        print(f"  threshold relative residual = {hard0_rc.real/threshold_pi-1:+.6e}")
        print(f"  matched Pi_hs(m_h^2) = {matched_pi.real:.12g} {matched_pi.imag:+.12g}i GeV^2")
        print(f"  Gamma_s(m_h) = {gamma_s:.12g} GeV")
        print(f"  |Pi/(a-b)| at m_s=m_h = {mixing_ratio:.12g}")
        print(f"  2|Pi/(a-b)| diagnostic = {2*mixing_ratio:.12g}")
        print("  width-regulated diagnostic scan: m_s [GeV], Gamma_s [GeV], 2|Pi/(a-b)|")
        for ms_scan in (10.0, 50.0, 100.0, 124.5, 125.0, 125.25, 125.5, 150.0):
            gamma_scan = scalar_width(ms_scan, vs, ma)
            a_scan = MH*MH-1j*MH*0.00407
            b_scan = ms_scan*ms_scan-1j*ms_scan*gamma_scan
            diagnostic = 2*abs(matched_pi)/abs(a_scan-b_scan)
            print(f"    {ms_scan:.2f}, {gamma_scan:.9g}, {diagnostic:.9g}")
        assert abs(uv_p2) < 1e-12
        assert abs(uv_const) < 1e-5
        assert abs(full_diff_B.imag-light_diff_B.imag) < 1e-9
        assert abs(hard_diff_exact.imag) < 1e-8
        assert abs(hard_diff_exact.real/hard_derivative_candidate-1) < 1e-3
        assert abs(hard0_rc.real/threshold_pi-1) < 3e-4
        print("  CHECKS: PASS")
        print()


if __name__ == "__main__":
    main()
