# ①の情報を文書から取り出す確認

確認日：2026-11-26。基準Git `7461e7b0aa39840abed9ee4bdc8fe873cb3e047f`。詳細は[情報監査](../../learning/audits/2026-11-26-information-audit.md)。これは保存文書に根拠を限定した**参照経路・内容の机上確認**であり、担当の実行コンテキストを会話履歴から隔離した実験ではない。新規Work起動、本番②、未知問題の独立評価、速度の実測を行ったという意味ではない。演習件数へ加えない。

## 読んだ順序

AGENTS→START_HERE→SPEC/OPERATIONS→DOCUMENTATION/INFORMATION_MAP→ready/READMEとSOLVE_RESTORE→両solveのCURRENT/CORE/INDEX→必要なdetails/共通知識→READINESS/COVERAGE→演習と更新根拠。初回答時の使用版と現在版は分けて読んだ。

## 文書から復元できた理解

| 確認する問い | 保存文書から復元した答え | 根拠 |
| --- | --- | --- |
| ①と②、ケースと単独推定の境界 | ①は回答全体。②は本人への短い初手と途中適応。ケース内推定はケースを維持。現在②未開始、①全体精度未認定 | [SPEC](../../SPEC.md)、[READINESS](../../learning/READINESS.md) |
| 何を読むと現在の知識になるか | CURRENTは案内、COREは採用A要約、INDEXは候補込み全情報、正本はdetails/shared。input・演習・HISTORYは過程/証拠 | [DOCUMENTATION](../../DOCUMENTATION.md)、両solveのINDEX |
| 問題の種類で方法は変わるか | ケースは目的/指標からC1〜C8を選び切替。フェルミはstock/flow/金額と母数/方法/境界で式を選ぶ。全問題へ同じ型を強制しない | [ケース方法](../../modes/case/solve/details/method-selection.md)、[フェルミ方法](../../modes/fermi/solve/details/method-selection.md) |
| 概数は何か | 人口1.2億、世帯6000万/2人、面積38万km²等のラフな基数と、確認した公表値/定義/時点を分ける。利用頻度/単価は自動で決まらない | [基数本文](../../shared/knowledge/facts/japan-anchors.md)、[住宅/車両](../../shared/knowledge/facts/housing-vehicles.md) |
| 予算3000万円・最大5人の新規事業なら最初から全投入か | 最大枠は投入義務ではない。顧客/支払/提供/コストを設計し、小さい検証・事前判断条件・能力/費用と段階投入を比較。B008は候補v2、実需が実証されたわけではない | [事業設計](../../modes/case/solve/details/new-business-design.md)、[013→014の証拠](../../modes/case/solve/learning/2026-11-26-05-casematch-unwanted-items.md) |
| 倉庫の同時収容38400箱は年出荷上限か | それだけでは年量は決まらない。平均在庫28800箱、同対象の平均滞在10稼働日、定常/入出庫等の仮定を加えると日2880、250日で72万箱という条件付き模型。荷捌きや需要の達成は別 | [幾何/能力](../../modes/fermi/solve/details/geometry-capacity.md)、[CM-F009](../../modes/fermi/solve/learning/2026-11-26-03-casematch-warehouse.md) |
| 制約を破った原案の訂正をどう読むか | C022の準備/片付け各5分なら週50分で可用45分を破る。合計5分として35分へ変えた後の模型で、原案が最初から適切だったとしない | [ケース追加原案・比較](../../modes/case/solve/learning/2026-11-26-01-gym-additional.md)、[READINESS](../../learning/READINESS.md) |
| 74問と45情報IDは何が違うか | 74は学習演習の証拠数。45は共有IDを除重複した現在の再利用カード数。固定留保8/旧試行/復元診断は別。いずれも精度の得点ではない | [演習台帳](../../learning/EXERCISES.md)、[監査の数え方](../../learning/audits/2026-11-26-information-audit.md) |

## 検出した不整合

- AGENTS/START_HERE/SPEC/learning-CURRENTにはcycle001実行中の現在地が残っていた。README/READINESSと到達先を照合すれば74問/cycle002まで復元できるが、入口単独では古い状態を渡す。
- SOLVE_RESTOREの「B008/B006いずれも候補v1」は、ケースB008候補v2と不整合。面積定義/幾何能力/買収撤退の新しい本文も条件付きの最小読込表から漏れていた。INDEXを内容まで読むと到達できるので、正式索引の欠落とは区別する。
- この確認で「保存文書から何を参照すればよいか」は点検できた。未見の広い題への回答精度や、実際の新チャットでの復元成功を証明したものではない。

## 統合後の読み戻し

主担当の更新後に、上記の旧記述・現行版・新たな知識/根拠への経路を再確認し、実際に読んだ範囲を追記する。旧版を読んだ本記録の事実は書き換えない。
