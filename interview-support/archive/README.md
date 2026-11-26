# 過去情報・旧版への入口

過去と現在を混ぜない。旧記録は当時の事実として保持し現行正本へ誘導する。Gitで取得できる旧版を全文複製する必要はない。

| 旧情報 | 当時の範囲 | 現在の参照先 |
| --- | --- | --- |
| [保存場所を用意した時点の文書（d07a318）](https://github.com/aoiseki0415/Evryday_Syukatsu/tree/d07a3186b43c944d976d0c26d398d05f4595e39e/interview-support) | 保存先と役割のみ確定。全体像は未決定 | [SPEC](../SPEC.md)、[OPERATIONS](../OPERATIONS.md) |
| [11/25保存先ログ](../logs/2026-11-25-storage-and-roles.md) | 初回の配置判断と操作 | [後続の方針ログ](../logs/2026-11-25-project-direction.md) |
| [B011/012候補v1の固定本文](2026-11-26-diagnosis-constraints-v1.txt) | CM-C015/016が事前実読した同居ファイル。元SHA `a35a470e7e961abe5a8f32907b55b3f496eb8be6e58d4fc290be9d14278499b3` と一致する保存内容。旧本文中の相対参照は当時の `modes/case/solve/details/` を基準に読む | [現在の診断/制約](../modes/case/solve/details/diagnosis-constraints.md)：B011候補v2/B012候補v1。旧版を現行として採用しない |
| [B013・6カード候補v1](https://github.com/aoiseki0415/Evryday_Syukatsu/blob/2ffa58f26bc43e9d289dfcd682596a2a1babe63c/interview-support/modes/case/solve/details/business-structures.md) | CM-C015が事前使用。元SHA `acdf568ef8a09450b55533221a81de6e67d1abbd4a897633792ab20494d7794b` | [現在の7カード候補v2](../modes/case/solve/details/business-structures.md) |
| [Fermi FACT001〜004・情報v1](https://github.com/aoiseki0415/Evryday_Syukatsu/blob/2ffa58f26bc43e9d289dfcd682596a2a1babe63c/interview-support/modes/fermi/solve/details/rough-anchors.md) | GYM028/CM-F010が事前使用した4カード同居本文。SHA `941589e039d8c2c4f5642aa8482ba6ee2aed59d7da1b0c27cba34be2be5f57ee` | [現在のラフ値](../modes/fermi/solve/details/rough-anchors.md)。001/002は情報v1、003/004は情報v2 |
| [Fermiの事前使用v2固定本文](2026-11-26-fermi-anchors-v2-used.txt) | GYM029/CM-F011の事前使用本文。SHA `2233c85037fcf23bc15032227841e3e89ff68e3beb39c5770560e24d6fab1400`と一致。旧本文中の相対参照は当時の`modes/fermi/solve/details/`基準 | 現行本文の後続の証拠追記と、演習前の使用内容を区別。情報版が同じでも本文hashで追跡する |

初回文書の親HANDOFF・親logsへの追記方針は、後続の本人指示で本領域だけの記録へ変更された。過去の操作記録は書き換えず現行運用で境界を示す。

## 4領域と優先度の導入前

[4ae7574時点の文書](https://github.com/aoiseki0415/Evryday_Syukatsu/tree/4ae75749989c0b195ec959027ef112f06c788894/interview-support)は2モードと共通学習の初版。①②の評価主体と優先度別の文書構造は後続の指示で具体化された。現行はSPEC・DOCUMENTATION・ROADMAPを読む。①の正誤を本人へ依頼する旧記述は現在の方針として使わない。
