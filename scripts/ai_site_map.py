"""Read-only, same-company focused crawl from Japanese homepages.

Stores fetched metadata/link evidence and a small private temporary content cache.
Run with the bundled Python (lxml, pypdf). No third-party sites are requested.
"""
import argparse, concurrent.futures, hashlib, io, json, re, time, subprocess, tempfile
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit, unquote, quote
from lxml import html
from pypdf import PdfReader

ROOTS = {
    'deloitte': ('デロイト トーマツ', 'https://www.deloitte.com/jp/ja.html', ['deloitte.com','deloitte.jp']),
    'ey': ('EYジャパン', 'https://www.ey.com/ja_jp', ['ey.com']),
    'pwc': ('PwCジャパン', 'https://www.pwc.com/jp/ja/', ['pwc.com']),
    'kpmg': ('KPMGジャパン', 'https://kpmg.com/jp/ja.html', ['kpmg.com','kpmg.or.jp','kpmg-consulting.jp']),
    'accenture': ('アクセンチュア', 'https://www.accenture.com/jp-ja', ['accenture.com','accenture.jp']),
}
TOPIC = re.compile(r'(?<![a-z])ai(?![a-z])|artificial[ -]intelligence|generative|agentic|machine[ -]learning|deep[ -]learning|data[ -]?(?:science|analytics|analysis|platform|architect|modern|management|governance|driven|engineering|fabric|mesh)|big[ -]data|analytics|データ(?:サイエンス|分析|活用|利活用|基盤|駆動|戦略|マネジメント|管理|ガバナンス|エンジニアリング|アーキテクチャ)|アナリティクス|人工知能|機械学習|深層学習|生成\s*AI|大規模言語モデル|エージェント型|データドリブン|数理最適化|統計分析|統計解析|自然言語処理|予測分析|natural.language.processing|(?<![a-z])(?:llm|rag|mlops)(?![a-z])', re.I)
BRIDGE = re.compile(r'(?:^|/)(?:services|consulting|technology|insights|perspectives|industries|careers|newsroom|press-room|press-releases|media|sitemap|site-map|knowledge)(?:[/.-]|$)|テクノロジー|コンサルティング|インサイト|業種別|サービス一覧|サイトマップ|ニュースリリース|ニュースルーム|採用情報', re.I)
TECH = re.compile(r'アーキテクチャ|architecture|技術解説|アルゴリズム|algorithm|rag\b|llm\b|mlops|machine.learning|機械学習|深層学習|データ(?:基盤|仮想化|メッシュ|ファブリック|モデリング|サイエンス)|data.(?:mesh|fabric|platform|engineering|lake|warehouse|science)|オントロジー|ontology|セマンティック|モデルテスト|model.test|量子|quantum|ニューラル|neural|vector|ベクトル|強化学習|reinforcement|言語モデル|モデルの|モデル開発|モデル評価|数理最適化|統計解析|自然言語処理|プロンプト|prompt|マルチモーダル|multimodal|ベンチマーク|benchmark', re.I)
GOV = re.compile(r'ガバナンス|governance|倫理|ethic|responsible|trustworthy|信頼|リスク|risk|規制|regulat|security|セキュリティ|privacy|プライバシー|人材|talent|workforce|スキル|skills|育成|研修|インタビュー|対談|座談会|採用|career|people|パートナー|partner|組織|culture|雇用|employment', re.I)
USE = re.compile(r'導入|実装|構築|支援|事例|開発|ソリューション|サービス|solution|implementation|deploy|case.stud|client.stor|customer.stor|サービス|活用|活躍|自動化|automation|変革|transformation', re.I)
BAD = re.compile(r'\.(?:jpg|jpeg|png|gif|svg|webp|mp4|mp3|zip|css|js|woff2?|xlsx?|pptx?|docx?)(?:$|\?)|/(?:privacy|cookies?|legal|contact-us|terms-of-use)(?:[/.?]|$)|[?&](?:search|q)=|mailto:|tel:',re.I)
CATS = {'1':'技術・データ基盤','2':'導入支援・活用事例','3':'経営・業界動向・調査','4':'ガバナンス・人材・組織'}

def allowed(u, company):
    h=urlsplit(u).hostname or ''
    return any(h==d or h.endswith('.'+d) for d in ROOTS[company][2])

def norm(u):
    p=urlsplit(u)
    # Fragments locate positions within a page; preserve all query variants.
    return urlunsplit((p.scheme.lower(),p.netloc.lower(),p.path or '/',p.query,''))

def clean(s): return re.sub(r'\s+',' ',s or '').strip()

def curl_read(url, company):
    """Use host TLS store; follow redirects only inside this company."""
    current=url
    for _ in range(8):
        if not allowed(current,company): raise ValueError('outside_company_redirect')
        with tempfile.TemporaryDirectory(prefix='ai-map-fetch-') as td:
            headers=Path(td)/'headers'; body=Path(td)/'body'
            wire_url=quote(current,safe=":/?&=%;,+@!$'()*[]~-._")
            p=subprocess.run(['curl','--silent','--show-error','--compressed','--max-time','28','--max-filesize','23068672','-D',str(headers),'-o',str(body),'-w','%{http_code}',wire_url],capture_output=True)
            if p.returncode: raise ValueError(p.stderr.decode(errors='replace')[:180])
            status=int(p.stdout.decode()); h=headers.read_text(errors='replace')
            location=re.findall(r'^location:\s*(.+)$',h,re.M|re.I)
            if status in (301,302,303,307,308) and location:
                current=norm(urljoin(current,location[-1].strip()));continue
            content=re.findall(r'^content-type:\s*(.+)$',h,re.M|re.I)
            return status,current,content[-1].strip() if content else '',body.read_bytes()
    raise ValueError('redirect_limit')

def get_links(tree, base, company):
    out=[]
    for a in tree.xpath('//a[@href]'):
        href=a.get('href','').strip()
        if not href or href.startswith(('#','mailto:','tel:','javascript:')): continue
        u=norm(urljoin(base,href))
        if not u.startswith(('http://','https://')) or not allowed(u,company) or BAD.search(u): continue
        label=clean(' '.join(a.itertext())+' '+a.get('aria-label','')+' '+a.get('title',''))[:500]
        parent=a.getparent()
        context=clean(' '.join(parent.itertext()))[:700] if parent is not None else label
        out.append({'url':u,'anchor':label,'context':context})
    return out

def fetch(item, company, cache):
    u=item['url']; key=hashlib.sha256(u.encode()).hexdigest(); f=cache/(key+'.json')
    if f.exists():
        cached=json.loads(f.read_text())
        needs_body_refresh=(cached.get('kind')=='html' and cached.get('parser_version',1)<3 and relevance(cached,ROOTS[company][1])[0] and not TOPIC.search(cached.get('title','')+' '+' '.join(cached.get('h1',[]))))
        retry_transport=(cached.get('status')==0 or (cached.get('status')==403 and 'final_url' not in cached))
        if not needs_body_refresh and not re.search('[ãâ][\u0080-\u00bf]',cached.get('title','')) and not retry_transport and not (cached.get('status')==200 and cached.get('error')): return cached
    rec={'url':u,'fetched_at':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'transport':'curl'}
    try:
        status,final_url,content_type,b=curl_read(u,company)
        rec.update(status=status,final_url=final_url,content_type=content_type)
        if status!=200: raise ValueError('HTTP '+str(status))
        rec['sha256']=hashlib.sha256(b).hexdigest()
        if b.startswith(b'%PDF'):
            pdf=PdfReader(io.BytesIO(b)); texts=[]; links=[]
            for page in pdf.pages:
                try: texts.append(page.extract_text() or '')
                except Exception: pass
                for ar in page.get('/Annots',[]):
                    try:
                        a=ar.get_object().get('/A',{}); target=a.get('/URI','')
                        if target and allowed(target,company) and not BAD.search(target): links.append({'url':norm(target),'anchor':'PDF内リンク','context':''})
                    except Exception: pass
            body=clean(' '.join(texts)); title=clean(str((pdf.metadata or {}).get('/Title','')))
            if not title or title.lower() in ('untitled','presentation'): title=body[:160]
            rec.update(kind='pdf',title=title,description='',headings=[],text=body,links=links,pdf_pages=len(pdf.pages),language='ja' if len(re.findall(r'[一-龯ぁ-んァ-ヶ]',body[:3000]))>50 else 'en')
        else:
            tree=html.fromstring(b.decode('utf-8',errors='replace'),base_url=rec['final_url']); links=get_links(tree,rec['final_url'],company)
            title=clean(' '.join(tree.xpath('//title/text()')))
            desc=clean(' '.join(tree.xpath('//meta[@name="description" or @property="og:description"]/@content')))
            lang=tree.get('lang','')
            for el in tree.xpath('//script|//style|//noscript|//header|//footer|//nav|//*[@role="navigation"]|//*[@id="onetrust-banner-sdk"]|//*[@id="onetrust-consent-sdk"]|//*[contains(@class,"slim-page-header")]|//*[contains(@class,"headerv2-container")]|//*[contains(@class,"cmp-experiencefragment--header")]|//*[contains(@class,"cmp-experiencefragment--footer")]|//*[contains(@class,"headerexperiencefragment")]|//*[contains(@class,"footerexperiencefragment")]|//*[contains(@class,"glb-footer")]|//*[contains(concat(" ",@class," ")," navigation ")]'):
                if el.getparent() is not None: el.drop_tree()
            main=tree.xpath('//main|//*[@role="main"]')
            content=main[0] if main else tree
            body=clean(' '.join(content.itertext()))
            heads=[clean(' '.join(x.itertext())) for x in content.xpath('.//h1|.//h2|.//h3')]
            # Description and heading1 focus classification away from related-card nav.
            h1=[clean(' '.join(x.itertext())) for x in content.xpath('.//h1')]
            actual_lang='ja' if len(re.findall(r'[一-龯ぁ-んァ-ヶ]',body[:3000]))>50 else lang or 'en'
            rec.update(kind='html',title=title,description=desc,headings=heads[:50],h1=h1,text=body,links=links,language=actual_lang,parser_version=3)
        rec['body_length']=len(rec.get('text',''))
    except Exception as e: rec.update(status=rec.get('status',0),error=str(e)[:250])
    f.write_text(json.dumps(rec,ensure_ascii=False))
    return rec

def relevance(r, root):
    if r['url']==root or r.get('status')!=200 or not r.get('text'): return False,'root/error/empty'
    t=r.get('title','')+' '+' '.join(r.get('h1',[]))
    desc=r.get('description',''); body=r.get('text','')
    if re.search(r'page not found|ページが見つかりません|アクセスできません',t,re.I): return False,'soft404'
    if re.search(r'Fast\s*50|Fast\s*500',t,re.I) and not TOPIC.search(t): return False,'general_company_ranking'
    simple=re.split(r'\s*[|｜]\s*',r.get('title',''))[0].strip()
    if re.fullmatch(r'業種|サービス|採用情報|リスク・アシュアランス|プライベート・エクイティ（PE）（ディールアドバイザリー）|Audit（監査）|Managed Services|Risk & Regulatory|Newsroom - Global press releases',simple,re.I): return False,'general_navigation_gateway'
    if TOPIC.search(t): return True,'title/h1'
    if TOPIC.search(desc) and len(TOPIC.findall(body))>=3: return True,'description+body'
    # Old AI URLs may redirect to a general company/services home page.
    # The destination, rather than the obsolete source slug, must qualify.
    if TOPIC.search(unquote(urlsplit(r.get('final_url',r['url'])).path).rstrip('/').split('/')[-1]) and len(TOPIC.findall(body))>=5: return True,'slug+body'
    if r.get('kind')=='pdf' and len(TOPIC.findall(body))>=10 and TOPIC.search(body[:2000]): return True,'pdf_body'
    return False,'not_primary_ai_data'

def category(r):
    t=r.get('title','')+' '+' '.join(r.get('h1',[]))
    if re.search(r'/people/|/careers/|/contacts/',urlsplit(r['url']).path): return '4'
    if GOV.search(t): return '4'
    if TECH.search(t): return '1'
    if re.search(r'state.of.ai|survey|調査|レポート|展望|outlook|pulse|市場動向|予測|調査結果',t,re.I): return '3'
    if USE.search(t): return '2'
    if r.get('kind')=='pdf': return '3'
    path=urlsplit(r['url']).path
    if re.search(r'/services/|/capabilities/|/case-studies/|/cases/|/clients/',path): return '2'
    return '3'

def candidate(link, parent, depth):
    u=link['url']; label=link['anchor']; context=link.get('context','')
    if TOPIC.search(label+' '+unquote(urlsplit(u).path)): return 'topic_link'
    if TOPIC.search(context) and (len(context)<450 or u.lower().endswith('.pdf')): return 'topic_context'
    # Generic gateways are traversed but not counted unless their own focus qualifies.
    if depth<=2 and BRIDGE.search(label+' '+urlsplit(u).path): return 'navigation_bridge'
    if parent.get('relevant') and (u.lower().split('?')[0].endswith('.pdf') or re.search(r'ダウンロード|download|read.*report|レポートを読む',label,re.I)): return 'related_download'
    return ''

def crawl(company, out, cache, maxdepth, limit):
    name,root,_=ROOTS[company]; cache=cache/company; cache.mkdir(parents=True,exist_ok=True)
    out.mkdir(parents=True,exist_ok=True); statefile=out/(company+'-state.json')
    state=json.loads(statefile.read_text()) if statefile.exists() else {'queue':[{'url':root,'depth':0,'parent':'','anchor':'日本語トップ','reason':'root'}],'records':{},'edges':[]}
    queue=state['queue']; records=state['records']; edges=state['edges']; seen=set(records)|{i['url'] for i in queue}
    batches=0
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        while queue and len(records)<limit:
            eligible=[i for i in queue if i['depth']<=maxdepth]
            if not eligible: break
            depth=min(i['depth'] for i in eligible)
            batch=[i for i in eligible if i['depth']==depth][:15]
            for i in batch: queue.remove(i)
            futures=[pool.submit(fetch,i,company,cache) for i in batch]
            for item,future in zip(batch,futures):
                full=future.result(); relevant,reason=relevance(full,root)
                rec={k:v for k,v in full.items() if k not in ('text','links')}
                rec.update(depth=item['depth'],parent=item['parent'],incoming_anchor=item['anchor'],discovery_reason=item['reason'],relevant=relevant,relevance_reason=reason,category=category(full) if relevant else '')
                records[item['url']]=rec
                parent=dict(full,relevant=relevant)
                for l in full.get('links',[]):
                    why=candidate(l,parent,item['depth']+1)
                    if not why: continue
                    edges.append({'from':item['url'],'to':l['url'],'anchor':l['anchor'],'reason':why})
                    if l['url'] not in seen:
                        seen.add(l['url']);queue.append({'url':l['url'],'depth':item['depth']+1,'parent':item['url'],'anchor':l['anchor'],'reason':why})
            batches+=1
            statefile.write_text(json.dumps(state,ensure_ascii=False,indent=1))
            if batches%4==0 or not queue:
                print(json.dumps({'company':company,'fetched':len(records),'relevant':sum(r['relevant'] for r in records.values()),'pending':len(queue),'depth':depth},ensure_ascii=False),flush=True)
            time.sleep(.15)
    statefile.write_text(json.dumps(state,ensure_ascii=False,indent=1))
    print(json.dumps({'company':company,'done_this_pass':True,'fetched':len(records),'relevant':sum(r['relevant'] for r in records.values()),'pending':len(queue)}),flush=True)

def refresh(company,out,cache):
    path=out/(company+'-state.json')
    if not path.exists(): return
    state=json.loads(path.read_text());records=state['records'];seen=set(records)|{x['url'] for x in state['queue']}
    newedges=[]; root=ROOTS[company][1]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        urls=list(records)
        for start in range(0,len(urls),15):
            batch=urls[start:start+15]
            fulls=list(pool.map(lambda u:fetch({'url':u},company,cache/company),batch))
            for u,full in zip(batch,fulls):
                old=records[u]; rel,why=relevance(full,root)
                rec={k:v for k,v in full.items() if k not in ('text','links')}
                rec.update({k:old[k] for k in ('depth','parent','incoming_anchor','discovery_reason')})
                rec.update(relevant=rel,relevance_reason=why,category=category(full) if rel else '')
                records[u]=rec; parent=dict(full,relevant=rel)
                for l in full.get('links',[]):
                    reason=candidate(l,parent,rec['depth']+1)
                    if not reason: continue
                    newedges.append({'from':u,'to':l['url'],'anchor':l['anchor'],'reason':reason})
                    if l['url'] not in seen:
                        seen.add(l['url']);state['queue'].append({'url':l['url'],'depth':rec['depth']+1,'parent':u,'anchor':l['anchor'],'reason':reason})
            if start%150==0: print(json.dumps({'company':company,'refreshed':start+len(batch),'of':len(urls)}),flush=True)
    state['edges']=newedges;path.write_text(json.dumps(state,ensure_ascii=False,indent=1))

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('company',choices=list(ROOTS)+['all']);a.add_argument('--out',default='/tmp/ai-site-map-20261028/state');a.add_argument('--cache',default='/tmp/ai-site-map-20261028');a.add_argument('--maxdepth',type=int,default=6);a.add_argument('--limit',type=int,default=6000);a.add_argument('--refresh',action='store_true')
    args=a.parse_args()
    def run(c):
        if args.refresh: refresh(c,Path(args.out),Path(args.cache))
        crawl(c,Path(args.out),Path(args.cache),args.maxdepth,args.limit)
    if args.company=='all':
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures=[executor.submit(run,c) for c in ROOTS]
            for f in futures: f.result()
    else: run(args.company)
