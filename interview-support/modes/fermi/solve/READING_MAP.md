# フェルミ①｜情報の構造と本文への読込地図

更新2026-11-26。これは①の情報配置を示す案内。**準備をいつ/どう実施するかの仕様は[②preparation](../support/details/preparation.md)**にあり、ここへ二重管理しない。正式な全項目と状態は[INDEX](INDEX.md)、短い必須要約は[CORE](CORE.md)。

```text
①の現行情報
 ├─ 基本の解法/検算       → details/method-selection
 ├─ 数字を決める方法     → details/number-setting-methods
 ├─ 基礎概数/分野の定義  → shared/facts・details/rough-anchors
 ├─ 型別の方法/条件      → details + shared/methods
 └─ 条件付き設定例       → references/NUMBER_INDEX → 用途別の行

根拠/過程は別層
 ├─ 資料をどう読んだか   → INPUT → input/
 ├─ 演習/再検討の証拠    → LEARNING → learning/
 └─ 議論/変更/旧版       → HISTORY → logs/・archive・固定Git
```

## 全30IDと本文の対応

以下は同じ本文に入る項目を束ねた案内。優先度と採否はINDEX/各本文を正本とし、ここで別の評価をしない。NSの7枝やFNUMの47行は新しい正式ID/演習数ではない。

| 情報のグループ | 正式ID（重複なし） | 読む本文・復元すること |
| --- | --- | --- |
| 全体回答/検算/型選択：3 | FERMI-SOLVE-A-001/002、B-002 | [method-selection](details/method-selection.md)。標準v2と型分岐候補v2を分ける |
| 数字設定方法：1 | FERMI-SOLVE-A-003 | [number-setting-methods](details/number-setting-methods.md)。根拠→橋渡し→値と検算。手順v1の採用で実数認定ではない |
| 型別の詳細：7 | FERMI-SOLVE-B-001/003/004/005/006/007/008 | [制約層](details/constraint-segmentation.md)、[人流](details/flow-boundaries.md)、[stock/更新/時間群加重](details/stock-time-weighting.md)、[根拠/幅/独立性](details/evidence-and-checks.md)、[幾何/能力](details/geometry-capacity.md)。条件付き採用と候補を区別 |
| 分野の概数/定義：4 | FERMI-FACT-001〜004 | [rough-anchors](details/rough-anchors.md)。道路/映画/機器/食関連支出。観測対象と今回の外挿を分ける |
| 共通基礎概数：8 | KNOW-JP-001〜008 | [人口/世帯/年齢/国土/就業/期間](../../../shared/knowledge/facts/japan-anchors.md)、[住宅/車両](../../../shared/knowledge/facts/housing-vehicles.md)。ラフ値/単位/時点/適用条件 |
| 共通の定義/確認：6 | KNOW-METHOD-001〜006 | [集計/料金/支出/工程](../../../shared/knowledge/methods/measurement-boundaries.md)、[状態/人数/業務量](../../../shared/knowledge/methods/state-workforce-boundaries.md)、[面積/補集合](../../../shared/knowledge/methods/area-boundaries.md)。必要な境界を本文から理解 |
| 条件付き数字例：1 | FERMI-REF-C-001 | [NUMBER_INDEX](references/NUMBER_INDEX.md)。利用/所有率、価格、空間/能力、頻度/更新、公開例へ。重要な基礎数値と独立した参照層 |

## 重みと取り扱い

- COREのAを最優先に理解し、INDEXで全体を把握する。Bの候補を飛ばさず、何に使えるか/何が未検証かまで確認する。
- Cの設定例は、方法から作った値の照合または導出困難時の補助。係数の原案/教材/観測/与件の性質と、対象条件を先に見る。
- 例を大量に覚えることで重要な方法・概数を埋もれさせない。一方、低優先度を理由に参照先から消さない。
- 元の演習全件はLEARNINGから辿れるが、通常の準備で全履歴を毎回読む必要はない。現行本文と最新の訂正/不足を読み、必要な根拠だけ遡る。
- 情報数や読了数だけで全型の精度/速さを保証しない。方法の新規適用/実数/速度の未検証は[READINESS](../../../learning/READINESS.md)に保持する。

本文追加/失効時はINDEXとこの地図の到達範囲を合わせ、②の準備ルートとの整合を確認する。詳細な作業結果は[今回の監査](../../../learning/audits/2026-11-26-fermi-numbers-support-audit.md)へ。
