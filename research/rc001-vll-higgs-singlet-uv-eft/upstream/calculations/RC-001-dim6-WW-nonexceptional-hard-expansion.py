#!/usr/bin/env python3
"""d-dimensional hard-region expansion of the fixed-routing Q_LD pure-WW boxes.

This script reduces the four cross-vertex numerator chains through first order
in external momenta. It keeps the d-dimensional gamma_mu A B C gamma^mu
identity for LD-W-01 and the d-dimensional angular tensor averages.

It computes a fixed-routing, unit-multiplicity triplet sub-block. It is not a
diagram generator and does not include the second external-field routing,
same-vertex graphs, external legs, counterterms, or the full Ward sum.
"""
import sympy as sp

d, eps, L = sp.symbols("d eps L", real=True)
p1, p2, p3, p4 = sp.symbols("p1 p2 p3 p4")
J, K = sp.symbols("J K")
cbar = sp.symbols("cbar")
WEIGHTS = {
    "01": -sp.Rational(1, 4),
    "02": sp.Rational(1, 4),
    "05": sp.Rational(1, 4),
    "06": -sp.Rational(1, 4),
}


def pair_hard_kernels():
    """Return coefficients of J and K after d-dimensional angular reduction.

    The heavy momentum is k-p1-p2. The two light-line shifts are:
      01: (-p1,p4), 02: (-p1,p3), 05: (-p2,p4), 06: (-p2,p3).
    """
    return {
        "01": (
            (d - 2)**2 / d * (p2 + p4),
            2 * (d - 2) / d * (p1 + p2),
        ),
        "02": (
            -p2 + 2 * (1 - 1/d) * p3,
            2 / d * (p1 + p2),
        ),
        "05": (
            2 * (1 - 1/d) * p2 + (1 - 2/d) * p3,
            -2 / d * (p1 + p2),
        ),
        "06": (
            -(p1 + p2),
            2 / d * (p1 + p2),
        ),
    }


def triplet_weighted_kernels():
    pairs = pair_hard_kernels()
    j = sp.factor(sum(WEIGHTS[k] * pairs[k][0] for k in WEIGHTS))
    k = sp.factor(sum(WEIGHTS[key] * pairs[key][1] for key in WEIGHTS))
    # Momentum conservation is imposed only after the ordered amplitude exists.
    j = sp.factor(j.subs(p4, -p1 - p2 - p3))
    return j, k


def expected_triplet_kernels():
    return (
        sp.factor(
            (d**2 - 3*d + 4)/(4*d) * p1
            + (d - 1)/(2*d) * p2
            + (d - 1)/4 * p3
        ),
        sp.factor(-(d - 1)/(2*d) * (p1 + p2)),
    )


def exceptional_kernels():
    """Set p1=p3=0, p2=P, p4=-P and compare to the old scalar kernels."""
    pairs = pair_hard_kernels()
    return {
        key: (
            sp.factor(value[0].subs({p1: 0, p2: 1, p3: 0, p4: -1})),
            sp.factor(value[1].subs({p1: 0, p2: 1, p3: 0, p4: -1})),
        )
        for key, value in pairs.items()
    }


def expand_masters():
    """Use the already checked scalar masters in the common MS-bar convention."""
    # J_hard = (Delta_UV + 1 - L)/M_E^2; K_hard = -1/M_E^2.
    # Keep Delta_UV symbolic as 1/eps + cbar to retain O(eps)*pole terms.
    delta = 1/eps + cbar
    j_master = delta + 1 - L
    k_master = -1
    return j_master, k_master, delta


def hard_amplitude_expansion():
    j_kernel, k_kernel = triplet_weighted_kernels()
    j_master, k_master, delta = expand_masters()
    amplitude = sp.expand(j_kernel * j_master + k_kernel * k_master)
    # d=4-2 eps; extract the pole and finite term componentwise.
    amplitude_eps = sp.series(
        amplitude.subs(d, 4 - 2*eps), eps, 0, 1
    ).removeO()
    pole = sp.simplify(sp.limit(eps * amplitude_eps, eps, 0))
    finite = sp.simplify(
        sp.limit(amplitude_eps - pole/eps, eps, 0)
    )
    return sp.factor(pole), sp.factor(finite), amplitude_eps


def soft_uv_residue():
    """The four-box EFT-soft residue in the same ordered momentum basis."""
    return sp.Rational(1, 2)*p1 + sp.Rational(3, 8)*p2 + sp.Rational(3, 4)*p3


def main():
    pairs = pair_hard_kernels()
    expected = {
        "01": (0, 2*(d-2)/d),
        "02": (-1, 2/d),
        "05": (2*(1-1/d), -2/d),
        "06": (-1, 2/d),
    }
    exceptional = exceptional_kernels()
    for key in pairs:
        assert sp.simplify(exceptional[key][0] - expected[key][0]) == 0, key
        assert sp.simplify(exceptional[key][1] - expected[key][1]) == 0, key

    j_kernel, k_kernel = triplet_weighted_kernels()
    expected_j, expected_k = expected_triplet_kernels()
    assert sp.simplify(j_kernel - expected_j) == 0
    assert sp.simplify(k_kernel - expected_k) == 0

    # The hard-region pole coefficient equals the EFT-soft UV residue.
    pole, finite, _ = hard_amplitude_expansion()
    assert sp.simplify(pole - soft_uv_residue()) == 0

    expected_finite = (
        (sp.Rational(1, 2)*(1-L))*p1
        + (sp.Rational(11, 16)-sp.Rational(3, 8)*L)*p2
        + (sp.Rational(1, 4)-sp.Rational(3, 4)*L)*p3
        + cbar*soft_uv_residue()
    )
    # In MS-bar, cbar=0. The pole is displayed separately above.
    finite_msbar = sp.factor(finite.subs(sp.Symbol("cbar"), 0))
    expected_finite_msbar = sp.factor(expected_finite.subs(sp.Symbol("cbar"), 0))
    assert sp.simplify(finite_msbar - expected_finite_msbar) == 0

    # The old exceptional projection reproduces 3/8 (J-K), including 11/16.
    old_finite = sp.simplify(finite_msbar.subs({p1: 0, p2: 1, p3: 0}))
    assert sp.simplify(old_finite - (sp.Rational(11, 16)-sp.Rational(3, 8)*L)) == 0

    print("RC-001 nonexceptional pure-WW hard-region expansion")
    print("Per-pair kernels (coefficient of J, coefficient of K):")
    for key, value in pairs.items():
        print(f"  LD-W-{key}: J={sp.factor(value[0])}; K={sp.factor(value[1])}")
    print("Triplet weighted kernels after momentum conservation:")
    print(f"  R_J(d) = {sp.factor(j_kernel)}")
    print(f"  R_K(d) = {sp.factor(k_kernel)}")
    print("d=4-2 eps pole residue:")
    print(f"  R_J(4) = {sp.factor(pole)}")
    print("  This equals the EFT-soft UV residue with opposite pole sign.")
    print("MS-bar finite local hard polynomial:")
    print(f"  C_hard = {sp.factor(finite_msbar)}")
    print("At mu=M_E (L=0):")
    print("  C_hard = (1/2) p1 + (11/16) p2 + (1/4) p3.")
    print("PASS: exceptional projection reproduces the prior 11/16 - 3L/8 coefficient.")
    print("BOUNDARY: fixed-routing triplet cross-box sub-block, not the complete Wilson coefficient.")


if __name__ == "__main__":
    main()
