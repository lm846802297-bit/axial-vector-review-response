#!/usr/bin/env python3
"""B5-1b SM-input sub-block: one-loop SM running to M_E=20 TeV.

This deliberately runs only the SM gauge/top/Higgs subsystem. It does NOT
claim a coupled UV VLL running result; the model-specific VLL beta functions
must be derived and validated before that evolution is integrated.
"""
import numpy as np
from scipy.integrate import solve_ivp

MZ = 91.1876
MT = 173.15
MH = 125.25
ME = 20_000.0

# Central MS-bar inputs based on Buttazzo et al.-style matching formulae.
# gY and g2 are quoted at MZ; g3, yt, lambda at MT.
gY_MZ = 0.3575
g2_MZ = 0.65171
g3_MT = 1.1645
yt_MT = 0.93587
lambda_MT = 0.12577 + 0.00205 * (MH - 125.0) - 0.00004 * (MT - 173.15)


def gauge_run(g0, b, mu0, mu1):
    return 1.0 / np.sqrt(
        1.0 / g0**2 - 2.0 * b * np.log(mu1 / mu0) / (16.0 * np.pi**2)
    )


def beta_sm(t, z):
    gy, g2, g3, yt, lam = z
    loop = 16.0 * np.pi**2
    return [
        (41.0 / 6.0) * gy**3 / loop,
        (-19.0 / 6.0) * g2**3 / loop,
        -7.0 * g3**3 / loop,
        yt * (4.5 * yt**2 - 8.0 * g3**2
              - 2.25 * g2**2 - (17.0 / 12.0) * gy**2) / loop,
        (24.0 * lam**2 + lam * (12.0 * yt**2 - 9.0 * g2**2
         - 3.0 * gy**2) - 6.0 * yt**4 + 9.0/8.0 * g2**4
         + 3.0/4.0 * g2**2 * gy**2 + 3.0/8.0 * gy**4) / loop,
    ]


def main():
    gy_mt = gauge_run(gY_MZ, 41.0/6.0, MZ, MT)
    g2_mt = gauge_run(g2_MZ, -19.0/6.0, MZ, MT)
    z0 = [gy_mt, g2_mt, g3_MT, yt_MT, lambda_MT]
    sol = solve_ivp(
        beta_sm, (0.0, np.log(ME / MT)), z0,
        rtol=1e-11, atol=1e-13, method="DOP853"
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    gy, g2, g3, yt, lam = sol.y[:, -1]
    Tsm_top_only = 3.0 * yt**2
    Dsm = 2.0 * Tsm_top_only - 4.5*g2**2 - 1.5*gy**2
    betaA = 0.060413097790 + 1.334678472294e-3 * Dsm
    betaB = 0.000577445793 + 6.758994620533e-5 * Dsm
    print("SM one-loop subsystem at M_E=20 TeV")
    print(f"gY={gy:.12f}")
    print(f"g2={g2:.12f}")
    print(f"g3={g3:.12f}")
    print(f"yt={yt:.12f}")
    print(f"lambdaH={lam:.12f}")
    print(f"T_SM(top-only)={Tsm_top_only:.12f}")
    print(f"D_SM(top-only)={Dsm:.12f}")
    print(f"beta_lambdaHS_A_instantaneous={betaA:.12e}")
    print(f"beta_lambdaHS_B_instantaneous={betaB:.12e}")
    print("CAVEAT: bottom/tau/electron Yukawas neglected; one-loop SM-only "
          "running; no VLL coupled running; no EFT evolution below M_E.")


if __name__ == "__main__":
    main()
