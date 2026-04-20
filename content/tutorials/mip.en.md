---
title: MIP Viewer
weight: 55
description: How to use the Maximum Intensity Projection (MIP) viewer
keywords: [ "MIP", "Maximum Intensity Projection", "dicom", "free dicom viewer" ]
---

## <center>Maximum Intensity Projection (MIP) {{< svg-inline "static/tuto/icon/mip.svg" >}}</center>

The MIP viewer allows displaying the maximum intensity projection of a volume defined by a number of slices of the image stack.

{{% badge title="Version" %}}4.7.0{{% /badge %}} MIP projection mode is no longer a standalone window. It is now integrated directly within the standard [DICOM 2D viewer](dicom-2d-viewer), with full synchronization and slab geometry overlay.

MIP is also available in other viewers, each with its own configuration:
- **[MPR viewer](mpr)**: MIP can be enabled per view via the view configuration button, allowing slab projection on any reconstruction plane.
- **[3D viewer](dicom-3d-viewer)**: offers MIP volume rendering type, but requires some [minimal hardware requirements](dicom-3d-viewer/#requirements).


### Activating MIP in the 2D Viewer
The MIP projection mode can be activated with {{< svg-inline "static/tuto/icon/mip.svg" >}} in the Basic 3D toolbar of the [DICOM 2D viewer](dicom-2d-viewer).

{{% notice note %}}
If the button is grayed out, it means that the current series has less than 5 images, which is the minimal number of images for using the MIP projection. 
{{% /notice %}}

{{% notice tip %}}
If the series is a **multi-phase 4D acquisition** (e.g., a cardiac CT with several temporal phases), Weasis will automatically split it into individual phase sub-series when 2–7 phases are detected. For series with 8 or more phases, a confirmation dialog is shown first. Open any resulting phase sub-series to use it in MIP mode. See [4D Series Sub-Series Splitting](dicom-explorer#4d-splitting) for details.
{{% /notice %}}

Once enabled, the MIP mode provides:

- **Full synchronization**: the MIP slab stays synchronized with the current slice position and any linked views.
- **Slab geometry overlay**: a visual overlay indicates the extent of the slab used for the projection directly on the image.
- **View indicator**: once MIP is active on a view, the same {{< svg-inline "static/tuto/icon/mip.svg" >}} icon appears in the top-right corner of that view to indicate MIP is enabled. Clicking this icon opens the same MIP options as the toolbar button, making it easy to adjust settings per view without leaving the layout.

### The MIP Options

The MIP options can be opened from two places:
- The {{< svg-inline "static/tuto/icon/mip.svg" >}} button in the Basic 3D toolbar (applies to the currently selected view).
- The {{< svg-inline "static/tuto/icon/mip.svg" >}} indicator icon in the top-right corner of any view that has MIP active.

![MIP Options](/tuto/mip.jpg?classes=shadow)
<br>

{{% notice note %}}
In MIP mode, annotations and measurements can be added on the projected image. However, they are **not persistent when scrolling** — they are tied to the slice on which they were drawn and will no longer be visible once you navigate to a different position. To permanently preserve annotations or measurements for a specific MIP configuration, use [Build a new series](#build-a-new-series).
{{% /notice %}}

#### Projection
The projection type defines the way the MIP is calculated. The options are:
* **None**: No projection, display the original image
* **Min**: Minimum Intensity Projection
* **Mean**: Mean Intensity Projection
* **Max**: Maximum Intensity Projection (the default value)

When a projection type other than **None** is selected, the slice thickness is automatically initialized to **2 pixels** (1 pixel before and 1 pixel after the current slice).

#### MIP thickness
The slice thickness defines the extent of the slab used for the projection. It is expressed as the number of pixels before and after the current slice (e.g., a value of 3 means 3 slices on each side, 7 slices total).

The dropdown list shows suggested pixel values with the corresponding physical thickness in millimeters in parentheses (e.g., `5 (3.5 mm)`), when the images are spatially calibrated. The last entry in the list is _Custom thickness_, which allows entering any arbitrary value manually.

#### Build a new series
It allows you to build a new MIP series according to the current options. The new MIP series is added to the [DICOM explorer](dicom-explorer/) and can be [exported](dicom-export/#exporting).
