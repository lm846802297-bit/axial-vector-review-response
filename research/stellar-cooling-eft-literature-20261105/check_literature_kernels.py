"""Compare Liu--Miller (1705.01633), Eq. (20), to explicit spinor amplitudes.

The reference module is the existing PR #53 matrix element, pinned in metadata.
No stellar profile, transport calculation, or exclusion contour is computed.
Usage: python check_literature_kernels.py --matrix-script PATH --output PATH
"""

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path

REFERENCE_COMMIT = "e94fd051365eec508ac85bfd223c7531c0c64230"
REFERENCE_PATH = (
    "research/stellar-cooling-original-uv-model-20261105/"
    "stellar_semi_compton_axial_matrix_element.py"
)


def published_kernels(s_hat, u_hat, t, fermion_mass, vector_mass):
    """Mostly-minus metric; S=s-mf^2, U=u-mf^2, t=(p'-p)^2.

    These are dimensionless A^(2->2) kernels. Multiply by e^2*g^2.
    Initial fermion and photon are unpolarized; all final modes are summed.
    """
    ratio = (s_hat + u_hat) ** 2 / (s_hat * u_hat)
    bracket = fermion_mass**2 * ((s_hat + u_hat) / (s_hat * u_hat)) ** 2
    bracket -= t / (s_hat * u_hat)
    a_p = -ratio + 2 * vector_mass**2 * bracket
    a_v = 4 - 2 * ratio + 4 * (vector_mass**2 + 2 * fermion_mass**2) * bracket
    a_a = 4 - (2 + 4 * fermion_mass**2 / vector_mass**2) * ratio
    a_a += 4 * (vector_mass**2 - 4 * fermion_mass**2) * bracket
    return a_p, a_v, a_a


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matrix-script", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("reference_matrix", args.matrix_script)
    reference = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reference)
    mf = reference.M_MU_MEV
    dot = reference.minkowski_dot
    points = [
        (30.0, 1.0, -0.8), (30.0, 1.0, 0.0), (30.0, 1.0, 0.8),
        (30.0, 10.0, 0.0), (100.0, 50.0, 0.0),
        (1.0, 0.001, 0.0), (10.0, 0.1, 0.5),
    ]
    rows = []
    max_relative = 0.0
    for energy, mass, cosine in points:
        p, k, pp, q = reference.cm_kinematics(energy, mass, cosine)
        s_hat = dot(p + k, p + k) - mf**2
        u_hat = dot(p - q, p - q) - mf**2
        t = dot(pp - p, pp - p)
        ap, av, aa = published_kernels(s_hat, u_hat, t, mf, mass)
        checks = []
        for label, gv, ga in [("vector", 1.0, 0.0), ("axial", 0.0, 1.0),
                              ("mixed", 0.25, 0.75), ("mixed_sign", 0.25, -0.75)]:
            direct = reference.polarization_resolved_matrix_element_squared(
                p, k, pp, q, mass, gv, ga, "all"
            )
            formula = gv**2 * av + ga**2 * aa
            relative = abs(direct - formula) / max(abs(direct), abs(formula), 1e-100)
            max_relative = max(max_relative, relative)
            checks.append(dict(case=label, spinor=direct, literature=formula,
                               relative_error=relative))
        rows.append(dict(photon_energy_muon_rest_MeV=energy, mediator_mass_MeV=mass,
                         cos_theta_cm=cosine, invariant_sum_residual_MeV2=s_hat+u_hat+t-mass**2,
                         axial_to_vector_ratio=aa/av,
                         axial_to_goldstone_ratio=aa/(4*mf**2/mass**2*ap), checks=checks))
    # Bollig et al. corrected v7: derivative coupling, no 1/2 convention.
    derivative_bound_GeV_inverse = 10**(-7.5)
    mass_mu_GeV = mf / 1000
    bound_samples = []
    for mass_GeV in (1e-6, 1e-5, 1e-4, 1e-3):
        ga = derivative_bound_GeV_inverse * mass_GeV
        energy_GeV = 0.03
        momentum_GeV = math.sqrt(energy_GeV**2-mass_GeV**2)
        # Two active flavors, each Gamma = gX^2*M/(24*pi); gX=abs(gA).
        decay_length_km = 1.973269804e-19 * 12*math.pi*momentum_GeV/(ga**2*mass_GeV**2)
        bound_samples.append(dict(mass_MeV=1000*mass_GeV, axial_coupling_reference=ga,
                                  vacuum_neutrino_decay_length_km=decay_length_km))
    output = dict(
        purpose="Independent published 2-to-2 kernel comparison; not a SN exclusion calculation",
        literature="https://arxiv.org/html/1705.01633v1#S2.SS2",
        reference_commit=REFERENCE_COMMIT, reference_path=REFERENCE_PATH,
        reference_sha256=hashlib.sha256(args.matrix_script.read_bytes()).hexdigest(),
        muon_mass_MeV=mf, comparison_count=sum(len(row["checks"]) for row in rows),
        maximum_relative_error=max_relative, comparison_passed=max_relative < 1e-8,
        points=rows,
        corrected_bollig_mapping=dict(
            source="https://arxiv.org/html/2005.07141v7",
            conditions="Relativistic longitudinal mode, low mass (safely below 1 MeV), free streaming; tree-level muon channels",
            derivative_bound_GeV_inverse=derivative_bound_GeV_inverse,
            equivalent_yukawa_reference=2*mass_mu_GeV*derivative_bound_GeV_inverse,
            change_from_obsolete_10_minus_8p1=10**0.6,
            neutrino_width="gX^2*M/(12*pi)", energy_GeV=0.03,
            samples=bound_samples,
        ),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({key: output[key] for key in
                      ("comparison_count", "maximum_relative_error", "comparison_passed", "reference_sha256")}, indent=2))
    print("Saved", args.output)
    if not output["comparison_passed"]:
        raise SystemExit("Published kernel and explicit amplitude disagree")


if __name__ == "__main__":
    main()
