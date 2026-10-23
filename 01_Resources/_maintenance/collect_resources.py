"""Refresh public URL metadata or download explicitly selected assets. Never executes downloads."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, re, sys, time
ROOT = Path(__file__).resolve().parents[1]
CACHE = Path('/tmp/badm534-research/pages')
class Text(HTMLParser):
 def __init__(self):
  super().__init__();self.parts=[];self.links=[];self.meta={};self.title=[];self.headings=[];self.skip=0;self.in_title=False;self.in_head=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('script','style'):self.skip+=1
  if tag=='title':self.in_title=True
  if tag in ('h1','h2','h3'):self.in_head=True
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if tag=='meta' and a.get('name','').startswith('citation_'):self.meta.setdefault(a['name'],[]).append(a.get('content',''))
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.skip=max(0,self.skip-1)
  if tag=='title':self.in_title=False
  if tag in ('h1','h2','h3'):self.in_head=False
 def handle_data(self,d):
  if not self.skip and d.strip():
   self.parts.append(d.strip())
   if self.in_title:self.title.append(d.strip())
   if self.in_head:self.headings.append(d.strip())
def get(url,limit=70_000_000):
 req=Request(url,headers={'User-Agent':'Mozilla/5.0 (educational course resource review)'})
 with urlopen(req,timeout=35) as r:
  b=r.read(limit+1)
  if len(b)>limit:raise ValueError('Size exceeds download limit')
  return b,r.status,r.url,r.headers.get('Content-Type','')
def check(r):
 try:
  b,status,url,ctype=get(r['url'],20_000_000)
  p=Text()
  if 'html' in ctype:p.feed(b.decode('utf-8',errors='replace'))
  meta={'id':r['id'],'checked_on':'2026-10-23','status':status,'final_url':url,'content_type':ctype,'title':' '.join(p.title),'headings':p.headings[:50],'citation':p.meta,'links':[urljoin(url,x) for x in p.links]}
  CACHE.mkdir(parents=True,exist_ok=True)
  (CACHE/(r['id']+'.txt')).write_text('\n'.join(p.parts))
  (CACHE/(r['id']+'.json')).write_text(json.dumps(meta,ensure_ascii=False,indent=2))
  print(r['id'],status,meta['title'][:90],flush=True)
  return {k:v for k,v in meta.items() if k not in ('links','headings','citation')}
 except Exception as e:
  print(r['id'],'FAILED',str(e),flush=True)
  return {'id':r['id'],'checked_on':'2026-10-23','status':'unresolved','error':str(e)}
def download(a):
 dest=ROOT/a['path']
 try:
  if dest.exists():b=dest.read_bytes();status='existing';url=a['url'];ct=''
  else:
   b,status,url,ct=get(a['url'])
   if dest.suffix=='.pdf' and not b.startswith(b'%PDF'):raise ValueError('Response is not PDF')
   if dest.suffix=='.ipynb':
    n=json.loads(b);assert n.get('nbformat') and 'cells' in n
   if dest.suffix=='.zip' and not b.startswith(b'PK'):raise ValueError('Response is not ZIP')
   if dest.suffix in ('.csv','.txt') and ('text/html' in ct or b.lstrip().lower().startswith(b'<!doctype html')):raise ValueError('HTML received instead of data/text')
   dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
  record=dict(a,status='saved',http_status=status,final_url=url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),downloaded_on='2026-10-23')
  print('SAVED',a['path'],len(b),flush=True);return record
 except Exception as e:
  print('FAILED',a['path'],str(e),flush=True);return dict(a,status='unresolved',error=str(e))
def main():
 mode=sys.argv[1]
 if mode=='check':
  rs=json.loads((ROOT/'RESOURCE_CATALOG.json').read_text())['resources']
  if len(sys.argv)>2:rs=[r for r in rs if r['id'] in sys.argv[2:]]
  with ThreadPoolExecutor(max_workers=6) as ex:out=list(ex.map(check,rs))
  old=ROOT/'_maintenance/link_checks.json';prev=json.loads(old.read_text()) if old.exists() else []
  byid={x['id']:x for x in prev};byid.update({x['id']:x for x in out})
  old.write_text(json.dumps(list(byid.values()),ensure_ascii=False,indent=2)+'\n')
 elif mode=='download':
  assets=json.loads((ROOT/'_maintenance/download_plan.json').read_text())
  if len(sys.argv)>2:assets=[a for a in assets if a['resource_id'] in sys.argv[2:]]
  with ThreadPoolExecutor(max_workers=5) as ex:out=list(ex.map(download,assets))
  old=ROOT/'_maintenance/download_manifest.json';prev=json.loads(old.read_text()) if old.exists() else []
  bypath={x['path']:x for x in prev};bypath.update({x['path']:x for x in out})
  old.write_text(json.dumps(list(bypath.values()),ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
