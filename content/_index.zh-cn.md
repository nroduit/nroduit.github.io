---
# These pages deliberately link to the English tutorials, which are the only
# translated content that exists. Hugo cannot resolve "/en/..." as a content
# path (the language is a filename suffix, not a directory), so the link
# checker reports false negatives; the emitted URLs are correct.
urlIgnoreCheck: [ "^/en/" ]
archetype: "home"
title: "Weasis：DICOM 查看器"
description: "面向医学影像的免费开源 DICOM 查看器 —— 可作为 Windows / macOS / Linux 上的原生应用程序运行，也可从任意 Web 门户启动。支持 PACS、DICOMweb、MPR、3D、AI 就绪。"
keywords: [ "DICOM 查看器", "开源 DICOM 查看器", "免费 DICOM 查看器", "DICOM 浏览器", "weasis", "医学影像", "PACS", "放射科", "影像软件", "dicom viewer" ]
aliases:
  - /dicom-chinese/
  - /dicom-查看器/
---

## <center>面向医学影像的开源查看器</center>

**Weasis** 是一款功能丰富的开源 DICOM 查看器，可作为**原生应用程序**使用，也可**从 Web 启动**。从日常阅片到 AI 辅助审阅与定量影像分析，它的设计目标是与医院、多中心临床试验和患者门户中的 PACS、VNA 和 DICOM 工作流无缝集成。

<p style="text-align:center;">
{{% button href="/en/getting-started/download-dicom-viewer" style="primary" icon="download" %}}下载 Weasis{{% /button %}}
{{% button href="/en/demo" style="green" icon="play" %}}试用在线示例{{% /button %}}
{{% button href="/en/tutorials" style="secondary" icon="book" %}}阅读教程{{% /button %}}
</p>

{{% notice note %}}
本主页提供中文版本。**其余文档目前仅有英文版本**，以下链接将跳转到英文页面。
{{% /notice %}}

### 文档导航

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
    <h4 style="margin-top:0;">🩺 临床医生与终端用户</h4>
    <p style="flex:1;">打开检查、操作 2D / MPR / 3D 查看器、测量、注释、共享所见。</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/tutorials">教程</a>
      <a class="nav-pill" href="/en/basics/shortcuts">快捷键</a>
      <a class="nav-pill" href="/en/faq">FAQ</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">🛠 集成商与管理员</h4>
    <p style="flex:1;">将 Weasis 接入 PACS、DICOMweb 端点、EHR / RIS / HIS 门户。</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/basics/customize/integration">集成</a>
      <a class="nav-pill" href="/en/getting-started/dcm4chee">dcm4chee</a>
      <a class="nav-pill" href="/en/viewer-hub">ViewerHub</a>
      <a class="nav-pill" href="/en/basics/customize/preferences">偏好设置</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">💻 开发者与贡献者</h4>
    <p style="flex:1;">开发插件、扩展架构、贡献代码、翻译或文档。</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/getting-started/#developer-documentation">开发者文档</a>
      <a class="nav-pill" href="/en/basics/architecture">架构</a>
      <a class="nav-pill" href="/en/basics/customize/build-plugins">插件</a>
    </div>
  </div>
</div>

### 为什么选择 Weasis

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1rem;margin:1rem 0;">
  <div style="border-left:4px solid #0d6efd;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">为临床阅片而设计</h4>
    支持所有常见 DICOM 检查 —— CT、MR、超声、X 光、乳腺摄影、PET、ECG、结构化报告、分割、放疗计划。多显示器、HiDPI、MPR、3D、完整的标注工具集。
  </div>
  <div style="border-left:4px solid #198754;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">适配您的环境</h4>
    连接到医院的 PACS 或 Web 归档，一键从任意临床门户打开，并可从本地文件夹、U 盘或 DICOM 光盘读取文件。支持离线工作。
  </div>
  <div style="border-left:4px solid #6c757d;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">可信、自由、开放</h4>
    采用 <a href="https://github.com/nroduit/Weasis/blob/master/LICENSE">EPL 2.0 / Apache 2.0</a> 双重许可，源码开放于 <a href="https://github.com/nroduit/Weasis">GitHub</a> —— 无供应商锁定。在 <a href="https://www.hug.ch/en">HUG</a> 等全球各地的医院、试验和门户中投入生产运行 —— 传承自<a href="/en/stories">日内瓦开源影像查看器的血脉</a>。
  </div>
</div>

[查看完整功能列表 →](/en/features) · [阅读案例研究 →](/en/stories)

### 表层简洁，内核强大

- **[3D](/en/tutorials/dicom-3d-viewer) 与 [MPR](/en/tutorials/mpr)** —— 体绘制、斜面重建、[同步视图](/en/tutorials/synch-view)、[MIP](/en/tutorials/mip) 厚层。
- **广泛的 DICOM 支持** —— CT、MR、US、X 光、PET、[SR](/en/tutorials/dicom-sr)、[ECG](/en/tutorials/dicom-ecg)、[音频](/en/tutorials/dicom-audio)、4D、多帧。
- **DICOM [SEG](/en/tutorials/dicom-segmentation) 与 [RT](/en/tutorials/dicom-rt)** —— 在 2D / MPR / 3D 中叠加显示、RTSTRUCT、RTDOSE 等剂量线、DVH。
- **[AI 友好对象](/en/tutorials/dicom-artificial-intelligence)** —— 二次捕获、参数图、GSPS、SR、分割。
- **[测量](/en/tutorials/draw-measure)** —— [校准](/en/tutorials/calibration)的距离、角度、ROI 统计、[直方图](/en/tutorials/histogram)；可保存为 [KO / PR](/en/tutorials/build-ko-pr)。
- **[PACS 与 Web 集成](/en/basics/customize/integration)** —— [DICOMweb](/en/tutorials/dicomweb-config)、DIMSE Q/R、通过 [`weasis://`](/en/getting-started/weasis-protocol) 从门户启动。
- **工作流效率** —— 多显示器、HiDPI、[面板停靠](/en/tutorials/docking)、[快捷键](/en/basics/shortcuts)、[主题](/en/tutorials/theme)、[语言区域](/en/tutorials/locale)。

{{< youtube id="ywaBAt2SqxM" title="Weasis DICOM viewer — overview" >}}
<br>

### 社区与支持

- **问题咨询** —— [GitHub Discussions](https://github.com/nroduit/Weasis/discussions) · [dcm4che 论坛](https://groups.google.com/group/dcm4che) · [FAQ](/en/faq)
- **错误报告与功能请求** —— [GitHub Issues](https://github.com/nroduit/Weasis/issues)（参见[如何提交有效的错误报告](/en/faq#how-do-i-report-a-bug)）
- **参与贡献** —— [贡献代码、翻译、文档或用户故事](/en/get-involved)
- **在出版物中引用 Weasis** —— [引用格式](/en/faq#how-to-cite-weasis-in-a-publication)