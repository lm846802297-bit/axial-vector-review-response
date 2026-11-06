"""Digitize Blinov Fig. 7 and compare its full luminosity curves.

The source figure is from arXiv:2511.09619v2, luminosity_snapshot_t=1.pdf.
Use --source path/to/that.pdf. Only derived numerical vertices are saved.
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
    rows=[];points={}
    for mass,index,count in [(1.,42,34),(10.,43,27),(200.,44,14)]:
        d=p.get_drawings()[index]
        if len(d['items'])!=count:raise ValueError('Source PDF path changed')
        xy=polyline(d)
        alpha=10**(-22+16*(xy[:,0]-54.82951354980469)/(397.99951171875-54.82951354980469))
        g=np.sqrt(4*np.pi*alpha)
        light=10**(52+3*(195.54043579101562-xy[:,1])/(195.54043579101562-20.904434204101562))
        # Only vertices inside the visible frame, before any off-page tails.
        keep=(light>=1e52)&(light<=1e55)
        g,light=g[keep],light[keep]
        points[str(mass)]={'g':g.tolist(),'luminosity_erg_s':light.tolist(),'drawing_index':index}
        for variant in ['blinov_literal','exact_modes']:
            src,_,columns,angles=build(mass,HERE/'data'/'sfho188_digitized.csv',variant)
            actual=luminosities(src,columns,angles,g)
            for gg,ll,aa in zip(g,light,actual):
                rows.append({'mass_MeV':mass,'variant':variant,'g':gg,
                             'reference_erg_s':ll,'calculated_erg_s':aa,'relative_error':aa/ll-1})
    data={'source_url':'https://arxiv.org/src/2511.09619v2',
          'archive_member':args.source.name,'pdf_sha256':hashlib.sha256(args.source.read_bytes()).hexdigest(),
          'reference_vertices':points,'comparison':rows}
    (out/'luminosity_comparison.json').write_text(json.dumps(data,indent=2)+'\n')
    print({m:max(abs(r['relative_error']) for r in rows if r['mass_MeV']==m and r['variant']=='blinov_literal') for m in [1.,10.,200.]})

if __name__=='__main__':main()
