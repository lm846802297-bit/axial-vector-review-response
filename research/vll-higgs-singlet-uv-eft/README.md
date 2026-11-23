# RC-001: VLL–Higgs–Singlet UV–EFT matching

This is the migrated Phase 1 baseline for the VLL–Higgs–Singlet workstream. It is separate from the axial-vector supernova calculation and from the existing Major Point 1 review-response checks.

## Active material

- [RC-001 research record](research/RC-001-vll-higgs-singlet-uv-eft.md)
- [Claim–evidence matrix](research/RC-001-claim-evidence-matrix.md)
- [Gauge-subgraph record](research/RC-001-gauge-subgraph-change-record.md)
- `calculations/` and `validation/` preserve the individual scripts, tests and native outputs at the source pins.

The legacy [main source pin](https://github.com/lm846802297-bit/high-energy-theory-research/tree/b2dd8f7e4427d0292bc299d273c780c05021fdab) contributes 336 research, calculation and validation files and 3 inactive original workflow texts. The two unmerged candidates are independent, not accepted changes:

- `candidate-archive/pr-09/`: 49 RC-001-specific files from [PR #9](https://github.com/lm846802297-bit/high-energy-theory-research/pull/9), pinned at `e83d8a407baf91c11f5afc92d61e3d704980363f` (47 unique paths; 2 differing versions also on main).
- `candidate-archive/pr-14/`: 4 RC-001-specific files from [PR #14](https://github.com/lm846802297-bit/high-energy-theory-research/pull/14), pinned at `8b9796b22974900f1e3398e774aa0e7a8e59692c` (3 unique paths; 1 differing version also on main).

Each candidate is an overlay for an isolated copy of the pinned source baseline. Do not combine or overwrite candidate variants without a separate research decision. The [reference sidecar](provenance/local-reference-audit.json) lists cross-layer and retained legacy links rather than rewriting exact source files.

## Byte identity and archive scope

[The publication manifest](provenance/publication-manifest.jsonl) records origin path/commit, original blob ID and SHA-256, migrated bytes/mode and checksums, and any sanitation. Of the 392 copied origin files, 384 are byte-identical and 8 are derivatives limited to private Library IDs or the transient absolute output directory. No workflow was installed or enabled. The historical v66 build/archive payload is not duplicated in Phase 1. Its [138-member inventory](provenance/v66-source-inventory.jsonl) pins the exact original [archive](https://github.com/lm846802297-bit/high-energy-theory-research/tree/b2dd8f7e4427d0292bc299d273c780c05021fdab/artifacts/higgs-portal-v66-20261019). Private Library bytes are not part of the migrated source.

## Replay and limits

With Python and SymPy installed, from this directory:

```sh
python -m unittest discover -s candidate-archive/pr-14/calculations -p 'test*.py' -v
python candidate-archive/pr-09/calculations/RC-001-C5-soft-bubble-trace-audit.py
python -m unittest discover -s calculations -p 'test_RC001_dim6_WW_fivepoint_LD_W_06_shifted_Yukawa_singlet_charge_closure.py' -v
```

The #14 endpoint unit tests passed 3/3; the #9 SFT-01 replay passed 10 exact checks. The LD-W-06 module returned three passes and two `IndexError` errors in the available runtime, identically in the migrated and pristine pinned origin trees. The replay does not establish full longitudinal Ward closure, a complete hard-minus-soft matching, final Wilson coefficients, or the predicted physical scalar mixing. See [migration replay notes](provenance/migration-replay.md).
