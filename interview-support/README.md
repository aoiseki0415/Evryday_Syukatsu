# ケース面接・フェルミ推定｜リアルタイム支援

開始・更新：2026-11-25。目的・2モードと共通基盤・記録と学習の運用を確定。解法の収集、演習、具体的な支援手順は未着手。

## 目的

**このプロジェクトの新しいWorkチャットで「ケース面接サポート」「フェルミ推定サポート」と伝えれば、Codexが現行文書と学習記録を読み、定めた手順で対話支援できる仕組みを作る。** アプリケーション開発は目的ではない。

中心は資料のinputだけでなく、問題への取り組み、回答例・本人のフィードバックとの照合や共同検討、改善の記録と次回への反映を通じて支援精度を高めること。

## 最初に読む

[START_HERE](START_HERE.md) → [SPEC](SPEC.md) → [OPERATIONS](OPERATIONS.md) → モード別の手順 → [採用済みの学び](learning/CURRENT.md)。本領域の作業規則は[AGENTS](AGENTS.md)。

| 依頼 | モード | フェルミ推定との関係 |
| --- | --- | --- |
| ケース面接を手伝ってほしい | [ケース面接](modes/case/PLAYBOOK.md) | 必要な推定を内部で使い、ケースモードを維持 |
| フェルミ推定を手伝ってほしい | [単独フェルミ推定](modes/fermi/PLAYBOOK.md) | 推定そのものが単独出題されるときのみ |

両者は完全独立ではない。解法・前提知識・探索経路・学びは適用範囲を明記し[共通基盤](shared/README.md)でつなぐ。

Notionの対応ページ：[ケース面接](https://app.notion.com/p/423161f280978186882eeb3b8d463ceb)／[単独フェルミ推定](https://app.notion.com/p/423161f28097813880b7e95b2a016062)／[共通運用・記録](https://app.notion.com/p/423161f2809781a285def6c74f0cd315)／[学習・知識更新](https://app.notion.com/p/423161f28097815fa33ef64eba128381)。

## 保存先と編集境界

- GitHub：既存repoの **interview-support/ と配下のみ**。Codex用に仕様、根拠、判断理由、試行・修正、実践と学習履歴を詳細に記録する。
- Notion：[専用ホーム](https://app.notion.com/p/423161f2809781ff9677d9f3c6a9e488)と子孫のみ。本人向けに最新の確定事項、重要なエッセンスと構造を端的に可視化する。
- 配下の拡張は可。関連資料の参照は、その資料を編集する権限ではない。親README・HANDOFF・logsや他のNotionページをついでに変更しない。初回の親文書へも追記する運用は、後続の領域限定指示で変更した。

## 構造

```text
interview-support/
├── AGENTS.md / START_HERE.md   作業規則・新チャットの入口
├── SPEC.md / OPERATIONS.md    現行の全体像・共通運用
├── modes/
│   ├── case/PLAYBOOK.md       ケース面接サポート
│   └── fermi/PLAYBOOK.md      単独フェルミ推定サポート
├── shared/
│   ├── knowledge/            解法・前提知識・施策例
│   └── research/             必要時に調べる探索経路
├── sessions/                 問題・支援・フィードバックの実記録
├── learning/                 採用済みの学びと改善の検証履歴
├── logs/                     議論・決定理由・操作の履歴
├── archive/                  旧版・失効情報への入口
└── assets/                   Notion用の構造図など
```

現行情報はSPEC・OPERATIONS・PLAYBOOK・learning/CURRENT、議論はlogs、実践はsessions、検証の経緯はlearningの日付付き記録、旧版はarchiveとGitの固定コミット。詳細は[運用](OPERATIONS.md)。

## 現在地と再開

親AGENTSのGit対象・状態確認とpullを行い、既存の親README/HANDOFFからこの領域へ到達したらSTART_HEREに従う。サポートの毎返信で全資料を再読せず、開始時に現行版を確認し変更時に再読する。

今回は全体構造と運用の整備まで。情報収集、会員サイト利用、知識のinput、問題演習はまだ実施しない。具体的な解法・対話手順・回答形式・評価基準も今後策定する。過去のGD・ケース資料を自動的に現行仕様へ採用しない。

GitHubは公開設定。認証情報、私的な連絡、非公開の問題・解説の全文等を保存せず、参照先と公開可能な要約を置く。
