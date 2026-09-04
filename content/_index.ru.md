---
# These pages deliberately link to the English tutorials, which are the only
# translated content that exists. Hugo cannot resolve "/en/..." as a content
# path (the language is a filename suffix, not a directory), so the link
# checker reports false negatives; the emitted URLs are correct.
urlIgnoreCheck: [ "^/en/" ]
archetype: "home"
title: "Weasis: DICOM-просмотрщик"
description: "Бесплатный DICOM-просмотрщик с открытым исходным кодом для медицинской визуализации — работает как нативное приложение на Windows / macOS / Linux или запускается из любого веб-портала. PACS, DICOMweb, MPR, 3D, поддержка ИИ."
keywords: [ "DICOM-просмотрщик", "просмотрщик dicom", "открытый dicom-просмотрщик", "бесплатный dicom-просмотрщик", "weasis", "медицинская визуализация", "рентгенология", "PACS", "DICOM", "dicom viewer" ]
aliases:
  - /dicom-russian/
  - /просмотрщик-dicom/
---

## <center>Открытый просмотрщик для медицинской визуализации</center>

**Weasis** — многофункциональный DICOM-просмотрщик с открытым исходным кодом, работающий и как **нативное приложение**, и **из веб-портала**. От повседневного просмотра до анализа с поддержкой ИИ и количественной визуализации — он спроектирован для гладкой интеграции с PACS, VNA и DICOM-процессами в больницах, многоцентровых клинических исследованиях и пациентских порталах.

<p style="text-align:center;">
{{% button href="/en/getting-started/download-dicom-viewer" style="primary" icon="download" %}}Скачать Weasis{{% /button %}}
{{% button href="/en/demo" style="green" icon="play" %}}Попробовать живой пример{{% /button %}}
{{% button href="/en/tutorials" style="secondary" icon="book" %}}Читать руководства{{% /button %}}
</p>

{{% notice note %}}
Эта главная страница доступна на русском языке. **Остальная документация пока только на английском** — ссылки ниже ведут на англоязычные страницы.
{{% /notice %}}

### Ориентируйтесь в документации

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
    <h4 style="margin-top:0;">🩺 Клиницисты &amp; конечные пользователи</h4>
    <p style="flex:1;">Открывайте исследования, управляйте 2D / MPR / 3D-просмотром, измеряйте, аннотируйте, делитесь результатами.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/tutorials">Руководства</a>
      <a class="nav-pill" href="/en/basics/shortcuts">Горячие клавиши</a>
      <a class="nav-pill" href="/en/faq">FAQ</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">🛠 Интеграторы &amp; администраторы</h4>
    <p style="flex:1;">Подключайте Weasis к вашему PACS, конечным точкам DICOMweb, порталам ЭМК / РИС / ГИС.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/basics/customize/integration">Интеграция</a>
      <a class="nav-pill" href="/en/getting-started/dcm4chee">dcm4chee</a>
      <a class="nav-pill" href="/en/viewer-hub">ViewerHub</a>
      <a class="nav-pill" href="/en/basics/customize/preferences">Настройки</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">💻 Разработчики &amp; контрибьюторы</h4>
    <p style="flex:1;">Разрабатывайте плагины, расширяйте архитектуру, вносите вклад в код, переводы или документацию.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/getting-started/#developer-documentation">Документация для разработчиков</a>
      <a class="nav-pill" href="/en/basics/architecture">Архитектура</a>
      <a class="nav-pill" href="/en/basics/customize/build-plugins">Плагины</a>
    </div>
  </div>
</div>

### Почему Weasis

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1rem;margin:1rem 0;">
  <div style="border-left:4px solid #0d6efd;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Создан для клинического просмотра</h4>
    Открывает все распространённые DICOM-исследования — КТ, МРТ, УЗИ, рентген, маммография, ПЭТ, ЭКГ, структурированные отчёты, сегментации, планы лучевой терапии. Многомониторность, HiDPI, MPR, 3D, полный набор инструментов аннотации.
  </div>
  <div style="border-left:4px solid #198754;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Вписывается в вашу среду</h4>
    Подключается к PACS или веб-архиву больницы, открывается из любого клинического портала одним кликом и читает файлы из локальной папки, USB-накопителя или DICOM-CD. Работает в автономном режиме.
  </div>
  <div style="border-left:4px solid #6c757d;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Надёжный, свободный, открытый</h4>
    Под лицензией <a href="https://github.com/nroduit/Weasis/blob/master/LICENSE">EPL 2.0 / Apache 2.0</a>, открытый код на <a href="https://github.com/nroduit/Weasis">GitHub</a> — без вендорского замка. Эксплуатируется в <a href="https://www.hug.ch/en">HUG</a> и в больницах, исследованиях и порталах по всему миру — наследник <a href="/en/stories">женевской линии</a> открытых визуализаторов.
  </div>
</div>

[Полный список возможностей →](/en/features) · [Читать кейсы →](/en/stories)

### Простой на поверхности, продвинутый внутри

- **[3D](/en/tutorials/dicom-3d-viewer) и [MPR](/en/tutorials/mpr)** — объёмный рендеринг, наклонная реконструкция, [синхронизированные виды](/en/tutorials/synch-view), слои [MIP](/en/tutorials/mip).
- **Широкая поддержка DICOM** — КТ, МРТ, УЗИ, рентген, ПЭТ, [SR](/en/tutorials/dicom-sr), [ЭКГ](/en/tutorials/dicom-ecg), [аудио](/en/tutorials/dicom-audio), 4D, мультифрейм.
- **DICOM [SEG](/en/tutorials/dicom-segmentation) и [RT](/en/tutorials/dicom-rt)** — наложения в 2D / MPR / 3D, RTSTRUCT, изодозы RTDOSE, DVH.
- **[Объекты, готовые для ИИ](/en/tutorials/dicom-artificial-intelligence)** — вторичный захват, параметрические карты, GSPS, SR, сегментации.
- **[Измерения](/en/tutorials/draw-measure)** — [калиброванные](/en/tutorials/calibration) расстояния, углы, статистика ROI, [гистограммы](/en/tutorials/histogram); сохраняются как [KO / PR](/en/tutorials/build-ko-pr).
- **[Интеграция PACS и веб](/en/basics/customize/integration)** — [DICOMweb](/en/tutorials/dicomweb-config), DIMSE Q/R, запуск из портала через [`weasis://`](/en/getting-started/weasis-protocol).
- **Эргономика рабочего процесса** — многомониторность, HiDPI, [докинг](/en/tutorials/docking), [горячие клавиши](/en/basics/shortcuts), [темы](/en/tutorials/theme), [локали](/en/tutorials/locale).

{{< youtube id="ywaBAt2SqxM" title="Weasis DICOM viewer — overview" >}}
<br>

### Сообщество &amp; поддержка

- **Вопросы** — [GitHub Discussions](https://github.com/nroduit/Weasis/discussions) · [Форум dcm4che](https://groups.google.com/group/dcm4che) · [FAQ](/en/faq)
- **Сообщения об ошибках и пожелания** — [Issues на GitHub](https://github.com/nroduit/Weasis/issues) (см. [как составить полезный отчёт об ошибке](/en/faq#how-do-i-report-a-bug))
- **Участвовать** — [вклад в код, переводы, документацию и рассказы](/en/get-involved)
- **Цитировать Weasis в публикации** — [формат цитирования](/en/faq#how-to-cite-weasis-in-a-publication)