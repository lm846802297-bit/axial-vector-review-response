"""Signed B positive scalar pole versus the H†(p3) charge source in LD-W-06."""
from functools import lru_cache
from itertools import product
import json
import platform
import sympy as s
from sympy.physics.matrices import mgamma

eta=s.diag(1,-1,-1,-1)
I=s.I
gm=tuple(mgamma(j) for j in range(4))
PL=(s.eye(4)-mgamma(5))/2
t=tuple(A/2 for A in (s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)))
dual=tuple(-A.T for A in t)
M2=s.Integer(400)
indices=tuple(product(range(2),repeat=4))

def dot(a,b):
    return (a.T*eta*b)[0]

def sq(a):
    return dot(a,a)

def slash(h):
    return sum((eta[m,m]*h[m]*gm[m] for m in range(4)),s.zeros(4))*PL

def differences(a,b):
    return sum(s.expand(x-y)!=0 for x,y in zip(a,b,strict=True))

def projected_prop(h):
    H=sq(h)-M2
    assert H
    return slash(h)/H

@lru_cache(None)
def slots(a,i,j,k,l):
    # Raw B positive WTI order, then an independently constructed
    # external H† action on the -T3/4 four-point seed.
    W=sum(t[b][j,i]*dual[a][k,n]*dual[b][n,l]
          for b,n in product(range(3),range(2)))
    Z=-sum(dual[a][k,n]*(2*int(i==l and n==j)-int(i==j and n==l))/4
           for n in range(2))
    WT=sum(t[b][j,i]*dual[b][k,n]*dual[a][n,l]
           for b,n in product(range(3),range(2)))
    assert W==Z
    return W,Z,WT

def born_routing(k,q,p1,p2,p3):
    p4=-p1-p2-p3-q
    P=p3+q
    a_light=k-p2
    b_light=k+P
    h=p4+b_light
    assert p1+h==a_light
    return P,p2-a_light,-P-b_light,a_light,b_light,h

def ordered_internal(k,q,p1,p2,p3):
    W=k
    rA=k-p2
    rY=k+q+p3
    rW=k+p3
    h=k-p1-p2
    a=2*p2-k
    b=-2*p3-k-q
    internal_B=-2*p3-k
    return a,b,internal_B,W,rA,rY,rW,h

POINTS=(
    ((4,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(2,1,1,1)),
    ((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1),(2,0,1,0)),
    ((5,1,2,1),(1,2,0,1),(1,0,1,0),(1,0,0,0),(2,1,1,1)),
)
def verify():
    symbolic=[s.Matrix(s.symbols(n+"_0:4")) for n in ("k","q","p1","p2","p3")]
    k,q,p1,p2,p3=symbolic
    P,ae,be,ra,rb,he=born_routing(*symbolic)
    a,b,bi,w,rA,rY,rW,h=ordered_internal(*symbolic)
    assert ae==a and bi==b+q and be==b-q
    assert ra==rA and rb==rY and he==h
    assert s.expand(-dot(q,rY+rW)-sq(rW)+sq(rY))==0
    assert s.expand(dot(a,bi)-dot(a,be)-2*dot(a,q))==0
    data=[]
    for point in POINTS:
        k,q,p1,p2,p3=map(s.Matrix,point)
        args=(k,q,p1,p2,p3)
        P,ae,be,ra,rb,he=born_routing(*args)
        a,b,bi,w,rA,rY,rW,h=ordered_internal(*args)
        K,A,Y,W=map(sq,(w,rA,rY,rW))
        assert all((K,A,Y,W,sq(P)))
        H=projected_prop(h)
        D=K*A*Y
        # Raw contracted B line contains Y and W poles. The stripped
        # extra +i vertex and +i propagator produce the explicit minus.
        internal_all=-dot(q,rY+rW)*dot(a,bi)*H/(K*A*Y*W)
        negative_piece=-dot(a,bi)*H/(K*A*W)
        positive=internal_all-negative_piece
        external=dot(ae,be)*projected_prop(he)/(sq(k)*sq(ra)*sq(rb))
        metric=dot(a,b)
        qterm=dot(a,q)
        assert q!=s.zeros(4,1) and metric
        assert not differences(positive,dot(a,b+q)*H/D)
        assert not differences(external,dot(a,b-q)*H/D)
        assert not differences(positive-external,2*qterm*H/D)
        counters={n:0 for n in ("pole_and_external_matrix_checks","factored_current_checks",
                      "residual_nonzero","copied_internal_current","wrong_relative_sign",
                      "wrong_weak_order","unshifted_B_propagator")}
        samples=[]
        for ext,n in product(range(3),indices):
            wgt,z,tw=slots(ext,*n)
            assert not differences(wgt*positive,wgt*dot(a,b+q)*H/D)
            assert not differences(z*external,z*dot(a,b-q)*H/D)
            raw=wgt*positive-z*external
            fct=2*qterm*wgt*H/D
            assert not differences(raw,fct)
            if not qterm:
                assert not differences(wgt*positive,z*external)
            counters["pole_and_external_matrix_checks"]+=32
            counters["factored_current_checks"]+=16
            counters["residual_nonzero"]+=differences(raw,s.zeros(4))
            counters["copied_internal_current"]+=differences(raw,wgt*positive-z*positive)
            counters["wrong_relative_sign"]+=differences(raw,wgt*positive+z*external)
            counters["wrong_weak_order"]+=differences(raw,wgt*positive-tw*external)
            counters["unshifted_B_propagator"]+=differences(raw,wgt*positive-z*external*Y/W)
            if not samples:
                for p,x in enumerate(raw):
                    value=s.expand(x)
                    if value:
                        samples.append({"generator":ext,"weak_indices":n,"dirac_row_col":[p//4,p%4],
                                        "common_normalized_value":str(value)})
                        break
        assert bool(counters["residual_nonzero"])==bool(qterm)
        assert bool(counters["copied_internal_current"])==bool(qterm)
        assert all(counters[n] for n in ("wrong_relative_sign","wrong_weak_order","unshifted_B_propagator"))
        data.append({"q_squared":str(sq(q)),"a_dot_b":str(metric),"a_dot_q":str(qterm),
             "shared_denominators_W_left_scalar_right_scalar_heavy":list(map(str,(K,A,Y,sq(h)-M2))),
             "right_scalar_wrong_unshifted_denominator":str(W),
             "entries":counters,"first_nonzero_entry":samples[0] if samples else None})
    return {"scope":"B positive Y pole and Hdag charge source only; fixed-k bare subset",
          "runtime":{"python":platform.python_version(),"sympy":s.__version__,"platform":platform.system(),"machine":platform.machine()},
          "symbolic":{"current_and_pole_maps":"exact","B_WTI_sign":"exact","a_dot_b_cancels_in_selected_pair":True},
          "points":data}

if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
