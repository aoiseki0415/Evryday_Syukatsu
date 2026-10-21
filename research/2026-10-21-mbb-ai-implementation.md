# BCG X DSの適合性の再評価と、MBB等のAI実装職の追加探索

確認日：2026年10月21日（日本時間）。ユーザーは「BCG X DSはデータサイエンスの色が強いのではないか。AIアーキテクトの仕事がどの程度含まれるか分からない」と指摘し、希望に近いなら残したうえでBCG級の挑戦先を追加探索するよう依頼した。以下は公開資料に基づく調査とCodexの提案で、応募先の決定ではない。

## 1. BCG X DSについて前の提案を修正する

- [公式の日本向け職種紹介](https://careers.bcg.com/jp/ja/japan-bcgx)は、DSを分析・機械学習・数理最適化による先端モデルの設計構築、Forward Deployed AI Engineerを技術の設計構築力によるプロダクト・ソリューション開発実装と説明する。
- [企業掲載の28卒DS求人](https://compass.labbase.jp/company/665/recruit/56146)には、AIエージェント/データプロダクトの設計実装、MLOps・データ基盤を含むアーキテクチャ構築もある。これは本番実装まで関与する根拠だが、全体システム設計が主務という根拠ではない。分析・モデル・経営への示唆を重視する記述とMLモデリング要件も同時に読む。
- **現時点の適合評価は「DSを中心にAIの社会実装まで扱う、条件付き候補」へ修正。** 顧客向けAIシステム全体の設計構築を中心にしたい本人に、強く一致すると述べた前の回答は過大だった。
- AIエージェント、MLOps、データ基盤の設計にはアーキテクチャの要素がある。一方、業務要件からアプリ/API/認証・権限/既存システム統合/非機能要件等までを個人が主担当にする比率や分担は未確認。DSの担当比率を数値で推定しない。
- BCG X内で仕事の中心がより近いのは**AI Engineer側**。ただしそれはDS専門採用と別経路であり、研究だけで開発・クラウド等の要件を代替できるとはしない。
- [公式28卒入口](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)はDSとAI Engineerを別募集。公式検索の求人ID59586は28卒AI Engineer。[個別公式求人](https://careers.bcg.com/global/en/job/59586/AI-Engineer-%E6%96%B0%E5%8D%92-New-Graduate-2028-BCG-X-Japan)はタイトルが確認できたが本文を取得できず、ブラウザ表示でも本文なしだった。[転載の28卒求人](https://www.joinrs.com/fr/jobs/4884133)にはWeb/モバイル・クラウド・技術選定・MLOps、本番運用、Python/TypeScript、関連研究等がある。細かな28卒要件は転載参考として扱い、公式応募画面で要確認。関連研究に神経科学が含まれるかは未確認。

## 2. MBB内の具体的候補

| 会社・組織・職種 | 実際の業務と研究との接点 | 新卒の入口・選考条件 | 比較上の位置づけ |
| --- | --- | --- | --- |
| **McKinsey／QuantumBlack／Data Engineer I（東京、求人105274）** | DSとデータエンジニアリングを横断する分析用プラットフォーム、ML用データパイプライン、データ環境・セキュリティを構築。Python、pandas/numpy、データ理解が研究と接続し得る。 | CS/工学/数学または同等経験、コード能力、クラウド等の理解、英語・日本語。実務経験年数の必須条件は記載なし、インターン等のパイプライン経験は歓迎。**28卒専用でも2028年入社可の確約でもない。** [公式求人](https://www.mckinsey.com/careers/search-jobs/jobs/dataengineer-quantumblackaibymckinsey-105274) | 追加の有力な確認対象。分析を理解してシステム基盤を作る仕事は具体的。ただしLLMアプリ全体の設計や将来Architectへの移行保証ではない。 |
| **McKinsey／QuantumBlack／Architect（東京・大阪、111203）** | 顧客要件、企業/クラウドアーキテクチャ、API、コンテナ、ネットワーク、可用性・性能、設計と実装を担当。DS等と協働。 | Python/Node.js等の専門経験5年以上、Web開発・クラウド・DevOps、日本語・英語。[公式求人](https://www.mckinsey.com/careers/search-jobs/jobs/architect-quantumblackaibymckinsey-111203) | 希望する到達先の実在を強く示す。ただし経験者向けで、28卒の応募先として数えない。DS研究を直接評価する採用枠とは異なる。 |
| **McKinsey／QuantumBlack／Data Scientist（東京、105275）** | 課題を分析問題へ変換してモデルを開発・評価。クラウド等も使うが採用の中心はML/統計。 | ML/data miningの実務経験2年以上、Python/SQL等、日本語・英語。[公式求人](https://www.mckinsey.com/careers/search-jobs/jobs/datascientist-quantumblackaibymckinsey-105275) | 研究との接点は強いが、BCG DSと同じ重心の問題があり、公開求人は新卒専用でもない。研究年数を実務2年と読み替えない。 |
| **McKinsey／Tech＆AI／Software Engineer（東京、105277）** | DSの分析を顧客向けWebプラットフォームとして実装。バックエンド/フロント/可視化を設計。 | CS等関連学位、JavaScript/React等、リリース実績、ポートフォリオ、日本語・英語。[公式求人](https://www.mckinsey.com/careers/search-jobs/jobs/softwareengineer-techai-105277) | システム実装に近いが、DSの専門性で採る統合枠とは言えない。28卒・入社時期未確認。 |
| **Bain／AI, Insights, & Solutions（AIS）／AI＆engineering、DS＆ML** | AIプラットフォーム、クラウド、MLモデル、本番コード、生成AIの導入を同じ専門組織で扱う。[公式組織紹介](https://www.bain.com/careers/work-with-us/integrated-teams/ai-insights-solutions-ais/) | 日本の28卒AIS専門枠は見つからず。一般新卒ACとAIS専門採用は区別。東京の経験者DS募集への企業側発信もあったが、リンク先[公式求人101880](https://www.bain.com/careers/find-a-role/position/?jobid=101880)は現在「Job not available」。 | **組織としての類似性は強いが、28卒の実行可能な候補としては保留。** 同じAIS内にも職種・専門分担があり、統合採用を確認したわけではない。 |
| **BCG X／AI Engineer・DS（28卒）** | エンジニア側はプロダクト開発実装、DS側はモデルを中心に本番化も扱う。 | [公式28卒入口](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)に関連修士/博士・フルタイム職歴なしの案内あり。DSは企業掲載要項に書類→技術テスト→面接。締切未記載。 | 日本の28卒専門入口は最も明瞭。ただし本人の研究に近いDS職と、望む仕事に近いAI Engineer職は別に評価する。 |

### McKinseyでDSとソフトウェアを両立した実例

[2021年8月3日の公式社員記事](https://www.mckinsey.com/careers/life-at-mckinsey/our-culture-and-communities/careers-blog/shuhei)では、東京QuantumBlackのSenior DSが機械学習・因果推論・最適化を組み合わせ、保守・拡張できる顧客向けソフトウェアを構築した事例がある。DSとエンジニアリングが接続する実例として使えるが、**5年前の記事であり、現在の全DSの仕事比率や28卒採用・配属の保証ではない**。

## 3. MBB周辺・技術企業まで広げた探索

下表は仕事内容を調べるために広げた比較対象で、各職種の難易度がBCGと同等以上と実証した一覧ではない。

| 会社・組織・職種 | 具体的な接点 | 日本の28卒との距離・注意点 |
| --- | --- | --- |
| **Oliver Wyman／Quotient・Digital** | DS・ソフトウェア・データエンジニアを擁するAI導入組織。戦略から実装までの類似組織。[公式採用](https://www.oliverwyman.com/careers/digital-technology.html)、[2024年6月の設立発表](https://www.oliverwyman.com/media-center/2024/jun/marsh-mclennans-oliver-wyman-launches-quotient-a-global-ai-offering-to-unlock-new-value-across-industries.html) | 東京28卒の専門枠未確認。[APAC新卒ページ](https://www.oliverwyman.com/careers/entry-level/asia-pacific.html)の東京募集は27年一般コンサル。企業のグローバルな組織と、日本の統合採用を混同しない。 |
| **Palantir／Forward Deployed Software Engineer（東京・Japan Government）** | 顧客と課題を定義し、アーキテクチャ・大量データ・Webアプリを横断して実装。DS等の背景を歓迎。[公式求人](https://jobs.lever.co/palantir/12e94938-55cb-4ad9-9c05-405ebc9ef430) | **卒業後の関連実務1年以上が必要**。英日・クリアランス要件もあり、28卒直接枠に数えない。求人本文はデータ活用システム中心で、全案件がLLMとは確認できない。 |
| **Palantir／Deployment Strategist（東京・Japan Commercial）** | 顧客課題・データ・業務を理解し、FDEとパイプライン統合、ワークフロー構築。Python/R/Matlab/SQL経験を歓迎。[公式求人](https://jobs.lever.co/palantir/ba8fdce3-7f60-45f6-8323-d74cc18c4320) | 本文に最低実務年数なし。ただし28卒専用・入社時期未確認。設計実装の中心はFDEと分担するため、本人がアーキテクトになる職種と扱わない。 |
| **OpenAI／Forward Deployed Engineer（東京）** | 顧客との課題探索・スコープ・システム設計・フルスタック開発・本番展開を担当。[公式求人](https://openai.com/careers/forward-deployed-engineer-tokyo-tokyo-japan/) | 顧客対応を含むエンジニア/技術導入経験5年以上を想定。28卒専門入口未確認。仕事は近いが、DS研究専門採用ではない。将来の職種比較に留める。 |
| **Anthropic／Applied AI Engineer（東京）** | Claudeの顧客向けアーキテクチャ・プロトタイプ・評価・既存基盤統合と導入支援。[公式ATS](https://job-boards.greenhouse.io/anthropic/jobs/5390799008) | Technical PM/FDE/Platform Engineer等の経験を求め、関連経験4年以上は歓迎。**4年を必須と誤記しない**。28卒専門入口未確認。商談技術支援・導入助言も大きく、自分で全工程を構築するとは限らない。 |

### 一般コンサル・その他の確認

- [Kearney公式採用](https://www.kearney.com/careers/opportunities)は技術者・DSを対象とし、Cervelloにもデータ/分析の実装サービスがある。ただし日本の28卒AI/DS統合専門枠は確認できなかった。[東京ATS](https://kearney.taleo.net/careersection/008/joblist.ftl)には一般BA等を掲載。
- [Strategy＆日本](https://www.strategyand.pwc.com/jp/ja/careers.html)は経営戦略コンサルタントの新卒入口。PwCデジタルコンサルと同じ採用・仕事とは扱わず、顧客AIシステム構築とDSを統合した28卒枠は確認できなかった。
- [AlixPartners日本採用](https://www.alixpartners.com/jp/careers/)・[求人入口](https://www.alixpartners.com/careers/job-search/)も探索したが、日本の28卒AI/DS統合専門枠は特定できなかった。募集がないと断定はしない。
- Google Cloudの東京AI Outcome Customer Engineerも公式検索で確認したが、公開要件は技術対応経験7年等の上級職。28卒候補には含めない。Databricksの日本求人一覧も探索したが、今回確認した範囲で28卒の統合専門枠は特定できなかった。
- Oliver Wymanの海外AI Engineer（Quotient WAVE、Madrid/London）には、同一求人内でsoftware/DS/core AIの強み別を受け入れる記載が[転載](https://notify.careers/postings/81b65676-6629-4272-b30d-e3bb4ef8abda)にあった。ただし[公式ATS](https://mmc.wd1.myworkdayjobs.com/mmc/job/madrid---castellana/oliver-wyman---ai-engineer--m-f-d----quotient-ai-specialist---madrid---london_r_360738)の本文は読めず、国内28卒の根拠にしない。BD/提案支援・再利用可能な試作も含むので、顧客SI中心とも断定しない。

## 4. 年度・選考の注意

- BCG X：28卒DS/AI Engineer入口公開。両職種の併願可否、現在の技術評価・職務分担は未確認。経営コンサルとエンジニア職の併願可という案内をDS/AI Engineer間に流用しない。
- McKinsey QuantumBlack DE等：東京の一般職種求人で、**28卒の正式募集、2028年入社の受入、締切・選考工程は未確認**。職歴年数条件がないことから28卒受付中とは推定しない。
- [McKinseyの28卒国内一般Business Analyst採用](https://www.mckinsey.com/jp/careers/careers-in-japan/application-process-for-undergrads-2028)は冬選考締切2026年9月15日が経過。**この締切をQB専門求人へ適用しない。**
- [Bainの28卒国内一般コンサル採用](https://www.bain.com/ja/careers/hiring-process/tokyo/domestic-undergrad/)は冬インターン応募締切2026年10月7日13:00が経過。一般ACからAISへ配属される保証はない。AIS専門募集と一般枠の締切を混同しない。
- 求人に明示の公開日がない場合は公開日不明、確認日は本資料冒頭。転載・個人の投稿は補助資料として扱い、募集資格の主な根拠は会社公式と企業入力求人。海外の体験談を東京28卒の選考手順へ当てはめない。

## 5. 現時点の比較提案

1. **希望する仕事の中心に最も近いMBBの28卒入口はBCG X AI Engineer。** DS採用と別である点は残る。研究を使いながら開発経験を示せるかを評価する。
2. **新しい確認候補はQuantumBlack東京Data Engineer。** 分析を理解して基盤を作る仕事と研究コードの接点があり、公開条件に必須経験年数がない。ただし28卒・専攻・入社時期の受入は未確認。一般AIアプリ全体のアーキテクトへの確約もない。
3. BCG X DSは、分析・モデル中心の仕事にも納得でき、AI実装にどの程度関われるか確認できた場合の条件付き挑戦先に変更する。「DS経歴で入れるから本人の最適な主軸」とはしない。
4. Bain AIS、Oliver Wyman Quotientは類似組織として実在するが、日本28卒専門入口の未確認が大きい。OpenAI/Anthropic/Palantir FDEは顧客導入職の到達先として参考にする。
5. **MBB級に限定して、DS専門性を採用で評価し、AIシステム全体の設計構築を主務にできる日本28卒の統合枠は、今回も明確に確認できなかった。** 一般コンサルや経験者求人を応募可能な代替先として水増ししない。

Notion編集・応募・登録・企業への問い合わせ送信なし。ユーザーは志望企業・応募順位をまだ決定していない。
