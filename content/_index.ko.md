---
archetype: "home"
title: "Weasis: DICOM 뷰어"
description: "의료 영상을 위한 무료 오픈 소스 DICOM 뷰어 — Windows / macOS / Linux 네이티브 애플리케이션으로 실행하거나 어떤 웹 포털에서도 실행할 수 있습니다. PACS, DICOMweb, MPR, 3D, AI 지원."
keywords: [ "DICOM 뷰어", "오픈 소스 DICOM 뷰어", "무료 DICOM 뷰어", "weasis", "DICOM 보기", "의료 영상", "영상의학", "PACS", "방사선과", "dicom viewer" ]
aliases:
  - /dicom-viewer-korean/
  - /dicom-뷰어/
---

## <center>의료 영상을 위한 오픈 소스 뷰어</center>

**Weasis**는 다기능 오픈 소스 DICOM 뷰어로, **네이티브 애플리케이션**과 **웹**에서 모두 실행됩니다. 일상적인 판독부터 AI 보조 검토와 정량적 영상 분석까지 — 병원, 다기관 임상시험, 환자 포털에서의 PACS, VNA, DICOM 워크플로와 자연스럽게 통합되도록 설계되었습니다.

<p style="text-align:center;">
{{% button href="/en/getting-started/download-dicom-viewer" style="primary" icon="download" %}}Weasis 다운로드{{% /button %}}
{{% button href="/en/demo" style="green" icon="play" %}}라이브 샘플 사용해 보기{{% /button %}}
{{% button href="/en/tutorials" style="secondary" icon="book" %}}튜토리얼 읽기{{% /button %}}
</p>

{{% notice note %}}
이 홈페이지는 한국어로 제공됩니다. **나머지 문서는 현재 영어로만 제공**되며, 아래 링크는 영어 페이지로 연결됩니다.
{{% /notice %}}

### 문서 둘러보기

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
    <h4 style="margin-top:0;">🩺 임상의 &amp; 최종 사용자</h4>
    <p style="flex:1;">검사 열기, 2D / MPR / 3D 뷰어 조작, 측정, 주석, 소견 공유.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/tutorials">튜토리얼</a>
      <a class="nav-pill" href="/en/basics/shortcuts">단축키</a>
      <a class="nav-pill" href="/en/faq">FAQ</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">🛠 통합자 &amp; 관리자</h4>
    <p style="flex:1;">Weasis를 PACS, DICOMweb 엔드포인트, EMR / RIS / HIS 포털에 연결.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/basics/customize/integration">통합</a>
      <a class="nav-pill" href="/en/getting-started/dcm4chee">dcm4chee</a>
      <a class="nav-pill" href="/en/viewer-hub">ViewerHub</a>
      <a class="nav-pill" href="/en/basics/customize/preferences">환경 설정</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">💻 개발자 &amp; 기여자</h4>
    <p style="flex:1;">플러그인 개발, 아키텍처 확장, 코드 · 번역 · 문서 기여.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/getting-started/#developer-documentation">개발자 문서</a>
      <a class="nav-pill" href="/en/basics/architecture">아키텍처</a>
      <a class="nav-pill" href="/en/basics/customize/build-plugins">플러그인</a>
    </div>
  </div>
</div>

### Weasis를 선택하는 이유

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1rem;margin:1rem 0;">
  <div style="border-left:4px solid #0d6efd;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">임상 판독을 위해 설계</h4>
    일반적인 모든 DICOM 검사 지원 — CT, MRI, 초음파, X-선, 유방촬영, PET, ECG, 구조화 보고서, 분할, 방사선 치료 계획. 다중 모니터, HiDPI, MPR, 3D, 완전한 주석 도구.
  </div>
  <div style="border-left:4px solid #198754;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">기존 환경에 자연스럽게 적응</h4>
    병원의 PACS나 웹 아카이브에 연결되고, 어떤 임상 포털에서도 한 번의 클릭으로 열리며, 로컬 폴더, USB 드라이브, DICOM CD의 파일을 읽습니다. 오프라인에서도 동작합니다.
  </div>
  <div style="border-left:4px solid #6c757d;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">신뢰할 수 있고, 자유롭고, 개방적</h4>
    <a href="https://github.com/nroduit/Weasis/blob/master/LICENSE">EPL 2.0 / Apache 2.0</a> 라이선스, <a href="https://github.com/nroduit/Weasis">GitHub</a>에 공개 — 벤더 종속 없음. <a href="https://www.hug.ch/en">HUG</a>를 비롯해 전 세계 병원, 임상시험, 포털에서 운영 중 — 오픈 이미징 뷰어의 <a href="/en/stories">제네바 계보</a>를 잇습니다.
  </div>
</div>

[전체 기능 목록 보기 →](/en/features) · [사례 연구 읽기 →](/en/stories)

### 겉은 단순하게, 속은 정교하게

- **[3D](/en/tutorials/dicom-3d-viewer) & [MPR](/en/tutorials/mpr)** — 볼륨 렌더링, 사선 재구성, [동기화 뷰](/en/tutorials/synch-view), [MIP](/en/tutorials/mip) 슬랩.
- **광범위한 DICOM 지원** — CT, MRI, US, X-선, PET, [SR](/en/tutorials/dicom-sr), [ECG](/en/tutorials/dicom-ecg), [오디오](/en/tutorials/dicom-audio), 4D, 멀티프레임.
- **DICOM [SEG](/en/tutorials/dicom-segmentation) & [RT](/en/tutorials/dicom-rt)** — 2D / MPR / 3D 오버레이, RTSTRUCT, RTDOSE 등선량, DVH.
- **[AI 친화적 객체](/en/tutorials/dicom-artificial-intelligence)** — 보조 캡처, 파라메트릭 맵, GSPS, SR, 분할.
- **[측정](/en/tutorials/draw-measure)** — [보정된](/en/tutorials/calibration) 거리, 각도, ROI 통계, [히스토그램](/en/tutorials/histogram); [KO / PR](/en/tutorials/build-ko-pr)로 저장.
- **[PACS 및 웹 통합](/en/basics/customize/integration)** — [DICOMweb](/en/tutorials/dicomweb-config), DIMSE Q/R, [`weasis://`](/en/getting-started/weasis-protocol)를 통한 포털 실행.
- **워크플로 편의성** — 다중 모니터, HiDPI, [도킹](/en/tutorials/docking), [단축키](/en/basics/shortcuts), [테마](/en/tutorials/theme), [로케일](/en/tutorials/locale).

{{< youtube id="ywaBAt2SqxM" title="Weasis DICOM viewer — overview" >}}
<br>

### 커뮤니티 &amp; 지원

- **질문** — [GitHub Discussions](https://github.com/nroduit/Weasis/discussions) · [dcm4che 포럼](https://groups.google.com/group/dcm4che) · [FAQ](/en/faq)
- **버그 신고 & 기능 요청** — [GitHub Issues](https://github.com/nroduit/Weasis/issues) ([좋은 버그 보고서 작성 방법](/en/faq#how-do-i-report-a-bug) 참조)
- **참여하기** — [코드, 번역, 문서, 사례 기여](/en/get-involved)
- **출판물에서 Weasis 인용** — [인용 형식](/en/faq#how-to-cite-weasis-in-a-publication)