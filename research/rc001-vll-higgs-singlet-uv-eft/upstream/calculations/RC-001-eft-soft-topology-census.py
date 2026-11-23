#!/usr/bin/env python3
"""Structural topology and heavy-mass power-counting audit for RC-001.

This script checks graph-theoretic loop counts and explicit 1/M_E powers for
candidate EFT soft topologies. It does NOT evaluate loop integrals, establish
that a tensor numerator is nonzero, or replace a FeynArts/FeynCalc diagram census.
The physical zero/nonzero annotations below are stated as analytic classification
assumptions and are documented in the accompanying research note.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Topology:
    tag: str
    name: str
    inverse_mass_powers: tuple[int, ...]
    vertices: int
    internal_lines: int
    one_particle_irreducible: bool
    sector: str
    assessment: str
    reason: str

    @property
    def loops(self) -> int:
        # Connected graph: L = I - V + 1. A self-contracted fermion tadpole
        # counts as one internal line and one independent loop.
        return self.internal_lines - self.vertices + 1

    @property
    def mass_power(self) -> int:
        return sum(self.inverse_mass_powers)


topologies = [
    Topology(
        "SFT-01", "C5 C5* light-fermion bubble; mixed H S H* S*",
        (1, 1), 2, 2, True, "dimension-six scalar 1PI",
        "KEEP: explicit soft integral already exists; independent graph-level check open",
        "The two conjugate dimension-five vertices provide exactly the four marked external scalars."
    ),
    Topology(
        "SFT-02", "QLD plus scalar quartic; fermion tadpole and one scalar line in four-scalar amplitude",
        (2, 0), 2, 2, False, "candidate mixed/pure scalar amplitude",
        "DROP from strict massless 1PI scalar matching at O(M_E^-2)",
        "The graph is scalar-line reducible; its only fermion loop is a scaleless one-propagator tadpole in the unbroken massless theory and vanishes in dimensional regularization."
    ),
    Topology(
        "SFT-03", "QRD plus scalar quartic; fermion tadpole and one scalar line in four-scalar amplitude",
        (2, 0), 2, 2, False, "candidate mixed/pure scalar amplitude",
        "DROP from strict massless 1PI scalar matching at O(M_E^-2)",
        "Same reducibility and scaleless-tadpole argument as SFT-02. A broken-phase mass insertion must be re-counted rather than promoted to O(M_E^-2)."
    ),
    Topology(
        "SFT-04", "QLD QLD light-fermion loop; pure H^4",
        (2, 2), 2, 2, True, "dimension-eight scalar 1PI",
        "EXCLUDE at O(M_E^-2); retain for O(M_E^-4)",
        "Two tree-level dimension-six insertions carry four inverse powers of M_E in total."
    ),
    Topology(
        "SFT-05", "QRD QRD light-fermion loop; pure S^4",
        (2, 2), 2, 2, True, "dimension-eight scalar 1PI",
        "EXCLUDE at O(M_E^-2); retain for O(M_E^-4)",
        "Two tree-level dimension-six insertions carry four inverse powers of M_E in total."
    ),
    Topology(
        "SFT-06", "QLD QRD light-fermion loop; mixed H^2 S^2",
        (2, 2), 2, 2, True, "dimension-eight scalar 1PI",
        "EXCLUDE at O(M_E^-2); retain for O(M_E^-4)",
        "The four external scalar legs are supplied directly, but the product of Wilson coefficients is O(M_E^-4)."
    ),
    Topology(
        "SFT-07", "QLD insertion with A' current exchange to S pair",
        (2, 0, 0), 3, 3, False, "mixed current/source sector",
        "TRACK separately; not a direct 1PI O_D projection",
        "At one loop and O(g_X^2 |y|^2/M_E^2), this is reducible through the exchanged A'. Its current form factor and matching counterpart must be handled if the connected amplitude or current-operator vector is matched."
    ),
    Topology(
        "SFT-08", "QRD insertion with hypercharge-current exchange to H pair",
        (2, 0, 0), 3, 3, False, "mixed current/source sector",
        "TRACK separately; not a direct 1PI O_D projection",
        "At one loop and O(g_Y^2 |lambda|^2/M_E^2), this is reducible through the exchanged B field. It belongs in the current/source ledger, not as an unqualified local four-scalar 1PI coefficient."
    ),
    Topology(
        "SFT-09", "QLD insertion with B/W current exchange to H pair",
        (2, 0, 0), 3, 3, False, "pure-H current/source sector",
        "TRACK separately for a complete connected amplitude/current vector",
        "The graph is O(g_SM^2 |y|^2/M_E^2) and one-loop, but is one-particle reducible through the gauge propagator."
    ),
    Topology(
        "SFT-10", "QRD insertion with A' current exchange to S pair",
        (2, 0, 0), 3, 3, False, "pure-S current/source sector",
        "TRACK separately for a complete connected amplitude/current vector",
        "The graph is O(g_X^2 |lambda|^2/M_E^2) and one-loop, but is one-particle reducible through the gauge propagator."
    ),
    Topology(
        "SFT-11", "Four C5 insertions in an eight-scalar light-fermion loop",
        (1, 1, 1, 1), 4, 4, True, "dimension-eight potential",
        "RETAIN for the O(M_E^-4) X^2 Y^2 sector",
        "This is the unbroken-phase dimension-eight soft topology. The broken-phase C5-squared constant projection is its VEV projection, not an independent extra graph to add again."
    ),
    Topology(
        "SFT-12", "C5 C7* light-fermion loop, if C7 survives EOM reduction",
        (1, 3), 2, 2, True, "conditional dimension-eight derivative/source sector",
        "CONDITIONAL: derive and reduce the tree-level 1/M_E^3 operator first",
        "The product is O(M_E^-4). If the dimension-seven representative is EOM-redundant, its induced source/potential companions must still be tracked."
    ),
    Topology(
        "SFT-13", "C5 C5* bubble with QLD/QRD VEV wavefunction insertion",
        (1, 1, 2), 3, 3, True, "broken-phase dimension-eight correction",
        "EXCLUDE at O(M_E^-2); retain at O(M_E^-4)",
        "At fixed v_h,v_s the extra Q6 insertion adds two inverse powers of M_E; this agrees with the explicit delta-Z scaling in source §243.4."
    ),
    Topology(
        "SFT-14", "C5 C5* crossed loop in external Lbar L H* H channel; internal right-handed lepton and S",
        (1, 1), 2, 2, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete dimension-six fermion-operator vector",
        "One internal fermion and one internal scalar propagator form a one-loop 1PI graph at O(M_E^-2)."
    ),
    Topology(
        "SFT-15", "C5 C5* crossed loop in external Lbar L S* S channel; internal right-handed lepton and H",
        (1, 1), 2, 2, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete dimension-six fermion-operator vector",
        "One internal fermion and one internal scalar propagator form a one-loop 1PI graph at O(M_E^-2)."
    ),
    Topology(
        "SFT-16", "C5 C5* crossed loop in external lRbar lR H* H channel; internal left-handed lepton and S",
        (1, 1), 2, 2, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete dimension-six fermion-operator vector",
        "One internal fermion and one internal scalar propagator form a one-loop 1PI graph at O(M_E^-2)."
    ),
    Topology(
        "SFT-17", "C5 C5* crossed loop in external lRbar lR S* S channel; internal left-handed lepton and H",
        (1, 1), 2, 2, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete dimension-six fermion-operator vector",
        "One internal fermion and one internal scalar propagator form a one-loop 1PI graph at O(M_E^-2)."
    ),
    Topology(
        "SFT-18", "C5 C5* scalar loop in external Lbar L lRbar lR four-fermion channel",
        (1, 1), 2, 2, True, "dimension-six four-fermion 1PI",
        "KEEP for the complete dimension-six four-fermion vector",
        "The four external fermions are supplied by the two C5 vertices; internal H and S propagators close a one-loop scalar bubble at O(M_E^-2)."
    ),
    Topology(
        "SFT-19", "QLD plus lambda_H scalar bubble in external Lbar L H* H channel",
        (2, 0), 2, 2, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete dimension-six fermion-operator vector",
        "Both H legs of QLD connect to the scalar quartic; the quartic supplies the external H pair. Two scalar propagators give a non-scaleless one-loop bubble."
    ),
    Topology(
        "SFT-20", "QLD plus lambda_HS scalar bubble in external Lbar L S* S channel",
        (2, 0), 2, 2, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete dimension-six fermion-operator vector",
        "The QLD H pair connects to the portal vertex; the portal supplies the external S pair. The scalar bubble is one-loop and O(lambda_HS |y|^2/M_E^2)."
    ),
    Topology(
        "SFT-21", "QRD plus lambda_S scalar bubble in external lRbar lR S* S channel",
        (2, 0), 2, 2, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete dimension-six fermion-operator vector",
        "Both S legs of QRD connect to the scalar quartic; the quartic supplies the external S pair. Two scalar propagators give a non-scaleless one-loop bubble."
    ),
    Topology(
        "SFT-22", "QRD plus lambda_HS scalar bubble in external lRbar lR H* H channel",
        (2, 0), 2, 2, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete dimension-six fermion-operator vector",
        "The QRD S pair connects to the portal vertex; the portal supplies the external H pair. The scalar bubble is one-loop and O(lambda_HS |lambda|^2/M_E^2)."
    ),
    Topology(
        "SFT-23", "C5 plus lambda_HS scalar bubble in the Lbar lR H S amplitude",
        (1, 0), 2, 2, True, "one-loop correction to dimension-five coefficient",
        "KEEP only if claiming one-loop closure of C5; not needed to extract the one-loop dimension-six scalar coefficient",
        "The C5 scalar legs connect to the portal vertex and the portal supplies the external H,S pair; two scalar propagators form one loop."
    ),
    Topology(
        "SFT-24", "C5 insertion with one-loop gauge corrections in the Lbar lR H S amplitude",
        (1, 0), 3, 3, True, "one-loop correction to dimension-five coefficient",
        "KEEP only if claiming one-loop closure of C5",
        "Gauge vertex, leg, and covariant-derivative contact graphs renormalize the dimension-five operator at O(g^2 C5); the gauge-invariant set and external-field scheme must be used together."
    ),
    Topology(
        "SFT-25", "QLD insertion with gauge-loop corrections in the Lbar L H* H amplitude",
        (2, 0), 3, 3, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete one-loop QLD coefficient",
        "Gauge vertex, leg, and covariant-derivative contact graphs give O(g^2 |y|^2/M_E^2) soft renormalization; include the gauge-invariant set and counterterms."
    ),
    Topology(
        "SFT-26", "QRD insertion with gauge-loop corrections in the lRbar lR S* S amplitude",
        (2, 0), 3, 3, True, "dimension-six fermion-scalar 1PI",
        "KEEP for the complete one-loop QRD coefficient",
        "Gauge vertex, leg, and covariant-derivative contact graphs give O(g^2 |lambda|^2/M_E^2) soft renormalization; include the gauge-invariant set and counterterms."
    ),
]

by_tag = {item.tag: item for item in topologies}
assert len(by_tag) == len(topologies), "Topology tags must be unique"
for item in topologies:
    assert item.loops == 1, f"Unexpected loop count for {item.tag}: {item.loops}"

assert by_tag["SFT-01"].mass_power == 2 and by_tag["SFT-01"].one_particle_irreducible
assert by_tag["SFT-02"].mass_power == 2 and not by_tag["SFT-02"].one_particle_irreducible
assert by_tag["SFT-03"].mass_power == 2 and not by_tag["SFT-03"].one_particle_irreducible
assert all(by_tag[tag].mass_power == 4 for tag in ("SFT-04", "SFT-05", "SFT-06", "SFT-11", "SFT-12", "SFT-13"))
assert all(not by_tag[tag].one_particle_irreducible for tag in ("SFT-07", "SFT-08", "SFT-09", "SFT-10"))
assert all(by_tag[tag].mass_power == 2 and by_tag[tag].one_particle_irreducible for tag in ("SFT-14", "SFT-15", "SFT-16", "SFT-17", "SFT-18", "SFT-19", "SFT-20", "SFT-21", "SFT-22", "SFT-25", "SFT-26"))
assert by_tag["SFT-23"].mass_power == 1 and by_tag["SFT-23"].one_particle_irreducible
assert by_tag["SFT-24"].mass_power == 1 and by_tag["SFT-24"].one_particle_irreducible

print("RC-001 EFT soft topology census")
print("Method: L = I - V + 1 for connected graphs; Wilson-coefficient powers are counted explicitly.")
print("Scope: structural/topological and mass-power checks only; no loop integral is evaluated.")
print()
for item in topologies:
    print(f"{item.tag} | L={item.loops} | 1/M_E^{item.mass_power} | "
          f"1PI={item.one_particle_irreducible} | {item.assessment}")
    print(f"  Reason: {item.reason}")

print()
print("PASS: unique topology IDs")
print("PASS: every listed candidate has the stated one-loop Euler count")
print("PASS: C5 C5* four-scalar bubble is O(M_E^-2) and 1PI")
print("PASS: scalar-quartic tadpole candidates in four-scalar amplitudes are reducible/scaleless in the massless unbroken scheme")
print("PASS: C5 C5* crossed two-fermion/two-scalar and four-fermion graphs are O(M_E^-2) and 1PI")
print("PASS: Q6-plus-quartic scalar bubbles in two-fermion/two-scalar channels are O(M_E^-2) and 1PI")
print("PASS: Q6 x Q6, C5 x C7, C5^4, and Q6-inserted C5^2 corrections are O(M_E^-4)")
print("PASS: gauge-current exchange candidates are kept distinct from the local 1PI scalar projection")
print("LIMIT: this census is not a Feynman-rule-complete diagram generation or independent loop-integral validation.")
print("OPEN: explicitly integrate the listed C5-crossed and Q6 scalar/gauge soft sectors required by the basis; close all fermionic amplitudes; then enumerate the full O(M_E^-4) hard/soft set.")
