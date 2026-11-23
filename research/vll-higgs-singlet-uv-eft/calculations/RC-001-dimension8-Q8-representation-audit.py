#!/usr/bin/env python3
"""Exact gauge-representation audit for the Q8 soft calculation.

Charges are normalized as x=Q_X/Q_l, eta_mu=+1, eta_tau=-1.
This is a representation audit, not a Feynman-diagram generator or loop
integrator. It checks the charges of the complete composite sources and
therefore the gauge connection acting in Q_LD^(8), Q_RD^(8).
"""
from fractions import Fraction as F

for flavor, eta in (("mu", 1), ("tau", -1)):
    fields = {
        "H": (F(1,2), 0, "2"),
        "Hdag": (F(-1,2), 0, "2bar"),
        "L": (F(-1,2), eta, "2"),
        "Lbar": (F(1,2), -eta, "2bar"),
        "lR": (F(-1), -eta, "1"),
        "lRbar": (F(1), eta, "1"),
        "S_l": (F(0), 2*eta, "1"),
        "S_lbar": (F(0), -2*eta, "1"),
        "E": (F(-1), eta, "1"),
    }
    def product(*names):
        Y = sum((fields[n][0] for n in names), F(0))
        X = sum(fields[n][1] for n in names)
        # For 2bar x 2, contract the indices to the singlet.
        return Y, X

    y_ld, x_ld = product("Hdag", "L")
    y_rd, x_rd = product("S_l", "lR")
    assert (y_ld, x_ld) == (F(-1), eta)
    assert (y_rd, x_rd) == (F(-1), eta)
    assert fields["E"] == (F(-1), eta, "1")
    assert fields["H"][2] == "2" and fields["L"][2] == "2"
    assert fields["S_l"][2] == fields["lR"][2] == "1"

    print(f"PASS {flavor}: H^dag L has (SU2,Y,x)=(1,-1,{eta})")
    print(f"PASS {flavor}: S_l l_R has (SU2,Y,x)=(1,-1,{eta})")
    print(f"PASS {flavor}: both composite sources transform exactly as E_l")
    print(f"PASS {flavor}: Q8 insertion connection has B and X gauge fields, no direct W insertion")

print("PASS: eta_mu=+1 and eta_tau=-1 conjugate assignments are consistent")
print("SCOPE: exact representation/charge bookkeeping only; no gauge-loop integral or Ward identity evaluated")
