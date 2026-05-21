---
title: GUI Overview
weight: 5
description: Essential aspects of the graphical user interface (GUI)
keywords: [ "GUI", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Essential aspects of the interface {{< svg-inline "static/tuto/icon/Weasis.svg" >}}</center>

The image below shows the main elements of the Weasis graphical user interface. Click any of the green or blue areas to jump to the dedicated documentation for that element.

{{< svg "static/tuto/gui-overview.svg" >}}

The default DICOM workspace has two main areas:

1. The **[DICOM Explorer](dicom-explorer)** on the left (blue) — used to import and export data and to pick the series to display.
2. The **main area** on the right (green) — hosts the open viewers and players as tabs. The available menus, toolbars, and tools change depending on the viewer currently in focus.
   * In the screenshot above, the active viewer is the **[DICOM 2D Viewer](dicom-2d-viewer)** {{< svg-inline "static/tuto/icon/view2d.svg" >}}, which is the default for image series.
   * A tab with a multi-view layout can only display images from a **single patient**, but the same patient can appear in several tabs.
   * Each tab is a docked panel that can be moved by drag-and-drop, including side-by-side splits — see [Docking](docking) for the full layout options.
   * For navigating through the Patient / Study / Series / Image hierarchy, see the [DICOM Explorer](dicom-explorer/) page.

## Minimal configuration before starting

A few settings make Weasis noticeably more comfortable the first time you launch it. Open the preferences dialog from the main menu: **_File > Preferences (Alt + P)_**.

### Language and regional settings
In the **General** tab, pick your preferred **language** and **regional format** (dates, numbers). Only languages with at least 30 % translation coverage appear in the list. Dates, numbers, and other locale-sensitive values follow the selected regional format throughout the interface.

➜ See [Language and regional settings](locale) for the detailed instructions.

### Theme and scaling factor
In the **Appearance** tab:
- Choose a **theme** that suits your environment and reduces eye strain. The recommended theme is **Core Dark — Flat Weasis**.
- Set a **scaling factor** that matches your system display scaling. This is especially recommended for **HiDPI screens** — Weasis will scale fonts, icons, and every UI component consistently.

➜ See [Styles and themes](theme) for the detailed instructions.

{{% notice tip %}}
Wherever you need more complete instructions, click the {{< svg-inline "static/tuto/icon/help.svg" >}} button in the preferences dialog or in any contextual pop-up — it opens the matching page of this documentation in your browser.
{{% /notice %}}

{{% notice tip %}}
In the **View** menu at the top, the toolbars and tools attached to the active viewer can be shown or hidden. These preferences are remembered across restarts. Show / hide preferences specific to the **DICOM Explorer** are only kept for the current session.
{{% /notice %}}

### Other viewers and players in the DICOM workspace {#other-viewers-and-players}
Depending on the SOP Class of the loaded series, Weasis opens one of the following:

* [Multi-Planar Reconstruction (MPR) viewer](mpr)
* [Maximum Intensity Projection (MIP) viewer](mip)
* [DICOM 3D Volume Renderer](dicom-3d-viewer)
* [DICOM ECG viewer](dicom-ecg)
* [DICOM Structured Report (SR) viewer](dicom-sr)
* [DICOM Audio player](dicom-audio)
* **DICOM PDF viewer** — opened with the default system application registered for PDF files.
* **DICOM Video player** — opened with the default system player registered for MPEG files.

Overlay viewers — applied on top of an image series rather than opened on their own — include [DICOM Segmentation (SEG)](dicom-segmentation), [DICOM RT](dicom-rt), and [Presentation State (PR / GSPS)](build-ko-pr#presentation-state-pr-or-gsps).

### Other workspaces
* **[Dicomizer](dicomizer)** — the workspace for converting standard images into DICOM objects.
* **Standard image explorer** — workspace for non-DICOM images (configured through the `non-dicom-explorer.json` profile).