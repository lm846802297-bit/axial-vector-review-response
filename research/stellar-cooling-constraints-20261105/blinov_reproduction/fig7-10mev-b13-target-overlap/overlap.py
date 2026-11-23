"""Same-grid B.16 weights inside generous outer bounds of B.13 targets."""
from __future__ import annotations
import hashlib
import json
import platform
import scipy
import sys
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
HERE=Path(__file__).resolve().parent
B=HERE/'baseline'
sys.path.insert(0,str(B))
from weighted import NATIVE_KEYS, CHANNELS
from inputs.reference import radial_rule, load_profile, local_rates, scalar_optical_depths, KM_TO_MEV_INV
from inputs.audit_b16_global_redshift import eq_b1_source_measure,float_array_sha256


def limits(rows,mass):
    r=np.array([p['r_km'] for p in rows])
    x=np.array([p['x'] for p in rows])
    e=np.array([p['omega_local_MeV'] for p in rows])
    t=np.array([p['final_payload']['temperature_MeV'] for p in rows])
    err=float(max(abs(e-(mass+x*t))))
    if err>1e-12 or len(set(zip(r,x)))!=len(rows) or min(x)<0:
        raise ValueError('unexpected B13 point measure or duplicates')
    return {'r_min':float(min(r)), 'r_max':float(max(r)), 'x_min':float(min(x)),
            'x_max':float(max(x)), 'omega_max':float(max(e)), 'n':len(rows),
            'n_radial':len(set(r)), 'n_x':len(set(x)), 'energy_equivalence_max_abs_mev':err}


def rectangle(r,t,e,mass,f):
    x=(e-mass)/t
    return (r>=f['r_min']) & (r<=f['r_max']) & (x>=f['x_min']) & (x<=f['x_max']) & (e<=f['omega_max'])


def gap_certificate(profile,m,f):
    """Conservative lower bound on m/N(r) - (m+x_max T(r))."""
    r=profile['r_km']
    l,rmax=f['r_min'],f['r_max']
    knots=np.r_[l,r[(r>l)&(r<rmax)],rmax]
    N=np.interp(knots,r,profile['lapse'])
    T=np.interp(knots,r,profile['T_MeV'])
    if not (np.all(N>0.) and np.all(T>0.)):
        raise ValueError("lapse and temperature must be positive")
    # Linear interpolation implies maxima are at interval endpoints; crude
    # separate endpoint maxima give a guaranteed lower bound at every radius.
    lower=m/np.maximum(N[:-1],N[1:])-m-f['x_max']*np.maximum(T[:-1],T[1:])
    idx=int(np.argmin(lower))
    return {'min_gap_lower_bound_mev':float(lower[idx]),
            'controlling_interval_km':knots[idx:idx+2].tolist(),
            'intervals':len(lower)}



def chord_rectangle(r,ro,p_native,reduced,m,e,q,f):
    R=q['radius_km']; ang, aw = leggauss(q['angular_order'])
    px,pw=leggauss(q['path_order'])
    r=r[:,None]
    v=np.sqrt(1-(m/e)**2)
    col=np.zeros((len(r),len(ang),len(e)))
    for ia, cosine in enumerate(ang):
        smax=-cosine*r+np.sqrt(R**2-r**2+r**2*cosine*cosine)
        s=smax*(1+px[None,:])/2
        pos=np.sqrt(np.maximum(r*r+s*s+2*r*s*cosine,0.))
        weights=smax*pw[None,:]/2
        t=np.interp(pos,p_native['r_km'],p_native['T_MeV'])
        for i in np.flatnonzero(e<=f['omega_max']):
            rate=np.interp(pos,ro,reduced[:,i])
            mask=rectangle(pos,t,e[i],m,f)
            col[:,ia,i]=np.sum(weights*rate*mask,axis=1)*KM_TO_MEV_INV/v[i]
    return col


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def run():
    def read(p): return json.loads(p.read_text())
    h=read(B/'inputs/high_order.json')
    native=read(B/'weighted-native.json')
    profile=B/'inputs/sfho188_digitized.csv'
    targets=HERE/'pr133-target-points.json'
    q=h['quadratures']
    mass=h['result']['mass_MeV']; R=q['radius_km']
    assert mass==10
    assert sha(profile)==h['profile_sha256']
    assert sha(B/'weighted-native.json')=='a93b2d515586976d7012a80bad6be7b2f004eccb3a70c9b5116746f04e8723bc'
    f=limits(read(targets),mass)
    assert f['n']==431 and f['x_max']==0.05
    p_native=np.genfromtxt(profile,delimiter=',',names=True)
    assert np.all(np.diff(p_native['r_km'])>0)
    cert=gap_certificate(p_native,mass,f)
    assert cert['min_gap_lower_bound_mev']>0
    r,rw=radial_rule(R,q['source_radial_order'])
    ro=np.r_[0.,radial_rule(R,q['opacity_order'])[0],R]
    sl=load_profile(profile,r); ol=load_profile(profile,ro)
    e=np.unique(np.r_[mass+np.geomspace(max(mass*1.e-6,1.e-6),q['energy_offset_MeV'],
                     q['base_energy_order']),mass/ol['lapse']])
    e=e[e>mass*(1.+1.e-10)]
    ids=h['grid_identity']
    assert all(float_array_sha256(grid)==ids[key+'_grid_sha256'] for grid,key in
        ((r,'source'),(ro,'opacity'),(e,'energy')))
    def rate(p): return local_rates(mass,e[None,:],p['T'][:,None],p['mu_numu'][:,None],p['mu_mu'][:,None])
    src, op=rate(sl),rate(ol)
    assert np.max(src['dimuon_production'])==np.max(op['dimuon_production'])==0
    x=e[None,:]/ol['T'][:,None]
    balance=-np.expm1(-x)*np.exp(np.minimum(x,700.))
    src_chan={};c={}
    for ch,n in NATIVE_KEYS.items():
        src_chan[ch],_=eq_b1_source_measure(r,rw,e,sl['lapse'],mass,src[n])
        c[ch],a=scalar_optical_depths(r,ro,balance*op[n],mass,e,R,q['angular_order'],q['path_order'])
    semi_reduced=balance*op[NATIVE_KEYS['semi_compton']]
    cr=chord_rectangle(r,ro,p_native,semi_reduced,mass,e,q,f)
    C=c['semi_compton']; assert np.all(cr>=0.) and np.all(cr<=C*(1+1e-13))
    energy=e<=f['omega_max']
    source_rectangle=rectangle(r[:,None],sl['T'][:,None],e[None,:],mass,f)
    s={ch:src_chan[ch][:,None,:]*a[None,:,None] for ch in CHANNELS}
    st=sum(s.values()); ct=sum(c.values()); S=s['semi_compton']
    def fraction(weight,mask): return float((weight*mask).sum()/weight.sum())
    out=[]
    for i in native['weak_peak_strong_indices']:
        row=native['points'][i];g=row['g'];P=np.exp(-g*g*ct);escaped=st*P
        W=S*P; D=escaped*g*g*C; dR=escaped*g*g*cr
        s_energy=fraction(W,energy)
        s_rect=fraction(W,source_rectangle[:,None,:])
        d_energy=fraction(D,energy)
        d_rect=float(dR.sum()/D.sum())
        assert s_rect<=s_energy and d_rect<=d_energy
        old=row['channel_tangents']['semi_compton']
        closure=max(abs(g*g*escaped.sum()/row['luminosity_erg_s']-1),
                    abs(W.sum()/escaped.sum()-old['source_only_dlnL_dln_channel_rate']),
                    abs(D.sum()/escaped.sum()+old['opacity_only_dlnL_dln_channel_rate']))
        assert closure < 2.e-13
        out.append({'vertex':i,'g':g,'source_energy_only_overlap_upper_bound':s_energy,
                    'source_r_x_energy_overlap_upper_bound':s_rect,
                    'opacity_energy_only_overlap_upper_bound':d_energy,
                    'opacity_r_x_energy_overlap_upper_bound':d_rect,
                    'archive_closure_max':float(closure)})
    return {'target_archive_sha256':sha(targets),'b16_weighted_archive_sha256':sha(B/'weighted-native.json'),
            'grid_identity':ids,'target_envelope':f,
            'source_gap_certificate':cert,
            'runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
            'thin_semi_compton_source_energy_only_overlap_upper_bound':fraction(S,energy),
            'thin_semi_compton_source_r_x_energy_overlap_upper_bound':fraction(S,source_rectangle[:,None,:]),
            'vertices':out,
            'scope':'Upper bounds for targeted #133 validation only; no B.13 values interpolated, rates or luminosities replaced, or full B.13 archive coverage inferred.'}
if __name__=='__main__':
    Path(sys.argv[1]).write_text(json.dumps(run(),indent=2,sort_keys=True,allow_nan=False)+'\n')
