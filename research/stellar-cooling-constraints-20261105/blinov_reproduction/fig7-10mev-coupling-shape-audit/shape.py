"""Normalization-free Fig. 7 shape check on exact archived vector vertices."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.optimize import linprog

ROOT=Path(__file__).resolve().parent
TOL=1e-12

def load(p):return json.loads(Path(p).read_text())
def sig(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def native_data():
    inputs=ROOT/'inputs'
    provenance=load(inputs/'provenance.json')
    for row in provenance:
        p=inputs/row['local_name'];data=p.read_bytes()
        assert sig(p)==row['sha256']
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==row['git_blob']
    c=load(inputs/'high_order.json')['result']
    a=load(inputs/'geometry.json'); d=load(inputs/'drawings.json')
    assert a['source']['pdf_sha256']==d['pdf_sha256']==c['fig7_reference']['pdf_sha256']
    assert c['profile']['sha256']==c['code_sha256']['profile'] if 'sha256' in c['profile'] else True
    cfg=c['configuration']; assert c['mass_MeV']==10 and cfg['couplings_are_g_not_alpha_V'] is True
    frame=a['axis_frame']; t=[x for x in a['curves'].values() if x['mass_MeV']==10][0]
    assert t['visible_vertices_used_in_reference']==25
    draw=[x for x in d['drawings'] if x['index']==t['drawing_index']][0]
    xy=np.array(draw['path_vertices'])
    xy=xy[(xy[:,1]>=frame['y_top'])&(xy[:,1]<=frame['y_bottom'])]
    assert len(xy)==25 and np.all(np.diff(xy[:,0])>0)
    # Transform stored vector coordinates; path and scalar archive are both checked.
    ax=frame['x_right']-frame['x_left'];ay=frame['y_bottom']-frame['y_top']
    gv=np.sqrt(4*np.pi*10.**(-22+16*(xy[:,0]-frame['x_left'])/ax))
    lv=10.**(52+3*(frame['y_bottom']-xy[:,1])/ay)
    fixed=c['eq_b2_fixed_omega_baseline']['points']; remap=c['path_redshift_only_diagnostic']['points']
    g=np.array([row['g'] for row in fixed]);r=np.array([row['reference_luminosity_erg_s'] for row in fixed]); thin=np.array([row['optically_thin_luminosity_erg_s'] for row in fixed])
    assert np.array_equal(g,[row['g'] for row in remap])
    assert np.array_equal(r,[row['reference_luminosity_erg_s'] for row in remap])
    assert np.array_equal(thin,[row['optically_thin_luminosity_erg_s'] for row in remap])
    assert np.max(abs((thin/g**2)/(thin[-1]/g[-1]**2)-1))<2.e-13
    diff=max(np.max(abs(gv/g-1)),np.max(abs(lv/r-1)))
    assert diff<2.e-13
    q=load(inputs/'c1_convergence.json'); qr=q['radial_grid_convergence']
    c1={'role':'separate C1 adaptive transport, not the literal Appendix B scalar B.16 lane',
        'profile_sha256':q['profile_sha256'],
        'radial_sizes':[qr['coarse_radial_points'],qr['fine_radial_points']],
        'relevance':qr['relevant_region_definition'],
        'max_relevant_pointwise_relative':qr['max_relevant_pointwise_relative_difference_all_boundaries_and_modes'],
        'raw_100km_total_tail_relative':qr['raw_100km_tail_relative_max'],
        'raw_100km_total_tail_reference_fraction_of_peak':qr['raw_100km_tail_reference_fraction_of_peak_at_relative_max'],
        'legacy_simpson_over_adaptive_at_final_g':q['legacy_simpson_over_adaptive_samples'][-1],
        'checksum_manifest_verified':qr['checksum_manifest_verified']}
    assert c1['radial_sizes']==[103,153] and c1['checksum_manifest_verified'] is True
    assert c1['profile_sha256']==c['code_sha256']['profile']
    return {'input_provenance':provenance,'g':g,'ref':r,
       'fixed':np.array([row['calculated_luminosity_erg_s'] for row in fixed]),
       'redshift':np.array([row['calculated_luminosity_erg_s'] for row in remap]),
       'thin':thin,'geometry_crosscheck_max_rel':float(diff),'source_pdf_sha256':d['pdf_sha256'],
       'pdf_path_width_pt':draw['width'],'pdf_y_scale_to_ln_L':3*np.log(10)/ay,'reference_drawing_index':t['drawing_index'],
       'pdf_vertices_xy':xy,'C1_grid_prior':c1}

def shape(x,y):
    x=np.asarray(x,float); y=np.asarray(y,float)
    assert x.ndim==1 and len(x)==len(y)>=3 and np.all(np.diff(x)>0)
    n=len(x); slopes=np.diff(y)/np.diff(x)
    ts=(x[1:-1]-x[:-2])/(x[2:]-x[:-2]); gap=y[1:-1]-(1-ts)*y[:-2]-ts*y[2:]
    # LP merely finds minimum perturbation band at fixed x for these necessary
    # shape inequalities. It returns no altered curve or opacity model.
    cons=[]; rs=[]
    for i in range(n-1):
        row=np.zeros(n+1); row[i]=-1.;row[i+1]=1.
        cons.append(row);rs.append(0.)
    for i,t in enumerate(ts):
        row=np.zeros(n+1);row[i]=-(1-t);row[i+1]=1;row[i+2]=-t
        cons.append(row);rs.append(0.)
    for i,v in enumerate(y):
        for sign in (1,-1):
            row=np.zeros(n+1);row[i]=sign;row[-1]=-1
            cons.append(row);rs.append(sign*v)
    obj=np.zeros(n+1);obj[-1]=1
    r=linprog(obj,A_ub=cons,b_ub=rs,bounds=[(None,None)]*n+[(0,None)],method='highs')
    assert r.success,r.message
    return {'n_monotonicity_violations':int(np.count_nonzero(np.diff(y)>TOL)),
            'n_convexity_violations':int(np.count_nonzero(gap>TOL)),
            'max_positive_log_convexity_excess':max(0.,float(np.max(gap))),
            'triplets':[{'middle_index':i+1,'jensen_excess_ln':float(v)} for i,v in enumerate(gap)],
            'negative_log_secants':(-slopes).tolist(),
            'min_vertical_log_envelope_for_shape_feasibility':float(r.fun)}

def scale_free_window(x,calc,ref,i,j):
    eps=x[j]-x[i]; db=calc[j]-calc[i]; dr=ref[j]-ref[i]
    return {'indices':[i,j],'reference_mean_escape_exponent':float(-dr/eps),
       'calculation_mean_escape_exponent':float(-db/eps),'log_ratio_change':float(db-dr),
       'ratio_change_multiplier':float(np.exp(db-dr))}

def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);a=p.parse_args()
    d=native_data();g=d['g'];x=(g/g[-1])**2;ypeak=int(np.argmax(d['ref']))
    Ln=lambda w:np.log((d[w]/d['ref'][-1])/x)
    logs={m:Ln(m) for m in ['ref','fixed','redshift']}
    test={m:shape(x,v) for m,v in logs.items()}
    for m in ('fixed','redshift'):
        assert test[m]['n_monotonicity_violations']==test[m]['n_convexity_violations']==0
    half=d['pdf_path_width_pt']*.5*d['pdf_y_scale_to_ln_L']
    for v in test.values():
        v['min_vertical_pdf_pt_for_shape_feasibility']=v['min_vertical_log_envelope_for_shape_feasibility']/d['pdf_y_scale_to_ln_L']
    tests_tail={m:shape(x[ypeak:],v[ypeak:]) for m,v in logs.items()}
    windows={}
    for i,j,label in [(0,ypeak,'weak_to_peak'),(ypeak,len(x)-1,'peak_to_strong'),(len(x)-2,len(x)-1,'last_active_segment')]:
        windows[label]={m:scale_free_window(x,logs[m],logs['ref'],i,j) for m in ('fixed','redshift')}
        windows[label]['g_bounds']=[float(g[i]),float(g[j])]
        windows[label]['vertical_only_half_path_width_at_two_vertices_ln_bound']=float(2*half)
    rows=[]
    for i,v in enumerate(g):
        r={'row':i,'g':float(v),'g_squared_normalized':float(x[i]),'pdf_xy':d['pdf_vertices_xy'][i].tolist(),
           'luminosity_erg_s':{m:float(d[m][i]) for m in ['ref','fixed','redshift','thin']},
           'luminosity_ratio_to_Fig7':{m:float(d[m][i]/d['ref'][i]) for m in ['fixed','redshift','thin']},
           'log_L_over_g_squared_common_normalization':{m:float(logs[m][i]) for m in logs}}
        rows.append(r)
    out={'research_scope':'fixed-g² positivity/shape diagnostic only; no fitting, opacity scaling, or change to the model',
      'inputs':d['input_provenance'],'source_pdf_sha256':d['source_pdf_sha256'],'source_path_index':d['reference_drawing_index'],
      'source_path_width_pdf_pt':d['pdf_path_width_pt'],'source_path_half_width_at_fixed_g_ln_L':float(half),
      'geometry_crosscheck_max_rel':d['geometry_crosscheck_max_rel'],'baseline_profile_sha256':d['C1_grid_prior']['profile_sha256'],
      'C1_grid_prior':d['C1_grid_prior'],'shape_all_vertices':test,'shape_peak_and_tail':tests_tail,
      'scale_free_windows':windows,'aligned_vertices':rows,
      'runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'source_sha256':sig(__file__)}
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True,allow_nan=False)+'\n')
    print('Vertices',len(rows),'peak',ypeak,'geometry relative max',d['geometry_crosscheck_max_rel'])
    print('Reference convexity positive',test['ref']['n_convexity_violations'],'fit bound pdf points',test['ref']['min_vertical_pdf_pt_for_shape_feasibility'],'path width',d['pdf_path_width_pt'])
    for k,v in windows.items():print(k,v)
if __name__=='__main__':main()
