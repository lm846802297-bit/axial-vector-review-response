#!/usr/bin/env python3
"""Exact 4D chiral Fierz tensor identities using SymPy matrices."""
from __future__ import annotations

import sympy as sp


def build_dirac_basis():
    eye2=sp.eye(2)
    zero2=sp.zeros(2)
    pauli=[
        sp.Matrix([[0,1],[1,0]]),
        sp.Matrix([[0,-sp.I],[sp.I,0]]),
        sp.Matrix([[1,0],[0,-1]]),
    ]
    gamma=[sp.diag(1,1,-1,-1)]
    for sigma in pauli:
        gamma.append(sp.BlockMatrix([[zero2,sigma],[-sigma,zero2]]).as_explicit())
    gamma5=sp.simplify(sp.I*gamma[0]*gamma[1]*gamma[2]*gamma[3])
    pr=sp.simplify((sp.eye(4)+gamma5)/2)
    pl=sp.simplify((sp.eye(4)-gamma5)/2)
    gamma_lower=[gamma[0],-gamma[1],-gamma[2],-gamma[3]]
    return gamma,gamma5,pr,pl,gamma_lower


def check_same_projector(projector,gamma):
    checked=0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    rhs=sp.Rational(1,2)*projector[a,d]*projector[c,b]
                    tensor=0
                    for mu in range(4):
                        for nu in range(4):
                            sigma_up=sp.I/2*(gamma[mu]*gamma[nu]-gamma[nu]*gamma[mu])
                            metric_mu=1 if mu==0 else -1
                            metric_nu=1 if nu==0 else -1
                            sigma_down=metric_mu*metric_nu*sigma_up
                            tensor+=(sigma_up*projector)[a,d]*(sigma_down*projector)[c,b]
                    rhs+=sp.Rational(1,8)*tensor
                    residual=sp.simplify(projector[a,b]*projector[c,d]-rhs)
                    assert residual==0, (a,b,c,d,residual)
                    checked+=1
    return checked


def check_opposite_projectors(first,second,projector_left,projector_right,gamma,gamma_lower):
    checked=0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    rhs=0
                    for mu in range(4):
                        rhs+=(gamma[mu]*projector_left)[a,d]*(gamma_lower[mu]*projector_right)[c,b]
                    rhs*=sp.Rational(1,2)
                    residual=sp.simplify(first[a,b]*second[c,d]-rhs)
                    assert residual==0, (a,b,c,d,residual)
                    checked+=1
    return checked


def audit():
    gamma,gamma5,pr,pl,gamma_lower=build_dirac_basis()
    eye=sp.eye(4)
    for mu in range(4):
        assert sp.simplify(gamma5*gamma[mu]+gamma[mu]*gamma5)==sp.zeros(4)
    assert sp.simplify(pr+pl)==eye
    assert sp.simplify(pr*pl)==sp.zeros(4)
    assert sp.simplify(pl*pr)==sp.zeros(4)

    checks={
        "RR_scalar_tensor":check_same_projector(pr,gamma),
        "LL_scalar_tensor":check_same_projector(pl,gamma),
        "RL_vector":check_opposite_projectors(pr,pl,pl,pr,gamma,gamma_lower),
        "LR_vector":check_opposite_projectors(pl,pr,pr,pl,gamma,gamma_lower),
    }
    assert all(v==256 for v in checks.values())
    total=sum(checks.values())
    assert total==1024
    return {
        "metric":"diag(+1,-1,-1,-1)",
        "sigma_definition":"sigma^{mu nu}=i/2[gamma^mu,gamma^nu]",
        "gamma5":"anticommutes with all four gamma matrices in this exact 4D check",
        "identities":checks,
        "total_exact_components_checked":total,
        "result":"PASS",
        "operator_note":"The c-number matrix identities have positive RHS; anticommuting-field operator Fierz identities acquire an overall minus from interchanging the middle two fermion fields.",
        "scope":"four-dimensional spinor algebra only; no d-dimensional evanescent mixing is computed",
    }


if __name__=="__main__":
    result=audit()
    print("RC-001 chiral Fierz exact-matrix audit")
    for name,count in result["identities"].items():
        print(f"PASS {name}: {count}/256 components")
    print(f"PASS total: {result['total_exact_components_checked']}/1024 exact components")
    print(result["operator_note"])
    print(result["scope"])
