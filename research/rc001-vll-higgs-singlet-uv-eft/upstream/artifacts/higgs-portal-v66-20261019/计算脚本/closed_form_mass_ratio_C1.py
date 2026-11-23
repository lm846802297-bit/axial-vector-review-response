import sys
sys.path.insert(0, '/mnt/data')
import general_mass_ratio_integral as g
import sympy as s, time
from functools import lru_cache
r=s.symbols('r', positive=True)
z=1-r**2
pi=s.pi
params={g.a:s.Integer(1),g.b:s.Rational(7,10),g.cL:s.Rational(3,5),g.sL:s.Rational(4,5),g.cR:s.Rational(5,13),g.sR:s.Rational(12,13)}
@lru_cache(None)
def Jclosed(p,powers,I):
 N=sum(powers); k=len(I); N1=sum(powers[i] for i in I)
 pref=s.Rational(1,s.factorial(N+3))
 for n in powers: pref*=s.factorial(n)
 if k==0: return pref
 if k==4: return pref/r**(2*p)
 h=s.hyper([p,N1+k],[N+4],z)
 return pref*s.hyperexpand(h)
order=('h','s','h','s'); al=0
T=0; cnt=0; t0=time.time()
for path,I,H,MM,C in g.path_data(order):
 S=sum(C.values())
 Bs=[s.expand(H*(s.Rational(2,3)*g.g[al]-2*g.d[al])),s.expand(s.Rational(1,3)*sum(C[pair]*g.f[pair][al] for pair in C)-s.Rational(2,3)*S*g.d[al]),s.expand(-s.Rational(2,3)*MM*g.d[al])]
 for p,B in enumerate(Bs,1):
  P=s.Poly(B.subs(params).subs({g.m1:r,g.m2:1}),*g.xs)
  for powers,coef in P.terms():
   if coef:
    T += coef*Jclosed(p,powers,I); cnt+=1
 print('path',path,'elapsed',round(time.time()-t0,1),'terms',cnt, 'ops',s.count_ops(T),flush=True)
T=s.factor(6*T/(16*pi**2))
print('FINAL elapsed',time.time()-t0,'ops',s.count_ops(T))
print(s.factor(T))
print('at2',s.N(T.subs(r,2),15),'at.5',s.N(T.subs(r,s.Rational(1,2)),15),'at1.0001',s.N(T.subs(r,s.Rational(10001,10000)),15))
