# フェルミ①｜数字設定方法の資料比較

更新：2026-11-26。note_id：FERMI-INPUT-NUM-20261126。無料公開部分を実読した記録。正式な手順本文と、過去問の設定例索引を混ぜない。新規問題演習は実施しない。

## 節目1：一次・教育資料を実読した時点

検索結果の紹介だけで採用せず、以下の原ページ/原PDFを開いた。確認日は全て2026-11-26。既存資料を再確認したものも含み、「新しい独立資料」の数を成果指標にしない。

| source_id・資料 | 実読範囲 | 比較に使う内容 | 採用の限界 |
| --- | --- | --- | --- |
| NUM-S01：[OpenStax University Physics 1 §1.5](https://openstax.org/books/university-physics-volume-1/pages/1-5-estimates-and-fermi-calculations) | 章本文の推定戦略、長さ→面積/体積、密度、上下限、幾何平均、有効数字、妥当性確認。海洋の例は方法説明として参照し解き直さない | 未知の量を馴染みのある小さな量へ分解。正の量を桁の上下から挟むときの幾何平均、丸め、単位検証 | 物理教育の方法であり、利用率/平均価格の実数を保証しない。幾何平均をすべての平均や価格の中央へ自動採用しない |
| NUM-S02：[University of Maryland Physics 374 Estimation](https://www.physics.umd.edu/courses/Phys374/fall05/content/2/pstruc/estimation.htm) | 全文、とくに課題の4つの条件と、草密度を身近な尺度から導く説明 | 数字だけの仮定と、観察に対応した導出を区別。1〜2桁の計算と前提の説明 | 2005年授業の「検索禁止」はその課題の条件であり本運用へ導入しない。人間の実体験を求める教材をCodexの架空体験へ置換しない |
| NUM-S03：[UC Berkeley Sense & Sensibility & Science §8.2](https://sensibility.berkeley.edu/index.php?title=8.2_Fermi_Problems) | 公開本文のLesson in Context、Takeaways、分解の4手順、記載された類推例。会員限定Additional Contentは未読 | 直接わからない量を推定可能な要素へ分解し、概算と上下限から主張を点検する | 教育用の類推例は説明モデル。例の価格・給与等を現在の日本の実測値へ転用しない |
| NUM-S04：[Statistics Canada, Non-probability sampling](https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch13/nonprob/5214898-eng.htm) | 導入、Convenience、Volunteer、Judgement、Quota各節 | 身近な集団の便利標本、参加・選択の偏り。層の人数を合わせても層内の選択偏りが残り得る | 自由な標本から全国率や統計的誤差を確定しない。補正を仮置きしたなら仮定のまま |
| NUM-S05：[ONS, Sample design and estimation](https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/sampledesignandestimation) | Summary、Sample design、Estimation、Aims。2016年更新の方法説明 | 母集団、抽出台帳、層・抽出、回答の重み付け、補助情報と分散を区別 | ONSの調査設計に関する説明。仮想的な層別値を重み付けするだけで、公式調査と同じ代表性を得たことにしない |
| NUM-S06：[NASA CEH v4 Appendix C](https://www.nasa.gov/wp-content/uploads/2020/07/ceh_appc.pdf) | C-1〜C-5（PDF1〜5ページ）の方法選択・比較表・Analogyと補正根拠の節。42ページ全体と回帰導出は未読 | 類推・関係式・積上げをデータ/対象/時間に応じて選ぶ。類似対象との差、線形の成立条件、補正根拠を明示 | 2015年費用推計の指針から方法を参照。単なる比例仮定を統計回帰の検証済みモデルと呼ばない |
| NUM-S07：[GAO-20-195G](https://www.gao.gov/products/gao-20-195g) | 公開概要のFast Facts/Highlightsと推計工程。全文476ページ/accessible517ページは今回未読 | 目的/範囲、前提、データ、方法、感度、記録、実績更新の接続 | 概要の確認範囲のみ。本文の細部を今回再読したという証拠にはしない。既存B006の出典と重複 |
| NUM-S08：[Analysts Uncertainty Toolkit ch.5](https://analystsuncertaintytoolkit.github.io/UncertaintyWeb/chapter_5.html) | inputsの幅/専門家判断、dominant uncertainty、scenario、judgement。Monte Carlo/convolution等の紹介は確認したが本番手順へ実装しない | 主観的な幅と確率の差、整合したシナリオ、主要不確実性を優先する条件 | 専門家判断をCodexの自信へ読み換えない。過去の誤差実績なしに較正分布を作らない。政府指針の承認制度を導入しない |
| NUM-S09：[House of Commons Library, Survey sampling](https://commonslibrary.parliament.uk/research-briefings/sn04447/) | Stratified/Cluster/Mixed samplingとNon-probability/Convenience。更新2026-03-17 | 集団間差を考えた層分けと、アクセスしやすい集団への偏りの確認 | 本件は代表性/層の説明に限定。標本サイズの一般目安や信頼区間重なりの判定を本運用の採用規則にはしない |
| NUM-S10：[グロービス経営大学院用語集「フェルミ推定」](https://mba.globis.ac.jp/about_mba/glossary/detail-20808.html) | 用語本文（定義・例・式→データ/概数→別式確認・訓練と基礎知識）。周囲の説明会案内は対象外 | 日本語の経営教育でも基礎知識と論理的な推論、別式確認を併用する位置づけ | 短い概説で、具体的な係数選択/代表性/独立性までは記載しない。別式で近いだけで正確さを保証する規則にしない |

MITの[Sanjoy Mahajan紹介ページ](https://web.mit.edu/sanjoy/www/)も開いて教材の所在を確認したが、リンク先コース本文を今回の証拠として実読完了とは扱わない。検索結果だけのページ、会員限定本文、SNSの未確認の主張は根拠へ追加していない。

日本語の[神奈川工科大学の論理思考教育報告PDF](https://kait.repo.nii.ac.jp/record/12148/files/kkb-047-004.pdf)は検索要約では数的根拠/班内観察に言及していたが、原PDF取得が429応答で失敗したため本文未読・採用根拠外とした。検索要約だけで内容を確定しない。

## 現時点での共通性・相違

- 共通：数字を思いつくだけで終えず、対象に対応する小さな量/既知量へつなぎ、前提・丸め・検証を残す。
- 相違：物理教材は桁と尺度の直観を重視し、調査機関は母集団/選択/代表性、費用推計指針は比較対象と補正/データ、uncertainty指針は幅の意味を重視する。これらは相互補完であり、資料数だけの独立した面接評価実験の一致ではない。
- 暫定統合：同条件の与件/既知値 → 観察/層別/類推/行動・物理導出の使える経路を選択 → 条件の近い設定例を補助参照 → 上下限・感度・別観測を点検する。厳密な一列の優劣ではなく、対象と残る自由係数で選ぶ。
- 不採用：研究室など一集団の率を全国率と確定、価格帯の単純中間を販売平均と確定、理由のない50%の連続使用、単なる分割を根拠強化とみなす、異なる解答例の平均を正解にする。

## 次の節目

上記を既存演習の初答・照合・修正と突き合わせ、採用手順と未実証の係数を切り分ける。経緯は[過去演習再検討](../learning/2026-11-26-07-number-methods-retrospective.md)、再利用本文は[数字設定方法](../details/number-setting-methods.md)へ反映する。

## 節目2：過去演習との照合後の統合判断

無料公開の実読資料はS01〜10の10件。既存演習では、手順/算術が支持されても率・購入頻度・価格の独立実証は残るという共通の不足を確認した。資料の記述だけを並列に残さず、[FERMI-SOLVE-A-003 v1](../details/number-setting-methods.md)へNS-01〜07とNS-CHECKとして整理した。

- **現行手順へ採用**：同条件の与件/観測値、経験/尺度の偏り確認、意味のある層別/正しい重み、比較対象との差を残す類推、行動/物理導出、幅の性質に合う代表値、条件付きの索引参照。
- **限定**：幾何平均は正の量の倍率中心、観察は代表性に留保、類推は補正の根拠、能力式は実需/稼働との橋渡しを条件にする。各機関の大規模調査/推計手続きを、本番の逐次承認や重い計算の義務へ移植しない。
- **不採用**：未知率を理由なく50%で埋める、前提を多くして精密に見せる、本人未共有の実経験を語る、例題の数字を現実の正解と固定する。
- **未検証**：新手順の新規問題での効果、個々の係数精度、本番速度。新しい演習・採点・留保評価は加えていない。B006候補v1は場面別の詳細/旧採否として残す。

新チャットでは、本ノートを現行手順の代用にせずA003本文を読む。個々の設定例は[参照索引](../references/NUMBER_INDEX.md)、採用までの過程は上記learningへ戻る。
