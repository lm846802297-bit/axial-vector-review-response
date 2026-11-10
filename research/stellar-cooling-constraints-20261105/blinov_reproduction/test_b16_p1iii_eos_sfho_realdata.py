"""Closure tests against the official SFHo/FRDM v1.03 single-particle tables.

P1-IIIe-B.  These tests consume the committed audit fixture
``outputs/p1iii_eos_sfho_realdata_fixture.csv``, which was produced from the
Hempel (2015) tables released by the University of Basel:

  sfho_frdm_eos_v1.03.bin        extended thermodynamic table (18 columns)
  sfho_frdm_spp_v1.03.tab        single-particle properties (7 columns)
  sfho_frdm_comp_v1.03.bin       nuclear composition (8 layers)

The fixture keeps the *real* tabulated values (m*_N, Sigma_V,N^tot, mu_N^nonrel,
xi, X_n, X_p, p_tot) for 224 (T, Yp, nB) cells, so the Fermi-integral closure
xi * 2/(2*pi)^3 Int d^3p f_N = X_N n_B can be re-checked on any machine without
the 400 MB binary tables.  The whole-table tests run only when
``SFHO_TABLES_DIR`` points at an extracted copy of the archives.

Validity domain (established by ``audit_b16_p1iii_eos_sfho_realdata_closure.py``
and documented in ``B16_P1IIIE_B_SFHO_REALDATA_CLOSURE_2026-11-11.md``):

  T <= 25.2 MeV   OR   nB >= 9.9e-5 fm^-3

Inside that domain the closure residual stays below 1e-3 for both species
(audited maxima: 6.13e-4 neutron, 8.86e-5 proton for X_p >= 1e-6).
Outside it, at T = 63.096 MeV with nB <= 1e-4 fm^-3 (16 of 224 cells), the
tabulated single-particle state saturates: mu*_N/T sticks at -14.891 and the
reconstructed free-nucleon density freezes at 9.19e-8 fm^-3, so the residual
grows like 1/(X_N n_B) up to ~1.4e5.  That corner is a resolution limit of the
table, not a convention error, and it is asserted below instead of being skipped
silently.
"""

from __future__ import annotations

import csv
import os
import tempfile
import unittest
from pathlib import Path

from audit_b16_p1iii_eos_nucleon_distribution import (
    aggregate_profile_rows,
    load_profile_csv,
)

HERE = Path(__file__).resolve().parent
FIXTURE_PATH = HERE / "outputs" / "p1iii_eos_sfho_realdata_fixture.csv"

#: Validity domain of the tabulated closure (see the module docstring).
DOMAIN_MAX_T_MEV = 25.2
DOMAIN_MIN_NB_FM3 = 9.9e-5
#: The audited maximum residual inside the domain is 6.13e-4 (neutron), 5.40e-4
#: (proton); 1e-3 leaves a margin without hiding a regression.
CLOSURE_TOLERANCE = 1e-3
XI_IDENTITY_TOLERANCE = 1e-6
#: Where the table has no resolution anymore.
FLOOR_T_MEV = 63.096
FLOOR_MAX_K_INDEX = 50
FLOOR_FREEZE_TOLERANCE = 1e-3
FLOOR_MINIMUM_RATIO = 1e2
#: Below this proton fraction the proton ratio is a ratio of denormals.
PROTON_FRACTION_FLOOR = 1e-6

TABLE_SHAPES = {
    "extended_eos": (81, 61, 326, 18),
    "single_particle": (81, 60, 326, 7),
    "composition": (81, 61, 326, 8),
}


def _read_fixture() -> list[dict[str, str]]:
    with FIXTURE_PATH.open("r", newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def _float(row: dict[str, str], key: str) -> float:
    return float(row[key])


def _in_validity_domain(row: dict[str, str]) -> bool:
    return (
        _float(row, "T_MeV") <= DOMAIN_MAX_T_MEV
        or _float(row, "nB_fm3") >= DOMAIN_MIN_NB_FM3
    )


class TestRealDataClosureFixture(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not FIXTURE_PATH.exists():
            raise unittest.SkipTest(f"fixture not found: {FIXTURE_PATH}")
        cls.rows = _read_fixture()

    def test_fixture_covers_the_audited_grid(self) -> None:
        self.assertEqual(len(self.rows), 224)
        temperatures = {round(_float(row, "T_MeV"), 6) for row in self.rows}
        proton_fractions = {round(_float(row, "Yp_tot"), 6) for row in self.rows}
        densities = {_float(row, "nB_fm3") for row in self.rows}
        self.assertEqual(len(temperatures), 8)
        self.assertEqual(len(proton_fractions), 4)
        self.assertEqual(len(densities), 7)
        self.assertEqual(
            {round(t, 3) for t in temperatures},
            {0.100, 0.251, 0.631, 1.585, 3.981, 10.000, 25.119, 63.096},
        )

    def test_floor_cells_are_pure_nucleon_matter(self) -> None:
        # The corner that fails is not cluster-dominated matter: the neutron
        # fraction is exactly 0.8 and X_n + X_p = 1 there.
        floor = [
            row
            for row in self.rows
            if abs(_float(row, "T_MeV") - FLOOR_T_MEV) < 1e-2
            and int(_float(row, "k_index")) <= FLOOR_MAX_K_INDEX
        ]
        self.assertEqual(len(floor), 8)
        for row in floor:
            self.assertGreater(_float(row, "X_n") + _float(row, "X_p"), 0.99)

    def test_xi_equals_the_excluded_volume_identity(self) -> None:
        # xi = 1 - (nB - X_n nB - X_p nB)/n0, i.e. the SPP filling factor is the
        # excluded-volume closure itself.  It is still taken from the table (the
        # author's rule), but this identity is what makes the closure test sharp.
        # Twelve cells originally rounded to xi = 1 + 4e-16; the kernel now
        # clamps that printing artifact, so all 224 cells answer.
        residuals = []
        unanswered = 0
        for row in self.rows:
            if row["xi_from_composition"].strip() == "":
                unanswered += 1
                continue
            residuals.append(
                abs(_float(row, "xi") - _float(row, "xi_from_composition"))
            )
        self.assertEqual(unanswered, 0)
        self.assertEqual(len(residuals), 224)
        self.assertLess(max(residuals), XI_IDENTITY_TOLERANCE)
        self.assertLess(sorted(residuals)[len(residuals) // 2], 1e-8)

    def test_closure_holds_inside_the_validity_domain(self) -> None:
        inside = [row for row in self.rows if _in_validity_domain(row)]
        outside = [row for row in self.rows if not _in_validity_domain(row)]
        self.assertEqual(len(inside), 208)
        self.assertEqual(len(outside), 16)
        self.assertEqual(
            {round(_float(row, "T_MeV"), 3) for row in outside}, {63.096}
        )
        self.assertEqual(
            {int(_float(row, "k_index")) for row in outside}, {1, 50, 100, 150}
        )

        neutron = [abs(_float(row, "ratio_n") - 1.0) for row in inside]
        proton = [
            abs(_float(row, "ratio_p") - 1.0)
            for row in inside
            if _float(row, "X_p") >= PROTON_FRACTION_FLOOR
        ]
        self.assertLess(max(neutron), CLOSURE_TOLERANCE)
        self.assertLess(sorted(neutron)[len(neutron) // 2], 1e-5)
        self.assertLess(max(proton), CLOSURE_TOLERANCE)
        self.assertEqual(len(proton), 145)

    def test_outside_the_domain_the_free_density_freezes(self) -> None:
        # At T = 63.096 MeV and nB <= 1e-10 fm^-3 the reconstructed free-nucleon
        # density is constant to 5e-4 while the target density drops by 10x;
        # the closure residual therefore diverges like 1/(X_n n_B).
        floor = [
            row
            for row in self.rows
            if abs(_float(row, "T_MeV") - FLOOR_T_MEV) < 1e-2
            and int(_float(row, "k_index")) <= FLOOR_MAX_K_INDEX
        ]
        self.assertEqual(len(floor), 8)
        densities = [_float(row, "nprime_n_fm3") for row in floor]
        spread = (max(densities) - min(densities)) / min(densities)
        self.assertLess(spread, FLOOR_FREEZE_TOLERANCE)
        for row in floor:
            self.assertGreater(
                abs(_float(row, "ratio_n") - 1.0), FLOOR_MINIMUM_RATIO
            )

    def test_degeneracy_factor_stays_in_the_unit_interval(self) -> None:
        for key in ("Fdeg_n", "Fdeg_p"):
            values = [_float(row, key) for row in self.rows]
            self.assertGreater(min(values), 0.0)
            self.assertLessEqual(max(values), 1.0)
        # The static degeneracy suppression must actually be exercised.
        self.assertGreater(len(self.rows), 0)
        self.assertLess(min(_float(row, "Fdeg_n") for row in self.rows), 1e-3)
        self.assertLess(min(_float(row, "Fdeg_p") for row in self.rows), 1e-3)

    def test_kernel_reproduces_the_closure_from_the_fixture_csv(self) -> None:
        # End-to-end: the committed CSV goes through the profile loader and the
        # kernel's own ensemble aggregation, without any table access.
        inside = [row for row in self.rows if _in_validity_domain(row)]
        with tempfile.TemporaryDirectory() as directory:
            filtered = Path(directory) / "p1iii_eos_sfho_realdata_filtered.csv"
            with filtered.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=list(self.rows[0]))
                writer.writeheader()
                writer.writerows(inside)
            payload = aggregate_profile_rows(
                load_profile_csv(filtered), order=256
            )
        self.assertEqual(len(payload["local_rows"]), 208)
        residuals = payload["max_relative_density_closure_residual"]
        self.assertEqual(set(residuals), {"n", "p"})
        self.assertLess(max(residuals.values()), 1e-3)
        # Every row must have used the tabulated filling factor, never the
        # composition-based fallback.
        sources = {row["xi_source"] for row in payload["local_rows"]}
        self.assertEqual(sources, {"single_particle_table"})


class TestOfficialTablesWhenAvailable(unittest.TestCase):
    """Whole-table checks; skipped unless SFHO_TABLES_DIR is configured."""

    @classmethod
    def setUpClass(cls) -> None:
        root = os.environ.get("SFHO_TABLES_DIR")
        if not root:
            raise unittest.SkipTest(
                "set SFHO_TABLES_DIR to an extracted SFHo/FRDM v1.03 archive"
            )
        from audit_b16_p1iii_eos_sfho_realdata_closure import locate_tables
        from sfho_eos_tables import Composition, ExtendedEOS, SPPTable

        cls.paths = locate_tables(Path(root))
        cls.extended = ExtendedEOS.load(cls.paths["extended_eos"])
        cls.single_particle = SPPTable.load(cls.paths["single_particle"])
        cls.composition = Composition.load(cls.paths["composition"])

    def test_table_shapes(self) -> None:
        self.assertEqual(self.extended.data.shape, TABLE_SHAPES["extended_eos"])
        self.assertEqual(
            self.single_particle.data.shape, TABLE_SHAPES["single_particle"]
        )
        self.assertEqual(self.composition.comp.shape, TABLE_SHAPES["composition"])

    def test_grids_follow_the_manual(self) -> None:
        temperatures = self.extended.temperature
        densities = self.extended.nb
        self.assertAlmostEqual(float(temperatures[0]), 0.1, places=12)
        self.assertAlmostEqual(float(temperatures[-1]), 158.489, delta=1e-3)
        self.assertAlmostEqual(float(densities[0]), 1e-12, delta=1e-23)
        # Fortran k >= 309 (array index >= 308) carries no density at all: the
        # nominal grid keeps going, but the stored column is exactly zero.
        self.assertAlmostEqual(float(densities[307]), 1.9054607, places=6)
        stored = self.extended.entry("nB_fm3")
        self.assertTrue((stored[:, :, 308:] == 0.0).all())
        self.assertTrue((stored[:, :, :308] > 0.0).all())

    def test_audited_cells_are_reproducible_from_the_tables(self) -> None:
        from audit_b16_p1iii_eos_sfho_realdata_closure import closure_cell

        indexed = {
            (int(_float(row, "t_index")), int(_float(row, "y_index")),
             int(_float(row, "k_index"))): row
            for row in _read_fixture()
        }
        for key in ((0, 10, 1), (40, 20, 200), (60, 30, 250), (70, 20, 300)):
            with self.subTest(cell=key):
                record = closure_cell(
                    self.extended, self.single_particle, *key, order=512
                )
                self.assertIn("ratio_n", record)
                expected = indexed[key]
                self.assertAlmostEqual(
                    record["ratio_n"] / _float(expected, "ratio_n"), 1.0,
                    delta=1e-6,
                )
                self.assertAlmostEqual(
                    record["nprime_n_fm3"] / _float(expected, "nprime_n_fm3"),
                    1.0,
                    delta=1e-6,
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
