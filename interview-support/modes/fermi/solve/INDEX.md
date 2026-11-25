# フェルミ①｜全情報の索引

状態：初期input→演習→再input→別問題適用を経て標準手順v2へ更新。型選択の候補と、定義/条件付き式の採用を区別する。領域全体の十分な精度は未認定。優先度と状態を別に読む。

## A 必須

| ID・要点 | 種類・状態・条件 | 根拠・版 |
| --- | --- | --- |
| [FERMI-SOLVE-A-001：全体回答](details/method-selection.md) | 方法／標準手順として採用済みv2。対象定義から検証・結論まで | 複数型の演習と再input、精度/速度の認定とは別 |
| [FERMI-SOLVE-A-002：検算・感度](details/method-selection.md) | 検証／標準手順として採用済みv2。算術とモデル/独立性を分ける | 係数の裏付けと全体精度は別に評価 |
| [KNOW-JP-001：人口](../../../shared/knowledge/facts/japan-anchors.md) | 共通概数／採用済み。全国在住者、ラフ1.2億等 | 公的統計確認v1、使用条件あり |
| [KNOW-JP-002：世帯](../../../shared/knowledge/facts/japan-anchors.md) | 共通概数／採用済み。ラフ6000万世帯・2人等 | 国勢調査確認v1、一般世帯の定義あり |
| [KNOW-METHOD-001：集計範囲・分母](../../../shared/knowledge/methods/measurement-boundaries.md) | 共通確認規則／採用済みv1。対象・イベント・実人数・期間を合わせる | 公式定義と演習後の再input |

## B 重要

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

## C 補足

未登録。

## 登録する項目

情報ID、要点、種類、優先度と理由、状態、適用条件、出典・確認日、学習/評価の根拠、詳細・変更履歴・後継へのリンク。失効した情報も状態と後継を残し、現行として利用しない。

[重要情報](CORE.md)／[詳細](details/README.md)／[履歴](HISTORY.md)。登録ルールは[DOCUMENTATION](../../../DOCUMENTATION.md)。

資料・比較ノートの全件は[INPUT](INPUT.md)、全演習は[LEARNING](LEARNING.md)へ。現在使う本文は上表で「採用済み」をA→B→Cにたどり、候補・失効とは分けて読む。方法候補と出典確認済み共通知識を混同しない。
