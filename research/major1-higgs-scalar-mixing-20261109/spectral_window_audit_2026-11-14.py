#!/usr/bin/env python3
"""Compare the archived spectral-area integral to its stated mass window."""
from coherent_two_pole_spectral_area import area_ratio, d_hh, d_sm, MH
from scipy.integrate import quad

def restricted_ratio(ms, vs, ma):
    lo, hi = 124.5, 126.0
    points = {lo, hi}
    for center in (MH, ms):
        if lo < center < hi:
            points.add(center)
        for dx in (1e-5, 2e-5, 5e-5, 1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3, .01, .03, .1, .3):
            for sign in (-1, 1):
                x = center + sign * dx
                if lo < x < hi:
                    points.add(x)
    points = sorted(points)
    def integrate(f):
        return sum(quad(f, a, b, epsabs=1e-10, epsrel=1e-7, limit=300)[0]
                   for a, b in zip(points[:-1], points[1:]))
    return integrate(lambda x: abs(d_hh(x, ms, vs, ma))**2) / integrate(lambda x: abs(d_sm(x))**2)

if __name__ == "__main__":
    print("benchmark,ms_GeV,archived_ratio,restricted_ratio,difference")
    for name, vs, ma in (("A", 70.886458, 10.), ("B", 315., 63.)):
        for ms in (100., 125.25, 150.):
            old = area_ratio(ms, vs, ma)
            new = restricted_ratio(ms, vs, ma)
            print(f"{name},{ms:.2f},{old:.12f},{new:.12f},{new-old:.12g}")
