---
archetype: "home"
title: "Weasis : visionneuse DICOM"
description: "Visionneuse DICOM libre et open source pour l'imagerie médicale — utilisable en application autonome sur Windows / macOS / Linux ou lancée depuis n'importe quel portail web. PACS, DICOMweb, MPR, 3D, compatible IA."
keywords: [ "visionneuse dicom", "visionneuse dicom libre", "visionneuse dicom open source", "visionneuse dicom gratuite", "weasis", "visualiseur dicom", "logiciel dicom", "dicom", "pacs", "imagerie médicale", "radiologie", "dicom viewer" ]
aliases:
  - /visionneuse-dicom/
  - /visionneuse-dicom-libre/
  - /visionneuse-dicom-gratuite/
---

## <center>Une visionneuse ouverte pour l'imagerie médicale</center>

**Weasis** est une visionneuse DICOM polyvalente et open source, utilisable à la fois en **application ntive** et **depuis le web**. De la lecture quotidienne à la relecture assistée par IA en passant par l'imagerie quantitative, elle est conçue pour s'intégrer facilement aux PACS, VNA et flux DICOM des hôpitaux, des essais cliniques multicentriques et des portails patients.

<p style="text-align:center;">
{{% button href="/en/getting-started/download-dicom-viewer" style="primary" icon="download" %}}Télécharger Weasis{{% /button %}}
{{% button href="/en/demo" style="green" icon="play" %}}Essayer un exemple en direct{{% /button %}}
{{% button href="/en/tutorials" style="secondary" icon="book" %}}Lire les tutoriels{{% /button %}}
</p>

{{% notice note %}}
Cette page d'accueil est disponible en français. **Le reste de la documentation est pour l'instant en anglais** — les liens ci-dessous renvoient donc vers les pages anglaises.
{{% /notice %}}

### Naviguer dans la documentation

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
    <h4 style="margin-top:0;">🩺 Cliniciens &amp; utilisateurs finaux</h4>
    <p style="flex:1;">Ouvrir des examens, piloter les visualisations 2D / MPR / 3D, mesurer, annoter, partager les résultats.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/tutorials">Tutoriels</a>
      <a class="nav-pill" href="/en/basics/shortcuts">Raccourcis</a>
      <a class="nav-pill" href="/en/faq">FAQ</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">🛠 Intégrateurs &amp; administrateurs</h4>
    <p style="flex:1;">Connecter Weasis à votre PACS, à vos points d'accès DICOMweb, à vos portails DPI / SIR / SIH.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/basics/customize/integration">Intégration</a>
      <a class="nav-pill" href="/en/getting-started/dcm4chee">dcm4chee</a>
      <a class="nav-pill" href="/en/viewer-hub">ViewerHub</a>
      <a class="nav-pill" href="/en/basics/customize/preferences">Préférences</a>
    </div>
  </div>
  <div style="border:1px solid rgba(128,128,128,0.3);border-radius:0.4rem;padding:1rem;display:flex;flex-direction:column;">
    <h4 style="margin-top:0;">💻 Développeurs &amp; contributeurs</h4>
    <p style="flex:1;">Écrire des plug-ins, étendre l'architecture, contribuer au code, aux traductions ou à la documentation.</p>
    <div class="nav-pills">
      <a class="nav-pill" href="/en/getting-started/#developer-documentation">Doc développeur</a>
      <a class="nav-pill" href="/en/basics/architecture">Architecture</a>
      <a class="nav-pill" href="/en/basics/customize/build-plugins">Plug-ins</a>
    </div>
  </div>
</div>

### Pourquoi Weasis

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1rem;margin:1rem 0;">
  <div style="border-left:4px solid #0d6efd;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Conçu pour la lecture clinique</h4>
    Ouvre tous les examens DICOM courants — TDM, IRM, échographie, radiographie, mammographie, TEP, ECG, comptes rendus structurés, segmentations, plans de radiothérapie. Multi-écran, HiDPI, MPR, 3D, panoplie complète d'annotations.
  </div>
  <div style="border-left:4px solid #198754;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">S'intègre à votre environnement</h4>
    Se connecte au PACS ou à l'archive web de l'hôpital, s'ouvre depuis n'importe quel portail clinique en un clic, et lit des fichiers depuis un dossier local, une clé USB ou un CD DICOM. Fonctionne hors ligne.
  </div>
  <div style="border-left:4px solid #6c757d;padding:0.6rem 1rem;">
    <h4 style="margin-top:0;">Fiable, libre et ouvert</h4>
    Sous licence <a href="https://github.com/nroduit/Weasis/blob/master/LICENSE">EPL 2.0 / Apache 2.0</a>, code ouvert sur <a href="https://github.com/nroduit/Weasis">GitHub</a> — aucun verrouillage propriétaire. Utilisé en production aux <a href="https://www.hug.ch/">HUG</a> et dans des hôpitaux, essais et portails du monde entier — héritier d'une <a href="/en/stories">lignée genevoise</a> de visionneuses d'imagerie ouvertes.
  </div>
</div>

[Voir la liste complète des fonctionnalités →](/en/features) · [Lire les études de cas →](/en/stories)

### Simple en surface, avancé en profondeur

- **[3D](/en/tutorials/dicom-3d-viewer) & [MPR](/en/tutorials/mpr)** — rendu volumique, reconstruction oblique, [vues synchronisées](/en/tutorials/synch-view), épaisseurs [MIP](/en/tutorials/mip).
- **Large couverture DICOM** — TDM, IRM, US, radiographie, TEP, [SR](/en/tutorials/dicom-sr), [ECG](/en/tutorials/dicom-ecg), [audio](/en/tutorials/dicom-audio), 4D, multi-frame.
- **DICOM [SEG](/en/tutorials/dicom-segmentation) & [RT](/en/tutorials/dicom-rt)** — superpositions en 2D / MPR / 3D, RTSTRUCT, isodoses RTDOSE, HDV.
- **[Objets provenant de l'IA](/en/tutorials/dicom-artificial-intelligence)** — captures secondaires, cartes paramétriques, GSPS, SR, segmentations.
- **[Mesures](/en/tutorials/draw-measure)** — distances [calibrées](/en/tutorials/calibration), angles, statistiques de ROI, [histogrammes](/en/tutorials/histogram) ; enregistrées en [KO / PR](/en/tutorials/build-ko-pr).
- **[Intégration PACS & web](/en/basics/customize/integration)** — [DICOMweb](/en/tutorials/dicomweb-config), DIMSE Q/R, lancement depuis un portail via [`weasis://`](/en/getting-started/weasis-protocol).
- **Ergonomie du flux de travail** — multi-écran, HiDPI, [ancrage des fenêtres](/en/tutorials/docking), [raccourcis](/en/basics/shortcuts), [thèmes](/en/tutorials/theme), [langues](/en/tutorials/locale).

{{< youtube id="ywaBAt2SqxM" title="Weasis, visionneuse DICOM — présentation" >}}
<br>

### Communauté &amp; support

- **Questions** — [Discussions GitHub](https://github.com/nroduit/Weasis/discussions) · [Forum dcm4che](https://groups.google.com/group/dcm4che) · [FAQ](/en/faq)
- **Rapports de bug & demandes de fonctionnalités** — [Issues GitHub](https://github.com/nroduit/Weasis/issues) (voir [comment rédiger un bon rapport de bug](/en/faq#how-do-i-report-a-bug))
- **S'impliquer** — [contribuer au code, aux traductions, à la documentation, partager une expérience](/en/get-involved)
- **Citer Weasis dans une publication** — [format de citation](/en/faq#how-to-cite-weasis-in-a-publication)