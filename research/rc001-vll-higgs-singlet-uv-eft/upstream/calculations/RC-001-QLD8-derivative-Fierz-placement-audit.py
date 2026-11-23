#!/usr/bin/env python3
"""Exact bookkeeping audit for QLD8 derivative/Fierz placement map.

This checks source-pair counts and verifies that the Fierz-rearranged
bilinear assignment preserves the derivative on each original fermion field.
It is not a Dirac-algebra or loop-renormalization calculation.
"""
from itertools import product

SOURCES = ("d", "u", "e")
CHIRAL_CLASS = {
    ("d", "d"): "RL",
    ("u", "u"): "LR",
    ("e", "e"): "RL",
    ("d", "u"): "RR",
    ("u", "d"): "LL",
    ("d", "e"): "RL",
    ("e", "d"): "LR",
    ("u", "e"): "LL",
    ("e", "u"): "RR",
}
UNIQUE_HERMITIAN = (
    ("d", "d"), ("u", "u"), ("e", "e"),
    ("d", "u"), ("d", "e"), ("u", "e"),
)
CROSS = (("d", "u"), ("d", "e"), ("u", "e"))


def derivative_assignment(r, s):
    """Return differentiated fields in the two crossed Fierz bilinears.

    Original pair: (bar(psi) chi)(bar(eta) xi).
    Fierz pair:    (bar(psi) Gamma xi)(bar(eta) Gamma' chi).
    r=0: D bar(psi); r=1: D chi.
    s=0: D bar(eta); s=1: D xi.
    """
    first = []
    second = []
    if r == 0:
        first.append("D_bar_psi")
    else:
        second.append("D_chi")
    if s == 0:
        second.append("D_bar_eta")
    else:
        first.append("D_xi")
    return tuple(first), tuple(second)


def audit():
    ordered_pairs = tuple(product(SOURCES, repeat=2))
    assert len(ordered_pairs) == 9
    assert set(ordered_pairs) == set(CHIRAL_CLASS)
    assert len(UNIQUE_HERMITIAN) == 6
    assert len(CROSS) == 3
    assert sum(1 for a, b in ordered_pairs if a == b) == 3
    assert sum(1 for a, b in ordered_pairs if a != b) == 6

    placements = tuple(product((0, 1), repeat=2))
    assert len(placements) == 4
    ordered_placements = [
        (pair, placement)
        for pair in ordered_pairs
        for placement in placements
    ]
    assert len(ordered_placements) == 36

    expected = {
        (0, 0): (("D_bar_psi",), ("D_bar_eta",)),
        (0, 1): (("D_bar_psi", "D_xi"), ()),
        (1, 0): ((), ("D_chi", "D_bar_eta")),
        (1, 1): (("D_xi",), ("D_chi",)),
    }
    observed = {}
    for placement in placements:
        got = derivative_assignment(*placement)
        assert got == expected[placement]
        flat = got[0] + got[1]
        assert len(flat) == 2
        assert len(set(flat)) == 2
        observed[f"{placement[0]}{placement[1]}"] = got

    class_counts = {}
    for cls in CHIRAL_CLASS.values():
        class_counts[cls] = class_counts.get(cls, 0) + 1
    assert class_counts == {"RL": 3, "LR": 2, "RR": 2, "LL": 2}

    return {
        "ordered_source_pairs": len(ordered_pairs),
        "diagonal_pairs": 3,
        "cross_pairs_with_hc": 3,
        "ordered_derivative_placements": len(ordered_placements),
        "placements_per_ordered_pair": len(placements),
        "chiral_class_counts": class_counts,
        "fierz_derivative_assignment": observed,
        "result": "PASS",
        "scope": "bookkeeping and derivative-label transport only; no d-dimensional loop mixing",
    }


if __name__ == "__main__":
    result = audit()
    print("RC-001 QLD8 derivative/Fierz placement audit")
    print(f"PASS: {result['ordered_source_pairs']} ordered source pairs")
    print(f"PASS: {result['diagonal_pairs']} diagonal and {result['cross_pairs_with_hc']} cross+HC structures")
    print(f"PASS: {result['ordered_derivative_placements']} ordered product-rule placements")
    print(f"PASS: chiral classes {result['chiral_class_counts']}")
    for key, value in result["fierz_derivative_assignment"].items():
        print(f"PASS: placement {key} -> {value}")
    print("LIMIT: bookkeeping only; no d-dimensional loop mixing or finite matching")
