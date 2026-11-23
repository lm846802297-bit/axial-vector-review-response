#!/usr/bin/env python3
"""Run frozen LD-W-06 source/tests with a pinned, temporary symbol repair."""
from pathlib import Path
import argparse
import hashlib
import platform
import subprocess
import sys
import tempfile

SOURCE = 'RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.py'
TEST = 'test_RC001_dim6_WW_fivepoint_LD_W_06_shifted_Yukawa_singlet_charge_closure.py'
ORIGINAL = {
    SOURCE:'15e6cf120beec06798feae6e6e14354d996f6271a736569d9eacf847ca4d57b8',
    TEST:'bf929a15995356584c3a367deb5a841e1c53a63feb55b149138b4ec3c66936ab',
}
HERE=Path(__file__).resolve().parent
DEFAULT_FROZEN=(HERE/"../../upstream/calculations").resolve()


def verify_archive(root):
    for name,expected in ORIGINAL.items():
        body=(root/name).read_bytes()
        if hashlib.sha256(body).hexdigest()!=expected:
            raise ValueError(f"Archive identity mismatch for {name}")


def derivative(source):
    for family in (b"p1",b"p2"):
        old=b'list(sp.symbols("'+family+b'0:4", real=True))'
        new=b'[sp.Symbol(f"'+family+b'_{i}", real=True) for i in range(4)]'
        if source.count(old)!=1:
            raise ValueError("Unexpected token count")
        source=source.replace(old,new,1)
    return source


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--frozen',type=Path,default=DEFAULT_FROZEN)
    p.add_argument('--variant',choices=('pristine','corrected'),default='corrected')
    a=p.parse_args()
    verify_archive(a.frozen)
    import sympy
    print(f"Python {platform.python_version()}, SymPy {sympy.__version__}",flush=True)
    with tempfile.TemporaryDirectory() as d:
        d=Path(d)
        source=(a.frozen/SOURCE).read_bytes()
        if a.variant=='corrected':
            source=derivative(source)
        print("executed source sha256="+hashlib.sha256(source).hexdigest(),flush=True)
        (d/SOURCE).write_bytes(source)
        (d/TEST).write_bytes((a.frozen/TEST).read_bytes())
        exitcode=subprocess.call([sys.executable,'-B',str(d/TEST)])
        print(f"archive tests exit={exitcode}",flush=True)
        if exitcode:
            return exitcode
        return subprocess.call([sys.executable,'-B',str(d/SOURCE)])
if __name__=='__main__':
    raise SystemExit(main())
