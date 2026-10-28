# 5社のAI・データ情報を探すためのサイト地図

確認日：2026-10-28。日本語トップから公式サイト内のリンクを追った調査。件数と手法は[README](README.md)、全ページは各社索引にある。ここでは、次の議論・自己分析・ESで何をどこから調べるかを残す。

## デロイト トーマツ

- 起点：[日本語トップ](https://www.deloitte.com/jp/ja.html)
- 中心経路：トップ → [Engineering, AI & Data](https://www.deloitte.com/jp/ja/services/consulting/services/engineering-ai-data.html?icid=top_engineering-ai-data) → [Artificial Intelligence & Data](https://www.deloitte.com/jp/ja/services/consulting/services/artificial-intelligence-and-data.html)。この配下からサービス、専門家、技術解説、世界・業界別調査に枝分かれする。
- 技術を知る入口：[RAGとマルチモーダルLLM](https://www.deloitte.com/jp/ja/Industries/technology/blogs/generative-ai-trends.html)、[経営管理エージェントの設計](https://www.deloitte.com/jp/ja/services/consulting/perspectives/management-ai-agent.html)、[データアーキテクチャ](https://www.deloitte.com/jp/ja/services/consulting/perspectives/data-architecture-for-data-driven-management.html)。仕組み・データ設計・評価・運用の具体論を探す。
- 導入を知る入口：[AI Factory](https://www.deloitte.com/jp/ja/services/consulting/services/ai-factory.html)。構想、検証、アプリ・基盤、本番導入、運用と人材育成の提供範囲を調べる。
- 調査を知る入口：[Deloitte AI Institute](https://www.deloitte.com/jp/ja/services/consulting/collections/ai-institute.html)、[企業におけるAIの活用状況](https://www.deloitte.com/jp/ja/issues/generative-ai/state-of-ai-in-enterprise.html)。日本語解説から英語原資料や業界別PDFへつながる。
- 構造上の特徴：日本語サービスの体系と、Deloitte Insights／AI Instituteの世界的な調査・解説網が相互につながる。技術から業界別の導入課題へ切り口を変えて深掘りしやすい。
- 選考での使い方：技術テーマを1つ、顧客・業界の課題を1つ選び、その接点を具体化する。記事の執筆法人、顧客事例か社内利用か、希望するコンサルティングAI&Dとの関係を原文で再確認する。
- [全URL索引](deloitte.md)

### ユーザー提示PDFへの到達を確認

次のリンク列を公式ページで確認した。代表経路は日本語トップから4リンク。トップの別の記事から入る短い経路もあり、索引の最短到達段数とは異なる。

1. 日本語トップ → Engineering, AI & Data（メインナビゲーション）。
2. Engineering, AI & Data → Artificial Intelligence & Data。
3. Artificial Intelligence & Data → 「企業におけるAIの活用状況」。
4. 同ページの「業界別に見る企業のAI活用状況」→「ライフサイエンス・ヘルスケア」→ [提示されたPDF URL](https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/StateofAI-LSHC.pdf?icid=mosaic-grid_---------------)。

提示URLをHTTP 200、PDF、42ページとして実取得できた。PDF内の物理ページ数42は今回のURL数に加算せず、1 URLとして扱う。同じ日本語紹介ページには[別の公式URLにある英語PDF](https://www.deloitte.com/content/dam/assets-shared/docs/about/2026/state-of-ai-lshc.pdf)もリンクされる。

この資料はライフサイエンス・ヘルスケアのAI活用調査で、AIの本番展開、人材、ソブリンAI、エージェント、フィジカルAI、データ基盤などを扱う。研究背景と顧客AI導入への関心をつなぐ際に再読する価値がある。指標を使うときは、調査対象・実施時期・回答者の見通しか実績かを本文で確認する。

## EYジャパン

- 起点：[日本語トップ](https://www.ey.com/ja_jp)
- 中心となる二つの入口：[AIインサイト](https://www.ey.com/ja_jp/services/ai)と[AI&データ](https://www.ey.com/ja_jp/services/consulting/data-analytics-modernization)。前者は経営・社会・業界の記事群、後者は提供サービスと専門家・実務に近い情報への入口。
- 関連する枝：[アナリティクス・コンサルティング](https://www.ey.com/ja_jp/services/consulting/analytics-consulting-services)、人材・組織、税務、監査、M&AのAIプラットフォーム。サービス紹介から担当者プロフィール、事例、ニュースリリース、英語の知見へ進む。
- 具体例：[ソニー銀行の生成AI活用と人材育成](https://www.ey.com/ja_jp/insights/financial-services/how-sony-bank-is-utilizing-generative-ai-to-develop-innovative-human-resources)、[Fractaとの下水道管路の劣化予測](https://www.ey.com/ja_jp/newsroom/2022/07/ey-japan-news-release-2022-07-11)。実際の課題、データ分析、導入や組織への定着をつなげて調べる入口になる。
- 構造上の特徴：横断的なAI発信と、個別サービス・専門家・事例がつながる。記事の論点と、誰がどの領域を担当しているかを併せて調べやすい。
- 選考での使い方：AI&データの希望業務に近いサービスを選び、その担当者や関連事例に進む。EY全体、EYSC、監査・税務などの所属を混同しない。
- [全URL索引](ey.md)

## PwCジャパン

- 起点：[日本語トップ](https://www.pwc.com/jp/ja/)
- 中心経路：トップ → [データ＆AI](https://www.pwc.com/jp/ja/services/data-analytics-ai.html) → [データアナリティクス](https://www.pwc.com/jp/ja/services/consulting/analytics.html)。個別の導入サービス、解説シリーズ、調査レポートへ進む。
- 実務を知る枝：[AIエージェント導入支援](https://www.pwc.com/jp/ja/services/consulting/analytics/ai-agent.html)、[データ基盤の構築](https://www.pwc.com/jp/ja/services/consulting/analytics/build-your-data-foundation.html)、[次世代データプラットフォーム](https://www.pwc.com/jp/ja/services/consulting/analytics/data-platform.html)。
- 技術を知る枝：「テクノロジー最前線 データアナリティクス＆AI編」などの連載。例として[自然言語処理・数理最適化とリスキリング](https://www.pwc.com/jp/ja/knowledge/column/technology-front-line/vol11.html)がある。シリーズ内の別回へ広げて、技術と業務用途を一緒に読む。
- 経営・統制を知る枝：[生成AI実態調査2026](https://www.pwc.com/jp/ja/knowledge/thoughtleadership/generative-ai-survey2026.html)、[AIガバナンス](https://www.pwc.com/jp/ja/services/data-analytics-ai/responsible-ai.html)。
- 構造上の特徴：大きなサービス群の下に、業務・課題別サービスと連載記事が細かく配置される。日本語の具体的な論点を連続して読む用途に向く。グローバルの調査・知見へのリンクもある。
- 選考での使い方：興味のある業務用途を1つ選び、導入サービスと技術連載を対にして読む。希望するDAX／AI&Analyticsとの関係は採用資料で別途確認する。
- [全URL索引](pwc.md)

## KPMGジャパン

- 起点：[日本語トップ](https://kpmg.com/jp/ja.html)
- 中心となる入口：[KPMG.ai](https://kpmg.com/jp/ja/insights/topic/ai.html)。関連サービス、顧客対談、AI調査、信頼・ガバナンス、海外の事例・PDFへ分岐する。
- 実務を知る枝：[データ分析ソリューション](https://kpmg.com/jp/ja/services/advisory/management-consulting/data-analytics.html)、[エマージングテクノロジーによる業務変革](https://kpmg.com/jp/ja/services/advisory/management-consulting/ai-bpr.html)、AI Assurance等。コンサルティングと監査・リスク側の両方に情報がある。
- 技術を知る枝：[AIが企業データの文脈を理解するための解説](https://kpmg.com/jp/ja/insights/2026/10/ai-readydata-01.html)、[RAGの業務適用に関するPDF](https://assets.kpmg.com/content/dam/kpmgsites/jp/pdf/2024/jp-rag_ai_03.pdf)。ガバナンス以外の技術・実装の論点も確認できる。
- 構造上の特徴：KPMG.aiを中心に、導入事例、部門別サービス、信頼やガバナンス、グローバル調査が接続する。AI、データ分析、監査業務への応用が複数法人にまたがる。
- 選考での使い方：Data & AI／DXAに直接関係する資料を探し、そのうえでグループ全体の監査・ガバナンス知見との接点を語る。全グループのページ数をDXAの業務比率に読み替えない。
- [全URL索引](kpmg.md)

## アクセンチュア

- 起点：[日本語トップ](https://www.accenture.com/jp-ja)
- 中心となる入口：[AI＆データ](https://www.accenture.com/jp-ja/services/ai-data)。個別サービス、導入事例、インサイト、PDFへ分岐する。トップから直接リンクされた[日本公式ニュースルーム](https://newsroom.accenture.jp/)も同社サイトとして含める。
- 技術・設計を知る枝：[インテリジェントエンタープライズを支えるAIアーキテクチャ](https://www.accenture.com/jp-ja/insights/ai-data/intelligent-digital-brain)、[AI Refinery](https://www.accenture.com/jp-ja/services/ai-data/ai-refinery)、AIエージェントやクラウド・データ基盤の解説。
- さらに技術資料へ進む入口：[AI Refinery SDKの概要](https://sdk.airefinery.accenture.com/ai_refinery_101/)は同社公式サブドメインにあり、エージェント機能・APIからモデルカタログや実装ガイドへつながる。概要は取得済みだが、今回の探索範囲の先にある下層は `unconfirmed.csv` に残っている。実装を深く知りたい回は、ここから追加で読む。
- 顧客への適用を知る枝：[消防安全点検へのAI・分析活用](https://www.accenture.com/jp-ja/case-studies/ai-data/singapore-civil-defence-redefines-fire-safety-regulation)、[ŠkodaのAI顧客対応](https://www.accenture.com/jp-ja/case-studies/ai-data/skoda-scales-global-customer-care-through-ai-innovation)。企業名・業務単位で導入の文脈を調べる。
- 構造上の特徴：サービス、顧客事例、技術・経営インサイト、公式ブログ・ニュースが相互に連結する。地域別URLや新旧パスが多いため、URL数と同一内容をまとめた参考値の差を確認する。
- 選考での使い方：AIアーキテクチャの記事を、特定の顧客事例のデータ・業務・運用要件に当てはめて考える。既存のAI&データ選考で聞いた職務説明と照合する。
- [全URL索引](accenture.md)

## 後続チャットの使い方

1. `inventory.jsonl` または各社Markdownを `rg` でテーマ検索する。例：`RAG`、`アーキテクチャ`、`医療`、`AIエージェント`、`ガバナンス`。
2. `topics` と `category` で近い資料を選ぶ。`parent_url` と `routes.csv` から入口・関連資料への経路を復元できる。
3. 説明やESに使う前に、選んだ原ページを開き、本文・日付・執筆法人・事例の実施段階を確認する。この索引は見出し・概要の把握と探索経路の記録であり、全記事の精読・暗記を意味しない。
4. 未取得URLは `unconfirmed.csv` を参照する。未取得のリンクタイトルだけを根拠に企業の実績や仕事内容を断定しない。
5. 今回の発信量比較はグループ公式サイト全体の指標。職種別の技術力、採用難易度、希望部署への配属、年収の評価とは別の調査として使う。
