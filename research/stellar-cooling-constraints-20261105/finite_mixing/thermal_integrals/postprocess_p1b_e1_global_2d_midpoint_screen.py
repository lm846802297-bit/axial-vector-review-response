#!/usr/bin/env python3
"""Aggregate and provenance-check the full P1-B E1 2D midpoint screen."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np
PROFILE_SHA='9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c'
TOL=1e-2

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-dir',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True)
 args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
 files=sorted(args.input_dir.glob('interval_*.json'));rows=[];source_sha=None
 for f in files:
  d=json.loads(f.read_text())
  if d.get('profile_sha256')!=PROFILE_SHA:raise RuntimeError(f'profile hash mismatch: {f}')
  if source_sha is None:source_sha=d['source_sha256']
  if d.get('source_sha256')!=source_sha:raise RuntimeError(f'source hash mismatch: {f}')
  if len(d.get('direct_midpoint_records',[]))!=17:raise RuntimeError(f'incomplete energy coverage: {f}')
  rows.append(d)
 rows.sort(key=lambda d:d['interval_index'])
 indices=[d['interval_index'] for d in rows]
 if len(indices)!=len(set(indices)):raise RuntimeError('duplicate interval outputs')
 if indices!=list(range(1686)):raise RuntimeError(f'incomplete radial coverage: {len(indices)} intervals')
 radial=[];energy=[];cells=[];max_db=0.;max_shell=0.;finite=True
 field_values={kind:{field:[] for field in ('production','absorption','reduced_absorption','spectral_source')} for kind in ('radial','energy','cell_bilinear','cell_pchip')}
 for d in rows:
  ix=d['interval_index']
  for x in d['radial_midpoint_checks']:
   radial.append({'interval_index':ix,'r_mid_km':d['r_mid_km'],'x':x['x'],'maximum_relative_error':x['maximum_relative_error']})
   for q,fields in x['per_charge_field_mode_relative_error'].items():
    for field,vals in fields.items():field_values['radial'][field].extend(vals)
  for x in d['energy_pchip_checks']:
   energy.append({'interval_index':ix,'r_mid_km':d['r_mid_km'],'x_mid':x['x_mid'],'maximum_relative_error':x['maximum_relative_error']})
   for q,fields in x['per_charge_field_mode_relative_error'].items():
    for field,vals in fields.items():field_values['energy'][field].extend(vals)
  for x in d['cell_midpoint_checks']:
   cells.append({'interval_index':ix,'r_left_km':d['r_left_km'],'r_mid_km':d['r_mid_km'],'r_right_km':d['r_right_km'],
     'x_mid':x['x_mid'],'omega_mid_MeV':x['omega_mid_MeV'],
     'bilinear_log_error':x['bilinear_log_maximum_relative_error'],
     'pchip_then_radial_log_error':x['pchip_then_radial_log_maximum_relative_error']})
   for q,fields in x['bilinear_per_charge_field_mode_relative_error'].items():
    for field,vals in fields.items():field_values['cell_bilinear'][field].extend(vals)
   for q,fields in x['pchip_per_charge_field_mode_relative_error'].items():
    for field,vals in fields.items():field_values['cell_pchip'][field].extend(vals)
  s=d['summary'];max_db=max(max_db,s['maximum_detailed_balance_residual']);max_shell=max(max_shell,s['maximum_final_muon_shell_residual'])
  finite=finite and s['all_rates_finite_nonnegative']
 def arr(items,key):return np.asarray([x[key] for x in items],float)
 re=arr(radial,'maximum_relative_error');ee=arr(energy,'maximum_relative_error');be=arr(cells,'bilinear_log_error');pe=arr(cells,'pchip_then_radial_log_error')
 def stats(v):return {'samples':int(len(v)),'maximum_error':float(v.max()),'p95_error':float(np.quantile(v,.95)),
   'median_error':float(np.median(v)),'samples_over_1pct':int(np.sum(v>=TOL))}
 per_field={kind:{field:stats(np.asarray(values,float)) for field,values in fields.items()} for kind,fields in field_values.items()}
 radial_worst=sorted(radial,key=lambda x:x['maximum_relative_error'],reverse=True)[:20]
 energy_worst=sorted(energy,key=lambda x:x['maximum_relative_error'],reverse=True)[:20]
 cell_worst=sorted(cells,key=lambda x:x['pchip_then_radial_log_error'],reverse=True)[:50]
 bilinear_worst=sorted(cells,key=lambda x:x['bilinear_log_error'],reverse=True)[:20]
 summary={'run':'P1B-E1-GLOBAL-03-FULL-2D-MIDPOINT-SCREEN','profile_sha256':PROFILE_SHA,'e1_source_sha256':source_sha,
  'radial_intervals_completed':len(rows),'radial_intervals_expected':1686,'complete_radial_coverage':True,
  'direct_b13_midpoint_evaluations':len(rows)*17,'screening_orders':[10,6,6,6],
  'radial_midpoint_interpolation':stats(re),'energy_pchip_at_radial_midpoints':stats(ee),
  '2d_cell_midpoint_interpolation':{'local_bilinear_log':stats(be),'sequential_pchip_sqrtx_then_radial_log':stats(pe)},
  'per_field_error_breakdown':per_field,
  'micro_consistency':{'maximum_detailed_balance_residual':max_db,'maximum_final_muon_mass_shell_residual':max_shell,'all_rates_finite_nonnegative':finite},
  'screening_acceptance':{'criterion':'maximum direct-midpoint discrepancy < 1% for radial, energy-PCHIP, and sequential 2D PCHIP interpolation',
   'radial_pass':bool(re.max()<TOL),'energy_pchip_pass':bool(ee.max()<TOL),'2d_pchip_pass':bool(pe.max()<TOL),
   'overall_interpolation_screen_pass':bool(re.max()<TOL and ee.max()<TOL and pe.max()<TOL)},
  'worst_locations':{'radial_midpoint':radial_worst[0],'energy_pchip_midpoint':energy_worst[0],
   '2d_pchip_cell':cell_worst[0],'bilinear_log_cell':bilinear_worst[0]},
  'top20_radial_midpoints':radial_worst,'top20_energy_pchip_midpoints':energy_worst,
  'top50_2d_pchip_cells':cell_worst,'top20_bilinear_cells':bilinear_worst,
  'quadrature_acceptance':'not claimed; new direct midpoint points use screening quadrature (10,6,6,6)',
  'full_star_emissivity_computed':False,'GR_optical_depth_computed':False,'luminosity_computed':False,
  'scope':'Full 1686-interval, 17-energy-node radial-midpoint and 2D cell-midpoint screen on the E1 nine-knot grid; selected high-order verification is a separate stage.'}
 (args.output_dir/'GLOBAL_2D_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
 for name,data in [('TOP20_RADIAL_MIDPOINTS.json',radial_worst),('TOP20_ENERGY_MIDPOINTS.json',energy_worst),
                   ('TOP50_2D_CELLS.json',cell_worst),('TOP20_BILINEAR_CELLS.json',bilinear_worst)]:
  (args.output_dir/name).write_text(json.dumps(data,indent=2)+'\n')
 with (args.output_dir/'RADIAL_INTERVAL_SCREEN.csv').open('w') as f:
  f.write('interval_index,r_left_km,r_mid_km,r_right_km,max_radial_error,max_energy_pchip_error,max_2d_pchip_error,max_2d_bilinear_error\n')
  for d in rows:
   f.write(f"{d['interval_index']},{d['r_left_km']:.12g},{d['r_mid_km']:.12g},{d['r_right_km']:.12g},{d['summary']['maximum_radial_midpoint_error']:.12g},{d['summary']['maximum_energy_pchip_error_at_radial_midpoints']:.12g},{d['summary']['maximum_cell_pchip_error']:.12g},{d['summary']['maximum_cell_bilinear_error']:.12g}\n")
 report=f'''# P1-B E1 Global-03: full-profile 2D radial-energy midpoint screen

**Profile:** reconstructed SFHo-18.8, t_pb = 1 s; 1687 radial vertices; SHA-256 `{PROFILE_SHA}`.  
**Kernel:** exact-recoil moving-muon semi-Compton B.13; m_A' = 10 MeV; pure-vector endpoint gV/gX = 1, gA/gX = 0.  
**Screening quadrature:** `(10,6,6,6)`; both muon charges and all three A' polarizations.

## Coverage

- All 1686 adjacent radial intervals were directly evaluated at the radial midpoint.
- All 17 E1 validation-energy coordinates were sampled at every radial midpoint: **{len(rows)*17:,} direct B.13 midpoint evaluations**.
- The nine E1 energy knots and eight sqrt(x)-midpoints were retained separately.
- The original E1 radial-node direct-data archive was read-only and its source/profile hashes were checked.

## Interpolation results

| Check | Samples | Maximum error | 95th percentile | Samples above 1% |
|---|---:|---:|---:|---:|
| Radial midpoint, all 17 x nodes | {len(re):,} | {re.max():.4%} | {np.quantile(re,.95):.4%} | {int(np.sum(re>=TOL)):,} |
| Energy PCHIP at radial midpoints | {len(ee):,} | {ee.max():.4%} | {np.quantile(ee,.95):.4%} | {int(np.sum(ee>=TOL)):,} |
| 2D local bilinear-log cell centers | {len(be):,} | {be.max():.4%} | {np.quantile(be,.95):.4%} | {int(np.sum(be>=TOL)):,} |
| 2D sequential PCHIP-in-sqrt(x), then log-radial cell centers | {len(pe):,} | {pe.max():.4%} | {np.quantile(pe,.95):.4%} | {int(np.sum(pe>=TOL)):,} |

The local bilinear-log result is retained as a diagnostic. The preferred interpolant uses the nine-knot PCHIP in sqrt(x) at each radial endpoint, followed by log-linear radial interpolation. All non-absorption channels are reconstructed from exact midpoint detailed balance and the exact spectral phase-space factor. Per-field maxima for production, absorption, reduced absorption and spectral source are recorded in `GLOBAL_2D_SUMMARY.json`.

## Algebraic checks

- Maximum mode-resolved detailed-balance residual: `{max_db:.3e}`.
- Maximum final-muon mass-shell residual: `{max_shell:.3e}`.
- All directly evaluated rates finite and nonnegative: `{finite}`.

## Disposition

- Radial interpolation screen: **{'PASS' if re.max()<TOL else 'FAIL'}**.
- Energy PCHIP at radial midpoints: **{'PASS' if ee.max()<TOL else 'FAIL'}**.
- Sequential 2D PCHIP screen: **{'PASS' if pe.max()<TOL else 'FAIL'}**.
- High-order quadrature: **not claimed**; this complete screen uses `(10,6,6,6)` only. The top-error cells must be re-evaluated with the high-order ladder before the local P1-B gate can be considered complete.

No full-star volume emissivity, GR optical depth, luminosity, Fig. 7 reproduction, or SN1987A limit is claimed by this run.
'''
 (args.output_dir/'REPORT.md').write_text(report)
 print(json.dumps({k:v for k,v in summary.items() if k not in ('top20_radial_midpoints','top20_energy_pchip_midpoints','top50_2d_pchip_cells','top20_bilinear_cells')},indent=2))
if __name__=='__main__':main()
