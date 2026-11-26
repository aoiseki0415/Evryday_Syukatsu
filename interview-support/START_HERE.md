# 新しいWorkチャットの入口

更新：2026-11-26。支援は①全体を解く能力と②本人への提示・適応に分かれる。両方の現行情報を引き継ぐ。準備未完了を準備済みとしない。

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
5. ②は原則①の十分な精度を確認してから。最新の本人指示でフェルミ②は開始済み、ケース②は未開始。support側のCURRENT→CORE→INDEXと必要な詳細、①の現行情報を読む。単独フェルミは[全体の順序](modes/fermi/support/details/workflow.md)→[準備](modes/fermi/support/details/preparation.md)→お題を待つ→[初回共有](modes/fermi/support/details/initial-response.md)。①精度認定と②開始を混同しない。
6. 本番支援は[ready](ready/README.md)に従い、①②、共通知識、探索経路の現行本文を読み込む。未策定・未評価なら状態を短く伝え、準備完了と装わない。

## 本番の対応方針

お題は文字またはスクショ。条件・数値・単位・制約を把握し、必要な根拠を使って回答全体を構築・確認したうえで、初手として必要な部分だけを素早く認識できる形で伝える。①の分析を初手で止めない。

以後の本人の未共有の思考過程は捏造しない。ケースは共有された現在地を優先するという既存方針を維持する。フェルミの初回後の唐突な質問への具体的対応は、今後の議論事項であり今回の仕様化範囲外。

## 現在地

①の主要演習先は[CaseMatchとケース面接ジム](shared/materials/README.md)、同等に活用する。最新の実施範囲と再開点は[CYCLES](learning/CYCLES.md)、精度と未達は[READINESS](learning/READINESS.md)を読む。特定サイクルの途中状態をこの入口へ複製しない。フェルミ②は開始/合意仕様あり、ケース②は開始前。①全体精度・10秒達成・実新規Work起動は未認定。アプリは作らない。

情報の充足確認は[情報監査](learning/audits/2026-11-26-information-audit.md)も参照。採用済み本文に加え、お題に必要な候補の条件/証拠/未評価も確認する。候補を利用しても採用済みへ昇格したことにはしない。
