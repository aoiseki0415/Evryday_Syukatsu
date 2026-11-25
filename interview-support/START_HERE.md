# 新しいWorkチャットの入口

更新：2026-11-25。支援は①全体を解く能力と②本人への提示・適応に分かれる。両方の現行情報を引き継ぐ。準備未完了を準備済みとしない。

## 開始時

1. 親AGENTSに従いGitルート・branch・origin・作業状態を確認し、git pull --ff-only origin main。取得できなければ最新と断定しない。
2. [SPEC](SPEC.md)、[OPERATIONS](OPERATIONS.md)、[ROADMAP](ROADMAP.md)、[READINESS](learning/READINESS.md)で目的・境界・現在の段階を読む。
3. 依頼から、ケース/単独フェルミ、①の学習/②の調整/本番支援/環境整理を判別する。明確な依頼を承認の質問で聞き直さない。

| 依頼・出題 | 進む先 |
| --- | --- |
| ケース面接（内部で推定が必要でも同じ） | [case/PLAYBOOK](modes/case/PLAYBOOK.md) |
| 推定そのものが単独出題 | [fermi/PLAYBOOK](modes/fermi/PLAYBOOK.md) |
| 情報と学習の整理・教材受領 | [INFORMATION_MAP](INFORMATION_MAP.md)、shared/materials、対象領域INPUT |

4. ①の学習では[SOLVE_WORKFLOW](learning/SOLVE_WORKFLOW.md) → [COVERAGE](learning/COVERAGE.md) → [CYCLESの再開点](learning/CYCLES.md)を読み、対象solveのINPUT・LEARNING、CURRENT→CORE→INDEXと必要な詳細を確認する。本人に正誤の判定を求めず、教材の解答・解説を評価根拠にする。使用知識のID・版・実適用箇所を演習記録に残し、inputと演習を繰り返す。
5. ②の学習は①の十分な精度を確認してから。support側のCURRENT→CORE→INDEXと必要な詳細、①の現行情報を読む。②では本人のフィードバックを使う。
6. 本番支援は[ready](ready/README.md)に従い、①②、共通知識、探索経路の現行本文を読み込む。未策定・未評価なら状態を短く伝え、準備完了と装わない。

## 本番の対応方針

お題は文字またはスクショ。条件・数値・単位・制約を把握し、必要な根拠を使って回答全体を構築・確認したうえで、初手として必要な部分だけを素早く認識できる形で伝える。①の分析を初手で止めない。

以後は本人の依頼を受け、共有された現在地と変更条件を優先する。未共有の思考過程を捏造せず、不可欠な不足だけ確認する。真因だけを伝えられた施策依頼等でも、最初の筋道へ戻すことを目的にしない。

## 現在地

①の主要演習先は[CaseMatchとケース面接ジム](shared/materials/README.md)、同等に活用する。ケース・フェルミ各1問の試行と各B候補1件、CaseMatch記事の初期確認を保存。網羅的input・継続的な精度確認は未完了。②は開始前、本番準備未完了。次はROADMAPに従い、試行だけで高精度としない。アプリは作らない。
