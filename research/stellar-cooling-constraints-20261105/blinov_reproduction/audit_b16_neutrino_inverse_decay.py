"""Independent angular-integral audit of Blinov B.6, B.10 and B.4.

The B.6 two-body phase-space integral is reduced with its on-shell delta
function to the neutrino-pair opening-angle average. This is evaluated
directly by Gauss-Legendre quadrature, independently of the logarithmic
antiderivative used in reference.py.

B.19 is separately identified as the Compton detailed-balance relation; it
is not the neutrino inverse-decay detailed-balance equation (B.10).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import expit

try:
    from .reference import DEFAULT_PROFILE, fermi_pair_average, local_rates
except ImportError:
    from reference import DEFAULT_PROFILE, fermi_pair_average, local_rates

HERE=Path(__file__).resolve().parent
DEFAULT_OUTPUT=HERE/"outputs"/"b16_neutrino_inverse_decay_10mev_2026-11-08.json"
SAMPLE_RADII_KM=(8.0,10.0,12.0,15.0,17.0,18.0,22.0,23.0,24.0,25.0)
SAMPLE_ENERGIES_MEV=(10.25,10.5,12.0,15.0,20.0,30.0,50.0,100.0)


def sha256(path:Path)->str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def direct_pair_integrals(mu,omega,temperature,velocity,order=192):
    """Directly integrate fbar(E1;-mu) fnu(E2;mu) over cos(theta).

    E1,2 = omega/2 (1 +/- v cos(theta)); the Legendre weights are normalized
    to the angular average (1/2) integral_{-1}^{+1} d cos(theta).
    """
    mu,omega,temperature,velocity=np.broadcast_arrays(
        np.asarray(mu,float),np.asarray(omega,float),
        np.asarray(temperature,float),np.asarray(velocity,float)
    )
    cosine,weights=leggauss(order)
    weights=weights/2.0
    ebar=omega[...,None]*(1.0+velocity[...,None]*cosine)/2.0
    enu=omega[...,None]*(1.0-velocity[...,None]*cosine)/2.0
    fbar=expit(-(ebar+mu[...,None])/temperature[...,None])
    fnu=expit((mu[...,None]-enu)/temperature[...,None])
    i_prod=np.sum(weights*fbar*fnu,axis=-1)
    i_abs=np.sum(weights*(1.0-fbar)*(1.0-fnu),axis=-1)
    return i_prod,i_abs


def max_relative_error(a,b):
    a,b=np.asarray(a,float),np.asarray(b,float)
    return float(np.max(np.abs(a-b)/np.maximum(np.abs(b),1.0e-300)))


def run(profile_path=DEFAULT_PROFILE,mass=10.0,angle_order=192):
    data=np.genfromtxt(profile_path,delimiter=",",names=True)
    radius=np.asarray(SAMPLE_RADII_KM,float)
    temperature=np.interp(radius,data["r_km"],data["T_MeV"])
    mu_numu=np.interp(radius,data["r_km"],data["mu_numu_MeV"])
    mu_mu=np.interp(radius,data["r_km"],data["mu_mu_MeV"])
    energies=np.asarray(SAMPLE_ENERGIES_MEV,float)
    velocity=np.sqrt(np.maximum(1.0-(mass/energies)**2,0.0))

    mu_grid=mu_numu[:,None]
    omega_grid=energies[None,:]
    temp_grid=temperature[:,None]
    velocity_grid=velocity[None,:]
    x=omega_grid/temp_grid
    prefactor=mass**2/(8.0*np.pi*omega_grid)

    # One-flavor direct B.6 angular integrals: nu_mu has the profile chemical
    # potential; nu_tau is set to zero as in the published SN-profile treatment.
    i_mu_prod,i_mu_abs=direct_pair_integrals(
        mu_grid,omega_grid,temp_grid,velocity_grid,angle_order
    )
    i_tau_prod,i_tau_abs=direct_pair_integrals(
        np.zeros_like(mu_grid),omega_grid,temp_grid,velocity_grid,angle_order
    )
    i_mu_analytic=fermi_pair_average(
        mu_grid,omega_grid,temp_grid,velocity_grid
    )
    i_tau_analytic=fermi_pair_average(
        np.zeros_like(mu_grid),omega_grid,temp_grid,velocity_grid
    )

    gamma_prod_mu=prefactor*i_mu_prod
    gamma_prod_tau=prefactor*i_tau_prod
    gamma_abs_mu=prefactor*i_mu_abs
    gamma_abs_tau=prefactor*i_tau_abs
    gamma_prod=gamma_prod_mu+gamma_prod_tau
    gamma_abs=gamma_abs_mu+gamma_abs_tau

    # B.10 detailed balance, then B.4 reduced absorption.
    gamma_abs_from_b10=np.exp(np.minimum(x,700.0))*gamma_prod
    gamma_star_from_b4=(1.0-np.exp(-x))*gamma_abs
    gamma_star_from_prod=np.expm1(np.minimum(x,700.0))*gamma_prod

    # Compare with the production and reduced-absorption implementation used
    # by the existing independent reference module.
    code=local_rates(
        mass,omega_grid,temp_grid,mu_grid,
        np.interp(radius,data["r_km"],data["mu_mu_MeV"])[:,None]
    )
    code_gamma_nu=np.asarray(code["neutrino_production"],float)
    code_gamma_star_nu=np.expm1(np.minimum(x,700.0))*code_gamma_nu

    # B.19 belongs to Compton, not inverse neutrino decay. Check its detailed
    # balance/reduced-rate algebra separately using the Compton production
    # component. The independent QED B.18/B.15/B.16 audit is archived elsewhere.
    gamma_prod_compton=np.asarray(code["compton_production"],float)
    gamma_abs_compton=np.exp(np.minimum(x,700.0))*gamma_prod_compton
    gamma_star_compton_b4=(1.0-np.exp(-x))*gamma_abs_compton
    gamma_star_compton_b19=np.expm1(np.minimum(x,700.0))*gamma_prod_compton

    log_db_mu=np.log(np.maximum(i_mu_abs,1.0e-300))-np.log(np.maximum(i_mu_prod,1.0e-300))-x
    log_db_tau=np.log(np.maximum(i_tau_abs,1.0e-300))-np.log(np.maximum(i_tau_prod,1.0e-300))-x

    point_rows=[]
    for ir,r in enumerate(radius):
        for ie,omega in enumerate(energies):
            point_rows.append({
                "radius_km":float(r),
                "temperature_MeV":float(temperature[ir]),
                "mu_numu_MeV":float(mu_numu[ir]),
                "omega_MeV":float(omega),
                "vector_speed":float(velocity[ie]),
                "I_nu_mu_direct":float(i_mu_prod[ir,ie]),
                "I_nu_mu_analytic":float(i_mu_analytic[ir,ie]),
                "I_nu_tau_direct":float(i_tau_prod[ir,ie]),
                "Gamma_prod_total_per_g2_MeV":float(gamma_prod[ir,ie]),
                "Gamma_abs_total_per_g2_MeV":float(gamma_abs[ir,ie]),
                "Gamma_star_total_per_g2_MeV":float(gamma_star_from_b4[ir,ie]),
                "Gamma_prod_code_per_g2_MeV":float(code_gamma_nu[ir,ie]),
                "Gamma_star_code_per_g2_MeV":float(code_gamma_star_nu[ir,ie]),
            })

    # Explicit outer-shell subset.
    outer_rows=[row for row in point_rows if row["radius_km"]>=22.0]
    return {
        "title":"Independent B.6/B.10/B.4 neutrino inverse-decay audit",
        "mass_MeV":mass,
        "profile":{"path":str(profile_path),"sha256":sha256(profile_path)},
        "configuration":{
            "angular_legendre_order":angle_order,
            "sample_radii_km":list(SAMPLE_RADII_KM),
            "sample_energies_MeV":list(SAMPLE_ENERGIES_MEV),
            "mu_nu_tau_assumption":"zero, following the published Blinov Appendix-B discussion of the unavailable tau-neutrino chemical-potential profile",
        },
        "equation_mapping":{
            "B6":"Direct two-body phase-space integral reduced to an angular average of fbar(E1;-mu_nu) fnu(E2;mu_nu).",
            "B10":"Neutrino inverse-decay detailed balance: Gamma_prod = exp(-omega/T) Gamma_abs.",
            "B4":"Reduced absorption: Gamma_star = (1-exp(-omega/T)) Gamma_abs = expm1(omega/T) Gamma_prod.",
            "B19":"Compton detailed balance only; it is not the neutrino inverse-decay detailed-balance equation.",
            "normalization":"Using Gamma(V->nubar nu)=alpha_V mV/6 and alpha_V=g^2/(4 pi), B7 gives Gamma_prod/g^2 = mV^2 I/(8 pi omega) per neutrino flavor.",
        },
        "validation":{
            "max_relative_error_direct_vs_analytic_I_nu_mu":max_relative_error(i_mu_prod,i_mu_analytic),
            "max_relative_error_direct_vs_analytic_I_nu_tau":max_relative_error(i_tau_prod,i_tau_analytic),
            "max_relative_error_direct_B6_total_vs_reference_Gamma_prod":max_relative_error(gamma_prod,code_gamma_nu),
            "max_abs_log_detailed_balance_residual_nu_mu":float(np.max(np.abs(log_db_mu))),
            "max_abs_log_detailed_balance_residual_nu_tau":float(np.max(np.abs(log_db_tau))),
            "max_relative_error_B10_absorption_vs_direct_inverse_integral":max_relative_error(gamma_abs_from_b10,gamma_abs),
            "max_relative_error_B4_two_equivalent_forms":max_relative_error(gamma_star_from_b4,gamma_star_from_prod),
            "max_relative_error_B4_reduced_neutrino_rate_vs_reference_code":max_relative_error(gamma_star_from_b4,code_gamma_star_nu),
            "max_relative_error_B19_compton_B4_identity":max_relative_error(gamma_star_compton_b4,gamma_star_compton_b19),
            "max_relative_error_B19_absorption_ratio":max_relative_error(
                gamma_abs_compton,
                np.exp(np.minimum(x,700.0))*gamma_prod_compton
            ),
        },
        "outer_shell_summary":{
            "radius_range_km":[22.0,25.0],
            "mu_numu_max_abs_MeV":float(np.max(np.abs(mu_numu[radius>=22.0]))),
            "temperature_range_MeV":[float(np.min(temperature[radius>=22.0])),float(np.max(temperature[radius>=22.0]))],
            "max_abs_log_detailed_balance_residual":float(max(
                np.max(np.abs(log_db_mu[radius>=22.0])),
                np.max(np.abs(log_db_tau[radius>=22.0]))
            )),
            "max_relative_error_B6_total_vs_code":max_relative_error(
                gamma_prod[radius>=22.0],code_gamma_nu[radius>=22.0]
            ),
            "points":outer_rows,
        },
        "pointwise_results":point_rows,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    p.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    p.add_argument("--mass",type=float,default=10.0)
    p.add_argument("--angle-order",type=int,default=192)
    a=p.parse_args()
    result=run(a.profile,a.mass,a.angle_order)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"equation_mapping":result["equation_mapping"],"validation":result["validation"],"outer_shell_summary":{k:v for k,v in result["outer_shell_summary"].items() if k!="points"}},indent=2))
    print(f"Saved {a.output}")


if __name__=="__main__":
    main()
