"""Finite-momentum photon mixing and a mass-dependent NA64 comparison.

Python + mpmath. NA64 Fig. 3 is visually digitized in log-log coordinates;
the stored intervals are deliberately conservative read-off ranges, not
machine-readable official data points. The comparison uses epsilon*sqrt(Br_inv).
"""
from pathlib import Path
import hashlib
import json
import platform
import mpmath as mp


def evaluate(dps):
    mp.mp.dps = dps
    e, mu, tau = map(mp.mpf, ('0.3028', '0.105658', '1.77686'))
    theta = mp.mpf('0.01')

    def weighted_log(mass, q):
        if q == 0:
            return mp.log(mass**2) / 6
        points = [mp.mpf(0), mp.mpf('0.5'), mp.mpf(1)]
        imaginary = mp.mpf(0)
        if q > 2 * mass:
            beta = mp.sqrt(1 - 4 * mass**2 / q**2)
            points += [(1 - beta)/2, (1 + beta)/2]
            imaginary = -mp.pi * (beta/4 - beta**3/12)

        def integrand(x):
            argument = mass**2 - q**2 * x * (1-x)
            if argument == 0:  # Isolated integrable logarithmic endpoint.
                return mp.mpf(0)
            return x * (1-x) * mp.log(abs(argument))

        real = mp.quad(integrand, sorted(set(points)))
        return mp.mpc(real, imaginary)

    def epsilon_per_g(q):
        return -e * mp.sin(theta)**2 / (2*mp.pi**2) * (
            weighted_log(tau, q) - weighted_log(mu, q))

    masses = list(map(mp.mpf, ['0','0.01','0.1','0.2','0.212','0.3','0.5','1','3','10','100']))
    rows=[]
    zero=epsilon_per_g(mp.mpf(0))
    for mass in masses:
        value=epsilon_per_g(mass)
        rows.append({
            'm_A_GeV':mp.nstr(mass,8),
            'epsilon_per_g_real':mp.nstr(value.real,18),
            'epsilon_per_g_imag':mp.nstr(value.imag,18),
            'abs_epsilon_per_g':mp.nstr(abs(value),18),
            'ratio_to_zero_momentum':mp.nstr(abs(value/zero),18),
        })
    me=mp.mpf('0.00051099895')

    def width_ratios(mass, epsilon_over_g):
        # Ratios to Gamma(nu_munu + nu_taunu)=g_X^2 m_A'/(12 pi).
        # The direct axial/vector muon widths are included above 2 m_mu.
        # EM-induced hadronic widths are O((e epsilon/g_X)^2) and negligible
        # at these benchmarks compared with the direct neutrino/muon widths.
        r_mu = mp.mpf(0)
        rmu = (mu/mass)**2
        if mass > 2*mu:
            r_mu = mp.sqrt(1-4*rmu) * (
                mp.sin(theta)**4*(1+2*rmu)
                + mp.cos(theta)**4*(1-4*rmu))
        re = (me/mass)**2
        r_e = (e*abs(epsilon_over_g))**2 * (
            1+2*re)*mp.sqrt(1-4*re)
        br_inv = 1/(1+r_mu+r_e)
        return br_inv, r_mu, r_e

    mass=mp.mpf('0.1')
    ep=abs(epsilon_per_g(mass))
    br, rmu_ratio, re_ratio = width_ratios(mass, epsilon_per_g(mass))
    reference=mp.mpf('1e-4')
    # Check the complete four-state sum against the paired-light formula.
    # The heavy mass is only an algebraic/numerical check, not a fitted UV point.
    heavy=mp.mpf('20000')
    weights=[mp.sin(theta)**2,-mp.sin(theta)**2,
             mp.cos(theta)**2,-mp.cos(theta)**2]
    scale_checks=[]
    for scale in map(mp.mpf,['1','1000']):
        full=e/(2*mp.pi**2)*sum(
            w*(weighted_log(m,mass)-mp.log(scale**2)/6)
            for w,m in zip(weights,[mu,tau,heavy,heavy]))
        scale_checks.append(abs(full/epsilon_per_g(mass)-1))
    assert abs(sum(weights))<mp.mpf('1e-30')
    assert max(scale_checks)<mp.mpf('1e-25')
    resonance_energy=mass**2/(2*me)
    heavy_threshold_bound=e/(12*mp.pi**2)*mp.mpf('0.01')**2
    comparison=[]
    for g in map(mp.mpf,['0.0001','0.1','1']):
        ratio=g*ep*mp.sqrt(br)/reference
        comparison.append({'g_X':str(g),'abs_epsilon':mp.nstr(g*ep,18),
                           'epsilon_sqrt_Br_over_reference':mp.nstr(ratio,18),
                           'rate_over_reference':mp.nstr(ratio**2,18)})
    # Conservative visual read-off intervals from NA64 PRL 131, 161801,
    # Fig. 3 (90% CL); lower edges are used for the ratios below.
    # The intervals cover line thickness/read-off uncertainty (~0.2--0.3 dex).
    na64_curve = [
        {'m_A_GeV':'0.01','epsilon_limit_low':'8e-6','epsilon_limit_high':'2e-5',
         'production':'bremsstrahlung; positron resonance below missing-energy cut'},
        {'m_A_GeV':'0.1','epsilon_limit_low':'5e-5','epsilon_limit_high':'1.2e-4',
         'production':'bremsstrahlung; positron resonance below missing-energy cut'},
        {'m_A_GeV':'0.2','epsilon_limit_low':'7e-5','epsilon_limit_high':'1.8e-4',
         'production':'bremsstrahlung; positron resonance below missing-energy cut'},
        {'m_A_GeV':'0.3','epsilon_limit_low':'1e-4','epsilon_limit_high':'2.5e-4',
         'production':'bremsstrahlung plus secondary-positron resonance'},
    ]
    mass_comparison=[]
    for point in na64_curve:
        m=mp.mpf(point['m_A_GeV'])
        eps_g=abs(epsilon_per_g(m))
        br_m, rmu_m, re_m=width_ratios(m, epsilon_per_g(m))
        eps_eff_per_g=eps_g*mp.sqrt(br_m)
        eps_lim_low=mp.mpf(point['epsilon_limit_low'])
        eps_lim_high=mp.mpf(point['epsilon_limit_high'])
        e_res=m**2/(2*me)
        ratio_g01=mp.mpf('0.1')*eps_eff_per_g/eps_lim_low
        ratio_g1=eps_eff_per_g/eps_lim_low
        mass_comparison.append({
            'm_A_GeV':point['m_A_GeV'],
            'epsilon_per_g_abs':mp.nstr(eps_g,18),
            'Br_inv':mp.nstr(br_m,18),
            'Gamma_mumu_over_Gamma_nunu':mp.nstr(rmu_m,18),
            'Gamma_ee_over_Gamma_nunu':mp.nstr(re_m,18),
            'epsilon_eff_per_g':mp.nstr(eps_eff_per_g,18),
            'NA64_epsilon_90CL_visual_interval':[
                point['epsilon_limit_low'],point['epsilon_limit_high']],
            'NA64_conservative_lower_edge_used':point['epsilon_limit_low'],
            'epsilon_eff_over_limit_at_gX_0p1':mp.nstr(ratio_g01,18),
            'rate_over_limit_at_gX_0p1':mp.nstr(ratio_g01**2,18),
            'epsilon_eff_over_limit_at_gX_1':mp.nstr(ratio_g1,18),
            'rate_over_limit_at_gX_1':mp.nstr(ratio_g1**2,18),
            'secondary_positron_resonance_energy_GeV':mp.nstr(e_res,18),
            'NA64_missing_energy_cut_GeV':'approximately 50',
            'production_channel_note':point['production'],
        })

    return {'loop_table':rows,'comparison_at_100MeV':comparison,
            'NA64_mass_dependent_comparison':mass_comparison,
            'NA64_curve_digitization':{
                'source':'Andreev et al. (NA64), PRL 131, 161801 (2023), arXiv:2307.02404, Fig. 3, page 3',
                'method':'manual visual read-off in log-log coordinates from the published PDF; intervals include line-thickness/read-off uncertainty',
                'uncertainty':'approximately 0.2--0.3 dex; conservative lower interval edge used in all ratios',
                'interpretation':'90% CL invisible-dark-photon epsilon limit; not a detector-level recast',
                'rescaling':'epsilon_eff = |epsilon_gammaAprime(m_Aprime^2)| sqrt(Br_inv)',
            },
            'Gamma_ee_over_Gamma_nunu_100MeV':mp.nstr(re_ratio,18),
            'Br_inv_100MeV':mp.nstr(br,18),
            'Gamma_mumu_over_Gamma_nunu_300MeV':mass_comparison[-1]['Gamma_mumu_over_Gamma_nunu'],
            'Br_inv_300MeV':mass_comparison[-1]['Br_inv'],
            'four_state_sum_check':{
                'physical_heavy_masses_GeV':['20000','20000'],
                'right_handed_angles':['0.01','0.01'],
                'renormalization_scales_GeV':['1','1000'],
                'sum_vector_couplings_over_g':mp.nstr(sum(weights),8),
                'max_relative_difference_from_light_pair':mp.nstr(max(scale_checks),8),
                'scope':'Checks threshold cancellation and scale independence; not a full UV fit.'},
            'NA64_kinematic_check':{
                'secondary_positron_resonance_Aprime_energy_GeV_at_100MeV':mp.nstr(resonance_energy,18),
                'secondary_positron_resonance_energy_GeV_by_mass':{
                    p['m_A_GeV']:next(x['secondary_positron_resonance_energy_GeV']
                                      for x in mass_comparison if x['m_A_GeV']==p['m_A_GeV'])
                    for p in na64_curve},
                'missing_energy_selection_GeV':'approximately 50',
                'Gamma_total_over_mass_at_g0p1_100MeV':mp.nstr(mp.mpf('0.1')**2/(12*mp.pi)*(1+re_ratio),18),
                'prompt_width_qualification':'At g_X=0.1 and 1 the 300 MeV benchmark is prompt; lower g_X may require decay-length-dependent acceptance.'},
            'common_bare_mass_equal_right_mixing_estimate':{
                'scope':'Leading order in all angles; common bare M_E, equal right angles, abs(theta_L)<=0.01, epsilon_ind=0.',
                'heavy_threshold_abs_bound_per_g':mp.nstr(heavy_threshold_bound,18),
                'total_abs_bound_per_g_at_100MeV':mp.nstr(ep+heavy_threshold_bound,18)}}


def main():
    low,high=evaluate(35),evaluate(55)
    # Independent working precisions check integration near timelike thresholds.
    differences=[abs(mp.mpf(a['abs_epsilon_per_g'])/mp.mpf(b['abs_epsilon_per_g'])-1)
                 for a,b in zip(low['loop_table'],high['loop_table'])]
    assert max(differences)<mp.mpf('1e-12')
    script=Path(__file__).resolve()
    root=script.parents[2]
    paths=['Replies_to_Referee_3_referee_facing_2026-11-04.tex',
           'overleaf-source/axial-vector-model-building-v6/main-v6.tex']
    result={
        'scope':'Equal right-handed mixing, paired degenerate heavy thresholds, epsilon_ind(mu_match)=0; Br_inv includes the direct dimuon channel above threshold.',
        'inputs':{'e':'0.3028','m_e_GeV':'0.00051099895','m_mu_GeV':'0.105658','m_tau_GeV':'1.77686',
                  'theta_R':'0.01','matching_condition':'epsilon_ind(mu_match)=0',
                  'NA64_experiment':'NA64 electron beam, arXiv:2307.02404, Fig. 3, 90% CL',
                  'NA64_comparison_masses_GeV':['0.01','0.1','0.2','0.3'],
                  'NA64_digitization':'visual log-log read-off; conservative lower edge used; not official tabulated data'},
        'results':high,
        'verification':{'working_precision_decimal_digits':[35,55],
                        'max_relative_change_loop_magnitudes':mp.nstr(max(differences),8)},
        'runtime':{'python':platform.python_version(),'mpmath':mp.__version__},
        'sha256':{**{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths},
                  script.name:hashlib.sha256(script.read_bytes()).hexdigest()},
    }
    out=script.parent/'outputs'/'kinetic_dark_photon_2026-11-04.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
    print(json.dumps(result,ensure_ascii=True,indent=2))


if __name__=='__main__':
    main()
