#!/usr/bin/env python3
"""Energy/angle-integrated transport moments of the P1-IIIb moving kernel."""
from __future__ import annotations
import importlib.util, json, math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent
MOVING_PATH=HERE/"audit_b16_p1iii_b_moving_fermi_gas_collision_kernel.py"
spec=importlib.util.spec_from_file_location("p1iii_b_moving_kernel",MOVING_PATH)
moving=importlib.util.module_from_spec(spec)
spec.loader.exec_module(moving)

def angle_energy_moments(E,costh,target,antinu,T,mu,span,n_ep,order_p,order_phi,pauli=True):
    mass=moving.MASS[target]
    ep0=E/(1.+E/mass*(1.-costh))
    x,w=leggauss(n_ep); eps=ep0+span*x
    vals=np.zeros(3)
    for ep,ww in zip(eps,w):
        rate=moving.differential_rate(E,float(ep),costh,target,antinu,T,mu,
                                     order_p,order_phi,pauli)
        vals += ww*span*rate*np.array([1.,1.-ep/E,1.-(ep/E)*costh])
    return vals

def integrated_moments(E=100.,target="n",antinu=False,nB_over_n0=1.e-3,Yp=.10,T=3.03,
                       n_theta=16,n_ep=48,order_p=48,order_phi=16,span=60.):
    nB=nB_over_n0*moving.N0
    n_species=((1.-Yp) if target=="n" else Yp)*nB
    mu=moving.solve_mu(n_species,moving.MASS[target],T)
    s,w=leggauss(n_theta); s=.5*(s+1.); w=.5*w
    medium=np.zeros(4); stationary=np.zeros(4)
    for ss,ww in zip(s,w):
        costh=1.-2.*ss*ss
        jac=4.*ss*ww
        v=angle_energy_moments(E,float(costh),target,antinu,T,mu,span,n_ep,order_p,order_phi,True)
        dtotal=v[0]/(n_species*moving.HBARC**3)
        dloss=v[1]/(n_species*moving.HBARC**3)
        dmom=v[2]/(n_species*moving.HBARC**3)
        medium += 2.*math.pi*jac*np.array([dtotal,dtotal*(1.-costh),dmom,dloss])
        h=moving.kernel.evaluate(E,float(costh),target,antinu)
        ds=h["dsdo"]
        eta=1./(1.+E/moving.MASS[target]*(1.-costh))
        stationary += 2.*math.pi*jac*np.array([ds,ds*(1.-costh),ds*(1.-eta*costh),ds*(1.-eta)])
    ratio=medium/stationary
    cm2=1.973269804e-11**2
    return {
      "target":target,"species":"antinu" if antinu else "nu",
      "E_MeV":E,"T_MeV":T,"Yp":Yp,"nB_over_n0":nB_over_n0,
      "mu_minus_M_MeV":mu-moving.MASS[target],
      "moment_order":["total","angular_transport","momentum_transfer","energy_loss"],
      "medium_1e-40_cm2":(medium*cm2/1.e-40).tolist(),
      "stationary_1e-40_cm2":(stationary*cm2/1.e-40).tolist(),
      "medium_over_stationary":ratio.tolist(),
      "quadrature":{"transformed_angle":n_theta,"outgoing_energy":n_ep,
                    "initial_p":order_p,"azimuth":order_phi,"Eprime_half_width_MeV":span}
    }

def build():
    rows=[]
    for ntheta in (8,16):
        rows.append(integrated_moments(n_theta=ntheta))
    return {
      "title":"P1-IIIb energy/angle-integrated moving-nucleon transport moments",
      "date":"2026-11-10",
      "definition":"Moments are integrated over outgoing E' and solid angle; energy loss uses 1-E'/E and momentum transfer uses 1-(E'/E)cos(theta).",
      "angular_transform":"s=sqrt((1-cos(theta))/2), cos(theta)=1-2s^2, dcos(theta)=4s ds; this clusters quadrature near the forward direction.",
      "results":rows,
      "scope":"Local ideal-gas free-nucleon collision kernel only; not a radial opacity or escape calculation."
    }

if __name__=="__main__":
    out=build()
    path=HERE/"outputs"/"p1iii_b_moving_transport_moments_2026-11-10.json"
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
