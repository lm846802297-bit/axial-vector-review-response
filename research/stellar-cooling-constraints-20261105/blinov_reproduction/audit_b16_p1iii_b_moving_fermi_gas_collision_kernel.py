#!/usr/bin/env python3
"""Finite-T moving-nucleon NC collision kernel using the P1-IIIb Dirac trace."""
from __future__ import annotations
import importlib.util, json, math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.special import expit

HERE=Path(__file__).resolve().parent
KERNEL_PATH=HERE/"audit_b16_p1iii_b_stationary_dirac_trace.py"
spec=importlib.util.spec_from_file_location("p1iii_b_stationary_kernel",KERNEL_PATH)
kernel=importlib.util.module_from_spec(spec)
spec.loader.exec_module(kernel)
HBARC=197.3269804; N0=0.16; GF=1.1663787e-11
METRIC=kernel.METRIC; GAMMA=kernel.GAMMA; GAMMA5=kernel.GAMMA5
SIGMA=kernel.SIGMA; IDENT=kernel.IDENT; MASS=kernel.MASS

def pmax(mu,mass,T,tail=40.):
    e=max(mass,mu)+tail*T
    return math.sqrt(max(0.,e*e-mass*mass))

def number_density(mu,mass,T,order=500):
    pm=pmax(mu,mass,T,40.)
    x,w=leggauss(order); p=.5*pm*(x+1.); wp=.5*pm*w
    f=expit((mu-np.sqrt(p*p+mass*mass))/T)
    return float(np.sum(wp*p*p*f)/(math.pi**2*HBARC**3))

def solve_mu(n_fm3,mass,T):
    return float(brentq(lambda mu:number_density(mu,mass,T)-n_fm3,
                        mass-200*T-1000.,mass+1000.,xtol=1.e-11,rtol=1.e-13))

def pmin_rel(q0,q,mass):
    if q<=abs(q0) or q<=0.: return math.inf
    a=q0/q; A=(q0*q0-q*q)/(2*q)
    eb=(a*A+math.sqrt(A*A+(1-a*a)*mass*mass))/(1-a*a)
    return abs(a*eb+A)

def precompute(E,Ep,costh,target,antinu):
    mass=MASS[target]; sint=math.sqrt(max(0.,1.-costh*costh))
    k=np.array([E,0.,0.,E]); kp=np.array([Ep,Ep*sint,0.,Ep*costh])
    q=k-kp; qvec=q[1:]; qmag=float(np.linalg.norm(qvec)); q0=float(q[0])
    qhat=qvec/qmag; khat=k[1:]/E
    e1=khat-np.dot(khat,qhat)*qhat; en=float(np.linalg.norm(e1))
    if en<1.e-12: e1=np.array([0.,1.,0.])
    else: e1=e1/en
    e2=np.cross(qhat,e1); Q2=qmag*qmag-q0*q0
    cv,ca,f2=kernel.ff(Q2,target,mass); vertex=[]
    for mu in range(4):
        pauli=sum(SIGMA[mu][nu]*METRIC[nu]*q[nu] for nu in range(4))
        vertex.append(cv*GAMMA[mu]+1j*f2/(2.*mass)*pauli-ca*GAMMA[mu]@GAMMA5)
    barred=[kernel.dbar(g) for g in vertex]
    first,second=(kernel.slash(k),kernel.slash(kp)) if antinu else (kernel.slash(kp),kernel.slash(k))
    L=np.array([[np.trace(first@(METRIC[mu]*GAMMA[mu])@(IDENT-GAMMA5)
                            @second@(METRIC[nu]*GAMMA[nu])@(IDENT-GAMMA5))
                 for nu in range(4)] for mu in range(4)])
    return {"mass":mass,"q0":q0,"qmag":qmag,"qhat":qhat,"e1":e1,"e2":e2,
            "qvec":qvec,"vertex":vertex,"barred":barred,"L":L}

def contract_moving(pre,p,phi):
    mass=pre["mass"]; q0=pre["q0"]; qmag=pre["qmag"]
    ei=math.sqrt(p*p+mass*mass)
    c=(2.*ei*q0+q0*q0-qmag*qmag)/(2.*p*qmag) if p>1.e-14 else 0.
    if abs(c)>1.+2.e-10: return 0.
    c=max(-1.,min(1.,c)); s=math.sqrt(max(0.,1.-c*c))
    pvec=p*(c*pre["qhat"]+s*(math.cos(phi)*pre["e1"]+math.sin(phi)*pre["e2"]))
    ppvec=pvec+pre["qvec"]; ef=ei+q0
    pp_shell=math.sqrt(float(np.dot(ppvec,ppvec))+mass*mass)
    if abs(pp_shell-ef)>2.e-9*max(1.,ef):
        raise ArithmeticError("Energy-shell closure failed in moving-nucleon kernel")
    pi=np.array([ei,*pvec]); pf=np.array([ef,*ppvec])
    Si=kernel.slash(pi)+mass*IDENT; Sf=kernel.slash(pf)+mass*IDENT
    A=np.zeros((4,4),dtype=complex)
    for mu in range(4):
        left=pre["vertex"][mu]@Si
        for nu in range(4):
            A += pre["L"][mu,nu]*(left@pre["barred"][nu])
    return float((.5*np.trace(Sf@A)).real)

def differential_rate(E,Ep,costh,target,antinu,T,mu,order_p=48,order_phi=16,pauli=True):
    pre=precompute(E,Ep,costh,target,antinu); q=pre["qmag"]; q0=pre["q0"]; mass=pre["mass"]
    if q<=abs(q0) or q<=0.: return 0.
    lo=pmin_rel(q0,q,mass); hi=pmax(mu,mass,T)
    if lo>=hi: return 0.
    x,w=leggauss(order_p); ps=.5*(hi-lo)*(x+1.)+lo; wp=.5*(hi-lo)*w
    phis=2.*math.pi*(np.arange(order_phi)+.5)/order_phi; integral=0.
    for p,weight in zip(ps,wp):
        ei=math.sqrt(p*p+mass*mass); ef=ei+q0
        fi=expit((mu-ei)/T); block=(1.-expit((mu-ef)/T)) if pauli else 1.
        if fi<1.e-300 or block<1.e-15: continue
        azimuthal=sum(contract_moving(pre,float(p),float(phi)) for phi in phis)/order_phi
        integral += weight*p/ei*fi*block*azimuthal
    return GF**2*Ep/(256.*math.pi**4*E*q)*integral

def integrated_angular_rate(E,costh,target,antinu,T,mu,span,n_ep,order_p,order_phi,pauli=True):
    mass=MASS[target]; ep0=E/(1.+E/mass*(1.-costh))
    x,w=leggauss(n_ep); eps=ep0+span*x
    if np.min(eps)<=0.: raise ValueError("Outgoing-energy interval crossed E'=0")
    rates=[differential_rate(E,float(ep),costh,target,antinu,T,mu,order_p,order_phi,pauli) for ep in eps]
    return float(np.sum(w*span*np.asarray(rates)))

def benchmark(target,antinu,nB_over_n0,Yp,T,E,costh,span,n_ep,order_p,order_phi,pauli=True):
    nB=nB_over_n0*N0; fraction=(1.-Yp) if target=="n" else Yp
    n_species=fraction*nB; mu=solve_mu(n_species,MASS[target],T)
    gamma=integrated_angular_rate(E,costh,target,antinu,T,mu,span,n_ep,order_p,order_phi,pauli)
    sigma_stationary=kernel.evaluate(E,costh,target,antinu)["dsdo"]
    ratio=gamma/(n_species*HBARC**3)/sigma_stationary
    return {"target":target,"species":"antinu" if antinu else "nu","nB_over_n0":nB_over_n0,
            "Yp":Yp,"T_MeV":T,"E_MeV":E,"cos_theta":costh,
            "mu_minus_M_MeV":mu-MASS[target],"pauli_blocking":pauli,
            "ratio_to_stationary_dsigma_dOmega":ratio,
            "quadrature":{"outgoing_energy":n_ep,"initial_p":order_p,"azimuth":order_phi,"Eprime_half_width_MeV":span}}

def build():
    cold=[]
    for target in ("n","p"):
        for antinu in (False,True):
            cold.append(benchmark(target,antinu,1.e-10,.10,.001,100.,-.5,2.5,128,32,16,True))
    dilute=[]
    for target in ("n","p"):
        for antinu in (False,True):
            dilute.append(benchmark(target,antinu,1.e-3,.10,3.03,100.,-.5,60.,48,48,16,True))
    density_scan=[]
    for d in (1.e-3,1.e-2,1.e-1):
        unblocked=benchmark("n",False,d,.10,3.03,100.,-.5,60.,48,48,16,False)
        blocked=benchmark("n",False,d,.10,3.03,100.,-.5,60.,48,48,16,True)
        density_scan.append({"nB_over_n0":d,
          "ratio_without_final_state_blocking":unblocked["ratio_to_stationary_dsigma_dOmega"],
          "ratio_with_final_state_blocking":blocked["ratio_to_stationary_dsigma_dOmega"],
          "final_state_blocking_factor":blocked["ratio_to_stationary_dsigma_dOmega"]/unblocked["ratio_to_stationary_dsigma_dOmega"]})
    conv=[]
    for n_ep,n_p,n_phi in ((32,32,12),(48,48,16),(64,64,20)):
        r=benchmark("n",False,1.e-3,.10,3.03,100.,-.5,60.,n_ep,n_p,n_phi,True)
        conv.append({"orders":[n_ep,n_p,n_phi],"ratio":r["ratio_to_stationary_dsigma_dOmega"]})
    span_conv=[]
    for span in (40.,50.,60.):
        r=benchmark("n",False,1.e-3,.10,3.03,100.,-.5,span,48,48,16,True)
        span_conv.append({"Eprime_half_width_MeV":span,"ratio":r["ratio_to_stationary_dsigma_dOmega"]})
    return {"title":"P1-IIIb moving-nucleon finite-temperature weak collision-kernel benchmarks",
      "date":"2026-11-10",
      "definition":"dGamma/(dEprime dOmega) = GF^2 Eprime/(256 pi^4 E q) int dp (p/Ep) f_i(1-f_f) <L_munu H^munu>_phi",
      "normalization":"f is per spin state; H=1/2 Dirac trace; spin sum is included once. Cold dilute limit is normalized to n_species*sigma_Horowitz.",
      "cold_dilute_limit":cold,"finite_temperature_dilute_benchmark":dilute,
      "neutron_nu_density_scan":density_scan,
      "dilute_benchmark_quadrature_convergence":conv,
      "outgoing_energy_window_convergence":span_conv,
      "limitations":["Free relativistic nucleons with vacuum Horowitz form factors only.",
        "Yp=0.10 and density points are illustrative ideal-gas benchmarks, not extracted SFHo-18.8 profiles.",
        "No RPA, NN correlations, mean fields, additional baryons, or EOS-consistent effective masses.",
        "The reported ratio is a local fixed-angle differential cross-section ratio after integrating Eprime, not a total opacity or radial escape probability.",
        "No B.2, pure-vector Fig. 7, or axial cooling curve is modified."]}

if __name__=="__main__":
    result=build()
    out=HERE/"outputs"/"p1iii_b_moving_fermi_gas_collision_kernel_2026-11-10.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(out),"cold":result["cold_dilute_limit"],
                      "dilute":result["finite_temperature_dilute_benchmark"],
                      "density_scan":result["neutron_nu_density_scan"],
                      "quadrature":result["dilute_benchmark_quadrature_convergence"],
                      "window":result["outgoing_energy_window_convergence"]},indent=2))
