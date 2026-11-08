"""Build concise Notion comparisons from the reviewed evidence, not numeric rankings."""
import json
import re
from pathlib import Path

BASE = Path(__file__).parent
ROOT = BASE.parents[1]


def read(name):
    return json.loads((BASE / name).read_text())


def save(name, data):
    (BASE / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def body(page):
    return page['text'].split('<content>', 1)[1].split('</content>', 1)[0].strip()


def mention(page_id, title):
    return f'<mention url="https://app.notion.com/p/{page_id}">{title}</mention>'


old = json.loads(Path('/tmp/notion-ai-rebuild-before.json').read_text())
general = read('general-firms-review.json')
strategy = read('strategy-firms-review.json')
gr = {x['id']: x for x in read('general-ratings.json')['rows']}
fas = read('fas-review.json')
# Keep the historical FAS source IDs intact; the new CVA review is a separate ledger.
def namespace_fas(value):
    if isinstance(value, dict):
        return {k: namespace_fas(v) for k, v in value.items()}
    if isinstance(value, list):
        return [namespace_fas(v) for v in value]
    return 'R-' + value if isinstance(value, str) and re.fullmatch(r'FAS[1-4]', value) else value
fas = namespace_fas(fas)
page_map = read('notion-map.json')
old_sources = json.loads((ROOT / 'research/2026-11-06-ideal-ai-environments/sources.json').read_text())
sources = {x['id']: x for x in old_sources}
sources.update({x['id']: x for x in general['sources']})
sources.update({x['id']: x for x in strategy['current_sources']})
sources.update({x['id']: x for x in fas['sources']})
article_sources = json.loads((ROOT / 'research/2026-11-07-ai-transformation-views/sources.json').read_text())
used_article_ids = {'AD02', 'AD04', 'BA03', 'BA04', 'BC02', 'BC03', 'NR02', 'NR03'}
sources.update({x['id']: dict(x, reused_from='2026-11-07-ai-transformation-views') for x in article_sources if x['id'] in used_article_ids})
sources['RB-future'] = {
    'id':'RB-future', 'title':'AIが書き換える組織：第3回（最終回）',
    'author':'田村誠一', 'published_at':'2026-09-24', 'checked_at':'2026-11-08',
    'url':'https://www.rolandberger.com/ja/Insights/Publications/AI%E3%81%8C%E6%9B%B8%E3%81%8D%E6%8F%9B%E3%81%88%E3%82%8B%E7%B5%84%E7%B9%94%EF%BC%9A%E7%AC%AC3%E5%9B%9E%EF%BC%88%E6%9C%80%E7%B5%82%E5%9B%9E%EF%BC%89.html',
    'kind':'公式論考（将来の支援思想）',
    'fact':'AIを前提に業務・役割・組織・人材・統制を継続的に再設計し、現場の試行を次の設計へ戻す運営能力を重視。',
    'limit':'顧客案件の実績や日本新卒の担当を示す資料ではない。',
    'read_scope':'本文冒頭から結論まで確認（strategy-firm reviewer）'
}

known_profiles = {
    'deloitte': '410161f28097810db713f7be6a311ea3',
    'pwc': '410161f28097818ca3dccf7f97240fc7',
    'ey': '410161f28097818d833cf0e8c4e87058',
    'kpmg': '410161f2809781e0a775d28b4fd3317b',
    'accenture': '410161f280978120b5c1f963596ed33e',
    'bcg': '410161f2809781439408eb8d6753c618',
    'mckinsey': '410161f2809781618229fb11a280bd1b',
    'bain': '410161f28097812dacb2fe5d2dd8ffdb',
    'di': '410161f28097819a8a52ce135a8a71c4',
    'globe': '410161f2809781ceb1dde28803a47b22',
    'nri': '410161f280978150a1eee42cd1410b4b',
    'mri': '410161f28097814288dbf1798fd5bd53',
    'igpi': '410161f2809781b18a46c7a142958b6b',
}
known_profiles.update(page_map.get('profiles', {}))
priority = {'DE-A', 'PW-A', 'EY-A', 'KP-A', 'AC-A', 'AC-B', 'BC-T', 'MK-D', 'BA-C', 'DI-T', 'GL-A', 'GL-S', 'NR-A', 'MR-A'}
hold = {'KA-D', 'AD-A', 'RB-A', 'FAS-C'}


def group(row_id):
    return '優先して比較' if row_id in priority else '追加確認・保留' if row_id in hold else '条件付きで残す'


rows = []
for firm in general['firms']:
    for r in firm['rows']:
        h = firm['hiring']
        work = next((x['url'] for x in general['sources'] if x['id'] in firm['evidence'][0]['sources']), '')
        if firm['id'] == 'accenture':
            work = 'https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level'
        hiring_url = sources[h['sources'][0]]['url']
        if firm['id'] == 'pwc':
            work = 'https://www.pwc.com/jp/ja/careers/consulting/campus/recruiting-info/technology-consulting.html'
        if firm['id'] == 'ey':
            work = sources['G-EY3' if r['id'] == 'EY-FS' else 'G-EY1']['url']
        if firm['id'] == 'kpmg':
            work = 'https://recruit.kpmg-consulting.jp/info/dxa'
        criteria = {k: {'symbol': gr[r['id']][k]['value'], 'evidence': gr[r['id']][k]['note'], 'source_ids': gr[r['id']][k]['source_ids']} for k in ['C1', 'C2', 'C3', 'C4', 'C5']}
        rows.append({'id': r['id'], 'company_id': firm['id'], 'company': firm['company'], 'environment': r['environment'], 'group': group(r['id']), 'reason': firm['reason'], 'entry_role': r['entry_role'], 'work_url': work, 'hiring_url': hiring_url, 'hiring_status': h['current_status'], 'deadline': h['deadline'], 'placement': h['placement'], 'criteria': criteria, 'remaining': firm['remaining_questions'], 'ds': '関連あり・担当は役割次第'})

groups = {}
for env in strategy['environments']:
    groups.setdefault(env['company_id'], []).append(env)
    e = env['entry']
    rows.append({'id': env['id'], 'company_id': env['company_id'], 'company': env['company'], 'environment': env['environment'], 'group': group(env['id']), 'reason': env['highlight'], 'entry_role': e.get('qualification', '国内一般新卒・専門接続は要確認'), 'work_url': env['work_url'], 'hiring_url': e['url'], 'hiring_status': e['status'], 'deadline': e['deadline'], 'placement': e.get('limit', '専門配属未確認'), 'criteria': env['criteria_05'], 'remaining': env['remaining_conditions'], 'ds': env['ds']})

fas_criteria = {k: {'symbol': v['value'], 'evidence': v['note'], 'source_ids': v['source_ids']} for k, v in fas['ratings'].items()}
for k in ['C4', 'C5']:
    fas_criteria[k] = {'symbol': '？', 'evidence': fas['future_support_fit']['unconfirmed'], 'source_ids': []}
rows.append({'id': 'FAS-C', 'company_id': 'kpmg_fas', 'company': 'KPMG FAS', 'environment': 'Client Value Analytics（CVA）', 'group': group('FAS-C'), 'reason': fas['reason'], 'entry_role': fas['role'] + '（28院卒専用）', 'work_url': sources['R-FAS2']['url'], 'hiring_url': sources['R-FAS1']['url'], 'hiring_status': fas['hiring']['current_status'], 'deadline': fas['hiring']['published_round_deadline'] + '（掲載回終了）', 'placement': fas['hiring']['placement'], 'criteria': fas_criteria, 'remaining': fas['remaining_questions'], 'ds': '中核。ただし顧客自身のAI変革の証拠は補強'})
for row in rows:
    row['profile_id'] = known_profiles.get(row['company_id'])
    assert set(row['criteria']) == {'C1', 'C2', 'C3', 'C4', 'C5'}
    assert all(v['symbol'] in ['●', '○', '△', '？'] for v in row['criteria'].values())
save('candidates.json', rows)
save('sources.json', list(sources.values()))

profile_payloads = []
for company_id, envs in groups.items():
    first = envs[0]
    profile_id = known_profiles.get(company_id)
    s = f'<callout icon="🔎" color="green_bg">\n<b>11/8・05の条件による再評価</b>\n\n{first["future_fit"]}\n</callout>\n\n## 比較する部門・役割\n\n| 候補ID・環境 | 判断 | 仕事紹介 |\n| --- | --- | --- |\n'
    for e in envs:
        s += f'| {e["id"]}｜{e["environment"]} | {e["assessment"]} | [公式職務]({e["work_url"]}) |\n'
    s += '\n## 条件との対応\n\n'
    for label, key in [('企業の工程・技術への関与', 'A_company'), ('本人の関与可能性', 'A_person'), ('変革の対象範囲', 'B_company')]:
        s += f'**{label}**：{first[key]}\n\n'
    s += '## 実案件・体制の根拠\n\n'
    for c in first.get('cases', []):
        src = sources.get(c.get('source'), {})
        link = f'[{c.get("source")}]({src["url"]})' if src.get('url') else c.get('source', '')
        s += f'### {c["client"]}\n\n| 観点 | 内容 |\n| --- | --- |\n| 対象・地域 | {c["scope"]}／{c["location"]} |\n| 進行状態 | {c["stage"]} |\n| 確認事実 | {c["fact"]} |\n| 限界 | {c["caution"]} |\n\n根拠：{link}\n\n'
    for url in first.get('evidence_urls', []):
        s += f'[今回確認した公式根拠]({url})\n\n'
    s += '## C1〜C5の根拠の確認状況\n\n| 条件 | 記号 | 根拠・限界 |\n| --- | --- | --- |\n'
    for key, v in first['criteria_05'].items():
        links = '／'.join(f'[根拠]({u})' for u in v.get('source_urls', []))
        s += f'| {key} | {v["symbol"]} | {v["evidence"]} {v["limit"]} {links} |\n'
    s += '\n●は具体的な案件・体制の根拠。○は提供説明・間接根拠・範囲限定、？は未確認。地域・証拠の詳しさ・個人担当の保証を示す尺度ではない。\n'
    s += '\n## 日本の新卒・28卒\n\n'
    for e in envs:
        h = e['entry']
        s += f'### {e["id"]}｜{e["environment"]}\n\n| 観点 | 11/8確認 |\n| --- | --- |\n| 現在受付 | {h["status"]} |\n| 期限 | {h["deadline"]} |\n| 資格・経路 | {h.get("qualification", "国内新卒制度を参照。専門接続は要確認")} |\n| 留意点 | {h.get("limit", "専門配属・個人担当は未確認")} |\n\n[公式募集]({h["url"]})\n\n'
    s += '## 残る確認事項\n\n' + '\n'.join('- ' + x for x in first['remaining_conditions']) + '\n'
    if profile_id and profile_id in old:
        s += '\n<toggle heading="h2" color="gray_bg">\n11/6時点の詳細・既存根拠（履歴）\n\n受付・期限は当時の記録。上の11/8確認を優先。\n\n' + body(old[profile_id]) + '\n</toggle>\n'
    s += '\n' + mention(page_map['06'], '06｜比較と選定へ戻る') + '\n'
    profile_payloads.append({'company_id': company_id, 'page_id': profile_id, 'title': first['company'] + '｜案件・条件との対応・国内新卒', 'body': s})

s = '<callout icon="🔎" color="yellow_bg">\n<b>11/8再評価：CVAは追加確認・保留。</b>\n\n' + fas['reason'] + '\n</callout>\n\n## 顧客AI変革との関係\n\n' + fas['future_support_fit']['distinction'] + '\n\n## 条件との対応\n\n| 条件 | 記号 | 根拠・不足 |\n| --- | --- | --- |\n'
for k, v in fas_criteria.items():
    s += f'| {k} | {v["symbol"]} | {v["evidence"]} |\n'
s += '\n## 国内28院卒の専門入口\n\n| 項目 | 確認 |\n| --- | --- |\n'
for key, label in [('cohort', '入社時期'), ('masters', '修了時期・専攻'), ('skills', '必要経験'), ('current_status', '現在受付'), ('published_round_deadline', '掲載回の締切'), ('placement', '専門配属')]:
    s += f'| {label} | {fas["hiring"][key]} |\n'
s += '\n' + fas['hiring']['warning'] + '\n\n## 出典\n\n'
for src in fas['sources']:
    s += f'**[{src["id"]}｜{src["title"]}]({src["url"]})**\n\n- 確認事実：{src["facts"]}\n- 限界：{src["limits"]}\n\n'
s += '\n## 残る確認事項\n\n' + '\n'.join('- ' + x for x in fas['remaining_questions']) + '\n\n' + mention(page_map['06'], '06｜比較と選定へ戻る')
profile_payloads.append({'company_id': 'kpmg_fas', 'page_id': known_profiles.get('kpmg_fas'), 'title': 'KPMG FAS CVA｜顧客AI変革との適合・28院卒入口', 'body': s})
save('strategy-profile-updates.json', profile_payloads)

assert len({x['id'] for x in rows}) == len(rows)
print(json.dumps({'rows': len(rows), 'company_groups': len({r['company_id'].replace('kpmg_fas','kpmg') for r in rows}), 'groups': {k: sum(r['group'] == k for r in rows) for k in ['優先して比較', '条件付きで残す', '追加確認・保留']}, 'profile_payloads': len(profile_payloads), 'source_records': len(sources)}, ensure_ascii=False))
