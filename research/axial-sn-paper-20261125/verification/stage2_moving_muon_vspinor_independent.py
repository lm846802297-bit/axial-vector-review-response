import math
import numpy as np

M=105.6583755
I2=np.eye(2,dtype=complex); Z2=np.zeros((2,2),complex)
SIGMA=(np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex))
G=[np.block([[I2,Z2],[Z2,-I2]])]
for s in SIGMA: G.append(np.block([[Z2,s],[-s,Z2]]))
G=np.array(G)
G5=1j*G[0]@G[1]@G[2]@G[3]
I4=np.eye(4,dtype=complex); MET=np.array([1.,-1.,-1.,-1.])
C=1j*G[2]@G[0]
def slash(v): return np.einsum('a,aij->ij',np.asarray(v)*MET,G)
def u_spinor(p,m,s):
    chi=np.zeros(2,complex); chi[s]=1
    sp=sum(SIGMA[i]*p[i+1] for i in range(3))
    return math.sqrt(p[0]+m)*np.r_[chi,sp@chi/(p[0]+m)]
def ubar(u): return u.conj().T@G[0]
def v_spinor(p,m,s): return C@ubar(u_spinor(p,m,s)).T
def prop(r,m): return (slash(r)+m*I4)/(r[0]**2-np.dot(r[1:],r[1:])-m*m)
def photon_basis(n):
    n=np.asarray(n,float); n=n/np.linalg.norm(n)
    ref=np.array([0.,1.,0.])
    if abs(np.dot(ref,n))>.9: ref=np.array([1.,0.,0.])
    e1=np.cross(ref,n); e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
    return (np.r_[0.,e1],np.r_[0.,e2])
def moving_kin(mass,omega,pabs,cm,cg,phi):
    E=math.hypot(M,pabs); K=math.sqrt(omega*omega-mass*mass)
    p=np.array([E,pabs*math.sqrt(1-cm*cm),0.,pabs*cm])
    n=np.array([math.sqrt(1-cg*cg)*math.cos(phi),math.sqrt(1-cg*cg)*math.sin(phi),cg])
    q=np.array([omega,0.,0.,K])
    Cden=E+omega-np.dot(p[1:],n)-K*cg
    kg=(mass*mass+2*(E*omega-p[3]*K))/(2*Cden)
    photon=np.r_[kg,kg*n]
    pf=p+q-photon
    shell=abs(pf[0]**2-np.dot(pf[1:],pf[1:])-M*M)/M**2
    return p,pf,photon,q,n,shell
def amp_electron(pi,pf,k,q,eg,eps_v,eps_a,gv,ga):
    GA=gv*slash(eps_v)+ga*slash(eps_a)@G5; GG=slash(eg)
    return GA@prop(pi+k,M)@GG+GG@prop(pi-q,M)@GA
def amp_positron(pi,pf,k,q,eg,eps_v,eps_a,gv,ga):
    GA=gv*slash(eps_v)+ga*slash(eps_a)@G5; GG=slash(eg)
    return GG@prop(-pi-k,M)@GA+GA@prop(-pi+q,M)@GG

cases=[
    (10.,30.,80.,.4,-.3,1.2),
    (1.,15.,45.,-.2,.7,2.3),
    (100.,180.,130.,.6,.2,.8),
    (1e-7,5.332961631033191e-4,640.1416278200652,.525532409916329,.9602898564975362,2.5653157283115897),
    (.01,.5,220.,-.7,-.4,4.1),
]
max_res=0.; max_shell=0.; records=[]
for mass,omega,pabs,cm,cg,phi in cases:
    p,pf,k,q,n,shell=moving_kin(mass,omega,pabs,cm,cg,phi)
    max_shell=max(max_shell,shell)
    K=math.sqrt(omega*omega-mass*mass)
    epsL=np.array([K/mass,0.,0.,omega/mass],complex)
    epsp=np.array([0.,1.,1j,0.],complex)/math.sqrt(2)
    epsm=np.array([0.,1.,-1j,0.],complex)/math.sqrt(2)
    modes=[epsL,epsp,epsm]
    gamma_modes=photon_basis(n)
    for label,gv,ga in [('vector',1.,0.),('axial',0.,-1.),('mixed',math.sin(.01)**2,-math.cos(.01)**2)]:
        direct=[]; mapped=[]
        pi,pout=pf,p
        for ih,ex in enumerate(modes):
            eps_v=ex-q/mass if ih==0 else ex
            eps_a=ex
            sd=sm=0.
            for eg in gamma_modes:
                md=amp_positron(pi,pout,k,q,eg,eps_v,eps_a,gv,ga)
                mm=amp_electron(pi,pout,k,q,eg,eps_v,eps_a,gv,-ga)
                for si in range(2):
                    vi=v_spinor(pi,M,si); ui=u_spinor(pi,M,si)
                    for sf in range(2):
                        vf=v_spinor(pout,M,sf); uf=u_spinor(pout,M,sf)
                        sd+=abs(ubar(vi)@md@vf)**2/2
                        sm+=abs(ubar(uf)@mm@ui)**2/2
            direct.append(sd); mapped.append(sm)
        direct=np.asarray(direct); mapped=np.asarray(mapped)
        residual=float(np.max(np.abs(direct-mapped)/np.maximum(np.maximum(abs(direct),abs(mapped)),1e-300)))
        max_res=max(max_res,residual)
        records.append((mass,omega,pabs,cm,cg,phi,label,residual,direct.tolist(),mapped.tolist()))
print('max_moving_vspinor_to_charge_map_relative_residual',max_res)
print('max_final_muon_shell_relative_error',max_shell)
for r in records: print(r)
