"""Stationary-muon recoil-domain geometry on frozen 10 MeV B.16 weights."""
from __future__ import annotations
import hashlib, json, platform, sys
from pathlib import Path
import numpy as np
import scipy
B=Path(__file__).resolve().parent/"baseline"
sys.path.insert(0,str(B))
from weighted import NATIVE_KEYS, CHANNELS
from inputs.reference import M_MU, radial_rule, load_profile, local_rates, scalar_optical_depths
from inputs.audit_b16_global_redshift import eq_b1_source_measure,float_array_sha256

def support(w,m,M):
    k=np.sqrt((w-m)*(w+m))
    cut=(M*M+m*m)/(2*M)
    # Positive photon energy at fixed outgoing V energy given an initial rest muon.
    cos_min=np.divide(w-M,k,out=np.full_like(w,-np.inf),where=k>0)
    incoming_support=(1-np.clip(cos_min,-1.,1.))/2
    # For V + mu(rest) -> gamma + mu at the *scattering* angle 90 degrees.
    e_out_90=(M*w+m*m/2)/(M+w)
    # Same invariant s in forward/inverse processes: exact p_V^2/p_gamma^2,
    # divided by beta_lab^2 (the no-recoil detailed balance phase-space factor).
    cm_phase_space_relative=1/(1+m*m/(2*M*w))**2
    return {
        "stationary_production_backward_forbidden": w>=cut,
        "stationary_absorption_recoil_90_gt_10pct": 1-e_out_90/w>0.1,
        "stationary_absorption_recoil_90_gt_50pct": 1-e_out_90/w>0.5,
        "stationary_production_cosine_support_fraction_geometric": incoming_support,
        "matched_s_p2ratio_relative_to_printed_lab_beta2": cm_phase_space_relative,
        "propagation_beta_lt_0p9": k/w<0.9,
    }

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run():
    def read(path):return json.loads((B/path).read_text())
    h=read('inputs/high_order.json')
    native=read('weighted-native.json')
    q=h['quadratures']
    mass=h['result']['mass_MeV'];R=q['radius_km']
    assert mass==10
    profile=B/'inputs/sfho188_digitized.csv'
    assert sha(profile)==h['profile_sha256']
    assert sha(B/'weighted-native.json')=='a93b2d515586976d7012a80bad6be7b2f004eccb3a70c9b5116746f04e8723bc'
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
    s={ch:src_chan[ch][:,None,:]*a[None,:,None] for ch in CHANNELS}
    st=sum(s.values());ct=sum(c.values())
    observables=support(e,mass,M_MU)
    def summarize(weight):
        norm=weight.sum()
        return {key:float(np.sum(weight*val)/norm) for key,val in observables.items()}
    thin_co=s['semi_compton'].sum(axis=(0,1))
    thin_nu=s['neutrino'].sum(axis=(0,1))
    out=[]
    for ix in native['weak_peak_strong_indices']:
        row=native['points'][ix];g=row['g'];surv=np.exp(-g*g*ct);esc=st*surv
        semiesc=(s['semi_compton']*surv).sum(axis=(0,1))
        nu_esc=(s['neutrino']*surv).sum(axis=(0,1))
        cop=(esc*(g*g*c['semi_compton'])).sum(axis=(0,1))
        nup=(esc*(g*g*c['neutrino'])).sum(axis=(0,1))
        total=esc.sum()
        old=row['channel_tangents']
        recovered=[g*g*total/row['luminosity_erg_s']-1.,
                   semiesc.sum()/total-old['semi_compton']['source_only_dlnL_dln_channel_rate'],
                   cop.sum()/total+old['semi_compton']['opacity_only_dlnL_dln_channel_rate'],
                   nu_esc.sum()/total-old['neutrino']['source_only_dlnL_dln_channel_rate'],
                   nup.sum()/total+old['neutrino']['opacity_only_dlnL_dln_channel_rate']]
        assert max(map(abs,recovered))<2.e-13
        # Beta-only diagnostic for neutrino; do not apply stationary-muon observables.
        beta=observables['propagation_beta_lt_0p9']
        out.append({"index":ix,"g":g,"semi_compton_escaped_source":summarize(semiesc),
                    "semi_compton_esc_weighted_opacity":summarize(cop),
                    "neutrino_escaped_source_fraction_beta_lt_0p9":float(np.dot(nu_esc,beta)/nu_esc.sum()),
                    "neutrino_esc_weighted_opacity_fraction_beta_lt_0p9":float(np.dot(nup,beta)/nup.sum()),
                    "maximum_archive_closure_absolute":max(map(abs,recovered))})
    return {"archive_ref":"972f282a2958aa39ada1c630901cc5720a451ea2",
            "runtime":[platform.python_version(),np.__version__,scipy.__version__],
            "domain":"Diagnostics of unmodified reconstructed B.16 source, escaping source, and derivative opacity measure; no model replacement or refit.",
            "energy_grid_sha256":ids['energy_grid_sha256'],
            "mass_MeV":mass,"stationary_muon_mass_MeV":M_MU,
            "stationary_production_backward_threshold_MeV":(M_MU*M_MU+mass*mass)/(2*M_MU),
            "stationary_absorption_90deg_loss_gt_50pct_energy_MeV":(M_MU+np.hypot(M_MU,2*mass))/2,
            "semi_compton_thin_source":summarize(thin_co),
            "neutrino_thin_source_fraction_beta_lt_0p9":float(np.dot(thin_nu,observables['propagation_beta_lt_0p9'])/thin_nu.sum()),
            "at_weak_peak_strong_vertices":out}
if __name__=='__main__':
    Path(sys.argv[1]).write_text(json.dumps(run(),indent=2,sort_keys=True,allow_nan=False)+'\n')
