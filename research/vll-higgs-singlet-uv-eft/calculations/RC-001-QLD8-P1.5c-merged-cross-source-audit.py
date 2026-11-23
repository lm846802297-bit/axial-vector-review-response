#!/usr/bin/env python3
import sympy as s
D,e=s.symbols("D epsilon")
Fss=(D**2+10*D-8)/48; Fts=(D+8)/12; Fst=-(D+8)/6
assert s.simplify(Fss.subs(D,4-2*e)-(1-s.Rational(3,4)*e+e**2/12))==0
assert s.simplify(Fts.subs(D,4-2*e)-(1-e/6))==0
assert s.simplify(Fst.subs(D,4-2*e)-(-2+e/3))==0
eta=[1,-1,-1,-1]
p1=s.Matrix(s.symbols("p10:14")); p2=s.Matrix(s.symbols("p20:24")); p3=s.Matrix(s.symbols("p30:34")); p4=-p1-p2-p3
dot=lambda a,b:s.expand(sum(eta[k]*a[k]*b[k] for k in range(4)))
q=p1+p2; d=p1-p2; R=p3-p4
assert s.simplify(dot(d,R)-(dot(p1,p1)-dot(p2,p2)+2*dot(p1,p3)-2*dot(p2,p3)))==0
wedge=lambda a,b:s.Matrix([s.expand(a[i]*b[j]-a[j]*b[i]) for i in range(4) for j in range(i+1,4)])
assert s.simplify(wedge(q,p4-p3)+2*wedge(q,p3))==s.zeros(6,1)
assert s.simplify(wedge(q,p3)-wedge(p1,p3)-wedge(p2,p3))==s.zeros(6,1)
assert s.Matrix.hstack(wedge(q,p4-p3),wedge(p1,p2)).rank()==2
J=s.zeros(4); J0=s.zeros(4); J1=s.zeros(4)
G=(D*(dot(d,d)+dot(R,R))+(D-20)*dot(q,q))/48
G0=(dot(d,d)+dot(R,R)-4*dot(q,q))/12
G1=-(dot(d,d)+dot(R,R)+dot(q,q))/24
for a in range(4):
 for b in range(4):
  g=s.Integer(eta[a] if a==b else 0)
  J[a,b]=D*(d[a]*d[b]+R[a]*R[b])/24-(D+12)*q[a]*q[b]/24+g*G
  J0[a,b]=(d[a]*d[b]+R[a]*R[b])/6-s.Rational(2,3)*q[a]*q[b]+g*G0
  J1[a,b]=-(d[a]*d[b]+R[a]*R[b])/12+q[a]*q[b]/12+g*G1
assert s.simplify(J-J.T)==s.zeros(4)
Je=J.subs(D,4-2*e).applyfunc(lambda x:s.series(x,e,0,2).removeO())
assert s.simplify(Je-J0-e*J1)==s.zeros(4)
color=[-1,1,1,-1]
assert [a*b for a,b in zip(color,[1,1,1,1])]==[-1,1,1,-1]
assert [a*b for a,b in zip(color,[-1,-1,1,1])]==[1,-1,1,-1]
assert [a*b for a,b in zip(color,[-1,1,-1,1])]==[1,1,-1,-1]
assert [a*b for a,b in zip(color,[-1,1,1,-1])]==[1,1,1,1]
assert sum(color)==0
print("PASS: exact SS/TS/ST coefficients and D=4-2epsilon expansions")
print("PASS: scalar momentum polynomial and mixed wedge reduction")
print("PASS: mixed wedge structures are independent (rank 2)")
print("PASS: exact symmetric D-dimensional TT tensor and O(epsilon) expansion")
print("PASS: SS/TS/ST/TT signs and zero direct-singlet color projection")
print("LIMIT: no Fierz, EOM/IBP, R* subtraction, external-gluon completion, or Z matrix")
