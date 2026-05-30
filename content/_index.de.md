---
archetype: "home"
title: "Weasis: DICOM-Viewer"
description: "Freier Open-Source-DICOM-Viewer für die medizinische Bildgebung — läuft als native Anwendung unter Windows / macOS / Linux oder wird aus einem beliebigen Webportal gestartet. PACS, DICOMweb, MPR, 3D, KI-bereit."
keywords: [ "DICOM-Viewer", "freier DICOM-Viewer", "Open-Source-DICOM-Viewer", "kostenloser DICOM-Viewer", "weasis", "DICOM-Betrachter", "DICOM-Software", "dicom", "PACS", "medizinische Bildgebung", "Radiologie", "dicom viewer" ]
aliases:
  - /dicom-viewer-deutsch/
  - /freier-dicom-viewer/
  - /open-source-dicom-viewer/
---

## <center>Ein offener Viewer für die medizinische Bildgebung</center>

**Weasis** ist ein vielseitiger Open-Source-DICOM-Viewer, der sowohl als **native Anwendung** als auch **aus dem Web** läuft. Vom alltäglichen Befunden über KI-gestützte Beurteilung bis zur quantitativen Bildgebung ist Weasis auf die nahtlose Integration in PACS, VNA und DICOM-Workflows von Krankenhäusern, multizentrischen Studien und Patientenportalen ausgelegt.

<p style="text-align:center;">
{{% button href="/en/getting-started/download-dicom-viewer" style="primary" icon="download" %}}Weasis herunterladen{{% /button %}}
{{% button href="/en/demo" style="green" icon="play" %}}Live-Beispiel ausprobieren{{% /button %}}
{{% button href="/en/tutorials" style="secondary" icon="book" %}}Tutorials lesen{{% /button %}}
</p>

{{% notice note %}}
Diese Startseite ist auf Deutsch verfügbar. **Die übrige Dokumentation ist derzeit nur auf Englisch** — die folgenden Links führen daher zu englischsprachigen Seiten.
{{% /notice %}}

### Durch die Dokumentation navigieren

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
    <h4 style="margin-top:0;">🩺 Ärzte &amp; Anwender</h4>
    <p style="flex:1;">Studien öffnen, 2D-/MPR-/3D-Viewer steuern, messen, annotieren, Befunde teilen.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/tutorials">Tutorials</a>
      <a class="nav-pill" href="/en/basics/shortcuts">Tastenkürzel</a>
      <a class="nav-pill" href="/en/faq">FAQ</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">🛠 Integratoren &amp; Administratoren</h4>
    <p style="flex:1;">Weasis mit Ihrem PACS, Ihren DICOMweb-Endpunkten, Ihren EPA-/RIS-/KIS-Portalen verbinden.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/basics/customize/integration">Integration</a>
      <a class="nav-pill" href="/en/getting-started/dcm4chee">dcm4chee</a>
      <a class="nav-pill" href="/en/viewer-hub">ViewerHub</a>
      <a class="nav-pill" href="/en/basics/customize/preferences">Einstellungen</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">💻 Entwickler &amp; Mitwirkende</h4>
    <p style="flex:1;">Plug-ins schreiben, die Architektur erweitern, Code, Übersetzungen oder Dokumentation beitragen.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/getting-started/#developer-documentation">Entwicklerdoku</a>
      <a class="nav-pill" href="/en/basics/architecture">Architektur</a>
      <a class="nav-pill" href="/en/basics/customize/build-plugins">Plug-ins</a>
    </div>
  </div>
</div>

### Warum Weasis

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1rem;margin:1rem 0;">
  <div style="border-left:4px solid #0d6efd;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Für die klinische Befundung gebaut</h4>
    Öffnet alle gängigen DICOM-Untersuchungen — CT, MRT, Ultraschall, Röntgen, Mammographie, PET, EKG, strukturierte Befunde, Segmentierungen, Bestrahlungspläne. Mehrbildschirm, HiDPI, MPR, 3D, vollständiger Annotationswerkzeugkasten.
  </div>
  <div style="border-left:4px solid #198754;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Fügt sich in Ihre Umgebung ein</h4>
    Verbindet sich mit dem PACS oder Web-Archiv Ihres Krankenhauses, öffnet aus jedem klinischen Portal per Klick und liest Dateien aus einem lokalen Ordner, USB-Stick oder einer DICOM-CD. Funktioniert offline.
  </div>
  <div style="border-left:4px solid #6c757d;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Vertrauenswürdig, frei und offen</h4>
    Frei unter <a href="https://github.com/nroduit/Weasis/blob/master/LICENSE">EPL 2.0 / Apache 2.0</a>, offen auf <a href="https://github.com/nroduit/Weasis">GitHub</a> — kein Vendor-Lock-in. Produktiv im <a href="https://www.hug.ch/en">HUG</a> und in Krankenhäusern, Studien und Portalen weltweit im Einsatz — Erbe einer <a href="/en/stories">Genfer Linie</a> offener Bildbetrachter.
  </div>
</div>

[Vollständige Funktionsliste ansehen →](/en/features) · [Fallstudien lesen →](/en/stories)

### An der Oberfläche einfach, im Kern fortgeschritten

- **[3D](/en/tutorials/dicom-3d-viewer) & [MPR](/en/tutorials/mpr)** — Volumenrendering, schräge Rekonstruktion, [synchronisierte Ansichten](/en/tutorials/synch-view), [MIP](/en/tutorials/mip)-Schichten.
- **Breite DICOM-Abdeckung** — CT, MRT, US, Röntgen, PET, [SR](/en/tutorials/dicom-sr), [EKG](/en/tutorials/dicom-ecg), [Audio](/en/tutorials/dicom-audio), 4D, Multi-Frame.
- **DICOM [SEG](/en/tutorials/dicom-segmentation) & [RT](/en/tutorials/dicom-rt)** — Überlagerungen in 2D / MPR / 3D, RTSTRUCT, RTDOSE-Isodosis, DVH.
- **[KI-taugliche Objekte](/en/tutorials/dicom-artificial-intelligence)** — Sekundärerfassung, parametrische Karten, GSPS, SR, Segmentierungen.
- **[Messungen](/en/tutorials/draw-measure)** — [kalibrierte](/en/tutorials/calibration) Distanzen, Winkel, ROI-Statistiken, [Histogramme](/en/tutorials/histogram); als [KO / PR](/en/tutorials/build-ko-pr) speicherbar.
- **[PACS- und Web-Integration](/en/basics/customize/integration)** — [DICOMweb](/en/tutorials/dicomweb-config), DIMSE Q/R, Portalstart über [`weasis://`](/en/getting-started/weasis-protocol).
- **Workflow-Ergonomie** — Mehrbildschirm, HiDPI, [Andocken](/en/tutorials/docking), [Tastenkürzel](/en/basics/shortcuts), [Themes](/en/tutorials/theme), [Sprachen](/en/tutorials/locale).

{{< youtube id="ywaBAt2SqxM" title="Weasis DICOM viewer — overview" >}}
<br>

### Community &amp; Support

- **Fragen** — [GitHub Discussions](https://github.com/nroduit/Weasis/discussions) · [dcm4che-Forum](https://groups.google.com/group/dcm4che) · [FAQ](/en/faq)
- **Fehlerberichte & Feature-Wünsche** — [GitHub Issues](https://github.com/nroduit/Weasis/issues) (siehe [wie ein nützlicher Fehlerbericht aussieht](/en/faq#how-do-i-report-a-bug))
- **Mitmachen** — [Code, Übersetzungen, Dokumentation oder Erfahrungsberichte beitragen](/en/get-involved)
- **Weasis in einer Publikation zitieren** — [Zitationsformat](/en/faq#how-to-cite-weasis-in-a-publication)