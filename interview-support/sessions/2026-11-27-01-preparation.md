# SESSION-FERMI-005：新チャットでの支援準備

日付：2026-11-27 JST。mode: fermi、purpose: ②の準備確認。本人の依頼は「フェルミ推定のサポート」「最初に運用ドキュメントを確認して準備」。お題・解答・本人評価はまだない。

## 参照版と実施範囲

- Gitルート、main、指定origin、既存変更を確認し、`git pull --ff-only origin main`はAlready up to date。読込基準は`716aca4c5d9172e46e6416125b6dcf55c7310af9`。既存の未追跡`.DS_Store`は操作対象外。
- 親のAGENTS、READMEの現在の運用、HANDOFF、STRATEGY、OPERATIONS、logs/READMEを確認。その後、本領域のAGENTS、START_HERE、SPEC、OPERATIONS、ROADMAP、READINESS、DOCUMENTATION、INFORMATION_MAP、ready、フェルミPLAYBOOKへ進んだ。
- [準備手順A-002 v1](../modes/fermi/support/details/preparation.md)に従い、以下の本文を実読。索引への到達だけを本文の読了としない。

| 読込対象 | 確認した本文・版と範囲 |
| --- | --- |
| フェルミ②・全4ID | CURRENT→CORE→INDEX、[workflow](../modes/fermi/support/details/workflow.md)／preparationはv1、[initial-response](../modes/fermi/support/details/initial-response.md)はA-003 v2・B-001 v1 |
| フェルミ①・全30IDの地図 | CURRENT→CORE→READING_MAP→INDEX→details一覧。A6/B23/C1の分類・採否・適用条件を確認 |
| 全体回答・検算・型選択 | [method-selection](../modes/fermi/solve/details/method-selection.md)：A-001/002標準v2、B-002候補v2 |
| 数字設定 | [number-setting-methods](../modes/fermi/solve/details/number-setting-methods.md)：A-003 v1、NS-01〜07と設定後の確認 |
| 型別の本文 | [制約層](../modes/fermi/solve/details/constraint-segmentation.md)B-001候補v1、[人流](../modes/fermi/solve/details/flow-boundaries.md)B-003候補v1、[stock/時間加重](../modes/fermi/solve/details/stock-time-weighting.md)B-004/005情報v2、[根拠/独立性](../modes/fermi/solve/details/evidence-and-checks.md)B-006候補v1、[幾何/能力](../modes/fermi/solve/details/geometry-capacity.md)B-007/008候補v1 |
| 基本・分野概数 | [人口等](../shared/knowledge/facts/japan-anchors.md)KNOW-JP001〜006 v1、[住宅/車両](../shared/knowledge/facts/housing-vehicles.md)007/008 v1、[rough-anchors](../modes/fermi/solve/details/rough-anchors.md)FACT001/002情報v1・003/004情報v2 |
| 共通の定義 | [集計/価格/支出/工程](../shared/knowledge/methods/measurement-boundaries.md)METHOD001〜004 v1、[状態/実人数/業務量](../shared/knowledge/methods/state-workforce-boundaries.md)005限定採用v2、[面積](../shared/knowledge/methods/area-boundaries.md)006限定採用v1 |
| 設定例 | [NUMBER_INDEX](../modes/fermi/solve/references/NUMBER_INDEX.md)：C-001参照用v1、全47群の分類・所在・利用規則を確認。各群の個別値/根拠/移植条件は使用時に本文を読む |
| 訂正・不足・探索 | solve/supportのHISTORY、②LEARNINGと直近2評価、READINESS、CYCLES、[最新構造監査](../learning/audits/2026-11-26-fermi-numbers-support-audit.md)、[PATHS](../shared/research/PATHS.md) |

## このチャットで復元した支援手順

準備→お題受領→対象/期間/単位を定義→方法選択と合理的な数字設定→全体回答を完算・点検→初回共有。所有/存在、利用/販売、売上、必要量、面積/体積、能力から適切な主経路を選ぶ。

初回共有は対象/結果→番号付き日本語式の段階展開→短い式/数字の理由。数値代入を含め最大4行、数字は最後の行だけ、直前の1要素に1値。要素名に期間と1人/1回等の分母を明示する。

## 確認範囲と未評価

- 準備手順の本文読込は完了。お題を受け取った後は、準備一式の再読を初回回答前に挟まない。
- 今回は問題を解いておらず、①演習・固定評価・②の問題実践へ加算しない。①全体の精度、現行形式での支援品質、初回10秒以内は今回未評価。
- モデル/思考量/Fastは文書の方針のみ確認し、実設定の確認・変更や比較は行っていない。読込記録を本番性能の検証成功としない。
- 保存済み概数の定義/時点を確認したが、外部統計を今回再取得した記録ではない。候補の採否、未観測係数、独立実測の不足は維持。過去の全演習/全設定例本文の再読は行っていない。
- 初回後の追加質問の具体仕様は未策定のまま。今回は新しい運用合意・知識改訂がないためNotionは編集しない。親文書・READINESSの性能認定も変更しない。

次は本人のお題を文字またはスクショで受け取り、現行A-003 v2で初回共有する。
