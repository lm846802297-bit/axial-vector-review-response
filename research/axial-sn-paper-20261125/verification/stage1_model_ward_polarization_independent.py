import math
import numpy as np

M=105.6583755
I2=np.eye(2,dtype=complex); Z2=np.zeros((2,2),complex)
SIGMA=(np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex))
G=[np.block([[I2,Z2],[Z2,-I2]])]
for s in SIGMA: G.append(np.block([[Z2,s],[-s,Z2]]))
G=np.array(G)
G5=1j*G[0]@G[1]@G[2]@G[3]
I4=np.eye(4,dtype=complex)
MET=np.array([1.,-1.,-1.,-1.])

def slash(v): return np.einsum('a,aij->ij',np.asarray(v)*MET,G)
def spinor(p,m,s):
    chi=np.zeros(2,complex); chi[s]=1
    sp=sum(SIGMA[i]*p[i+1] for i in range(3))
    return math.sqrt(p[0]+m)*np.r_[chi,sp@chi/(p[0]+m)]
def ubar(u): return u.conj().T@G[0]
def kin(eg,ma,c,m=M):
    if eg < ma+ma*ma/(2*m): raise ValueError('below threshold')
    p=np.array([m,0.,0.,0.]); k=np.array([eg,0.,0.,eg])
    a=m+eg; b=eg*c; d=m*eg+ma*ma/2
    disc=d*d-(a*a-b*b)*ma*ma
    if disc < -1e-10*max(d*d,1): raise ValueError('no root')
    eq=(a*d+b*math.sqrt(max(disc,0)))/(a*a-b*b)
    qabs=math.sqrt(max(eq*eq-ma*ma,0))
    q=np.array([eq,qabs*math.sqrt(max(1-c*c,0)),0.,qabs*c])
    pp=p+k-q
    return p,k,pp,q
def amp(p,k,pp,q,m,egam,ex,gv,ga):
    s=(p[0]+k[0])**2-np.dot(p[1:]+k[1:],p[1:]+k[1:])
    r=p-q; u=r[0]**2-np.dot(r[1:],r[1:])
    ps=(slash(p+k)+m*I4)/(s-m*m)
    pu=(slash(r)+m*I4)/(u-m*m)
    vx=slash(ex)@(gv*I4-ga*G5)
    vg=slash(egam)
    return vx@ps@vg+vg@pu@vx
def pamp(p,k,pp,q,m,egam):
    s=(p[0]+k[0])**2-np.dot(p[1:]+k[1:],p[1:]+k[1:])
    r=p-q; u=r[0]**2-np.dot(r[1:],r[1:])
    ps=(slash(p+k)+m*I4)/(s-m*m)
    pu=(slash(r)+m*I4)/(u-m*m)
    vg=slash(egam)
    return G5@ps@vg+vg@pu@G5
def pols(q,ma):
    v=q[1:]; n=v/np.linalg.norm(v) if np.linalg.norm(v)>0 else np.array([0.,0.,1.])
    ref=np.array([0.,1.,0.]) if abs(n[1])<.9 else np.array([1.,0.,0.])
    e1=np.cross(ref,n); e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
    return [np.r_[0.,e1],np.r_[0.,e2],np.r_[np.linalg.norm(v)/ma,q[0]*n/ma]]
def rel(a,b): return abs(a-b)/max(abs(a),abs(b),1e-300)
def prop(r,m):
    return (slash(r)+m*I4)/(r[0]**2-np.dot(r[1:],r[1:])-m*m)
def photon_basis(photon):
    n=np.asarray(photon[1:],float); n=n/np.linalg.norm(n)
    ref=np.array([0.,1.,0.])
    if abs(np.dot(ref,n))>.9: ref=np.array([1.,0.,0.])
    e1=np.cross(ref,n); e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
    return (np.r_[0.,e1],np.r_[0.,e2])
def v_spinor(p,m,s):
    C=1j*G[2]@G[0]
    return C@ubar(spinor(p,m,s)).T
def electron_amplitude(pi,pf,k,q,m,eg,ex,gv,ga):
    GA=slash(ex)@(gv*I4+ga*G5); GG=slash(eg)
    return GA@prop(pi+k,m)@GG+GG@prop(pi-q,m)@GA
def positron_amplitude(pi,pf,k,q,m,eg,ex,gv,ga):
    GA=slash(ex)@(gv*I4+ga*G5); GG=slash(eg)
    return GG@prop(-pi-k,m)@GA+GA@prop(-pi+q,m)@GG

bench=[(10.,2.,.3),(1.,.1,-.5),(200.,50.,.8),(1.,.5,.1),(30.,10.,-.9)]
ward=[]; photon=[]; shell=[]; polnorm=[]; polorth=[]; gold=[]; eqtest=[]
for eg,ma,c in bench:
    p,k,pp,q=kin(eg,ma,c)
    shell.append(abs(pp[0]**2-np.dot(pp[1:],pp[1:])-M*M)/M**2)
    for ep in (np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.])):
        A=amp(p,k,pp,q,M,ep,q,0.,1.)
        P=pamp(p,k,pp,q,M,ep)
        for si in range(2):
            ui=spinor(p,M,si)
            for sf in range(2):
                uf=spinor(pp,M,sf); lhs=ubar(uf)@A@ui; rhs=2*M*(ubar(uf)@P@ui)
                gold.append(rel(lhs,rhs))
    for gv,ga in [(1.,0.),(0.,1.),(.2,-.9)]:
        for ex in pols(q,ma):
            A=amp(p,k,pp,q,M,k,ex,gv,ga)
            for si in range(2):
                ui=spinor(p,M,si)
                for sf in range(2):
                    uf=spinor(pp,M,sf); photon.append(abs(ubar(uf)@A@ui))
    es=pols(q,ma)
    for i,e in enumerate(es):
        polnorm.append(abs(np.dot(e*MET,e)+1))
        for j,f in enumerate(es):
            if i!=j: polorth.append(abs(np.dot(e*MET,f)))
    eL=es[2]
    for ep in (np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.])):
        AL=amp(p,k,pp,q,M,ep,eL,0.,1.)
        AQ=amp(p,k,pp,q,M,ep,q/ma,0.,1.)
        for si in range(2):
            ui=spinor(p,M,si)
            for sf in range(2):
                uf=spinor(pp,M,sf)
                eqtest.append(rel(ubar(uf)@AL@ui,ubar(uf)@AQ@ui))
print('environment numpy',np.__version__)
print('benchmarks',bench)
print('max_shell_rel',max(shell))
print('max_goldstone_ward_rel',max(gold))
print('max_photon_ward_abs_amplitude',max(photon))
print('max_pol_norm_resid',max(polnorm))
print('max_pol_orth_resid',max(polorth))
map_res=[]
for gx,vs,ml,theta in [(0.02,100.,M,0.),(0.1,1000.,M,1e-2),(0.07,315.,1776.86,1e-2)]:
    ma=2*gx*vs; ga=-gx*math.cos(theta)**2
    y_gold=math.cos(theta)**2*ml/vs
    y_ward=2*abs(ga)*ml/ma
    map_res.append(rel(y_gold,y_ward))
print('finite_mixing_goldstone_map_resid',map_res)
print('goldstone_equivalence_epsL_vs_q_over_m_rel_by_benchmark')
for i in range(0,len(eqtest),8): print(bench[i//8],max(eqtest[i:i+8]))

comp_res=[]; photon_rel=[]; vector_shift=[]
for eg,ma,c in bench:
    p,k,pp,q=kin(eg,ma,c); es=pols(q,ma)
    lhs=sum(np.outer(e,e.conj()) for e in es)
    rhs=-np.diag(MET)+np.outer(q,q)/ma**2
    comp_res.append(np.max(np.abs(lhs-rhs)))
    for gv,ga in [(1.,0.),(0.,1.),(.2,-.9)]:
        for ex in es:
            for si in range(2):
                ui=spinor(p,M,si)
                for sf in range(2):
                    uf=spinor(pp,M,sf)
                    phys=max(abs(ubar(uf)@amp(p,k,pp,q,M,ep,ex,gv,ga)@ui)
                             for ep in (np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.])))
                    ward=abs(ubar(uf)@amp(p,k,pp,q,M,k,ex,gv,ga)@ui)
                    photon_rel.append(ward/max(phys,1e-300))
    eL=es[2]; eV=eL-q/ma
    for ep in (np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.])):
        A1=amp(p,k,pp,q,M,ep,eL,1.,0.)
        A2=amp(p,k,pp,q,M,ep,eV,1.,0.)
        for si in range(2):
            ui=spinor(p,M,si)
            for sf in range(2):
                uf=spinor(pp,M,sf)
                vector_shift.append(rel(ubar(uf)@A1@ui,ubar(uf)@A2@ui))
print('max_polarization_completeness_abs_residual',max(comp_res))
print('max_photon_ward_relative_residual',max(photon_rel))
print('max_vector_longitudinal_shift_relative_residual',max(vector_shift))
for eg in (10.,100.,1000.,10000.):
    ma=1.; c=.3
    p,k,pp,q=kin(eg,ma,c); eL=pols(q,ma)[2]
    ep=np.array([0.,1.,0.,0.])
    AL=amp(p,k,pp,q,M,ep,eL,0.,1.)
    AQ=amp(p,k,pp,q,M,ep,q/ma,0.,1.)
    vals=[]
    for si in range(2):
        ui=spinor(p,M,si)
        for sf in range(2):
            uf=spinor(pp,M,sf); vals.append(rel(ubar(uf)@AL@ui,ubar(uf)@AQ@ui))
    print('equiv_Egamma_over_ma',eg/ma,'EA_over_ma',q[0]/ma,'max_amp_rel',max(vals))

C=1j*G[2]@G[0]
def fermion_propagator(r,m):
    den=r[0]**2-np.dot(r[1:],r[1:])-m*m
    return (slash(r)+m*I4)/den
vspinor_residuals=[]; vspinor_rows=[]
vpoints=[(10.,2.,.3),(1.,.1,-.5),(200.,50.,.8),(30.,10.,-.9),(100.,.01,.6)]
for eg,ma,c in vpoints:
    target,photon,pf,q=kin(eg,ma,c); pi,pfout=pf,target
    e1,e2,eL=pols(q,ma)
    modes=(eL,(e1+1j*e2)/math.sqrt(2),(e1-1j*e2)/math.sqrt(2))
    gamma_modes=photon_basis(photon)
    for label,gv,ga in [('vector',1.,0.),('axial',0.,1.),('mixed',.2,-.9)]:
        direct=[]; mapped=[]
        for ex in modes:
            sd=sm=0.
            for ep in gamma_modes:
                Mp=positron_amplitude(pi,pfout,photon,q,M,ep,ex,gv,ga)
                Mm=electron_amplitude(pi,pfout,photon,q,M,ep,ex,gv,-ga)
                for si in range(2):
                    vi=v_spinor(pi,M,si); ui=spinor(pi,M,si)
                    for sf in range(2):
                        vf=v_spinor(pfout,M,sf); uf=spinor(pfout,M,sf)
                        sd+=abs(ubar(vi)@Mp@vf)**2/2
                        sm+=abs(ubar(uf)@Mm@ui)**2/2
            direct.append(sd); mapped.append(sm)
        direct=np.asarray(direct); mapped=np.asarray(mapped)
        residual=float(np.max(np.abs(direct-mapped)/np.maximum(np.maximum(abs(direct),abs(mapped)),1e-300)))
        vspinor_residuals.append(residual)
        vspinor_rows.append((eg,ma,c,label,direct.tolist(),mapped.tolist(),residual))
print('max_direct_v_spinor_vs_u_charge_map_relative_residual',max(vspinor_residuals))
for row in vspinor_rows: print('vspinor_case',row)
pcheck=np.array([math.hypot(M,73.),73.,0.,0.])
veq=[]; vnorm=[]
for s in range(2):
    v=v_spinor(pcheck,M,s)
    veq.append(np.linalg.norm((slash(pcheck)+M*I4)@v))
    vnorm.append(ubar(v)@v)
print('max_v_dirac_equation_norm',max(veq))
print('vbar_v',vnorm)
for eg,c in ((100.,.8),(1000.,.8),(1000.,.99)):
    ma=1.; p,k,pp,q=kin(eg,ma,c); eL=pols(q,ma)[2]
    sum_l=0.; sum_q=0.
    for ep in (np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.])):
        ml=amp(p,k,pp,q,M,ep,eL,0.,1.)
        mq=amp(p,k,pp,q,M,ep,q/ma,0.,1.)
        for si in range(2):
            ui=spinor(p,M,si)
            for sf in range(2):
                uf=spinor(pp,M,sf)
                sum_l+=abs(ubar(uf)@ml@ui)**2
                sum_q+=abs(ubar(uf)@mq@ui)**2
    print('goldstone_limit_EA_over_ma',q[0]/ma,'spin_pol_sum_rel',abs(sum_l-sum_q)/max(sum_l,sum_q,1e-300))
seesaw_map_res=[]
for mL,mR,ME,vs,gx in ((10.,5.,20000.,1000.,.02),(20.,100.,20000.,315.,.07),(40.,80.,1000.,500.,.03)):
    mass_matrix=np.array([[0.,mL],[mR,ME]])
    UL,svals,Vh=np.linalg.svd(mass_matrix)
    idx=int(np.argmin(svals)); ml=float(svals[idx])
    uL=UL[:,idx]; uR=Vh.T[:,idx]
    thetaR=math.atan2(abs(uR[1]),abs(uR[0]))
    y_phase=(mR/vs)*abs(uL[1])*abs(uR[0])
    ma=2*gx*vs; gA=-gx*math.cos(thetaR)**2
    y_ward=2*abs(gA)*ml/ma
    seesaw_map_res.append(rel(y_phase,y_ward))
print('exact_seesaw_goldstone_vs_ward_map_residuals',seesaw_map_res)
