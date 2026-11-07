"""Mode-resolved vector/axial local response scan; no transport or exclusion curve."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import sys
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0, str(ROOT))
import rates
from finite_mixing.model import muon_couplings
def stats(values):
 a=np.asarray(values,dtype=float); a=a[np.isfinite(a)]
 if not a.size:return {"n":0,"min":None,"max":None,"mean":None,"max_over_min":None}
 lo,hi=float(a.min()),float(a.max())
 return {"n":int(a.size),"min":lo,"max":hi,"mean":float(a.mean()),"max_over_min":None if lo<=0 else hi/lo}

def compton_scan():
 masses=[0.01,0.1,1.,10.,100.]; efactors=[1.001,1.05,1.5,3.,10.]
 cosines=np.linspace(-.9,.9,19); rows=[]; c=muon_couplings(1.,1e-2)
 for mass in masses:
  for ef in efactors:
   energy=mass*ef
   _,a=rates.compton_matrix_elements(mass,[energy],cosines,current="axial")
   _,v=rates.compton_matrix_elements(mass,[energy],cosines,current="vector")
   ratio=np.divide(a[0],v[0],out=np.full_like(a[0],np.nan),where=v[0]>1e-28)
   _,mixed=rates.compton_mixed_matrix_elements(mass,[energy],cosines,c.g_vector,c.g_axial)
   incoherent=c.g_vector**2*v+c.code_axial_minus_gamma5_coefficient**2*a
   interference=mixed-incoherent; denom=np.maximum(np.abs(mixed),1e-300)
   rows.append({"mass_MeV":mass,"mediator_energy_MeV":energy,"energy_over_mass":ef,
    "differential_ratio_A_over_V_by_mode":{mode:stats(ratio[:,i]) for i,mode in enumerate(rates.MODES)},
    "mixed_interference_fraction_by_mode":{mode:stats(interference[0,:,i]/denom[0,:,i]) for i,mode in enumerate(rates.MODES)}})
 integrated=[]
 for mass in masses:
  energies=np.array([mass*f for f in efactors])
  _,kv=rates.compton_kernels(mass,energies,order=96,current="vector")
  _,ka=rates.compton_kernels(mass,energies,order=96,current="axial")
  sv=kv.sum(axis=1); sa=ka.sum(axis=1)
  for j,e in enumerate(energies):
   integrated.append({"mass_MeV":mass,"mediator_energy_MeV":float(e),"energy_over_mass":float(e/mass),
    "integrated_ratio_A_over_V_by_mode":{mode:(float(sa[j,i]/sv[j,i]) if sv[j,i]>0 else None) for i,mode in enumerate(rates.MODES)},
    "integrated_ratio_polarization_sum":float(sa[j].sum()/sv[j].sum())})
 # Also integrate the actual finite-mixing current at amplitude level.
 # The pure V and A curves above are unit-coupling response functions.
 mixed_integrated=[]
 c=muon_couplings(1.,1e-2)
 for mass in masses:
  energies=np.array([mass*f for f in efactors])
  _,km=rates.compton_mixed_kernels(mass,energies,c.g_vector,c.g_axial,order=96)
  sm=km.sum(axis=1)
  _,kv=rates.compton_kernels(mass,energies,order=96,current="vector")
  sv=kv.sum(axis=1)
  for j,e in enumerate(energies):
   mixed_integrated.append({
    "mass_MeV":mass,"mediator_energy_MeV":float(e),
    "mixed_over_vector_by_mode":{mode:(float(sm[j,i]/sv[j,i]) if sv[j,i]>0 else None) for i,mode in enumerate(rates.MODES)},
    "mixed_over_vector_polarization_sum":float(sm[j].sum()/sv[j].sum())})
 return {"differential":rows,"angular_integrated":integrated,
         "finite_mixing_integrated":mixed_integrated,
         "grid":{"masses_MeV":masses,"energy_over_mass":efactors,"cosines":cosines.tolist(),"theta_muR_mixed_benchmark":1e-2}}

def dimuon_scan():
 threshold=2*rates.M_MU; factors=[1.0001,1.001,1.01,1.05,1.2,1.5,2.,3.,5.]
 rows=[]; temp=30.; mu=80.
 for factor in factors:
  mass=threshold*factor; energy=1.25*mass
  pa,aa=rates.charged_muon_decay_rates(mass,energy,temp,mu,current="axial",order=96)
  pv,av=rates.charged_muon_decay_rates(mass,energy,temp,mu,current="vector",order=96)
  beta=np.sqrt(1-threshold**2/mass**2)
  c=muon_couplings(1.,1e-2)
  pm,am=rates.charged_muon_decay_rates_mixed(mass,energy,temp,mu,c.g_vector,c.g_axial,order=96)
  incoherent_prod=c.g_vector**2*pv+c.code_axial_minus_gamma5_coefficient**2*pa
  incoherent_abs=c.g_vector**2*av+c.code_axial_minus_gamma5_coefficient**2*aa
  rows.append({"mass_MeV":float(mass),"mass_over_dimuon_threshold":factor,"beta_mu":float(beta),
   "vacuum_width_ratio_A_over_V":float(beta**2/(1+2*rates.M_MU**2/mass**2)),
   "thermal_production_ratio_A_over_V_by_mode":{mode:(float(pa[i]/pv[i]) if pv[i]>0 else None) for i,mode in enumerate(rates.MODES)},
   "thermal_absorption_ratio_A_over_V_by_mode":{mode:(float(aa[i]/av[i]) if av[i]>0 else None) for i,mode in enumerate(rates.MODES)},
   "finite_mixing_production_over_vector_by_mode":{mode:(float(pm[i]/pv[i]) if pv[i]>0 else None) for i,mode in enumerate(rates.MODES)},
   "finite_mixing_absorption_over_vector_by_mode":{mode:(float(am[i]/av[i]) if av[i]>0 else None) for i,mode in enumerate(rates.MODES)},
   "interference_fraction_in_production_by_mode":{mode:(float((pm[i]-incoherent_prod[i])/pm[i]) if pm[i]!=0 else None) for i,mode in enumerate(rates.MODES)},
   "interference_fraction_in_absorption_by_mode":{mode:(float((am[i]-incoherent_abs[i])/am[i]) if am[i]!=0 else None) for i,mode in enumerate(rates.MODES)}})
 return {"threshold_MeV":threshold,"temperature_MeV":temp,"muon_chemical_potential_MeV":mu,"rows":rows}

def run():
 return {"title":"Mode-resolved vector/axial local response scan",
  "scope":"Local kernels only; no stellar transport, profile fit, rescaling, or exclusion curve.",
  "conventions":{"polarization_order":list(rates.MODES),"ratio":"unit-coupling axial response divided by unit-coupling vector response","mixed_benchmark":"theta_muR=1e-2, gX=1; neutrino couplings unchanged"},
  "rates_py_sha256":hashlib.sha256((ROOT/"rates.py").read_bytes()).hexdigest(),
  "compton":compton_scan(),"dimuon":dimuon_scan(),
  "interpretation":"A local response ratio is not by itself a luminosity or opacity rescaling."}

def main():
 p=argparse.ArgumentParser(); p.add_argument("--output",type=Path,default=HERE/"outputs"/"vector_axial_response_scan.json")
 args=p.parse_args(); result=run(); args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print(json.dumps({"output":str(args.output),"compton_points":len(result["compton"]["differential"]),"integrated_points":len(result["compton"]["angular_integrated"]),"dimuon_points":len(result["dimuon"]["rows"]),"rates_sha256":result["rates_py_sha256"]},indent=2))
if __name__=="__main__":main()
