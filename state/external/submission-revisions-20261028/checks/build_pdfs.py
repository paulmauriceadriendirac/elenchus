from pathlib import Path
import subprocess,json,sys,re,difflib
import fitz
R=Path('/workspace/scratch/45bb36400b49');O=R/'submission-revisions-20261028';T=R/'tmp/submission-final-20261028/pdf'
T.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(O/'checks'));from wordcount import count
items=[('essays/01-Holistic-Accuracy-v3.md','Holistic-Accuracy-v3.pdf'),('essays/02-Free-Evidence-v3.md','Free-Evidence-v3.pdf'),('essays/03-Causation-v3.md','Causation-v3.pdf'),('methodology/A5-Methodology.md','A5-Methodology.pdf'),('methodology/A6-Methodology.md','A6-Methodology.pdf'),('methodology/A4-Methodology.md','A4-Methodology.pdf'),('Review-Guide.md','Review-Guide.pdf')]
counts=[];scans=[]
for (source,pdf),ident,old in zip(items[:3],['A5','A6','A4'],['01-holistic-accuracy-A5-v2.md','02-free-evidence-A6-v2.md','04-causation-A4-v2-reserve.md']):
 c=count(str(O/source));assert c['strict']<=6000;counts.append(c)
 p=O/'methodology'/f'{ident}-Methodology.md';text=p.read_text();text=re.sub(r'Its source count is [\d,]+',f'Its source count is {c["strict"]:,}',text);p.write_text(text)
 oldpath=R/'review-edition-20261025/essays'/old
 (O/'revision-diffs'/f'{ident}-v2-to-v3.diff').write_text(''.join(difflib.unified_diff(oldpath.read_text().splitlines(True),(O/source).read_text().splitlines(True),fromfile=old,tofile=source)))
 scan=subprocess.run([sys.executable,str(O/'checks/check_injection.py'),str(O/source),'--names','paulmauriceadriendirac,elenchus,/workspace/'],text=True,capture_output=True)
 assert scan.returncode==0,scan.stdout
 scans.append({'file':source,'result':scan.stdout})
(O/'word-counts.json').write_text(json.dumps(counts,indent=2)+'\n')
g=O/'Review-Guide.md';text=g.read_text()
for title,c in zip(['Holistic Accuracy and the Lockean Thesis','When Acting on Knowledge Makes Free Evidence Harmful','What Normality Can and Cannot Do in Theories of Actual Causation'],counts):
 text=re.sub(r'\| '+re.escape(title)+r' \| [\d,]+ \|',f'| {title} | {c["strict"]:,} |',text)
g.write_text(text)
(O/'checks/manuscript-scan.json').write_text(json.dumps(scans,indent=2)+'\n')
header=T/'header.tex'
header.write_text(r'''\usepackage{fancyhdr}
\usepackage{sectsty}
\allsectionsfont{\raggedright}
\usepackage{microtype}
\usepackage{xurl}
\usepackage{newunicodechar}
\newunicodechar{∎}{\ensuremath{\square}}
\newunicodechar{⇒}{\ensuremath{\Rightarrow}}
\newunicodechar{⇔}{\ensuremath{\Leftrightarrow}}
\newunicodechar{→}{\ensuremath{\rightarrow}}
\newunicodechar{¬}{\ensuremath{\neg}}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0pt}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{3pt}
\widowpenalty=10000
\clubpenalty=10000
\allowdisplaybreaks
''')
manifest=[]
for source,dest in items:
 cmd=['pandoc',str(O/source),'-o',str(O/dest),'--standalone','--from=markdown+autolink_bare_uris','--pdf-engine=xelatex','-V','mainfont=DejaVu Serif','-V','sansfont=DejaVu Sans','-V','monofont=DejaVu Sans Mono','-V','mathfont=Latin Modern Math','-V','fontsize=11pt','-V','papersize=letter','-V','geometry:margin=0.75in','-V','linestretch=1.02','-V','colorlinks=true','-V','urlcolor=blue','--include-in-header='+str(header)]
 p=subprocess.run(cmd,text=True,capture_output=True)
 (T/(dest+'.log')).write_text(p.stdout+p.stderr)
 assert p.returncode==0,p.stderr
 doc=fitz.open(O/dest)
 doc.set_metadata({'title':(O/source).read_text().splitlines()[0].lstrip('# '),'author':'','subject':'','keywords':'','creator':'','producer':'','creationDate':'','modDate':''})
 tmp=T/(dest+'.clean.pdf');doc.save(tmp,garbage=4,deflate=True);doc.close();tmp.replace(O/dest)
 doc=fitz.open(O/dest)
 texts=[page.get_text() for page in doc]
 assert all(t.strip() for t in texts)
 if source.startswith('essays/'):
  assert not re.search(r'paulmauriceadriendirac|elenchus|/workspace/|AI Philosophy Competition|OpenReview','\n'.join(texts),re.I)
 manifest.append({'source':source,'pdf':dest,'pages':len(doc),'bytes':(O/dest).stat().st_size,'last_page_words':len(texts[-1].split())})
 for i,page in enumerate(doc):
  page.get_pixmap(matrix=fitz.Matrix(.65,.65),alpha=False).save(T/f'{dest[:-4]}-{i+1:02d}.png')
 doc.close();print(manifest[-1],flush=True)
combined=fitz.open();toc=[]
for pdf,label in [('Review-Guide.pdf','Reading guide'),('Holistic-Accuracy-v3.pdf','Holistic Accuracy'),('Free-Evidence-v3.pdf','Free Evidence'),('Causation-v3.pdf','Causation')]:
 toc.append([1,label,len(combined)+1]);part=fitz.open(O/pdf);combined.insert_pdf(part);part.close()
combined.set_toc(toc);combined.set_metadata({'title':'Three essays: reading copy, 28 October 2026'})
combined.save(O/'Three-Essays-Reading-Copy.pdf',garbage=4,deflate=True)
manifest.append({'pdf':'Three-Essays-Reading-Copy.pdf','pages':len(combined),'bytes':(O/'Three-Essays-Reading-Copy.pdf').stat().st_size})
combined.close()
(O/'checks/pdf-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
