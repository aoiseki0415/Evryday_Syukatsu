# 2026年10月21日：二つの主軸とAIシステム実装職の整理

最新の追加調査は末尾「④に絞った志望度不問の統合探索」と[統合調査資料](../research/2026-10-21-ai-data-organizations.md)を参照。以下の冒頭部分は議論当初の整理であり、その後の2×2への修正と最新の候補追加を優先する。

## 今回決まったこと

- 今後の就活戦略では、次の二つを主軸として検討する。
  1. NRIのITソリューション等、ITシステム全体の設計・構築へ直接進む道。
  2. データサイエンス・AIの専門性を入口にし、AI・ITシステムの設計・実装・導入・運用へ進む道。
- 二つの優先順位、応募企業、部署・職種はまだ決定していない。
- 2は純粋な分析専業だけを意味しない。AIモデルを業務や既存システムに組み込み、本番運用できる仕組みにする役割を中心に検討する。

## 2に該当する職種の公式情報

- [アクセンチュア AI＆Dataアーキテクト職](https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level)：ビジネス課題の分析から、ソリューション選定、アーキテクチャ設計、実装・運用までを一気通貫で支援すると説明されている。現在ユーザーが結果待ちの特別選考の職種に該当する。
- [日本IBM AIイノベーター](https://www.ibm.com/jp-ja/careers/blog/2028-new-graduate-recruiting-positions)：課題の再定義、AI活用の構想設計、プロトタイプ開発、APIや既存システムとの統合設計、システム実装を一貫して行う職種。
- [BCG X Forward Deployed AI Engineer](https://careers.bcg.com/jp/ja/japan-bcgx)：AI等の先端技術を使い、具体的なプロダクトやソリューションを設計・構築・実装する職種。2028年卒向けにはAI Engineer職の新卒採用案内がある。
- [デロイト トーマツ FDE](https://www.deloitte.com/jp/ja/about/press-room/nr20260430.html)：クライアントの現場で、AI・データ連携を含むシステムを設計・実装し、戦略と実行を接続する役割。
- [AWS Professional Services](https://aws.amazon.com/jp/careers/teams/professionalservices/)：データ＆アナリティクス、ML、アプリケーション、インフラ等の専門家が、企画構想から移行や構築まで支援する。2028年卒での個別職種の募集状況は別途確認する。
- [NRI Solution Ai](https://www.nri.com/jp/service/solution/solution_ai.html)：課題整理、AI選定、既存システムを意識した開発、堅牢な基盤構築、運用を一体として提供している。新卒時の具体的配属経路は未確認。

## 今回の解釈

- 2の中心候補は、AI＆Dataアーキテクト、AI Engineer／Forward Deployed Engineer、AIイノベーター、AI・MLコンサルタント、データ＆アナリティクス系Professional Servicesなど。
- データサイエンス経験は、モデル作成だけでなく、データの性質、評価、不確実性、分析パイプラインを理解した上でシステム設計へ進むための入口として使える。
- ユーザーの考えは、単に「分析経験がAI職の応募資格になる」というものではない。AIを使って実現する用途の一つがデータ分析であり、分析を実際に経験した人は、利用者が何をしたいか、どのデータが必要か、何を正しい結果とみなすかを理解した上で、AIを含む分析基盤・業務システムを設計できるのではないか、という仮説。この接続は、特にデータ・AIソリューションアーキテクト、MLシステム、データ基盤、MLOpsに近い職種で検証する。
- 「データサイエンティスト」という職種名だけで選ばない。募集要項に、既存システム統合、データ基盤、API、クラウド、MLOps、実装、運用のどこまで含まれるかを確認する。
- 純粋な分析・PoC中心の職種は、本人が望むIT・AIシステム設計との距離を個別に評価する。

## 次の論点

- 1と2それぞれについて、実際に応募する企業・部署・職種を特定する。
- 2の候補ごとに、本人がコードを書く範囲、アーキテクチャ設計の範囲、既存システム統合、配属確度、新卒選考を比較する。
- 研究経験を、分析能力だけでなくAIシステムの設計・実装志向へどう接続して語るかを検討する。

Notionは編集していない。

## 追記：顧客向けシステム構築という本人の目標（同日）

- ユーザーは「AIモデルを作りたいわけではない」と明言。SIerのように顧客に合うITシステムを構築し、その中でAIの導入・システム構築・設計にも携わりたい。先の「データサイエンスを入口にする」という表現を、分析職そのものが目的だと読まない。
- 検討する①②は職種への**入口の違い**。①広いITシステム構築、②AIを含むシステム構築。どちらでも業務理解→要件→設計→実装→導入・運用に近い仕事を探す。研究経験との接続は仮説であり、採用確率の高さは未確認。
- 企業の「格」や選考難易度は客観的な序列として扱わず、[Notionの志望度4以上](https://app.notion.com/p/32d161f28097806e868de3a30cc28441)を本人の比較基準とする。未記載企業も必ず探索する。
- 同DBの全企業名・志望度を確認。NRI、IBM、NTTデータ、アクセンチュアはレベル5。PwC、EY、KPMG、デロイト、MRI、MURCはレベル4。アビームはレベル3、NEC・富士通・日立はレベル2、BCGはレベル1として掲載済み（ただしBCG Xの職種評価とは別）。AWS、Microsoft、アバナード、日鉄ソリューションズ、MUIT、三菱総研DCSは同DBに企業名がない。Notionの値は過去の本人の主観的な志望度であり、一般的な入社難度ではない。

## 28卒の公式調査（2026年10月21日確認）

候補は提案・調査結果であり、ユーザーが応募を決めたものではない。期限と公開範囲は変更され得る。特別選考・マイページの個別情報は外部公開情報から確定しない。

| 企業・入口 | 仕事との接続 | 28卒の公開状況・留意点 |
| --- | --- | --- |
| [NRI ITソリューション](https://working.nri.co.jp/recruit/2028/contents/internship/it/) | AEは企画・提案から開発・運用、TEはクラウド・AI等の導入、基盤構築まで。 | 28卒冬インターンITソリューションは9月24日締切済み。[11～12月の1dayイベント](https://working.nri.co.jp/recruit/2028/contents/event/it/)あり。本選考は公開ページで未確認。 |
| [NTTデータ SE](https://nttdata-recruit.com/job/job_se.html) | 業務SEと方式SE。後者は技術要素の組合せ・設計・実装を担う。 | [公開募集要項](https://nttdata-recruit.com/recruit/requirements.html)は27卒。28卒本選考要項は未確認。 |
| [IBM ITスペシャリスト／AIイノベーター](https://www.ibm.com/jp-ja/careers/blog/2028-new-graduate-recruiting-positions) | 前者は要件定義から保守運用、将来アーキテクト。後者はAIのAPI統合・実装も行う。 | [28卒の職種別募集要項](https://www.ibm.com/jp-ja/careers/career-opportunities)公開。AIイノベーターは開発スキル要件を精査する。 |
| [アクセンチュア AI＆Dataアーキテクト／RDEエンジニア](https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level) | AI＆Dataは設計から実装・運用、RDEエンジニアは設計から実装・成果創出。 | 28卒エントリー受付中。ユーザーのCEO起点の特別選考とは別経路。 |
| [PwC ITSC／デジタルコンサルタント](https://www.pwc.com/jp/ja/careers/consulting/campus/selection.html) | ITSCは業務アプリ導入を通じ構想から実行・効果創出。デジタルはAI・アーキテクチャ等、担当領域は幅広い。 | 28卒ITSC国内本選考第1タームは11月15日23:59締切。デジタル職は28卒本選考が案内済み、公開期限は2027年1月8日。 |
| [アビーム デジタルコンサルタント](https://www.abeam.com/jp/ja/recruit/newgrad/course2028/solution-cs/) | 28卒から旧AI・テクノロジーコースを統合。AI・アプリ・クラウドで戦略から実行・定着。配属先はAI & Technology Modernization BU等。 | 28卒秋タームES最終締切は10月29日14:00。採用充足で終了し得る。 |
| [EYSC テクノロジーコンサルタント](https://www.eysc.jp/recruit/new_graduate/entry/new/index.html) | IT戦略・導入支援。[テクノロジー組織](https://www.ey.com/ja_jp/about-us/ey-strategy-and-consulting)にデジタルエンジニアリング、AI＆データ等。 | 28卒国内本選考の案内あり。詳細期限と配属はマイページ確認。 |
| [KPMGコンサルティング IT／Digital Transformation](https://recruit.kpmg-consulting.jp/new-graduate) | ITコンサル等の入口あり。[AI実装事例](https://recruit.kpmg-consulting.jp/work/technologyconsulting/case-study02)もある。ただしNotion記載のテクノロジーリスク職は目的との距離を個別評価。 | 28卒秋選考案内あり。[募集フロー](https://recruit.kpmg-consulting.jp/new-graduate/job-description)はマイページで詳細。 |
| [デロイト トーマツ コンサルティング](https://www.deloitte.com/jp/ja/careers/deloitte-tohmatsu-consulting-students.html) | 技術案件はあるが新卒は広いコンサルタント枠。FDEなど特定部門への配属を保証する募集とは確認できない。 | 28卒MyPage受付。夏選考終了、秋以降に本選考開始と案内。 |
| [BCG X AI Engineer](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x) | [Forward Deployed AI Engineer](https://careers.bcg.com/jp/ja/japan-bcgx)は顧客と具体的なAIプロダクト・ソリューションを設計・構築・実装。 | 28卒新卒AI Engineerを案内。関連修士・博士の応募条件あり。公開ミラー求人ではソフトウェア・クラウド開発経験が強く求められており、[公式求人への再確認](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)が必要。PlatinionのIT Architect新卒枠とは混同しない。 |
| [AWS SA／Professional Services](https://aws.amazon.com/jp/careers/newgraduate/) | SAは技術設計・顧客支援。[ProServe](https://aws.amazon.com/jp/careers/teams/professionalservices/)はアプリ・基盤の設計、開発も行い、本人の実装志向により近い可能性。 | 28卒SA本選考開始。ProServeは「応募予定職種」だが28卒個別求人・時期は未確認。 |
| [NEC SE／AIテクノロジーサービス](https://jpn.nec.com/recruit/newgraduate/matching/department/index.html) | [AI部門](https://jpn.nec.com/recruit/newgraduate/matching/department/704/)は提案、検証、導入、設計、開発、運用。エンタープライズアプリSI等も近い。 | 28卒マイページ入口はあるが、公開の部門別一覧は27卒。28卒の同一部門募集は未確認。 |
| [富士通 ソリューションエンジニア](https://fujitsu.recruiting.jp.fujitsu.com/recruit/) | 顧客向けシステム構築側を志向するならデータサイエンティスト枠より近い。 | [28卒プレエントリー](https://fujitsu.recruiting.jp.fujitsu.com/recruit/entry/)あり。公開募集要項は27卒。 |
| [日鉄ソリューションズ SE](https://www.nssol.nipponsteel.com/recruiting/) | [業務システムの企画・設計・構築](https://www.nssol.nipponsteel.com/recruiting/company/business/)とAIの実業務適用。 | 28卒の本選考職種・期限は公開情報で未確認。 |
| [アバナード 新卒エンジニア](https://www.avanade.com/ja-jp/career/job-details/R00347593) | ソフトウェア、Data Platform、AI等の分野で顧客向けITシステムを設計・構築。AIを組み込む実装志向と近い。 | 2028年4月入社向けの求人を公開。求人ページに応募導線あり。職種ごとの配属確度・締切は要確認。 |
| [Microsoft CSA](https://www.microsoft.com/ja-jp/mscorp/college/mskk-recruit-tech) | Microsoftクラウド導入・技術支援。自らシステムを構築する比重は案件で確認が必要。 | 28卒向け夏インターン募集は終了。28卒本選考は未確認。 |
| [MURC デジタルイノベーション](https://www.murc.jp/service/digital/) | システム構想、要件整理、ベンダー選定、PMOが中心で、本人の直接構築志向より上流寄り。 | [28卒募集要項](https://career.murc.jp/information/requirements.html)は2027年2月頃掲載予定。 |

補足：[PwC ITSCの旧年度選考体験談](https://www.onecareer.jp/companies/89/experiences/2025/165920/920911)ではアプリケーションを用いたワークが記載されるが、現行選考の保証には使わない。Xの断片的な投稿は公式募集要項と照合できず、職種・期限の根拠には用いない。Notion編集は行っていない。

## 追記：ユーザーの訂正と2×2での再調査（同日）

上部の「二つの主軸」は先の暫定整理。ユーザーはその後、**前回の整理が目的地と選考経路を混同していた**と指摘した。現在の議論の枠組みは「ITアーキテクト／AIアーキテクト」×「直接応募／研究で培ったデータサイエンスを採用上の強みとして使う」の4セル。優先順位と応募先は**未決定**。データサイエンス職に入ること自体を目的にしていない。

| 到達先と入口 | 実在する候補と確認できたこと | 28卒・限界 |
| --- | --- | --- |
| ITアーキテクト × 直接 | [NRI AE/TE](https://working.nri.co.jp/recruit/contents/business/ourjobs/ourjobs_b.html)は業務アプリと基盤・処理方式の設計開発。[NTTデータ業務SE/方式SE](https://nttdata-recruit.com/job/job_se.html)も設計・開発。[IBM ITスペシャリスト](https://www.ibm.com/jp-ja/careers/career-opportunities)、[PwC ITソリューションコンサルタント](https://www.pwc.com/jp/ja/careers/consulting/campus/selection.html)も該当。 | IBM/PwCは28卒募集職種。NRI/NTTデータは28卒の本選考要項・職種割当を別途確認する。DSは一般ITアーキテクト採用の明示要件とは限らない。 |
| AIアーキテクト × 直接 | [IBM AIイノベーター28卒要項](https://www.ibm.com/downloads/documents/jp-ja/15db805fff4249c9)はAI構想、API・既存システム統合、実装。応募にはAIの自主学習・検証とプログラミングまたはシステム開発の成果物が必要。[BCG X 28卒AI Engineer](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)、[アバナード28卒AIエンジニア](https://www.avanade.com/ja-jp/career/job-details/R00347593)も候補。 | BCG Xは新卒AI EngineerとDSが別枠。仕事内容・配属の詳細は個別求人で確認する。アバナードはプログラミング経験を重視。 |
| ITアーキテクト × DSの強み | 対象を広いSI全般ではなく**データ基盤・データアーキテクチャ**に寄せると接点がある。[NTTデータのデータ＆インテリジェンス](https://www.nttdata.com/jp/ja/services/data-and-intelligence/)は分析基盤とデータ連携の設計実装。[アバナード28卒Data Platformエンジニア](https://www.avanade.com/ja-jp/career/job-details/R00347593)は新卒入口がある。[NRI TE](https://working.nri.co.jp/recruit/contents/business/ourjobs/ourjobs_b.html)も基盤側だがDSを採用上の優遇要件とする資料は未確認。 | このセルで**DS経験が採用条件として明示され、かつ一般的なITアーキテクト職へ直結する28卒募集**は確認できなかった。アバナードの募集はプログラミング経験を重視。データ基盤への配属や将来の一般ITアーキテクト移行は保証されない。 |
| AIアーキテクト × DSの強み | [アクセンチュア28卒AI＆Dataアーキテクト](https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level)はAIとDSの専門性を明示し、課題分析から設計・実装・運用まで。[NECアナリティクスコンサルティング統括部](https://jpn.nec.com/recruit/newgraduate/matching/department/602/)は「データサイエンティスト（SE職）」として統計・機械学習・最適化とプログラム設計開発を歓迎しAIシステム導入まで扱う。[EYSC AI＆データ](https://www.eysc.jp/recruit/new_graduate/capabilities/tc/aid-message/)はAI・データ経験とITソリューション導入が接続する。[日本総研のITソリューション内データサイエンス](https://www.jri.co.jp/recruit/new_graduates/business/it_solutions/data_science/)はデータ分析経験を望ましい条件とし本番実装も行う。 | アクセンチュア28卒は明確。NECの部門ページは27卒向けで28卒同部門の募集未確認。EYは28卒テクノロジーコンサルタントのAI＆データ配属が保証されない。日本総研は28卒エントリーがあるが公開の詳細コース募集は27卒。NEC/日本総研のDSはモデル開発が主務の一部となり、本人の希望との距離を確認する。 |

補足：[IBM 28卒コンサルティング事業本部DS](https://www.ibm.com/jp-ja/careers/career-opportunities)は分析・AIの専門性を採る明確な経路だが、[職種説明](https://www.ibm.com/jp-ja/careers/blog/2028-new-graduate-recruiting-positions)の主務はAI/機械学習/最適化による課題解決。アーキテクチャ担当を保証しない。[BCG X 28卒](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)もDSとAI Engineerは別職種で、DS採用からAI Engineerになる前提で選ばない。[PwCデジタルコンサルタント](https://www.pwc.com/jp/ja/careers/consulting/campus/recruiting-info/technology-consulting.html)はAI・分析・システムの幅があるが部署配属と実装の比率に幅がある。

この結果からの**提案（決定ではない）**は、IT側をNRI/NTTデータ/IBM/PwCの直接経路として残し、AI側ではアクセンチュアAI＆Data、IBM AIイノベーター、EY AI＆データ、NECアナリティクスなどでDS経験と設計実装の両立を比べること。IT×DSはNTTデータ/アバナード等のデータ基盤職として別途比較し、DS経験で一般ITアーキテクト採用に有利だと推定しない。Notionは編集していない。

## 追記：4セルを企業・職種・28卒入口まで広げた探索（同日）

ユーザーは4セルの整理に同意し、Notionの志望度4以上の企業を優先しつつ、未掲載企業も含めて具体的な部署・職種・採用情報をさらに広く求めた。以下は**調査・提案**であり応募先の決定ではない。2026年10月21日に公開の公式資料を確認。Notionの志望度は本人の過去の記録で、世間一般の就職難易度ではない。28卒の選考は、職種別募集、会社単位の入口、インターン・プレエントリーだけを区別する。非公開のマイページ内日程や配属は未確認とする。

### ITアーキテクト × 直接

- [NRI AE/TE](https://working.nri.co.jp/recruit/contents/business/ourjobs/ourjobs_b.html)はアプリ／基盤アーキテクトへのキャリアが明示される。[28卒サイト](https://working.nri.co.jp/recruit/2028/index.html)はイベント・インターンが公開されるが本選考詳細は未確認。
- [NTTデータ 業務SE／方式SE](https://nttdata-recruit.com/job/job_se.html)は顧客業務・システム方式の設計・構築。[公開募集要項](https://nttdata-recruit.com/recruit/requirements.html)は27卒用で28卒の募集条件は未確認。
- [IBMコンサルティング事業本部 ITスペシャリスト](https://www.ibm.com/jp-ja/careers/blog/2028-new-graduate-recruiting-positions)は要件定義から構築・運用を担い、将来アーキテクトへ進む説明がある。[28卒の職種別募集](https://www.ibm.com/jp-ja/careers/career-opportunities)を確認。
- [PwC ITソリューションコンサルタント](https://www.pwc.com/jp/ja/careers/consulting/campus/selection.html)は業務アプリの構想から実行・効果創出。28卒国内本選考第1タームのESは**2026年11月15日23:59 JST**締切。文理・現在のITスキルを問わず、DSは採用要件でない。
- [KPMG Technology Consulting](https://recruit.kpmg-consulting.jp/work/technologyconsulting)はIT設計・実行の仕事がある。[28卒新卒入口](https://recruit.kpmg-consulting.jp/new-graduate)はあるが、[FAQ](https://recruit.kpmg-consulting.jp/new-graduate/faq)では入社後12～18カ月の育成後に専門チームへ配属。希望部門に直接入れるとは言えない。
- [デロイト コンサルティング](https://www.deloitte.com/jp/ja/careers/deloitte-tohmatsu-consulting-students.html)は28卒入口があるが、募集単位は幅広いコンサルタント。AI・エンジニアリング部門やFDEへの新卒配属は未確認。
- Notion外の[日本総研 ITソリューション](https://www.jri.co.jp/recruit/new_graduates/)、[日鉄ソリューションズ SE](https://www.nssol.nipponsteel.com/recruiting/internship/)、[MUIT オープンコースSE](https://www.it.mufg.jp/recruiting/fresh/recruit/guideline.html)も候補。28卒は日本総研のエントリー、NSSOLのマイページ／イベント、MUITのメンバーサイトまで確認。MUIT公開募集要項のコース内容は27卒用。

### AIアーキテクト × 直接

- [IBM AIイノベーター](https://www.ibm.com/jp-ja/careers/blog/2028-new-graduate-recruiting-positions)はAIの構想、モデル選定・評価、API／既存システム統合と実装。28卒の独立職種として募集要項がある。
- [BCG X 28卒 AI Engineer](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)はDSと別職種。関連領域の修士・博士課程と職歴条件を公開。[BCG Xの仕事紹介](https://careers.bcg.com/jp/ja/japan-bcgx)でForward Deployed AI Engineerの構築実装を確認したが、新卒入社時の担当範囲は個別求人で確認が必要。
- [アバナード28卒エンジニア求人](https://www.avanade.com/ja-jp/career/job-details/R00347593)にはAIエンジニア、Data Platformエンジニア、ソフトウェアエンジニアなどの分野が併記され、システム設計・構築に携わる。2028年4月入社向けでプログラミング経験が望ましい。採用後の分野確約は確認できない。
- [AWS 28卒ソリューションアーキテクト](https://aws.amazon.com/jp/careers/newgraduate/)は本選考受付開始。ただし設計助言の比率が高く、顧客システムの実装そのものを担う[Professional Services](https://aws.amazon.com/jp/careers/teams/professionalservices/)は28卒個別募集未確認。
- [Microsoft Cloud Solution Architect](https://www.microsoft.com/ja-jp/mscorp/college/mskk-recruit-tech)はクラウド導入支援の職種だが、公開の募集は終了しており28卒本選考を確認できない。顧客システムの実装範囲も要確認。
- [NRI AI Design／AXイノベーションセンター AIソリューション推進部](https://www.nri.com/jp/service/solution/solution_ai.html)はAI選定、既存システム連携、基盤構築・運用を扱う実在組織。ただし28卒の同部門指定採用は未確認。

### ITアーキテクト × DSの強み

- **該当する仕事はあるが、28卒でDS経験が選考上の明示要件で、かつITアーキテクトへの配属・経路が確定する募集は確認できなかった。** 分析職ではなく、データ基盤・データエンジニアリング職として候補を置く。
- [EYSC AI&データ](https://www.eysc.jp/recruit/capabilities/tc/aid/)にはIoTデータ基盤の構想・開発・運用、データ加工・可視化・AI環境構築の実例がある。[28卒新卒入口](https://www.eysc.jp/recruit/new_graduate/entry/new/index.html)は本選考受付中。ただしAI&データへの配属は未確認。
- [NTTデータ Data & Intelligence](https://www.nttdata.com/jp/ja/services/data-and-intelligence/)は分析基盤やデータ連携を実装。28卒はSEという広い入口で、DSによる選考上の優位や当該チーム配属は未確認。
- Notion外の[McKinsey QuantumBlack 東京 Data Engineer](https://www.mckinsey.com/careers/search-jobs/jobs/dataengineer-quantumblackaibymckinsey-105274)は顧客データ品質・分析基盤・MLデータパイプラインを構築する公開求人。28卒新卒専用募集ではなく、応募資格・採用可能性は要確認。一般的なITアーキテクトではなくデータアーキテクチャ寄り。
- Notion外の[TDSE 28卒エンジニア](https://www.tdse.jp/recruit/preentry/)はMLOps基盤、アプリ、DB設計・運用を担う。28卒はプレエントリー受付で、本選考日程は未公開。同社の知名度・選考難易度をNotionレベル4相当と断定しない。
- Notion外の[住友商事グループ InsightEdge 28卒ソフトウェアエンジニア](https://herp.careers/v1/insightedge/Enkj0X4CKAA5)は分析系バックエンド、分析基盤の設計構築を担当する公開求人。[同社28卒データサイエンティスト](https://herp.careers/v1/insightedge/ULzcvO5ofDdd)とは別枠。後者は本番化時にアーキテクトチームと協働するが、本人自身のアーキテクト配属を意味しない。会社の採用管理サービス上の公式求人を検索結果で確認し、直接ページは取得制限のため全文読取不可。
- [アバナード Data Platformエンジニア](https://www.avanade.com/ja-jp/career/job-details/R00347593)も28卒枠がある。ただし募集要件はプログラミング経験中心で、DS研究経験の採用上の評価や同分野への配属確約は確認できない。

### AIアーキテクト × DSの強み

- [アクセンチュア 28卒AI＆Dataアーキテクト](https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level)はAI・DSの専門性と、課題分析→ソリューション選定→アーキテクチャ→実装・運用を同じ職種説明で明示。4セル中、ユーザーの仮説を最も直接裏付ける28卒枠。ユーザーのCEO起点特別選考とは別の公開通常選考であり、結果は未確定。
- [NEC アナリティクスコンサルティング統括部](https://jpn.nec.com/recruit/newgraduate/matching/department/602/)はデータサイエンティスト（SE職）が顧客へAIを導入し業務システムに組み込む。統計・ML・数理最適化とプログラム設計・開発力を活かせると明記。ただしページは27卒部門別募集で28卒同部門募集は未確認。分析業務の比重も大きい。
- [IBM 28卒コンサルティング事業本部 データサイエンティスト募集要項](https://www.ibm.com/jp-ja/downloads/documents/jp-ja/1227c12efab8b25d)はML・数理最適化の経験を歓迎し、エンジニアリングも習得する意思を求める。分析・モデルを主務とし、AIアーキテクト配属は確認できない。
- [日本総研 ITソリューション内データサイエンス](https://www.jri.co.jp/recruit/new_graduates/business/it_solutions/data_science/)はSMBCグループ向けにAIモデルの構築から本番実装まで行う。組織が目指すキャリアはデータサイエンティストであり、本人の実装・設計志向とずれ得る。
- [デロイト リスクアドバイザリー 28卒AI・アナリティクスコンサルタント](https://www.deloitte.com/jp/ja/careers/deloitte-tohmatsu-risk-advisory-students.html)は専門ユニット「デロイトアナリティクス＆デジタルガバナンス」へ入社時配属。仕事内容は課題特定、分析、インサイト、戦略・実行支援で、システムのアーキテクチャ設計は明記されず、本人の最終目標とは距離がある。
- [BCG X 28卒Data Scientist](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)、[MUITデータサイエンスコース](https://www.it.mufg.jp/recruiting/fresh/recruit/guideline.html)、[InsightEdge 28卒DS](https://herp.careers/v1/insightedge/ULzcvO5ofDdd)もDS経歴の入口として実在。ただし各々AIシステム設計者への直接配属・昇格は確認できず、モデル・分析の比重を見極める必要がある。MUIT公開募集要項は27卒用。

### 議論へ持ち込む暫定結論と未解決点

- 4セルのうち、**AI×DSのアクセンチュア**は仕事内容と採用上の専門性が同じ28卒職種で結び付いている。**IT×直接**はNRI、NTTデータ、IBM、PwC等に明確な入口がある。**IT×DS**はデータ基盤へ絞れば仕事は見えるが、本人の研究が採用上評価されて一般ITアーキテクトへ進めるという連結は未証明。
- [EYの実案件](https://www.eysc.jp/recruit/capabilities/tc/tccase/offerings-13/)では統計・AIモデルをDSユニット、既存システム連携やダッシュボード構築をデジタル・エンジニアリングユニットが分担。DS採用からシステム設計を担当できるとは限らない根拠。
- 比較の次段階では、各社の「新卒時に部署を選べるか」「本人が設計・実装を担当する割合」「モデル開発の比率」「一般顧客向けかグループ内向けか」「研究から示せるプログラミング・クラウド・API経験」を確認する。
- X等も補助的に検索したが、該当職種・28卒条件を職種単位で検証できる投稿は見つからず、今回の募集・期限の根拠には使わなかった。Notionは編集していない。

## ④に絞った志望度不問の統合探索

### ユーザーの追加指示

- アクセンチュアAI＆Dataのように、DSとAI（特にAIアーキテクチャ）を同時に扱う企業・部署を、今回は志望度の上限を外して網羅的・探索的に調べる。
- この探索を一度区切れるよう、既出候補も再確認して全体を統合し、このチャットで結果を提示する。

### 実施と主な発見

- [統合調査資料](../research/2026-10-21-ai-data-organizations.md)に、AI・DS専門企業、大手コンサル、SIer、データ/クラウドベンダーの部署・職種、DS経験の評価、28卒状況と根拠を保存した。公開採用・職種別ATSを中心に、企業掲載LabBase/AtCoder Jobs求人、公式note・社員技術記事も確認した。
- **ARISE analytics**は28卒AIエンジニアの入口があり、統計や研究でのプログラミングを歓迎。分析基礎から、データアーキテクト・ソリューションエンジニア等を選ぶ経路を公式に示す。
- **フューチャーAIXG**はAI/DSの研究と顧客実装の専門組織。28卒のTech選考で研究を評価し、アドバンスト採用では専門部門の候補にAIXGを明示。研究歴だけで高度専門性の審査に通るとは推定しない。
- **ABEJA**は28卒DSに加えて、DSと協働して顧客のAIシステムを要件定義から運用まで構築するソリューションエンジニアを募集。ユーザーの仕事志向には後者の説明が近い。開発経験の条件がある。
- **RONNABYTE（旧DATUM STUDIO）・ちゅらデータ**は28卒AI/データ系の入口があり、AIアプリ・本番化・データ基盤・アーキテクチャと研究経験の接点が具体的。RONNABYTEは2026年10月1日の統合・商号変更を現行特設サイトで確認。ちゅらデータは別法人・子会社として残る。
- **エクサウィザーズ**の28卒エンジニアには顧客ML/LLMのPoCから導入を進めるFDEを含む。研究での実装・検証を評価するが自社製品等への配属もあり、FDE確約とは扱わない。
- **ブレインパッド、TDSE、電通デジタル、AVILEN、Ridge-i、pluszero、GRI、InsightEdge、NTTデータ数理システム**でもDSと実装の接点と新卒入口を確認。28卒プレ登録と本選考、27卒参考の職種説明を区別。GRI掲載求人の専攻条件、pluszeroのML等の研究開発要件など、本人の現在の経験だけで満たすとしない。
- 大手側ではEY AI＆データ、デロイトAI＆D、PwC AI実装、KPMG DXA/Data＆AI、アビームAI＆Technology Modernization、Capgemini Insights＆Data等が組織として候補。新卒からの部門配属確度は別途確認する。

### 前回の読み取りの訂正

- アバナード28卒Engineerのページは、本文に関連する中途職や27年10月入社求人が混在していた。**28卒Engineer募集タイトルは確認できるが、Data Platform/AIの職種内訳まで28卒確定としない。** 中途Data＆AIの仕事内容は実在する別の根拠として扱う。
- 「DS採用からアーキテクト確約」を唯一の探索条件にすると、同じ組織でDSとシステムエンジニアが協働する有力候補を落とす。ユーザーの最新指示は、組織として両方を扱う候補も対象。職種分担を明示して候補に含める。
- **④に合う仕事がほとんどない、とは結論しない。** 新卒の入口まで具体的な複数候補が見つかった。応募順位の決定ではなく、比較対象が増えた段階。

### 期限・次の比較

- Ridge-i早期選考：2026年10月31日まで。RONNABYTEの企業掲載28卒求人：2026年11月1日まで。いずれも終了時刻未記載。アビーム秋タームES：2026年10月29日14:00。PwCデジタルコンサル：2027年1月8日23:59（日本時間、28卒最終募集と案内）。根拠は統合資料の個別行。
- 残る判断は、顧客向けの設計実装を本人がどこまで担当するか、分析・モデル開発の比率、研究経験の評価方法、内定時の職種/部門確定、専攻条件。探索追加を際限なく続けるより今回の母集団を比較するための資料にする、というCodexの提案。
- Notion編集、応募、登録、問い合わせ送信は行っていない。GitHub用記録とHANDOFFを更新して引き継ぐ。

## 採用単位のAI/データ統合と企業評価による再絞り込み

### ユーザーの最新の希望

- AI＆データという同じチームだけでなく、**募集単位でもAIとデータの両方を扱う先**を重視する。BCGとIBMが職種別募集ではないかと確認を依頼。EY・デロイトに魅力を感じている。
- **アクセンチュア以上の企業評価・就職難易度を優先したい**と再度明示。直前の志望度不問の探索から絞る段階になった。
- 「職種別募集は自分に不利かもしれない」は仮説であり、合格率や有利不利の確定ではない。応募企業・順位は未決定。

### 調査・修正

- [採用単位別の調査資料](../research/2026-10-21-ai-data-hiring-units.md)に根拠と提案を保存。専門枠、広い共通枠、同じ組織内の別職種、中途の専門求人を区別した。
- **BCG Xの重要な新情報：** [公式28卒入口](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)ではDS/AI Engineerは別ポジション。ただし[企業掲載28卒DS求人](https://compass.labbase.jp/company/665/recruit/56146)に、AIエージェント・データプロダクトの設計実装と、MLOps・データ基盤を含むアーキテクチャ構築を明示。以前の説明を補足し、**DS職の中で設計実装ができる候補**として残す。Python・MLモデリング・研究・英語等の条件がある。
- [IBM](https://www.ibm.com/jp-ja/careers/career-opportunities)もAIイノベーターとDSは別採用。AI側に研究の開発成果物が使えるので、職種分離だけで研究が評価されないとは言わない。DS側のエンジニアリング学習要件と、AIアーキテクチャを主担当にする採用は同一ではない。
- [デロイトRAの28卒AI・アナリティクス](https://www.deloitte.com/jp/ja/careers/deloitte-tohmatsu-risk-advisory-students.html)は、専門ユニット入社時配属を明記。ただし主たる新卒職務は分析・示唆・戦略実行支援で、システム設計実装の比率は未確認。デロイトコンサルティングAI＆Dの経験者向けアーキテクト求人とは別経路。
- [PwCデジタル](https://www.pwc.com/jp/ja/careers/consulting/campus/recruiting-info/technology-consulting.html)はAI＆アナリティクスと生成AI/エージェント実装・運用を共通入口内に持つが配属確約未確認。[EY](https://www.eysc.jp/recruit/new_graduate/entry/new/index.html)もTCという広い入口。コンサルタント期はACG/TCGで経験し、シニアからユニット正式配属。AI＆データ指定の28卒専門枠とは扱わない。
- [KPMG DXA Data/AIソリューションアーキテクト](https://recruit.kpmg-consulting.jp/job-description/13955)は分析/モデルと顧客システム設計実装を同じ求人で扱うが中途。新卒は一般枠・育成後配属で、同職務指定の28卒入口は未確認。
- **新候補KPMG FAS CVA**の[28卒AI・データサイエンス主導型コンサルタント](https://recruit.kpmg-fas.jp/recruitinginformation-d.html)は研究のPython/R分析経験を明示。統合枠として重要だが、公開締切2026-05-29 13:00は経過済み。追加募集未確認で、現在応募できる候補には数えない。仕事はM&A/経営分析寄り。
- 大学通信の[2025入社難易度指標](https://univ-online.com/article/ranking/36523/)も確認。出身大学の入試難易度の加重平均であり、企業・専門職の採用合格率ではない。企業評価を重視するユーザーの方針と、全Big4がアクセンチュアAI＆Dataより難しいという未証明の主張は分ける。

### 比較提案と未決定点

- Codexの提案は、BCG X DSを上振れを狙う挑戦先として残し、専門配属が明確なデロイトRA AI・アナリティクス、共通枠のPwCデジタル/EYテクノロジーを中心に比較すること。デロイトコンサルティングAI＆D/KPMG Data＆AIは新卒配属確度を確認する対象。
- 同じ採用枠であることは、本人が両方の仕事を担う保証ではない。研究要件・ML実績・モデル開発の比率・システム実装の担当範囲が次の論点。EY・デロイトへの応募や優先順位を決定したわけではない。
- Notion編集、応募、登録、問い合わせ送信なし。関連資料とHANDOFFをGitHubへ記録して引き継ぐ。

## BCG DSの重心の再評価とMBB級への追加探索

### ユーザーの指摘と現時点の判断

- ユーザーはBCG X DSについて「データサイエンスの色が強いのではないか、AIアーキテクトのニュアンスが読み取れない」と指摘。希望に近ければよいが、BCG級の挑戦先に類似の企業・部署があるか追加調査を依頼した。
- [公式BCG職種紹介](https://careers.bcg.com/jp/ja/japan-bcgx)と28卒企業掲載DS要項を比較。**DSが分析・モデルを中心にするという理解を支持し、Codexが前に強く適合を推した評価を修正。** AI実装・アーキテクチャの記載はあるが、顧客システム全体設計が主務である証拠ではない。担当比率は未確認で、DSは条件付き候補とする比較提案。AI Engineerの方が仕事の中心は近いが別選考・開発経験が必要。

### 探索と根拠

- [MBB等の追加調査資料](../research/2026-10-21-mbb-ai-implementation.md)を作成。McKinsey、Bain、BCGに加えOliver Wyman、Kearney、AlixPartners、Strategy＆、Palantir、OpenAI、Anthropic、Google Cloud、Databricks等の公開採用・職種説明を探索した。
- **McKinsey QuantumBlack東京Data Engineer（105274）**が追加の具体候補。分析用基盤・MLパイプライン構築、Python/pandas等を扱い、必須経験年数の記載なし、インターン等の経験は歓迎。ただし28卒・専攻・2028年入社の受入は未確認。研究のデータ処理経験が接続し得るという推論と、採用資格の確定を区別する。
- 同組織のArchitect（111203）は顧客要件からクラウド/API/全体設計・実装を扱うが専門経験5年以上。東京DS（105275）はML等の実務2年以上。Tech＆AI Software Engineer（105277）は顧客向け分析Webシステムを作るが、Web開発の実績を求め、DS採用そのものではない。
- **Bain AIS**はDS/MLとAIエンジニアリングを併せ持つ実在組織だが、日本28卒の専門入口は未確認。東京経験者DSのリンク先101880は現在公式に掲載終了表示。一般ACから専門配属を保証しない。
- Oliver Wyman Quotientも類似組織だが国内28卒専門入口未確認。Palantir東京FDEはデータ活用システムの顧客設計実装とDS背景の接点が強いが、卒業後実務1年以上。Deployment Strategistは分析経験を歓迎するがFDEとの分担がある。OpenAI/Anthropicの東京導入職は仕事内容が近く、公開求人は経験者向け・28卒指定未確認。
- McKinsey一般28卒BA冬選考締切は2026-09-15、Bain一般28卒冬インターン応募締切は2026-10-07 13:00で経過済み。QB/AISの専門求人に一般採用の締切を流用しない。BCG Xの28卒専門入口は公開されている。

### 比較提案と操作記録

- MBB級に限定して、DS専門性の採用とAIシステム全体設計を主務とする日本28卒の統合枠は明確に確認できていない。**類似の仕事があることと、今28卒で応募できることを分ける。**
- 仕事との適合ではBCG X AI Engineer、新しい受入確認対象としてQuantumBlack東京DE、分析中心も許容できる場合の条件付きBCG X DSを比較する提案。ユーザーが応募先・順位を決めたわけではない。
- BCG公式AI Engineer個別求人は取得本文とブラウザの両方で職務本文が表示されなかったため、詳細要件の転載は参考扱い。ブラウザは公開ページの確認と必須クッキーの選択のみで、一時タブを閉じた。
- Notion編集、応募、登録、問い合わせ送信なし。調査資料、前回資料の修正注記、HANDOFF、同日ログを記録する。
