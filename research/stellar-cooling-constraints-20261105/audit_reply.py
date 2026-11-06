"""Reproducible source preservation, build dependency and PDF audit.

Run after latexmk and copying the checked build to the tracked root PDF.
This checks source structure and text; it does not replace visual inspection.
"""
import hashlib
import json
import platform
import re
import subprocess
from pathlib import Path
import pymupdf

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
NAME='Replies_to_Referee_3_referee_facing_2026-11-04'
BASE='7ef9a4a65fc0f9afd25ed857325760775faf71bd'

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    before=subprocess.check_output(['git','show',BASE+':'+NAME+'.tex'],cwd=ROOT).decode('utf-8')
    after=(ROOT/(NAME+'.tex')).read_text(encoding='utf-8')
    # Only these eight wrappers are layout edits to pre-existing mathematics.
    stripped=after.replace('\\resizebox{\\linewidth}{!}{$\\displaystyle{\n','').replace('\n}$}\n','\n')
    quotes=lambda s:re.findall(r'\\begin\{quote\}(.*?)\\end\{quote\}',s,re.S)
    assert quotes(before)==quotes(after) and len(quotes(after))==27
    markers=[r'\noindent {\bf Major Points 2)}.',r'\noindent {\bf Major Points 3)}.',
             r'\noindent {\bf 4.4)}.',r'\noindent {\bf Minor Point 1)}.',r'\noindent {\large Summary:}']
    unchanged={
        'Major1_including_all_1p3_scientific_content':before[:before.index(markers[0])]==stripped[:stripped.index(markers[0])],
        'Major3_through_Major4p3':before[before.index(markers[1]):before.index(markers[2])]==stripped[stripped.index(markers[1]):stripped.index(markers[2])],
        'all_Minor_replies':before[before.index(markers[3]):before.index(markers[4])]==stripped[stripped.index(markers[3]):stripped.index(markers[4])],
    }
    assert all(unchanged.values()),unchanged
    cited=set(k.strip() for body in re.findall(r'\\cite\w*\{([^}]+)\}',after) for k in body.split(','))
    bibs=[ROOT/(p+'.bib') for p in re.search(r'\\bibliography\{([^}]+)\}',after).group(1).split(',')]
    keys=[]
    for p in bibs:keys+=re.findall(r'@\w+\s*\{\s*([^,\s]+)',p.read_text(encoding='utf-8'))
    assert not(cited-set(keys)),cited-set(keys)
    assert len(keys)==len(set(keys))
    labels=re.findall(r'\\label\{([^}]+)\}',after)
    refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',after)
    assert len(labels)==len(set(labels)) and not(set(refs)-set(labels))
    stack=[]
    for kind,name in re.findall(r'\\(begin|end)\{([^}]+)\}',after):
        if kind=='begin':stack.append(name)
        else:assert stack.pop()==name
    assert not stack
    pdf=ROOT/(NAME+'.pdf');built=ROOT/'build'/(NAME+'.pdf')
    assert sha(pdf)==sha(built)
    log=(ROOT/'build'/(NAME+'.log')).read_text(encoding='utf-8',errors='replace')
    assert not re.search(r'undefined|There were undefined|Citation .* Warning',log,re.I)
    doc=pymupdf.open(pdf)
    unresolved=[i+1 for i,p in enumerate(doc) if '[?]' in p.get_text() or '??' in p.get_text()]
    assert not unresolved
    fontrefs={font[0] for p in doc for font in p.get_fonts()}
    unembedded=[xref for xref in fontrefs if not doc.extract_font(xref)[3]]
    assert not unembedded
    dependencies=[ROOT/(NAME+'.tex'),*bibs,ROOT/'JHEP.bst',HERE/'outputs/axial_stellar_constraints_reply.pdf']
    report=dict(base_commit=BASE,referee_quotes_unchanged=len(quotes(after)),unchanged_science_blocks=unchanged,
        new_layout_wrappers=after.count('\\resizebox{\\linewidth}{!}{$\\displaystyle{'),
        unique_citation_keys=len(cited),labels=len(labels),environments_balanced=True,
        pdf_pages=len(doc),pdf_sha256=sha(pdf),pdf_matches_build=True,
        unresolved_pdf_markers=unresolved,all_fonts_embedded=True,
        overfull_warnings=re.findall(r'Overfull[^\n]*',log),
        dependency_sha256={str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in dependencies},
        versions=dict(python=platform.python_version(),pymupdf=pymupdf.__version__),
        visual_review='Separate human-readable record; this script does not inspect appearance',ci='executed by the referee-response build workflow')
    (HERE/'outputs/reply_audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
