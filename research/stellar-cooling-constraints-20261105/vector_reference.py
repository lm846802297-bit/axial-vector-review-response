"""Independent spin-summed vector rates from Blinov et al. (2511.09619v2).

This module is an audit/reference, not a replacement for rates.py. In particular,
the literal summed-opacity prescription is retained only to reproduce Fig. 4;
a rate summed over initial vector polarizations is not a per-particle opacity.
All rates are at unit g_X, in MeV. Source: Appendix B, Eqs. B.7--B.19.
"""
import numpy as np
from scipy.special import expit
from scipy.integrate import quad

M_MU = 105.6583755
ALPHA = 1/137.035999084


def fermi_pair_average(chemical, energy, temperature, velocity):
    """B.9, evaluated via the equivalent antiderivative of Fermi functions.

    I = <f(E1-mu) f(E2+mu)> with a uniform rest-frame polar angle.
    f1*f2 = (1-f1-f2)/(exp(E/T)-1) avoids exponentially large numbers.
    This does not call the angular quadrature used by rates.py.
    """
    mu, e, t, v = np.broadcast_arrays(chemical, energy, temperature, velocity)
    half_range = e*v/2
    emin, emax = e/2-half_range, e/2+half_range
    width = 2*half_range
    safe_width = np.where(width > 0, width, 1.)
    mean_f = np.zeros_like(e, dtype=float)
    for sign in [1, -1]:
        mean_f += t/safe_width*(np.logaddexp(0., (sign*mu-emin)/t)
                               - np.logaddexp(0., (sign*mu-emax)/t))
    inverse_bose = np.exp(-e/t)/(-np.expm1(-e/t))
    out = (1-mean_f)*inverse_bose
    # The antiderivative loses precision both at v=0 and when E/T is tiny:
    # then <f1+f2> approaches 1 and 1-mean_f suffers catastrophic cancellation.
    # At E/T < 1e-3 the exact angular average differs from the rest-limit value
    # only at O((E/T)^2), below 1e-7 relative; use that controlled limit.
    at_rest = expit((mu-e/2)/t)*expit((-mu-e/2)/t)
    out = np.where((v < 1e-7) | (e/t < 1e-3), at_rest, out)
    if np.any(out < -1e-13):
        raise FloatingPointError("Negative Fermi-pair integral")
    return np.maximum(out, 0.)


def summed_decay_production(mass, energy, temperature, mu_numu, mu_mu):
    """B.7 and B.11: sum all 3 final V polarizations, both active flavors."""
    e,t,nu,mu = np.broadcast_arrays(energy, temperature, mu_numu, mu_mu)
    velocity = np.sqrt(np.maximum(1-(mass/e)**2, 0.))
    neutrino = mass**2/(8*np.pi*e)*sum(
        fermi_pair_average(c,e,t,velocity) for c in [nu,np.zeros_like(nu)])
    dimuon = np.zeros_like(neutrino)
    if mass > 2*M_MU:
        beta = np.sqrt(1-4*M_MU**2/mass**2)
        width = mass/(12*np.pi)*beta*(1+2*M_MU**2/mass**2)
        dimuon = 3*mass/e*width*fermi_pair_average(mu,e,t,velocity*beta)
    return neutrino,dimuon


def thomson_absorption_modes(mass, energy, temperature, density):
    """B.14--B.18 decomposed into physical (L,+,-) modes, no recoil.

    v*sigma_abs,h = 2 alpha/(3 m_mu^2) * (M^2/E^2,1,1).
    The sum of the resulting production rates is 2*n_eff*sigma_prod/v*f_B.
    """
    e=np.asarray(energy)
    t=np.asarray(temperature)
    n=np.asarray(density)
    modes=np.stack([(mass/e)**2,np.ones_like(e),np.ones_like(e)],axis=-1)
    return (2*ALPHA/(3*M_MU**2)*n[...,None,None]
            /(-np.expm1(-e/t[...,None]))[...,None]*modes)


def number_density(temperature, chemical):
    """Independent adaptive quadrature for negative muons, in fm^-3."""
    return quad(lambda p:p*p*expit((chemical-np.hypot(p,M_MU))/temperature),
                0,np.inf,epsabs=1e-7,epsrel=1e-10)[0]/np.pi**2/197.3269804**3


def uniform_sphere_escape(tau):
    """Volume/direction average exp(-kappa*s), tau=kappa*R."""
    tau=np.asarray(tau,dtype=float)
    return 3/(4*tau)*(1-1/(2*tau*tau)
                      +(1/tau+1/(2*tau*tau))*np.exp(-2*tau))
