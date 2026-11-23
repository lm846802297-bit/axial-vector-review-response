from itertools import product, combinations
from functools import lru_cache
import sympy as sp
import mpmath as mp
x1,x2,x3,x4=sp.symbols('x1 x2 x3 x4'); xs=[x1,x2,x3,x4]
a,b,cL,cR,sL,sR=sp.symbols('a b c_L c_R s_L s_R')
m1,m2=sp.symbols('m1 m2', positive=True)
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
A=x2+x3
f={(0,1):[x4**2,A*(A-1),x3**2,-x4*(2*A-1),-2*x3*x4,x3*(2*A-1)],
(0,2):[x4**2,A*(A-1),x3*(x3-1),-x4*(2*A-1),-x4*(2*x3-1),2*x2*x3-x2+2*x3**2-2*x3],
(0,3):[x4*(x4-1),A**2,x3**2,-A*(2*x4-1),-x3*(2*x4-1),2*x3*A],
(1,2):[x4**2,(A-1)**2,x3*(x3-1),-2*x4*(A-1),-x4*(2*x3-1),(2*x3-1)*(A-1)],
(1,3):[x4*(x4-1),A*(A-1),x3**2,-2*x4*A+A+x4-1,-x3*(2*x4-1),x3*(2*A-1)],
(2,3):[x4*(x4-1),A*(A-1),x3*(x3-1),-2*x4*A+A+x4-1,-2*x3*x4+x3+x4-1,2*x2*x3-x2+2*x3**2-2*x3]}
d=[x4*(1-x4),A*(1-A),x3*(1-x3),2*x4*A,2*x3*x4,2*x3*(1-A)]
g=[sp.expand(f[(0,1)][k]+f[(2,3)][k]-f[(0,2)][k]-f[(1,3)][k]+f[(0,3)][k]+f[(1,2)][k]+sp.Rational(1,2)*(f[(0,2)][k]+f[(1,3)][k])) for k in range(6)]

def path_data(order):
 V=[{'h':Yh,'s':Ys}[z] for z in order]
 for path in product((1,2),repeat=4):
  u=[V[r][path[r]-1,path[(r+1)%4]-1] for r in range(4)]
  v=[V[r][path[(r+1)%4]-1,path[r]-1] for r in range(4)]
  # path labels are (a,b,c,d); propagator masses are (b,c,d,a)
  edge_states=[path[1],path[2],path[3],path[0]]
  mu=[m1 if z==1 else m2 for z in edge_states]
  I=tuple(i for i,z in enumerate(edge_states) if z==1)
  H=sp.expand(u[0]*v[1]*u[2]*v[3]+v[0]*u[1]*v[2]*u[3])
  MM=sp.expand(sp.prod(mu)*(sp.prod(u)+sp.prod(v)))
  C={}
  for i,j in combinations(range(4),2):
   val=0
   for sig in product((0,1),repeat=4):
    trans={r for r in range(4) if sig[r]!=sig[(r+1)%4]}
    if trans=={i,j}:
     val += sp.prod(u[r] if sig[r]==0 else v[r] for r in range(4))*sp.prod(mu[r] for r in range(4) if r not in (i,j))
   C[(i,j)]=sp.expand(val)
  yield path,I,H,MM,C

@lru_cache(maxsize=None)
def J(p,powers,I, m1v,m2v):
 N=sum(powers); k=len(I); N1=sum(powers[i] for i in I)
 pref=mp.mpf(1)
 for n in powers: pref*=mp.factorial(n)
 pref/=mp.factorial(N+3)
 if k==0: return pref/(m2v**(2*p))
 if k==4: return pref/(m1v**(2*p))
 return pref/(m2v**(2*p))*mp.hyp2f1(p,N1+k,N+4,1-(m1v**2)/(m2v**2))

def intpoly(poly,p,I,subs,m1v,m2v):
 P=sp.Poly(sp.expand(poly.subs({**subs,m1:sp.Float(m1v),m2:sp.Float(m2v)})),*xs)
 out=mp.mpf('0')
 for powers,coef in P.terms():
  cv=complex(sp.N(coef,18))
  out += cv*J(p,powers,I,m1v,m2v)
 return out

def calc(order,m1v,m2v,params):
 subs={a:params['a'],b:params['b'],cL:params['cL'],sL:params['sL'],cR:params['cR'],sR:params['sR']}
 total=[mp.mpf('0') for _ in range(6)]
 for path,I,H,MM,C in path_data(order):
  S=sum(C.values())
  for al in range(6):
   B1=sp.expand(H*(sp.Rational(2,3)*g[al]-2*d[al]))
   B2=sp.expand(sp.Rational(1,3)*sum(C[pair]*f[pair][al] for pair in C)-sp.Rational(2,3)*S*d[al])
   B3=sp.expand(-sp.Rational(2,3)*MM*d[al])
   total[al]+=6*(intpoly(B1,1,I,subs,m1v,m2v)+intpoly(B2,2,I,subs,m1v,m2v)+intpoly(B3,3,I,subs,m1v,m2v))/(16*mp.pi**2)
 return total

if __name__=='__main__':
 mp.mp.dps=20
 # Exact-ish test point, with normalized mixing pairs.
 params={'a':1.0,'b':0.7,'cL':0.6,'sL':0.8,'cR':5/13,'sR':12/13}
 for ratio in [1.0,1.0001]:
  print('\nratio m1/m2 =',ratio, flush=True)
  for order in [('h','s','h','s'),('h','h','s','s')]:
   vals=calc(order,ratio,1.0,params)
   print(''.join(order),*[mp.nstr(v,14) for v in vals],flush=True)
