"""Static spherical GR ray/optical-depth kernel.

Metric: ds^2=-N(r)^2 dt^2+B(r)^2 dr^2+r^2 dOmega^2, B=sqrt(g_rr).
This is a GR-extension module, not the paper-exact flat-chord B.2 baseline.
gamma_abs_star(r_km, omega_local_MeV) must return a reduced local-time rate in MeV.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

KM_TO_MEV_INV = 5.067730716156395e15

@dataclass(frozen=True)
class StaticSphericalMetric:
    radius_km: np.ndarray
    lapse: np.ndarray
    B: np.ndarray

    def __post_init__(self):
        r=np.asarray(self.radius_km,float); n=np.asarray(self.lapse,float); b=np.asarray(self.B,float)
        if r.ndim!=1 or len(r)<2 or n.shape!=r.shape or b.shape!=r.shape:
            raise ValueError("metric arrays must be equal-length 1D arrays")
        if not (np.all(np.isfinite(r)) and np.all(np.isfinite(n)) and np.all(np.isfinite(b))):
            raise ValueError("metric arrays must be finite")
        if np.any(np.diff(r)<=0) or np.any(r<0) or np.any(n<=0) or np.any(b<=0):
            raise ValueError("radii must increase and lapse/B must be positive")
        object.__setattr__(self,"radius_km",r); object.__setattr__(self,"lapse",n); object.__setattr__(self,"B",b)

    @property
    def r_min(self): return float(self.radius_km[0])
    @property
    def r_max(self): return float(self.radius_km[-1])
    def N(self,r): return np.interp(r,self.radius_km,self.lapse)
    def sqrt_g_rr(self,r): return np.interp(r,self.radius_km,self.B)
    def local_energy(self,E_inf,r): return E_inf/self.N(r)

@dataclass(frozen=True)
class RayResult:
    escapes_to_rmax: bool
    E_inf_MeV: float
    angular_momentum_MeV_km: float
    turning_radius_km: float|None
    optical_depth: float
    proper_path_km: float
    deflection_rad: float
    path_segments: tuple
    reason: str

def radial_momentum_squared(metric,mass_MeV,E_inf_MeV,L_MeV_km,r_km):
    omega=metric.local_energy(E_inf_MeV,r_km); r=np.asarray(r_km,float)
    if L_MeV_km==0: cent=np.zeros_like(r)
    else:
        ratio=np.full_like(r,np.inf); np.divide(L_MeV_km,r,out=ratio,where=r>0); cent=ratio*ratio
    return omega**2-mass_MeV**2-cent

def _first_root(metric,mass,E,L,a,b,direction,samples=1025):
    grid=np.linspace(a,b,samples)
    if direction<0: grid=grid[::-1]
    vals=np.asarray(radial_momentum_squared(metric,mass,E,L,grid),float)
    finite=np.abs(vals[np.isfinite(vals)])
    scale=max(float(np.max(finite)) if len(finite) else 1.0,1.0); tol=2e-13*scale
    for i in range(len(grid)-1):
        x0,x1=float(grid[i]),float(grid[i+1]); f0,f1=float(vals[i]),float(vals[i+1])
        if abs(f0)<=tol and i==0: continue
        if f0*f1<0 or (f0>tol and f1<=tol):
            lo,hi=sorted((x0,x1))
            return float(brentq(lambda x:float(radial_momentum_squared(metric,mass,E,L,x)),lo,hi,xtol=1e-12,rtol=1e-12))
    return None

def _segment(metric,mass,E,L,a,b,gamma,unit=KM_TO_MEV_INV,turn_at_a=False):
    if b<=a: return 0.0,0.0,0.0
    def base(r):
        w=float(metric.local_energy(E,r)); k=np.sqrt(max(w*w-mass*mass,0))
        pr=np.sqrt(max(float(radial_momentum_squared(metric,mass,E,L,r)),0))
        return w,k,pr,float(metric.sqrt_g_rr(r))
    if turn_at_a:
        h=max((b-a)*1e-7,1e-10); rp=min(a+h,b)
        deriv=(float(radial_momentum_squared(metric,mass,E,L,rp))-float(radial_momentum_squared(metric,mass,E,L,a)))/(rp-a)
        if deriv<=0: raise ValueError("radial momentum does not open at turning point")
        wa,_,_,Ba=base(a); ga=float(gamma(a,wa))
        lim_tau=2*ga*Ba*wa*np.sqrt((b-a)/deriv)
        lim_len=2*Ba*np.sqrt((b-a)*max(wa*wa-mass*mass,0)/deriv)
        lim_phi=0 if L==0 or a==0 else 2*Ba*L/(a*a)*np.sqrt((b-a)/deriv)
        def f(t,kind):
            if t==0: return (lim_tau,lim_len,lim_phi)[kind]
            r=a+(b-a)*t*t; w,k,pr,B=base(r); dr=2*(b-a)*t
            if pr<=0: return 0.0
            if kind==0: return float(gamma(r,w))*B*w/pr*dr*unit
            if kind==1: return B*k/pr*dr
            return 0.0 if L==0 or r==0 else B*L/(r*r*pr)*dr
        return tuple(float(quad(lambda t:f(t,j),0,1,epsabs=1e-10,epsrel=2e-8,limit=300)[0]) for j in range(3))
    def vals(r):
        w,k,pr,B=base(r)
        if pr<=0: raise ValueError("radial segment crosses a turning point")
        return w,k,pr,B
    tau=quad(lambda r:float(gamma(r,vals(r)[0]))*vals(r)[3]*vals(r)[0]/vals(r)[2]*unit,a,b,epsabs=1e-10,epsrel=2e-8,limit=300)[0]
    ell=quad(lambda r:vals(r)[3]*vals(r)[1]/vals(r)[2],a,b,epsabs=1e-10,epsrel=2e-8,limit=300)[0]
    phi=quad(lambda r:0.0 if L==0 or r==0 else vals(r)[3]*L/(r*r*vals(r)[2]),a,b,epsabs=1e-10,epsrel=2e-8,limit=300)[0]
    return float(tau),float(ell),float(phi)

def propagate_ray(metric:StaticSphericalMetric,*,mass_MeV:float,source_radius_km:float,
                  source_local_energy_MeV:float,source_mu:float,
                  gamma_abs_star:Callable[[float,float],float],r_max_km:float|None=None,
                  length_to_mev_inv:float=KM_TO_MEV_INV)->RayResult:
    if mass_MeV<=0 or source_local_energy_MeV<=mass_MeV: raise ValueError("require mass>0 and source energy>mass")
    if not -1<=source_mu<=1: raise ValueError("source_mu must lie in [-1,1]")
    rs=float(source_radius_km); rmax=metric.r_max if r_max_km is None else float(r_max_km)
    if not metric.r_min<=rs<=rmax<=metric.r_max: raise ValueError("source/rmax outside metric table")
    E=float(metric.N(rs))*float(source_local_energy_MeV)
    if E<=mass_MeV:
        return RayResult(False,E,0,None,float("inf"),0,0,tuple(),"E_infinity <= mass")
    ks=np.sqrt(source_local_energy_MeV**2-mass_MeV**2)
    L=rs*ks*np.sqrt(max(1-source_mu**2,0))
    p2s=float(radial_momentum_squared(metric,mass_MeV,E,L,rs))
    if p2s < -1e-8*max(ks*ks,1): raise ValueError("inconsistent source direction")
    turning=None
    if source_mu < -1e-12:
        if L<=1e-14:
            if metric.r_min>0:
                return RayResult(False,E,L,None,float("inf"),0,0,tuple(),"radial inward ray needs metric through centre")
            t1,l1,p1=_segment(metric,mass_MeV,E,L,0,rs,gamma_abs_star,length_to_mev_inv)
            t2,l2,p2=_segment(metric,mass_MeV,E,L,0,rmax,gamma_abs_star,length_to_mev_inv)
            return RayResult(True,E,L,0,t1+t2,l1+l2,p1+p2,((0,rs),(0,rmax)),"radial ray crosses centre")
        turning=_first_root(metric,mass_MeV,E,L,metric.r_min,rs,-1)
        if turning is None:
            return RayResult(False,E,L,None,float("inf"),0,0,tuple(),"no inner turning point")
        scan=np.linspace(turning+max(1e-10,(rmax-turning)*1e-9),rmax,1025)
        if np.any(np.asarray(radial_momentum_squared(metric,mass_MeV,E,L,scan))<=0):
            return RayResult(False,E,L,turning,float("inf"),0,0,tuple(),"outer forbidden region")
        ti,li,pi=_segment(metric,mass_MeV,E,L,turning,rs,gamma_abs_star,length_to_mev_inv,True)
        to,lo,po=_segment(metric,mass_MeV,E,L,turning,rmax,gamma_abs_star,length_to_mev_inv,True)
        return RayResult(True,E,L,turning,ti+to,li+lo,pi+po,((turning,rs),(turning,rmax)),"inward ray turns and escapes")
    tangent=abs(source_mu)<=1e-12
    start=rs+max(1e-10,(rmax-rs)*1e-9) if tangent else rs
    scan=np.linspace(start,rmax,1025)
    if np.any(np.asarray(radial_momentum_squared(metric,mass_MeV,E,L,scan))<=0):
        root=_first_root(metric,mass_MeV,E,L,start,rmax,1)
        return RayResult(False,E,L,root,float("inf"),0,0,tuple(),"outward forbidden region")
    tau,ell,phi=_segment(metric,mass_MeV,E,L,rs,rmax,gamma_abs_star,length_to_mev_inv,tangent)
    return RayResult(True,E,L,None,tau,ell,phi,((rs,rmax),),"outward ray escapes")
