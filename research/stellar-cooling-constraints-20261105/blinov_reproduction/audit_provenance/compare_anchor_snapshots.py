#!/usr/bin/env python3
"""Compare the pinned C4-C4-A anchor with the current archived table."""
import csv
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
old = HERE / 'c4c4_anchor_original_8be3757.csv'
current = BASE / 'outputs/c4c4_energy_dependence_2026-11-12/local_rates_96.csv'


def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def rows(path):
    with path.open(newline='', encoding='utf8') as f:
        return list(csv.DictReader(f))


a, b = rows(old), rows(current)
assert len(a) == len(b) == 96
assert a[0].keys() == b[0].keys()
keys = ('E_MeV', 'r_km', 'species', 'antinu')
changed, cols, max_rel = 0, {}, 0.0
for x, y in zip(a, b):
    assert all(x[k] == y[k] for k in keys)
    if x != y:
        changed += 1
    for k in x:
        if x[k] != y[k]:
            cols[k] = cols.get(k, 0) + 1
            v, w = float(x[k]), float(y[k])
            assert w != 0
            max_rel = max(max_rel, abs(v / w - 1))
assert blob(old) == '8be3757cf28011132a82b5c2373aa3c1fa59d342'
assert blob(current) == 'f5d8303fba5fc53de2e8bdd14c9feed40ff6a197'
print(json.dumps({'rows': len(a), 'changed_rows': changed, 'changed_columns': cols,
                  'max_relative_difference': max_rel, 'old_blob': blob(old),
                  'current_blob': blob(current),
                  'old_sha256': hashlib.sha256(old.read_bytes()).hexdigest()}, indent=2))
