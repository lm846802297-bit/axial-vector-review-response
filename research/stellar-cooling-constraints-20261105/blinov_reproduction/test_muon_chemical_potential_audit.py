import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from audit_muon_chemical_potential import (
    fermi_muon_thermodynamics,
    inverse_full_mu_from_net_density,
    audit,
    DEFAULT_PROFILE,
)


class MuonChemicalPotentialAuditTests(unittest.TestCase):
    def test_net_density_is_monotonic_in_full_chemical_potential(self):
        low = fermi_muon_thermodynamics(40.0, 30.0)["n_mu_net_fm3"]
        mid = fermi_muon_thermodynamics(80.0, 30.0)["n_mu_net_fm3"]
        high = fermi_muon_thermodynamics(120.0, 30.0)["n_mu_net_fm3"]
        self.assertLess(low, mid)
        self.assertLess(mid, high)

    def test_antimuons_are_suppressed_for_positive_muon_chemical_potential(self):
        result = fermi_muon_thermodynamics(100.0, 30.0)
        self.assertGreater(result["n_mu_minus_fm3"], result["n_mu_plus_fm3"])
        self.assertLess(result["antimuon_to_muon_ratio"], 0.02)

    def test_inverse_density_recovers_full_mu(self):
        mu = 102.84368885496772
        temperature = 33.92744041961383
        density = fermi_muon_thermodynamics(mu, temperature)["n_mu_net_fm3"]
        recovered = inverse_full_mu_from_net_density(density, temperature)
        self.assertAlmostEqual(recovered, mu, places=7)

    def test_caputo_mu_and_digitized_muon_density_are_consistent_at_10km(self):
        result = audit(DEFAULT_PROFILE, [10.0])
        row = result["samples"][0]
        self.assertLess(abs(row["caputo_fermi_density_relative_residual"]), 0.02)
        self.assertLess(abs(row["caputo_mu_inversion_residual_MeV"]), 0.5)

    def test_ferreira_and_caputo_profiles_are_not_a_constant_rest_mass_shift(self):
        result = audit(DEFAULT_PROFILE, [0.0, 5.0, 10.0, 15.0])
        offsets = [
            row["mu_ferreira_minus_mu_caputo_MeV"]
            for row in result["samples"]
        ]
        self.assertGreater(max(offsets)-min(offsets), 50.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
