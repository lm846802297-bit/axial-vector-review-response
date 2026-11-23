"""Exact LD-W-06 graph-subset assembly in the frozen relative conventions."""
from itertools import product
from functools import lru_cache
import json, platform, sys
import sympy as s

I=s.I
half=s.Rational(1,2)
eta=s.diag(1,-1,-1,-1)
t=[s.Matrix([[0,1],[1,0]])/2,s.Matrix([[0,-I],[I,0]])/2,s.diag(1,-1)/2]
gamma=[s.diag(1,1,-1,-1)]
for T in t:
    sigma=2*T
    gamma.append(s.zeros(2).row_join(sigma).col_join((-sigma).row_join(s.zeros(2))))
def sq(v):return dot(v,v)
def dot(a,b):return (a.T*eta*b)[0]
def slash(a):return sum((eta[j,j]*a[j]*gamma[j] for j in range(4)),s.zeros(4))
def zero(m):return all(s.expand(x)==0 for x in m)

@lru_cache
def weak(ext):
    A=[s.kronecker_product(s.eye(2),T,s.eye(2),s.eye(2)) for T in t]
    B=[s.kronecker_product(s.eye(2),s.eye(2),-T.T,s.eye(2)) for T in t]
    seed=s.Matrix([int(i==j and k==l) for i,j,k,l in product(range(2),repeat=4)])
    wa=sum((A[b]*A[ext]*B[b]*seed for b in range(3)),s.zeros(16,1))
    wb=sum((A[b]*B[ext]*B[b]*seed for b in range(3)),s.zeros(16,1))
    sa=sum(((A[b]*A[ext]+A[ext]*A[b])*B[b]*seed for b in range(3)),s.zeros(16,1))
    sb=sum((A[b]*(B[ext]*B[b]+B[b]*B[ext])*seed for b in range(3)),s.zeros(16,1))
    G=sum((s.LeviCivita(ext,b,c)*A[b]*B[c]*seed for b,c in product(range(3),repeat=2)),s.zeros(16,1))
    assert wa==half*(sa+I*G) and wb==half*(sb+I*G)
    return wa,wb,sa,sb,G

    # Contract the all-incoming Yang-Mills vertex before inserting currents.
def ym_contraction(q,k,K,a,b):
    ql,kl,Kl=eta*q,eta*k,eta*K
    kernel=s.Matrix(4,4,lambda mu,nu:sum(q[al]*(
       eta[al,mu]*(ql-kl)[nu]+eta[mu,nu]*(kl+Kl)[al]
       +eta[nu,al]*(-Kl-ql)[mu]) for al in range(4)))
    return (a.T*kernel*b)[0]

class Route:
    def __init__(self,k,q,p1,p2,p3,M2):
        self.k,self.q,self.p1,self.p2,self.p3,self.M2=k,q,p1,p2,p3,M2
        self.K=k+q
        self.h=k-p1-p2
        self.ay,self.aw=k-p2,self.K-p2
        self.by,self.bw=self.K+p3,k+p3
        self.a,self.b=2*p2-k,-2*p3-self.K
        self.al,self.bl=2*p2-self.K,-2*p3-k
        self.u,self.v,self.A,self.Aw,self.B,self.Bw=map(sq,(k,self.K,self.ay,self.aw,self.by,self.bw))
        self.H=sq(self.h)-M2
        assert all(x!=0 for x in [self.u,self.v,self.A,self.Aw,self.B,self.Bw,self.H])
        self.hp=slash(self.h)/self.H
    def at(self,k):
        return Route(k,self.q,self.p1,self.p2,self.p3,self.M2)

def raw(r,ext):
    wa,wb,sa,sb,G=weak(ext)
    lin_a=-dot(r.q,r.ay+r.aw)*dot(r.al,r.b)/(r.A*r.Aw*r.v*r.B)
    lin_b=-dot(r.q,r.by+r.bw)*dot(r.a,r.bl)/(r.B*r.Bw*r.u*r.A)
    sg_a=dot(r.q,r.b)/(r.v*r.A*r.B)
    sg_b=dot(r.a,r.q)/(r.u*r.A*r.B)
    three=-I*ym_contraction(r.q,r.k,r.K,r.a,r.b)/(r.u*r.v*r.A*r.B)
    line_a_W=dot(r.al,r.b)/(r.Aw*r.B*r.v)
    line_b_W=-dot(r.a,r.bl)/(r.Bw*r.A*r.u)
    return [z*r.hp for z in (lin_a*wa+lin_b*wb+sg_a*sa+sg_b*sb+three*G)],line_a_W,line_b_W

def grouped(r,ext,shift_A=False,wrong_contact=False,drop_rfg=False,omit_heavy_shift=False):
    _,_,sa,sb,G=weak(ext)
    ab=dot(r.a,r.b)
    aq,bq=dot(r.a,r.q),dot(r.b,r.q)
    asym=(-ab+3*bq)/(2*r.v*r.A*r.B)
    bsym=(ab+3*aq)/(2*r.u*r.A*r.B)
    R=(dot(r.a,r.k)*dot(r.b,r.k)-dot(r.a,r.K)*dot(r.b,r.K))/(r.u*r.v)
    metric=ab*(1/r.u-1/r.v)
    contact=bq/r.v+aq/r.u
    if wrong_contact: contact=-contact
    group=I*(-half*metric+half*contact-(0 if drop_rfg else R))/(r.A*r.B)
    out=[z*r.hp for z in asym*sa+bsym*sb+group*G]
    b_C=dot(r.a,r.bl)/(r.u*r.A*r.Bw)
    if shift_A:
        hm=r.h-r.q; Hm=sq(hm)-r.M2
        assert Hm!=0
        delta=(slash(r.h)*(2*dot(r.h,r.q)-sq(r.q))-slash(r.q)*r.H)/(Hm*r.H)
        if omit_heavy_shift:
            delta=s.zeros(4)
        return [x+half*b_C*((sa[i]-sb[i])*r.hp+(sa[i]+I*G[i])*delta)
                for i,x in enumerate(out)], delta
    a_C=dot(r.al,r.b)/(r.v*r.Aw*r.B)
    return [x+half*(a_C*(sa[i]+I*G[i])-b_C*(sb[i]+I*G[i]))*r.hp
            for i,x in enumerate(out)]

POINTS=[
 ((4,1,2,1),(1,2,0,1),(1,0,1,0),(0,1,0,2),(2,1,1,1)),
 ((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1),(2,0,1,0)),
]

def verify():
    h=s.Matrix(s.symbols("h0:4"));q=s.Matrix(s.symbols("q0:4"));M=s.Symbol('M2')
    H=sq(h)-M; Hm=sq(h-q)-M
    # Polynomial identity, with denominators cleared.
    assert zero(slash(h-q)*H-slash(h)*Hm-slash(h)*(2*dot(h,q)-sq(q))+slash(q)*H)
    rows=[]
    for data in POINTS:
        r=Route(*map(s.Matrix,data),s.Integer(400))
        alt=r.at(r.k-r.q)
        bad={"contact_sign":0,"missing_RFG":0,"missing_shifted_heavy":0}
        n_raw=n_shift=0
        for ext in range(3):
            wa,wb,sa,sb,G=weak(ext)
            rawsum,aW,bW=raw(r,ext)
            _,aW_old,_=raw(alt,ext)
            assert aW_old==-bW
            expected=grouped(r,ext)
            for a,b in zip(rawsum,expected,strict=True):
                assert zero(a-b);n_raw+=16
            shifted,delta=grouped(r,ext,shift_A=True)
            assert zero(delta-alt.hp+r.hp)
            deployed=[a+wa[i]*(aW_old*alt.hp-aW*r.hp) for i,a in enumerate(rawsum)]
            for a,b in zip(deployed,shifted,strict=True):
                assert zero(a-b);n_shift+=16
            for kind,arg in (("contact_sign",{"wrong_contact":True}),("missing_RFG",{"drop_rfg":True}),
                             ("missing_shifted_heavy",{"omit_heavy_shift":True})):
                test,_=grouped(r,ext,shift_A=True,**arg)
                bad[kind]+=sum(sum(v!=0 for v in a-b) for a,b in zip(test,shifted,strict=True))
        assert all(bad.values())
        rows.append({"q_squared":str(sq(r.q)),"heavy_unshifted":str(r.H),
                     "heavy_shifted_A":str(alt.H),"unshifted_raw_matrix_checks":n_raw,
                     "shifted_raw_matrix_checks":n_shift,"negative_control_changed_entries":bad,
                     "V_A_dot_q":str(dot(r.a,r.q)),"V_B_dot_q":str(dot(r.b,r.q))})
    return {"points":rows,"python":platform.python_version(),"sympy":s.__version__,
            "exact_symbolic_cleared_heavy_difference_matrix_checks":16,
            "scope":"scalar-line A/B plus two seagulls plus contracted 3W subset; no Yukawa/LSZ/BRST closure or Wilson coefficient"}
if __name__=='__main__':
    print(json.dumps(verify(),indent=2,sort_keys=True))
