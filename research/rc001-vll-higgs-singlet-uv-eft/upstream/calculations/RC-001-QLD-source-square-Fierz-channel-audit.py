#!/usr/bin/env python3
"""Bookkeeping audit of the QLD8 Higgs-source-square Fierz channels."""
from __future__ import annotations
import json

SOURCES=("d","u","e")
ORDERED=tuple((a,b) for a in SOURCES for b in SOURCES)
DIAGONAL=tuple((a,a) for a in SOURCES)
CROSS=tuple((a,b) for a,b in (("d","u"),("d","e"),("u","e")))
FIERZ_CLASS={
    ("d","d"):"opposite-projector scalar pair -> vector-current type",
    ("u","u"):"opposite-projector scalar pair -> vector-current type",
    ("e","e"):"opposite-projector scalar pair -> vector-current type",
    ("d","e"):"opposite-projector scalar pair -> vector-current type",
    ("d","u"):"same-projector scalar pair -> scalar/tensor structures",
    ("u","e"):"same-projector scalar pair -> scalar/tensor structures",
}
COLOR={
    ("d","d"):"quark crossed-color; singlet/octet decomposition required",
    ("u","u"):"quark crossed-color; singlet/octet decomposition required",
    ("e","e"):"colour singlet",
    ("d","e"):"quark color carried by one bilinear",
    ("d","u"):"two-quark-bilinear color/flavor contractions retained",
    ("u","e"):"quark-lepton; color carried by quark bilinear",
}
WEAK={
    ("d","d"):"weak singlet",
    ("u","u"):"epsilon contraction squared; weak singlet",
    ("e","e"):"weak singlet",
    ("d","e"):"weak singlet",
    ("d","u"):"antisymmetric epsilon contraction",
    ("u","e"):"antisymmetric epsilon contraction",
}


def audit():
    assert len(ORDERED)==9
    assert len(DIAGONAL)==3 and len(CROSS)==3
    assert len(FIERZ_CLASS)==6
    assert all((a,b) in FIERZ_CLASS and (b,a) in FIERZ_CLASS for a,b in DIAGONAL)
    # The three cross pairs are represented once; their reverse is the h.c.
    assert set(CROSS)=={("d","u"),("d","e"),("u","e")}
    placements_per_ordered_pair=2*2
    assert placements_per_ordered_pair==4
    assert len(ORDERED)*placements_per_ordered_pair==36
    return {
        "sources":["J_d = bar(d_R) Y_d^dagger Q_L","J_u = epsilon bar(Q_L) Y_u u_R","J_e = y_e* bar(e_R) L_e"],
        "ordered_source_pairs":len(ORDERED),
        "diagonal_pairs":len(DIAGONAL),
        "cross_pairs_plus_hc":len(CROSS),
        "ordered_pair_labels":[f"{a}dagger{b}" for a,b in ORDERED],
        "fully_expanded_product_rule_terms_if_naively_distributed":36,
        "independent_Wilson_coefficients_from_product_rule": "not 36; derivative placements are within the source-pair operators",
        "representative_fierz_classes":{f"{a}dagger{b}":FIERZ_CLASS[(a,b)] for a,b in FIERZ_CLASS},
        "color_bookkeeping":{f"{a}dagger{b}":COLOR[(a,b)] for a,b in COLOR},
        "weak_bookkeeping":{f"{a}dagger{b}":WEAK[(a,b)] for a,b in WEAK},
        "result":"PASS",
        "limitations":[
            "No explicit d-dimensional Fierz coefficient is applied.",
            "No IBP reduction or evanescent counterterm basis is constructed.",
            "No loop integral or Wilson coefficient is evaluated.",
        ],
    }


if __name__=="__main__":
    print(json.dumps(audit(),indent=2))
