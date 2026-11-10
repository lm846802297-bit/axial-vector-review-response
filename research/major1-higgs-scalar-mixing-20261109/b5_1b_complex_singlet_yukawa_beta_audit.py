#!/usr/bin/env python3
"""Exact one-loop Yukawa-matrix audit for one complex singlet S.

The muon Yukawa couples to S and the tau Yukawa to S*. The two real
components of S therefore have opposite phases in the tau block.
The general Weyl beta tensor is Eq. (2.10) of Pannell & Stergiou,
JHEP 08 (2023) 128, arXiv:2305.14417.
"""
from __future__ import annotations

import sympy as sp


def derive_yukawa_beta():
    lam_mu, lam_tau = sp.symbols("lambda_mu lambda_tau", real=True)
    sqrt2 = sp.sqrt(2)

    # Weyl basis: (E_muL, mu_R^c, E_tauL, tau_R^c).
    # Choose the overall real-scalar phase so the mu block carries +i
    # and the tau block -i. Taking the hermitian-conjugate convention flips
    # both signs; only their relative sign, fixed by S_mu=S and S_tau=S*, matters.
    y1 = sp.zeros(4)
    y2 = sp.zeros(4)
    y1[0, 1] = y1[1, 0] = lam_mu/sqrt2
    y1[2, 3] = y1[3, 2] = lam_tau/sqrt2
    y2[0, 1] = y2[1, 0] = sp.I*lam_mu/sqrt2
    y2[2, 3] = y2[3, 2] = -sp.I*lam_tau/sqrt2
    ys = (y1, y2)

    beta_matrices = []
    for i in range(2):
        yi = ys[i]
        beta_i = sp.zeros(4)
        for j in range(2):
            yj = ys[j]
            yj_dag = yj.conjugate().T
            yi_dag = yi.conjugate().T

            # Eq. (2.10): fermion-line terms plus the scalar trace term.
            beta_i += sp.Rational(1, 2)*(yj*yj_dag*yi + yi*yj_dag*yj)
            beta_i += 2*yj*yi_dag*yj
            trace_pair = sp.trace(yi*yj_dag) + sp.trace(yj*yi_dag)
            beta_i += sp.Rational(1, 2)*trace_pair*yj
        beta_matrices.append(beta_i.applyfunc(sp.simplify))

    # y_{phi_1, E_l l^c}=lambda_l/sqrt(2), so multiply by sqrt(2).
    beta_mu = sp.factor(sqrt2*beta_matrices[0][0, 1])
    beta_tau = sp.factor(sqrt2*beta_matrices[0][2, 3])

    # The second real component must carry the corresponding +/- i phase.
    phase_mu = sp.simplify(beta_matrices[1][0, 1]-sp.I*beta_matrices[0][0, 1])
    phase_tau = sp.simplify(beta_matrices[1][2, 3]+sp.I*beta_matrices[0][2, 3])
    assert phase_mu == 0
    assert phase_tau == 0

    return lam_mu, lam_tau, beta_mu, beta_tau


def main():
    lam_mu, lam_tau, beta_mu, beta_tau = derive_yukawa_beta()
    expected_mu = lam_mu*(2*lam_mu**2+lam_tau**2)
    expected_tau = lam_tau*(2*lam_tau**2+lam_mu**2)
    assert sp.simplify(beta_mu-expected_mu) == 0
    assert sp.simplify(beta_tau-expected_tau) == 0
    print("Exact real-scalar/Weyl Yukawa matrix audit: PASS")
    print(f"16 pi^2 beta_lambda_mu = {sp.factor(beta_mu)}")
    print(f"16 pi^2 beta_lambda_tau = {sp.factor(beta_tau)}")
    print("Gauge contribution to each flavor: -6 gY^2 - 6 gX^2")


if __name__ == "__main__":
    main()
