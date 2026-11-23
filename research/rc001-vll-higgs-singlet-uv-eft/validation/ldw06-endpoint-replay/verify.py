#!/usr/bin/env python3
"""Check all replay gates and emit a deterministic report without raw paths."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
import sympy
from replay import DEFAULT_FROZEN, HERE, ORIGINAL, SOURCE, derivative, verify_archive
from test_signed_route import HA, HB, H0, Q, denominator, plus, vec

BASE = "89cd043984012215f74ae331049a626badea9d57"
EXPECTED_INDEXERRORS = [
    "test_A_and_B_secondary_heavy_channels", "test_main_preserves_LSZ_boundary"
]


def collect(args):
    return subprocess.run([sys.executable, *args], cwd=HERE, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, text=True, check=False)


def test_status(text):
    return dict(re.findall(r"(?m)^(test_\w+) \([^\n()]+\) \.\.\. (ok|ERROR|FAIL)$", text))


def verify():
    verify_archive(DEFAULT_FROZEN)
    commands = [
        ["-B","replay.py","--variant","pristine"],
        ["-B","replay.py","--variant","corrected"],
        ["-B","-m","unittest","-v","test_signed_route"],
    ]
    pristine, derived, independent = map(collect, commands)
    ps,ds,ss=map(test_status,(pristine.stdout,derived.stdout,independent.stdout))
    if not (pristine.returncode==1 and len(ps)==5
            and [k for k,v in ps.items() if v=="ERROR"]==EXPECTED_INDEXERRORS
            and list(ps.values()).count("ok")==3
            and re.findall(r"(?m)^IndexError: (.+)$",pristine.stdout)==["list index out of range"]*2):
        raise RuntimeError("Unexpected pristine regression outcome")
    scope_markers=["A-side bar-L/H endpoint variations share h-q (8/4+4 vector components)",
                   "B-side Hdagger/L endpoint variations share h+q (8/4+4 vector components)",
                   "96/96 weak components", "does not cancel the full scalar-line/three-W integrand",
                   "No complete STI or Wilson coefficient is claimed."]
    if not (derived.returncode==0 and set(ds)==set(ps)
            and set(ds.values())=={"ok"} and all(t in derived.stdout for t in scope_markers)):
        raise RuntimeError("Temporary derivative did not pass original suite and entry-point gates")
    if not (independent.returncode==0 and len(ss)==3 and set(ss.values())=={"ok"}):
        raise RuntimeError("Independent routing test gate did not pass")
    momenta=((6,1,0,1),(1,1,0,0),(1,0,1,0),(0,2,0,1))
    arch=[denominator(vec(p,momenta),400) for p in (H0,HB,HA)]
    ends=[denominator(vec(p,momenta),400) for p in (plus(HA,Q,-1),plus(HB,Q,1))]
    temporary=derivative((DEFAULT_FROZEN/SOURCE).read_bytes())
    return {
        "scope":"LD-W-06 local endpoint test reproducibility only; no CI or full STI/Wilson claim.",
        "target_main_input_commit":BASE,
        "runtime":{"python":platform.python_version(),"sympy":sympy.__version__},
        "commands":[["python",*c] for c in commands],
        "input_sha256":ORIGINAL,
        "temporary_derivative_sha256":hashlib.sha256(temporary).hexdigest(),
        "patch_sha256":hashlib.sha256((HERE/"SYMBOL_REPAIR.patch").read_bytes()).hexdigest(),
        "pristine":{"exit":pristine.returncode,"test_cases":ps,"errors":[
            {"test":t,"exception":"IndexError","message":"list index out of range"} for t in EXPECTED_INDEXERRORS]},
        "corrected":{"exit":derived.returncode,"test_cases":ds,"route_checks_each_side":8,"weak_index_checks":96},
        "independent":{"exit":independent.returncode,"test_cases":ss},
        "rational_diagnostic":{"anchor_order":["h0","h0-q","h0+q"],"anchor_denominators":arch,
                               "common_endpoint_order":["hA-q","hB+q"],"endpoint_denominators":ends},
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output",type=Path,help="Path to the generated JSON report")
    out=parser.parse_args().output
    out.write_text(json.dumps(verify(),indent=2,sort_keys=True,allow_nan=False)+"\n",encoding="utf-8")
