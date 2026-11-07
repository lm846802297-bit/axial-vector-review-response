"""Digitize all six Blinov Fig. 7 curves and compare the luminosity curves.

The source figure is from arXiv:2511.09619v2, luminosity_snapshot_t=1.pdf.
Use --source path/to/that.pdf. Only derived numerical vertices are saved.
The source PDF hash, drawing indices, path colours and item counts are pinned.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import fitz
from extract_vector_reference import polyline
from run_vector_audit import build,HERE
from transport import luminosities


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',type=Path,required=True)
    args=ap.parse_args()
    p=fitz.open(args.source)[0]
    out=HERE/'outputs'/'vector_audit';out.mkdir(parents=True,exist_ok=True)
    pdf_sha256=hashlib.sha256(args.source.read_bytes()).hexdigest()
    if pdf_sha256!=EXPECTED_PDF_SHA256:
        raise ValueError(f'Pinned Fig. 7 source PDF changed: {pdf_sha256}')
    drawings=p.get_drawings()
    rows=[];points={}
    for mass,index,count,expected_color in CURVES:
        d=drawings[index]
        if len(d['items'])!=count:raise ValueError(f'Source PDF path changed for m={mass:g} MeV')
        if d['fill'] is not None or not np.allclose(d['color'],expected_color,rtol=0,atol=1e-8):
            raise ValueError(f'Source PDF path identity changed for m={mass:g} MeV')
        xy=polyline(d)
        alpha=10**(-22+16*(xy[:,0]-54.82951354980469)/(397.99951171875-54.82951354980469))
        g=np.sqrt(4*np.pi*alpha)
        light=10**(52+3*(195.54043579101562-xy[:,1])/(195.54043579101562-20.904434204101562))
        # Only vertices inside the visible frame, before any off-page tails.
        keep=(light>=1e52)&(light<=1e55)
        g,light=g[keep],light[keep]
        if len(g)<5:raise ValueError(f'Too few visible vertices for m={mass:g} MeV')
        points[str(mass)]={'g':g.tolist(),'luminosity_erg_s':light.tolist(),
                           'drawing_index':index,'drawing_color':list(d['color']),
                           'source_item_count':count}
        for variant in ['blinov_literal','exact_modes']:
            src,_,columns,angles=build(mass,HERE/'data'/'sfho188_digitized.csv',variant)
            actual=luminosities(src,columns,angles,g)
            for gg,ll,aa in zip(g,light,actual):
                rows.append({'mass_MeV':mass,'variant':variant,'g':gg,
                             'reference_erg_s':ll,'calculated_erg_s':aa,'relative_error':aa/ll-1})
    data={'source_url':'https://arxiv.org/src/2511.09619v2',
          'archive_member':args.source.name,'pdf_sha256':pdf_sha256,
          'figure':'Blinov et al., JHEP 06 (2026) 155, Fig. 7; visually cross-checked against the version-of-record PDF',
          'reference_vertices':points,'comparison':rows}
    (out/'luminosity_comparison.json').write_text(json.dumps(data,indent=2)+'\n')
    print({m:max(abs(r['relative_error']) for r in rows if r['mass_MeV']==m and r['variant']=='blinov_literal') for m in [1.,10.,200.]})

if __name__=='__main__':main()
