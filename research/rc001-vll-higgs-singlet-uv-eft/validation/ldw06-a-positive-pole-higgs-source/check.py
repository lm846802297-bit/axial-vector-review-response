"""A-side scalar +Delta_Y source interface with explicitly aligned loop arguments."""
from functools import lru_cache
from itertools import product
import json
import platform
import sympy as s
from sympy.physics.matrices import mgamma

eta=s.diag(1,-1,-1,-1)
gm=tuple(mgamma(j) for j in range(4))
PL=(s.eye(4)-mgamma(5))/2
t=tuple(A/2 for A in (s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)))
dual=tuple(-A.T for A in t)
M2=s.Integer(400)
indices=tuple(product(range(2),repeat=4))

def dot(a,b):
    return (a.T*eta*b)[0]

def sq(a):
    return dot(a,a)

def prop(h):
    H=sq(h)-M2
    assert H
    return sum((eta[m,m]*h[m]*gm[m] for m in range(4)),s.zeros(4))*PL/H

def changes(a,b):
    return sum(s.expand(x-y)!=0 for x,y in zip(a,b,strict=True))

@lru_cache(None)
def weak(a,i,j,k,l):
    # Direct A Ward scalar order: original external H flows to b then a.
    WA=sum(t[b][j,n]*t[a][n,i]*dual[b][k,l]
           for b,n in product(range(3),range(2)))
    AT=sum(t[a][j,n]*t[b][n,i]*dual[b][k,l]
           for b,n in product(range(3),range(2)))
    Z2=-sum(t[a][j,n]*(2*int(i==l and k==n)-int(i==n and k==l))/4
            for n in range(2))
    G=sum(s.LeviCivita(a,b,c)*t[b][j,i]*dual[c][k,l]
          for b,c in product(range(3),repeat=2))
    assert Z2==AT and WA-AT==s.I*G
    return WA,Z2,WA+AT,s.I*G

def internal_route(k,q,p1,p2,p3):
    K=k+q
    h=k-p1-p2
    rY=k-p2
    rW=K-p2
    rB=K+p3
    a=2*p2-k
    b=-2*p3-K
    # The scalar line before the extra external W feels the original
    # p2 at the ordinary internal W endpoint with momentum K.
    internal_A=p2-rW
    return K,h,rY,rW,rB,a,b,internal_A

def external_box(ell,q,p1,p2,p3):
    # Solve lower four-point momenta from incoming H(p2), W(q), and
    # outgoing scalar momentum P = p2+q into the lower four-point box.
    p4=-p1-p2-p3-q
    P=p2+q
    ra=ell-P
    rb=ell+p3
    h=p4+rb
    assert ra==p1+h and p1+P+p3+p4==s.zeros(4,1)
    return P,ra,rb,h,P-ra,-p3-rb

points=(
    ((4,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(2,1,1,1)),
    ((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1),(2,0,1,0)),
    ((5,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(1,0,0,0)),
)

def verify():
    k,q,p1,p2,p3=[s.Matrix(s.symbols(n+"_0:4")) for n in ("k","q","p1","p2","p3")]
    K,h,rY,rW,rB,a,b,ai=internal_route(k,q,p1,p2,p3)
    P,ra,rb,he,ae,be=external_box(K,q,p1,p2,p3)
    assert (ra,rb,he,ae,be)==(rY,rB,h,a+q,b)
    assert ai==a-q
    P0,_,_,he0,_,_=external_box(k,q,p1,p2,p3)
    assert P0==P and he0==h-q
    assert s.expand(dot(q,rY+rW)-(sq(rW)-sq(rY)))==0
    rows=[]
    for pt in points:
        k,q,p1,p2,p3=map(s.Matrix,pt)
        K,h,rY,rW,rB,a,b,ai=internal_route(k,q,p1,p2,p3)
        P,ra,rb,he,ae,be=external_box(K,q,p1,p2,p3)
        _,ra0,rb0,he0,ae0,be0=external_box(k,q,p1,p2,p3)
        V,A,AW,B=map(sq,(K,rY,rW,rB))
        assert all((V,A,AW,B,sq(P),sq(k),sq(ra0),sq(rb0)))
        D=V*A*B
        heavy=prop(h)
        P_minus=prop(he0)
        # +ig from the W insertion and +i from its extra propagator.
        # Direct A-line W contraction; subtract the negative-Delta_W
        # contribution, positive here after multiplying the phase.
        full=-dot(q,rY+rW)*dot(ai,b)*heavy/(D*AW)
        negative=dot(ai,b)*heavy/(V*AW*B)
        pos=full-negative
        charge_box=dot(ae,be)*prop(he)/(sq(K)*sq(ra)*sq(rb))
        no_reanchor=dot(ae0,be0)*P_minus/(sq(k)*sq(ra0)*sq(rb0))
        wrong_heavy_only=dot(ae,be)*P_minus/D
        copied_current=dot(ai,b)*heavy/D
        ab=dot(a,b)
        bq=dot(b,q)
        assert q!=s.zeros(4,1) and ab
        counts={key:0 for key in ("pole_and_source_checks","factored_pair_checks","symmetric_nonzero",
                  "commutator_nonzero","total_nonzero","wrong_pole_sign","wrong_source_weak_order",
                  "wrong_same_loop_label","omitted_reanchored_heavy_shift","copied_internal_current")}
        example=None
        for g,n in product(range(3),indices):
            w,z,SA,iG=weak(g,*n)
            assert not changes(w*pos,-w*dot(a-q,b)*heavy/D)
            assert not changes(z*charge_box,z*dot(a+q,b)*heavy/D)
            counts["pole_and_source_checks"]+=32
            direct=w*pos-z*charge_box
            sym=-SA*ab*heavy/D
            comm=iG*bq*heavy/D
            assert not changes(direct,sym+comm)
            counts["factored_pair_checks"]+=16
            counts["symmetric_nonzero"]+=changes(sym,s.zeros(4))
            counts["commutator_nonzero"]+=changes(comm,s.zeros(4))
            counts["total_nonzero"]+=changes(direct,s.zeros(4))
            counts["wrong_pole_sign"]+=changes(direct,-w*pos-z*charge_box)
            counts["wrong_source_weak_order"]+=changes(direct,w*pos-w*charge_box)
            counts["wrong_same_loop_label"]+=changes(direct,w*pos-z*no_reanchor)
            counts["omitted_reanchored_heavy_shift"]+=changes(direct,w*pos-z*wrong_heavy_only)
            counts["copied_internal_current"]+=changes(direct,w*pos-z*copied_current)
            if example is None:
                for j,value in enumerate(direct):
                    value=s.expand(value)
                    if value:
                        example={"generator":g,"weak_index":n,"Dirac_row_column":[j//4,j%4],
                                 "common_normalized_value":str(value)}
                        break
        assert all(counts[key] for key in ("symmetric_nonzero","total_nonzero","wrong_pole_sign",
                    "wrong_source_weak_order","wrong_same_loop_label","omitted_reanchored_heavy_shift"))
        assert bool(counts["commutator_nonzero"])==bool(bq)
        assert bool(counts["copied_internal_current"])==bool(bq)
        rows.append({"q_squared":str(sq(q)),"a_dot_b":str(ab),"b_dot_q":str(bq),
                     "shared_anchored_W_scalar_scalar_heavy_denominators":list(map(str,(V,A,B,sq(h)-M2))),
                     "unanchored_heavy_denominator":str(sq(he0)-M2),"entries":counts,"representative":example})
    return {"scope":"single A positive Y-pole and external H charge only; no integral translation asserted",
            "runtime":{"python":platform.python_version(),"sympy":s.__version__,"platform":platform.system(),
                       "machine":platform.machine()},
            "symbolic":{"A_WTI_sign":"exact","anchored_momenta":"exact","bare_pole_sign_and_slot_order":"explicit"},
            "points":rows}

if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
