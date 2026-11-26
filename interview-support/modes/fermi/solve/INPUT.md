# フェルミ①｜回答全体を解く：input

## 2026-11-26：数字設定の追加調査

- [INPUT06：数字を合理的に設定する方法](input/2026-11-26-06-number-setting-methods.md)：教育/統計/推計の無料10資料。実読範囲/共通性/相違/採否と未読を記録。
- [INPUT07：設定例の公開資料と過去演習](input/2026-11-26-07-number-settings-sources.md)：公開例/価格表と旧演習の設定を照合。[設定例索引](references/NUMBER_INDEX.md)へ。
- ①の手順本文、設定例の参照層、資料比較と過去演習再検討を分離。今回は新規問題/新しい精度評価を追加しない。

状態：複数発行者の無料本文を読んだ初期input v1を保存。網羅的な調査の完了ではなく、演習差分から再調査する。実績と採用状態はLEARNING・INDEXを参照。

## 対象

- 推定問題の種類、適した分解・推定方法、式を選ぶ条件と例外。
- 人口等のラフな値、単位・地域・期間・定義、使える条件、確認値・出典・丸め方。
- 変数と仮定、代入計算、単位換算、重複・漏れ・桁の誤りを防ぐ方法。
- 結果の妥当性、上下限や別推定との比較、仮定の変更による影響の確認方法。
- 提供教材の解答・解説・採点観点、誤答と修正例、再利用可能なルールと例外。

## 収集・参照のルール

共通の[①実行仕様](../../../learning/SOLVE_WORKFLOW.md)と[カバレッジ](../../../learning/COVERAGE.md)に沿う。読解・比較は[資料ひな形](../../../templates/SOURCE.md)からinput/へ保存し、ここへ全件の参照を残す。比較後に再利用する解法・知識はdetails/または共通知識へ置き、INDEXへ登録する。inputノートを現行の知識本文と混同しない。

資料ごとにsource_id、題名・版、参照箇所、要点、適用条件、確認日、確定/候補/失効を記録する。教材の所在と問題・解答・解説の有無は[共通台帳](../../../shared/materials/README.md)を参照する。

両モードで使える知識の本文は[shared/knowledge](../../../shared/knowledge/README.md)に置き、ここから参照する。①の全体回答・解法を②へ全文複製しない。元資料や採用済みの知識と区別して保存する。

## 登録済みの情報

- [FERMI-INPUT-20261126-05：PC更新の再input](input/2026-11-26-05-pc-renewal-followup.md)：CM-F010原案後、同じ内閣府PDFの表5を追加実読。買替え世帯の旧品平均年数と、全stockの年齢/物理寿命/年購入率を区別してFACT003情報v2へ。

- [FERMI-INPUT-20261126-03：演習の係数不足から分野別アンカーへ](input/2026-11-26-03-assumption-anchors.md)：道路長/幅、映画の年量/価格/供給単位、機器普及/保有、世帯食関連支出の一次資料。観測値・ラフ値・橋渡し・感度と取得不能を分離し、FACT001–004へ。
- [FERMI-INPUT-20261126-04：食関連分類の再input](input/2026-11-26-04-food-boundaries-followup.md)：公式分類XLSX/利用案内を追加確認。飲食店の宅配/持帰りと学校給食、調理食品、飲料素材、年計/月平均を区別。カード初版や過去原案へ事前使用を遡及しない。

- [生産・出荷・在庫と工程能力の再input](input/2026-11-26-02-production-flow.md)：段ボールの比較後、e-Statの用語とNISTの工程資料へ戻った。生産P/出荷S/完成在庫と、最終工程能力/全体達成を区別。実工場数・実稼働・本問の正答実数は未調査。
- [AREA-DEF-INPUT-20261126-01：森林演習後の定義再input](../../../shared/knowledge/input/2026-11-26-area-definitions.md)：統計局2資料の指定箇所。可住地/林野/森林、補集合と独立検算の違い。実面積/森林率は調査せず、KNOW-METHOD-006へ定義だけを整理。
- [FERMI-ADD-INPUT-20261126-01：面積/密度・物理量/能力の追加input](input/2026-11-26-01-additional-methods.md)：公式/教育5資料の指定範囲。線/面積/体積、能力の分母、自由係数の説明を候補化。資料の例・全国稼働率を本問の実係数へ置換しない。
- [FERMI-PHOTO-INPUT-20261125：写真プリント問題後の再input](input/2026-11-25-photo-print-followup.md)：一次4資料群で商品/経路/受取/送料、経験調査の分母、広い市場見込の範囲を確認。年間利用世帯率/同対象売上は取得できず、全国平均/新アンカーへ採用しない。
- [FERMI-INDEPENDENT-INPUT-20261125：自由係数・幅・独立照合の再input](input/2026-11-25-independent-check-followup.md)：無料一次3文書の限定範囲。元情報/橋渡し/仮定、別方法・別担当・別観測の違い、制約/感度/シナリオを整理。A/Bの現行版は不変で、候補の実適用は演習へ分離する。
- [FERMI-STOCK-INPUT-20261125：タイヤ交換後の再input](input/2026-11-25-stock-transfer-followup.md)：3一次資料の指定範囲、調査対象/設問・状態/推奨/行動・寿命分布/重み。初回答の係数や1200万本を実証した資料とはしない。
- [住宅・車両の追加アンカーinput](../../../shared/knowledge/input/2026-11-25-additional-anchors.md)：公的な定義/時点、粗い数と未採用の探索入口。
- [共通Care再input](../../../shared/knowledge/input/2026-11-25-care-followup.md)：状態stockと遷移、実人数/時間/FTEの境界。METHOD-005本文へ接続。
- [演習後の再input](input/2026-11-25-feedback-methods.md)：stock/flow・寿命、道路区分、平均と加重、現存と必要配置。一次/公式6資料、採用範囲と保留を分離。
- [共通の測定・収益・工程の再input](../../../shared/knowledge/input/2026-11-25-followup-definitions.md)：駅・分母のずれ、期間、能力と実量を確認。

- [FERMI-INPUT-20261125-METHODS：初期input・複数資料比較](input/2026-11-25-initial-methods.md)：CaseMatch・ジム・教育資料等の読解範囲と方法の違いを保存。初期候補v1へ統合した経緯を保持し、[現在の全体回答・型選択・検算の本文v2](details/method-selection.md)から旧版の固定Git履歴へ戻れる。
- [概数アンカーの一次確認ノート](../../../shared/knowledge/input/2026-11-25-facts-measures.md) → [ラフ値と定義の本文](../../../shared/knowledge/facts/japan-anchors.md)。

- [CM-ART-01：評価観点のinputノート](input/2026-11-25-casematch-evaluation.md)。本文確認済み、資料読解と採用済み解法を分離。
- [CM-001／GYM-001の台帳](../../../shared/materials/README.md)。同等の主要演習先。GYM-001は[1問の比較記録](learning/2026-11-25-01-gym-navigation-pilot.md)あり。

公開/非公開の範囲を守り、原資料の全文を公開GitHubへ複製しない。記事内の細かい数字をそのまま覚えるのではなく、ラフな値・定義・時点・使える条件を整理する。
