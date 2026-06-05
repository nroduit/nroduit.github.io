---
title: Build DICOM KO and PR
weight: 335
description: How to build and export DICOM Key Object Selection and Presentation State (GSPS)
keywords: [ "Key Object Selection", "Presentation State", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to build and export DICOM KO and PR</center>

Weasis can author two standard DICOM annotation objects directly from the viewer:

- **Key Object Selection (KO)** — a list of "key images" inside a series. Use it to flag the slices that matter for a finding so a reader can scroll only through those.
- **Presentation State (PR / GSPS)** — drawings, measurements, and other graphic overlays that reference the source images. Use it to share findings across systems without baking annotations into the pixels.

Both objects can be saved as proper DICOM files and sent to a PACS through the standard [DICOM Export](dicom-export) workflow, so they travel with the study and can be re-applied by any DICOM-compatible viewer.

### Key Object Selection (KO) {#key-object-selection-ko}

To make the KO controls visible, enable the **Key Object Selection** toolbar from **_View > Toolbars > Key Object Selection Toolbar_** in the main menu.

When a DICOM KO is loaded with the series, it appears in the explorer menu (1) and can also be picked from the icon on the right side of the view (6). KO objects created in Weasis behave the same way.

![Build KO](/tuto/ko-actions.jpg?classes=shadow&width=100%)

Actions available in the KO toolbar:

- **Apply a KO** (2) {{< svg-inline "static/tuto/icon/keyImage.svg" >}} — select which KO drives the current view.
- **Mark / unmark a key image** (3) — click the **star** icon, or press **K** (default — customizable since {{< badgeC "v4.7.0" >}} in [Keyboard Shortcuts](../basics/shortcuts)) to add the current image to the active KO, or create a new one if none exists yet.
- **Filter to key images only** (4) — when active, scrolling skips every image that is not part of the selected KO, so you see only the flagged slices.
- **Create / delete a KO** (5) — start a new KO (optionally seeded from an existing one) or delete a KO. Only KOs created by Weasis can be deleted.

### Presentation State (PR or GSPS) {#presentation-state-pr-or-gsps}

- **Apply a PR loaded from a DICOM file** (1) {{< svg-inline "static/tuto/icon/imagePresentation.svg" >}} — since {{% badge title="Version" %}}2.6.0{{% /badge %}}, PRs are **not** applied automatically; click the dedicated icon (2) above the image to apply one. To have the most recent PR applied by default, enable **Apply by default the most recent Presentation State** under **_File > Preferences (Alt + P)_** (also configurable through the [default preferences](../basics/customize/preferences/)).
- **Create a new PR** — any drawing or measurement (see [Draw & Measure](draw-measure)) can be exported into a DICOM Presentation State. Image-rendering parameters (zoom, calibration, window/level, LUT…) are **not yet** included in the exported PR.

![Build PR](/tuto/pr-actions.jpg?classes=shadow&width=100%)
<br>

### Exporting Key Object Selection or Presentation State

Newly created KO and PR objects are exported through the standard [DICOM Export](dicom-export) dialog — open it from the toolbar icon or from **_File > Export > DICOM_**.

![Export KO locally](/tuto/export-ko-pr.png?classes=shadow)
<br>

1. Pick the export destination — **Local Device**, **DICOM Send**, or **CD/DVD Image** (see [DICOM Export](dicom-export#exporting) for the per-destination options).
2. Choose the export options. Series created inside Weasis (including new KO and PR objects) are flagged **NEW** in the selection tree.
3. Select the patient(s), study, series, or individual instances to export.
4. Click **Export** to write or transfer the files, then close the window.