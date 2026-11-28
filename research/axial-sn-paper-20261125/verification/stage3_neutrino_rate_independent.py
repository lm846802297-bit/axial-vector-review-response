import numpy as np
from numpy.polynomial.legendre import leggauss

def fermi(x): return np.exp(-np.logaddexp(0.0,x))
def rates(mass,energy,T,mu_nu,order=160):
    z,w=leggauss(order)
    k=np.sqrt(max(energy*energy-mass*mass,0.0))
    e1=(energy+k*z)/2; e2=(energy-k*z)/2
    W=np.stack([3*(1-z*z)/4,3*(1+z)**2/8,3*(1-z)**2/8],axis=-1)
    prod=np.zeros(3); absorp=np.zeros(3); flavors=[]
    for mu in (mu_nu,0.0):
        x1=(e1-mu)/T; x2=(e2+mu)/T
        pp=np.einsum('z,zh->h',w*fermi(x1)*fermi(x2),W)
        aa=np.einsum('z,zh->h',w*fermi(-x1)*fermi(-x2),W)
        flavors.append((pp,aa)); prod+=pp; absorp+=aa
    pref=mass*mass/(energy*24*np.pi)
    return pref*prod,pref*absorp,[(pref*a,pref*b) for a,b in flavors]

m=10.0
for E in (m,30.0):
    p,a,_=rates(m,E,1e-4,0.)
    expected=m*m/(E*12*np.pi)
    print('vacuum',E,'prod',p,'abs',a,'expected_each_mode',expected,'max_rel',np.max(abs(a/expected-1)))
for mu in (45.,-45.,0.):
    E,T=40.,30.
    p,a,fl=rates(10.,E,T,mu)
    target=np.exp(-E/T)*a
    print('thermal',mu,'prod',p,'abs',a,'balance_rel',np.max(abs(p-target)/np.maximum(abs(p),1e-300)))
    print('flavor_prod_mu_tau',fl[0][0].sum(),fl[1][0].sum())
    if mu==0:
        print('zero_mu_circular_rel',abs(p[1]-p[2])/max(p[1],p[2]))
    else:
        pn,_,_=rates(10.,E,T,-mu)
        print('sign_flip_circular_rel',np.max(abs(p[[0,2,1]]-pn)/np.maximum(abs(p),1e-300)))
