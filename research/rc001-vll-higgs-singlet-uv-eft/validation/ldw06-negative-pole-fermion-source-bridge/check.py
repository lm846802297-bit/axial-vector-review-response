"""Exact LD-W-06 negative scalar WTI poles, two anchors, and fermion source."""
from functools import lru_cache
from itertools import product
import json
import platform
import sympy as s
from sympy.physics.matrices import mgamma

I=s.I
eta=s.diag(1,-1,-1,-1)
gammas=tuple(mgamma(a) for a in range(4))
PL=(s.eye(4)-mgamma(5))/2
t=(s.Matrix([[0,1],[1,0]])/2,s.Matrix([[0,-I],[I,0]])/2,s.diag(1,-1)/2)
dual=tuple(-x.T for x in t)
R=(dual,t,dual,t)
SI=s.Rational(1,2)
slot_indices=tuple(product(range(2),repeat=4))

def dot(a,b):
    return (a.T*eta*b)[0]

def sq(a):
    return dot(a,a)

def slash(a):
    return sum((eta[m,m]*a[m]*gammas[m] for m in range(4)),s.zeros(4))*PL

def different(A,B):
    return sum(s.expand(a-b)!=0 for a,b in zip(A,B,strict=True))

def apply(i,a,n,seed):
    return sum(R[i][a][n[i],m]*seed(*n[:i],m,*n[i+1:]) for m in (0,1))

def T0(i,j,z,l):
    return int(i==j and z==l)

def tab(i,j,z,l):
    return -s.Rational(1,4)*(2*int(i==l and z==j)-int(i==j and z==l))

@lru_cache(None)
def weights(a,n):
    # Direct index products on the actual H, H† line slots.
    i,j,z,l=n
    WA=sum(t[b][j,m]*t[a][m,i]*dual[b][z,l] for b,m in product(range(3),range(2)))
    WAtilde=sum(t[a][j,m]*t[b][m,i]*dual[b][z,l] for b,m in product(range(3),range(2)))
    WB=sum(t[b][j,i]*dual[a][z,m]*dual[b][m,l] for b,m in product(range(3),range(2)))
    WBtilde=sum(t[b][j,i]*dual[b][z,m]*dual[a][m,l] for b,m in product(range(3),range(2)))
    G=sum(s.LeviCivita(a,b,c)*t[b][j,i]*dual[c][z,l] for b,c in product(range(3),repeat=2))
    z1,z4=apply(0,a,n,tab),apply(3,a,n,tab)
    assert WA-WAtilde==I*G and WB-WBtilde==I*G
    assert z1==-WA and z4==-WBtilde
    return WA,WAtilde,WB,WBtilde,I*G,z1,z4

class Route:
    def __init__(self,k,q,p1,p2,p3):
        self.k,self.q,self.p1,self.p2,self.p3=k,q,p1,p2,p3
        self.K=k+q
        self.h=k-p1-p2
        self.rAY,self.rAW=k-p2,self.K-p2
        self.rBY,self.rBW=self.K+p3,k+p3
        self.A,self.AL=2*p2-k,2*p2-self.K
        self.B,self.BL=-2*p3-self.K,-2*p3-k
    def shift(self,q):
        return Route(self.k+q,self.q,self.p1,self.p2,self.p3)
    def factors_A(self):
        return self.AL,self.B,self.K,self.rAW,self.rBY
    def factors_B(self):
        return self.A,self.BL,self.k,self.rAY,self.rBW

def scale(currents_and_poles):
    vl,vr,*poles=currents_and_poles
    d=s.prod(map(sq,poles))
    assert d
    return dot(vl,vr)/d

def prop(h,M2):
    d=sq(h)-M2
    assert d
    return slash(h)/d

def source_from_vertices(r,j,M2):
    # Four-point light/heavy routing from solving the actual shifted
    # lower vertices for bar L or L with internal W fixed to r.k.
    k,q,p1,p2,p3=r.k,r.q,r.p1,r.p2,r.p3
    p4=-p1-p2-p3-q
    assert j in (1,4)
    if j==1:
        p1=p1+q
    else:
        p4=p4+q
    assert p1+p2+p3+p4==s.zeros(4,1)
    left,right=k-p2,k+p3
    H=p4+right
    assert H==left-p1
    return scale((p2-left,-p3-right,k,left,right))*prop(H,M2)

def verified_maps(r):
    ap=r.shift(-r.q)
    bp=r.shift(r.q)
    assert ap.factors_A()==r.factors_B()
    assert bp.factors_B()==r.factors_A()
    assert ap.h==r.h-r.q and bp.h==r.h+r.q
    return ap,bp

POINTS=(
 ((4,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(2,1,1,1)),
 ((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1),(2,0,1,0)),
)

def verify():
    symbols=[s.Matrix(s.symbols(n+"_0:4")) for n in ("k","q","p1","p2","p3")]
    r=Route(*symbols)
    verified_maps(r)
    H=sq(r.h)-s.Symbol("M2")
    Hp=sq(r.h+r.q)-s.Symbol("M2")
    assert not different(H*slash(r.h+r.q)-Hp*slash(r.h),
                         H*slash(r.q)-(2*dot(r.h,r.q)+sq(r.q))*slash(r.h))
    rows=[]
    for v in POINTS:
        r=Route(*map(s.Matrix,v))
        ap,bp=verified_maps(r)
        M2=s.Integer(400)
        CA,CB=scale(r.factors_A()),scale(r.factors_B())
        Ph,Pm,Pp=[prop(rr.h,M2) for rr in (r,ap,bp)]
        q=r.q
        H0,Hplus=sq(r.h)-M2,sq(bp.h)-M2
        plus_delta=(H0*slash(q)-(2*dot(r.h,q)+sq(q))*slash(r.h))/(H0*Hplus)
        assert not different(plus_delta,Pp-Ph)
        F1,F4=[source_from_vertices(r,j,M2) for j in (1,4)]
        assert not different(F1,CB*Pm) and not different(F4,CB*Ph)
        counts={n:0 for n in ("B_translated_literal","A_B_anchor_translate_not_rebase",
                   "commutator_bridge","fermion_charge_source_interface","wrong_B_heavy_shift",
                   "wrong_B_order","same_k_anchor_difference","nonzero_source_residual")}
        rep=None
        for a,n in product(range(3),slot_indices):
            WA,TA,WB,TB,iG,Z1,Z4=weights(a,n)
            # Relative to g2*P4, A contributes + from -delta_A and B
            # contributes - from +delta_B. Their weak tensors differ.
            raw_A=WA*CA*Ph-WB*scale(bp.factors_B())*Pp
            fact_A=CA*(SI*((WA+TA)-(WB+TB))*Ph-WB*plus_delta)
            assert not different(raw_A,fact_A)
            counts["B_translated_literal"]+=16
            # B-anchor uses A(k-q) and B(k). It equals A-anchor(k-q),
            # not A-anchor(k).
            raw_B=WA*scale(ap.factors_A())*Pm-WB*CB*Ph
            A_at_kminusq=WA*scale(ap.factors_A())*Pm-WB*scale(ap.shift(q).factors_B())*Ph
            assert not different(raw_B,A_at_kminusq)
            counts["A_B_anchor_translate_not_rebase"]+=16
            C_A=SI*(WA-TA)*CA*Ph-SI*(WB-TB)*CA*Pp
            assert not different(C_A,-SI*iG*CA*plus_delta)
            counts["commutator_bridge"]+=16
            # Include external charge source -Z1 F1 -Z4 F4 only.
            # Deliberately do not include inverse terms or H/H† source.
            subtotal=raw_B-Z1*F1-Z4*F4
            reduced=2*WA*F1-iG*F4
            assert not different(raw_B,WA*F1-WB*F4)
            assert not different(subtotal,reduced)
            counts["fermion_charge_source_interface"]+=16
            counts["wrong_B_heavy_shift"]+=different(raw_A,CA*(WA-WB)*Ph)
            counts["wrong_B_order"]+=different(raw_A,CA*(WA*Ph-TB*Pp))
            counts["same_k_anchor_difference"]+=different(raw_A,raw_B)
            counts["nonzero_source_residual"]+=different(subtotal,s.zeros(4))
            if rep is None:
                for idx,x in enumerate(subtotal):
                    x=s.expand(x)
                    if x!=0:
                        rep={"generator":a,"weak_indices":n,"dirac_row_col":[idx//4,idx%4],
                             "normalized_exact_value":str(x)}
                        break
        assert all(counts.values()) and rep is not None
        rows.append({"q_squared":str(sq(q)),"heavy_denominators_h_minus_q_h_h_plus_q":
                        [str(sq(rr.h)-M2) for rr in (ap,r,bp)],
                     "signed_entry_counts":counts,"fermion_charge_only_remainder_sample":rep})
    return {"scope":"two internal negative WTI poles and two fermion charge-source entries only",
            "runtime":{"python":platform.python_version(),"sympy":s.__version__,
                       "platform":platform.system(),"machine":platform.machine()},
            "symbolic":{"complete_momentum_current_maps":12,
                        "cleared_plus_heavy_matrix_entries":16,"weak_slot_components_per_test_point":48},
            "points":rows}

if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
