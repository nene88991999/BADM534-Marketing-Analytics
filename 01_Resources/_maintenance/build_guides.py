"""Build local resource guides and Finder bookmarks from the curated catalog."""
from pathlib import Path
from urllib.parse import quote
import collections,hashlib,json,plistlib,re,zipfile
ROOT=Path(__file__).resolve().parents[1]
catp=ROOT/'RESOURCE_CATALOG.json';catalog=json.loads(catp.read_text());rs=catalog['resources'];by={r['id']:r for r in rs}
checks={x['id']:x for x in json.loads((ROOT/'_maintenance/link_checks.json').read_text())}
manifest=json.loads((ROOT/'_maintenance/download_manifest.json').read_text())
by['E06']['rights']='Author-posted version explicitly permits personal use and prohibits redistribution. Keep the local PDF for instructor reading; link to the author source in the public wiki.'
by['C02']['rights']='Personal research and study only per author site; link rather than republish.'
by['AI13']['owner']='Joel Becker, Nate Rush, Beth (Elizabeth) Barnes, and David Rein'
by['T06']['access']='Search-indexed publisher page; direct retrieval returned HTTP 403. Complete book and software may require payment.'
by['D05']['access']='Search-indexed official GroupLens page; direct retrieval timed out. Dataset use is subject to the linked README terms.'
by['T05']['access']='Public publisher sample PDF; complete book requires library or purchased access.'
by['E09']['access']='Public author abstract and citation; full text links to the publisher and may require library access.'
for r in rs:
 r['local_files']=[]
 r['link_check']=checks.get(r['id'],{'status':'not_checked'})
 r['prerequisites']=('None beyond general computing familiarity' if r['category'][:2] in ('00','01') else 'Python tables and basic statistics; see category notes for advanced material')
 # Metadata from primary paper landing pages, without reproducing abstracts.
 p=Path('/tmp/badm534-research/pages')/(r['id']+'.json')
 if p.exists():
  meta=json.loads(p.read_text()).get('citation',{})
  if meta:r['citation_metadata']={k:v for k,v in meta.items() if k!='citation_abstract'}
for a in manifest:
 a['rights']=by[a['resource_id']]['rights']
 if a['status']=='saved':by[a['resource_id']]['local_files'].append(a['path'])
(ROOT/'_maintenance/download_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# Extract only data and documentation from the five UCI archives; preserve original archives.
extracted=[]
def unpack(zpath,target,resource_id,depth=0):
 with zipfile.ZipFile(zpath) as z:
  assert z.testzip() is None
  for info in z.infolist():
   if info.is_dir():continue
   part=Path(info.filename)
   if part.is_absolute() or '..' in part.parts:raise ValueError('Unsafe archive path')
   if '__MACOSX' in part.parts or part.name.startswith('._') or part.name=='.DS_Store':continue
   out=target/part;out.parent.mkdir(parents=True,exist_ok=True);b=z.read(info);out.write_bytes(b)
   rel=str(out.relative_to(ROOT));extracted.append({'resource_id':resource_id,'archive':str(zpath.relative_to(ROOT)),'path':rel,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
   if out.suffix=='.zip' and depth==0:unpack(out,out.parent/out.stem,resource_id,depth+1)
for a in manifest:
 if a['status']=='saved' and a['path'].endswith('.zip'):
  zpath=ROOT/a['path'];unpack(zpath,zpath.parent/'Extracted',a['resource_id'])
(ROOT/'_maintenance/extracted_files.json').write_text(json.dumps(extracted,indent=2)+'\n')
for x in extracted:by[x['resource_id']]['local_files'].append(x['path'])
catalog['resources']=sorted(rs,key=lambda r:(r['category'],int(re.search(r'\d+',r['id']).group())))
catalog['scope']='Curated resource library covering the sample syllabus and AI-assisted coding. Sources are material for later lesson design, not validated assignments.'
catp.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
labels={
'00_Course_Map_and_Teaching':'Course Map and Teaching',
'01_Python_Data_and_Reproducibility':'Python, Data, and Reproducibility',
'02_Customer_Data_and_Visualization':'Customer Data and Visualization',
'03_Regression_and_Statistical_Foundations':'Regression and Statistical Foundations',
'04_Conjoint_Segmentation_and_CLV':'Conjoint, Segmentation, and Customer Lifetime Value',
'05_Text_Social_and_Network_Analysis':'Text, Social Media, and Network Analysis',
'06_Causal_Inference_and_Experiments':'Causal Inference and Experiments',
'07_Prediction_and_Machine_Learning':'Prediction and Machine Learning',
'08_Current_Topics_in_Marketing':'Current Topics in Marketing',
'09_AI_Assisted_Coding':'AI-Assisted Coding',
'10_Datasets_and_Project_Resources':'Datasets and Project Resources',
'11_GitHub_HTML_and_Interactive_Teaching':'GitHub, HTML, and Interactive Teaching'}
intro={
'00':'Read the course map before selecting readings. The aim is to preserve the marketing decisions and methods in the sample syllabus while teaching students to use coding assistants effectively.',
'01':'Begin with tables, functions, notebook execution, and elementary checks. Students need enough Python literacy to inspect data and explain generated code. Use the author notebooks as adaptation sources.',
'02':'Start from the customer or managerial question. Define the unit of observation and the denominator before constructing visual summaries. Require students to check joins and missing values before using generated charts.',
'03':'Review regression as a way to summarize relationships and quantify uncertainty. Introduce model specification and interpretation before asking an assistant to fit a model. Causal interpretations require a separately justified design.',
'04':'Keep the three decisions distinct: product configuration and pricing; useful customer segments; and future customer value. Basic RFM and clustering can precede probabilistic CLV. Bayesian choice and CLV examples are advanced extensions.',
'05':'Use a transparent baseline and a small manually labeled evaluation set before adding embeddings or LLMs. Networks are an optional extension from the syllabus introduction; the dated schedule emphasizes text analysis.',
'06':'Specify treatment, outcome, target population, assignment mechanism, and comparison before estimation. Begin with randomized experiments, then use observational designs to discuss identification and their assumptions.',
'07':'Choose a prediction target, decision time, and evaluation split before modeling. Start with a simple baseline. Relate prediction metrics to the cost and benefit of the marketing decision.',
'08':'Select a small number of extensions after the core methods. Marketing mix models, recommendations, forecasting, and generative AI can each support projects; the collection is deliberately broader than one semester of required readings.',
'09':'Use coding assistants throughout the course. Require a clear problem specification, small implementation steps, checks against known cases, and an explanation of the resulting analysis. The provider guides are alternatives, not a requirement to subscribe to every tool.',
'10':'The five UCI archives and extracted contents are saved locally. Larger, restricted, or registration-dependent sources remain linked. Matching a dataset to a method requires checking its unit, timing, outcome, and data-generating process.',
'11':'These are design and hosting references for the later wiki phase. GitHub Pages serves static files. Browser Python and external notebooks offer different ways to add executable exercises; their package support and resource limits need testing.'}
def rel_link(path,base):return quote(str(Path(path).relative_to(base)),safe='/')
def reference(key):
 r=by[key];return f"[{key}: {r['title']}]({r['url']})"
for category,title in labels.items():
 folder=ROOT/category;folder.mkdir(exist_ok=True);group=[r for r in catalog['resources'] if r['category']==category]
 lines=[f'# {title}','',f'Updated October 23, 2026. {len(group)} curated resources. [Master Guide](../README.md).','',intro[category[:2]],'','## Reading Guide','', '| ID | Resource | Priority | Format |','| --- | --- | --- | --- |']
 for r in group:lines.append(f"| {r['id']} | [{r['title']}]({r['url']}) | {r['priority']} | {r['kind']} |")
 lines+=['','Core identifies candidates for the eventual required readings. Reference material supports exercises and troubleshooting. Optional material supports extensions. Instructor material informs teaching and assessment; these labels are recommendations, not a finalized syllabus.','', '## Annotated Resources','']
 links=folder/'Links';links.mkdir(exist_ok=True)
 for r in group:
  slug=re.sub(r'[^A-Za-z0-9]+','_',r['title']).strip('_')[:105]
  (links/(r['id']+'_'+slug+'.webloc')).write_bytes(plistlib.dumps({'URL':r['url']}))
  lines += [f"### {r['id']}. {r['title']}",'',f"**Source:** {r['owner']}. [Open Resource]({r['url']}). **Priority:** {r['priority']}. **Syllabus:** {r['modules']}.",'',r['focus'],'',f"**Teaching Use:** {r['teaching_use']}"]
  if r['cautions']:lines+=['',f"**Conditions and Adaptation:** {r['cautions']}"]
  lines+=['',f"**Access and Reuse:** {r['access']} {r['rights']}"]
  if r['local_files']:
   lines+=['','**Local Files:**','']
   for fp in r['local_files']:lines.append(f"- [{str(Path(fp).relative_to(category))}]({quote(str(Path(fp).relative_to(category)),safe='/')})")
  else:lines+=['','**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.']
  ck=r['link_check'];lines+=['', '**Verification:** '+('Source URL retrieved successfully on October 23, 2026.' if ck.get('status')==200 else 'Direct retrieval incomplete: '+ck.get('error','not checked')+'. Retained as an optional/reference lead; check access before assigning.'),'']
 if category[:2]=='00':lines+=['## Planning Documents','','- [Syllabus Coverage and Teaching Priorities](Planning_Notes/README.md)','']
 if category[:2]=='09':lines+=['## Teaching Workflow','','- [AI Coding and Assessment Notes](Teaching_Notes/README.md)','']
 if category[:2]=='10':lines+=['## Dataset Selection','','- [Dataset Guide and Project Options](Dataset_Guide/README.md)','']
 if category[:2]=='11':lines+=['## Later Wiki Decisions','','- [Hosting and Interactivity Notes](Design_Notes/README.md)','']
 (folder/'README.md').write_text('\n'.join(lines))
# Top-level guide.
count_by=collections.Counter(r['category'] for r in rs);files=[a for a in manifest if a['status']=='saved'];pdfs=sum(a['path'].endswith('.pdf') for a in files);nbs=sum(a['path'].endswith('.ipynb') for a in files);size=sum(a['bytes'] for a in files)
lines=['# BADM 534 Resource Library','','Collected October 23, 2026 for Nathan Yang\'s planned version of **Data Analytics for Marketing Applications**. The collection follows Unnati Narang\'s eight-module Spring 2026 syllabus and adds resources for AI-assisted coding throughout the course. The wiki and new syllabus have not been built.','','## Start Here','',f'The library contains **{len(rs)} annotated resources across 12 topic folders**, **{pdfs} PDFs**, **{nbs} source notebooks**, **5 UCI dataset archives with extracted files**, and companion data, Python functions, and licenses. The {len(files)} downloaded source files occupy approximately {size/1e6:.1f} MB before archive extraction. Web resources also have Finder bookmarks in each folder\'s `Links` directory.','','1. Read the [Syllabus Coverage and Teaching Priorities](00_Course_Map_and_Teaching/Planning_Notes/README.md).','2. Review the [AI Coding and Assessment Notes](09_AI_Assisted_Coding/Teaching_Notes/README.md).','3. Choose starting data from the [Dataset Guide](10_Datasets_and_Project_Resources/Dataset_Guide/README.md).','4. Use the topic guides below to select short readings and source examples.','5. Consult the [Hosting and Interactivity Notes](11_GitHub_HTML_and_Interactive_Teaching/Design_Notes/README.md) when beginning wiki design.','','## Topic Folders','','| Folder | Coverage | Resources |','| --- | --- | ---: |']
for category,title in labels.items():lines.append(f'| [{title}]({category}/README.md) | '+('M'+category[:2].lstrip('0') if 1<=int(category[:2])<=8 else 'Across modules')+f' | {count_by[category]} |')
lines+=['','## A Focused Starting Set','','A manageable starting set is the Python marketing research notebooks (P10), pandas tutorials (P03), Wilke\'s visualization book (V01), ISLP and its labs (R01-R02), Sawtooth\'s conjoint readings (C01/C12), the segmentation book (C04), PyMC-Marketing CLV (C07), scikit-learn text features (X02), Facure\'s causal handbook (E01), the experimental-design paper (E06), scikit-learn pitfalls and evaluation (M02/M04), and one coding-assistant guide (AI01, AI03, or AI04). Use the seven coding studies AI09-AI14 and AI17 primarily for instructor preparation.','','The eight modules already cover a substantial semester. Treat advanced Bayesian estimation, uplift, embeddings, recommendations, and full marketing mix modeling as alternatives for extensions or projects. Python remains the default; R sources provide conceptual or instructor references.','','## How the Collection Was Selected','','The search combined the syllabus topics with marketing decisions, teaching materials, datasets, Python implementations, AI coding practices, and static HTML execution. Sources favor authors, publishers, university projects, official package documentation, and original research. Text, notebooks, and exercises are preferred; videos are not required. An author repository is counted once even when multiple companion files are saved. A book and its separate code repository can have distinct records because they have different uses and licenses.','','This is a broad curated foundation, not an exhaustive inventory of everything online. Each entry records the source, teaching use, priority, cautions, access/reuse notes, and available local files. General search results, unverified mirrors, bulk review dumps, and commercial registrations were not copied into the library.','','## Verification and Access','','All 117 source URLs were checked. 115 returned successful responses. Two useful reference leads have incomplete direct access: T06 (DecisionPro, HTTP 403) and D05 (GroupLens, timeout); both were found through official indexed pages. They are marked in their guides and are not required for the core collection. Successful retrieval confirms availability at collection time, not permanent access or technical suitability.','','Downloaded PDFs were parsed; ZIP archives passed CRC checks; notebooks were checked as notebook JSON; file hashes and exact source URLs are recorded. Selected GitHub files use commit-pinned download URLs. **Source notebooks have not been executed or converted into assignments.** Their dependencies, remote assets, outputs, and data-loading paths require adaptation and execution checks during lesson development.','','## Public Wiki Reuse','','Keep the instructor resource library separate from the eventual public site. Publicly readable material does not automatically permit copying to GitHub. In particular, the Python for Data Analysis web text restricts copying, Train\'s electronic book restricts use to personal research and study, and the Kohavi paper explicitly prohibits redistribution. Link to those sources. Retain license notices for repository code and cite datasets. Open-license materials still require attribution and attention to third-party exceptions.','','The sample syllabus remains in `00_Sample_Materials`. It includes private course-access information and a copyright notice, so this library links to it locally rather than copying its full text into a public-ready index. The conflict between its two AI-use passages is documented in the course map.','','## Files for Maintenance','','[RESOURCE_CATALOG.json](RESOURCE_CATALOG.json) is the portable structured catalog for later filtering or import into the wiki. [_maintenance/README.md](_maintenance/README.md) explains source provenance, download and extraction manifests, link checks, and how to rebuild these guides. Review live AI documentation and package behavior again before the teaching term.','']
if (ROOT/'00_Index/README.md').exists():
 lines += ['## Additional Material in the Shared Folder','','A [separate index](00_Index/README.md) and additional module folders are preserved outside this catalog. Counts and verification here refer to the 117 entries in RESOURCE_CATALOG.json and the 12 linked topic folders.','']
(ROOT/'README.md').write_text('\n'.join(lines))
print(json.dumps({'resources':len(rs),'downloaded_files':len(files),'pdfs':pdfs,'notebooks':nbs,'archives':5,'extracted_files':len(extracted),'downloaded_mb':round(size/1e6,1)},indent=2))
