#!/usr/bin/env python3
"""RC-001 B2c-IVn-h/06: LD-W-02 projector/order reconciliation.

Reduce the actual A-oriented fermion-WTI endpoints in the F-S open chain.
The single-W endpoint order is kept distinct from the graph-specific two-W
R_FG projection; only the chiral projector placement is reconciled here.
"""
from itertools import product
import sympy as sp

I=sp.I
ETA=(1,-1,-1,-1)
SIGMA=(
 sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),
 sp.Matrix([[1,0],[0,-1]])
)
GAMMA=[sp.diag(1,1,-1,-1)]
for sigma in SIGMA:
 GAMMA.append(sp.Matrix.vstack(
  sp.Matrix.hstack(sp.zeros(2),sigma),
  sp.Matrix.hstack(-sigma,sp.zeros(2))))
GAMMA5=I*GAMMA[0]*GAMMA[1]*GAMMA[2]*GAMMA[3]
PL=(sp.eye(4)-GAMMA5)/2
PR=(sp.eye(4)+GAMMA5)/2
GAMMA_DOWN=[ETA[mu]*GAMMA[mu] for mu in range(4)]


def slash(p):
 return sum((ETA[i]*p[i]*GAMMA[i] for i in range(4)),sp.zeros(4))


def dot(a,b):
 return sp.expand(sum(ETA[i]*a[i]*b[i] for i in range(4)))


def zero(m):
 return all(sp.simplify(m[i,j])==0 for i,j in product(range(4),repeat=2))


def verify_chiral_intertwining():
 r=list(sp.symbols("r0:4",real=True))
 checks=0
 for mu in range(4):
  assert zero(PL*GAMMA[mu]-GAMMA[mu]*PR)
  assert zero(PR*GAMMA[mu]-GAMMA[mu]*PL)
  checks+=2
 assert zero(PL*slash(r)-slash(r)*PR)
 assert zero(PR*slash(r)-slash(r)*PL)
 return checks+2


def rational_endpoint_projector_order():
 k=[5,1,2,0]; q=[0,1,1,2]
 p1=[1,1,0,1]; p2=[0,2,1,0]; p3=[2,0,1,1]
 p4=[-p1[i]-p2[i]-p3[i]-q[i] for i in range(4)]
 kap=[k[i]+q[i] for i in range(4)]
 r_aw=[k[i]-p1[i] for i in range(4)]
 r_ay=[r_aw[i]-q[i] for i in range(4)]
 h=[k[i]-p1[i]-p2[i] for i in range(4)]
 h_a=[h[i]-q[i] for i in range(4)]
 v_b=[-2*p3[i]-kap[i] for i in range(4)]
 # S_A^W=-slash(r_A^W)/r_AW^2; S_A^Y=-slash(r_A^Y)/r_AY^2.
 # The WTI RHS is S_A^W P_R - P_L S_A^Y.
 checks=0
 for mu in range(4):
  raw_w=GAMMA_DOWN[mu]*(-slash(r_aw))*PR*slash(h_a)*PL
  red_w=-GAMMA_DOWN[mu]*slash(r_aw)*slash(h_a)*PL
  raw_y=GAMMA_DOWN[mu]*PL*slash(r_ay)*slash(h_a)*PL
  red_y=GAMMA_DOWN[mu]*slash(r_ay)*slash(h_a)*PL
  assert zero(raw_w-red_w)
  assert zero(raw_y-red_y)
  checks+=32
 # The actual scalar-current contraction is on the right of the open chain.
 end_w=slash(v_b)*(-slash(r_aw))*slash(h_a)*PL
 end_y=slash(v_b)*slash(r_ay)*slash(h_a)*PL
 assert end_w!=end_y and end_w!=sp.zeros(4) and end_y!=sp.zeros(4)
 r_by=[kap[i]+p3[i] for i in range(4)]
 den=(dot(k,k),dot(kap,kap),dot(r_aw,r_aw),dot(r_ay,r_ay),
      dot(r_by,r_by),dot(h,h)-400,dot(h_a,h_a)-400)
 assert all(x!=0 for x in den)
 return checks,den,dot(v_b,k),dot(v_b,kap),end_w,end_y


def verify_RFG_is_separate():
 k=[5,1,2,0]; q=[0,1,1,2]; kap=[k[i]+q[i] for i in range(4)]
 p1=[1,1,0,1]; p2=[0,2,1,0]; p3=[2,0,1,1]
 p4=[-p1[i]-p2[i]-p3[i]-q[i] for i in range(4)]
 r_aw=[k[i]-p1[i] for i in range(4)]
 r_ay=[r_aw[i]-q[i] for i in range(4)]
 r_by=[k[i]+p4[i]+q[i] for i in range(4)]
 h=[k[i]-p1[i]-p2[i] for i in range(4)]
 h_a=[h[i]-q[i] for i in range(4)]
 v_b=[-2*p3[i]-kap[i] for i in range(4)]
 # Actual two-W R_FG numerator for the F-S graph.
 rfg=(dot(v_b,k)*slash(k)*(-slash(r_aw))*slash(h)
      -dot(v_b,kap)*slash(kap)*(-slash(r_aw))*slash(h))*PL
 # The contracted single-W endpoints have the scalar current at the left;
 # the oriented A-WTI fixes the relative signs and r_A^W/r_A^Y momenta.
 single_w=slash(v_b)*(-slash(r_aw))*slash(h_a)*PL
 single_y=slash(v_b)*slash(r_ay)*slash(h_a)*PL
 assert rfg!=sp.zeros(4) and single_w!=sp.zeros(4) and single_y!=sp.zeros(4)
 assert single_w!=single_y and rfg!=single_w and rfg!=single_y
 nz=lambda m:sum(sp.simplify(m[i,j])!=0 for i,j in product(range(4),repeat=2))
 return nz(rfg),nz(single_w),nz(single_y)


def main():
 c=verify_chiral_intertwining()
 checks,den,vk,vkap,ew,ey=rational_endpoint_projector_order()
 rfg,single_w,single_y=verify_RFG_is_separate()
 assert (c,checks,rfg,single_w,single_y)==(10,128,16,16,16)
 assert vk==-33 and vkap==-18
 print("RC-001 B2c-IVn-h/06: LD-W-02 projector/order reconciliation")
 print(f"PASS: gamma/projector intertwining ({c}/10 identities).")
 print(f"PASS: actual A-WTI endpoint reductions ({checks}/128 matrix entries).")
 print("PASS: the two endpoints share rightmost P_L and ordered gamma_mu slash(r_A) slash(h_A),")
 print("      while retaining distinct r_A^W and r_A^Y momenta.")
 print(f"PASS: R_FG and both distinct single-W endpoint numerators remain separate ({rfg}/16, {single_w}/16, {single_y}/16 nonzero entries).")
 print(f"RATIONAL V_B DOTS: V_B(kappa).k={vk}, V_B(kappa).kappa={vkap}.")
 print(f"RATIONAL DENOMINATORS: {den}.")
 print("BOUNDARY: projector placement is reconciled; no equality of single-W endpoints")
 print("          and the two-W R_FG projection is asserted.")
 print("          No complete matter/scalar/three-W/LSZ/ST sum or Wilson coefficient is claimed.")


if __name__=="__main__":
 main()
