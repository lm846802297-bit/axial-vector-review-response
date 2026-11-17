#!/usr/bin/env python3
"""Compare two gzipped width-scan CSVs without changing either archive."""
import argparse
import csv
import gzip
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

LOWER = 'fourmu_Gamma_over_sigma_lower_bound'
UPPER = 'fourmu_Gamma_over_sigma_upper_bound'


def digest(path, decompress=False):
    hasher = hashlib.sha256()
    size = 0
    opener = gzip.open if decompress else open
    with opener(path, 'rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            hasher.update(block)
            size += len(block)
    return {'sha256': hasher.hexdigest(), 'bytes': size}


def compare_archives(old_path, current_path):
    result = {
        'rows': 0, 'different_rows': 0, 'changed_columns': {},
        'old_lower_greater_count': 0, 'current_lower_greater_count': 0,
        'changed_bound_pairs': 0, 'exact_swapped_pairs': 0,
        'swapped_within_1e_minus_12': 0, 'max_relative_difference_from_swap': 0.0,
        'nonfinite_bound_rows': 0,
    }
    changes = Counter()
    with gzip.open(old_path, 'rt', encoding='utf-8', newline='') as old_stream, \
         gzip.open(current_path, 'rt', encoding='utf-8', newline='') as new_stream:
        old_reader, new_reader = csv.DictReader(old_stream), csv.DictReader(new_stream)
        if old_reader.fieldnames != new_reader.fieldnames or not {LOWER, UPPER}.issubset(old_reader.fieldnames or []):
            raise ValueError('CSV headers differ or required bound columns are missing')
        result['column_count'] = len(old_reader.fieldnames)
        for old, new in zip(old_reader, new_reader, strict=True):
            if None in old or None in new or any(v is None for v in old.values()) or any(v is None for v in new.values()):
                raise ValueError('Malformed CSV row')
            result['rows'] += 1
            changed = [key for key in old_reader.fieldnames if old[key] != new[key]]
            if changed:
                result['different_rows'] += 1
                changes.update(changed)
            before = (old[LOWER], old[UPPER])
            after = (new[LOWER], new[UPPER])
            if before != after:
                result['changed_bound_pairs'] += 1
                result['exact_swapped_pairs'] += before == after[::-1]
            try:
                values = tuple(map(float, before + after))
            except ValueError:
                result['nonfinite_bound_rows'] += 1
                continue
            if not all(map(math.isfinite, values)):
                result['nonfinite_bound_rows'] += 1
                continue
            a, b, c, d = values
            result['old_lower_greater_count'] += a > b
            result['current_lower_greater_count'] += c > d
            if before != after:
                relative = max(abs(a-d)/max(abs(a), abs(d), 1e-300),
                               abs(b-c)/max(abs(b), abs(c), 1e-300))
                result['max_relative_difference_from_swap'] = max(result['max_relative_difference_from_swap'], relative)
                result['swapped_within_1e_minus_12'] += relative < 1e-12
    result['changed_columns'] = dict(changes)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--old', required=True, type=Path)
    parser.add_argument('--current', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    result = compare_archives(args.old, args.current)
    result['old_archive'] = {'gzip': digest(args.old), 'csv': digest(args.old, decompress=True)}
    result['current_archive'] = {'gzip': digest(args.current), 'csv': digest(args.current, decompress=True)}
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
