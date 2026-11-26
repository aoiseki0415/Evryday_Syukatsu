# ケース①｜全情報の索引

状態：初期input→演習→再input→別問題適用を経て標準手順v2へ更新。採用範囲と候補/未評価を枝ごとに分ける。領域全体の十分な精度は未認定。優先度と状態を別に読む。

## A 必須

| ID・要点 | 種類・状態・条件 | 根拠・版 |
| --- | --- | --- |
| [CASE-SOLVE-A-001：回答全体の骨格](details/method-selection.md) | 方法／標準手順として採用済みv2。問い・仮説・比較・結論・検証 | 複数型の演習・再input・転用が根拠。全型の精度認定とは別 |
| [KNOW-JP-001：人口](../../../shared/knowledge/facts/japan-anchors.md) | 共通概数／採用済み。全国在住者、ラフ1.2億等 | 公的統計確認v1、使用条件あり |
| [KNOW-JP-002：世帯](../../../shared/knowledge/facts/japan-anchors.md) | 共通概数／採用済み。ラフ6000万世帯・2人等 | 国勢調査確認v1、一般世帯の定義あり |
| [KNOW-METHOD-001：集計範囲・分母](../../../shared/knowledge/methods/measurement-boundaries.md) | 共通確認規則／採用済みv1。対象・イベント・実人数・期間を合わせる | 公式定義と演習後の再input |

## B 重要

| ID・要点 | 種類・優先度の理由 | 状態・適用条件 | 出典・評価・履歴 |
| --- | --- | --- | --- |
| [CASE-SOLVE-B-001：効果の下振れ境界を目標から逆算](details/target-sensitivity.md) | 検証・結論／定量目標の実行判断に重要 | 候補。目標と施策効果を定量化できる場合。2026-11-25確認 | [CM-TEXT-001](learning/2026-11-25-01-casematch-text-pilot.md)。生成類題1問と計算照合のみ。独立・未見評価なし。[変更](../../../logs/2026-11-25-research-and-casematch.md)。失効・後継なし |

- [CASE-SOLVE-B-002：問題型・条件に応じた方法選択](details/method-selection.md)：v2。枝別に限定採用と候補を区別。適用/切替/検証条件を読み、全分岐を検証済みとしない。
- [CASE-SOLVE-B-003/004/005：コホートと継続採算、行動障害、現行実装と最終指標](details/cohorts-behavior-metrics.md)：条件付きの確認手順として採用済みv2。具体的な原因/介入効果率は未検証。
- [CASE-SOLVE-B-006/007：段階投資の限界判断・複合施策の検証](details/staged-decisions.md)：B006は条件付き確認手順として限定採用v2。追加差と判断基準を接続。B007は候補v1、セット/成分の検証実装は未評価。
- [CASE-SOLVE-B-008：新規事業を設計し仮説を検証](details/new-business-design.md)：B候補v2。利用/支払/決定、提供/課金/費用、役割/月別能力、段階検証を接続。専用3問を比較し、最大枠≠必要投入、事前判定、分岐量と能力/費用を補強。3問目CM-C-014は改訂候補v2を事前使用。実需・独立未見/速度は未確認。
- [CASE-SOLVE-B-009/010：買収・自力と撤退/転用の比較](details/acquisition-exit.md)：両B候補v1。価値と対価、配賦と回避支出、同じ目的/期間と閾値を接続。追加inputと閉条件各1問の比較を根拠とし、複雑な取引/現実の採算は未確認。
- [CASE-SOLVE-B-011/012：原因の識別と、必要全作業/期間の制約照合](details/diagnosis-constraints.md)：両B候補v1。競合仮説ごとの予測/反証、実装/利用/成果/因果と、原文の各/毎/期間→全作業→同期間再集計を整理。C019/022の誤りを予防規則へ抽出し、資料読解のみで独立再現性を認定しない。
- [CASE-SOLVE-B-013：顧客・取引・提供の構造6カード](details/business-structures.md)：B候補v1。物販/継続/仲介/人・施設サービス/B2B/公共の分析入口。誰が利用/支払/決定/提供し何で課金/費用となるかを接続。業界データの網羅や実需を証明したものではない。
- [CASE-MEASURE-B-001〜006：原因条件から選ぶ施策仮説](details/measure-hypotheses.md)：すべてB候補v1。継続価値、購買/訪問障害、制約工程、価格の純増、支援アクセス、技能/業務移管。演習から抽出した作用・費用・最終指標・反証であり、実際の効果率や企業報告の事実とは別。
- [KNOW-METHOD-005：状態/実人数・業務量/FTE/移管の境界](../../../shared/knowledge/methods/state-workforce-boundaries.md)：共通B限定採用v2。状態台帳/時間・技能/移管の定義・条件付き確認。効果率・公的FTEの現行制度・未評価枝は未確定。
- [KNOW-JP-003：年齢の概数](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-JP-004：国土面積](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-JP-005：就業者](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-JP-006：期間換算](../../../shared/knowledge/facts/japan-anchors.md)：共通B、出典・定義確認の範囲で採用済みv1。問題固有の率・頻度は別仮定。
- [KNOW-MEASURE-001：在庫と補充行動](../../../shared/knowledge/measures/mechanisms.md)：共通B、企業公式の事例事実として採用済みv1。転用効果は仮説で演習検証対象。
- [KNOW-MEASURE-002：自動化と運用](../../../shared/knowledge/measures/mechanisms.md)：共通B、企業公式の事例事実として採用済みv1。転用効果は仮説で演習検証対象。
- [KNOW-MEASURE-003：食品ロス](../../../shared/knowledge/measures/mechanisms.md)：共通B、企業公式の事例事実として採用済みv1。転用効果は仮説で演習検証対象。
- [KNOW-MEASURE-004：受取制約](../../../shared/knowledge/measures/mechanisms.md)：共通B、企業公式の事例事実として採用済みv1。転用効果は仮説で演習検証対象。
- [KNOW-MEASURE-005：会費と商品販売を組み合わせる事業構造](../../../shared/knowledge/measures/business-models.md)：共通B、CostcoのFY2025公式報告の事例事実に限定採用v1。会費認識/更新率の母数・経過期間と構成差を確認。転用効果や2026年の現行条件を認定しない。

- [KNOW-METHOD-002〜004：客室指標/価格、回避支出、工程能力](../../../shared/knowledge/methods/measurement-boundaries.md)：共通B、公式定義・条件付き代数・モデルの範囲で採用済みv1。問題全体の高精度認定とは分ける。

- [KNOW-JP-007/008：住宅・車両の概数](../../../shared/knowledge/facts/housing-vehicles.md)：B採用済みv1。時点・居住/空き家・乗用/全車種の条件あり。世帯と戸数、保有と年販売を混ぜない。

- [KNOW-METHOD-006：面積の定義と補集合](../../../shared/knowledge/methods/area-boundaries.md)：共通B限定採用v1。面積・居住域・土地用途を扱う時だけ参照。公式定義と同一境界の代数を採用し、森林率や施策効果は未認定。

## C 補足

未登録。

## 登録する項目

情報ID、要点、種類、優先度と理由、状態、適用条件、出典・確認日、学習/評価の根拠、詳細・変更履歴・後継へのリンク。失効した情報も状態と後継を残し、現行として利用しない。

[重要情報](CORE.md)／[詳細](details/README.md)／[履歴](HISTORY.md)。登録ルールは[DOCUMENTATION](../../../DOCUMENTATION.md)。

資料・比較ノートの全件は[INPUT](INPUT.md)、全演習は[LEARNING](LEARNING.md)へ。現在使う本文は上表で「採用済み」をA→B→Cにたどり、候補・失効とは分けて読む。方法候補と出典確認済み共通知識を混同しない。
