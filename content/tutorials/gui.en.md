---
title: GUI Overview
weight: 5
description: Essential aspects of the graphical user interface (GUI)
keywords: [ "GUI", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Essential aspects of the interface{{< svg "static/tuto/icon/Weasis.svg" >}}</center>

The following image shows the main elements of the graphical user interface (GUI). For more detailed documentation on the various elements of the interface, click on the green or blue areas of the image.

{{< svg "static/tuto/gui-overview.svg" >}}

The interface of the default DICOM workspace consists mainly of 2 parts:
1. The [DICOM Explorer](../dicom-explorer) on the left (in blue). It allows you to import and export data, as well as select the series to be visualized.
2. Depending on the data imported, different viewer/player types (represented by a tab) are displayed in the main section (green). Menus , toolbars and tools change according to the type of viewer selected. 
   * The selected viewer is the image above is the [DICOM 2D viewer](../dicom-2d-viewer) {{< svg "static/tuto/icon/view2d.svg" >}} which is the viewer opened by default. 
   * A tab containing a multi-view layout can display images from only one patient. However, one patient can appear in several tabs.
   * A tab is also docked panel that can be arranged by dragging and dropping it to the desired location. This makes it possible to display 2 tabs side by side.
   * See also [DICOM Explorer](../dicom-explorer/) to understand how to navigate through the Patient/Study/Series/Image.

{{% notice note %}}
Select your preferred language and regional settings in the [preferences](../locale). Adapt the graphical interface to your needs by [modifying the theme or the scaling factor](../theme) for a better user experience on HiDPI screens.
{{% /notice %}}

{{% notice tip %}}
In the View menu at the top, toolbars and tools related to the selected viewer can be shown or hidden. These display preferences are retained even after a restart. Only Explorer preferences are retained for the duration of the session.
{{% /notice %}}

### List of other viewers/Players in the DICOM workspace
* [Multiplanar Reconstruction (MPR) viewer](../mpr)
* [Maximum Intensity Projection (MIP) viewer](../mip)
* [DICOM 3D viewer](../dicom-3d-viewer)
* [DICOM ECG viewer](../dicom-ecg)
* DICOM Structured Report (SR) viewer
* DICOM Audio player
* DICOM PDF viewer (external)
* DICOM Video player (external)

### List of other workspaces
* Dicomizer
* Explorer of standard images (based on the non-dicom-explorer.json configuration profile)


