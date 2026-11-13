"""Run the specified stationary-profile cooling benchmark and sensitivity scans."""
import argparse,json,time
from pathlib import Path
import numpy as np
from rates import compton_kernels,compton_absorption,neutrino_rates,charged_muon_decay_rates
from transport import (radial_rule,effective_muon_density,angular_columns,
                       luminosities,source_weights,surface_blackbody)
HERE=Path(__file__).resolve().parent

def load_profile(path,r,zero_numu=False):
    data=np.genfromtxt(path,delimiter=',',names=True)
    result={n:np.interp(r,data['r_km'],data[n]) for n in ('T_MeV','mu_mu_MeV','mu_numu_MeV','lapse')}
    if zero_numu: result['mu_numu_MeV']*=0
    return result

def find_intervals(gs,ls,threshold):
    """All logarithmically interpolated crossings, no assumption one island."""
    x=np.log(gs);y=np.log(np.maximum(ls,1e-300))-np.log(threshold)
    crossings=[]
    for j in range(len(x)-1):
        if y[j]*y[j+1]<0:
            crossings.append(float(np.exp(x[j]-y[j]*(x[j+1]-x[j])/(y[j+1]-y[j]))))
    bounds=[float(gs[0])]+crossings+[float(gs[-1])]
    result=[]
    for a,b in zip(bounds[:-1],bounds[1:]):
        if np.interp(np.log(np.sqrt(a*b)),x,y)>0:result.append([a,b])
    return result

def evaluate(mass,profile,couplings,current='axial',nr=66,ne=140,na=20,ns=40,nc=32,
             radius=25.,emax_offset=1200.,compton_scale=1.,zero_numu=False):
    r,rw=radial_rule(radius,nr)
    grid=np.r_[0,r,radius]
    p=load_profile(profile,grid,zero_numu)
    # Log kinetic-energy mesh resolves both threshold and low-mass thermal peak.
    e=mass+np.geomspace(max(mass*1e-6,1e-6),emax_offset,ne)
    e=np.unique(np.r_[e,mass/p['lapse']])
    e.sort()
    # Exactly at threshold v=0 is not sampled.
    e=e[e>mass*(1+1e-9)]
    t=p['T_MeV']
    nmu=effective_muon_density(t,p['mu_mu_MeV'])
    ca=compton_absorption(compton_kernels(mass,e,nc,current),t,nmu)*compton_scale
    cp=np.exp(-e[None,:,None]/t[:,None,None])*ca
    npd,nab=neutrino_rates(mass,e[None,:],t[:,None],p['mu_numu_MeV'][:,None])
    mpd,mab=charged_muon_decay_rates(mass,e[None,:],t[:,None],p['mu_mu_MeV'][:,None],current=current)
    prod=cp+npd+mpd
    red=-np.expm1(-e[None,:,None]/t[:,None,None])*(ca+nab+mab)
    columns,wa=angular_columns(r,grid,red,mass,e,radius,na,ns)
    src=source_weights(r,rw,e,p['lapse'][1:-1],prod[1:-1],mass)
    ls=luminosities(src,columns,wa,couplings)
    thin_unit=np.sum(src)
    parts={}
    for label,rate in [('Compton',cp),('neutrino',npd),('dimuon',mpd)]:
        parts[label]=float(np.sum(source_weights(r,rw,e,p['lapse'][1:-1],rate[1:-1],mass))/thin_unit)
    return dict(mass_MeV=float(mass),luminosity_erg_s=ls.tolist(),
                intervals_4p4e52=find_intervals(couplings,ls,4.4e52),
                intervals_3e52=find_intervals(couplings,ls,3e52),
                thin_unit_erg_s=float(thin_unit),thin_fractions=parts,
                surface_blackbody_erg_s=float(surface_blackbody(radius,t[-1],p['lapse'][-1],mass,e)))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--profile',type=Path,default=HERE/'data'/'sfho188_digitized.csv')
    ap.add_argument('--output',type=Path,default=HERE/'outputs'/'scan.json')
    ap.add_argument('--masses',default='')
    ap.add_argument('--mass-count',type=int,default=60)
    ap.add_argument('--current',choices=['axial','vector'],default='axial')
    ap.add_argument('--nr',type=int,default=66);ap.add_argument('--ne',type=int,default=140)
    ap.add_argument('--na',type=int,default=20);ap.add_argument('--ns',type=int,default=40)
    ap.add_argument('--nc',type=int,default=32);ap.add_argument('--radius',type=float,default=25.)
    ap.add_argument('--emax-offset',type=float,default=1200.)
    ap.add_argument('--compton-scale',type=float,default=1.)
    ap.add_argument('--zero-numu',action='store_true')
    ap.add_argument('--gmin',type=float,default=1e-14)
    ap.add_argument('--gmax',type=float,default=1e-4)
    ap.add_argument('--gcount',type=int,default=241)
    args=ap.parse_args()
    masses=np.array([float(x) for x in args.masses.split(',')]) if args.masses else np.unique(np.r_[np.geomspace(.01,500,args.mass_count),1,10,100,200,211,212,300])
    couplings=np.geomspace(args.gmin,args.gmax,args.gcount)
    config={k:v for k,v in vars(args).items() if k in ('nr','ne','na','ns','nc','radius','emax_offset','compton_scale','zero_numu','current')}
    output=dict(description='Conditional fixed-profile ballistic cooling benchmark; not hydrodynamics or LESN',config=config,
                profile=str(args.profile.name),couplings=couplings.tolist(),results=[])
    args.output.parent.mkdir(parents=True,exist_ok=True)
    start=time.time()
    for mass in masses:
        row=evaluate(mass,args.profile,couplings,**config)
        output['results'].append(row)
        print(f"{mass:.6g} MeV: {row['intervals_4p4e52']} ({time.time()-start:.1f}s)",flush=True)
        args.output.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
