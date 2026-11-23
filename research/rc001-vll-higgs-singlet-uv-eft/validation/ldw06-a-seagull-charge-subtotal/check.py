"""One A contact on the already established A-positive/Higgs-charge subtotal."""
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
    # Fundamental H at A: independently differentiate the two labelled
    # gauge fields in the quadratic term of (D H)^dagger D H.
    w=u*t[c]+v*t[d]
    kinetic=g**2*w*w
    vertex=I*kinetic.applyfunc(lambda z:s.diff(z,u,v).subs({u:0,v:0}))
    normalized=vertex/(g*I*g)
    assert normalized==s.Rational(1,2)*int(c==d)*E
    return normalized

@lru_cache(None)
def weak(a,i,j,k,l):
    contact=sum(quartic(a,b)[j,i]*RB[b][k,l] for b in range(3))
    S=s.Rational(1,2)*int(i==j)*RB[a][k,l]
    W=sum((t[b]*t[a])[j,i]*RB[b][k,l] for b in range(3))
    WT=sum((t[a]*t[b])[j,i]*RB[b][k,l] for b in range(3))
    C=I*sum(s.LeviCivita(a,b,c)*t[b][j,i]*RB[c][k,l]
            for b,c in product(range(3),repeat=2))
    assert contact==S and W+WT==S and W-WT==C
    return contact,S,W,WT,C

def vertex_route(k,q,p1,p2,p3):
    # At A, p2 and extra q enter and ordinary W kappa exits.
    K=k+q
    rA=K-p2-q
    h=rA-p1
    p4=-p1-p2-p3-q
    rB=h-p4
    assert rB==K+p3 and p2+q+rA==K
    return K,rA,rB,h,-p3-rB

points=(
 ((4,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(2,1,1,1)),
 ((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1),(2,0,1,0)),
 ((5,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(1,0,0,0)),
)

def check():
    assert sum(1 for a,b in product(range(3),repeat=2) if quartic(a,b).shape==(2,2))==9
    k,q,p1,p2,p3=[s.Matrix(s.symbols(z+"_0:4")) for z in ("k","q","p1","p2","p3")]
    assert vertex_route(k,q,p1,p2,p3)==(k+q,k-p2,k+q+p3,k-p1-p2,-2*p3-k-q)
    rows=[]
    for point in points:
        k,q,p1,p2,p3=map(s.Matrix,point)
        assert q!=s.zeros(4,1)
        Kappa,A,B,h,b=vertex_route(k,q,p1,p2,p3)
        a=2*p2-k
        K,X,Y,old=map(sq,(Kappa,A,B,Kappa-p2))
        assert all((K,X,Y,old))
        Q=heavy(h)
        D=K*X*Y
        Bq=dot(b,q)
        AB=dot(a,b)
        assert AB
        # The raw four-index contraction is a^mu q^nu g_{mu nu}.
        contraction=sum(b[m]*g0[m,n]*q[n] for m,n in product(range(4),repeat=2))
        assert contraction==Bq
        vals={n:0 for n in ("contact_entry_checks","increment_entry_checks","nonzero_contact",
                 "nonzero_uncontracted_contact","nonzero_subtotal","wrong_sign","single_order",
                 "wrong_A_scalar_pole","extra_A_scalar_propagator","wrong_internal_W_shift","wrong_heavy_shift",
                 "wrong_uncontracted_sign","single_order_uncontracted")}
        sample=None
        contact_sample=None
        for c,i,j,z,l in product(range(3),*([range(2)]*4)):
            raw,S,W,WT,C=weak(c,i,j,z,l)
            contact=raw*contraction*Q/D
            expected=S*Bq*Q/D
            assert not changes(contact,expected)
            vals["contact_entry_checks"]+=16
            vals["nonzero_contact"]+=changes(contact,s.zeros(4))
            for m in range(4):
                vec=raw*g0[m,m]*b[m]*Q/D
                vals["nonzero_uncontracted_contact"]+=changes(vec,s.zeros(4))
                vals["wrong_uncontracted_sign"]+=changes(vec,-vec)
                vals["single_order_uncontracted"]+=changes(vec,W*g0[m,m]*b[m]*Q/D)
            # Adopt only the already published pair relation; no re-splitting
            # or recomputing either previous A or B pole/source matrix.
            fixed_pair=(-S*AB+C*Bq)*Q/D
            joined=fixed_pair+contact
            assert not changes(joined,(S*(Bq-AB)+C*Bq)*Q/D)
            assert not changes(joined-fixed_pair,S*Bq*Q/D)
            assert not changes(joined-S*(Bq-AB)*Q/D,C*Bq*Q/D)
            vals["increment_entry_checks"]+=16
            vals["nonzero_subtotal"]+=changes(joined,s.zeros(4))
            vals["wrong_sign"]+=changes(joined,fixed_pair-contact)
            vals["single_order"]+=changes(joined,fixed_pair+W*Bq*Q/D)
            vals["wrong_A_scalar_pole"]+=changes(joined,fixed_pair+contact*X/old)
            vals["extra_A_scalar_propagator"]+=changes(joined,fixed_pair+contact/old)
            vals["wrong_internal_W_shift"]+=changes(joined,fixed_pair+contact*K/sq(k))
            vals["wrong_heavy_shift"]+=changes(joined,fixed_pair+raw*Bq*heavy(h-q)/D)
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
        for akey in ("nonzero_contact","wrong_sign","single_order","wrong_A_scalar_pole",
                     "extra_A_scalar_propagator","wrong_internal_W_shift","wrong_heavy_shift"):
            assert bool(vals[akey])==bool(Bq)
        assert vals["nonzero_subtotal"]
        rows.append({"q_squared":str(sq(q)),"b_dot_q":str(Bq),"a_dot_b":str(AB),"W_Ay_By_h_denominators":list(map(str,(K,X,Y,sq(h)-M2))),
                     "wrong_Aw_denominator":str(old),"entries":vals,"subtotal_sample":sample,"contact_sample":contact_sample})
    return {"scope":"one A seagull on the previously established A positive-pole plus reanchored H charge relation; no complete Ward or loop statement",
            "runtime":{"python":platform.python_version(),"sympy":s.__version__,"platform":platform.system(),
                       "machine":platform.machine()},
            "symbolic":{"quartic_generator_pairs":9,"quartic_matrix_entries":36,"vertex_route":"exact"},
            "points":rows}

if __name__=="__main__":
    print(json.dumps(check(),indent=2))
