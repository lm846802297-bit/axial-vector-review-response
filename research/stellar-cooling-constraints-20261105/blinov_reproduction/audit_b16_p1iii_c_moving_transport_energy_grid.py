#!/usr/bin/env python3
"""P1-IIIc energy-grid extension of the moving finite-T nu-N collision kernel."""
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

ENERGIES=(50.,100.,150.,255.,500.)
T=3.03
YP=.10
NB_OVER_N0=1.e-3
NSIGMA=7.

def integrated_moments(E,target,antinu,n_theta=8,n_ep=24,order_p=20,order_phi=6,nsigma=NSIGMA):
    """Integrate E' and solid angle, using an angle-dependent thermal window."""
    mass=moving.MASS[target]
    nB=NB_OVER_N0*moving.N0
    n_species=((1.-YP) if target=="n" else YP)*nB
    mu=moving.solve_mu(n_species,mass,T)

    s,w=leggauss(n_theta)
    s=.5*(s+1.)
    w=.5*w
    medium=np.zeros(4)
    stationary=np.zeros(4)
    widths=[]

    for ss,ww in zip(s,w):
        costh=1.-2.*ss*ss
        jac=4.*ss*ww
        ep0=E/(1.+E/mass*(1.-costh))
        q=math.sqrt(max(0.,E*E+ep0*ep0-2.*E*ep0*costh))
        half_width=max(.5,nsigma*q*math.sqrt(T/mass))
        widths.append(half_width)
        ep_lo=max(1.e-8,ep0-half_width)
        ep_hi=ep0+half_width

        x,we=leggauss(n_ep)
        eps=.5*(ep_hi-ep_lo)*x+.5*(ep_hi+ep_lo)
        we=.5*(ep_hi-ep_lo)*we
        vals=np.zeros(3)
        for ep,weight in zip(eps,we):
            rate=moving.differential_rate(
                E,float(ep),float(costh),target,antinu,T,mu,order_p,order_phi,True
            )
            vals+=weight*rate*np.array([1.,1.-ep/E,1.-(ep/E)*costh])

        dtotal=vals[0]/(n_species*moving.HBARC**3)
        dloss=vals[1]/(n_species*moving.HBARC**3)
        dmom=vals[2]/(n_species*moving.HBARC**3)
        medium+=2.*math.pi*jac*np.array([
            dtotal,dtotal*(1.-costh),dmom,dloss
        ])

        ds=moving.kernel.evaluate(E,float(costh),target,antinu)["dsdo"]
        eta=1./(1.+E/mass*(1.-costh))
        stationary+=2.*math.pi*jac*ds*np.array([
            1.,1.-costh,1.-eta*costh,1.-eta
        ])

    cm2=(1.973269804e-11)**2
    return {
        "E_MeV":E,
        "target":target,
        "species":"antinu" if antinu else "nu",
        "mu_minus_M_MeV":mu-mass,
        "medium_1e-40_cm2":(medium*cm2/1.e-40).tolist(),
        "stationary_1e-40_cm2":(stationary*cm2/1.e-40).tolist(),
        "medium_over_stationary":(medium/stationary).tolist(),
        "energy_window_halfwidth_minmax_MeV":[float(min(widths)),float(max(widths))]
    }

def main():
    rows=[]
    for energy in ENERGIES:
        for target in ("n","p"):
            for antinu in (False,True):
                rows.append(integrated_moments(energy,target,antinu))

    payload={
      "title":"P1-IIIc moving-nucleon finite-temperature transport-moment energy grid",
      "date":"2026-11-10",
      "benchmark":{
        "T_MeV":T,"Yp":YP,"nB_over_n0":NB_OVER_N0,"n0_fm3":moving.N0,
        "composition_status":"Illustrative ideal-gas composition; not extracted from a same-snapshot SFHo-18.8 profile."
      },
      "incident_energies_MeV":list(ENERGIES),
      "moment_order":["total","angular_transport","momentum_transfer","net_energy_loss"],
      "units":"Cross sections in 1e-40 cm^2; ratios are moving finite-T / stationary Horowitz.",
      "energy_window":"At each angle integrate Eprime over [max(1e-8,Eprime_stationary - 7*q*sqrt(T/M)), Eprime_stationary + 7*q*sqrt(T/M)]; q and Eprime_stationary are evaluated at the stationary recoil point. The half-width is floored at 0.5 MeV.",
      "baseline_quadrature":{"transformed_angle":8,"outgoing_energy":24,"initial_nucleon_momentum":20,"azimuth":6,"energy_window_nsigma":7},
      "results":rows,
      "scope":"Local free relativistic nucleon collision kernel at one illustrative thermodynamic point. Not a radial opacity, energy-sphere calculation, Boltzmann transport solution, or B.2 escape probability.",
      "limitations":[
        "Yp=0.10, T=3.03 MeV, and nB/n0=1e-3 are illustrative inputs, not a same-snapshot SFHo-18.8 radial profile.",
        "No EOS effective masses or mean fields, RPA, NN correlations, strange axial form factor, additional baryons, or neutrino final-state blocking.",
        "Baseline grid uses moderate quadrature; selected higher-order spot checks and energy-window tests are documented in the companion report.",
        "No B.2 opacity, pure-vector Fig. 7 baseline, or axial-vector cooling curve is modified."
      ]
    }
    out=HERE/"outputs"/"p1iii_c_moving_transport_energy_grid_2026-11-10.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(out),"rows":len(rows)},indent=2))

if __name__=="__main__":
    main()
