# LD-W-06 local endpoint replay

This validation-only replay leaves the [frozen shifted-Yukawa source](../../upstream/calculations/RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.py) and its [five archive tests](../../upstream/calculations/test_RC001_dim6_WW_fivepoint_LD_W_06_shifted_Yukawa_singlet_charge_closure.py) unchanged. It verifies their exact hashes against target main `89cd043984012215f74ae331049a626badea9d57` before making a temporary derivative. The source/test Git blobs are `2f9f45641dba1dfcce8f803fda162e6c928a3232` and `c9d58820e1691b99ab4a384b96e9d4a5e830b3b6`.

In SymPy 1.14.0, `symbols("p10:4")` and `symbols("p20:4")` return empty tuples. Two of the five pristine tests reach the same out-of-range access. The [two-line change](SYMBOL_REPAIR.patch) explicitly creates four separate symbols for each external vector in the temporary copy only. All five unmodified archival tests then pass, as do the entry point and the three independent routing tests. [verification.json](verification.json) records the observed test statuses and versions; it contains no raw traceback or temporary paths. This is a local rerun on Python 3.12.14 and SymPy 1.14.0, not CI.

With $h_0=k-p_1-p_2$, $h_A=h_0+q$, and $h_B=h_0-q$, the common endpoint routes are $h_A-q=h_B+q=h_0$. At the archived rational point, $(-377,-389,-365)$ are the separate Minkowski denominators of $(h_0,h_0-q,h_0+q)$; the actual two endpoint denominators are both $-377$. The independent check rejects either wrong shift sign. This establishes a local reproducible test, not a full scalar-line/three-W or reducible LSZ cancellation, STI closure, or Wilson coefficient.

## Replay

From this directory in the target checkout:

```sh
sha256sum -c SHA256SUMS
python -B verify.py /tmp/ldw06-verification-replay.json
cmp verification.json /tmp/ldw06-verification-replay.json
```

`verify.py` checks the expected pristine failure, the repaired archived suite and entry point, and the independent signed routing tests. It checks the canonical inputs at `../../upstream/calculations/`; no archive files are duplicated here. The exact output is reproducible on the recorded runtime. See [task brief](TASK_BRIEF.md) for scope and conventions.
