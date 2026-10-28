"""Publish compact URL/route/topic indexes, never whole scraped articles."""
import collections, csv, hashlib, json, re
from pathlib import Path
from urllib.parse import urlsplit,urlunsplit,unquote
import ai_site_map as crawl

BASE=Path('research/2026-10-28-ai-site-map')
CACHE=Path('/tmp/ai-site-map-20261028')
STATE=CACHE/'state'
TAGS={
 '生成AI・LLM':r'generative|gen.?ai|生成AI|言語モデル|LLM',
 'AIエージェント':r'agent|エージェント|エージェンティック',
 'フィジカルAI・ロボティクス':r'physical.ai|robot|フィジカル|ロボティ|ロボット|embodied',
 'データ基盤・設計':r'data.(?:platform|architecture|fabric|mesh|engineering)|データ(?:基盤|アーキテクチャ|メッシュ|ファブリック)|アーキテクチャ|architecture|ontology|オントロジー',
 '分析・予測・最適化':r'analytics|data.science|optimization|アナリティクス|データ分析|データサイエンス|数理最適化|需要予測',
 '信頼・ガバナンス・セキュリティ':r'governance|responsible|trust|risk|security|ガバナンス|信頼|倫理|リスク|セキュリティ',
 '人材・働き方':r'talent|workforce|skills|人材|スキル|働き方|研修|育成|採用|career',
 '経営・投資・ROI':r'strateg|investment|ROI|経営|投資|戦略|価値創出',
 '医療・ライフサイエンス':r'health|life.science|pharma|medical|医療|製薬|ヘルスケア|ライフサイエンス',
 '金融':r'bank|insurance|financial.service|銀行|金融|保険',
 '製造・サプライチェーン':r'manufactur|supply.chain|industrial|製造|サプライチェーン|生産計画',
 '公共':r'public.sector|government|公共|自治体|政府',
 '消費財・小売':r'consumer|retail|消費財|小売',
 'エネルギー':r'energy|utilities|エネルギー|電力',
 '対談・インタビュー':r'interview|対談|インタビュー|座談会',
 '顧客事例':r'case.stud|client.stor|customer.stor|事例',
 '調査・報告書':r'report|survey|pulse|調査|レポート|報告書|state.of.ai',
}

def without_query(url):
 p=urlsplit(url);return urlunsplit((p.scheme,p.netloc,p.path,'',''))

def csvwrite(path,rows,fields):
 with path.open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore',lineterminator='\n');w.writeheader()
  w.writerows({k:re.sub(r'[ \t]+(?=\n|$)','',v.replace('\r','')) if isinstance(v,str) else v for k,v in row.items()} for row in rows)

def main():
 summaries={};allrows=[];gaps=[];audits=[];routes=[];overrides={}
 if (BASE/'review-overrides.json').exists():overrides=json.loads((BASE/'review-overrides.json').read_text())
 for c,(name,root,_) in crawl.ROOTS.items():
  state=json.loads((STATE/(c+'-state.json')).read_text());records=state['records']
  graph=collections.defaultdict(list)
  for e in state['edges']: graph[e['from']].append(e)
  # First-discovery routes remain valid evidence when later relevance rules narrow.
  for u,r in records.items():
   if r.get('parent'): graph[r['parent']].append({'from':r['parent'],'to':u,'anchor':r.get('incoming_anchor','')})
  for r in state['queue']:
   if r.get('parent'): graph[r['parent']].append({'from':r['parent'],'to':r['url'],'anchor':r.get('anchor','')})
  parents={root:None};depths={root:0};q=collections.deque([root])
  while q:
   u=q.popleft()
   for e in graph[u]:
    v=e['to']
    if v not in depths:depths[v]=depths[u]+1;parents[v]=e;q.append(v)
  rows=[]
  for u,r in records.items():
   cf=CACHE/c/(hashlib.sha256(u.encode()).hexdigest()+'.json')
   full=json.loads(cf.read_text()) if cf.exists() else r
   rel,reason=crawl.relevance(full,root)
   override=overrides.get(u,{})
   if 'include' in override:rel=override['include'];reason=override['reason']
   audit={'company':c,'url':u,'status':r['status'],'relevant':rel,'basis':reason,'error':r.get('error',''),'fetched_at':r.get('fetched_at','')}
   audits.append(audit)
   if r['status']!=200 or r.get('error'):
    gaps.append({'company':c,'url':u,'state':'fetch_failed','depth':depths.get(u,r['depth']),'from':r.get('parent',''),'anchor':r.get('incoming_anchor','')[:180],'detail':r.get('error','')})
   if not rel:continue
   assert crawl.allowed(u,c)
   assert u in depths, (c,u,'no_root_path')
   t=full.get('title','').replace('\n',' ').strip()
   if full.get('kind')=='pdf' and (len(t)>120 or re.search(r'copyright|©|PowerPoint Presentation|Microsoft Word|DAS Design Center',t,re.I)):
    # Bad PDF metadata / body-derived titles must not republish article text.
    t=unquote(urlsplit(u).path).split('/')[-1]
   t=override.get('title',t)
   # Repeated site logos do not add content to the title.
   t=re.sub(r'( Accenture){2,}$','',t)
   topictext=t+' '+full.get('description','')+' '+' '.join(full.get('headings',[])[:8])
   tags=[tag for tag,rx in TAGS.items() if re.search(rx,topictext,re.I)]
   if not tags:tags=['AI・データ全般']
   body=full.get('text',''); lang=full.get('language','')
   if len(re.findall(r'[一-龯ぁ-んァ-ヶ]',t))>3 or len(re.findall(r'[一-龯ぁ-んァ-ヶ]',body[:3000]))>50: lang='ja'
   elif lang.startswith('en'):lang='en'
   category=override.get('category',crawl.category(full))
   parent=parents.get(u) or {}
   row={'company':c,'company_ja':name,'category':category,'category_ja':crawl.CATS[category],'title':t[:220],'url':u,'final_url':r.get('final_url',u),'language':lang,'format':full.get('kind',''),'pdf_physical_pages':full.get('pdf_pages',''),'depth':depths[u],'parent_url':parent.get('from',r.get('parent','')),'incoming_anchor':parent.get('anchor',r.get('incoming_anchor',''))[:180],'topics':' / '.join(tags),'inclusion_basis':reason,'review':'manual' if override else 'rule_based','fetched_at':r.get('fetched_at',''),'content_sha256':r.get('sha256','')}
   rows.append(row)
   path=[];cur=u
   while parents.get(cur):
    e=parents[cur];path.append(e);cur=e['from']
   for e in reversed(path):routes.append({'company':c,'from':e['from'],'to':e['to'],'anchor':e['anchor'][:180]})
  for item in state['queue']:
   gaps.append({'company':c,'url':item['url'],'state':'frontier_not_fetched','depth':depths.get(item['url'],item['depth']),'from':item['parent'],'anchor':item['anchor'][:180],'detail':'bounded traversal; relevance unconfirmed'})
  rows.sort(key=lambda r:(r['category'],r['depth'],r['title'],r['url']));allrows+=rows
  cats=collections.Counter(r['category'] for r in rows);langs=collections.Counter(r['language'] for r in rows)
  summary={'name':name,'root':root,'confirmed_urls':len(rows),'categories':{crawl.CATS[k]:cats[k] for k in crawl.CATS},'languages':dict(langs),'html':sum(r['format']=='html' for r in rows),'pdf':sum(r['format']=='pdf' for r in rows),'without_query':len({without_query(r['url']) for r in rows}),'unique_final_without_query':len({without_query(r['final_url']) for r in rows}),'content_hashes':len({r['content_sha256'] for r in rows}),'depths':dict(sorted(collections.Counter(r['depth'] for r in rows).items())),'fetched_urls':len(records),'failed_urls':sum(r['status']!=200 or bool(r.get('error')) for r in records.values()),'unfetched_frontier':len(state['queue'])}
  summaries[c]=summary
  md=[f'# {name}：AI・データ関連ページ索引','',f'確認日：2026-10-28。日本語起点：{root}','',f'確認済み {len(rows)} URL。HTML {summary["html"]}／PDF {summary["pdf"]}。分類は見出し・概要・本文抽出による概括で、手動確認したページにはCSVでmanualを付す。全記事を精読した記録ではない。','', 'URL別の入口と主題を検索し、具体的な志望理由・ESで引用する際は原資料を読み直す。','']
  for cat,label in crawl.CATS.items():
   md += [f'## {cat}. {label}：{cats[cat]} URL','','| ページ | 主題タグ | 言語・形式 | 到達段数 |','|---|---|---|---|']
   for r in rows:
    if r['category']==cat:
     title=r['title'].replace('|','／').replace('[','（').replace(']','）')
     md.append(f'| [{title}]({r["url"]}) | {r["topics"]} | {r["language"]} / {r["format"]} | {r["depth"]} |')
   md.append('')
  (BASE/(c+'.md')).write_text('\n'.join(md),encoding='utf-8')
  csvwrite(BASE/(c+'.csv'),rows,list(rows[0]) if rows else ['url'])
 (BASE/'summary.json').write_text(json.dumps(summaries,ensure_ascii=False,indent=2))
 with (BASE/'inventory.jsonl').open('w') as f:
  for r in allrows:f.write(json.dumps(r,ensure_ascii=False)+'\n')
 # Only route bridges needed to connect AI/data pages are retained in the graph.
 dedup={(e['company'],e['from'],e['to']):e for e in routes}
 csvwrite(BASE/'routes.csv',list(dedup.values()),['company','from','to','anchor'])
 csvwrite(BASE/'unconfirmed.csv',gaps,['company','url','state','depth','from','anchor','detail'])
 csvwrite(BASE/'crawl-audit.csv',audits,['company','url','status','relevant','basis','error','fetched_at'])
 print(json.dumps(summaries,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
