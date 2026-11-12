"""Reproduce external vector benchmarks without changing production scan data.

The literal Blinov mode reproduces the published spin-summed opacity formula
as a DIAGNOSTIC. It is not silently promoted to the physical per-mode solver.
Run: OPENBLAS_NUM_THREADS=1 python run_vector_audit.py
"""
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar
import rates
import transport as tr
from run_scan import load_profile,find_intervals
from vector_reference import (summed_decay_production,thomson_absorption_modes,
                              number_density)
from extract_vector_reference import crossings

HERE=Path(__file__).resolve().parent


def build(mass,profile,variant,nr=88,ne=180,na=24,ns=64,nc=40):
    radius=25.
    r,rw=tr.radial_rule(radius,nr);grid=np.r_[0,r,radius]
    p=load_profile(profile,grid)
    lapse=p['lapse'] if variant!='no_gr_diagnostic' else np.ones_like(grid)
    e=mass+np.geomspace(max(mass*1e-6,1e-6),1200.,ne)
    e=np.unique(np.r_[e,mass/lapse]);e=e[e>mass*(1+1e-9)]
    t=p['T_MeV'];n=tr.effective_muon_density(t,p['mu_mu_MeV'])
    exponential=np.exp(-e[None,:,None]/t[:,None,None])
    if variant in ['blinov_literal','blinov_average']:
        # Independently evaluate B.7/B.9/B.11; no use of decay quadrature.
        nu,mm=summed_decay_production(mass,e[None,:],t[:,None],
                                     p['mu_numu_MeV'][:,None],p['mu_mu_MeV'][:,None])
        ca=thomson_absorption_modes(mass,e,t,n).sum(-1,keepdims=True)
        cp=exponential*ca
        components=[cp,nu[...,None],mm[...,None]]
        prod=sum(components)
        # B.10/B.19; algebraically equivalent but stable at high energy.
        red=prod*np.expm1(e[None,:,None]/t[:,None,None])
        if variant=='blinov_average':red=red/3
    elif variant=='exact_recoil_scalar':
        # Same scalar summed-opacity transport as the literal B.14 lane,
        # but replace only the no-recoil Compton kernel by the exact-recoil
        # fixed-target kernel. Sum all three polarizations before transport.
        ca=rates.compton_absorption(
            rates.compton_kernels(mass,e,nc,'vector'),t,n
        ).sum(-1,keepdims=True)
        cp=exponential*ca
        nu,na_rate=rates.neutrino_rates(
            mass,e[None,:],t[:,None],p['mu_numu_MeV'][:,None])
        mm,ma_rate=rates.charged_muon_decay_rates(
            mass,e[None,:],t[:,None],p['mu_mu_MeV'][:,None],current='vector')
        nu=nu.sum(-1,keepdims=True);na_rate=na_rate.sum(-1,keepdims=True)
        mm=mm.sum(-1,keepdims=True);ma_rate=ma_rate.sum(-1,keepdims=True)
        components=[cp,nu,mm];prod=sum(components)
        red=-np.expm1(-e[None,:,None]/t[:,None,None])*(ca+na_rate+ma_rate)
    else:
        if variant=='thomson_modes':ca=thomson_absorption_modes(mass,e,t,n)
        else:ca=rates.compton_absorption(rates.compton_kernels(mass,e,nc,'vector'),t,n)
        cp=exponential*ca
        nu,na_rate=rates.neutrino_rates(mass,e[None,:],t[:,None],p['mu_numu_MeV'][:,None])
        mm,ma_rate=rates.charged_muon_decay_rates(mass,e[None,:],t[:,None],p['mu_mu_MeV'][:,None],current='vector')
        components=[cp,nu,mm];prod=sum(components)
        red=-np.expm1(-e[None,:,None]/t[:,None,None])*(ca+na_rate+ma_rate)
    columns,angles=tr.angular_columns(r,grid,red,mass,e,radius,na,ns)
    weights=[tr.source_weights(r,rw,e,lapse[1:-1],part[1:-1],mass) for part in components]
    return sum(weights),weights,columns,angles


def evaluate(mass,profile,variant,couplings,**resolution):
    source,parts,columns,angles=build(mass,profile,variant,**resolution)
    ls=tr.luminosities(source,columns,angles,couplings)
    # Optimize the physical peak in g, so a coarse coupling grid cannot
    # falsely close a small contour island at the high-mass endpoint.
    j=int(np.argmax(ls))
    bounds=np.log(couplings[[max(j-1,0),min(j+1,len(couplings)-1)]])
    peak=minimize_scalar(lambda x:-tr.luminosities(source,columns,angles,[np.exp(x)])[0],
                         bounds=bounds,method='bounded',options={'xatol':1e-8})
    channel={}
    for name,src in zip(['Compton','neutrino','dimuon'],parts):
        channel[name]={'thin_unit_erg_s':float(src.sum()),
                      'escaped_erg_s_at_g_1e-10_1e-9_1e-8':tr.luminosities(
                           src,columns,angles,[1e-10,1e-9,1e-8]).tolist()}
    return {'mass_MeV':float(mass),'intervals_4p4e52':find_intervals(couplings,ls,4.4e52),
            'intervals_3e52':find_intervals(couplings,ls,3e52),
            'maximum_luminosity_erg_s':float(-peak.fun),'coupling_at_maximum':float(np.exp(peak.x)),
            'channels':channel}


def profile_audit():
    d=np.genfromtxt(HERE/'data'/'sfho188_digitized.csv',delimiter=',',names=True)
    plotted=np.loadtxt(HERE/'data'/'n_mu_over_n0_caputo_vertices.csv',delimiter=',',skiprows=1)
    rows=[]
    for r in [0.,5.,8.,10.,15.]:
        t,mu,alt=[np.interp(r,d['r_km'],d[k]) for k in ['T_MeV','mu_mu_MeV','mu_mu_Ferreira_MeV']]
        nplot=np.interp(r,plotted[:,0],plotted[:,1])*.181
        ncap=number_density(t,mu);nalt=number_density(t,alt)
        rows.append({'r_km':r,'T_MeV':t,'caputo_mu_MeV':mu,'ferreira_mu_MeV':alt,
            'delta_mu_MeV':alt-mu,'caputo_n_fm3':ncap,'plotted_n_fm3':nplot,
            'caputo_density_relative_error':ncap/nplot-1,
            'ferreira_density_over_caputo_plot':nalt/nplot})
    return {'samples':rows,
        'definition_check':'Both papers use f=1/(exp((E-mu)/T)+1) with E including rest energy. The difference is radius-dependent, not a constant +/-m_mu convention.',
        'raw_data_access':'2026-11-07: Garching Bollig2016_radial_profiles endpoint returns HTTP 401 Basic authentication; no protected data acquired.',
        'disposition':'Caputo mu reproduces its separately plotted negative-muon density. Keep baseline; origin of Ferreira discrepancy remains unresolved without raw snapshot/column metadata.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output-dir',type=Path,default=HERE/'outputs'/'vector_audit')
    ap.add_argument('--masses',default='1,2,3,5,7,10,15,20,30,50,70,100,120,150,180,200,205,210,211,212,220,240,250,255,260,265,280,300')
    args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    profile=HERE/'data'/'sfho188_digitized.csv'
    gs=np.geomspace(1e-12,1e-5,401)
    config=dict(nr=88,ne=180,na=24,ns=64,nc=40)
    records={'date':'2026-11-07','configuration':config,'profile_sha256':hashlib.sha256(profile.read_bytes()).hexdigest(),
             'status':'Research audit; full physics acceptance remains open',
             'profile_audit':profile_audit(),'scans':{},'comparison':[], 'convergence':[]}
    masses=[float(m) for m in args.masses.split(',')]
    start=time.time()
    for variant in ['exact_modes','thomson_modes','blinov_literal','blinov_average']:
        rows=[]
        for mass in masses:
            row=evaluate(mass,profile,variant,gs,**config);rows.append(row)
            print(variant,mass,row['intervals_4p4e52'],f'{time.time()-start:.1f}s',flush=True)
        records['scans'][variant]=rows
        (args.output_dir/'audit.json').write_text(json.dumps(records,indent=2)+'\n')
    # A controlled redshift switch is useful for Wang, but is not a claim of
    # full reproduction of its differing and partly inconsistent formulas.
    records['scans']['no_gr_diagnostic']=[evaluate(m,profile,'no_gr_diagnostic',gs,**config) for m in [1.,10.,100.,200.,300.]]
    curves={n:np.loadtxt(HERE/'data'/'vector_reference'/f'{n}_cooling_vertices.csv',delimiter=',',skiprows=1)
            for n in ['blinov','wang']}
    for variant,rows in records['scans'].items():
        for row in rows:
            for name,verts in curves.items():
                ref=crossings(verts,row['mass_MeV'])
                ours=row['intervals_4p4e52' if name=='blinov' else 'intervals_3e52']
                if len(ref)==2 and len(ours)==1:
                    records['comparison'].append({'reference':name,'variant':variant,'mass_MeV':row['mass_MeV'],
                        'reference_lower':ref[0],'reference_upper':ref[1],
                        'calculated_lower':ours[0][0],'calculated_upper':ours[0][1],
                        'relative_lower':ours[0][0]/ref[0]-1,'relative_upper':ours[0][1]/ref[1]-1})
    # Only selected points are rerun, with independent resolution increases.
    for variant in ['exact_modes','blinov_literal']:
        for mass in [1.,100.,200.]:
            fine=evaluate(mass,profile,variant,gs,nr=132,ne=280,na=40,ns=96,nc=64)
            base=next(x for x in records['scans'][variant] if x['mass_MeV']==mass)
            records['convergence'].append({'variant':variant,'mass_MeV':mass,
                'fine_intervals_4p4e52':fine['intervals_4p4e52'],
                'relative_boundary_changes':(np.array(fine['intervals_4p4e52'][0])/base['intervals_4p4e52'][0]-1).tolist()})
    # Refine both mass endpoints with optimized peak luminosity, no fitted rescaling.
    records['endpoint_brackets_MeV']={}
    for variant,lo,hi in [('exact_modes',250.,265.),('blinov_literal',200.,220.)]:
        assert evaluate(lo,profile,variant,gs,**config)['maximum_luminosity_erg_s']>4.4e52
        assert evaluate(hi,profile,variant,gs,**config)['maximum_luminosity_erg_s']<4.4e52
        while hi-lo>.1:
            mid=(lo+hi)/2
            row=evaluate(mid,profile,variant,gs,**config)
            if row['maximum_luminosity_erg_s']>4.4e52:lo=mid
            else:hi=mid
        records['endpoint_brackets_MeV'][variant]=[lo,hi]
    records['runtime_seconds']=time.time()-start
    records['code_sha256']={p:hashlib.sha256((HERE/p).read_bytes()).hexdigest()
                           for p in ['run_vector_audit.py','vector_reference.py','rates.py','transport.py']}
    (args.output_dir/'audit.json').write_text(json.dumps(records,indent=2)+'\n')
    import csv
    with (args.output_dir/'contour_comparison.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(records['comparison'][0]));writer.writeheader();writer.writerows(records['comparison'])
    print('Endpoint brackets:',records['endpoint_brackets_MeV'])

if __name__=='__main__':main()
