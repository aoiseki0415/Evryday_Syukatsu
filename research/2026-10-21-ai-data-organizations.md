# DSと顧客向けAIシステム実装を併せて扱う組織の探索

確認日：2026年10月21日（日本時間）。今回のユーザー依頼は、従来の2×2の④「データサイエンスの背景を生かし、顧客向けAIシステムの設計・実装を目指す」に限定し、**志望度・企業規模を問わず**アクセンチュアAI＆Dataの類似先を広く探すこと。以下は調査結果とCodexの比較提案であり、応募・志望順位の決定ではない。

**同日後続の絞り込み：** ユーザーが「AIとデータを同じ採用枠で扱うこと」「アクセンチュア以上を狙う企業評価」を再び優先したため、現在の比較は[採用単位別の再調査](2026-10-21-ai-data-hiring-units.md)を参照。BCG X DSの28卒求人にもAIエージェント設計実装とアーキテクチャ構築の記載が見つかった。職種が分かれることだけでシステム実装を担当しないとは判断しない。本資料は広い探索の記録として保存する。

## 判定と情報源

- 同一職種で分析・モデル評価とシステム実装を扱う場合、同一組織内でDSとシステム開発者が協働する場合、入社後に専門トラックを選ぶ場合を区別した。組織の業務が広いことから、個人が全工程を担当するとは推定しない。
- 新卒時から「AIアーキテクト」という職名であることは必須条件にしない。AIエンジニア、ソリューションエンジニア、機械学習エンジニア、FDEも調べた。FDEは顧客の現場で要件整理から実装・導入を進める役割だが、会社ごとに範囲が異なる。
- 研究・統計・研究コードが歓迎されることと、ML/LLMやWeb・クラウド開発の能力を求められることは別。EEGの統計解析経験だけで機械学習開発要件を満たすとは扱わない。
- 企業公式採用、職種別ATS、公式社員記事を中心に使用。LabBase・AtCoder Jobs・Wantedlyは**企業が掲載した求人・記事**として参照した。Xも検索したが、今回の採否・期限を確定できる補助資料は得られなかった。公式note・技術ブログは実務理解に使い、個人の経験を全員の配属・キャリア保証としない。
- 以下のURLは全て今回確認。公開日が表示されない採用ページは公開日不明。28卒登録・イベントは本選考開始と区別。中途求人は仕事内容の証拠に限り使用し、28卒応募可とはしない。

## 1. 新卒の具体的な入口を確認した候補

| 企業・部署・職種 | DSとAIシステムの接点 | 採用での研究経験の扱い・注意点 | 28卒と出典 |
| --- | --- | --- | --- |
| アクセンチュア／AI＆Dataアーキテクト | 課題分析、ソリューション選定、アーキテクチャ設計、実装・運用。今回の比較基準。 | AI・DSとシステム設計実装の両方を職種内で扱う。本人の特別選考結果は未確定。 | [28卒職種案内](https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level) |
| ARISE analytics／AIエンジニア、将来データアーキテクト・ソリューションエンジニア | アナリストで分析の基礎を学んだ後、専門性と希望に応じて5トラック。分析システムのクラウド設計実装、アプリ開発の道を明示。 | 統計知識、研究・課外活動でのPython/R等を歓迎。経験必須ではない。AIエンジニア自体はアルゴリズム寄りで、システム志向は他トラックも比較する。 | [28卒AIエンジニア・プレエントリー](https://www.ariseanalytics.com/recruit/potential/)、[キャリア](https://www.ariseanalytics.com/recruit/career-development/) |
| フューチャー／AI戦略推進グループ AIXG／ITコンサルタント | AI・DSの専門組織。研究と顧客向け社会実装を両輪とする。LLMOps・非機能要件を含むAIシステム導入の発信もある。 | ポテンシャルのTech選考は大学の研究を評価対象とする。アドバンスト採用ではAIXGが募集部門で、専門性が認められれば関連部門配属。高度な専門性の審査がある。 | [28卒エントリー・カテゴリ別採用](https://www.future.co.jp/recruit/recruit/rec-fresh/)、[2026-08-27公式イベント記事](https://note.com/future_event/n/nb10ade94560e)（イベント終了済み） |
| ABEJA／フルスタックエンジニア（ソリューションエンジニア） | DSと協働してモデルを業務システムに統合。要件定義、技術選定、クラウド、データパイプライン、学習推論環境、運用まで。 | データ集計・分析パイプライン、ML研究開発の経験を歓迎。ただしソフトウェア開発6カ月以上等が必要。DS職も別にあり、モデル中心の仕事内容。 | [28卒ソリューションエンジニア](https://hrmos.co/pages/abeja/jobs/2286439113463750657)、[28卒DS](https://hrmos.co/pages/abeja/jobs/2286439113463750656) |
| Ridge-i／AIエンジニア | 顧客課題・データ理解、分析・モデル開発、PoCから実装。アーキテクチャ設計・技術方針をチームで決める。 | Python経験が必要。線形代数・微積分・統計、ML実装、クラウド基礎を歓迎。研究概要・コードを提出できる。モデル開発の比率も高い。 | [28卒早期選考](https://hrmos.co/pages/ridge-i/jobs/1702962962645885022)：2026-10-01～10-31。書類→オンライン面接1～2回→対面最終。終了時刻の記載なし。 |
| ブレインパッド／機械学習エンジニア・アナリティクスSE・データプラットフォームエンジニア | DS組織と連携し、MLを動かすシステム、分析アプリ、分析基盤を設計・開発・運用。 | DSとエンジニアは別コース。本人の志向ならエンジニア側も重要。28卒画面の職種詳細は明示的に27年度参考情報。 | [公式新卒](https://www.brainpad.co.jp/recruit/entry/new/)、[28卒エンジニア登録](https://brainpad-recruit.snar.jp/index.aspx?id=MZhTT-Ua8n8)。28卒詳細は要再確認。 |
| RONNABYTE（旧DATUM STUDIO）／データスペシャリスト（AI・データエンジニア） | 分析、データ基盤、アーキテクチャ設計、技術選定、構築、AIアプリ開発、運用改善まで。 | プログラム開発能力または一定の研究成果を条件に挙げる。研究と開発の双方を提示できる入口。配属後の担当は確認する。 | [企業掲載28卒求人](https://compass.labbase.jp/company/1721/recruit/57097)：2026-08-26～11-01。面談（選考あり）→適性→面接2回。 |
| ちゅらデータ／AIエンジニア・データエンジニア | 生成AI/MLアプリ、PoCの本番化、MLOps/LLMOps/AgentOps、AIエージェント実行基盤。RONNABYTEの子会社で採用は別。 | 研究等でのプログラミングと生成AI利活用が必須。クラウド・ML研究・DB等の歓迎条件も1つ以上必要。論文・研究コードを提出できる。 | [28卒求人](https://herp.careers/v1/churadata/SnkYm4eB2yxX)。勤務地は沖縄本社表記。期限記載未確認。 |
| エクサウィザーズ／エンジニア、FDE | MLとソフトウェアを融合した採用。顧客のML/LLM PoC→要件定義→AI・アプリ開発→導入運用・効果検証。 | 研究で動くものを作った経験も対象。数学・論文理解・アルゴリズム実装を評価。ただしFDE以外に自社製品・インフラ等への配属もある。 | [企業掲載28卒本選考](https://compass.labbase.jp/company/246/recruit/57782)。書類→現場面接（トライアルの場合あり）→CTO。期限未確認。 |
| 電通デジタル／AI・DS、ソフトウェア・AIシステムエンジニアリング | 分析・AI活用と、分析基盤・生成/予測AIを使う業務システム開発を扱う。マーケティングの比重が高い。 | 2コースは別選考。研究から分析側へ入るか、開発側で強みを示すかを判断する必要。コース・タームの併願不可。 | [28卒要項・スケジュール](https://www.dentsudigital.co.jp/careers/newgrad/recruiting/)、[職域](https://www.dentsudigital.co.jp/careers/newgrad/jobs/)。早期2026年10月/11月、通常2027年2月エントリー。対象コースはマイページ。 |
| AVILEN／DS・AIエンジニア・AIコンサルタント | コンサル、DS、エンジニア、PMのチームで顧客AI開発導入。新卒枠の説明はデータ取得・モデル開発が中心。 | ML・深層学習実装、研究でのLLM利用を歓迎。将来AIコンサル/PM/EMへ進む記載はあるがアーキテクト配属保証ではない。 | [28卒統合募集](https://hrmos.co/pages/avilen/jobs/1689179272041807998)、[職種紹介](https://avilen.jp/recruit/jobs/)。期限未確認。 |
| GRI／AIエンジニア | 分析、時系列等のモデル、MLOps基盤、基盤アーキテクチャ、顧客導入・運用を扱う。 | Python/R・時系列解析と接続しやすい記述。ただし掲載対象専攻は工学/情報系等で、神経科学専攻の応募可否は要確認。 | [企業掲載28卒求人](https://compass.labbase.jp/company/1254/recruit/52764)：2026-05-21～2027-03-31。書類→面談等→最終。 |
| pluszero／AIエンジニア | 数理・統計・AIとシステム開発を合わせ、データ前処理、手法設計、API化・システム組込み、本番運用。 | 研究・開発でのプログラミングに加え、AI周辺分野の研究またはML等の開発経験が必要。一般的な統計経験だけで充足とは言えない。 | [企業掲載28卒求人](https://jobs.atcoder.jp/offers/1480)。書類→コーディング試験2回→最終。期限未確認。 |
| IBM Consulting／AIイノベーター、DS | 前者はAI選定評価・API統合・システム実装。後者はML/最適化が軸で、エンジニアリングも学ぶ人物を求める。別職種として比較。 | AIイノベーターは研究での開発成果も認めるが、自主的な先端AI検証経験が必要。DSはML/最適化知識歓迎。 | [28卒募集一覧](https://www.ibm.com/jp-ja/careers/career-opportunities)、[AIイノベーター要項](https://www.ibm.com/downloads/documents/jp-ja/15db805fff4249c9)、[DS要項](https://www.ibm.com/jp-ja/downloads/documents/jp-ja/1227c12efab8b25d)。期限はマイページ。 |
| BCG X／AI Engineer、Data Scientist | AI/DSとエンジニアリングの組織。顧客AIプロダクト・ソリューション設計構築。DSとAI Engineerは別職種。 | 関連分野の修士/博士・フルタイム職歴なし等。神経科学の学位が関連分野に該当するか、実装能力の要求を要確認。 | [28卒案内](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)、[実務・FDE紹介](https://careers.bcg.com/jp/ja/japan-bcgx)。新卒AI EngineerとFDEが同一の採用タイトルとは扱わない。 |
| TDSE／エンジニア、DS | ML/分析プロジェクトでMLOps基盤、アプリ、DBを設計運用。DS専門集団の中で分担する。 | DS職は分析・戦略の比率が高い。エンジニア側の28卒専門要件は未確定情報として扱う。 | [28卒プレエントリーと両職種](https://www.tdse.jp/recruit/preentry/)。登録受付であり本選考受付とは別。 |
| InsightEdge／DS、ソフトウェアエンジニア | 住友商事グループのAI/分析とシステム開発。SWEは分析系バックエンド・基盤の設計構築。DSと分担。 | [28卒DS](https://herp.careers/v1/insightedge/ULzcvO5ofDdd)は研究での統計解析・プログラム経験を必須と明示。ただし分析中心。 | [28卒SWE](https://herp.careers/v1/insightedge/Enkj0X4CKAA5)も掲載。ATS本文取得は403のため企業掲載求人の検索収録本文で確認。幅広い外部顧客SIとは顧客範囲が異なる。 |
| NTTデータ数理システム／コンサルティングエンジニア・DS・AI・ソフトウェアエンジニア | 数理/統計/AIによる顧客ソリューション、グラフRAG、要件定義、モデル実装、導入運用、商用ソフト開発。 | 生物等を含む研究経験を面接で深く聞くと説明。モデル・アルゴリズムや自社ソフトの比率もある。 | [28卒要項](https://www.i-note.jp/msi/recruit/job.html)、[選考](https://www.i-note.jp/msi/recruit/session.html)。初回説明会・試験は2026年12月下旬予定。数学/英語→研究レポート又はGitHub→面接。試験の出題内訳は27卒実績。 |

## 2. 大手コンサル等のAI・データ組織

組織としてDSとAIシステム構築が共存する根拠はある。ただし、多くは28卒の一般コンサル／技術コースから入るため、希望組織への配属・実装比率を確認する必要がある。

| 企業・組織 | 実際に扱うこととDSの接点 | 新卒入口と未確認点 | 公式根拠 |
| --- | --- | --- | --- |
| EY／Technology Consulting：AI＆データ | DS、AI活用、データ/クラウド基盤、顧客IT導入・定着。研究・専門経験を歓迎する説明。 | 28卒本選考案内あり。AI＆データ配属・エンジニアリングの担当範囲は要確認。 | [新卒部門紹介](https://www.eysc.jp/recruit/new_graduate/capabilities/tc/aid-message/)、[基盤実装事例](https://www.eysc.jp/recruit/new_graduate/capabilities/tc/tccase/offerings-10/)、[28卒](https://www.eysc.jp/recruit/new_graduate/entry/new/index.html) |
| デロイト トーマツ／AI＆D、EngineeringのFDE | DS/データエンジニアとAI・クラウド・AIプロダクト実装を扱う。 | 28卒一般コンサル採用あり。FDE求人は経験者向け。AI＆Dの新卒配属保証は未確認。RAのAI Analytics採用は別組織・職種。 | [組織・職務](https://www.deloitte.com/jp/ja/careers/deloitte-tohmatsu-consulting.html)、[28卒](https://www.deloitte.com/jp/ja/careers/deloitte-tohmatsu-consulting-students.html)、[FDE発表2026-04-30](https://www.deloitte.com/jp/ja/about/press-room/nr20260430.html) |
| PwC／Digital＆AI Transformation：AI実装／デジタルコンサルタント | 分析、AIシステム、AIエージェント、MLOps/LLMOps、データ活用を扱う。 | 28卒デジタルコンサル募集。冬期締切2027-01-08 23:59（日本時間）。専門配属とDS経験の評価方法は要確認。 | [部門](https://www.pwc.com/jp/ja/careers/consulting/mid-career/department/tc-d-a.html)、[新卒DC](https://www.pwc.com/jp/ja/careers/consulting/campus/recruiting-info/technology-consulting.html)、[日程](https://www.pwc.com/jp/ja/careers/consulting/campus/selection.html) |
| KPMG／DXA内Data＆AI | データアーキテクチャ、分析、AIモデル運用評価、生成AI・エージェント開発。 | 28卒窓口あり。通常は12～18カ月育成後に専門チーム配属。中途DXAの要件を新卒要件に転用しない。 | [DXA](https://recruit.kpmg-consulting.jp/info/dxa)、[新卒](https://recruit.kpmg-consulting.jp/new-graduate)、[育成FAQ](https://recruit.kpmg-consulting.jp/new-graduate/faq) |
| アビーム／AI＆Technology Modernization BU／デジタルコンサルタント | AI/データとアプリ・クラウドを使った構想、実装、導入・定着。 | 28卒デジタルコース。2026-10-29 14:00（日本時間）秋ターム最終ES。SPI・AI面接・面接等。旧AIコースは統合され配属幅あり。 | [28卒コース・選考](https://www.abeam.com/jp/ja/recruit/newgrad/course2028/solution-cs/) |
| アバナード／Data＆AI | 顧客向けAIアプリ、RAG、データ基盤、AI全体設計。本番導入のエンジニア職が存在。 | 28卒Engineer募集タイトルを確認。現在ページ本文は関連する中途求人や27年10月採用が混在し、28卒でのData＆AI職種内訳は確定できない。 | [28卒Engineerページ](https://www.avanade.com/ja-jp/career/job-details/R00347593)。関連求人を28卒の必須条件と読み違えない。 |
| キャップジェミニ／Insights＆Data | DS/予測分析・生成AI、AIアプリ、データレイク、クラウドアーキテクチャを扱う。 | 28卒向け採用活動を確認。DATA部門AI Engineerは経験者求人で、新卒からの部門入口未確認。 | [データ＆AI](https://www.capgemini.com/jp-jp/services/data-and-ai/)、[国内採用](https://www.capgemini.com/jp-jp/careers/)、[AI Engineer求人](https://careers.capgemini.com/job/Tokyo-DATA-%E9%83%A8%E9%96%80-AI-Engineer/1384354533/) |

## 3. SIer・総合IT企業の専門領域

| 企業・組織 | DSとAIシステムの実務 | 28卒入口・判断上の限界 | 根拠 |
| --- | --- | --- | --- |
| NTTデータ／Data＆Intelligence、技術革新統括本部AI技術部 | データ基盤・分析・AI活用とAI統合ソフトウェアアーキテクチャ。2026年の公式社員記事で新卒出身者のAI技術部在籍も確認。 | 一般SE入口。公開募集要項は27卒で、28卒の当該部署への専門採用は未確認。 | [サービス](https://www.nttdata.com/jp/ja/services/data-and-intelligence/)、[2026-03-16アーキテクト記事](https://www.nttdata.com/global/ja/recruit/uptodata/articles/6967/)、[募集要項](https://nttdata-recruit.com/recruit/requirements.html) |
| NRI／AXイノベーションセンター等のAIソリューション領域 | DS/ML/最適化とAIのシステム化、API、基盤・運用。NRIデジタルにもDSとアーキテクトの協働あり。 | 28卒サイトあり。NRI一般AE/TEとAI部門配属は別問題。NRIデジタルの新卒直接募集は未確認。 | [Solution Ai](https://www.nri.com/jp/service/solution/solution_ai.html)、[28卒](https://working.nri.co.jp/recruit/2028/index.html)、[NRIデジタル](https://www.nri-digital.jp/about/) |
| NEC／アナリティクスコンサルティング、AI技術サービス領域 | DS（SE）として顧客AI導入・システム化。AIサービス側にはシステム全体の設計も。 | 部門別採用がある。現在確認した個別募集は27卒。統計/ML/最適化やプログラム経験を評価する枠だが28卒同一枠は未確定。 | [DS（SE）部門](https://jpn.nec.com/recruit/newgraduate/matching/department/602/)、[AIサービス部門](https://jpn.nec.com/recruit/newgraduate/matching/department/704/) |
| 富士通／AI戦略・ビジネス開発本部等 | コンサル/ソリューションエンジニア/DSがAI活用や共通アーキテクチャを扱う。 | 28卒プレエントリーあり。部門紹介と27卒職種を28卒の確約としない。 | [部門紹介](https://fujitsu.recruiting.jp.fujitsu.com/about/department/post-18835/)、[入口](https://fujitsu.recruiting.jp.fujitsu.com/recruit/entry/) |
| 日立／AI・デジタルシステム領域、デジタル事業開発 | DSによるデータ分析/AIモデル、PoCからAIシステム導入。 | 技術系ジョブマッチングあり。確認した募集要項は27卒。28卒のテーマと要件は未確認。 | [AI・デジタルの仕事](https://www.hitachi.co.jp/recruit/newgraduate/jm-navi/ai_digital/index.html)、[DS採用](https://www.hitachi.co.jp/products/it/aisssaiyo/recruit.html) |
| 日鉄ソリューションズ／デジタル技術・ソリューション領域 | DS/AIとデータ基盤・システム化を扱い、データアーキテクトへのキャリア例も示す。 | 28卒イベント入口あり。キャリア説明資料は2024年中途向けで、新卒配属保証ではない。 | [2024-12部門採用資料](https://www.nssol.nipponsteel.com/recruiting/presentation/pdf/dts_202412.pdf)、[28卒イベント](https://www.nssol.nipponsteel.com/recruiting/internship/) |
| 電通総研／AIトランスフォーメーションセンター AITC | DSとAIサービスエンジニア、AI活用コンサル・開発・システム実装。 | AITCから新卒総合採用への案内あり。確認した詳細要項は27卒、28卒AITC配属条件未確認。 | [AITC採用](https://aitc.dentsusoken.com/recruit/)、[AI領域](https://www.dentsusoken.com/saiyo/x-innovation/)、[募集](https://www.dentsusoken.com/saiyo/application/) |
| BIPROGY／Rinza関連のAI・データ領域 | 分析、MLと顧客AI導入・エンジニアリング。 | 28卒登録あり。AI/DSの仕事体験実績はあるが、専用本選考・現在の細かな部署名は未確認。 | [Rinza](https://www.biprogy.com/solution/service/rinza.html)、[28卒採用入口](https://www.biprogy.com/recruit/recruiting/) |
| SCSK／NebulaShift ai・di関連領域 | DS/AIエンジニアとAIシステムの参照アーキテクチャ、データ基盤・AIエージェントを扱う。 | 28卒MyPageあり。NebulaShiftはサービス名で正式な採用部署名ではない。専門配属・DS優遇要件未確認。 | [ai・2024-12-16](https://www.scsk.jp/news/2024/pdf/20241216.pdf)、[di・2025-06-19](https://www.scsk.jp/news/2025/pdf/20250619.pdf)、[新卒](https://www.scsk.jp/recruit/saiyo/index.html) |

## 4. 追加の専門企業・開発組織

| 企業・組織・職種 | 仕事内容と研究の接点 | 新卒の確認範囲 | 根拠 |
| --- | --- | --- | --- |
| PKSHA／アルゴリズムエンジニア・ソフトウエアエンジニア／AIソリューション | 分析/アルゴリズムとWebAPI組込み・顧客システム。前者は研究でのアルゴリズム構築・理工学専門性を歓迎、後者はアプリ開発力を要求。 | 新卒2職種あり。28卒の個別募集要件・期限は未確認。 | [公式新卒](https://www.pkshatech.com/recruitment/newgrads/)、[越境する社員例](https://voice.pkshatech.com/n/n9e5538ed18a1) |
| JDSC／DS・エンジニア・FDE | ビジネス/DS/エンジニアリングを組み合わせ、分析からシステム実装運用まで。 | 新卒・28卒インターン発信あり。ただし今回見つけた28卒企画だけでDS・FDEの新卒直結枠とは確定できない。 | [公式採用](https://jdsc.ai/recruit/)、[求人一覧](https://herp.careers/v1/jdsc)、[企業発信28卒インターン](https://www.wantedly.com/companies/jdsc/post_articles/1048052) |
| Laboro.AI／ML・LLMエンジニア、システム開発エンジニア | 顧客別カスタムAIを分析・モデル側とシステム側が協働して構築。 | 職種別求人あり。28卒募集は未確認。ML経験とソフトウェア経験を職種別に見る。 | [会社の求人一覧](https://recruit.jobcan.jp/laboroai) |
| ELYZA／LLMソリューション開発 | LLM研究と顧客AIシステム実装を扱う。ML/ソフトウェアの協働。 | 長期インターンあり。28卒本選考未確認。LLM固有の技術要件があり、統計分析経験と同一ではない。 | [事業](https://elyza.ai/)、[LLMソリューション職](https://herp.careers/v1/elyza0/yEe0Rc0YfJhk) |
| ヘッドウォータース／エンジニア、生成AI・AIデータ/プラットフォーム領域 | 顧客AI導入、アプリ/クラウド/データ基盤、MLOps。 | 28卒エンジニア求人を公式サイトに掲載。生成AI・AIデータ個別求人は中途で、新卒からの希望配属は要確認。 | [公式採用・28卒求人リンク](https://www.headwaters.co.jp/recruit/)、[MLOps](https://www.headwaters.co.jp/service/ai/synclect_cl.html) |
| クラスメソッド／データ事業本部、AI・データ系エンジニア | 分析基盤とLLMアプリ、クラウドの要件設計・開発運用。 | 28卒エンジニア求人あり。学習/プログラミング/Git等重視。DS研究が特に優遇される根拠は弱く、開発志向が強い候補。 | [28卒要項](https://careers.classmethod.jp/requirements/new-graduate2028-engineer/)、[データ領域](https://careers.classmethod.jp/data-engineer/) |
| デロイト トーマツ ディープスクエア／AI開発 | DS、生成AI、動画像解析と企画・設計・システム実装。シニアAIエンジニアにアーキテクチャ設計を明示。 | 新卒/インターンの開発コース掲載。28卒正社員採用・配属は未確認。 | [公式採用](https://deepsquare.deloitte.jp/recruit/)（本文直接取得403、検索収録本文を参照） |
| SREホールディングス／AI・データサイエンス領域 | 統計/ML/時系列/因果推論とAIソフトウェア、MLOps、Webアプリ。 | 新卒サイトあり。研究・DSからシステム構築へ進む28卒の個別枠未確認。 | [新卒](https://sre-group.co.jp/recruit/graduate/data/index.html)、[DS求人群](https://herp.careers/v1/sregroup/requisition-groups/21f2878a-7d4d-4076-b750-1b2992874c63) |
| HACARUS／DS・AIソリューション | 少量データ分析と顧客現場へのAIシステム導入、RAG/エージェント、画像・エッジ領域。 | 過去のインターン→新卒事例あり。28卒募集未確認。一般業務ITより製造/現場の比重が高い。 | [現行サービス](https://hacarus.com/ja/services/ais/)、[新卒社員事例2021-01-05](https://hacarus.com/ja/information/20210105-engineer-interview/) |
| FLYWHEEL／データ・AIソフトウェア領域 | Conataによるデータ活用とAIシステム実装。DSとソフトウェア開発を併せて扱う。 | 新卒入社の実績を公式発信。今回28卒詳細は未確認。 | [新卒受入の公式記事](https://www.flywheel.jp/newsrelease/new-employee/)、[企業掲載26卒求人](https://jp.linkedin.com/jobs/view/2026%E5%8D%92-%E6%96%B0%E5%8D%92%E6%8E%A1%E7%94%A8-%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2-new-grad-software-engineer-at-flywheel-inc-4145504495)（終了済み） |
| Fusic／機械学習エンジニア・Webエンジニア | データ/モデルからクラウドのシステム構築運用まで扱う。 | 新卒のWeb系とML職の募集区分に注意。確認できたML新卒例は26卒で、28卒ML職は未確認。 | [公式職種一覧](https://fusic.co.jp/recruit/positions)、[会社掲載26卒ML求人](https://jobs.atcoder.jp/offers/580) |

## 5. 仕事内容は近いが国内28卒の入口が弱いベンダー

| 企業・組織 | 実務上の接点 | 28卒の状況・限界 | 根拠 |
| --- | --- | --- | --- |
| AWS／Professional ServicesのData＆Analytics・AI/ML | 顧客AI/ML、データ基盤、アプリ/インフラの構想・設計・実装。DS/MLとアーキテクトが協働。 | 日本の28卒SA本選考あり。ProServeの国内28卒個別枠は未確認。海外28対象インターンを日本枠と混同しない。 | [ProServe](https://aws.amazon.com/jp/careers/teams/professionalservices/)、[日本新卒](https://aws.amazon.com/jp/careers/newgraduate/) |
| Microsoft／Cloud Solution Architect、Data＆AI関連 | Azureを軸にデータ・AI導入・アーキテクチャ支援。システムを自ら作る比重はロールで異なる。 | 28卒CSA等の夏インターン募集は終了。国内Data＆AI専門枠の本選考未確認。 | [28卒技術職の要項](https://www.microsoft.com/ja-jp/mscorp/college/mskk-recruit-tech) |
| DataRobot／Professional Services AI Engineer・国内FDE | 予測AIと生成AIの顧客アプリを要件整理→設計→実装導入。日本FDEチームを2026年7月新設。 | 日本求人あり。経験者向けで28卒専用募集未確認。 | [AI Engineer求人](https://www.datarobot.com/jp/careers/open-positions/job/102663/)、[国内FDE紹介](https://www.datarobot.com/jp/blog/datarobotjapan_fde_tech-summit/) |
| Databricks／Field Engineering・Delivery Solutions Architect | データ・AI基盤の顧客設計導入を扱う。販売前の技術支援とデリバリーは分ける。 | 東京の当該求人は存在。国内28卒新卒枠未確認。 | [現行求人一覧](https://www.databricks.com/jp/company/careers/open-positions) |

## 6. 既出候補の位置付けの再点検

- [McKinsey QuantumBlack東京Data Engineer](https://www.mckinsey.com/careers/search-jobs/jobs/dataengineer-quantumblackaibymckinsey-105274)はDSと実装が共存する有力な組織。ただし国内28卒入口未確認。[東京DS求人](https://www.mckinsey.com/careers/search-jobs/jobs/datascientist-quantumblackaibymckinsey-105275)には職務経験条件があり、新卒可とはしない。
- [日本総研のIT・DS](https://www.jri.co.jp/recruit/new_graduates/business/it_solutions/data_science/)と[MUIT](https://www.it.mufg.jp/recruiting/fresh/index.html)は候補として残るが、グループ内金融の比率が高い。MUITの確認したDSコース要項は27卒で、28卒のAIアーキテクトへの接続は未確認。
- [CTC](https://www.ctc-g.co.jp/solutions/datarobot/?menu=1)、[TIS](https://www.tis.co.jp/recruit/beamover/information/?columnid=2192&media=25077)、[JSOL](https://promotion.jsol.co.jp/data-acceleration-program/support/)にはAI/データとシステム構築の事業上の接点がある。ただし今回、28卒でDS研究を評価する特定部署・枠まで確定できず、上表の候補と同じ確度で推さない。
- BCG PlatinionはITアーキテクチャの志向では比較対象だが、今回はDSとAIを併せる④としてBCG Xを中心にした。MRI/MURCも、DS研究から顧客AIシステム構築へ進む具体的な新卒経路は今回確認できず、①・②等の別論点とする。
- Preferred NetworksはAI開発・社会実装の候補として残るが、研究・モデル・自社基盤の色があり、顧客別SIをやりたいという本人の目的との比較が必要。Google Cloud、Oracleも導入支援の仕事は比較対象だが、国内28卒でDS専門性を用いる対象枠は今回確定できていない。「募集がない」「合う仕事がない」と断定しない。
- ALBERTはアクセンチュアとの統合関係があり、独立した代替応募先として加算しない。DATUM STUDIOは2026年10月1日にエイトハンドレッドと統合し[RONNABYTEへ商号変更](https://ronnabyte.jp/)。ちゅらデータは別法人の子会社として残る。

## 7. 比較提案と残る論点

今回の結論は「④がほとんど存在しない」ではない。**DS/研究を評価し、AIシステムの実装も扱う新卒の入口が複数確認できた。** 前回までの調査は大手一般採用と「アーキテクト」の名称に寄り、AI・DS専門企業の探索が不足していた。

以下はCodexの提案であり、ユーザーの志望順位ではない。

1. DSから設計・構築へのキャリアが明瞭な比較先：**ARISE analytics、RONNABYTE、ちゅらデータ、フューチャーAIXG**。ARISEは分析基礎→専門トラック、フューチャーは高度専門性を評価する部門採用が特徴。
2. システムを作る仕事を中心に、研究経験を生かす比較先：**ABEJAのソリューションエンジニア、エクサウィザーズのFDE、ブレインパッドのエンジニア、IBM AIイノベーター、BCG X AI Engineer**。開発力を別途示す必要がある。
3. 大手AI＆Data部門として比較する先：**アクセンチュア、EY、デロイト、PwC、KPMG、アビーム**。希望配属と、分析/提案/実装の仕事の配分を確認する。
4. モデル構築も相当行う前提で比較する先：**Ridge-i、pluszero、GRI、AVILEN、NTTデータ数理システム**。モデルを作ることが目的でない本人にとって、実装の範囲だけでなく日々の担当比率が重要。

説明会や面談の際に必要な未解決事項は、(a)新卒がAIアプリ/API/基盤の設計実装を担うか、(b)解析/モデル開発とシステム設計開発の配分、(c)職種・配属を内定時に確定できるか、(d)神経科学・統計/信号処理の研究が採用でどのように評価されるか、(e)28卒の現行締切・専攻条件。自動応募・問い合わせ送信は行わない。

Notionは編集していない。網羅探索を一度区切るための候補母集団であり、市場の全求人を完全に列挙したものでも、未確認枠の不存在を証明したものでもない。
