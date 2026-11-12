
import sys, os, csv, json, time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
from numba import njit
ROOT=Path("/mnt/data/c4c3_work/research/stellar-cooling-constraints-20261105/blinov_reproduction")
OUT=ROOT/"outputs"
LOCAL=Path("/mnt/data/c4c3-local-independent")
LOCAL.mkdir(exist_ok=True)
sys.path.insert(0,str(ROOT))
import audit_b16_p1iii_eos_c4c2_full_angle_total_scattering as c4
import audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel as b2
PROFILE=OUT/"caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2=OUT/"p1iii_eos_full_radial_occupation_2026-11-11.csv"
GAMMA=np.asarray(b2.kernel.GAMMA); METRIC=np.asarray(b2.kernel.METRIC); IDENT=np.asarray(b2.kernel.IDENT)
@njit
def mm4(a,b):
 out=np.zeros((4,4),np.complex128)
 for i in range(4):
  for j in range(4):
   z=0j
   for k in range(4): z+=a[i,k]*b[k,j]
   out[i,j]=z
 return out
@njit
def cn(mstar,q0,qmag,qhat,e1,e2,qvec,vertex,barred,L,p,phi,GAMMA,METRIC,IDENT):
 ei=np.sqrt(p*p+mstar*mstar)
 cosine=(2*ei*q0+q0*q0-qmag*qmag)/(2*p*qmag) if p>1e-14 else 0.0
 if abs(cosine)>1.0+2e-10: return 0.0
 cosine=max(-1.0,min(1.0,cosine)); sine=np.sqrt(max(0.0,1.0-cosine*cosine))
 cp=np.cos(phi); sp=np.sin(phi); pv=np.zeros(3); pp=np.zeros(3)
 for i in range(3):
  pv[i]=p*(cosine*qhat[i]+sine*(cp*e1[i]+sp*e2[i])); pp[i]=pv[i]+qvec[i]
 ef=ei+q0; pp2=pp[0]**2+pp[1]**2+pp[2]**2
 if abs(np.sqrt(pp2+mstar*mstar)-ef)>2e-9*max(1.0,ef): raise ArithmeticError("shell")
 pi=np.array([ei,pv[0],pv[1],pv[2]]); pf=np.array([ef,pp[0],pp[1],pp[2]])
 Si=np.zeros((4,4),np.complex128); Sf=np.zeros((4,4),np.complex128)
 for mu in range(4):
  for a in range(4):
   for b in range(4):
    Si[a,b]+=METRIC[mu]*pi[mu]*GAMMA[mu,a,b]; Sf[a,b]+=METRIC[mu]*pf[mu]*GAMMA[mu,a,b]
 for a in range(4):
  for b in range(4):
   Si[a,b]+=mstar*IDENT[a,b]; Sf[a,b]+=mstar*IDENT[a,b]
 A=np.zeros((4,4),np.complex128); left=np.zeros((4,4,4),np.complex128)
 for mu in range(4): left[mu]=mm4(vertex[mu],Si)
 for mu in range(4):
  for al in range(4):
   tmp=mm4(left[mu],barred[al])
   for a in range(4):
    for b in range(4): A[a,b]+=L[mu,al]*tmp[a,b]
 tr=0j
 for a in range(4):
  for b in range(4): tr+=Sf[a,b]*A[b,a]
 return 0.5*tr.real
def fast_contract(pre,p,phi):
 return cn(pre["mstar"],pre["q0"],pre["qmag"],pre["qhat"],pre["e1"],pre["e2"],pre["qvec"],np.asarray(pre["vertex"]),np.asarray(pre["barred"]),np.asarray(pre["L"]),p,phi,GAMMA,METRIC,IDENT)
PROFILE_DATA=None; C2_DATA=None
def init_worker():
 global PROFILE_DATA,C2_DATA
 PROFILE_DATA=c4.load_profile(PROFILE); C2_DATA=c4.load_c2_reference(C2)
 b2.contract_moving_eos=fast_contract
def one_radius(i):
 s,occ=PROFILE_DATA[i],C2_DATA[i]
 if abs(s["r_km"]-occ["r_km"])>1e-12: raise ValueError(f"radial mismatch {i}")
 xi,nB=s["xi_SPP"],s["nB_fm3"]; out=[]
 for sp in ("n","p"):
  X=s[f"X_{sp}"]; nprime=occ[f"nprime_{sp}_fm3"]; nu=occ[f"nu_{sp}_EOS_MeV"]; ms=s[f"mstar_{sp}_MeV"]
  for anti in (False,True):
   gamma,root=c4.integrate_total_rate(100.0,sp,anti,s["T_MeV"],nu,ms,n_cos=8,order_ep=48,order_p=36,order_phi=12,support_scan_points=10001)
   if not (gamma>0 and np.isfinite(gamma) and root<1e-7): raise ArithmeticError(f"bad rate i={i} {sp} {anti}")
   nfree=xi*nprime; neos=X*nB
   out.append({"profile_index":i,"r_km":s["r_km"],"species":sp,"antinu":str(anti),"E_MeV":100.0,"T_MeV":s["T_MeV"],"mstar_MeV":ms,"nu_MeV":nu,"X_free":X,"xi_SPP":xi,"nB_fm3":nB,"nprime_available_fm3":nprime,"n_free_total_volume_fm3":nfree,"n_free_EOS_target_fm3":neos,"density_closure_relative_residual":nfree/neos-1.0,"gamma_available_volume_MeV":gamma,"sigma_per_target_MeV_minus2":gamma/(nprime*b2.HBARC**3),"kappa_sc_MeV":xi*gamma,"n_cos":8,"n_Eprime":48,"n_p":36,"n_phi":12,"support_root_max_relative_residual":root})
 return out
def main():
 ck=LOCAL/"rates_checkpoint.jsonl"; done={}
 if ck.exists():
  raw=ck.read_text().replace("\\n","\n")
  for line in raw.splitlines():
   if line.strip():
    x=json.loads(line); done[int(x[0]["profile_index"])]=x
 pending=[i for i in range(301) if i not in done]
 print("resume",len(done),"pending",len(pending),flush=True); t0=time.time()
 with ProcessPoolExecutor(max_workers=5,initializer=init_worker) as pool:
  fs={pool.submit(one_radius,i):i for i in pending}
  for f in as_completed(fs):
   i=fs[f]; rows=f.result(); done[i]=rows
   with ck.open("a") as st: st.write(json.dumps(rows,separators=(",",":"))+"\n")
   print("DONE",i,rows[0]["r_km"],"elapsed",round(time.time()-t0,1),"completed",len(done),"/301",flush=True)
 rows=[r for i in sorted(done) for r in done[i]]
 with (LOCAL/"local_independent_radial_rates_301x4.csv").open("w",newline="") as st:
  w=csv.DictWriter(st,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
 print("FINISHED",len(rows),"rows",round(time.time()-t0,1),"s",flush=True)
if __name__=="__main__": main()
