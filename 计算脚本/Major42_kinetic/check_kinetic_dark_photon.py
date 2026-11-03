"""Finite-momentum photon mixing and the NA64 electron-channel comparison.

Python + mpmath. The experimental reference is an illustrative 1e-4 scale
at 100 MeV, not a digitized mass-dependent exclusion curve.
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

    masses = list(map(mp.mpf, ['0','0.01','0.1','0.2','0.212','0.5','1','3','10','100']))
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
    mass=mp.mpf('0.1')
    ep=abs(epsilon_per_g(mass))
    me=mp.mpf('0.00051099895')
    re=(me/mass)**2
    visible_ratio=(e*ep)**2*(1+2*re)*mp.sqrt(1-4*re)
    br=1/(1+visible_ratio)
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
    return {'loop_table':rows,'comparison_at_100MeV':comparison,
            'Gamma_ee_over_Gamma_nunu_100MeV':mp.nstr(visible_ratio,18),
            'Br_inv_100MeV':mp.nstr(br,18),
            'four_state_sum_check':{
                'physical_heavy_masses_GeV':['20000','20000'],
                'right_handed_angles':['0.01','0.01'],
                'renormalization_scales_GeV':['1','1000'],
                'sum_vector_couplings_over_g':mp.nstr(sum(weights),8),
                'max_relative_difference_from_light_pair':mp.nstr(max(scale_checks),8),
                'scope':'Checks threshold cancellation and scale independence; not a full UV fit.'},
            'NA64_kinematic_check':{
                'secondary_positron_resonance_Aprime_energy_GeV':mp.nstr(resonance_energy,18),
                'missing_energy_selection_GeV':'approximately 50',
                'Gamma_total_over_mass_at_g0p1':mp.nstr(mp.mpf('0.1')**2/(12*mp.pi)*(1+visible_ratio),18)},
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
        'scope':'Equal right-handed mixing, paired degenerate heavy thresholds, zero independent matching coefficient; closed new channels.',
        'inputs':{'e':'0.3028','m_mu_GeV':'0.105658','m_tau_GeV':'1.77686',
                  'theta_R':'0.01','experimental_reference_epsilon':'1e-4',
                  'experimental_reference_mass_GeV':'0.1',
                  'reference_type':'order-of-magnitude comparison only; not a digitized limit',
                  'experiment':'NA64 electron beam, arXiv:2307.02404, Fig. 3'},
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
