---
archetype: "home"
title: "Weasis: visor DICOM"
description: "Visor DICOM libre y de código abierto para imagen médica — funciona como aplicación nativa en Windows / macOS / Linux o se lanza desde cualquier portal web. PACS, DICOMweb, MPR, 3D, compatible con IA."
keywords: [ "visor dicom", "visor dicom libre", "visor dicom open source", "visor dicom gratuito", "weasis", "visualizador dicom", "software dicom", "dicom", "pacs", "imagen médica", "radiología", "dicom viewer" ]
aliases:
  - /visor-dicom/
  - /visor-dicom-libre/
  - /visor-dicom-gratuito/
---

## <center>Un visor abierto para la imagen médica</center>

**Weasis** es un visor DICOM versátil y de código abierto, utilizable tanto como **aplicación nativa** como **desde la web**. De la lectura habitual a la revisión asistida por IA y la imagen cuantitativa, está diseñado para integrarse fácilmente con PACS, VNA y flujos DICOM de hospitales, ensayos clínicos multicéntricos y portales para pacientes.

<p style="text-align:center;">
{{% button href="/en/getting-started/download-dicom-viewer" style="primary" icon="download" %}}Descargar Weasis{{% /button %}}
{{% button href="/en/demo" style="green" icon="play" %}}Probar una muestra en vivo{{% /button %}}
{{% button href="/en/tutorials" style="secondary" icon="book" %}}Leer los tutoriales{{% /button %}}
</p>

{{% notice note %}}
Esta página principal está disponible en español. **El resto de la documentación está por ahora en inglés** — los enlaces que siguen redirigen a las páginas en inglés.
{{% /notice %}}

### Navegar por la documentación

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
    <h4 style="margin-top:0;">🩺 Clínicos &amp; usuarios finales</h4>
    <p style="flex:1;">Abrir estudios, manejar los visualizadores 2D / MPR / 3D, medir, anotar, compartir hallazgos.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/tutorials">Tutoriales</a>
      <a class="nav-pill" href="/en/basics/shortcuts">Atajos</a>
      <a class="nav-pill" href="/en/faq">FAQ</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">🛠 Integradores &amp; administradores</h4>
    <p style="flex:1;">Conectar Weasis a tu PACS, a tus endpoints DICOMweb, a tus portales HCE / SIR / SIH.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/basics/customize/integration">Integración</a>
      <a class="nav-pill" href="/en/getting-started/dcm4chee">dcm4chee</a>
      <a class="nav-pill" href="/en/viewer-hub">ViewerHub</a>
      <a class="nav-pill" href="/en/basics/customize/preferences">Preferencias</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">💻 Desarrolladores &amp; colaboradores</h4>
    <p style="flex:1;">Crear complementos, ampliar la arquitectura, contribuir con código, traducciones o documentación.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/getting-started/#developer-documentation">Documentación para desarrolladores</a>
      <a class="nav-pill" href="/en/basics/architecture">Arquitectura</a>
      <a class="nav-pill" href="/en/basics/customize/build-plugins">Plug-ins</a>
    </div>
  </div>
</div>

### Por qué Weasis

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1rem;margin:1rem 0;">
  <div style="border-left:4px solid #0d6efd;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Diseñado para la lectura clínica</h4>
    Abre todos los estudios DICOM habituales — TC, RM, ecografía, radiografía, mamografía, PET, ECG, informes estructurados, segmentaciones, planes de radioterapia. Multi-monitor, HiDPI, MPR, 3D, conjunto completo de herramientas de anotación.
  </div>
  <div style="border-left:4px solid #198754;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Encaja en tu entorno</h4>
    Se conecta al PACS o archivo web de tu hospital, se abre desde cualquier portal clínico con un clic, y lee archivos desde una carpeta local, un USB o un CD DICOM. Funciona sin conexión.
  </div>
  <div style="border-left:4px solid #6c757d;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Fiable, libre y abierto</h4>
    Bajo licencia <a href="https://github.com/nroduit/Weasis/blob/master/LICENSE">EPL 2.0 / Apache 2.0</a>, código abierto en <a href="https://github.com/nroduit/Weasis">GitHub</a> — sin dependencia de proveedor. En uso productivo en los <a href="https://www.hug.ch/en">HUG</a> y en hospitales, ensayos y portales de todo el mundo — heredero de un <a href="/en/stories">linaje ginebrino</a> de visores de imagen abiertos.
  </div>
</div>

[Ver la lista completa de funcionalidades →](/en/features) · [Leer los casos de estudio →](/en/stories)

### Sencillo en la superficie, avanzado por dentro

- **[3D](/en/tutorials/dicom-3d-viewer) y [MPR](/en/tutorials/mpr)** — renderizado volumétrico, reconstrucción oblicua, [vistas sincronizadas](/en/tutorials/synch-view), capas [MIP](/en/tutorials/mip).
- **Amplia cobertura DICOM** — TC, RM, US, radiografía, PET, [SR](/en/tutorials/dicom-sr), [ECG](/en/tutorials/dicom-ecg), [audio](/en/tutorials/dicom-audio), 4D, multi-frame.
- **DICOM [SEG](/en/tutorials/dicom-segmentation) y [RT](/en/tutorials/dicom-rt)** — superposiciones en 2D / MPR / 3D, RTSTRUCT, isodosis RTDOSE, DVH.
- **[Objetos preparados para IA](/en/tutorials/dicom-artificial-intelligence)** — captura secundaria, mapas paramétricos, GSPS, SR, segmentaciones.
- **[Mediciones](/en/tutorials/draw-measure)** — distancias [calibradas](/en/tutorials/calibration), ángulos, estadísticas de ROI, [histogramas](/en/tutorials/histogram); guardadas como [KO / PR](/en/tutorials/build-ko-pr).
- **[Integración PACS y web](/en/basics/customize/integration)** — [DICOMweb](/en/tutorials/dicomweb-config), DIMSE Q/R, lanzamiento desde portal mediante [`weasis://`](/en/getting-started/weasis-protocol).
- **Ergonomía del flujo de trabajo** — multi-monitor, HiDPI, [acoplamiento de paneles](/en/tutorials/docking), [atajos](/en/basics/shortcuts), [temas](/en/tutorials/theme), [idiomas](/en/tutorials/locale).

{{< youtube id="ywaBAt2SqxM" title="Weasis DICOM viewer — overview" >}}
<br>

### Comunidad &amp; soporte

- **Preguntas** — [Discusiones en GitHub](https://github.com/nroduit/Weasis/discussions) · [Foro dcm4che](https://groups.google.com/group/dcm4che) · [FAQ](/en/faq)
- **Informes de errores y solicitudes de funcionalidades** — [Issues en GitHub](https://github.com/nroduit/Weasis/issues) (ver [cómo redactar un buen informe de error](/en/faq#how-do-i-report-a-bug))
- **Participar** — [contribuir con código, traducciones, documentación, casos de uso](/en/get-involved)
- **Citar Weasis en una publicación** — [formato de citación](/en/faq#how-to-cite-weasis-in-a-publication)