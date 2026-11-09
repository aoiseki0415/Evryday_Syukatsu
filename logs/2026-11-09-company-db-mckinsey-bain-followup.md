# 企業DB更新の相談とMcKinsey・Bain募集確認

確認日：2026年11月9日（JST）。[Notion「コンサル」企業DB](https://app.notion.com/p/32d161f28097806e868de3a30cc28441)と両社の公式採用情報を読み直した。先行する調査時点ではNotionを変更せず、後続の本人指示により同日、下記の対象行を更新した。

## 本人の希望と表の現状

- AI導入支援で注目した企業を企業DBに反映したい。既存の会社は重複追加しない。McKinseyとBCGは一般ビジネスコンサルではなく専門職への応募を想定。ADLとグロービングも候補に挙げた。具体的な志望度の段階は今回まだ指定していない。
- DBには「企業名」「志望度」「志望するコース」があり、独立した「職種」列はない。更新前のSQLで確認した既存行はMcKinsey、BCG、Bainがいずれもレベル1、希望コース空欄。ADLとグロービングは企業名の表記ゆれも含め検索した範囲で見当たらなかった。この時点のDB値は[AI導入支援06の暫定評価](https://app.notion.com/p/410161f280978090a555d5f5eb53fd70)へ連動していなかった。
- この時点では会社の新規追加、既存行の評価変更、希望コースの記入を保留した。後続指示で対象とレベルが確定し、下記の更新を実施した。

## McKinsey：BA - Tech & AI 113784

[東京・大阪の公式求人](https://www.mckinsey.com/careers/search-jobs/jobs/businessanalyst-techai-113784)は、英語で「Up-to 3 years of professional experience」、日本語で対象業界における「3年未満の実務経験」と記載する。**3年以上の経験を要求する文ではない**。ただし「経験なし」の在学生がこの個別求人の応募資格を満たすか、研究・インターン経験をどう扱うかは明記されていない。専門職の求人は存在するが、国内28卒専用求人、入社時期、締切の表記もない。

[日本28卒一般BA要項](https://www.mckinsey.com/jp/careers/careers-in-japan/application-process-for-undergrads-2028)は夏5月31日・冬9月15日が締切済みで、一般BAへのリンクを掲示する。この日程を個別Tech & AI求人へ転用しない。[日本Digital採用ページ](https://www.mckinsey.com/jp/careers/role-descriptions/careers-in-digital)には新卒応募FAQがあり、同日先行の確認では新卒制度自体は存在すると読めたが、113784の未経験28卒資格を証明しない。

結論：**「実務経験が3年未満だから無理」は誤読の可能性がある一方、実務経験ゼロで113784へ応募できるとも未確認**。本人が専門職に絞るなら、募集側への資格確認または応募画面の卒年・経験要件確認が必要。一般BAへ応募する判断と混同しない。

## Bain：国内28卒の冬インターン後

[東京オフィスの国内28卒公式ページ](https://www.bain.com/ja/careers/hiring-process/tokyo/domestic-undergrad/)は、国内在学生向け冬インターンの応募期限を2026年10月7日13時とする。掲載する選考フローは**書類→適性検査→面接→インターン→本採用面接→内定**。したがって「本採用面接」はこれからインターン参加者に対して行う段階であり、締切後の別の一般応募回を意味しない。28卒向け独立した本選考・追加公募の日程は、公開公式ページでは確認できない。

[東京オフィス募集要項](https://www.bain.com/ja/careers/hiring-process/tokyo/)も国内新卒と海外新卒・MBA・中途を分ける。国内ページのボストンキャリアフォーラム選考は、その時期に国外にいる交換留学生等向けのフルタイム選考であり、国内在学生の代替入口にしない。過年度の[27卒冬インターン公式PDF](https://www.bain.com/contentassets/b6223c7dc0324659ae23e807cc90594f/class-of-2027-winter-internship-program.pdf)も同種の冬募集を示すが、28卒の追加公募が将来ないことまでは証明しない。

結論：**現時点で国内28卒の新規応募可能な別本選考は確認できない**。追加回の有無は未発表・未確認であり、「28卒採用が完全終了」とも断定しない。MyPage内の案内は未確認。

## 後続指示とNotion反映

本人はMcKinsey Tech & AIを候補に残し、BCG XのData Scientist／AI Engineerは二択のまま、ADL・グロービングを加えた4社を**レベル5**に指定。NRI・NTTデータ・IBMは**レベル4**へ下げるよう指定した。06の比較内容、インターン/本選考の進捗、マイページ情報は変更しない。Bainは「無理そうかも」との所感で、DB変更の対象指定はなかった。

| 対象 | 操作 | 志望するコースの記入 |
| --- | --- | --- |
| [McKinsey](https://app.notion.com/p/332161f280978052857cf7d62072cf10) | 既存レベル1→5 | Business Analyst – Tech & AI |
| [BCG](https://app.notion.com/p/331161f2809780d2a529c85a4e2b4edb) | 既存レベル1→5 | BCG X：Data Scientist／AI Engineer（選択検討中） |
| [ADL](https://app.notion.com/p/413161f2809781b0a708f30345f50e63) | 新規、レベル5、種類「戦略」 | 東京オフィス新卒採用（AI・デジタル領域志望） |
| [グロービング](https://app.notion.com/p/413161f280978144a5f4e9e06243aca3) | 新規、レベル5、種類「戦略」 | 国内新卒：戦略コンサルタント／AIコンサルタント・デジタルコンサルタント（選択検討中） |
| [NRI](https://app.notion.com/p/331161f2809780e48c72f3f43e1d8156)、[NTTデータ](https://app.notion.com/p/3c6161f280978067b2aecf4c5500646c)、[IBM](https://app.notion.com/p/3a9161f280978096898af6261cc314cd) | 各既存レベル5→4 | 既存値を保持 |

対象7行の企業名・志望度・希望コースを読み戻した。既存更新5行について選考進捗・マイページ情報を更新前後で照合し、一致した。Bainはレベル1のまま。06ページは操作しなかった。追加の全DB集計はNotionのQuery Data Source利用上限に達して実行できなかったが、指定行の読み戻しは完了している。

**根拠と留保**：[McKinsey個別求人](https://www.mckinsey.com/careers/search-jobs/jobs/businessanalyst-techai-113784)、[BCG XのDS](https://careers.bcg.com/jp/ja/job/58408/Data-Scientist-%E6%96%B0%E5%8D%92-New-Graduate-2028-BCG-X-Japan)／[AI Engineer](https://careers.bcg.com/jp/ja/job/59586/AI-Engineer-%E6%96%B0%E5%8D%92-New-Graduate-2028-BCG-X-Japan)、[ADL東京採用](https://www.adlittle.com/jp-ja/apply)、[グロービング国内新卒要項](https://globe-ing-recruit.snar.jp/jobboard/detail.aspx?id=Z5bZ6XgZjSU)。McKinseyの未経験28卒資格は未確認。ADLの28卒夏募集は終了し、冬の正式実施・日程・受付は未確認。「志望するコース」は志向・検討中の選択肢を記し、専門配属の保証ではない。06の時点付き暫定評価は本人の指定で保持し、今回の企業DB評価へ自動同期しない。
