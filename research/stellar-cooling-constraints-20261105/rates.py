"""Mode-resolved unit-coupling rates for a fixed-profile SN benchmark.

Units: all masses/energies/temperatures in MeV, densities in MeV^3,
cross sections in MeV^-2, rates in MeV. Multiply every returned rate or
cross section by gX^2. Modes are (longitudinal, circular +, circular -).

The inverse-Compton kernel keeps exact vacuum two-body recoil with the
initial muon at rest in the medium frame. Multiplication by n_mu_eff and
thermal detailed balance is a specified nonrelativistic-muon approximation,
NOT an exact moving-muon thermal integral. Photons have vacuum dispersion.
The neutrino and dimuon 1<->2 rates retain exact Fermi blocking and kinematics.

Sources: Liu--Miller arXiv:1705.01633 Eq20/34 (summed-kernel validation);
Blinov et al. arXiv:2511.09619v2 Appendix B (balance and neutrino normalization).
"""
from functools import lru_cache
import numpy as np

M_MU = 105.6583755
ALPHA = 1/137.035999084
E2 = 4*np.pi*ALPHA
MODES = ("L", "+", "-")
_I2 = np.eye(2, dtype=complex)
_Z2 = np.zeros((2, 2), dtype=complex)
_SIGMA = (np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1]))
_GAMMA = np.array([np.block([[_I2, _Z2], [_Z2, -_I2]])] +
                  [np.block([[_Z2, s], [-s, _Z2]]) for s in _SIGMA])
_G5 = 1j*_GAMMA[0]@_GAMMA[1]@_GAMMA[2]@_GAMMA[3]
_I4 = np.eye(4)
_METRIC = np.array([1, -1, -1, -1])


@lru_cache(maxsize=16)
def quadrature(order):
    if order < 4:
        raise ValueError("At least four angular nodes are required")
    return np.polynomial.legendre.leggauss(order)


def _slash(v):
    return np.einsum("...a,aij->...ij", np.asarray(v)*_METRIC, _GAMMA)


def _dagger(a):
    return a.conj().swapaxes(-2, -1)


def _fermion(x):
    """Fermi occupation at dimensionless x=(E-mu)/T, overflow safe."""
    return np.exp(-np.logaddexp(0., x))


def _decay_inputs(mass, energy, temperature, chemical):
    energy, temperature, chemical = np.broadcast_arrays(
        np.asarray(energy, float), np.asarray(temperature, float), np.asarray(chemical, float))
    if mass <= 0 or np.any(energy < mass) or np.any(temperature <= 0):
        raise ValueError("Require M>0, E>=M, T>0")
    return energy, temperature, chemical


def compton_matrix_elements(mass, energies, cosines, current="axial", photon_ward=False):
    """Return eg[nE,nc], |M_h|^2[nE,nc,3], with only initial mu spin averaged.

    Unit mediator coupling, e^2 included. Initial A' travels along +z in
    the medium/muon-rest frame. The trace is the time-reversed production
    amplitude; physical photon polarizations are constructed in its plane.
    photon_ward=True replaces both photon polarizations by its momentum.
    """
    energies = np.atleast_1d(np.asarray(energies, float))
    cosines = np.atleast_1d(np.asarray(cosines, float))
    if mass <= 0 or np.any(energies < mass) or np.any(abs(cosines) > 1):
        raise ValueError("Require M>0, E>=M, |cos(theta)|<=1")
    if current not in ("axial", "vector"):
        raise ValueError("current must be axial or vector")
    ee, cc = np.broadcast_arrays(energies[:, None], cosines[None, :])
    kk = np.sqrt(np.maximum((ee-mass)*(ee+mass), 0.))
    ss = np.sqrt(np.maximum(1-cc*cc, 0.))
    denominator = M_MU + ee - kk*cc
    eg = (mass*mass+2*M_MU*ee)/(2*denominator)
    zeros = np.zeros_like(ee)
    p = np.stack([np.full_like(ee, M_MU), zeros, zeros, zeros], axis=-1)
    q = np.stack([ee, zeros, zeros, kk], axis=-1)
    photon = np.stack([eg, eg*ss, zeros, eg*cc], axis=-1)
    pp = p+q-photon
    # Stable propagator denominators; these identities avoid mass subtraction.
    prop_s = (_slash(p+q)+M_MU*_I4)/(mass*mass+2*M_MU*ee)[..., None, None]
    prop_u = (_slash(p-photon)+M_MU*_I4)/(-2*M_MU*eg)[..., None, None]
    spin_out, spin_in = _slash(p)+M_MU*_I4, _slash(pp)+M_MU*_I4
    if current == "vector":
        # Ward identity permits eps_L -> eps_L-q/M and prevents catastrophic
        # cancellation for M/E << 1 in the conserved vector-current case.
        small = mass/(ee+kk)
        eps_l = np.stack([-small, zeros, zeros, small], axis=-1)
    else:
        eps_l = np.stack([kk/mass, zeros, zeros, ee/mass], axis=-1)
    eps_mediator = (eps_l, np.array([0, 1, 1j, 0])/np.sqrt(2),
                    np.array([0, 1, -1j, 0])/np.sqrt(2))
    eps_gamma = (np.stack([zeros, cc, zeros, -ss], axis=-1), np.array([0, 0, 1, 0]))
    if photon_ward:
        eps_gamma = (photon,)
    answer = []
    for eps in eps_mediator:
        vx = _slash(eps)
        if current == "axial":
            vx = vx@(-_G5)
        total = np.zeros_like(ee)
        for photon_polarization in eps_gamma:
            vg = _slash(photon_polarization)
            amplitude = vx@prop_s@vg + vg@prop_u@vx
            conjugate = _GAMMA[0]@_dagger(amplitude)@_GAMMA[0]
            trace = np.trace(spin_out@amplitude@spin_in@conjugate, axis1=-2, axis2=-1)
            total += trace.real/2
        answer.append(total*E2)
    return eg, np.stack(answer, axis=-1)


def compton_kernels(mass, energies, order=32, current="axial"):
    """Return (eg, dOmega-weighted v*sigma) at unit coupling.

    eg shape (nE,nangle); weighted cross section shape (nE,nangle,3).
    Sum axis 1 for the vacuum v*sigma per incident mode. These weights
    already contain the complete azimuthal and Gauss-Legendre integration.
    """
    cosines, weights = quadrature(order)
    eg, msq = compton_matrix_elements(mass, energies, cosines, current)
    ee = np.atleast_1d(np.asarray(energies, float))[:, None]
    kk = np.sqrt(np.maximum((ee-mass)*(ee+mass), 0.))
    denominator = M_MU + ee - kk*cosines
    factor = eg/(64*np.pi**2*M_MU*ee*denominator)*(2*np.pi*weights)
    return eg, factor[..., None]*msq


def compton_absorption(kernels, temperature, n_mu_eff):
    """Gamma_abs = n_mu_eff integral v*dSigma*(1+f_gamma).

    Scalar inputs return (nE,3); radial vectors return (nr,nE,3).
    Use gamma_prod=exp(-E/T)*gamma_abs and gamma_red=abs-prod, with E
    the *mediator* energy. This prescription enforces thermal balance at
    the retained muon-rest/effective-density approximation.
    """
    eg, weights = kernels
    temperature, density = np.broadcast_arrays(np.asarray(temperature, float), np.asarray(n_mu_eff, float))
    if np.any(temperature <= 0) or np.any(density < 0):
        raise ValueError("Require T>0 and nonnegative density")
    stimulated = 1/(-np.expm1(-eg/temperature[..., None, None]))
    return density[..., None, None]*np.sum(stimulated[..., None]*weights, axis=-2)


def neutrino_rates(mass, energy, temperature, mu_numu, order=48):
    """Return (Gamma_prod,Gamma_abs) for nu_mu and nu_tau at unit gX.

    Inputs broadcast normally; output shape is broadcast_shape+(3,).
    nu_mu chemical potential is supplied, nu_tau chemical potential is 0.
    Includes Pauli blocking, all boosts and no spin average between modes.
    """
    energy, temperature, chemical = _decay_inputs(mass, energy, temperature, mu_numu)
    z, weights = quadrature(order)
    polarization_weights = np.stack([3*(1-z*z)/4, 3*(1+z)**2/8, 3*(1-z)**2/8], axis=-1)
    k = np.sqrt(np.maximum((energy-mass)*(energy+mass), 0.))
    e1 = (energy[..., None]+k[..., None]*z)/2
    e2 = (energy[..., None]-k[..., None]*z)/2
    prod = np.zeros(energy.shape+(3,))
    absorp = np.zeros_like(prod)
    for mu in [chemical, np.zeros_like(chemical)]:
        x1, x2 = (e1-mu[..., None])/temperature[..., None], (e2+mu[..., None])/temperature[..., None]
        prod += np.einsum("...z,zh->...h", _fermion(x1)*_fermion(x2), weights[:, None]*polarization_weights)
        absorp += np.einsum("...z,zh->...h", _fermion(-x1)*_fermion(-x2), weights[:, None]*polarization_weights)
    prefactor = mass*mass/(energy*24*np.pi)
    return prefactor[..., None]*prod, prefactor[..., None]*absorp


def charged_muon_decay_rates(mass, energy, temperature, mu_mu, current="axial", order=48):
    """Mode-resolved mu+mu- inverse decay / decay, exact free-fermion kinematics.

    Axial vacuum width per mediator polarization is M*beta^3/(12*pi).
    The angular tensor is delta_ij-n_i*n_j, giving the normalized L/T
    weights below. Vector tensor delta_ij-beta^2*n_i*n_j yields the vector
    comparison weights and M*beta*(1+2*m_mu^2/M^2)/(12*pi) width.
    """
    energy, temperature, chemical = _decay_inputs(mass, energy, temperature, mu_mu)
    if current not in ("axial", "vector"):
        raise ValueError("current must be axial or vector")
    if mass <= 2*M_MU:
        zero = np.zeros(energy.shape+(3,))
        return zero, zero.copy()
    z, weights = quadrature(order)
    beta = np.sqrt(1-4*M_MU*M_MU/(mass*mass))
    if current == "axial":
        wl, wt = 3*(1-z*z)/4, 3*(1+z*z)/8
        width = mass*beta**3/(12*np.pi)
    else:
        norm = 2*(1-beta*beta/3)
        wl = (1-beta*beta*z*z)/norm
        wt = (1-beta*beta*(1-z*z)/2)/norm
        width = mass*beta*(1+2*M_MU*M_MU/(mass*mass))/(12*np.pi)
    angular = weights[:, None]*np.stack([wl, wt, wt], axis=-1)
    k = np.sqrt(np.maximum((energy-mass)*(energy+mass), 0.))
    e1, e2 = (energy[..., None]+k[..., None]*beta*z)/2, (energy[..., None]-k[..., None]*beta*z)/2
    x1, x2 = (e1-chemical[..., None])/temperature[..., None], (e2+chemical[..., None])/temperature[..., None]
    prod = np.einsum("...z,zh->...h", _fermion(x1)*_fermion(x2), angular)
    absorp = np.einsum("...z,zh->...h", _fermion(-x1)*_fermion(-x2), angular)
    return (mass/energy*width)[..., None]*prod, (mass/energy*width)[..., None]*absorp
