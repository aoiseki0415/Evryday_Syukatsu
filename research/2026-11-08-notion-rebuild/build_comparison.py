"""Render the role-level comparison; saved child-page tags are appended at write time."""
import json
from pathlib import Path

BASE = Path(__file__).parent
rows = json.loads((BASE / 'candidates.json').read_text())
page_map = json.loads((BASE / 'notion-map.json').read_text())
def mention(page_id, title):
    return f'<mention url="https://app.notion.com/p/{page_id}">{title}</mention>'
short = {'deloitte':'デロイト', 'pwc':'PwC', 'ey':'EY', 'kpmg':'KPMGコンサル', 'accenture':'アクセンチュア', 'bcg':'BCG', 'mckinsey':'マッキンゼー', 'bain':'ベイン', 'di':'DI', 'globe':'グロービング', 'nri':'NRI', 'mri':'三菱総研', 'kearney':'カーニー', 'adl':'ADL', 'igpi':'IGPI', 'rolandberger':'ローランド・ベルガー', 'oliverwyman':'オリバー・ワイマン', 'kpmg_fas':'KPMG FAS'}
features = {
 'DE-A':'構想を技術側へ翻訳するDeployment StrategistとFDEの協働。①軸足の技術接点が明瞭。',
 'PW-A':'ビジネス側とデータサイエンティストが同じ顧客チームでAI開発・本番移行を支援（移行予定を含む）。',
 'EY-A':'国内の少人数AI&データチームが戦略・設計・開発・テストを接続。',
 'KP-A':'全社活用構想、現場の実用化、人材育成へ。若手のAI技術検証の実例もある。',
 'AC-A':'独立したAI&Data職。技術が明瞭な入口で、①を担う比率を確認したい。',
 'AC-B':'業務・組織と技術の共同変革。RDEは将来の役割像で、別の新卒募集職ではない。',
 'BC-T':'経営・デジタル構想を軸にXやPlatinion等と接続。国内の個人担当は未確約。',
 'MK-D':'DigitalとQuantumBlackが価値設計・開発・顧客の能力構築をつなぐ。',
 'BA-C':'一般コンサルとAI・開発の専門家が混成チームで企業変革を支える。',
 'DI-T':'Technology & Amplifyの専用新卒入口。経営構想からAI・ITの実行へつなぐ。',
 'GL-A':'AI技術を担いつつ全社AI戦略・組織設計と本番MLOpsをつなぐ案件。',
 'GL-S':'戦略側から技術チームとの共同変革へ。本人の③④参加の形を確認したい。',
 'NR-A':'AI戦略部と実装側をつなぐ体制。海外事例を日本の本人実績とは分ける。',
 'MR-A':'全社設計と現場AIの検証を往復する支援。28本選考の現行要項は未確認。',
 'EY-FS':'金融のリスク評価・実証から経営課題へ。対象範囲と①軸足の個人担当を確認。',
 'AC-S':'①を軸にする入口。RDEの方向性は近いが、③④での個人の技術参加は要確認。',
 'BC-X':'技術と経営の協働は明瞭。Data Scientist本人の①責任と現在応募可否を確認。',
 'IG-D':'経営と技術、自走する組織を接続。国内一般新卒からDIへの接続・28対象を確認。',
 'OW-Q':'Quotientの戦略・実装と組織統制は近い。東京新卒からの専門接続が未確認。',
 'KA-D':'Cervelloとの共同実装は具体的。全社AI変革と国内新卒の接点の補強が必要。',
 'AD-A':'AI基盤・技術組織の開発は確認。全社変革と国内本人の接続を補強したい。',
 'RB-A':'分析・技術チームとの協働は確認。顧客全社AI変革と国内職務の根拠を補強。',
 'FAS-C':'経営価値とAI分析を接続する院卒専用職。顧客自身の全社AI変革の実例は不足。',
}
def label(r):
    return r['id']+'｜'+short[r['company_id']]+'／'+r['environment']
compact = {'DE-A':'デロイト／AI&Data','PW-A':'PwC／DAX・AI','EY-A':'EY／AI&データ','KP-A':'KPMGコンサル／DXA','AC-A':'アクセンチュア／AI職','AC-B':'アクセンチュア／BC職','BC-T':'BCG／TDA','MK-D':'マッキンゼー／Digital','BA-C':'ベイン／コンサル×AI','DI-T':'DI／T&A','GL-A':'グロービング／AI・デジタル','GL-S':'グロービング／戦略','NR-A':'NRI／AI戦略','MR-A':'三菱総研／産業DX','EY-FS':'EY／金融TC','AC-S':'アクセンチュア／戦略職','BC-X':'BCG X／Data Scientist','IG-D':'IGPI／DI協働','OW-Q':'OW／Quotient協働','KA-D':'カーニー／D&A','AD-A':'ADL／AI・デジタル','RB-A':'ローランド／AI・分析','FAS-C':'KPMG FAS／CVA'}
def matrix(group):
    out = '| 候補環境 | C1 | C2 | C3 | C4 | C5 |\n| --- | --- | --- | --- | --- | --- |\n'
    for r in rows:
        if r['group']==group:
            out += '| '+r['id']+'｜'+compact[r['id']]+' | '+' | '.join(r['criteria'][c]['symbol'] for c in ['C1','C2','C3','C4','C5'])+' |\n'
    return out

s = '''<callout icon="🎯" color="green_bg">
<b>05の条件で、23環境を再評価。まず比較を深めたいのは12社・14環境。</b>

①構想を軸に、③④の技術的な学びと、全社の価値・組織の変革をつなぐ環境を探す。

<date start="2026-11-08" /> 確認｜17企業グループ・23環境。KPMGコンサルティングとKPMG FASは別法人・別職務として比較し、グループ数では一つ。

以下は<b>公開根拠に基づくCodexの推薦</b>。本人の志望順位・応募決定は未確定。
</callout>

<columns>
<column ratio="34">
<callout icon="🟢" color="green_bg">
<b>優先して比較｜14</b>

中核条件の案件・体制が確認できる。
</callout>
</column>
<column ratio="33">
<callout icon="🟡" color="yellow_bg">
<b>条件付きで残す｜5</b>

近い環境だが役割・国内接続等の確認が重要。
</callout>
</column>
<column ratio="33">
<callout icon="🔎" color="gray_bg">
<b>追加確認・保留｜4</b>

関連性はある。中核条件の裏付けを補強する。
</callout>
</column>
</columns>

## 1｜条件の確認状況を比べる

| C1 | C2 | C3 | C4 | C5 |
| --- | --- | --- | --- | --- |
| 価値・全社 | 技術への実質関与 | 構想と実装の接続 | 人・組織の設計 | 統制と継続変革 |

**● 具体的な案件・体制の根拠　○ 提供説明・間接根拠・範囲限定　？ 未確認**

記号は「根拠の確認状況」。関与の程度、会社の優劣、担当保証の点数ではない。●にも海外事例・匿名短記・一部工程が含まれるため、数を足して順位を付けない。C4・C5は加点観点であり、未確認だけで除外しない。

### 優先して比較する環境

'''+matrix('優先して比較')+'''
上表の○は仕事の不適合とは限らない。会社の活動が確認できても、**本人が①を軸に③④へどう入るか**は各社の詳細に残す。

<toggle heading="h3" color="yellow_bg">
条件付きで残す5環境

'''+matrix('条件付きで残す')+'\n'+ '\n'.join('- **'+label(r)+'**：'+features[r['id']] for r in rows if r['group']=='条件付きで残す')+'''
</toggle>

<toggle heading="h3" color="gray_bg">
追加確認・保留の4環境

'''+matrix('追加確認・保留')+'\n'+'\n'.join('- **'+label(r)+'**：'+features[r['id']] for r in rows if r['group']=='追加確認・保留')+'''
</toggle>

## 2｜それぞれ、何が特徴なのか

仕事紹介から公式の職務説明へ。案件・条件別の根拠は末尾「5｜企業別の案件・判断根拠」から開ける。**仕事紹介と募集は別のリンク**に分ける。同じ会社の別職務も別候補として見る。

| 候補 | 特徴をひとことで | 仕事紹介 |
| --- | --- | --- |
'''
for r in rows:
    if r['group']=='優先して比較':
        s += '| '+label(r)+' | '+features[r['id']]+' | [公式紹介]('+r['work_url']+') |\n'
s += '\n<toggle heading="h3">\n条件付き・保留の仕事紹介と、全候補のデータサイエンスとの接点\n\n| 候補 | 接点 | 仕事紹介 |\n| --- | --- | --- |\n'
for r in rows:
    s += '| '+label(r)+' | '+r['ds']+' | [公式紹介]('+r['work_url']+') |\n'
s += '''\nデータサイエンスは加点で、必須条件ではない。Deployment Strategistの略称DSとデータサイエンティストは区別する。
</toggle>

## 3｜日本の新卒・28卒の入口

**仕事の適合／国内新卒制度／28卒資格／現在受付／専門配属**を分けて見る。公開情報の確認時点は11/8。MyPage内部や本人の応募状況は確認していない。

| 今回押さえる変更 | 確認したこと |
| --- | --- |
| BCG一般コンサル | 28卒春インターンは2027/1/14 12:00 JST締切。Xの募集期限へ転用しない |
| オリバー・ワイマン | 東京一般新卒28は2026/11/25 23:59 JST締切。Quotient配属は未確認 |
| KPMGコンサル | 通年新卒制度は確認。27年4月以降卒業が対象。28専用の現在回・DXA配属は別途確認 |
| KPMG FAS CVA | 掲載回は2026/5/29 13:00締切済み。AIX・フォレンジックの2027/1/6を転用しない |
| 三菱総研 | 取得できた28向け情報は夏インターン終了。28本選考の現行要項・受付は未確認 |

'''
sets = [('総合5社の入口', {'deloitte','pwc','ey','kpmg','accenture'}), ('優先候補の戦略・シンクタンク等', {'bcg','mckinsey','bain','di','globe','nri','mri'}), ('追加確認先の国内入口', {'kearney','adl','igpi','rolandberger','oliverwyman','kpmg_fas'})]
for title, firms in sets:
    s += '\n<toggle heading="h3">\n'+title+'\n\n| 候補・入口 | 現在受付 | 期限 | 専門配属・留意点 | 募集 |\n| --- | --- | --- | --- | --- |\n'
    for r in rows:
        if r['company_id'] in firms:
            s+='| '+label(r)+' | '+r['hiring_status']+' | '+r['deadline']+' | '+r['placement']+' | [公式等の募集]('+r['hiring_url']+') |\n'
    s+='\n</toggle>\n'
s += '''
<callout icon="📌" color="blue_bg">
<b>締切済みでも仕事環境は比較に残す。</b>

マッキンゼー・ベイン・DI等の終了した募集回と、仕事の適合は別。28資格・専門経路が未確認の先は「現時点で応募可能な確定候補」にしない。経験者・海外専門職は仕事内容の補助根拠に限る。
</callout>

## 4｜ここから選定するための確認

| 確かめたいこと | 具体的に聞く・見る情報 |
| --- | --- |
| ①を軸に③④にも入れるか | 若手の担当、共同チーム、技術判断・検証・改善への参加 |
| 全社の変革まで届くか | 全社配布や基盤の範囲だけでなく、事業価値・組織・意思決定をどう変えたか |
| 顧客に合わせて技術を選べるか | 複数製品の選択・提携・自社製品の制約。提携があるだけで除外しない |
| 将来像に向かう仕事か | 人・組織、統制、顧客能力の構築を技術導入とどうつなぐか |

**現時点の結論**：まず優先14環境を比較の中心に置き、条件付き5環境を並行して確認する。保留4環境は不足証拠が取れたら再評価する。本人の最終的な志望・応募先は、この先の議論で決める。

<toggle heading="h3">
調査範囲と限界

- 旧45社・61ラベルの探索記録を再読し、総合5社、戦略・シンクタンク等の既存候補と見落とし候補を追加確認した。
- 旧45社全てのページを今回の日時で取り直したという意味ではない。再利用した根拠と11/8追加確認を詳細・資料索引で分ける。
- 会社の思想、提供範囲、実案件、本人の職務、IDCの世界評価は別の根拠。海外・別法人の活動を日本の担当へ合成しない。
- 全社計画と部分実装、実証と本番、予定と成果を分ける。全社共通基盤だけで全社変革の完了を断定しない。
- 資料不足は未確認。選定結果は調査上の推薦であり、就職難易度の客観的順位付けではない。
</toggle>

'''+mention(page_map['05'],'05｜条件の定義へ戻る')+'\n\n'+mention(page_map['references'],'参考資料｜記事・IDC・追加探索へ')+'''

## 5｜企業別の案件・判断根拠

各ページは「11/8の再評価 → 実案件と限界 → 国内新卒入口 → 残る質問 → 以前の詳細」の順。
'''
s = s.replace('## 3｜日本の新卒・28卒の入口', (BASE/'idc-comparison.md').read_text()+'\n\n## 3｜日本の新卒・28卒の入口')
(BASE/'06-comparison.md').write_text(s)
print('Rendered 06: '+str(len(s))+' characters')
