#!/usr/bin/env python3
"""RC-001: physical SU(2) field-representation bridge for five-point tensors."""
from itertools import product
import sympy as sp

I = sp.I
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
T = tuple(s/2 for s in SIGMA)
EPS = sp.LeviCivita
INDICES = tuple(product(range(2), repeat=4))


def delta(i,j):
    return sp.Integer(int(i == j))


def T0(i,j,k,l):
    return delta(i,j)*delta(k,l)


def T3(i,j,k,l):
    return sum(SIGMA[a][i,j]*SIGMA[a][k,l] for a in range(3))


def act_signed(tensor,slot,a,ix):
    i,j,k,l=ix
    out=sp.Integer(0)
    if slot==0:
        for m in range(2): out += T[a][m,i]*tensor(m,j,k,l)
    elif slot==1:
        for m in range(2): out -= T[a][j,m]*tensor(i,m,k,l)
    elif slot==2:
        for m in range(2): out += T[a][m,k]*tensor(i,j,m,l)
    elif slot==3:
        for m in range(2): out -= T[a][l,m]*tensor(i,j,k,m)
    return sp.simplify(out)


def apply_signed(tensor,slot,a):
    return lambda *ix: act_signed(tensor,slot,a,ix)


# Physical field generators are the negatives of the signed WTI actions:
# bar L, H, Hdagger, L = (-t^T, +t, -t^T, +t).
def act_phys(tensor,slot,a,ix):
    return sp.simplify(-act_signed(tensor,slot,a,ix))


def apply_phys(tensor,slot,a):
    return lambda *ix: act_phys(tensor,slot,a,ix)


PAIRS=(
    ("LD-W-01",0,3,0,-sp.Rational(1,4)),
    ("LD-W-02",0,2,0, sp.Rational(1,4)),
    ("LD-W-03",0,1,-sp.Rational(3,4),0),
    ("LD-W-04",3,2,-sp.Rational(3,4),0),
    ("LD-W-05",3,1,0, sp.Rational(1,4)),
    ("LD-W-06",2,1,0,-sp.Rational(1,4)),
)


def pair_phys(a_slot,b_slot):
    return lambda *ix: sp.simplify(sum(
        act_phys(apply_phys(T0,b_slot,b),a_slot,b,ix)
        for b in range(3)
    ))


def G_phys(a_slot,b_slot,external_a):
    return lambda *ix: sp.simplify(sum(
        EPS(external_a,b,c)
        * act_phys(apply_phys(T0,b_slot,c),a_slot,b,ix)
        for b,c in product(range(3),repeat=2)
    ))


def verify_rep_algebra():
    checks=0
    for slot in range(4):
        for a,b in product(range(3),repeat=2):
            for basis_ix in INDICES:
                basis=lambda *ix: sp.Integer(ix==basis_ix)
                lhs=lambda *ix: (
                    act_phys(apply_phys(basis,slot,b),slot,a,ix)
                    -act_phys(apply_phys(basis,slot,a),slot,b,ix)
                )
                rhs=lambda *ix: sum(
                    I*EPS(a,b,c)*act_phys(basis,slot,c,ix)
                    for c in range(3)
                )
                for ix in INDICES:
                    assert sp.simplify(lhs(*ix)-rhs(*ix))==0
                    checks+=1
    return checks


def verify_pair_and_ordering():
    pair_checks=a_checks=b_checks=0
    for pair_id,a_slot,b_slot,c0,c3 in PAIRS:
        seed=pair_phys(a_slot,b_slot)
        for ix in INDICES:
            expected=c0*T0(*ix)+c3*T3(*ix)
            assert sp.simplify(seed(*ix)-expected)==0,(pair_id,ix)
            pair_checks+=1

        for external_a in range(3):
            G=G_phys(a_slot,b_slot,external_a)

            # A line: internal-W generator b precedes external-W generator a.
            graph_A=lambda *ix: sp.simplify(sum(
                act_phys(
                    apply_phys(apply_phys(T0,a_slot,external_a),b_slot,b),
                    a_slot,b,ix
                )
                for b in range(3)
            ))
            reverse_A=apply_phys(seed,a_slot,external_a)
            for ix in INDICES:
                assert sp.simplify(graph_A(*ix)-reverse_A(*ix)-I*G(*ix))==0
                a_checks+=1

            # B line: external-W generator a precedes internal-W generator b.
            graph_B=apply_phys(seed,b_slot,external_a)
            reverse_B=lambda *ix: sp.simplify(sum(
                act_phys(
                    apply_phys(apply_phys(T0,b_slot,external_a),a_slot,b),
                    b_slot,b,ix
                )
                for b in range(3)
            ))
            for ix in INDICES:
                assert sp.simplify(graph_B(*ix)-reverse_B(*ix)-I*G(*ix))==0
                b_checks+=1
    return pair_checks,a_checks,b_checks


def verify_seagulls():
    checks=0
    for _,a_slot,b_slot,_,_ in PAIRS:
        for scalar_slot,other_slot in ((a_slot,b_slot),(b_slot,a_slot)):
            if scalar_slot not in (1,2):
                continue
            for external_a in range(3):
                def sg(*ix):
                    total=sp.Integer(0)
                    for b in range(3):
                        other=apply_phys(T0,other_slot,b)
                        total += act_phys(
                            apply_phys(other,scalar_slot,b),
                            scalar_slot,external_a,ix
                        )
                        total += act_phys(
                            apply_phys(other,scalar_slot,external_a),
                            scalar_slot,b,ix
                        )
                    return sp.simplify(total)
                for ix in INDICES:
                    expected=sp.Rational(1,2)*act_phys(
                        T0,other_slot,external_a,ix
                    )
                    assert sp.simplify(sg(*ix)-expected)==0
                    checks+=1
    return checks


def main():
    rep=verify_rep_algebra()
    pair,a,b=verify_pair_and_ordering()
    sg=verify_seagulls()
    assert pair==96 and a==288 and b==288 and sg==288

    print("RC-001 physical SU(2) field-representation bridge")
    print(f"PASS: physical field generators satisfy [R^a,R^b]=+i epsilon R ({rep} component checks).")
    print("REPRESENTATIONS: R_barL=-t^T, R_H=+t, R_Hdag=-t^T, R_L=+t.")
    print(f"PASS: six pair projections unchanged ({pair}/96).")
    print(f"PASS: A-line physical graph-order commutator = +i G_AB ({a}/288).")
    print(f"PASS: B-line physical graph-order commutator = +i G_AB ({b}/288).")
    print(f"PASS: physical scalar-seagull tensor = one-half opposite-endpoint generator ({sg}/288).")
    print("BOUNDARY: field-representation algebra only; no Lorentz-weighted graph sum or full STI closure.")


if __name__=="__main__":
    main()
