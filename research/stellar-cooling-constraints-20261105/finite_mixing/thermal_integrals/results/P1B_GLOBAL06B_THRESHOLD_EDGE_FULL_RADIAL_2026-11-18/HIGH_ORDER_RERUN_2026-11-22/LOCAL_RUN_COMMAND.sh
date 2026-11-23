#!/bin/bash
set -euo pipefail
cd /mnt/data/b13-independent-rerun-20261122/source
DRIVER=finite_mixing/thermal_integrals/run_p1b_global06b_threshold_edge_high_order_targets.py
TARGET=finite_mixing/thermal_integrals/results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_TARGETS_INPUT.json
PROFILE=data/sfho188_digitized.csv
RUN=/mnt/data/b13-independent-rerun-20261122
python3 "$DRIVER" --targets "$TARGET" --profile "$PROFILE" --output "$RUN/results" --workers 4
