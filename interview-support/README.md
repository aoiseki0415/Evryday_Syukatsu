# ケース面接・フェルミ推定｜対話支援の基盤

更新：2026-11-25。SOLVE-CYCLE-001で両①の広い初期inputを保存し、CaseMatch文字AIとケース面接ジムの演習・照合・再inputを進行中。現在の記録と残る穴はlearning/CYCLES・COVERAGE、精度はREADINESSから確認する。②は未開始、本番準備未完了。

## 目的と進め方

新しいWorkチャットで支援を依頼すると、Codexが文書と学習成果を読み込み、準備後に対話支援する。アプリ開発は目的に含めない。

**①お題への回答全体を正確に導く → 十分な精度を教材で確認 → ②その一部を、本人に素早く認識できる形で提示する方法を調整。** 最初に示すのがきっかけだけでも、Codexの分析対象は回答全体。

| | ① solve：問題集・解答・解説で学習 | ② support：①を土台に本人の評価で調整 |
| --- | --- | --- |
| ケース | [解法・知識・全体回答](modes/case/solve/README.md) | [初手・途中依頼への支援](modes/case/support/README.md) |
| 単独フェルミ | [解法・概数・全体回答](modes/fermi/solve/README.md) | [式・仮定・結果の提示と追加支援](modes/fermi/support/README.md) |

ケース内で推定が必要ならケースモードのまま。単独フェルミモードは推定そのものが単独出題される場合のみ。共通知識は参照で共有する。

## 入口

- [START_HERE](START_HERE.md)：新チャットで読む順・モードと目的の判別。
- [SPEC](SPEC.md)：現行の全体仕様。
- [INFORMATION_MAP](INFORMATION_MAP.md)：4領域それぞれに保管する情報。
- [DOCUMENTATION](DOCUMENTATION.md)：A/B/C、重要要約・全情報索引・種類別本文・議論履歴の役割。
- [ROADMAP](ROADMAP.md)：これから行うことと現在地。
- [OPERATIONS](OPERATIONS.md)：編集境界・記録・更新の運用。
- [NOTION_INDEX](NOTION_INDEX.md)：4領域と目的別文書のNotion保存先。
- [精度と移行条件](learning/READINESS.md)／[準備セット](ready/README.md)。
- [①の反復学習手順](learning/SOLVE_WORKFLOW.md)／[調査・問題種類の範囲](learning/COVERAGE.md)／[サイクルと再開点](learning/CYCLES.md)。

## 保存構造

```text
interview-support/
├── AGENTS.md / START_HERE.md
├── SPEC.md / INFORMATION_MAP.md / ROADMAP.md / OPERATIONS.md
├── modes/
│   ├── case/
│   │   ├── PLAYBOOK.md
│   │   ├── solve/    ①のINPUT・LEARNING、CORE・INDEX・details・HISTORY
│   │   └── support/  ②のINPUT・LEARNING、CORE・INDEX・details・HISTORY
│   └── fermi/        caseと同じ情報・学習文書の構造
├── shared/
│   ├── materials/   問題集・解答・解説の共通台帳
│   ├── knowledge/   共通知識・ラフな値・施策・出典
│   └── research/    必要時に素早く調べる探索経路
├── learning/        4領域索引・①実行手順/カバレッジ/サイクル・精度/移行状態
├── templates/       情報項目・資料比較・演習・サイクル・変更の記録ひな形
├── sessions/        ②や本番の対話記録
├── ready/           次のチャットが読む準備セット
├── logs/            議論・決定理由・操作の履歴
├── archive/         旧版への入口
└── assets/          Notion用の構造図
```

各領域のINPUTは資料の索引、実資料ノートは受領後にinput/へ。LEARNINGは学習方法と索引、実績は実施後にlearning/へ。CURRENTは現行文書への入口。採用済みAはCORE、全項目はINDEX、本文はdetails、議論と変更はHISTORYから履歴へ。空の実績・教材を作らず、未登録・未評価を明記する。

## Notionと編集境界

[Notionホーム](https://app.notion.com/p/423161f2809781ff9677d9f3c6a9e488)は本人向けの最新の要点と構造を可視化する入口。GitHubはCodex向けの詳細な正本。

編集はこのフォルダとNotionホームの配下のみ。階層追加は可。親README・HANDOFF・logsや他のNotionページをついでに変更しない。既存の親文書のリンクから本READMEへ到達し、START_HEREへ進む。公開GitHubには認証情報、私的な連絡、非公開の問題・解説の全文を保存しない。

次は網羅的inputと①の継続演習。[主要演習先と資料](shared/materials/README.md)に従い、CaseMatchの講評とケース面接ジムの解答例による自己比較を同等に活用する。音声AI面接は①では使わず、②で本人が解きながら支援を試す候補とする。
