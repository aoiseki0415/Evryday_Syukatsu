# フェルミ①｜全情報の索引

状態：初期input→演習→再input→別問題適用を経て標準手順v2へ更新。型選択の候補と、定義/条件付き式の採用を区別する。領域全体の十分な精度は未認定。優先度と状態を別に読む。

更新2026-11-26。数字設定方法A-003と設定例参照層C-001を追加し、全30ID（A6/B23/C1）。[情報の構造と読込地図](READING_MAP.md)から本文へ辿れる。今回の学習は無料Web調査/過去演習再検討で、新規問題は0。

## A 必須

| ID・要点 | 種類・状態・条件 | 根拠・版 |
| --- | --- | --- |
| [FERMI-SOLVE-A-001：全体回答](details/method-selection.md) | 方法／標準手順として採用済みv2。対象定義から検証・結論まで | 複数型の演習と再input、精度/速度の認定とは別 |
| [FERMI-SOLVE-A-002：検算・感度](details/method-selection.md) | 検証／標準手順として採用済みv2。算術とモデル/独立性を分ける | 係数の裏付けと全体精度は別に評価 |
| [FERMI-SOLVE-A-003：数字を合理的に設定する方法](details/number-setting-methods.md) | 方法／標準手順として採用済みv1。全型の主要係数を左右するためA。根拠選択/補正/加重/類推/制約/代表値/索引/検証 | [無料10資料の比較](input/2026-11-26-06-number-setting-methods.md)と[過去演習再検討](learning/2026-11-26-07-number-methods-retrospective.md)。個々の率/価格の実数精度と新問/速度は未検証 |
| [KNOW-JP-001：人口](../../../shared/knowledge/facts/japan-anchors.md) | 共通概数／採用済み。全国在住者、ラフ1.2億等 | 公的統計確認v1、使用条件あり |
| [KNOW-JP-002：世帯](../../../shared/knowledge/facts/japan-anchors.md) | 共通概数／採用済み。ラフ6000万世帯・2人等 | 国勢調査確認v1、一般世帯の定義あり |
| [KNOW-METHOD-001：集計範囲・分母](../../../shared/knowledge/methods/measurement-boundaries.md) | 共通確認規則／採用済みv1。対象・イベント・実人数・期間を合わせる | 公式定義と演習後の再input |

## B 重要

- [FERMI-FACT-001：道路長と道路部/車道幅](details/rough-anchors.md)：B採用済みv1（公表定義/概数の限定範囲）。一般道路約120万km・道路部約6m/車道約4m。物体の設置率・実間隔は別仮定。
- [FERMI-FACT-002：映画の年量・価格・スクリーン](details/rough-anchors.md)：B採用済みv1（2025年公表値/概数）。約1.9億延べ入場/年・1500円・3700スクリーン。実人数/館数/特定館の稼働とは別。
- [FERMI-FACT-003：世帯機器の保有・買替え調査](details/rough-anchors.md)：B採用済み情報v2（調査対象/定義/概数）。普及率の重掛け・保有と家庭個人利用・買替え世帯旧品年数と年購入率を区別。全国総世帯・別機器への自動流用不可。GYM028/CM-F010初回答はv1使用。
- [FERMI-FACT-004：世帯の食関連支出と分類](details/rough-anchors.md)：B採用済み情報v2。平均支出と利用世帯率・頻度/単価、外食の宅配/持帰り/給食、飲料素材/容器、品目/用途と年計/月平均を区別。全国市場/単身やPET個数へ直接流用不可。

- [FERMI-SOLVE-B-007/008：幾何の分母・能力から生産/出荷への橋渡し](details/geometry-capacity.md)：B候補v1。面積/線/体積、通路/空隙、能力/良品生産/完成在庫/出荷、平均在庫と滞在を区別。今回12問の比較を統合した候補で、初回答当時はFADD/PROD候補を使用。実係数・独立実績・3次元全般・速度は未認定。
- [FERMI-SOLVE-B-006：仮定の根拠・別経路・幅の扱い](details/evidence-and-checks.md)：B候補v1。元情報と橋渡し、共有入力と別観測、感度/シナリオ/上下限を区別。自由係数の実数精度や全型への定着は未確認。既存A-002 v2を補う。
| ID・要点 | 種類・理由 | 状態・適用条件 | 根拠・履歴 |
| --- | --- | --- | --- |
| [FERMI-SOLVE-B-001：制約差のある層で割合を作る](details/constraint-segmentation.md) | 解法・分解／利用や所有の制約差が重要な場合 | 候補、2026-11-25。別問題での再現は未確認 | [GYM-FERMI-001](learning/2026-11-25-01-gym-navigation-pilot.md)。旧状態なし、自己比較から新規。[変更](../../../logs/2026-11-25-research-and-casematch.md)。失効・後継なし |

- [FERMI-SOLVE-B-002：問題型・条件に応じた方法選択](details/method-selection.md)：B候補v2。各分岐の適用/切替/検証条件と演習根拠を対応。未実施枝・仮定根拠を留保。
- [FERMI-SOLVE-B-004/005：stock/更新と時間/群の加重](details/stock-time-weighting.md)：B採用済み情報版v2。調査対象/分母、寿命分布・残存の重み、推奨/行動・販売/装着を補強。条件付き式/定義の採用で、実係数・実数精度は未認定。
- [KNOW-JP-003：年齢の概数](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-JP-004：国土面積](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-JP-005：就業者](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-JP-006：期間換算](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。

- [FERMI-SOLVE-B-003：人流の境界と加重](details/flow-boundaries.md)：B候補v1。東京駅の対象ずれから登録、羽田/列車で転用を自己照合。
- [KNOW-METHOD-002〜004：客室指標/価格、回避支出、工程能力](../../../shared/knowledge/methods/measurement-boundaries.md)：共通B、公式定義・条件付き代数・モデルの範囲で採用済みv1。問題全体の高精度認定とは分ける。
- [KNOW-METHOD-005：状態/実人数・業務量/FTE/移管の境界](../../../shared/knowledge/methods/state-workforce-boundaries.md)：共通B限定採用v2。状態stockと遷移、実人数と換算業務量が関わる場合の定義/条件付き確認。現行制度・効果率・未評価枝は未確定。

- [KNOW-JP-007/008：住宅・車両の概数](../../../shared/knowledge/facts/housing-vehicles.md)：B採用済みv1。時点・居住/空き家・乗用/全車種の条件あり。世帯と戸数、保有と年販売を混ぜない。

- [KNOW-METHOD-006：面積の定義と補集合](../../../shared/knowledge/methods/area-boundaries.md)：共通B限定採用v1。公式の可住地/林野/森林の定義・同一境界の代数を採用。全国比率・画像補正・独立観測成功は未評価。

## C 補足

| ID・要点 | 種類・優先度理由 | 状態・条件 | 根拠 |
| --- | --- | --- | --- |
| [FERMI-REF-C-001：数字設定の参照索引](references/NUMBER_INDEX.md) | 条件付きの例。暗記する基礎概数と独立した補助層なのでC | 参照用v1として登録/本文監査。47参照群の個別実数を一括認定しない。方法からの照合/導出困難時、元条件/性質を確認して使う | [資料ノート](input/2026-11-26-07-number-settings-sources.md)、[39学習問等の全件走査](learning/2026-11-26-08-number-settings-retrospective.md)。新規演習は0 |

追加2IDはいずれも更新2026-11-26、前版/後継なし。変更理由/旧版は[今回のログ](../../../logs/2026-11-26-fermi-numbers-and-support.md)。FNUM行数を正式知識ID数へ足さず、旧演習の使用版へ後付けしない。

## 登録する項目

情報ID、要点、種類、優先度と理由、状態、適用条件、出典・確認日、学習/評価の根拠、詳細・変更履歴・後継へのリンク。失効した情報も状態と後継を残し、現行として利用しない。

[重要情報](CORE.md)／[詳細](details/README.md)／[履歴](HISTORY.md)。登録ルールは[DOCUMENTATION](../../../DOCUMENTATION.md)。

資料・比較ノートの全件は[INPUT](INPUT.md)、全演習は[LEARNING](LEARNING.md)へ。採用済みをA→B→Cで読み、問題に必要な候補も適用条件・未評価範囲を付けて本文へ進む。候補の使用を採用済みへ変更せず、使用版を初回答へ固定する。失効した情報は現行に使わない。方法候補と出典確認済み共通知識を混同しない。
