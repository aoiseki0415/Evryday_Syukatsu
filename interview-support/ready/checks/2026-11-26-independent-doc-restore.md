# cycle003後の会話履歴なし文書復元確認

確認日：2026-11-26。面接チャットの過去履歴を渡さない別担当が、`START_HERE.md`を入口に保存本文と必要な原記録を読み、主担当へ報告した。Git/ネットワーク/UI/Notionを操作せず、文書の読取と固定snapshotのSHA計算のみ。主担当がこの記録を保存した。新規Workの起動、未知問題への回答、実数の精度/速度、本番②の実証ではない。新規演習・自作診断のどちらにも加算しない。

## 復元できた理解

| 項目 | 別担当が復元した内容 | 根拠 |
| --- | --- | --- |
| 目的/範囲 | アプリを作らず新Workで文書から支援へ。①は全体回答、②は本人への切り出し/途中適応。ケース内推定はケースを維持。両①の精度確認後②へ、現在①未認定/②未開始 | [SPEC](../../SPEC.md)、[OPERATIONS](../../OPERATIONS.md) |
| 現在の演習 | 82＝ケース43（CM15/ジム28）＋フェルミ39（CM11/ジム28）、49＋25＋8。固定留保8/旧試行2/旧文書診断2/同題修正/重複は非加算 | [EXERCISES](../../learning/EXERCISES.md)、[READINESS](../../learning/READINESS.md) |
| 情報の単位/採否 | 53＝case20＋Fermi14＋shared19。case参照39＋Fermi参照28−共通14。A6/B47、採用限定32/枝混在1/候補20。カード数≠値/式/資料/演習数。優先度≠採否、必要候補を条件付きで読んでも採用へしない | [監査](../../learning/audits/2026-11-26-information-audit.md)、[両INDEXへの入口](../../learning/CYCLES.md) |
| 現行版 | ケースB011候補v2/B012候補v1/B013候補v2（7業態は公式網羅分類ではない）。FACT001/002は情報v1・003/004は情報v2。A標準v2は不変 | [診断/制約](../../modes/case/solve/details/diagnosis-constraints.md)、[事業構造](../../modes/case/solve/details/business-structures.md)、[概数](../../modes/fermi/solve/details/rough-anchors.md) |
| 概数の適用 | 観測/丸め/仮定を区別。道路の対象、映画延べ入場、全世帯平均への普及率重掛け禁止、選ばれた買替旧品年数≠全stock寿命、外食/持帰り/給食/調理食品・飲料素材、単身/全国/料金等の橋渡し | [概数本文](../../modes/fermi/solve/details/rough-anchors.md)、[共有基数](../../shared/knowledge/README.md) |
| サイト評価の性質 | 2サイトは同等の主要先。初回答を先に保存、CMは実送信要約へのAI講評と全文自己比較、Gymは解説要点との自己比較。同式再計算/丸め一致≠独立実測。毎問二重提出/機械的半々ではない | [実行手順](../../learning/SOLVE_WORKFLOW.md)、[今回の実サイクル](../../learning/cycles/2026-11-26-02-information-quality.md) |
| 最新/履歴の分離 | 原案使用版→講評→原案の自己判定→同問訂正→再input/本文改訂→別問をたどれる。後の結果を旧原案/旧固定留保へ戻さない | 下の原証拠の抜き取り確認 |

## 原証拠まで戻った確認

- [CM015](../../modes/case/solve/learning/2026-11-26-06-casematch-diagnosis.md)：B011/B013 v1の事前使用、送信時対象補足、AI講評と原案要改善、J-PAL再input→B011v2を追跡。
- [CM016](../../modes/case/solve/learning/2026-11-26-07-casematch-constraints.md)：初回答のA3h/B2h・共通各2h、上界A2/B4、土A5/B6・日A3/B4を実読し、100人回/10万円という閉条件の結果と整合。
- [旧C022](../../modes/case/solve/learning/2026-11-26-01-gym-additional.md)：準備/片付け「各5分」と週35分の不一致、字義では50分＞45分、前後合計5分の35分は後の修正版/未再評価を確認。
- [GYM-C027](../../modes/case/solve/learning/2026-11-26-08-gym-information-transfer.md)：継続と対象流出の二重控除の恐れを原案に残し、排他的な状態式を別節訂正したことを確認。
- [CM-F011](../../modes/fermi/solve/learning/2026-11-26-06-casematch-takeout.md)：約2.3兆円の原案、要約のAI同式再計算、会費配賦の補足が別節。単身/本体構成/料金等の実数精度未確認を保持。
- 旧[B011/012 v1](../../archive/2026-11-26-diagnosis-constraints-v1.txt)と[Fermi事前使用v2](../../archive/2026-11-26-fermi-anchors-v2-used.txt)を実際にhash計算し、記録の`a35a470e…99b3`/`2233c850…1400`と一致。

## 発見と主担当の修正確認

読取時、COVERAGEの一部に「現在74問」、両CURRENTにcycle002のみの追加経路、監査追査末尾に8問統合中の記述が残った。主担当へ通知し、現在82/旧cycle002の履歴を分け、両CURRENTをCYCLES/003へ修正した。監査担当の最終追査は別記録へ。別担当が修正後の全ページ/Notion/Git反映まで確認したとは扱わない。

主担当は別途、Git`2ffa58f`のB013初版/FACT初版hash一致と、同commitのCM015/016初回答節が現在本文と文字列一致することを確認した。これは別担当のGit読取結果ではなく主担当の検証。

## 残る課題

銀行状態式/因果設計の異型反復、全国/現年/単身/個人利用の橋渡し、対象構成/料金等の支配的係数と同対象観測、実需/効果/費用、独立図表/一般物理3D・複雑工程/非定常、固定版の独立反復と条件をそろえた速さ。文書だけから現行の理解/留保を復元できた範囲の確認であり、完全な記憶継承や広い問題精度を保証しない。
