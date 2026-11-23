"""One B contact on the already established B-positive/charge subtotal."""
from functools import lru_cache
from itertools import product
import json
import platform
import sympy as s
from sympy.physics.matrices import mgamma

g=s.Symbol("g",nonzero=True)
u,v=s.symbols("u v")
I=s.I
g0=s.diag(1,-1,-1,-1)
gamma=tuple(mgamma(m) for m in range(4))
PL=(s.eye(4)-mgamma(5))/2
t=tuple(T/2 for T in (s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)))
RB=tuple(-T.T for T in t)
E=s.eye(2)
M2=s.Integer(400)

def dot(a,b):
    return (a.T*g0*b)[0]

def sq(a):
    return dot(a,a)

def changes(A,B):
    return sum(s.expand(x-y)!=0 for x,y in zip(A,B,strict=True))

def heavy(h):
    H=sq(h)-M2
    assert H
    return sum((g0[m,m]*h[m]*gamma[m] for m in range(4)),s.zeros(4))*PL/H

@lru_cache(None)
def quartic(c,d):
    # D=partial-ig R W. The quadratic kinetic term has +g².
    # Differentiate the two labelled W sources before reducing SU(2).
    w=u*RB[c]+v*RB[d]
    result=(g**2*w*w).applyfunc(lambda z:s.diff(z,u,v).subs({u:0,v:0}))*I
    ordinary=I*g
    normalized=result/(g*ordinary)
    expected=s.Rational(1,2)*int(c==d)*E
    assert normalized==expected
    return normalized

@lru_cache(None)
def weak(a,i,j,k,l):
    contact=sum(t[b][j,i]*quartic(a,b)[k,l] for b in range(3))
    S=s.Rational(1,2)*t[a][j,i]*int(k==l)
    W=sum(t[b][j,i]*(RB[a]*RB[b])[k,l] for b in range(3))
    WT=sum(t[b][j,i]*(RB[b]*RB[a])[k,l] for b in range(3))
    C=I*sum(s.LeviCivita(a,b,c)*t[b][j,i]*RB[c][k,l]
            for b,c in product(range(3),repeat=2))
    assert contact==S and W+WT==S and W-WT==C
    return contact,S,W,WT,C

def vertex_route(k,q,p1,p2,p3):
    # Incoming at contact: ordinary internal W k, extra W q, original H† p3.
    rB_y=k+q+p3
    p4=-p1-p2-p3-q
    h=p4+rB_y
    rA=p1+h
    assert rB_y==h-p4 and k==p2+rA
    return rA,rB_y,h,p2-rA

points=(
 ((4,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(2,1,1,1)),
 ((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1),(2,0,1,0)),
 ((5,1,2,1),(1,2,0,1),(1,0,1,0),(1,0,0,0),(2,1,1,1)),
)

def check():
    assert sum(1 for a,b in product(range(3),repeat=2) if quartic(a,b).shape==(2,2))==9
    k,q,p1,p2,p3=[s.Matrix(s.symbols(z+"_0:4")) for z in ("k","q","p1","p2","p3")]
    assert vertex_route(k,q,p1,p2,p3)==(k-p2,k+p3+q,k-p1-p2,2*p2-k)
    rows=[]
    for point in points:
        k,q,p1,p2,p3=map(s.Matrix,point)
        assert q!=s.zeros(4,1)
        A,B,h,a=vertex_route(k,q,p1,p2,p3)
        K,X,Y,old=map(sq,(k,A,B,k+p3))
        assert all((K,X,Y,old))
        Q=heavy(h)
        D=K*X*Y
        Aq=dot(a,q)
        # The raw four-index contraction is a^mu q^nu g_{mu nu}.
        contraction=sum(a[m]*g0[m,n]*q[n] for m,n in product(range(4),repeat=2))
        assert contraction==Aq
        vals={n:0 for n in ("contact_entry_checks","increment_entry_checks","nonzero_contact",
                 "nonzero_uncontracted_contact","nonzero_subtotal","wrong_sign","single_order",
                 "old_B_scalar_pole","extra_B_scalar_propagator","wrong_internal_W_shift",
                 "wrong_uncontracted_sign","single_order_uncontracted")}
        sample=None
        contact_sample=None
        for c,i,j,z,l in product(range(3),*([range(2)]*4)):
            raw,S,W,WT,C=weak(c,i,j,z,l)
            contact=raw*contraction*Q/D
            expected=S*Aq*Q/D
            assert not changes(contact,expected)
            vals["contact_entry_checks"]+=16
            vals["nonzero_contact"]+=changes(contact,s.zeros(4))
            for m in range(4):
                vec=raw*g0[m,m]*a[m]*Q/D
                vals["nonzero_uncontracted_contact"]+=changes(vec,s.zeros(4))
                vals["wrong_uncontracted_sign"]+=changes(vec,-vec)
                vals["single_order_uncontracted"]+=changes(vec,W*g0[m,m]*a[m]*Q/D)
            # Adopt only the already published pair relation; no re-splitting
            # or recomputing either previous A or B pole/source matrix.
            fixed_pair=2*W*Aq*Q/D
            joined=fixed_pair+contact
            assert not changes(joined,(2*S+C)*Aq*Q/D)
            assert not changes(joined-fixed_pair,S*Aq*Q/D)
            assert not changes(fixed_pair-S*Aq*Q/D,C*Aq*Q/D)
            vals["increment_entry_checks"]+=16
            vals["nonzero_subtotal"]+=changes(joined,s.zeros(4))
            vals["wrong_sign"]+=changes(joined,fixed_pair-contact)
            vals["single_order"]+=changes(joined,fixed_pair+W*Aq*Q/D)
            vals["old_B_scalar_pole"]+=changes(joined,fixed_pair+contact*Y/old)
            vals["extra_B_scalar_propagator"]+=changes(joined,fixed_pair+contact/old)
            vals["wrong_internal_W_shift"]+=changes(joined,fixed_pair+contact*K/sq(k+q))
            if contact_sample is None:
                for idx,entry in enumerate(contact):
                    x=s.expand(entry)
                    if x:
                        contact_sample={"generator":c,"weak_indices":[i,j,z,l],"dirac_row_column":[idx//4,idx%4],"value":str(x)}
                        break
            if sample is None:
                for idx,entry in enumerate(joined):
                    x=s.expand(entry)
                    if x:
                        sample={"generator":c,"weak_indices":[i,j,z,l],"dirac_row_column":[idx//4,idx%4],"value":str(x)}
                        break
        assert all(vals[z] for z in ("nonzero_uncontracted_contact","wrong_uncontracted_sign","single_order_uncontracted"))
        for akey in ("nonzero_contact","nonzero_subtotal","wrong_sign","single_order","old_B_scalar_pole",
                     "extra_B_scalar_propagator","wrong_internal_W_shift"):
            assert bool(vals[akey])==bool(Aq)
        rows.append({"q_squared":str(sq(q)),"a_dot_q":str(Aq),"W_Ay_By_h_denominators":list(map(str,(K,X,Y,sq(h)-M2))),
                     "wrong_Bw_denominator":str(old),"entries":vals,"subtotal_sample":sample,"contact_sample":contact_sample})
    return {"scope":"one B seagull on the previously established B positive-pole plus Hdag charge relation; no complete Ward or loop statement",
            "runtime":{"python":platform.python_version(),"sympy":s.__version__,"platform":platform.system(),
                       "machine":platform.machine()},
            "symbolic":{"quartic_generator_pairs":9,"quartic_matrix_entries":36,"vertex_route":"exact"},
            "points":rows}

if __name__=="__main__":
    print(json.dumps(check(),indent=2))
