"""Aggregated symbolic mass-ratio coefficients for the UV box parameter integrals.

This computes one requested vertex ordering and coefficient at a time.  It groups
all polynomial terms with identical (p, powers, heavy-mass-index set) before
hypergeometric expansion, which avoids repeatedly carrying large expressions.
"""
import sys, time, argparse
from collections import defaultdict
from functools import lru_cache
sys.path.insert(0, '/mnt/data')
import general_mass_ratio_integral as g
import sympy as s

r = s.symbols('r', positive=True)
params = {g.a:s.Integer(1), g.b:s.Rational(7,10), g.cL:s.Rational(3,5),
          g.sL:s.Rational(4,5), g.cR:s.Rational(5,13), g.sR:s.Rational(12,13)}

@lru_cache(None)
def Jclosed(p, powers, I):
    N=sum(powers); k=len(I); N1=sum(powers[i] for i in I)
    pref=s.Rational(1,s.factorial(N+3))
    for n in powers: pref*=s.factorial(n)
    if k == 0: return pref
    if k == 4: return pref/r**(2*p)
    return pref*s.hyperexpand(s.hyper([p,N1+k],[N+4],1-r**2))

def calc(order, al):
    grouped=defaultdict(lambda:s.Integer(0))
    for path,I,H,MM,C in g.path_data(order):
        S=sum(C.values())
        Bs=[s.expand(H*(s.Rational(2,3)*g.g[al]-2*g.d[al])),
            s.expand(s.Rational(1,3)*sum(C[pair]*g.f[pair][al] for pair in C)-s.Rational(2,3)*S*g.d[al]),
            s.expand(-s.Rational(2,3)*MM*g.d[al])]
        for p,B in enumerate(Bs,1):
            poly=s.Poly(B.subs(params).subs({g.m1:r,g.m2:1}),*g.xs)
            for powers,coef in poly.terms():
                if coef:
                    grouped[(p,tuple(powers),tuple(I))] += coef
    grouped={k:s.factor(v) for k,v in grouped.items() if v != 0}
    print('grouped keys',len(grouped),flush=True)
    T=s.Integer(0); t0=time.time()
    for n,(key,coef) in enumerate(grouped.items(),1):
        p,powers,I=key
        T += coef*Jclosed(p,powers,I)
        if n%100==0: print('integrals',n,'elapsed',round(time.time()-t0,1),flush=True)
    T=s.factor(6*T/(16*s.pi**2))
    return T

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--order',default='hshs'); ap.add_argument('--alpha',type=int,default=1); args=ap.parse_args()
    t=time.time(); e=calc(tuple(args.order),args.alpha-1)
    print('TOTAL_SECONDS',round(time.time()-t,2),'OPS',s.count_ops(e),flush=True)
    print('EXPR',s.sstr(e),flush=True)
    print('LIMIT_R1',s.limit(e,r,1),flush=True)
    for q in [s.Rational(1,2),s.Rational(7,10),s.Rational(13,10),s.Integer(2)]: print('VALUE',q,s.N(e.subs(r,q),16),flush=True)
