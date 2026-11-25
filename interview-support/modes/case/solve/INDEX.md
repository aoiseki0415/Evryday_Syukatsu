# ケース①｜全情報の索引

状態：初期input v1と方法候補を登録。共通概数/事例は確認済みの範囲で採用。領域の十分な精度は未評価。優先度と状態を別に読む。

## A 必須

| ID・要点 | 種類・状態・条件 | 根拠・版 |
| --- | --- | --- |
| [CASE-SOLVE-A-001：回答全体の骨格](details/method-selection.md) | 方法／候補。問い・仮説・比較・結論・検証 | 初期input比較v1、演習検証へ |
| [KNOW-JP-001：人口](../../../shared/knowledge/facts/japan-anchors.md) | 共通概数／採用済み。全国在住者、ラフ1.2億等 | 公的統計確認v1、使用条件あり |
| [KNOW-JP-002：世帯](../../../shared/knowledge/facts/japan-anchors.md) | 共通概数／採用済み。ラフ6000万世帯・2人等 | 国勢調査確認v1、一般世帯の定義あり |


| [KNOW-METHOD-001：集計範囲・分母](../../../shared/knowledge/methods/measurement-boundaries.md) | 共通確認規則／採用済みv1。対象・イベント・実人数・期間を合わせる | 公式定義と演習後の再input |

## B 重要

| ID・要点 | 種類・優先度の理由 | 状態・適用条件 | 出典・評価・履歴 |
| --- | --- | --- | --- |
| [CASE-SOLVE-B-001：効果の下振れ境界を目標から逆算](details/target-sensitivity.md) | 検証・結論／定量目標の実行判断に重要 | 候補。目標と施策効果を定量化できる場合。2026-11-25確認 | [CM-TEXT-001](learning/2026-11-25-01-casematch-text-pilot.md)。生成類題1問と計算照合のみ。独立・未見評価なし。[変更](../../../logs/2026-11-25-research-and-casematch.md)。失効・後継なし |

- [CASE-SOLVE-B-002：問題型・条件に応じた方法選択](details/method-selection.md)：B候補v1。各分岐の適用/切替/検証条件付き。全分岐の演習検証はこれから。
- [KNOW-JP-003：年齢の概数](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-JP-004：国土面積](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-JP-005：就業者](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-JP-006：期間換算](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-MEASURE-001：在庫と補充行動](../../../shared/knowledge/measures/mechanisms.md)：共通B、企業公式の事例事実として採用済みv1。転用効果は仮説で演習検証対象。
- [KNOW-MEASURE-002：自動化と運用](../../../shared/knowledge/measures/mechanisms.md)：共通B、企業公式の事例事実として採用済みv1。転用効果は仮説で演習検証対象。
- [KNOW-MEASURE-003：食品ロス](../../../shared/knowledge/measures/mechanisms.md)：共通B、企業公式の事例事実として採用済みv1。転用効果は仮説で演習検証対象。
- [KNOW-MEASURE-004：受取制約](../../../shared/knowledge/measures/mechanisms.md)：共通B、企業公式の事例事実として採用済みv1。転用効果は仮説で演習検証対象。

- [KNOW-METHOD-002〜004：客室指標/価格、回避支出、工程能力](../../../shared/knowledge/methods/measurement-boundaries.md)：共通B、公式定義・条件付き代数・モデルの範囲で採用済みv1。問題全体の高精度認定とは分ける。

## C 補足

未登録。

## 登録する項目

情報ID、要点、種類、優先度と理由、状態、適用条件、出典・確認日、学習/評価の根拠、詳細・変更履歴・後継へのリンク。失効した情報も状態と後継を残し、現行として利用しない。

[重要情報](CORE.md)／[詳細](details/README.md)／[履歴](HISTORY.md)。登録ルールは[DOCUMENTATION](../../../DOCUMENTATION.md)。

資料・比較ノートの全件は[INPUT](INPUT.md)、全演習は[LEARNING](LEARNING.md)へ。現在使う本文は上表で「採用済み」をA→B→Cにたどり、候補・失効とは分けて読む。方法候補と出典確認済み共通知識を混同しない。
