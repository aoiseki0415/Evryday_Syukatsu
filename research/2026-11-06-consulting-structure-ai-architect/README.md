# コンサルの4概念と、AIアーキテクトの現在地

記録日：2026年11月6日（日本時間）。11/5後半から本チャットで進めた概念整理、AIに限定した調査、表示方法の修正を統合した。**合意した比較方法／本人の志向／Codexの暫定評価／一次情報／未決定**を区別する。

## 最初に読むもの

| 知りたいこと | 正本・参照先 |
| --- | --- |
| 現在の就活方針と二本のルート | [STRATEGY.md](../../STRATEGY.md) |
| 最新の理想企業像と次の探索フレームワーク | [ideal-company-framework.md](ideal-company-framework.md)、[JSON](ideal-company-framework.json) |
| AI普及後の支援内容についての議論の種（未確定） | [future-consulting-discussion-seed.md](future-consulting-discussion-seed.md) |
| 4概念の定義・関係 | [framework.md](framework.md) |
| AIに絞った問いA・Bの結論と限界 | [ai-current-state.md](ai-current-state.md) |
| 確認した記事・案件・提供体制 | [evidence.md](evidence.md)、[evidence.json](evidence.json) |
| 議論・修正が進んだ順序 | [process.md](process.md)、[操作ログ](../../logs/2026-11-06-consulting-structure-ai-architect.md) |
| 図のセルと意味を再利用 | [framework.json](framework.json)（一般図）、[comparison.json](comparison.json)（AI限定） |
| 今回の確認結果 | [verification.json](verification.json) |

## 人が見るNotion

- [コンサルの構造化](https://app.notion.com/p/40f161f280978009a9a0f7ba92ea2381)：上部は一般構造、下部「AIアーキテクト（支援領域：AI・データ）に絞った議論」はA・Bのマトリックス。
- [問いAの調査根拠](https://app.notion.com/p/40f161f2809781baa997d046afb8e9f8)：関与の範囲・程度、評価観点、具体的根拠と留保。
- [問いBの調査根拠](https://app.notion.com/p/40f161f280978163a7f2fb1845065074)：対象範囲、トレンド、国内10・海外4の事例。

表面は図、実情報・理由は下位ページ。Aは関与の程度を**同じ色の4段階の濃淡**で表し、Bは支援対象の確認状況を**丸・三角**で表す。記号の意味を混ぜない。

## この記録で確定したこと／していないこと

- **合意**：対象範囲・支援領域・企業カテゴリー・支援工程の4概念。Aは範囲と程度を別の評価軸とし、工程の着色範囲と色の濃さで同時表示する。
- **本人の志向（最新追補）**：①構想・方針策定に軸足を置き、技術理解を深めるため②〜④、特に③④にも関与したい。構想と実装がつながる環境から、本人が両方へ関われる可能性を間接的に考える。Bは全社変革の具体的な案件・事例から評価。個人の担当保証をこの段階の必須条件にはしない。
- **暫定**：カテゴリー別の各セルの評価はCodexの所感。4段階の尺度を使うことと、各値を本人が企業評価として確定したことは別。
- **調査**：14事例・12サービス等・3市場資料を保存。存在・提供範囲と、案件の頻度を分ける。
- **未決定・未実施**：具体企業の探索・適合確認、個人の担当と配属、関与の細かな程度・配分、将来の需要仮説、企業・職種の追加や志望順位。理想の企業像は上の追補として具体化した。
- **継続条件**：AI側の候補探索はSIer除外、総合はBig4＋Accenture、日本の28卒・大学院生向け新卒入口必須、DSは加点。市場比較のSIer・海外事例は応募候補の復活を意味しない。
- 前の[52候補](../2026-11-05-ai-architect-shortlist/README.md)と共有シートは旧条件の履歴。今回は未編集。新条件で企業×職種を選び直す調査・募集再確認はしていない。

## 表示資産

[理想の企業像の図解](assets/ideal-company-framework.png)と[描画スクリプト](assets/render_ideal_company_framework.py)も保存。

[図A：工程と関与の程度](assets/ai-process-involvement.png)、[図B：対象範囲](assets/ai-scope-coverage.png)を保存。[Aの描画スクリプト](assets/render_ai_process.py)はPillowを使用し、macOSのヒラギノフォントを参照する。Notionの画像を再生成する場合は、先にcomparison.jsonの意味と暫定性を確認する。
