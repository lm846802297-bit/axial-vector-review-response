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

Sample-grid validity classification (established by ``audit_b16_p1iii_eos_sfho_realdata_closure.py``
and documented in ``B16_P1IIIE_B_SFHO_REALDATA_CLOSURE_2026-11-11.md``; not a continuous-domain theorem):

  T <= 25.2 MeV   OR   nB >= 9.9e-5 fm^-3

Inside that domain the closure residual stays below 1e-3 for both species
(audited maxima: 6.13e-4 neutron, 8.86e-5 proton for X_p >= 1e-6).
Outside it, 16 cells remain at T = 63.096 MeV and nB = 1.10e-12, 1e-10,
1e-8, or 1e-6 fm^-3 (four Yp values at each density). All have X_n+X_p=1,
but they do not all share the same chemical-potential floor: only the eight
lowest-density cells show the clear n'_n plateau; the 1e-8 cells are transitional,
and the 1e-6 cells are much closer to density closure while still outside the
1e-3 acceptance threshold. The tests keep these regimes distinct.
"""

from __future__ import annotations

import csv
import os
import tempfile
import unittest
from pathlib import Path

import numpy as np

from audit_b16_p1iii_eos_nucleon_distribution import (
    HBARC_MEV_FM,
    MASS_SPLITTING_MEV,
    aggregate_profile_rows,
    load_profile_csv,
    phase_space_integrals,
    state_from_hs_spp,
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
        # The lowest two density rows are nucleon-only, but their composition
        # follows the four tabulated Yp values rather than a fixed (0.8, 0.2).
        floor = [
            row
            for row in self.rows
            if abs(_float(row, "T_MeV") - FLOOR_T_MEV) < 1e-2
            and int(_float(row, "k_index")) <= FLOOR_MAX_K_INDEX
        ]
        self.assertEqual(len(floor), 8)
        for row in floor:
            self.assertAlmostEqual(
                _float(row, "X_n") + _float(row, "X_p"), 1.0, delta=1e-8
            )
            self.assertAlmostEqual(_float(row, "X_p"), _float(row, "Yp_tot"), delta=1e-8)
            self.assertAlmostEqual(_float(row, "X_n"), 1.0 - _float(row, "Yp_tot"), delta=1e-8)

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
            state = state_from_hs_spp(
                "n", _float(row, "T_MeV"), _float(row, "mstar_n_MeV"),
                _float(row, "SigmaV_n_MeV"), _float(row, "mu_nonrel_n_MeV")
            )
            self.assertLess(
                abs(state.effective_chemical_potential_mev / _float(row, "T_MeV") + 14.891),
                5e-4,
            )
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

    def test_outside_domain_has_three_distinct_regimes(self) -> None:
        outside = [row for row in self.rows if not _in_validity_domain(row)]
        self.assertEqual(len(outside), 16)
        by_k = {
            k: [row for row in outside if int(_float(row, "k_index")) == k]
            for k in (1, 50, 100, 150)
        }
        self.assertTrue(all(len(group) == 4 for group in by_k.values()))
        for row in outside:
            self.assertAlmostEqual(
                _float(row, "X_n") + _float(row, "X_p"), 1.0, delta=1e-8
            )
            self.assertAlmostEqual(
                _float(row, "X_p"), _float(row, "Yp_tot"), delta=1e-8
            )
        for k in (1, 50):
            self.assertGreater(min(_float(r, "ratio_n") for r in by_k[k]), 1e2)
            self.assertGreater(min(_float(r, "ratio_p") for r in by_k[k]), 1e2)
        self.assertTrue(all(10.0 < _float(r, "ratio_n") < 16.0 for r in by_k[100]))
        self.assertTrue(all(20.0 < _float(r, "ratio_p") < 100.0 for r in by_k[100]))
        self.assertTrue(all(1.0 < _float(r, "ratio_n") < 1.03 for r in by_k[150]))
        self.assertTrue(all(1.05 < _float(r, "ratio_p") < 1.57 for r in by_k[150]))

    def test_real_eos_quadrature_converges_1024_to_2048(self) -> None:
        # The old 512-node rule under-resolved the narrow f(1-f) shell at
        # T=0.1 MeV and high density. The fixture now stores 1024-node values.
        for row in self.rows:
            for species in ("n", "p"):
                state = state_from_hs_spp(
                    species,
                    _float(row, "T_MeV"),
                    _float(row, f"mstar_{species}_MeV"),
                    _float(row, f"SigmaV_{species}_MeV"),
                    _float(row, f"mu_nonrel_{species}_MeV"),
                )
                n1024, blocked1024 = phase_space_integrals(state, order=1024)
                n2048, blocked2048 = phase_space_integrals(state, order=2048)
                f1024 = blocked1024 / n1024
                f2048 = blocked2048 / n2048
                nprime1024 = n1024 / HBARC_MEV_FM**3
                self.assertLess(abs(f1024 - _float(row, f"Fdeg_{species}")), 5e-10)
                self.assertLess(abs(f1024 - f2048), 1e-7)
                self.assertLess(abs(n1024 / n2048 - 1.0), 2e-8)
                self.assertLess(
                    abs(nprime1024 / _float(row, f"nprime_{species}_fm3") - 1.0),
                    2e-9,
                )

    def test_effective_mass_splitting_matches_the_sfho_table(self) -> None:
        residuals = [
            abs(
                (_float(row, "mstar_n_MeV") - _float(row, "mstar_p_MeV"))
                - MASS_SPLITTING_MEV
            )
            for row in self.rows
        ]
        self.assertLess(max(residuals), 1e-4)

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
                load_profile_csv(filtered), order=1024
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

    def test_spp_proton_fraction_and_density_match_extended_table(self) -> None:
        from sfho_eos_tables import NB_PHYSICAL

        spp_yp = self.single_particle.column("Yp_tot")[:, :, :NB_PHYSICAL]
        ext_yp = self.extended.entry("Yp_tot")[:, 1:, :NB_PHYSICAL]
        self.assertLess(float(np.abs(spp_yp - ext_yp).max()), 1e-8)

        spp_nb = self.single_particle.column("nB_fm3")[:, :, :NB_PHYSICAL]
        ext_nb = self.extended.entry("nB_fm3")[:, 1:, :NB_PHYSICAL]
        # The SPP ASCII density column is rounded; the full-table audit found O(4e-7) relative differences.
        self.assertLess(float(np.abs(spp_nb / ext_nb - 1.0).max()), 1e-6)

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


class ArchiveManifestTests(unittest.TestCase):
    """The published archives are fetched, not committed: keep the record honest.

    A truncated SHA-256 is internally invalid rather than merely wrong, and it
    survives review because nobody re-counts 64 hex characters.  These tests tie
    the checksum manifest, the downloader's ``FILES`` table and the audit record
    together offline, so a transcription slip fails here instead of at download
    time on a user's machine.
    """

    MANIFEST = HERE / "sfho_frdm_v1.03_manifest.sha256"
    DOWNLOADER = HERE / "sfho_frdm_v1.03_download.py"
    AUDIT_JSON = HERE / "outputs" / "p1iii_eos_sfho_realdata_closure_2026-11-11.json"

    def _manifest(self) -> dict[str, str]:
        entries: dict[str, str] = {}
        for line in self.MANIFEST.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            digest, name = line.split()
            self.assertNotIn(name, entries, f"duplicate manifest entry {name}")
            entries[name] = digest
        return entries

    def _downloader_files(self) -> dict[str, tuple[int, str]]:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "_sfho_frdm_download", self.DOWNLOADER
        )
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        return {
            entry["name"]: (int(entry["bytes"]), entry["sha256"])
            for entry in module.FILES
        }

    def test_every_manifest_hash_is_a_full_sha256(self) -> None:
        manifest = self._manifest()
        self.assertEqual(len(manifest), 5)
        for name, digest in manifest.items():
            with self.subTest(archive=name):
                self.assertEqual(len(digest), 64)
                self.assertRegex(digest, r"^[0-9a-f]{64}$")

    def test_downloader_table_matches_the_manifest(self) -> None:
        manifest = self._manifest()
        files = self._downloader_files()
        self.assertEqual(set(files), set(manifest))
        for name, digest in manifest.items():
            with self.subTest(archive=name):
                size, recorded = files[name]
                self.assertGreater(size, 0)
                self.assertEqual(recorded, digest)

    def test_manifest_matches_the_audit_record(self) -> None:
        import json

        provenance = json.loads(
            self.AUDIT_JSON.read_text(encoding="utf-8")
        )["provenance"]
        archives = provenance["archive_sha256"]
        manifest = self._manifest()
        self.assertEqual(set(archives), set(manifest))
        for name, digest in archives.items():
            with self.subTest(archive=name):
                self.assertEqual(len(digest), 64)
                self.assertEqual(manifest[name], digest)


if __name__ == "__main__":
    unittest.main(verbosity=2)
