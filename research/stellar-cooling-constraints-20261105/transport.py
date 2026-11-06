"""Stationary spherical ballistic cooling, mode-resolved reduced absorption.

Implements the transport prescription of arXiv:2511.09619v2 Eqs17-21.
Lengths are km at the API boundary; energies/rates use MeV, hbar=c=1.
This is fixed-profile post-processing, not hydrodynamics or full GR transport.
"""
import numpy as np
from scipy.special import expit
from numpy.polynomial.legendre import leggauss
KM_IN_MEV_INV=1e18/197.3269804
MEV2_IN_ERG_PER_S=1.602176634e-6/6.582119569e-22
M_MU=105.6583755

def radial_rule(radius,order):
    # Composite quadrature resolves the surface and the hot muon-rich shell.
    edges=np.unique(np.r_[0,np.array([5,8,10,12,15,18,20,22,24])[np.array([5,8,10,12,15,18,20,22,24])<radius],radius])
    n=max(4,int(np.ceil(order/(len(edges)-1))))
    x,w=leggauss(n)
    return (np.concatenate([(a+b)/2+(b-a)*x/2 for a,b in zip(edges[:-1],edges[1:])]),
            np.concatenate([(b-a)*w/2 for a,b in zip(edges[:-1],edges[1:])]))

def effective_muon_density(T,mu,order=100):
    """2 spin states for each charge, integral f(1-f), MeV^3."""
    T,mu=np.broadcast_arrays(np.asarray(T),np.asarray(mu))
    x,w=leggauss(order)
    pmax=np.maximum(20*T, np.sqrt(np.maximum(mu*mu-M_MU*M_MU,0))+15*T)
    p=pmax[...,None]*(1+x)/2
    E=np.sqrt(p*p+M_MU*M_MU)
    fminus=expit((mu[...,None]-E)/T[...,None])
    fplus=expit((-mu[...,None]-E)/T[...,None])
    return np.sum(w*p*p*(fminus*(1-fminus)+fplus*(1-fplus)),axis=-1)*pmax/(2*np.pi**2)

def angular_columns(r_source,radial_grid,reduced_rate,mass,energies,radius,angular_order=24,path_order=48):
    """Return unit-coupling tau [source,angle,energy,mode], angular weights."""
    r=np.asarray(r_source)[:,None]
    c,wa=leggauss(angular_order)
    x,ws=leggauss(path_order); ws=ws/2
    v=np.sqrt(1-(mass/np.asarray(energies))**2)
    columns=[]
    for cost in c:
        smax=-r*cost+np.sqrt(radius**2-r*r+r*r*cost*cost)
        s=smax*(1+x[None,:])/2
        pos=np.sqrt(np.maximum(r*r+s*s+2*r*s*cost,0))
        j=np.clip(np.searchsorted(radial_grid,pos)-1,0,len(radial_grid)-2)
        frac=(pos-radial_grid[j])/(radial_grid[j+1]-radial_grid[j])
        # Integrate the radial piecewise-linear basis once, then contract it
        # with every energy/mode. This avoids a large path-by-energy tensor.
        basis=np.zeros((len(r_source),len(radial_grid)))
        row=np.broadcast_to(np.arange(len(r_source))[:,None],j.shape)
        np.add.at(basis,(row.ravel(),j.ravel()),(smax*ws*(1-frac)).ravel())
        np.add.at(basis,(row.ravel(),(j+1).ravel()),(smax*ws*frac).ravel())
        col=np.einsum('rj,jeh->reh',basis,reduced_rate)*KM_IN_MEV_INV/v[None,:,None]
        columns.append(col)
    return np.stack(columns,axis=1),wa/2

def luminosities(source_weights,columns,angular_weights,couplings):
    """source_weights already contains radial/energy quadrature and units."""
    result=[]
    for coupling in couplings:
        escape=np.einsum('raeh,a->reh',np.exp(-coupling**2*columns),angular_weights)
        result.append(coupling**2*np.sum(source_weights*escape))
    return np.asarray(result)

def energy_weights(energies,lower_bounds):
    """Exact integration weights for piecewise-linear f from each cutoff."""
    e=np.asarray(energies)
    low=np.asarray(lower_bounds)[:,None]
    a=np.maximum(e[:-1],low); b=np.broadcast_to(e[1:],a.shape)
    length=np.maximum(b-a,0)
    slope=np.where(length>0,((b-e[:-1])**2-(a-e[:-1])**2)/(2*np.diff(e)),0)
    w=np.zeros((len(low),len(e)))
    w[:,:-1]+=length-slope; w[:,1:]+=slope
    return w

def source_weights(r,rw,energies,lapse,prod,mass):
    e=np.asarray(energies); k=np.sqrt(e*e-mass*mass)
    ew=energy_weights(e,mass/lapse)
    geom=4*np.pi*(r*KM_IN_MEV_INV)**2*rw*KM_IN_MEV_INV*lapse**2
    phase=k*e*e/(2*np.pi**2)
    return geom[:,None,None]*ew[:,:,None]*phase[None,:,None]*prod*MEV2_IN_ERG_PER_S

def surface_blackbody(radius,T,lapse,mass,energies):
    """Three equally thermalized modes; useful unresolved-surface diagnostic."""
    e=np.asarray(energies)
    ew=energy_weights(e,np.array([mass/lapse]))[0]
    v2=1-mass**2/e**2
    return (4*np.pi*(radius*KM_IN_MEV_INV)**2*lapse**2*3/(8*np.pi**2)*
            np.sum(ew*e**3*v2/np.expm1(e/T))*MEV2_IN_ERG_PER_S)
