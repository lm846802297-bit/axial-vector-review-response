"""Generate publication-style benchmark contours from saved numerical scans."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
OUT=HERE/'outputs'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.labelsize':11,
                     'pdf.fonttype':42,'ps.fonttype':42,'figure.dpi':160})
def read(name):
    d=json.loads((OUT/name).read_text())
    return d,np.array([r['mass_MeV'] for r in d['results']]),np.array(d['couplings'])
a,m,g=read('axial.json');v,mv,gv=read('vector.json')
endpoint,_,_=read('endpoint.json')
assert endpoint['config']==a['config'] and endpoint['couplings']==a['couplings']
rows={r['mass_MeV']:r for r in a['results']}
rows.update({r['mass_MeV']:r for r in endpoint['results']})
a['results']=[rows[k] for k in sorted(rows)]
m=np.array(sorted(rows))
L=np.array([r['luminosity_erg_s'] for r in a['results']])
LV=np.array([r['luminosity_erg_s'] for r in v['results']])
fig,(ax,frac)=plt.subplots(1,2,figsize=(11.4,4.8),gridspec_kw={'width_ratios':[1.65,1]})
z=(np.log10(np.maximum(L,1e-200))-np.log10(4.4e52)).T
ax.contourf(m,g,z,levels=[0,100],colors=['#dce7f3'],alpha=1)
ax.contour(m,g,z,levels=[0],colors=['#235d91'],linewidths=1.7)
ax.contour(mv,gv,(np.log10(np.maximum(LV,1e-200))-np.log10(4.4e52)).T,levels=[0],colors=['#252525'],linestyles=['--'],linewidths=1.2)
ax.contour(m,g,(np.log10(np.maximum(L,1e-200))-np.log10(3e52)).T,levels=[0],colors=['#235d91'],linestyles=[':'],linewidths=1)
ax.fill_between([1,500],1e-6,1e-4,color='#ece8de',alpha=.6,zorder=-1)
ax.text(2,1.1e-5,'Original Fig. 2 window\n(shown portion)',fontsize=8,color='#756c5b')
ax.text(.022,3e-9,'Axial excluded:\n'+r'$L_{\rm axial}>4.4\times10^{52}$ erg s$^{-1}$',color='#235d91',fontsize=9)
ax.plot([],[],color='#235d91',lw=1.7,label=r'Axial: Raffelt $L_R=4.4\times10^{52}$ erg s$^{-1}$$')
ax.plot([],[],color='k',ls='--',lw=1.2,label=r'Vector $\mu$-current comparison only')
ax.plot([],[],color='#235d91',ls=':',label=r'Axial: $L_R=3.0\times10^{52}$ erg s$^{-1}$ (canonical estimate)')
ax.set(xscale='log',yscale='log',xlim=(.01,500),ylim=(1e-14,1e-4),xlabel=r'$m_{A^\prime}$ [MeV]',ylabel=r'$|g_X| \simeq |g_A^\mu|$')
ax.legend(loc='lower right',fontsize=7.4,frameon=False)
for key,col in [('Compton','#b44b3b'),('neutrino','#235d91'),('dimuon','#53835a')]:
    vals=np.array([r['thin_fractions'][key] for r in a['results']])
    frac.plot(m,vals,lw=1.8,color=col,label=key)
frac.axvline(2*105.6583755,color='.65',lw=.8,ls=':')
frac.set(xscale='log',yscale='log',xlim=(.01,500),ylim=(1e-4,1.2),xlabel=r'$m_{A^\prime}$ [MeV]',ylabel='Fraction of optically thin axial luminosity')
frac.legend(frameon=False,loc='lower left')
for axis in (ax,frac): axis.grid(which='major',alpha=.15);axis.tick_params(which='both',direction='in',top=True,right=True)
fig.suptitle('SN1987A: axial-EFT fixed-profile benchmark',fontsize=13)
fig.text(.5,.012,'Reconstructed SFHo-18.8 (1 s); three modes; exact-recoil muon-rest approximation; R = 25 km.\nBallistic cooling only. Unshaded regions are not a statement of global viability.',ha='center',fontsize=8)
fig.tight_layout(rect=(0,.08,1,.95))
fig.savefig(OUT/'axial_stellar_constraints.pdf')
fig.savefig(OUT/'axial_stellar_constraints.png')
# A stacked version keeps labels readable at the response letter's text width.
fig.set_size_inches(6.0,6.8)
ax.set_position([.16,.52,.80,.38])
frac.set_position([.16,.10,.80,.30])
ax.get_legend().remove()
ax.legend(loc='lower right',fontsize=8,frameon=False)
frac.set_ylabel('Fraction of optically thin\naxial luminosity',fontsize=9)
frac.legend(frameon=False,fontsize=8,loc='lower left',ncol=3)
fig._suptitle.set_fontsize(11)
fig.texts[-1].set_fontsize(6.5)
fig.savefig(OUT/'axial_stellar_constraints_reply.pdf')
fig.savefig(OUT/'axial_stellar_constraints_reply.png')
plt.close(fig)
fig,ax=plt.subplots(figsize=(7,4.5))
for mass,col in [(1,'#235d91'),(10,'#b44b3b'),(100,'#53835a'),(200,'#8464a1')]:
    row=next(r for r in a['results'] if r['mass_MeV']==mass)
    ax.plot(g,row['luminosity_erg_s'],label=f'{mass:g} MeV',color=col,lw=1.8)
ax.axhline(4.4e52,color='k',ls='--',label=r'$L_{\rm crit}=4.4\times10^{52}$ erg s$^{-1}$')
ax.set(xscale='log',yscale='log',xlim=(1e-12,1e-5),ylim=(1e49,1e56),xlabel=r'$|g_X|$',ylabel=r'Escaping luminosity [erg s$^{-1}$]')
ax.legend(frameon=False,fontsize=9,ncol=2);ax.grid(alpha=.15);fig.tight_layout()
fig.savefig(OUT/'luminosity_checks.pdf');fig.savefig(OUT/'luminosity_checks.png')
print('Saved constraint and luminosity figures')
# Additional GeV-axis comparison view. This is generated from the same saved
# scans; it does not replace or alter either of the existing MeV-axis figures.
plt.close(fig)
m_GeV = m / 1000.0
mv_GeV = mv / 1000.0

figG, (axG, fracG) = plt.subplots(
    1, 2, figsize=(11.4, 4.8), gridspec_kw={'width_ratios': [1.65, 1]}
)
zG = (np.log10(np.maximum(L, 1e-200)) - np.log10(4.4e52)).T
axG.contourf(m_GeV, g, zG, levels=[0, 100], colors=['#dce7f3'], alpha=1)
axG.contour(m_GeV, g, zG, levels=[0], colors=['#235d91'], linewidths=1.7)
axG.contour(
    mv_GeV, gv,
    (np.log10(np.maximum(LV, 1e-200)) - np.log10(4.4e52)).T,
    levels=[0], colors=['#252525'], linestyles=['--'], linewidths=1.2
)
axG.contour(
    m_GeV, g,
    (np.log10(np.maximum(L, 1e-200)) - np.log10(3e52)).T,
    levels=[0], colors=['#235d91'], linestyles=[':'], linewidths=1
)

# Show only the intersection of the original Fig. 2 display window with
# this panel's zoom range: m_A' >= 10^-3 GeV and g_X >= 10^-6.
axG.fill_between(
    [1e-3, 0.5], 1e-6, 1e-4,
    color='#ece8de', alpha=.6, zorder=-1
)
axG.text(
    1.6e-3, 3.0e-6, 'Fig. 2 overlap\n(shown portion)',
    fontsize=8, color='#756c5b'
)
axG.text(
    2.2e-5, 3e-9,
    'Axial excluded:\n' + r'$L_{\rm axial}>4.4\times10^{52}$ erg s$^{-1}$',
    color='#235d91', fontsize=9
)

axG.plot(
    [], [], color='#235d91', lw=1.7,
    label=r'Axial: Raffelt $L_R=4.4\times10^{52}$ erg s$^{-1}$$'
)
axG.plot(
    [], [], color='k', ls='--', lw=1.2,
    label=r'Vector $\mu$-current comparison only'
)
axG.plot(
    [], [], color='#235d91', ls=':',
    label=r'Axial: $L_R=3.0\times10^{52}$ erg s$^{-1}$ (canonical estimate)'
)
axG.set(
    xscale='log', yscale='log',
    xlim=(1e-5, 0.5), ylim=(1e-14, 1e-4),
    xlabel=r'$m_{A^\prime}$ [GeV]',
    ylabel=r'$|g_X| \simeq |g_A^\mu|$'
)
axG.legend(loc='lower right', fontsize=7.4, frameon=False)

for key, col in [('Compton', '#b44b3b'),
                 ('neutrino', '#235d91'),
                 ('dimuon', '#53835a')]:
    vals = np.array([r['thin_fractions'][key] for r in a['results']])
    fracG.plot(m_GeV, vals, lw=1.8, color=col, label=key)

fracG.axvline(2 * 105.6583755 / 1000.0, color='.65', lw=.8, ls=':')
fracG.set(
    xscale='log', yscale='log',
    xlim=(1e-5, 0.5), ylim=(1e-4, 1.2),
    xlabel=r'$m_{A^\prime}$ [GeV]',
    ylabel='Fraction of optically thin axial luminosity'
)
fracG.legend(frameon=False, loc='lower left')
for axis in (axG, fracG):
    axis.grid(which='major', alpha=.15)
    axis.tick_params(which='both', direction='in', top=True, right=True)

figG.suptitle('SN1987A: axial-EFT fixed-profile benchmark (GeV)', fontsize=13)
figG.text(
    .5, .02,
    'Same saved scan; mass coordinates only are converted: m[GeV] = m[MeV]/1000.\n'
    'Shading: visible overlap with Fig. 2. Ballistic cooling only; unshaded is not globally allowed.',
    ha='center', fontsize=7.5
)
figG.tight_layout(rect=(0, .09, 1, .95))
figG.savefig(OUT / 'axial_stellar_constraints_gev.pdf')
figG.savefig(OUT / 'axial_stellar_constraints_gev.png')

# A vertically stacked GeV version is used in the referee response letter.
# It is made from the already-rendered wide GeV figure: preserve all plotted
# artists, contour data, annotations, axis scales/limits, labels, and legends.
# Only the canvas size and the two Axes positions are changed. The explanatory
# footer is omitted because its full content is carried by the LaTeX caption.
figG.texts[-1].remove()
figG.set_size_inches(6.0, 6.6)
axG.set_position([0.16, 0.54, 0.80, 0.36])
fracG.set_position([0.16, 0.12, 0.80, 0.29])
figG.savefig(OUT / 'axial_stellar_constraints_reply_gev.pdf')
figG.savefig(OUT / 'axial_stellar_constraints_reply_gev.png')
plt.close(figG)
