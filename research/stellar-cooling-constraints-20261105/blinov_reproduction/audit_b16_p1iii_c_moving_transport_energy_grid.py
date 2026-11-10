#!/usr/bin/env python3
"""P1-IIIc moving-nucleon transport moments over incident-energy grid."""
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

def integrated_moments(E,target,antinu,n_theta=8,n_ep=24,order_p=20,order_phi=6,nsigma=7.):
    mass=moving.MASS[target]
    nB=NB_OVER_N0*moving.N0
    n_species=((1.-YP) if target=="n" else YP)*nB
    mu=moving.solve_mu(n_species,mass,T)
    s,w=leggauss(n_theta); s=.5*(s+1.); w=.5*w
    medium=np.zeros(4); stationary=np.zeros(4); widths=[]
    for ss,ww in zip(s,w):
        costh=1.-2.*ss*ss
        jac=4.*ss*ww
        ep0=E/(1.+E/mass*(1.-costh))
        q=math.sqrt(max(0.,E*E+ep0*ep0-2.*E*ep0*costh))
        half_width=max(.5,nsigma*q*math.sqrt(T/mass))
        widths.append(half_width)
        ep_lo=max(1.e-8,ep0-half_width); ep_hi=ep0+half_width
        x,we=leggauss(n_ep)
        eps=.5*(ep_hi-ep_lo)*x+.5*(ep_hi+ep_lo)
        we=.5*(ep_hi-ep_lo)*we
        vals=np.zeros(3)
        for ep,weight in zip(eps,we):
            rate=moving.differential_rate(E,float(ep),float(costh),target,antinu,T,mu,order_p,order_phi,True)
            vals+=weight*rate*np.array([1.,1.-ep/E,1.-(ep/E)*costh])
        dtotal=vals[0]/(n_species*moving.HBARC**3)
        dloss=vals[1]/(n_species*moving.HBARC**3)
        dmom=vals[2]/(n_species*moving.HBARC**3)
        medium+=2.*math.pi*jac*np.array([dtotal,dtotal*(1.-costh),dmom,dloss])
        ds=moving.kernel.evaluate(E,float(costh),target,antinu)["dsdo"]
        eta=1./(1.+E/mass*(1.-costh))
        stationary+=2.*math.pi*jac*ds*np.array([1.,1.-costh,1.-eta*costh,1.-eta])
    return {
      "E_MeV":E,"target":target,"species":"antinu" if antinu else "nu",
      "mu_minus_M_MeV":mu-mass,"medium_over_stationary":(medium/stationary).tolist(),
      "energy_window_halfwidth_minmax_MeV":[float(min(widths)),float(max(widths))]
    }

def main():
    baseline=[]
    for E in ENERGIES:
        for target in ("n","p"):
            for anti in (False,True):
                baseline.append(integrated_moments(E,target,anti))

    high_specs=((50.,"n",False),(100.,"n",False),(255.,"n",False),(500.,"n",False),
                (50.,"p",True),(100.,"p",True),(255.,"p",True),(500.,"p",True),(500.,"n",True))
    high=[]
    for E,target,anti in high_specs:
        row=integrated_moments(E,target,anti,12,32,24,8,7.)
        row["quadrature"]=[12,32,24,8]
        high.append(row)

    windows=[]
    for E in ENERGIES:
        if E not in (50.,100.,255.,500.): continue
        rows=[]
        for nsigma in ((5.,7.,9.) if E==100. else (5.,9.)):
            row=integrated_moments(E,"n",False,12,32,24,8,nsigma)
            rows.append({"nsigma":nsigma,"medium_over_stationary":row["medium_over_stationary"],
                         "halfwidth_minmax_MeV":row["energy_window_halfwidth_minmax_MeV"]})
        windows.append({"E_MeV":E,"target":"n","species":"nu","rows":rows})

    max_quad=0.
    for h in high:
        b=next(x for x in baseline if x["E_MeV"]==h["E_MeV"] and x["target"]==h["target"] and x["species"]==h["species"])
        max_quad=max(max_quad,float(np.max(np.abs(np.asarray(h["medium_over_stationary"])/np.asarray(b["medium_over_stationary"])-1.))))
    max_window=0.
    for w in windows:
        r5=next(x for x in w["rows"] if x["nsigma"]==5.)
        r9=next(x for x in w["rows"] if x["nsigma"]==9.)
        max_window=max(max_window,float(np.max(np.abs(np.asarray(r5["medium_over_stationary"])/np.asarray(r9["medium_over_stationary"])-1.))))

    stationary_path=HERE/"outputs"/"p1iii_b_stationary_dirac_trace_2026-11-10.json"
    stationary_validation={}
    if stationary_path.exists():
        stationary_validation=json.loads(stationary_path.read_text(encoding="utf-8")).get("validation",{})

    payload={
      "title":"P1-IIIc moving-nucleon finite-temperature transport-moment energy grid",
      "date":"2026-11-10",
      "benchmark":{"T_MeV":T,"Yp":YP,"nB_over_n0":NB_OVER_N0,"n0_fm3":moving.N0,
                   "composition_status":"Illustrative ideal-gas composition; not extracted from a same-snapshot SFHo-18.8 profile."},
      "incident_energies_MeV":list(ENERGIES),
      "moment_order":["total","angular_transport","momentum_transfer","net_energy_loss"],
      "ratio_definition":"Moving finite-T / stationary Horowitz; each ratio array follows moment_order.",
      "energy_window":"Angle-dependent half-width max(0.5 MeV, nsigma*q*sqrt(T/M)), centered on stationary recoil Eprime and clipped at Eprime=0.",
      "baseline_quadrature":{"transformed_angle":8,"outgoing_energy":24,"initial_nucleon_momentum":20,"azimuth":6,"energy_window_nsigma":7},
      "results":baseline,"higher_order_spot_checks":high,"energy_window_convergence":windows,
      "validation":{"max_relative_difference_baseline_vs_higher_order_spot_checks":max_quad,
                    "max_window_5sigma_vs_9sigma_relative_difference":max_window,
                    "stationary_target_trace":stationary_validation},
      "scope":"Local free relativistic nucleon collision kernel at one illustrative thermodynamic point. Not a radial opacity, energy-sphere calculation, Boltzmann transport solution, or B.2 escape probability.",
      "limitations":[
        "Yp=0.10, T=3.03 MeV, and nB/n0=1e-3 are illustrative inputs, not a same-snapshot SFHo-18.8 radial profile.",
        "No EOS effective masses or mean fields, RPA, NN correlations, strange axial form factor, additional baryons, or neutrino final-state blocking.",
        "Baseline grid uses moderate quadrature; higher-order spot checks cover selected channels, not every grid point.",
        "No B.2 opacity, pure-vector Fig. 7 baseline, or axial-vector cooling curve is modified."
      ]
    }
    out=HERE/"outputs"/"p1iii_c_moving_transport_energy_grid_2026-11-10.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(out),"baseline_rows":len(baseline),"higher_order_checks":len(high),
                      "window_checks":len(windows),"validation":payload["validation"]},indent=2))

if __name__=="__main__":
    main()
