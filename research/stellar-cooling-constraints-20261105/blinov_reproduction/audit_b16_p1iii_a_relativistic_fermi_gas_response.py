#!/usr/bin/env python3
"""Relativistic finite-T free-Fermi-gas density response for P1-IIIa."""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.special import expit

HBARC, N0, T, YP = 197.3269804, 0.16, 3.03, 0.10
MASS = {"n": 939.56542052, "p": 938.27208816}
DENSITIES = (1.e-3, 1.e-2, 1.e-1)
QVALUES = (30., 100., 200., 300., 500.)

def pmax(mu, mass, tail=80.):
    e = max(mass, mu) + tail*T
    return math.sqrt(max(0., e*e-mass*mass))

def density(mu, mass, order=600):
    pm = pmax(mu, mass, 40.)
    x,w = leggauss(order)
    p,wp = .5*pm*(x+1), .5*pm*w
    f = expit((mu-np.sqrt(p*p+mass*mass))/T)
    return float(np.sum(wp*p*p*f)/(math.pi**2*HBARC**3))

def solve_mu(n, mass):
    return float(brentq(lambda m: density(m,mass)-n,
                        mass-250*T-2000., mass+1000., xtol=1.e-11, rtol=1.e-13))

def pmin(q0,q,m):
    if q<=abs(q0) or q<=0: return math.inf
    a=q0/q
    A=(q0*q0-q*q)/(2*q)
    eb=(a*A+math.sqrt(A*A+(1-a*a)*m*m))/(1-a*a)
    return abs(a*eb+A)

def S(q0,q,mu,m,order=600,pauli=True):
    if q<=abs(q0) or q<=0: return 0.
    lo,hi=pmin(q0,q,m),pmax(mu,m)
    if lo>=hi: return 0.
    x,w=leggauss(order)
    p=.5*(hi-lo)*x+.5*(hi+lo)
    wp=.5*(hi-lo)*w
    ei=np.sqrt(p*p+m*m)
    ef=ei+q0
    fi=expit((mu-ei)/T)
    ff=expit((mu-ef)/T)
    block=1-ff if pauli else 1.
    return float(np.sum(wp*p*ef*fi*block)/(math.pi*q))

def S_nr(q0,q,mu,m):
    if q<=abs(q0) or q<=0 or q0==0: return 0.
    pz=m*q0/q-q/2
    eperp=pz*pz/(2*m)
    a=(mu-m-eperp)/T
    b=(mu-m-eperp-q0)/T
    lr=np.logaddexp(0.,a)-np.logaddexp(0.,b)
    return float(m*m*T/(math.pi*q)*lr/(-math.expm1(-q0/T)))

def static_direct(q,mu,m,order=240):
    pm=pmax(mu,m)
    x,w=leggauss(order)
    p=.5*pm*(x+1); wp=.5*pm*w
    c,wc=leggauss(order)
    ei=np.sqrt(p[:,None]**2+m*m)
    ef=np.sqrt(p[:,None]**2+q*q+2*p[:,None]*q*c[None,:]+m*m)
    fi=expit((mu-ei)/T); ff=expit((mu-ef)/T)
    return float(np.sum(wp[:,None]*wc[None,:]*p[:,None]**2*fi*(1-ff))/(2*math.pi**2))

def spectrum(q,mu,m,order=240):
    x,w=leggauss(order); q0=q*x; wq=q*w
    vals=np.array([S(float(z),q,mu,m,order=order) for z in q0])
    norm=np.sum(wq*vals)
    mean=np.sum(wq*q0*vals)/norm
    sig=math.sqrt(np.sum(wq*(q0-mean)**2*vals)/norm)
    up=np.sum(wq[q0<0]*vals[q0<0])/norm
    stat=norm/(2*math.pi)
    stat2=static_direct(q,mu,m,order)
    return {"mean_q0_MeV":float(mean),"sigma_q0_MeV":float(sig),
            "upscatter_response_fraction":float(up),
            "sum_rule_relative_residual":float(stat/stat2-1.)}

def build():
    thermo=[]; pauli=[]; spectra=[]; dbmax=0.; qconv=0.; nr=[]
    densmax=0.; summax=0.
    for d in DENSITIES:
        nb=d*N0
        for sp in ("n","p"):
            frac=1-YP if sp=="n" else YP
            n=frac*nb; m=MASS[sp]; mu=solve_mu(n,m)
            densmax=max(densmax,abs(density(mu,m,900)/n-1))
            pf=HBARC*(3*math.pi**2*n)**(1/3)
            thermo.append({"nB_over_n0":d,"species":sp,"n_species_fm3":n,
                           "mu_minus_M_MeV":mu-m,"pF_MeV":pf,
                           "fugacity_exp_mu_minus_M_over_T":math.exp((mu-m)/T)})
            for q in QVALUES:
                q0=math.sqrt(m*m+q*q)-m
                sb=S(q0,q,mu,m,600,True); su=S(q0,q,mu,m,600,False)
                pauli.append({"nB_over_n0":d,"species":sp,"q_MeV":q,
                              "q0_stationary_recoil_MeV":q0,
                              "Pauli_suppression_ratio":sb/su})
                s300=S(q0,q,mu,m,300); s900=S(q0,q,mu,m,900)
                qconv=max(qconv,abs(s300/s900-1))
            for q in (30.,100.,500.):
                for fracq in ((.1,.5,.9) if q<500 else (.1,.5)):
                    q0=fracq*q
                    spv=S(q0,q,mu,m,500); smv=S(-q0,q,mu,m,500)
                    if spv>0 and smv>0:
                        dbmax=max(dbmax,abs((smv/spv)/math.exp(-q0/T)-1))
            if d in (1.e-3,1.e-1):
                for q in (5.,30.,100.,200.,300.,500.):
                    q0=math.sqrt(m*m+q*q)-m
                    sr=S(q0,q,mu,m,800)
                    sn=S_nr(q0,q,mu,m)
                    if sp=="n" and d==1.e-3:
                        nr.append({"q_MeV":q,"relativistic_over_NR_minus1":sr/sn-1})
    for d in (1.e-3,1.e-1):
        for sp in ("n","p"):
            n=(1-YP if sp=="n" else YP)*d*N0
            m=MASS[sp]; mu=solve_mu(n,m)
            for q in (30.,100.,200.,500.):
                row=spectrum(q,mu,m)
                row.update({"nB_over_n0":d,"species":sp,"q_MeV":q,
                            "q0_stationary_recoil_MeV":math.sqrt(m*m+q*q)-m})
                spectra.append(row)
                summax=max(summax,abs(row["sum_rule_relative_residual"]))
    lowq=max(abs(r["relativistic_over_NR_minus1"]) for r in nr if r["q_MeV"]<=30.)
    q500=next(r["relativistic_over_NR_minus1"] for r in nr if r["q_MeV"]==500.)
    return {
      "title":"P1-IIIa relativistic finite-temperature free-Fermi-gas dynamic density response",
      "date":"2026-11-10",
      "scope":"Scalar density response only; not yet the complete vector/axial weak collision kernel.",
      "literature_basis":"Reddy, Prakash & Lattimer, PRD 58, 013009 (1998), Eqs. (14), (16), (17). The relativistic dispersion is an explicit extension of their free-gas phase-space integral.",
      "benchmark":{"T_MeV":T,"Yp":YP,"nB_over_n0":list(DENSITIES),
                   "n0_fm3":N0,"dispersion":"sqrt(p^2+M^2), U=0, m*=M",
                   "Yp_status":"Illustrative fixed-composition benchmark, not extracted from SFHo-18.8."},
      "definition":"S_N(q0,q)=2 int d3p/(2pi)^3 2pi delta(q0+E_p-E_{p+q}) f(p)[1-f(p+q)]",
      "units":"S_N: MeV^2; integral dq0/(2pi) S_N: MeV^3",
      "thermodynamics":thermo,"pauli_blocking_at_stationary_recoil_line":pauli,
      "response_spectrum_moments":spectra,
      "nonrelativistic_limit_checks_low_density_neutron":nr,
      "validation":{"density_equation_max_relative_residual":densmax,
                    "detailed_balance_max_relative_residual":dbmax,
                    "static_sum_rule_max_relative_residual":summax,
                    "300_vs_900_node_max_relative_difference":qconv,
                    "relativistic_vs_NR_max_difference_q_le_30_MeV":lowq,
                    "relativistic_vs_NR_difference_q_500_MeV":q500},
      "limitations":["No weak-current tensor or leptonic contraction yet.",
        "No weak magnetism or finite nucleon form factors in this scalar response.",
        "No mean fields, effective masses, RPA, NN correlations, or other baryons.",
        "No neutrino final-state blocking.",
        "The response-spectrum upscattering fraction is not a final neutrino energy-gain probability.",
        "Yp=0.10 is illustrative and must be replaced by a same-snapshot SFHo-18.8 composition profile."]
    }

def main():
    payload=build()
    out=Path(__file__).resolve().parent/"outputs"/"p1iii_a_relativistic_fermi_gas_response_2026-11-10.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,indent=2)+"\n")
    print(json.dumps({"output":str(out),"validation":payload["validation"]},indent=2))

if __name__=="__main__": main()
