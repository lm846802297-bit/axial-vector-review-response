#!/usr/bin/env python3
"""Full-profile 2D radial-energy midpoint screen for the exact B.13 kernel.

Input is the immutable P1B-E1 1687-node / 17-energy direct-kernel archive.
For every one of the 1686 adjacent radial intervals this script directly
re-evaluates B.13 at the radial midpoint and all 17 local x coordinates.
It tests radial interpolation, energy PCHIP at radial midpoints, and 2D cell
midpoint interpolation (local bilinear-log and sequential PCHIP-in-sqrt(x)
then log-linear-in-radius). All production/reduced-absorption/spectral-source
channels are reconstructed from interpolated absorption by exact midpoint
detailed balance.

This is a low-order screening run, not global high-order quadrature acceptance.
"""
from __future__ import annotations
import argparse, hashlib, json, math, os, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
import numpy as np
from scipy.interpolate import PchipInterpolator

HERE=Path(__file__).resolve().parent
ROOT=next((p for p in (HERE,*HERE.parents) if (p/'data'/'sfho188_digitized.csv').exists()),Path('/mnt/data/p1b-final-bundle'))
THERMAL=ROOT/'finite_mixing'/'thermal_integrals'
PROFILE=ROOT/'data'/'sfho188_digitized.csv'
EXPECTED_PROFILE_SHA='9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c'
EXPECTED_E1_SOURCE_SHA='e48a388c7572880115ae6cb4bc8bae6fabefcc3a5982981243a585a527a6ce9e'
ORDERS=(10,6,6,6)
MASS=10.0
TOL=1e-2
# Initialized in each process.
TABLE=None
RADIUS=None
AUDIT=None


def _init_worker(profile_path):
    global TABLE,RADIUS,AUDIT
    if str(THERMAL) not in sys.path: sys.path.insert(0,str(THERMAL))
    if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as audit
    TABLE=np.genfromtxt(profile_path,delimiter=',',names=True)
    RADIUS=np.asarray(TABLE['r_km'],float)
    # Preserve the audited piecewise-linear profile interpolation, but avoid
    # reparsing the complete 1687-row CSV on every direct kernel evaluation.
    def fast_load_profile(path,radii):
        rr=np.asarray(radii,float)
        return {name:np.interp(rr,RADIUS,np.asarray(TABLE[col],float)) for name,col in {
            'T':'T_MeV','mu_mu':'mu_mu_MeV','mu_numu':'mu_numu_MeV','lapse':'lapse'}.items()}
    audit.load_profile=fast_load_profile
    AUDIT=audit


def _reconstruct(absorption,omega,temp):
    boltz=math.exp(-omega/temp)
    red=-math.expm1(-omega/temp)
    k=math.sqrt(max(omega*omega-MASS*MASS,0.0))
    pref=omega*omega*k/(2.0*math.pi**2)
    pred={}
    for charge,arr in absorption.items():
        aa=np.asarray(arr,float)
        prod=boltz*aa
        pred[charge]={
            'absorption':aa.tolist(),
            'production':prod.tolist(),
            'reduced_absorption':(red*aa).tolist(),
            'spectral_source':(pref*prod).tolist(),
        }
    return pred


def _pchip_absorption(endpoint_records, coarse_x, x_eval):
    out={}
    sx=np.sqrt(np.asarray(coarse_x,float)); s_eval=math.sqrt(float(x_eval))
    for charge in ('mu_minus','mu_plus'):
        vals=np.asarray([endpoint_records[float(x)]['charge_resolved'][charge]['absorption'] for x in coarse_x],float)
        modes=[]
        for mode in range(3):
            y=vals[:,mode]
            if np.all(y>0):
                ip=PchipInterpolator(sx,np.log(y),extrapolate=False)
                value=float(np.exp(ip(s_eval)))
            else:
                # Zero-safe fallback: PCHIP the positive values linearly.
                value=float(PchipInterpolator(sx,y,extrapolate=False)(s_eval))
            modes.append(max(value,0.0))
        out[charge]=modes
    return out


def _relative_error(direct,pred):
    return AUDIT.compare_midpoint_to_interpolation(direct,pred)


def _compact_direct(v):
    return {
        'radius_km':v['radius_km'],'omega_local_MeV':v['omega_local_MeV'],
        'temperature_MeV':v['temperature_MeV'],'mu_minus_chemical_potential_MeV':v['mu_minus_chemical_potential_MeV'],
        'lapse':v['lapse'],'orders':v['orders'],'charge_resolved':v['charge_resolved'],
        'maximum_mode_detailed_balance_relative_residual':v['maximum_mode_detailed_balance_relative_residual'],
        'final_muon_shell_relative_error':v['final_muon_shell_relative_error'],
        'charge_sum_closure_relative_residual':v['charge_sum_closure_relative_residual'],
        'all_rates_finite_and_nonnegative':v['all_rates_finite_and_nonnegative']
    }


def _load_endpoint_chunk(chunks_dir,index,expected_sha):
    path=Path(chunks_dir)/f'chunk_{index:04d}.json'
    d=json.loads(path.read_text())
    if d.get('profile_sha256')!=EXPECTED_PROFILE_SHA or d.get('source_sha256')!=expected_sha:
        raise RuntimeError(f'Provenance mismatch in {path}')
    return {float(r['x']):r for r in d['records']}


def _worker(task):
    idx,chunks_dir,outdir,coarse_x,validation_x,expected_sha=task
    out=Path(outdir)/f'interval_{idx:04d}_{idx+1:04d}.json'
    if out.exists():
        d=json.loads(out.read_text())
        if d.get('profile_sha256')==EXPECTED_PROFILE_SHA and d.get('source_sha256')==expected_sha and d.get('orders')==list(ORDERS):
            return {'index':idx,'status':'skipped_verified','max_cell_error':d['summary']['maximum_cell_pchip_error']}
        raise RuntimeError(f'Existing output provenance mismatch: {out}')
    left=_load_endpoint_chunk(chunks_dir,idx,expected_sha)
    right=_load_endpoint_chunk(chunks_dir,idx+1,expected_sha)
    r0=float(RADIUS[idx]);r1=float(RADIUS[idx+1]);rm=0.5*(r0+r1)
    temp=float(np.interp(rm,RADIUS,np.asarray(TABLE['T_MeV'],float)))
    cache={};direct={};records=[]
    max_db=0.;max_shell=0.;all_positive=True
    for x in validation_x:
        omega=MASS+float(x)*temp
        v=AUDIT.evaluate_point(PROFILE,rm,omega,ORDERS,cache)
        direct[float(x)]=v
        max_db=max(max_db,v['maximum_mode_detailed_balance_relative_residual'])
        max_shell=max(max_shell,v['final_muon_shell_relative_error'])
        all_positive=all_positive and v['all_rates_finite_and_nonnegative']
        records.append({'x':float(x),**_compact_direct(v)})

    radial_checks=[]
    for x in validation_x:
        omega=MASS+float(x)*temp
        pred=AUDIT.interpolate_cell(left[float(x)],left[float(x)],right[float(x)],right[float(x)],omega,temp)
        cmp=_relative_error(direct[float(x)],pred)
        radial_checks.append({'x':float(x),'maximum_relative_error':cmp['maximum_relative_error'],
                              'per_charge_field_mode_relative_error':cmp['per_charge_field_mode_relative_error']})

    energy_checks=[]
    for x in validation_x:
        if any(abs(float(x)-float(c))<1e-12 for c in coarse_x): continue
        omega=MASS+float(x)*temp
        abs_mid=_pchip_absorption(direct,coarse_x,x)
        pred=_reconstruct(abs_mid,omega,temp)
        cmp=_relative_error(direct[float(x)],pred)
        energy_checks.append({'x_mid':float(x),'maximum_relative_error':cmp['maximum_relative_error'],
                              'per_charge_field_mode_relative_error':cmp['per_charge_field_mode_relative_error']})

    cell_checks=[]
    for j in range(len(coarse_x)-1):
        x0=float(coarse_x[j]);x1=float(coarse_x[j+1])
        xm=0.25*(math.sqrt(x0)+math.sqrt(x1))**2 # midpoint in sqrt(x)
        omega=MASS+xm*temp
        direct_point=direct[float(min(validation_x,key=lambda z:abs(float(z)-xm)))]
        if abs(float(min(validation_x,key=lambda z:abs(float(z)-xm)))-xm)>1e-10:
            raise RuntimeError(f'No direct midpoint node for x={xm}')
        # Local bilinear log interpolation (protocol baseline).
        bilinear=AUDIT.interpolate_cell(left[x0],left[x1],right[x0],right[x1],omega,temp)
        cb=_relative_error(direct_point,bilinear)
        # PCHIP in sqrt(x) at each radial endpoint, then log-linear in radius.
        a0=_pchip_absorption(left,coarse_x,xm);a1=_pchip_absorption(right,coarse_x,xm)
        ar={q:[AUDIT._interpolate_pair(a0[q][k],a1[q][k],0.5) for k in range(3)] for q in ('mu_minus','mu_plus')}
        pchip=_reconstruct(ar,omega,temp)
        cp=_relative_error(direct_point,pchip)
        cell_checks.append({'x_mid':xm,'omega_mid_MeV':omega,
          'bilinear_log_maximum_relative_error':cb['maximum_relative_error'],
          'pchip_then_radial_log_maximum_relative_error':cp['maximum_relative_error'],
          'bilinear_per_charge_field_mode_relative_error':cb['per_charge_field_mode_relative_error'],
          'pchip_per_charge_field_mode_relative_error':cp['per_charge_field_mode_relative_error']})

    worst_rad=max(radial_checks,key=lambda z:z['maximum_relative_error'])
    worst_energy=max(energy_checks,key=lambda z:z['maximum_relative_error'])
    worst_cell=max(cell_checks,key=lambda z:z['pchip_then_radial_log_maximum_relative_error'])
    summary={'maximum_radial_midpoint_error':worst_rad['maximum_relative_error'],'worst_radial_x':worst_rad['x'],
      'maximum_energy_pchip_error_at_radial_midpoints':worst_energy['maximum_relative_error'],'worst_energy_x':worst_energy['x_mid'],
      'maximum_cell_bilinear_error':max(x['bilinear_log_maximum_relative_error'] for x in cell_checks),
      'maximum_cell_pchip_error':worst_cell['pchip_then_radial_log_maximum_relative_error'],'worst_cell_x':worst_cell['x_mid'],
      'maximum_detailed_balance_residual':max_db,'maximum_final_muon_shell_residual':max_shell,
      'all_rates_finite_nonnegative':all_positive}
    payload={'run':'P1B-E1-GLOBAL-03-FULL-2D-MIDPOINT-SCREEN','interval_index':idx,'left_radial_index':idx,'right_radial_index':idx+1,
      'r_left_km':r0,'r_mid_km':rm,'r_right_km':r1,'dr_km':r1-r0,'temperature_mid_MeV':temp,
      'profile_sha256':EXPECTED_PROFILE_SHA,'source_sha256':expected_sha,'orders':list(ORDERS),
      'coarse_x':list(map(float,coarse_x)),'validation_x':list(map(float,validation_x)),
      'direct_midpoint_records':records,'radial_midpoint_checks':radial_checks,'energy_pchip_checks':energy_checks,
      'cell_midpoint_checks':cell_checks,'summary':summary,
      'acceptance':{'screening_tolerance':TOL,'radial_midpoint_pass_1pct':summary['maximum_radial_midpoint_error']<TOL,
        'energy_pchip_pass_1pct':summary['maximum_energy_pchip_error_at_radial_midpoints']<TOL,
        'cell_pchip_pass_1pct':summary['maximum_cell_pchip_error']<TOL,
        'quadrature_high_order_verified':False}}
    tmp=out.with_suffix('.tmp');tmp.write_text(json.dumps(payload,separators=(',',':'))+'\n');tmp.replace(out)
    return {'index':idx,'status':'completed','max_radial_error':summary['maximum_radial_midpoint_error'],
      'max_energy_error':summary['maximum_energy_pchip_error_at_radial_midpoints'],
      'max_cell_error':summary['maximum_cell_pchip_error']}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--chunks-dir',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True)
    ap.add_argument('--workers',type=int,default=4);ap.add_argument('--start',type=int,default=0);ap.add_argument('--end',type=int,default=1686)
    ap.add_argument('--indices',type=int,nargs='*',default=None)
    args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    profile_sha=hashlib.sha256(PROFILE.read_bytes()).hexdigest()
    if profile_sha!=EXPECTED_PROFILE_SHA:raise RuntimeError(f'Profile SHA mismatch: {profile_sha}')
    files=sorted(args.chunks_dir.glob('chunk_*.json'))
    if len(files)!=1687:raise RuntimeError(f'Expected 1687 E1 direct-data chunks, got {len(files)}')
    first=json.loads(files[0].read_text());expected_sha=first['source_sha256']
    for idx in (0,703,1487,1686):
        d=json.loads((args.chunks_dir/f'chunk_{idx:04d}.json').read_text())
        if d['profile_sha256']!=profile_sha or d['source_sha256']!=expected_sha or len(d['records'])!=17:
            raise RuntimeError(f'Anchor chunk {idx} failed provenance/coverage check')
    coarse_x=np.asarray(first['coarse_x'],float);validation_x=np.asarray(first['validation_grid_x'],float)
    if len(coarse_x)!=9 or len(validation_x)!=17:raise RuntimeError('Unexpected E1 grid shape')
    indices=args.indices if args.indices is not None else list(range(args.start,args.end))
    tasks=[(int(i),str(args.chunks_dir),str(args.output_dir),coarse_x.tolist(),validation_x.tolist(),expected_sha) for i in indices]
    t0=time.time();results=[]
    with ProcessPoolExecutor(max_workers=args.workers,initializer=_init_worker,initargs=(str(PROFILE),)) as pool:
        futures=[pool.submit(_worker,t) for t in tasks]
        for n,f in enumerate(as_completed(futures),1):
            z=f.result();results.append(z)
            if n%25==0 or n==len(tasks):
                print(f'completed {n}/{len(tasks)} radial intervals; last={z}; elapsed={time.time()-t0:.1f}s',flush=True)
    # Aggregate every verified interval, including prior verified checkpoints.
    rows=[]
    for f in sorted(args.output_dir.glob('interval_*.json')):
        d=json.loads(f.read_text())
        if d.get('profile_sha256')==profile_sha and d.get('source_sha256')==expected_sha and d.get('orders')==list(ORDERS):rows.append(d)
    rows.sort(key=lambda x:x['interval_index'])
    indices_seen=[x['interval_index'] for x in rows]
    if len(indices_seen)!=len(set(indices_seen)):raise RuntimeError('Duplicate radial interval checkpoints')
    def flatten(key):return [x for row in rows for x in row[key]]
    radial=flatten('radial_midpoint_checks');energy=flatten('energy_pchip_checks');cells=flatten('cell_midpoint_checks')
    radial_err=np.asarray([x['maximum_relative_error'] for x in radial],float)
    energy_err=np.asarray([x['maximum_relative_error'] for x in energy],float)
    bilinear_err=np.asarray([x['bilinear_log_maximum_relative_error'] for x in cells],float)
    cell_err=np.asarray([x['pchip_then_radial_log_maximum_relative_error'] for x in cells],float)
    summaries=[x['summary'] for x in rows]
    def worst(collection,key):return max(collection,key=lambda x:x[key]) if collection else None
    summary={'run':'P1B-E1-GLOBAL-03-FULL-2D-MIDPOINT-SCREEN','profile_sha256':profile_sha,'e1_source_sha256':expected_sha,
      'radial_intervals_completed':len(rows),'radial_intervals_expected':1686,'complete_radial_coverage':indices_seen==list(range(1686)),
      'direct_b13_midpoint_evaluations':len(rows)*17,'orders':list(ORDERS),'coarse_energy_knots':coarse_x.tolist(),'validation_energy_nodes':validation_x.tolist(),
      'radial_midpoint_screen':{'samples':len(radial),'maximum_error':float(radial_err.max()),'p95_error':float(np.quantile(radial_err,.95)),
        'median_error':float(np.median(radial_err)),'samples_over_1pct':int(np.sum(radial_err>=TOL)),'worst':worst(radial,'maximum_relative_error')},
      'energy_pchip_at_radial_midpoints':{'samples':len(energy),'maximum_error':float(energy_err.max()),'p95_error':float(np.quantile(energy_err,.95)),
        'median_error':float(np.median(energy_err)),'samples_over_1pct':int(np.sum(energy_err>=TOL)),'worst':worst(energy,'maximum_relative_error')},
      '2d_cell_midpoint_screen':{'samples':len(cells),'bilinear_log_maximum_error':float(bilinear_err.max()),
        'pchip_then_radial_log_maximum_error':float(cell_err.max()),'pchip_p95_error':float(np.quantile(cell_err,.95)),
        'pchip_median_error':float(np.median(cell_err)),'cells_over_1pct_bilinear':int(np.sum(bilinear_err>=TOL)),
        'cells_over_1pct_pchip':int(np.sum(cell_err>=TOL)),'worst_pchip':worst(cells,'pchip_then_radial_log_maximum_relative_error')},
      'micro_consistency':{'maximum_detailed_balance_residual':max(x['maximum_detailed_balance_residual'] for x in summaries),
        'maximum_final_muon_mass_shell_residual':max(x['maximum_final_muon_shell_residual'] for x in summaries),
        'all_rates_finite_nonnegative':all(x['all_rates_finite_nonnegative'] for x in summaries)},
      'screening_acceptance':{'tolerance':TOL,'radial_pass':bool(radial_err.max()<TOL),'energy_pchip_pass':bool(energy_err.max()<TOL),
        'cell_pchip_pass':bool(cell_err.max()<TOL),'overall_interpolation_screen_pass':bool(radial_err.max()<TOL and energy_err.max()<TOL and cell_err.max()<TOL)},
      'quadrature_acceptance':'not claimed; all new direct midpoints use screening order (10,6,6,6)',
      'full_star_emissivity_computed':False,'GR_optical_depth_computed':False,'luminosity_computed':False,
      'runtime_seconds_this_invocation':time.time()-t0,
      'scope':'Complete low-order full-profile radial midpoint and 2D cell-midpoint interpolation screen on the E1 nine-knot energy grid; selected high-order follow-up required.'}
    (args.output_dir/'GLOBAL_2D_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    # Top 50 cells/intervals retained for targeted high-order checks.
    ranked=sorted(cells,key=lambda x:x['pchip_then_radial_log_maximum_relative_error'],reverse=True)[:50]
    (args.output_dir/'TOP50_2D_CELLS.json').write_text(json.dumps(ranked,indent=2)+'\n')
    print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':main()
