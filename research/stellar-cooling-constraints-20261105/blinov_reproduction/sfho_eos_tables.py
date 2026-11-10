#!/usr/bin/env python3
"""Readers for the official Basel/Hempel SFHo/FRDM EOS tables (v1.03).

Sources (University of Basel, M. Hempel):

* ``sfho_frdm_bin.zip``        -- extended thermodynamic table, 18 entries
* ``sfho_frdm_spp.zip``        -- single-particle properties, 7 columns
* ``sfho_frdm_comp.zip``       -- nuclear composition, 8 layers
* ``sfho_frdm_shen98format.zip`` -- Shen98 ASCII cross-check, 19 columns

Version note.  The four SFHo/FRDM archives are v1.03 data (uploaded
2012-07-09); the accompanying manual is v1.04, which only added the IUFSU
table and updated the manuscript/plot section.  The version-history page
therefore does not indicate a data mismatch.

Binary layout.  Every ``.bin`` file is a single Intel Fortran
unformatted-sequential record: a 4-byte little-endian payload length, the
payload, and the same length again.  A file of payload ``8*N`` bytes
therefore has size ``8 + 8*N``.  Arrays are column-major, so the fastest
index is the first Fortran dimension (temperature).

Grid (manual Secs. 2-4)::

    T   = 0.1 * 10**(0.04*(i-1))  MeV       i = 1..81   (0.1 .. 158.5)
    Yp  = 0.01*j                             j = 0..60   (extended table)
                                             j = 1..60   (SPP, Shen98)
    nB  = 1e-12 * 10**(0.04*(k-1)) fm^-3     k = 1..326  (1e-12 .. 10)

SFHo-specific caveat: the field equations have no solution above
``nB = 1.905 fm^-3``, so the extended thermodynamic and composition payloads have no physical
solution for Fortran k >= 309; the composition module returns immediately (``if (k.ge.309)
return``). The SPP file still carries nominal coordinate columns at those indices;
its remaining properties are not physical solutions. Never interpret the entire
SPP row as an all-zero record, and never average closure residuals over those entries.
"""
from __future__ import annotations

import os
import struct
from dataclasses import dataclass
from pathlib import Path

import numpy as np

HQC_MEV_FM = 197.3269631
# Hempel's EOS-internal conversion used for the composition-table MeV^3
# columns. The occupation kernel separately uses its physical HBARC_MEV_FM.
HQC3_MEV3 = HQC_MEV_FM**3
# Vacuum masses used by the Hempel-to-Fiorillo occupation mapping.
NEUTRON_MASS_MEV = 939.565346
PROTON_MASS_MEV = 938.272013
AMU_MEV = 931.49432
# nb0 = 0.15824150805 * hqc^3 is the saturation density used by the
# distributed Hempel/Lattimer-Swesty excluded-volume module.
NUCLEON_BAG_DENSITY_FM3 = 0.15824150805

T_ENTRIES = 81
Y_ENTRIES = 61
Y_ENTRIES_SPP = 60
NB_ENTRIES = 326
#: Fortran k of the first all-zero density row: the interaction has no solution
#: for k >= 309 (K_MAX_REAL), so array indices 308..325 are exactly zero.
K_MAX_REAL = 309
#: Number of physical density rows; array indices 0..NB_PHYSICAL-1 are filled.
NB_PHYSICAL = K_MAX_REAL - 1

EXTENDED_ENTRIES = (
    "nB_fm3",
    "Yp_tot",
    "E_total_MeV",
    "p_total_MeV_fm3",
    "S_total_kB",
    "mu_n_nonrel_MeV",
    "mu_p_nonrel_MeV",
    "mu_e_nonrel_MeV",
    "F_total_MeV",
    "X_n",
    "X_p",
    "X_d",
    "X_t",
    "X_h",
    "X_alpha",
    "X_A",
    "mean_A",
    "mean_Z",
)

SPP_COLUMNS = (
    "nB_fm3",
    "Yp_tot",
    "SigmaV_n_tot_MeV",
    "SigmaV_p_tot_MeV",
    "xi",
    "mstar_n_MeV",
    "mstar_p_MeV",
)

SHEN98_COLUMNS = (
    "log10_rhoB",
    "nB_fm3",
    "log10_Yp",
    "Yp_tot",
    "F_per_baryon_MeV",
    "E_per_baryon_MeV",
    "S_per_baryon_kB",
    "mean_A_heavy",
    "mean_Z_heavy",
    "mean_effective_mass_MeV",
    "X_n",
    "X_p",
    "X_light_clusters",
    "X_heavy",
    "p_B_MeV_fm3",
    "mu_n_nonrel_MeV",
    "mu_p_nonrel_MeV",
    "mean_a",
    "mean_z",
)


def temperature_grid() -> np.ndarray:
    return 0.1 * 10.0 ** (0.04 * np.arange(T_ENTRIES))


def ye_grid(include_zero: bool = True) -> np.ndarray:
    start = 0 if include_zero else 1
    return 0.01 * np.arange(start, Y_ENTRIES)


def baryon_density_grid() -> np.ndarray:
    return 1.0e-12 * 10.0 ** (0.04 * np.arange(NB_ENTRIES))


def default_tables_dir() -> Path | None:
    """Directory holding the extracted v1.03 tables, if the caller exported it."""
    value = os.environ.get("SFHO_TABLES_DIR")
    return Path(value) if value else None


def _read_single_record(path: Path) -> bytes:
    """Read one Fortran unformatted-sequential record and validate both markers."""
    with path.open("rb") as stream:
        header = stream.read(4)
        if len(header) != 4:
            raise ValueError(f"{path.name} is too short to hold a record marker")
        (length,) = struct.unpack("<i", header)
        payload = stream.read(length)
        (trailer,) = struct.unpack("<i", stream.read(4))
    if len(payload) != length:
        raise ValueError(f"{path.name}: payload truncated")
    if trailer != length:
        raise ValueError(
            f"{path.name}: trailing record marker {trailer} != {length}"
        )
    return payload


def _floats(payload: bytes) -> np.ndarray:
    if len(payload) % 8 != 0:
        raise ValueError("payload length is not a multiple of 8 bytes")
    return np.frombuffer(payload, dtype="<f8")


@dataclass(frozen=True)
class ExtendedEOS:
    """Extended thermodynamic table, ``data[i, j, k, entry]``.

    ``i`` runs over temperature, ``j`` over Yp (0..60, so j=0 is Yp=0),
    ``k`` over baryon density and ``entry`` over :data:`EXTENDED_ENTRIES`.
    The stored energy and free energy include the nucleon rest masses, and
    the proton chemical potential already contains the Coulomb part.
    """

    path: Path
    data: np.ndarray
    temperature: np.ndarray
    ye: np.ndarray
    nb: np.ndarray

    @classmethod
    def load(cls, path: Path) -> "ExtendedEOS":
        data = _floats(_read_single_record(path))
        expected = T_ENTRIES * Y_ENTRIES * NB_ENTRIES * len(EXTENDED_ENTRIES)
        if data.size != expected:
            raise ValueError(
                f"{path.name}: {data.size} doubles, expected {expected}"
            )
        array = data.reshape(
            (T_ENTRIES, Y_ENTRIES, NB_ENTRIES, len(EXTENDED_ENTRIES)),
            order="F",
        )
        return cls(
            path=path,
            data=array,
            temperature=temperature_grid(),
            ye=ye_grid(include_zero=True),
            nb=baryon_density_grid(),
        )

    def entry(self, name: str) -> np.ndarray:
        return self.data[..., EXTENDED_ENTRIES.index(name)]


@dataclass(frozen=True)
class SPPTable:
    """Single-particle table, ``data[i, jj, k, column]``.

    ``i`` is the temperature block index, ``jj = 0..59`` the Yp block
    (Yp = 0.01..0.60; the table has no Yp=0 block), ``k`` the density index
    and ``column`` the entry of :data:`SPP_COLUMNS`.  ``mstar`` is the Dirac
    effective mass and ``SigmaV_tot`` the total vector self-energy
    ``Sigma_V^R + W`` of Hempel (2015) Eqs. (95)-(99).
    """

    path: Path
    data: np.ndarray
    temperature: np.ndarray
    ye: np.ndarray
    nb: np.ndarray

    @classmethod
    def load(cls, path: Path) -> "SPPTable":
        blocks: list[tuple[float, np.ndarray]] = []
        rows: list[list[float]] = []
        current_temperature: float | None = None

        with path.open("r", encoding="utf-8", errors="strict") as stream:
            for line in stream:
                stripped = line.strip()
                if not stripped:
                    continue
                if stripped.startswith("Temperature"):
                    if current_temperature is not None:
                        blocks.append(
                            (current_temperature, np.asarray(rows, float))
                        )
                        rows = []
                    current_temperature = float(stripped.split("=")[1])
                    continue
                if stripped.startswith(("c", "C")) and not stripped[0].isdigit():
                    continue
                fields = stripped.split()
                if len(fields) != len(SPP_COLUMNS):
                    raise ValueError(
                        f"{path.name}: unexpected column count "
                        f"{len(fields)} in line {stripped[:40]!r}"
                    )
                rows.append([float(value) for value in fields])
        if current_temperature is not None:
            blocks.append((current_temperature, np.asarray(rows, float)))

        if len(blocks) != T_ENTRIES:
            raise ValueError(
                f"{path.name}: {len(blocks)} temperature blocks, "
                f"expected {T_ENTRIES}"
            )
        per_block = Y_ENTRIES_SPP * NB_ENTRIES
        for temperature, block in blocks:
            if block.shape != (per_block, len(SPP_COLUMNS)):
                raise ValueError(
                    f"{path.name}: block T={temperature} has shape "
                    f"{block.shape}, expected ({per_block}, 7)"
                )
        data = np.stack(
            [
                block.reshape(Y_ENTRIES_SPP, NB_ENTRIES, len(SPP_COLUMNS))
                for _, block in blocks
            ]
        )
        temperatures = np.asarray([temperature for temperature, _ in blocks])
        return cls(
            path=path,
            data=data,
            temperature=temperatures,
            ye=ye_grid(include_zero=False),
            nb=baryon_density_grid(),
        )

    def column(self, name: str) -> np.ndarray:
        return self.data[..., SPP_COLUMNS.index(name)]


@dataclass(frozen=True)
class Composition:
    """Nuclear composition table.

    ``comp[i, j, k, layer]`` with the layers decoded from the distributed
    ``sfho_frdm_composition_module.f`` writes and the physical checks in the
    companion audit script:

    ==== ==========================================================
    0    mu_n_nonrel [MeV] (matches the extended table to 1e-4 MeV)
    1    proton-side chemical potential, not mu_p and not mu_p - mu_e
    2    close to, but not exactly, the SPP filling factor xi
    3    Coulomb-type term / nb0 (order MeV)
    4    nuclear-suppression switch: 1.0 means no nuclei; fractional values
         occur in the transition region
    5    electron-density input passed to sub_coulomb [MeV^3]. This is a
         Coulomb-background input, not a globally valid n_e = Yp_tot*nB
         column; it is zero when the no-nuclei switch is 1 and can differ
         from the volume-averaged charge density in the coexistence region
    6    free neutron density n_n [MeV^3]
    7    free proton density n_p [MeV^3]
    ==== ==========================================================
    """

    path: Path
    az: np.ndarray
    mass_mev: np.ndarray
    binding_mev: np.ndarray
    comp: np.ndarray

    @classmethod
    def load(cls, path: Path) -> "Composition":
        payload = _read_single_record(path)
        kmax = 8140
        expected = kmax * 2 * 4 + kmax * 8 + kmax * 8 + (
            T_ENTRIES * Y_ENTRIES * NB_ENTRIES * 8 * 8
        )
        if len(payload) != expected:
            raise ValueError(
                f"{path.name}: {len(payload)} bytes, expected {expected}"
            )
        offset = 0
        az = np.frombuffer(payload[offset : offset + kmax * 2 * 4], "<i4")
        offset += kmax * 2 * 4
        az = az.reshape(kmax, 2, order="F")
        mass = np.frombuffer(payload[offset : offset + kmax * 8], "<f8").copy()
        offset += kmax * 8
        binding = np.frombuffer(
            payload[offset : offset + kmax * 8], "<f8"
        ).copy()
        offset += kmax * 8
        comp = np.frombuffer(payload[offset:], "<f8").reshape(
            (T_ENTRIES, Y_ENTRIES, NB_ENTRIES, 8), order="F"
        )
        return cls(path=path, az=az, mass_mev=mass, binding_mev=binding, comp=comp)


def sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while True:
            block = stream.read(chunk)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


__all__ = [
    "AMU_MEV",
    "Composition",
    "EXTENDED_ENTRIES",
    "ExtendedEOS",
    "HQC3_MEV3",
    "HQC_MEV_FM",
    "K_MAX_REAL",
    "NB_PHYSICAL",
    "NB_ENTRIES",
    "NEUTRON_MASS_MEV",
    "NUCLEON_BAG_DENSITY_FM3",
    "PROTON_MASS_MEV",
    "SHEN98_COLUMNS",
    "SPP_COLUMNS",
    "SPPTable",
    "T_ENTRIES",
    "Y_ENTRIES",
    "baryon_density_grid",
    "default_tables_dir",
    "sha256_file",
    "temperature_grid",
    "ye_grid",
]
