#!/usr/bin/env python3
"""Independent Dirac-trace validation of the Horowitz free-nucleon NC kernel."""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

METRIC=np.array([1.,-1.,-1.,-1.]); IDENT=np.eye(4,dtype=complex); ZERO=np.zeros((2,2),complex)
PAULI=(np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex))
GAMMA=[np.diag([1,1,-1,-1]).astype(complex)]
for s in PAULI: GAMMA.append(np.block([[ZERO,s],[-s,ZERO]]))
GAMMA5=1j*GAMMA[0]@GAMMA[1]@GAMMA[2]@GAMMA[3]
SIGMA=[[1j/2*(GAMMA[a]@GAMMA[b]-GAMMA[b]@GAMMA[a]) for b in range(4)] for a in range(4)]
MASS={"n":939.56542052,"p":938.27208816}
GF=1.1663787e-11; HBARC=1.973269804e-11; MEV2_TO_CM2=HBARC**2
SIN2W,GA0,LP,LN=.2325,1.260,1.793,-1.913
ENERGIES=(50.,100.,150.,255.,500.)
ANGLES=(-.999,-.99,-.9,-.5,0.,.5,.9,.99,.999)

def slash(v): return sum(METRIC[a]*v[a]*GAMMA[a] for a in range(4))
def dbar(a): return GAMMA[0]@a.conj().T@GAMMA[0]
def ff(Q2,t,M):
    tau=Q2/(4*M*M); etaem=1/(1+5.6*tau); gd=(1+4.97*tau)**-2
    f1p=(1+tau*(1+LP))*gd/(1+tau); f2p=LP*gd/(1+tau)
    f1n=tau*LN*(1-etaem)*gd/(1+tau); f2n=LN*(1+tau*etaem)*gd/(1+tau)
    if t=="p": return (0.5-2*SIN2W)*f1p-.5*f1n, GA0/2*(1+3.53*tau)**-2, (0.5-2*SIN2W)*f2p-.5*f2n
    return (0.5-2*SIN2W)*f1n-.5*f1p, -GA0/2*(1+3.53*tau)**-2, (0.5-2*SIN2W)*f2n-.5*f2p

def horowitz_brace(E,x,t,anti):
    M=MASS[t]; e=E/M; eta=1/(1+e*(1-x)); ep=eta*E; Q2=2*E*ep*(1-x); cv,ca,f2=ff(Q2,t,M)
    s=-1 if anti else 1
    return cv**2*(1+eta**2-eta*(1-x))+ca**2*(1+eta**2+eta*(1-x))+s*2*ca*(cv+f2)*(1-eta**2)+eta**2*e**2/2*(1-x)*(f2**2*(3-x)+4*cv*f2*(1-x))

def kin(E,x,t):
    M=MASS[t]; eta=1/(1+E/M*(1-x)); ep=eta*E; st=math.sqrt(max(0,1-x*x))
    k=np.array([E,0,0,E]); kp=np.array([ep,ep*st,0,ep*x]); p=np.array([M,0,0,0]); pp=p+k-kp; q=pp-p
    return k,kp,p,pp,q,eta,2*E*ep*(1-x)

def tensors(E,x,t):
    k,kp,p,pp,q,eta,Q2=kin(E,x,t); M=MASS[t]; cv,ca,f2=ff(Q2,t,M)
    gv=[]; ga=[]
    for mu in range(4):
        pauli=sum(SIGMA[mu][nu]*METRIC[nu]*q[nu] for nu in range(4))
        gv.append(cv*GAMMA[mu]+1j*f2/(2*M)*pauli)
        ga.append(-ca*GAMMA[mu]@GAMMA5)
    def ht(a,b):
        return np.array([[.5*np.trace((slash(pp)+M*IDENT)@a[mu]@(slash(p)+M*IDENT)@dbar(b[nu])) for nu in range(4)] for mu in range(4)])
    hvv=ht(gv,gv); haa=ht(ga,ga); hva=ht(gv,ga)+ht(ga,gv)
    return k,kp,p,pp,q,eta,Q2,hvv,haa,hva

def evaluate(E,x,t,anti):
    k,kp,p,pp,q,eta,Q2,hvv,haa,hva=tensors(E,x,t); H=hvv+haa+hva
    first,second=(slash(k),slash(kp)) if anti else (slash(kp),slash(k))
    L=np.array([[np.trace(first@(METRIC[mu]*GAMMA[mu])@(IDENT-GAMMA5)@second@(METRIC[nu]*GAMMA[nu])@(IDENT-GAMMA5)) for nu in range(4)] for mu in range(4)])
    C=np.sum(L*H).real; cvv=np.sum(L*hvv).real; caa=np.sum(L*haa).real; cva=np.sum(L*hva).real
    M=MASS[t]; e=E/M; cv,ca,f2=ff(Q2,t,M)
    bvv=cv**2*(1+eta**2-eta*(1-x))+eta**2*e**2/2*(1-x)*(f2**2*(3-x)+4*cv*f2*(1-x))
    baa=ca**2*(1+eta**2+eta*(1-x)); bva=(-1 if anti else 1)*2*ca*(cv+f2)*(1-eta**2)
    norm=32*M*M*E*E
    B=horowitz_brace(E,x,t,anti)
    ds_trace=GF**2*eta**2*C/(128*math.pi**2*M*M)
    ds_hor=GF**2*E*E*eta**2*B/(4*math.pi**2)
    ward=(METRIC*q)@hvv
    return {"res_dsigma":ds_trace/ds_hor-1,"res_brace":C/norm/B-1,
      "res_ward":np.linalg.norm(ward)/(np.linalg.norm(hvv)*np.linalg.norm(q)),
      "res_herm":np.linalg.norm(H-H.conj().T)/np.linalg.norm(H),
      "res_decomp":abs(cvv+caa+cva-C)/abs(C),
      "res_components":max(abs(a-b)/max(abs(a),abs(b),1e-30) for a,b in zip((cvv/norm,caa/norm,cva/norm),(bvv,baa,bva))),
      "VV":cvv/norm,"AA":caa/norm,"VA":cva/norm,"dsdo":ds_trace}

def moments(E,t,anti,n):
    x,w=leggauss(n); sums=np.zeros(4)
    for xx,ww in zip(x,w):
        r=evaluate(E,float(xx),t,anti); eta=1/(1+E/MASS[t]*(1-xx)); dsdx=2*math.pi*r["dsdo"]
        sums+=ww*np.array([dsdx,dsdx*(1-xx),dsdx*(1-eta*xx),dsdx*(1-eta)])
    return sums*MEV2_TO_CM2

def build():
    rows=[]; mx={k:0. for k in ("res_dsigma","res_brace","res_ward","res_herm","res_decomp","res_components")}
    for E in ENERGIES:
      for t in ("n","p"):
       for anti in (False,True):
        for x in ANGLES:
         r=evaluate(E,x,t,anti)
         for key in mx: mx[key]=max(mx[key],abs(r[key]))
         rows.append({"E_MeV":E,"target":t,"species":"antinu" if anti else "nu","cos_theta":x,
          "relative_dsigma_residual":r["res_dsigma"],"VV":r["VV"],"AA":r["AA"],"VA":r["VA"]})
    ints=[]; qmax=0.
    for E in ENERGIES:
      for t in ("n","p"):
       for anti in (False,True):
        vals={n:moments(E,t,anti,n) for n in (32,64,128,256)}; ref=vals[256]
        for n in (32,64,128): qmax=max(qmax,float(np.max(np.abs(vals[n]/ref-1))))
        ints.append({"E_MeV":E,"target":t,"species":"antinu" if anti else "nu",
          "sigma_total_1e-40_cm2":float(ref[0]/1e-40),"sigma_angular_transport_1e-40_cm2":float(ref[1]/1e-40),
          "sigma_momentum_transfer_1e-40_cm2":float(ref[2]/1e-40),"sigma_energy_loss_1e-40_cm2":float(ref[3]/1e-40)})
    mx["moment_quadrature"]=qmax
    return {"title":"P1-IIIb stationary-target Dirac-trace validation","date":"2026-11-10",
      "reference":"Horowitz, Phys. Rev. D 65, 043001 (2002)",
      "conventions":{"metric":"(+---)","q":"p'-p=k-k'","vertex":"F1 gamma^mu + i F2 sigma^{mu nu}q_nu/(2M) - GA gamma^mu gamma5",
       "H":"1/2 Tr[(p'+M)Gamma^mu(p+M)barGamma^nu]","anti":"swap k and k' in leptonic trace",
       "identity":"L_munu H^munu = 32 M^2 E_nu^2 * Horowitz_brace",
       "cross_section":"d sigma/d Omega = GF^2 eta^2 (L.H)/(128 pi^2 M^2)"},
      "grid":{"energies_MeV":list(ENERGIES),"targets":["n","p"],"species":["nu","antinu"],"cos_theta":list(ANGLES)},
      "validation":mx,"pointwise_rows":rows,"integrated_moments":ints,
      "limitations":["Stationary target only; no finite-T Fermi motion or Pauli blocking.",
       "No RPA, NN correlations, mean fields, EOS inputs, radial optical depth or B.2 escape probability."]}

if __name__=="__main__":
    result=build(); out=Path(__file__).resolve().parent/"outputs"/"p1iii_b_stationary_dirac_trace_2026-11-10.json"
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"output":str(out),"validation":result["validation"]},indent=2))
