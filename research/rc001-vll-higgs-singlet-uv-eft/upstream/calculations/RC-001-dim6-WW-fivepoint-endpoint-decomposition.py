#!/usr/bin/env python3
"""RC-001 B2c-IVb: exact endpoint identities for the UV five-point Ward sum."""
from itertools import product
import sympy as sp

I=sp.I
ETA=(1,-1,-1,-1)
SIGMA=(
    sp.Matrix([[0,1],[1,0]]),
    sp.Matrix([[0,-I],[I,0]]),
    sp.Matrix([[1,0],[0,-1]]),
)
T=tuple(s/2 for s in SIGMA)
GAMMA=[sp.diag(1,1,-1,-1)]
for s in SIGMA:
    GAMMA.append(sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2),s),
        sp.Matrix.hstack(-s,sp.zeros(2))
    ))
GAMMA5=I*GAMMA[0]*GAMMA[1]*GAMMA[2]*GAMMA[3]
PL=(sp.eye(4)-GAMMA5)/2
PR=(sp.eye(4)+GAMMA5)/2
METRIC=sp.diag(*ETA)


def dot(a,b):
    return sp.expand(sum(ETA[i]*a[i]*b[i] for i in range(4)))


def slash(a):
    return sum((ETA[i]*a[i]*GAMMA[i] for i in range(4)),sp.zeros(4))


def zero(m):
    return all(sp.simplify(m[i,j])==0 for i in range(m.rows) for j in range(m.cols))


def delta(i,j):
    return sp.Integer(int(i==j))


def T0(i,j,k,l):
    return delta(i,j)*delta(k,l)


def act_phys(tensor,slot,a,ix):
    i,j,k,l=ix
    out=sp.Integer(0)
    if slot==0:
        for m in range(2): out-=T[a][m,i]*tensor(m,j,k,l)
    elif slot==1:
        for m in range(2): out+=T[a][j,m]*tensor(i,m,k,l)
    elif slot==2:
        for m in range(2): out-=T[a][m,k]*tensor(i,j,m,l)
    elif slot==3:
        for m in range(2): out+=T[a][l,m]*tensor(i,j,k,m)
    return sp.simplify(out)


def apply_phys(tensor,slot,a):
    return lambda *ix: act_phys(tensor,slot,a,ix)


def verify_yukawa_singlets():
    checks=0
    for a in range(3):
        for ix in product(range(2),repeat=4):
            left=act_phys(T0,0,a,ix)+act_phys(T0,1,a,ix)
            right=act_phys(T0,2,a,ix)+act_phys(T0,3,a,ix)
            assert sp.simplify(left)==0
            assert sp.simplify(right)==0
            checks+=2
    return checks


def verify_fermion_endpoints():
    q=list(sp.symbols("qF0:4",real=True))
    rw=list(sp.symbols("rFW0:4",real=True))
    ry=[rw[i]-q[i] for i in range(4)]
    Sw=-slash(rw)/dot(rw,rw)
    Sy=-slash(ry)/dot(ry,ry)
    assert zero(Sw*slash(q)*PL*Sy-(Sw*PR-PL*Sy))

    rbw=list(sp.symbols("rFBW0:4",real=True))
    rby=[rbw[i]+q[i] for i in range(4)]
    SBw=slash(rbw)/dot(rbw,rbw)
    SBy=slash(rby)/dot(rby,rby)
    assert zero(SBy*slash(q)*PL*SBw-(PL*SBw-SBy*PR))
    return 32


def verify_scalar_endpoints():
    q=list(sp.symbols("qS0:4",real=True))
    rw=list(sp.symbols("rSW0:4",real=True))
    ryA=[rw[i]-q[i] for i in range(4)]
    lhsA=dot(q,[rw[i]+ryA[i] for i in range(4)])/(dot(rw,rw)*dot(ryA,ryA))
    rhsA=1/dot(ryA,ryA)-1/dot(rw,rw)
    assert sp.simplify(lhsA-rhsA)==0

    ryB=[rw[i]+q[i] for i in range(4)]
    lhsB=dot(q,[rw[i]+ryB[i] for i in range(4)])/(dot(rw,rw)*dot(ryB,ryB))
    rhsB=1/dot(rw,rw)-1/dot(ryB,ryB)
    assert sp.simplify(lhsB-rhsB)==0
    return 2


def metric(mu,nu):
    return sp.Integer(ETA[mu]) if mu==nu else sp.Integer(0)


def K(mu,nu,p):
    return sp.expand(dot(p,p)*metric(mu,nu)-ETA[mu]*p[mu]*ETA[nu]*p[nu])


def gamma3(alpha,mu,nu,q,k):
    return (
        metric(alpha,mu)*ETA[nu]*(q[nu]-k[nu])
        +metric(mu,nu)*ETA[alpha]*(2*k[alpha]+q[alpha])
        +metric(nu,alpha)*ETA[mu]*(-k[mu]-2*q[mu])
    )


def verify_three_w_and_fg():
    q=list(sp.symbols("qW0:4",real=True))
    k=list(sp.symbols("kW0:4",real=True))
    kq=[k[i]+q[i] for i in range(4)]
    for mu,nu in product(range(4),repeat=2):
        lhs=sum(q[a]*gamma3(a,mu,nu,q,k) for a in range(4))
        rhs=K(mu,nu,kq)-K(mu,nu,k)
        assert sp.simplify(lhs-rhs)==0

    G=METRIC
    covk=sp.Matrix([ETA[i]*k[i] for i in range(4)])
    covkq=sp.Matrix([ETA[i]*kq[i] for i in range(4)])
    Kk=dot(k,k)*G-covk*covk.T
    Kkq=dot(kq,kq)*G-covkq*covkq.T
    Dk=G/dot(k,k)
    Dkq=G/dot(kq,kq)
    lhs=Dkq*(Kkq-Kk)*Dk
    rem=(sp.Matrix(k)*sp.Matrix(k).T-sp.Matrix(kq)*sp.Matrix(kq).T)/(dot(k,k)*dot(kq,kq))
    assert zero(sp.simplify(lhs-(Dk-Dkq+rem)))
    return 16,16


def main():
    yuk=verify_yukawa_singlets()
    ferm=verify_fermion_endpoints()
    scalar=verify_scalar_endpoints()
    three,fg=verify_three_w_and_fg()

    print("RC-001 B2c-IVb endpoint decomposition")
    print(f"PASS: physical SU(2) charge sums vanish at both Yukawa singlets ({yuk}/96).")
    print(f"PASS: A/B oriented fermion endpoint WTIs ({ferm}/32 Dirac components).")
    print(f"PASS: A/B oriented scalar endpoint WTIs ({scalar}/2).")
    print(f"PASS: three-W transverse inverse-kernel difference ({three}/16).")
    print(f"PASS: Feynman-gauge propagator chain including R_FG ({fg}/16).")
    print("ENDPOINT LEDGER:")
    print("  Yukawa-vertex gauge variation: cancels between the two light fields at each singlet vertex.")
    print("  Internal-W endpoint: matter-line terms must be combined with the three-W difference.")
    print("  Scalar endpoint: scalar-line insertion and seagull must be combined.")
    print("  Feynman-gauge remainder R_FG: retained for gauge-fixing/ghost STI completion.")
    print("  External-leg/LSZ and counterterms: separate terms in the full renormalized identity.")
    print("BOUNDARY: no complete Lorentz-weighted 24-graph sum or hard matching coefficient.")


if __name__=="__main__":
    main()
