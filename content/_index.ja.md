---
archetype: "home"
title: "Weasis: DICOMビューア"
description: "医用画像のための無料・オープンソース DICOM ビューア — Windows / macOS / Linux のネイティブアプリケーションとして、または任意の Web ポータルから起動できます。PACS、DICOMweb、MPR、3D、AI 対応。"
keywords: [ "DICOMビューア", "DICOM ビューア", "DICOMビューワー", "オープンソース DICOM ビューア", "無料 DICOM ビューア", "weasis", "DICOM 表示", "医用画像", "PACS", "放射線科", "dicom viewer" ]
aliases:
  - /dicom-viewer-japanese/
  - /dicom-ビューア/
---

## <center>医用画像のためのオープンソースビューア</center>

**Weasis** は、多機能でオープンソースの DICOM ビューアであり、**ネイティブアプリケーション**としても、**Web から**も利用できます。日常的な読影から AI 支援によるレビュー、定量的画像解析まで、病院・多施設臨床試験・患者向けポータルにおける PACS、VNA、DICOM ワークフローへのシームレスな統合を念頭に設計されています。

<p style="text-align:center;">
{{% button href="/en/getting-started/download-dicom-viewer" style="primary" icon="download" %}}Weasis をダウンロード{{% /button %}}
{{% button href="/en/demo" style="green" icon="play" %}}ライブサンプルを試す{{% /button %}}
{{% button href="/en/tutorials" style="secondary" icon="book" %}}チュートリアルを読む{{% /button %}}
</p>

{{% notice note %}}
このトップページは日本語でご覧いただけます。**それ以外のドキュメントは現時点では英語のみ**となっており、以下のリンクは英語ページに移動します。
{{% /notice %}}

### ドキュメントを探す

<style>
.nav-pills{display:flex;flex-wrap:wrap;gap:0.4em;margin-top:0.6em;}
.nav-pill{
  display:inline-flex;align-items:center;gap:0.35em;
  padding:0.35em 0.85em;
  border:1px solid var(--SECONDARY-color, #0d6efd);
  color:var(--SECONDARY-color, #0d6efd);
  background:transparent;
  border-radius:1em;
  text-decoration:none;
  font-weight:600;font-size:0.9em;line-height:1.2;
  transition:background-color .15s ease, color .15s ease, border-color .15s ease, box-shadow .15s ease, transform .1s ease;
}
.nav-pill:hover{
  background:var(--SECONDARY-color, #0d6efd);
  color:#fff;
  text-decoration:none;
  box-shadow:0 2px 6px rgba(0,0,0,.15);
}
.nav-pill:focus-visible{
  outline:2px solid var(--SECONDARY-HOVER-color, #0a58ca);
  outline-offset:2px;
}
.nav-pill:active{
  background:var(--SECONDARY-HOVER-color, #0a58ca);
  border-color:var(--SECONDARY-HOVER-color, #0a58ca);
  color:#fff;
  transform:translateY(1px);
  box-shadow:none;
}
</style>

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:1rem;margin:1rem 0;">
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">🩺 臨床医・エンドユーザー</h4>
    <p style="flex:1;">検査を開き、2D / MPR / 3D ビューアを操作し、計測・注釈・所見の共有を行う。</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/tutorials">チュートリアル</a>
      <a class="nav-pill" href="/en/basics/shortcuts">ショートカット</a>
      <a class="nav-pill" href="/en/faq">FAQ</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">🛠 インテグレーター・管理者</h4>
    <p style="flex:1;">Weasis を PACS、DICOMweb エンドポイント、EHR / RIS / HIS ポータルに接続する。</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/basics/customize/integration">連携</a>
      <a class="nav-pill" href="/en/getting-started/dcm4chee">dcm4chee</a>
      <a class="nav-pill" href="/en/viewer-hub">ViewerHub</a>
      <a class="nav-pill" href="/en/basics/customize/preferences">設定</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">💻 開発者・コントリビューター</h4>
    <p style="flex:1;">プラグインの開発、アーキテクチャの拡張、コード・翻訳・ドキュメントへの貢献。</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/getting-started/#developer-documentation">開発者ドキュメント</a>
      <a class="nav-pill" href="/en/basics/architecture">アーキテクチャ</a>
      <a class="nav-pill" href="/en/basics/customize/build-plugins">プラグイン</a>
    </div>
  </div>
</div>

### なぜ Weasis か

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1rem;margin:1rem 0;">
  <div style="border-left:4px solid #0d6efd;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">臨床読影向けに設計</h4>
    一般的なすべての DICOM 検査をサポート — CT、MRI、超音波、X 線、マンモグラフィ、PET、ECG、構造化レポート、セグメンテーション、放射線治療計画。マルチモニター、HiDPI、MPR、3D、アノテーションツール一式。
  </div>
  <div style="border-left:4px solid #198754;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">あなたの環境になじむ</h4>
    病院の PACS や Web アーカイブに接続し、任意の臨床ポータルからワンクリックで起動。ローカルフォルダ、USB ドライブ、DICOM CD のファイルも読み込めます。オフラインでも動作します。
  </div>
  <div style="border-left:4px solid #6c757d;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">信頼性、無料、オープン</h4>
    <a href="https://github.com/nroduit/Weasis/blob/master/LICENSE">EPL 2.0 / Apache 2.0</a> ライセンス、<a href="https://github.com/nroduit/Weasis">GitHub</a> でソース公開 — ベンダーロックインなし。<a href="https://www.hug.ch/en">HUG</a> をはじめ世界中の病院・臨床試験・ポータルで本番稼働中 — オープン画像ビューアの<a href="/en/stories">ジュネーブ系譜</a>の継承者です。
  </div>
</div>

[機能一覧を見る →](/en/features) · [事例を読む →](/en/stories)

### 見た目はシンプル、中身は奥深く

- **[3D](/en/tutorials/dicom-3d-viewer) & [MPR](/en/tutorials/mpr)** — ボリュームレンダリング、斜断面再構成、[同期ビュー](/en/tutorials/synch-view)、[MIP](/en/tutorials/mip) スラブ。
- **広範な DICOM 対応** — CT、MRI、US、X 線、PET、[SR](/en/tutorials/dicom-sr)、[ECG](/en/tutorials/dicom-ecg)、[音声](/en/tutorials/dicom-audio)、4D、マルチフレーム。
- **DICOM [SEG](/en/tutorials/dicom-segmentation) & [RT](/en/tutorials/dicom-rt)** — 2D / MPR / 3D での重ね合わせ、RTSTRUCT、RTDOSE 等線量、DVH。
- **[AI 対応オブジェクト](/en/tutorials/dicom-artificial-intelligence)** — 二次キャプチャ、パラメトリックマップ、GSPS、SR、セグメンテーション。
- **[計測](/en/tutorials/draw-measure)** — [校正済み](/en/tutorials/calibration)の距離、角度、ROI 統計、[ヒストグラム](/en/tutorials/histogram)；[KO / PR](/en/tutorials/build-ko-pr) として保存可能。
- **[PACS & Web 連携](/en/basics/customize/integration)** — [DICOMweb](/en/tutorials/dicomweb-config)、DIMSE Q/R、[`weasis://`](/en/getting-started/weasis-protocol) によるポータル起動。
- **ワークフローの使いやすさ** — マルチモニター、HiDPI、[ドッキング](/en/tutorials/docking)、[ショートカット](/en/basics/shortcuts)、[テーマ](/en/tutorials/theme)、[ロケール](/en/tutorials/locale)。

{{< youtube id="ywaBAt2SqxM" title="Weasis DICOM viewer — overview" >}}
<br>

### コミュニティとサポート

- **質問** — [GitHub Discussions](https://github.com/nroduit/Weasis/discussions) · [dcm4che フォーラム](https://groups.google.com/group/dcm4che) · [FAQ](/en/faq)
- **バグ報告・機能要望** — [GitHub Issues](https://github.com/nroduit/Weasis/issues)（[バグ報告の書き方](/en/faq#how-do-i-report-a-bug)を参照）
- **参加・貢献** — [コード、翻訳、ドキュメント、事例の貢献](/en/get-involved)
- **出版物での Weasis 引用** — [引用形式](/en/faq#how-to-cite-weasis-in-a-publication)