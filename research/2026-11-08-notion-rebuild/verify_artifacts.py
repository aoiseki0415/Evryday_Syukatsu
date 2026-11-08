"""Verify the saved Notion readbacks and preservation; no external mutation."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).parent
before = json.loads(Path('/tmp/notion-ai-rebuild-before.json').read_text())
after = json.loads(Path('/tmp/notion-ai-rebuild-after.json').read_text())
rows = json.loads((BASE / 'candidates.json').read_text())
sources = json.loads((BASE / 'sources.json').read_text())
mapping = json.loads((BASE / 'notion-map.json').read_text())
def body(p):
    return p['text'].split('<content>', 1)[1].split('</content>', 1)[0].strip()
def external_urls(pages):
    urls = set()
    for p in pages.values():
        for u in re.findall(r'https?://[^\s<>\"]+', body(p)):
            u = u.rstrip(').,／')
            if not any(d in u for d in ['app.notion.com/', 'www.notion.so/', 'notion.so/']):
                urls.add(u)
    return urls
def annotations(pages):
    return Counter((c, t) for p in pages.values() for c, t in re.findall(r'<span color="(red|green)">(.*?)</span>', body(p), re.S))
def media(pages):
    # Copied media gets a new block ID (URL authority), but retains the asset UUID.
    return set(u.split('/',3)[3].split('?',1)[0] for p in pages.values() for u in re.findall(r'notion-file-block://[^\s\"<>\)]+',body(p)))
def children(page_id):
    return re.findall(r'<page url="https://app\.notion\.com/p/([a-f0-9]+)">',body(after[page_id]))

missing_pages = sorted(set(before)-set(after))
missing_urls = sorted(external_urls(before)-external_urls(after))
missing_media = sorted(media(before)-media(after))
missing_annotations = annotations(before)-annotations(after)
source_ids = {x['id'] for x in sources}
unknown_sources = sorted({s for r in rows for v in r['criteria'].values() for s in v.get('source_ids',[]) if s not in source_ids})
overview = body(after[mapping['06']])
missing_candidates = [r['id'] for r in rows if r['id']+'｜' not in overview]
missing_work_links = [r['id'] for r in rows if r['work_url'] not in overview]
missing_hiring_links = [r['id'] for r in rows if r['hiring_url'] not in overview]
bad_pages = [k for k,p in after.items() if p.get('truncated') or p.get('unknown_block_count',0) or p.get('unknown_block_ids')]
original_article_ids = [k for k,p in before.items() if k.startswith('411') and '顧客AI変革をどう支援するか' in p['title']]
unchanged_articles = [k for k in original_article_ids if body(before[k]) == body(after[k])]
checks = {
 'all_original_pages_reachable': not missing_pages,
 'all_original_external_urls_preserved': not missing_urls,
 'all_original_red_green_annotations_preserved': not missing_annotations,
 'all_original_media_assets_preserved': not missing_media,
 'all_article_detail_bodies_unchanged': len(unchanged_articles)==len(original_article_ids),
 'no_truncated_or_unknown_blocks': not bad_pages,
 'source_ids_unique': len(source_ids)==len(sources),
 'all_criteria_source_ids_resolve': not unknown_sources,
 'all_candidates_have_profiles': all(r.get('profile_id') in after for r in rows),
 'all_candidates_and_links_in_overview': not (missing_candidates+missing_work_links+missing_hiring_links),
 'root_has_eight_sections': len(children(mapping['root']))==8,
 'comparison_has_eighteen_profiles': len(children(mapping['06']))==18,
 'references_has_nine_children': len(children(mapping['references']))==9,
 'candidate_counts': Counter(r['group'] for r in rows)==Counter({'優先して比較':14,'条件付きで残す':5,'追加確認・保留':4}),
}
result = {
 'checked_at':'2026-11-08', 'checks':checks,
 'counts': {'original_pages':len(before),'current_pages':len(after),'original_external_urls':len(external_urls(before)),'original_media_assets':len(media(before)),'original_red_green_annotation_occurrences':sum(annotations(before).values()),'article_details_unchanged':len(unchanged_articles),'candidate_environments':len(rows),'company_groups':len({r['company_id'].replace('kpmg_fas','kpmg') for r in rows}),'profile_pages':len(children(mapping['06'])),'source_records':len(sources)},
 'issues':{'missing_pages':missing_pages,'missing_urls':missing_urls,'missing_media':missing_media,'missing_annotations':list(missing_annotations.elements()),'unknown_sources':unknown_sources,'missing_candidate_ids':missing_candidates,'missing_work_links':missing_work_links,'missing_hiring_links':missing_hiring_links,'bad_pages':bad_pages},
 'visual_check':json.loads((BASE/'visual-qa.json').read_text()),
 'independent_review':{'status':'passed_with_repair','note':'General-firm reviewer checked 05/06 and ratings. PwC feature now explicitly includes planned production migration.'},
 'git_delivery_verification':{'method':'Compare final HEAD with origin refs/heads/main after push','result_location':'Final conversation tool result; this file verifies the Notion/data readbacks, not its own containing commit'}
}
(BASE/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
manifest=[]
for k,p in before.items():
    manifest.append({'page_id':k,'original_title':p['title'],'reachable_after':k in after,'body_identical':k in after and body(p)==body(after[k]),'original_body_sha256':hashlib.sha256(body(p).encode()).hexdigest(),'current_body_sha256':hashlib.sha256(body(after[k]).encode()).hexdigest() if k in after else None})
(BASE/'preservation-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# Save the authored core pages, not complete snapshots or third-party full text.
for key,name in [('root','home'),('00','glossary'),('01','01-structure'),('02','02-current'),('03','03-orientation'),('04','04-future'),('05','05-criteria'),('06','06-comparison'),('references','references')]:
    (BASE/(name+'.md')).write_text(body(after[mapping[key]])+'\n')
print(json.dumps({'checks':checks,'counts':result['counts'],'issues':result['issues']},ensure_ascii=False,indent=2))
if not all(checks.values()):
    raise SystemExit(1)
