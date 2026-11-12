# C4-C4-B source and input provenance

- Profile Git blob SHA: 9ff7818b0679992c0a9ba402330ec7f0d1f3041b
- C2 occupation Git blob SHA: c472040a4551e68ffadbf7addf9402663f99e7e3
- C4-C3 100-MeV 301x4 baseline Git blob SHA: 2b060ffa863430c6e35a1355d0316c1d1c0b4c7c
- C4-C4-A 96-row anchor archive Git blob SHA: 8be3757cf28011132a82b5c2373aa3c1fa59d342
- C4-B2 effective-mass kernel blob SHA: 97a2706e978cd22f7ebc08c1f87ce6abd97ad0a7
- C4-C1 exact support blob SHA: 8f7291be8738e0273353a8c30039c6be1ed8e6a9
- C4-C2 full-angle integrator blob SHA: 2912788345e482e52308e02e6cbbc87c734a18b0
- Reused C4-C3 Numba accelerator source blob SHA: 821e39edfe235f5a8fcac6b2e074bb0dcb9631c6

The C4-C3 100-MeV rates are reused, not recalculated. The C4-C4-A anchor archive is an independent unaccelerated reference for the four anchor radii. The Numba accelerator changes only the innermost Dirac-matrix contraction; it does not change phase-space support, Fermi factors, weak form factors, or quadrature nodes.
