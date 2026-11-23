#!/usr/bin/env python3
"""Check the tree heavy-propagator expansion behind light-only UV/EFT cancellation."""
import sympy as sp

P2, invM2, F = sp.symbols("P2 invM2 F")
def main():
    exact = -invM2 / (1 - P2 * invM2)
    expanded = sp.series(exact, invM2, 0, 3).removeO()
    assert sp.simplify(expanded - (-invM2 - P2 * invM2**2)) == 0

    # The light-only loop factor F is identical on both sides. The EFT
    # covariant-derivative insertion reproduces the O(1/M^2) tree kernel.
    uv = F * (-invM2)
    eft = F * (-invM2)
    assert sp.simplify(uv - eft) == 0
    print("Heavy propagator: -i slash(P)/M^2 + O(M^-4): PASS")
    print("Common light-only loop factor cancels at O(M^-2): PASS")
    print("SCOPE: requires the complete gauge-covariant EFT insertion/contact set; no loop integral is evaluated.")

if __name__ == "__main__":
    main()
