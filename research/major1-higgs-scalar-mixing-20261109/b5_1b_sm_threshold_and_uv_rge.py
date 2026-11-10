#!/usr/bin/env python3
"""B5-1b: weak-scale SM matching, threshold running, and one-loop UV RGEs.

Dependencies: numpy, scipy, sympy.
This is a first-pass one-loop leading-log calculation. It deliberately runs
the VLL EFT below M_E and the full VLL theory only above M_E.

SM matching interpolants: Buttazzo et al., arXiv:1307.3536, with PDG 2025
central inputs inserted. See the companion Markdown note for the input scheme,
equations, assumptions, and physical interpretation.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from b5_1b_complex_singlet_yukawa_beta_audit import derive_yukawa_beta

PI = math.pi
MT = 172.56
MH = 125.20
MW = 80.369
ALPHA_S_MZ = 0.1180
ME = 20_000.0
VH = 246.22
THETA_L = 1.0e-2
M_MU = 0.1056583755
M_TAU = 1.77686

BENCH = {
    "A": {"vS": 70.886458, "mX": 10.0,
          "lambdaHS": 0.210763976387},
    "B": {"vS": 315.0, "mX": 63.0,
          "lambdaHS": 0.0106733764886},
}
KEYS = ["gY", "g2", "g3", "gX", "yt", "y_mu", "y_tau",
        "lam_mu", "lam_tau", "lamH", "lamS", "lamHS"]


def weak_scale_matching():
    lamH = (0.12604 + 0.00206*(MH-125.15)
            - 0.00004*(MT-173.34))
    yt = (0.93690 + 0.00556*(MT-173.34)
          - 0.00042*((ALPHA_S_MZ-0.1184)/0.0007))
    g2 = (0.64779 + 0.00004*(MT-173.34)
          + 0.00011*((MW-80.384)/0.014))
    gY = (0.35830 + 0.00011*(MT-173.34)
          + 0.00020*((MW-80.384)/0.014))
    g3 = (1.1666 + 0.00314*((ALPHA_S_MZ-0.1184)/0.0007)
          - 0.00046*(MT-173.34))
    return np.array([gY, g2, g3, yt, lamH])


def sm_rhs(t, y):
    gY, g2, g3, yt, lamH = y
    fac = 1.0/(16.0*PI**2)
    return fac*np.array([
        (41.0/6.0)*gY**3,
        (-19.0/6.0)*g2**3,
        -7.0*g3**3,
        yt*((9.0/2.0)*yt**2-(17.0/12.0)*gY**2
            -(9.0/4.0)*g2**2-8.0*g3**2),
        24.0*lamH**2 + lamH*(12.0*yt**2-9.0*g2**2-3.0*gY**2)
        -6.0*yt**4 + (9.0/8.0)*g2**4
        +(3.0/4.0)*g2**2*gY**2+(3.0/8.0)*gY**4
    ])


def run_sm_to_threshold():
    y0 = weak_scale_matching()
    sol = solve_ivp(sm_rhs, (0.0, math.log(ME/MT)), y0,
                    rtol=1e-12, atol=1e-14, dense_output=True)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:, -1]


def initial_uv(benchmark, ms, sm_at_ME):
    p = BENCH[benchmark]
    vs, mX, lamHS = p["vS"], p["mX"], p["lambdaHS"]
    gY, g2, g3, yt, lamH = sm_at_ME
    yvll = math.sqrt(2.0)*ME*THETA_L/VH
    return {
        "gY": gY, "g2": g2, "g3": g3,
        "gX": mX/(2.0*vs),
        "yt": yt,
        "y_mu": yvll, "y_tau": yvll,
        "lam_mu": math.sqrt(2.0)*M_MU/(THETA_L*vs),
        "lam_tau": math.sqrt(2.0)*M_TAU/(THETA_L*vs),
        "lamH": lamH,
        "lamS": ms**2/(2.0*vs**2),
        "lamHS": lamHS
    }


# For one complex S with the muon coupling to S and tau coupling to S*,
# the explicit real-scalar/Weyl matrix projection gives 2*self + other flavor.
# Do not use 2*lambda_l^2 + (lambda_mu^2 + lambda_tau^2): that double-counts self.
def uv_rhs(t, y):
    gY, g2, g3, gX, yt, ymu, ytau, lmu, ltau, lH, lS, lHS = y
    fac = 1.0/(16.0*PI**2)
    TSM = 3.0*yt**2
    TVH = ymu**2+ytau**2
    TVS = lmu**2+ltau**2
    return fac*np.array([
        (19.0/2.0)*gY**3,
        (-19.0/6.0)*g2**3,
        -7.0*g3**3,
        8.0*gX**3,
        yt*((9.0/2.0)*yt**2+TVH-(17.0/12.0)*gY**2
            -(9.0/4.0)*g2**2-8.0*g3**2),
        ymu*((3.0/2.0)*ymu**2+TSM+TVH-(15.0/4.0)*gY**2
             -(9.0/4.0)*g2**2-6.0*gX**2),
        ytau*((3.0/2.0)*ytau**2+TSM+TVH-(15.0/4.0)*gY**2
              -(9.0/4.0)*g2**2-6.0*gX**2),
        lmu*(2.0*lmu**2+ltau**2-6.0*gY**2-6.0*gX**2),
        ltau*(2.0*ltau**2+lmu**2-6.0*gY**2-6.0*gX**2),
        24.0*lH**2+2.0*lHS**2
        +lH*(12.0*yt**2+4.0*TVH-9.0*g2**2-3.0*gY**2)
        -6.0*yt**4-2.0*(ymu**4+ytau**4)
        +(9.0/8.0)*g2**4+(3.0/4.0)*g2**2*gY**2
        +(3.0/8.0)*gY**4,
        20.0*lS**2+2.0*lHS**2-48.0*gX**2*lS+96.0*gX**4
        +4.0*lS*TVS-2.0*(lmu**4+ltau**4),
        lHS*(12.0*lH+8.0*lS+4.0*lHS
             -(9.0/2.0)*g2**2-(3.0/2.0)*gY**2-24.0*gX**2
             +2.0*(TSM+TVH+TVS))
    ])


def beta_decomposition(p):
    gY, g2, g3, gX, yt, ymu, ytau, lmu, ltau, lH, lS, lHS = [
        p[k] for k in KEYS
    ]
    fac = 1.0/(16.0*PI**2)
    TSM = 3.0*yt**2
    TVH = ymu**2+ytau**2
    TVS = lmu**2+ltau**2
    beta_hs = {
        "scalar_linear": lHS*(12.0*lH+8.0*lS)*fac,
        "portal_squared": 4.0*lHS**2*fac,
        "SM": lHS*(2.0*TSM-4.5*g2**2-1.5*gY**2)*fac,
        "VLL_Yukawa": 2.0*lHS*(TVH+TVS)*fac,
        "U1X_gauge": -24.0*gX**2*lHS*fac,
    }
    beta_h = {
        "scalar": (24.0*lH**2+2.0*lHS**2)*fac,
        "Yukawa_wave": 4.0*lH*(TSM+TVH)*fac,
        "Yukawa_box": -2.0*(3.0*yt**4+ymu**4+ytau**4)*fac,
        "gauge_linear": (-9.0*lH*g2**2-3.0*lH*gY**2)*fac,
        "gauge_quartic": ((9.0/8.0)*g2**4+(3.0/4.0)*g2**2*gY**2
                          +(3.0/8.0)*gY**4)*fac,
    }
    beta_s = {
        "scalar": (20.0*lS**2+2.0*lHS**2)*fac,
        "Yukawa_wave": 4.0*lS*TVS*fac,
        "Yukawa_box": -2.0*(lmu**4+ltau**4)*fac,
        "gauge_linear": -48.0*gX**2*lS*fac,
        "gauge_quartic": 96.0*gX**4*fac,
    }
    return beta_hs, beta_h, beta_s


def integrate_uv(benchmark, ms, sm_at_ME, ratio_max=3.5):
    p = initial_uv(benchmark, ms, sm_at_ME)
    y0 = np.array([p[k] for k in KEYS], dtype=float)
    sol = solve_ivp(uv_rhs, (0.0, math.log(ratio_max)), y0,
                    rtol=1e-11, atol=1e-13, dense_output=True,
                    max_step=0.002)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol, p


def first_zero_scale(sol, key, ratio_max=3.5):
    idx = KEYS.index(key)
    ts = np.linspace(0.0, math.log(ratio_max), 3000)
    vals = np.array([sol.sol(t)[idx] for t in ts])
    for i in range(len(ts)-1):
        if vals[i]*vals[i+1] < 0.0:
            root = brentq(lambda t: sol.sol(t)[idx], ts[i], ts[i+1])
            return ME*math.exp(root)
    return None


def symbolic_checks():
    M2, mu2 = sp.symbols("M2 mu2", positive=True)
    f = lambda z: z**2*(sp.log(z/mu2)-sp.Rational(3, 2))
    pure = sp.simplify(sp.diff(f(M2), M2, 2).subs(mu2, M2))
    mixed = sp.simplify(
        (-sp.diff(f(M2), M2)/M2+sp.diff(f(M2), M2, 2)).subs(mu2, M2)
    )
    bX = sp.Rational(2, 3)*10+sp.Rational(1, 3)*4
    bY = sp.Rational(41, 6)+2*sp.Rational(4, 3)
    assert pure == 0
    assert mixed == 2
    assert bX == 8
    assert bY == sp.Rational(19, 2)
    lm, lt, beta_lm, beta_lt = derive_yukawa_beta()
    assert sp.simplify(beta_lm-lm*(2*lm**2+lt**2)) == 0
    assert sp.simplify(beta_lt-lt*(2*lt**2+lm**2)) == 0
    return pure, mixed, bX, bY, beta_lm, beta_lt


def main():
    sm = run_sm_to_threshold()
    gY, g2, g3, yt, lamH = sm
    TSM = 3.0*yt**2
    DSM = 2.0*TSM-4.5*g2**2-1.5*gY**2
    print("B5-1b one-loop threshold and UV-RGE audit")
    print(f"SM inputs at Mt: lambdaH={weak_scale_matching()[4]:.10f}, "
          f"yt={weak_scale_matching()[3]:.10f}, "
          f"g2={weak_scale_matching()[1]:.10f}, "
          f"gY={weak_scale_matching()[0]:.10f}, "
          f"g3={weak_scale_matching()[2]:.10f}")
    print("SM-only values at ME=20 TeV:")
    print(f"gY={gY:.12f} g2={g2:.12f} g3={g3:.12f} "
          f"yt={yt:.12f} lambdaH={lamH:.12f}")
    print(f"T_SM={TSM:.12f} D_SM={DSM:.12f}")

    for bname in ("A", "B"):
        print(f"\nBENCHMARK {bname}")
        p0 = initial_uv(bname, 100.0, sm)
        dy0 = uv_rhs(0.0, np.array([p0[k] for k in KEYS]))
        print(f"  beta_lambda_mu={dy0[7]:+.9e} "
              f"beta_lambda_tau={dy0[8]:+.9e}")
        for ms in (10.0, 50.0, 100.0, 150.0):
            p = initial_uv(bname, ms, sm)
            bHS, bH, bS = beta_decomposition(p)
            print(
                f"ms={ms:6.2f} lambdaS={p['lamS']:.9e} "
                f"betaS={sum(bS.values()):+.9e} "
                f"betaH={sum(bH.values()):+.9e} "
                f"betaHS={sum(bHS.values()):+.9e}"
            )
            sol, _ = integrate_uv(bname, ms, sm)
            print(f"  formal zero scales: lambdaS={first_zero_scale(sol,'lamS')} "
                  f"lambdaH={first_zero_scale(sol,'lamH')}")
            for ratio in (1.5, 2.0):
                d = dict(zip(KEYS, sol.sol(math.log(ratio))))
                print(f"  mu/ME={ratio:.1f}: lambdaH={d['lamH']:.9f} "
                      f"lambdaS={d['lamS']:.9f} "
                      f"lambdaHS={d['lamHS']:.9f} "
                      f"lambda_tau={d['lam_tau']:.9f}")

    solA, _ = integrate_uv("A", 100.0, sm)
    target = 1.01*math.sqrt(4.0*PI)
    idx = KEYS.index("lam_tau")
    ts = np.linspace(0.0, math.log(3.5), 3000)
    vals = np.array([solA.sol(t)[idx] for t in ts])
    for i in range(len(ts)-1):
        if vals[i] < target <= vals[i+1]:
            root = brentq(lambda t: solA.sol(t)[idx]-target, ts[i], ts[i+1])
            print(f"\nA lambda_tau exceeds sqrt(4pi) by 1% at "
                  f"mu={ME*math.exp(root):.6f} GeV")
            break

    print("\nSYMBOLIC CHECKS (pure CW quartic, mixed CW portal, bX, bY):",
          symbolic_checks())
    print("PASS: threshold evolution and one-loop coupled UV system completed.")
    print("LIMIT: one-loop leading-log only; independent RGE-generator and "
          "two-loop checks remain required.")


if __name__ == "__main__":
    main()
