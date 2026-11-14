#!/usr/bin/env python3
"""Targeted high-order checks for global E1 worst energy/radial cells."""
from __future__ import annotations
import argparse,hashlib,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.interpolate import PchipInterpolator
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
for p in (ROOT,HERE):
 if str(p) not in sys.path:sys.path.insert(0,str(p))
import audit_b13_local_kernel_radial_energy_10mev as audit
PROFILE=ROOT/"data"/"sfho188_digitized.csv";EXPECTED="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
ORDERS=((16,10,10,10),(20,12,12,12),(24,14,14,14),(28,16,16,16),(32,18,18,18))
BASE_X=np.asarray([.5,2.,6.,18.,36.])
def bisect(nodes):return np.asarray(sorted(set(nodes.tolist()+[(.5*(math.sqrt(a)+math.sqrt(b)))**2 for a,b in zip(nodes[:-1],nodes[1:])])),float)
def rel(a,b):return abs(float(a)-float(b))/max(abs(float(a)),abs(float(b)),1e-300)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True)
 ap.add_argument('--radii',type=float,nargs='*',default=[14.7423493862152,8.4821412022467,22.1918941570485])
 ap.add_argument('--worst-x',type=float,default=.78125)
 ap.add_argument('--radial-interval-indices',type=int,nargs='*',default=[1024,1479,1487])
 args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
 sha=hashlib.sha256(PROFILE.read_bytes()).hexdigest()
 if sha!=EXPECTED:raise RuntimeError('profile SHA mismatch')
 coarse=bisect(BASE_X); energy_x=np.asarray(sorted(set(coarse.tolist()+[args.worst_x])),float)
 anchor_results=[]
 for radius in args.radii:
  bg=audit.load_profile(PROFILE,np.asarray([radius],float));temp=float(bg['T'][0]);prev=None;ladder=[];final=None;final_change=None
  for order in ORDERS:
   current={};maxchg=0.;worstchg=None;cache={}
   for x in energy_x:
    val=audit.evaluate_point(PROFILE,radius,10.+float(x)*temp,order,cache);current[float(x)]=val
    if prev is not None:
     change=audit.compare_points(prev[float(x)],val)['maximum_relative_change']
     if change>maxchg:maxchg=change;worstchg={'x':float(x),'relative_change':change}
   ladder.append({'orders':list(order),'maximum_change_vs_previous':None if prev is None else maxchg,'worst_point':worstchg})
   final=current;final_change=None if prev is None else maxchg
   if prev is not None and maxchg<1e-3:break
   prev=current
  q=final;errors=[]
  for charge in audit.CHARGES:
   knots=np.asarray([q[float(x)]['charge_resolved'][charge]['absorption'] for x in coarse],float)
   ip=[PchipInterpolator(np.sqrt(coarse),np.log(np.maximum(knots[:,j],1e-300))) for j in range(3)]
   direct=np.asarray(q[float(args.worst_x)]['charge_resolved'][charge]['absorption'],float)
   for j,mode in enumerate(audit.MODES):
    pred=float(np.exp(ip[j](math.sqrt(args.worst_x))))
    errors.append({'charge':charge,'mode':mode,'direct':float(direct[j]),'interpolated':pred,'relative_error':rel(direct[j],pred)})
  worst=max(errors,key=lambda z:z['relative_error'])
  payload={'run':'P1B-E1-TARGETED-HIGH-ORDER','profile_sha256':sha,'radius_km':radius,'temperature_MeV':temp,'energy_x':energy_x.tolist(),
   'orders_ladder':ladder,'final_orders':list(ladder[-1]['orders']),'final_successive_order_change':final_change,
   'quadrature_pass':bool(final_change is not None and final_change<1e-3),'PCHIP_worst_midpoint_x':args.worst_x,
   'maximum_PCHIP_interpolation_error_at_worst_x':worst['relative_error'],'worst_channel':worst,'all_channels':errors,
   'maximum_detailed_balance_residual':max(v['maximum_mode_detailed_balance_relative_residual'] for v in q.values()),
   'maximum_final_muon_mass_shell_residual':max(v['final_muon_shell_relative_error'] for v in q.values()),
   'all_rates_finite_nonnegative':all(v['all_rates_finite_and_nonnegative'] for v in q.values()),
   'scope':'Selected radial anchors and worst energy midpoint only; not a full high-order radial/energy scan.'}
  path=args.output_dir/f"energy_anchor_{radius:.8f}.json";path.write_text(json.dumps(payload,indent=2)+'\n');anchor_results.append(payload)
  print(f"energy anchor r={radius:.6f} km: final order={payload['final_orders']}, dQ={final_change:.3e}, dE={worst['relative_error']:.3e}",flush=True)
 table=np.genfromtxt(PROFILE,delimiter=',',names=True);radii=np.asarray(table['r_km'],float);radial_results=[]
 for idx in args.radial_interval_indices:
  r0=float(radii[idx]);r1=float(radii[idx+1]);rm=.5*(r0+r1);rs=(r0,rm,r1)
  bgm=audit.load_profile(PROFILE,np.asarray([rm],float));tm=float(bgm['T'][0]);x=.5;omega=10.+x*tm
  values={};node_ladders=[]
  for rr in rs:
   bg=audit.load_profile(PROFILE,np.asarray([rr],float));tt=float(bg['T'][0]);w=10.+x*tt;prev=None;last=None;lad=[];cache={}
   for order in ORDERS:
    v=audit.evaluate_point(PROFILE,rr,w,order,cache);change=None if prev is None else audit.compare_points(prev,v)['maximum_relative_change']
    lad.append({'orders':list(order),'maximum_change_vs_previous':change});last=v
    if change is not None and change<1e-3:break
    prev=v
   values[rr]=last;node_ladders.append({'radius_km':rr,'temperature_MeV':tt,'orders_ladder':lad,'final_orders':lad[-1]['orders'],'final_change':lad[-1]['maximum_change_vs_previous']})
  direct=values[rm];left=values[r0];right=values[r1]
  prediction=audit.interpolate_cell(left,left,right,right,omega,tm)
  comparison=audit.compare_midpoint_to_interpolation(direct,prediction)
  radial_payload={'left_radial_index':idx,'r_left_km':r0,'r_mid_km':rm,'r_right_km':r1,'x':x,'omega_mid_MeV':omega,
    'node_quadrature':node_ladders,'maximum_radial_midpoint_interpolation_error':comparison['maximum_relative_error'],
    'per_charge_field_mode_relative_error':comparison['per_charge_field_mode_relative_error'],
    'all_nodes_quadrature_pass':all(n['final_change'] is not None and n['final_change']<1e-3 for n in node_ladders),
    'maximum_detailed_balance_residual':max(v['maximum_mode_detailed_balance_relative_residual'] for v in values.values()),
    'maximum_final_muon_shell_residual':max(v['final_muon_shell_relative_error'] for v in values.values())}
  radial_results.append(radial_payload)
  (args.output_dir/f"radial_interval_{idx:04d}.json").write_text(json.dumps(radial_payload,indent=2)+'\n')
  print(f"radial interval {idx}: high-order midpoint error={comparison['maximum_relative_error']:.3e}",flush=True)
 summary={'run':'P1B-E1-TARGETED-HIGH-ORDER-SUMMARY','profile_sha256':sha,'energy_anchor_checks':anchor_results,'radial_midpoint_checks':radial_results,
  'all_energy_anchor_quadrature_pass':all(x['quadrature_pass'] for x in anchor_results),
  'all_energy_anchor_interpolation_pass_1pct':all(x['maximum_PCHIP_interpolation_error_at_worst_x']<1e-2 for x in anchor_results),
  'all_radial_midpoint_nodes_quadrature_pass':all(x['all_nodes_quadrature_pass'] for x in radial_results),
  'scope':'Targeted high-order verification only; not a global high-order quadrature acceptance.'}
 (args.output_dir/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps({k:v for k,v in summary.items() if k not in ('energy_anchor_checks','radial_midpoint_checks')},indent=2))
if __name__=='__main__':main()
