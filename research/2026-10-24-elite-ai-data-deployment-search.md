# Big4以外の「データの強みから顧客向けAIシステム導入」探索

確認日：2026年10月24日（日本時間）。公式採用情報を優先して確認。募集状況と応募資格は変わる。就職難易度の企業横断・職種別の比較可能なデータは見つからず、ここで「Big4以上」の順位を実証していない。MBBと著名なグローバルAI／クラウド／データ企業を挑戦先として探索した。

## 本人の希望と判定条件

- 本人の到達先は、顧客の業務に合うAIシステムについて、課題・データ・モデルや既製AIサービス・既存システム／API・クラウド・評価・セキュリティ・運用を組み合わせて設計し、実装・本番導入へつなぐこと。基盤モデル研究や分析専業は主目的ではない。
- 「データサイエンスを入口にする」は、神経科学研究で培った分析・仮説検証・データ品質の経験が、その職種の求める人物像や採用審査に明示的に合い、入社後の仕事にも接続すること。データサイエンス部門とAI実装部門が同じ会社に存在するだけでは該当としない。
- 仕事の一致、データの強みの採用上の価値、同一募集単位、国内の28卒入口を別々に判定する。

## 重要な結論

調べた範囲で、**日本の28卒が応募できることを公式に確認でき、同一の募集職種で「分析経験を採用の入口として生かす」かつ「顧客向けAIシステムの全体設計・実装・導入を主業務とする」候補は、Big4／Accenture以外で確認できなかった**。これは不存在の証明ではない。現在の公式求人で仕事内容が最も近いDatabricks、Google Cloud、OpenAI、Palantirは経験者向け。BCG Xには28卒のDS職とAI Engineer職があるが別募集。McKinsey QuantumBlackのData Engineer Iは若手向けに見えるものの、28卒専用入口ではなく、中心業務はデータ基盤とMLパイプライン。AWSは28卒SA募集が実在するがAI・DSを一体で採る職種ではない。

## 企業×部署・職種×入口

| 企業・部署・職種 | 実際の担当範囲・データ経験との接点 | 国内28卒の入口・欠ける条件 |
| --- | --- | --- |
| [Databricks：Forward Deployed Engineering / Forward Deployed Engineer 東京](https://www.databricks.com/company/careers/professional-services-operations/forward-deployed-engineer-8741922002?gh_jid=8741922002) | 顧客のデータ・AI課題に対し、アーキテクチャを所有し、データ取り込み、ML/AIモデル統合、顧客アプリ、既存システム統合から本番まで実装。**仕事内容は今回最も近い部類**。採用はデータエンジニアリング／分析基盤／ソフトウェア工学の経験重視で、神経科学の分析だけでは足りない。 | 公式求人は**8年以上**の経験を要求。28卒入口ではない。製品Databricks上の実装が中心。 |
| [Google Cloud：Forward Deployed Engineer, Generative AI 東京](https://www.google.com/about/careers/applications/jobs/results/116466339920388806-forward-deployed-engineer-generative-ai-google-cloud-japanese-english) | 顧客の既存API・データ・セキュリティにAIを接続し、エージェントの本番化、評価基盤、監視まで作る。**AIアーキテクト像と非常に近い**。PythonとMLパッケージ、応用AIが要件なのでデータ／MLの強みも採用上関係する。 | **Python＋ML関連5年**とクラウド設計・導入経験が最低要件。28卒向けではない。 |
| [OpenAI：Applied AI Engineering / Applied AI Engineer 東京](https://openai.com/careers/applied-ai-engineer-tokyo-tokyo-japan/) | 顧客の用途選定からアーキテクチャ、試作、評価、既存環境統合、本番化・利用定着まで。データは評価・検索・運用判断の基盤で、**新規モデル研究は主務ではない**。 | 年数の明記はないが、**企業のAI/MLシステムを本番まで届けた実績**を求める現行求人。28卒募集としては確認できない。研究でのデータ解析のみで足りるとは言えない。 |
| [Palantir：Forward Deployed Software Engineer / Japan Government 東京](https://jobs.lever.co/palantir/12e94938-55cb-4ad9-9c05-405ebc9ef430) | 顧客課題の理解、データ整理、アーキテクチャ相談、カスタムアプリ開発を同じ職種で担当。採用要件にData Science分野を明記。ただしAI導入は案件次第で、求人の中心説明は**データを使うシステム構築**。 | **卒業後の関連実務1年以上**が必須。安全保障上の条件あり。[新卒求人一覧](https://www.palantir.com/careers/open-positions/)では東京の新卒FDSEを確認できない。 |
| [McKinsey：QuantumBlack / Data Engineer I 東京・大阪](https://www.mckinsey.com/careers/search-jobs/jobs/dataengineer-quantumblackaibymckinsey-105274) | DS・ML Engineerと組んで顧客データの品質確認、MLパイプライン、分析基盤、再現可能なデプロイを担当。学位、Python等、分析ライブラリを要件に含み、業務上のDS接点はある。 | **28卒専用求人とは表示されない**。実務経験は加点で必須年数の明記なし。ただしAIアプリ全体の設計より**データ・ML基盤が中心**。[同社Architect職](https://www.mckinsey.com/careers/search-jobs/jobs/architect-quantumblackaibymckinsey-111203)は別求人・5年以上の経験。 |
| [BCG X Japan：Data Scientist／Forward Deployed AI Engineer](https://careers.bcg.com/jp/ja/japan-bcgx) | 同じBCG X内で、DSは分析・機械学習・モデル設計、AI Engineerは顧客向けAIプロダクトの設計・実装が主担当。共同作業はありうるが、**個人の職務と選考入口は分離**。 | [28卒案内](https://careers.bcg.com/jp/ja/japan-new-grads-bcg-x)はDS職とAI Engineer職の**別応募**を指示。現時点で確認した[DS個別求人](https://careers.bcg.com/global/en/job/58408/Data-Scientist-%E6%96%B0%E5%8D%92-New-Graduate-2028-BCG-X-Japan)と[AI Engineer個別求人](https://careers.bcg.com/global/en/job/59586/AI-Engineer-%E6%96%B0%E5%8D%92-New-Graduate-2028-BCG-X-Japan)はいずれも「filled」。公式案内と個別求人の状態が食い違うため、応募時は新しい募集を再検索。 |
| [AWS Japan：28卒Solutions Architect](https://www.amazon.jobs/pl/jobs/10503564/2028-aws-solution-architect-field-ags-apj-tech-cs) | 顧客システムを分析しAWSサービスを組み合わせて設計、導入まで伴走。設計図を描く仕事として本人の「アーキテクト」に近いが、AWS側も実装担当エンジニアとは区別している。 | [28卒本選考受付中](https://aws.amazon.com/jp/careers/newgraduate/solutionsarchitect/)。**クラウド全般のSA採用**であり、AI&Data特化やDS経験重視は公式要項にない。応募は採用枠終了まで、他のAmazon/AWS職種と同時選考不可。 |
| [Snowflake：Frontier Engineering / Solutions Architect 東京](https://careers.snowflake.com/us/en/c/professional-services-jobs?subSearchTextbox=2025) | 公式求人一覧で東京の職名を確認。同社の[FDEによる顧客導入事例](https://www.snowflake.com/en/customers/all-customers/case-study/order-co/)にはデータ移行、品質検証、ML推論基盤とAI補助開発がある。ただし**東京の当該SA本人がそれをどこまで実装するか**は求人本文で検証できていない。 | 東京28卒の同職種募集は確認できず。東京の「AI Deployment Strategist」は別職種で、技術実装の本人担当とは扱わない。 |
| [Anthropic：Applied AI Engineer 東京](https://job-boards.greenhouse.io/anthropic/jobs/5390799008) | 顧客向けClaudeの構成設計・既存環境統合・試作・評価・導入助言。データ分析より技術アドバイザー／AI実装が中心。 | FDE／プラットフォーム等の経験が最低要件、4年以上を優遇。28卒入口は確認できず。 |
| [Bain：AI, Insights, and Solutions](https://www.bain.com/vector-digital/advanced-analytics/advanced-analytics-group/) | AI・分析・ソフトウェアの横断組織があり、事業としては合致する。 | 日本28卒向けの「DSで入り、AIシステム設計・導入も担う」**単一職種の公式求人を確認できない**。組織の存在のみで候補とはしない。 |

## 応募上の読み方

- **28卒として今選考対象にしやすい拡張候補**：AWS SAは募集要項が明確。ただしAI×DSルートではなくIT／クラウドアーキテクトからAI案件へ進む別ルート。BCG Xは28卒枠の存在が公式に明示されるが、希望するDSからAIアーキテクトへの一体職種ではなく、確認した個別求人はfilled。McKinsey QuantumBlack Data Engineer Iは応募資格を個別確認する価値があるが、「AIアーキテクトになれる入口」と保証できない。
- **仕事内容の参照・将来の経験者応募候補**：Databricks FDE、Google Cloud GenAI FDE、OpenAI Applied AI Engineer、Palantir FDSE。これらは「データ・AI・顧客システム導入が一つの職種で成立する」実例。ただし28卒の現行ターゲットに加えない。
- **研究経験で主張できる範囲**：データ品質、目的に合う評価指標、仮説検証、分析の限界を見極める力。各社が求める本番システムのコード、クラウド、API連携、セキュリティ、運用の経験を既に持つとは言わない。
- 本調査は候補探索であり、本人の志望先を増やす**決定はしていない**。Notionは編集していない。
