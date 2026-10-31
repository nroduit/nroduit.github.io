---
title: "DICOM RT Viewer: Structures, Isodoses and DVH"
weight: 220
description: "Display radiotherapy data: RT Structure Set contours, isodose lines and a dose colorwash from the RT Dose, and the dose-volume histogram chart."
linkTitle: "DICOM RT"
keywords: [ "dicom rt viewer", "rtstruct", "rt dose", "isodose lines", "dose colorwash", "dvh chart", "radiotherapy dicom" ]
---

## <center>The three objects a treatment is stored in {{< svg-inline "static/tuto/icon/rt.svg" >}}</center>

Radiotherapy treatment data is distributed across three companion DICOM objects:

* **RTSTRUCT** — contoured structures (target volumes, organs at risk, body outline) referenced to a planning CT.
* **RTPLAN** — prescribed dose, fractionation, beam geometry, and machine setup.
* **RTDOSE** — the computed dose distribution as a 3D pixel grid, with optional pre-computed DVH histograms.

When a CT series is loaded together with its associated RTSTRUCT, RTPLAN, and RTDOSE files, Weasis automatically links them and the **RT Tool** appears in the right panel.

### How to display structures
1. Click **_Load RT_** {{% badge style="red" %}}A{{% /badge %}} to load the linked DICOM STRUCT, PLAN, and DOSE objects. The button becomes inactive once loading completes.
2. {{% badge style="info" %}}Optional{{% /badge %}} Select a structure set {{% badge style="red" %}}B{{% /badge %}} if more than one is available.
3. {{% badge style="info" %}}Optional{{% /badge %}} Select a plan {{% badge style="red" %}}C{{% /badge %}} if more than one is available.

Try to open an RT sample {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/rt.xml"
{{< /launch >}}

{{% annotate src="/tuto/dicom-rt.webp" viewbox="0 0 1126 627" alt="Breast plan with its structures drawn on an axial CT, the RT Tool listing the structures, and the tooltip of the heart showing its volume and the dose it receives" class="shadow" %}}
A | | 880,48 | 26
B | | 1106,87 | 26
C | | 1080,125 | 26
D | | 1012,160 | 26
E | | 955,195 | 26
F | | 1000,230 | 26
G | | 1040,300 | 26
H | | 960,572 | 26
I | | 670,372 | 26
{{% /annotate %}}
<br>

The contours are drawn exactly as they are stored in the RTSTRUCT, as smooth outlines rather than following the edges of the image pixels {{< since "4.8.0" >}}.

Hover over a structure, on the image or in the tree {{% badge style="red" %}}G{{% /badge %}}, to show its tooltip {{% badge style="red" %}}I{{% /badge %}} with its slice thickness, its volume and, when a dose is loaded, the minimum, maximum and mean dose it receives, in percent of the prescribed dose. In the image above, the heart receives on average 33 % of the 1400 cGy prescribed to the breast. The dose values start with **PROVIDED** when they come from the DVH stored in the DICOM file, and with **CALCULATED** when Weasis computed them from the dose grid.

{{% callout note %}}
The region tree exposes a context menu with the following actions:
* **Select / unselect all child nodes** (parent nodes only) — toggle visibility for every sub-region in a group at once.
* **Fill opacity** — controls the transparency of the region's interior relative to its border.
    - Default value: 20%
    - Perceived opacity = _Line opacity × Fill opacity_
    - Example: 80 % line + 20 % fill → 16 % perceived interior opacity.
* **Export to clipboard as CSV** — copies region data (volume measurements, dose calculations) for analysis in spreadsheets or external tools.
* **Pixel statistics from the selected view** (leaf nodes only) — computes statistical descriptors of pixel values inside the region. For the parameter definitions, see [Pixel Statistics](draw-measure/#selected-measurement).
{{% /callout %}}

### How to display isodoses
1. Switch to the **Isodoses** tab {{% badge style="red" %}}F{{% /badge %}}.
2. Check the **Isodoses** root node — it is unchecked by default.
3. {{% badge style="info" %}}Optional{{% /badge %}} Adjust the graphic opacity {{% badge style="red" %}}H{{% /badge %}} (default: 50 %).

![DICOM DOSE](/tuto/dicom-rt-dose.webp?classes=shadow)
<br>

{{% callout tip %}}
The **Structures** and **Isodoses** root nodes act as master switches — toggle them to show or hide all overlays at once, while child nodes keep individual control over specific items.
{{% /callout %}}

{{% callout note %}}
The isodose overlay is rendered directly from the **RTDOSE pixel grid** (resampled to the CT image grid using nearest-neighbor interpolation) instead of vector contours {{< since "4.7.0" >}}. This provides a more faithful representation of the dose distribution stored in the DICOM file, especially around steep dose gradients.
{{% /callout %}}

### How to display the dose as a colorwash {#colorwash}

A **colorwash** paints the whole dose distribution over the CT in color, instead of drawing a few isodose lines {{< since "4.8.0" >}}: every point of the image is tinted according to the dose it receives, so the shape of the high-dose region and how quickly the dose falls off around it can be read at a glance.

1. Load the RT objects and select the plan (see [How to display structures](#how-to-display-structures)).
2. Check **Colorwash** {{% badge style="red" %}}D{{% /badge %}}, next to the prescribed **Dose** of the plan at the top of the RT Tool.

![Axial CT of the breast plan with the dose shown as a colorwash and its Isodose color bar graduated from 0 to 120 % of the prescribed dose](/tuto/dicom-rt-colorwash.webp?classes=shadow)
<br>

The dose grid of the plan is laid over the selected view with the **Isodose** [color map](color-maps/), graduated in **percent of the prescribed dose** from 0 to 120 %. Its colors are bands, like the isodose levels: nothing below 10 %, then blue, light blue, green, yellow and orange up to 100 %, **red** from the prescription and **magenta** from 110 %, where an overdose stands out. When the plan gives no prescribed dose, the scale is measured on the dose grid instead.

The colorwash uses the [image fusion](fusion) overlay, so everything described there applies:

* a **color bar** beside the view shows the scale;
* the **Fusion** section of the **Image tool** panel changes the opacity (50 % by default), the color map or the top of the scale;
* the overlay follows the view as you scroll, zoom or change the window, and it can be combined with the isodose lines and the structures.

Uncheck **Colorwash** to remove it. The [Reset](dicom-2d-viewer#reset) action also turns it off.

### How to display the DVH chart
The Dose-Volume Histogram (DVH) summarizes, for each selected structure, the fraction of its volume that receives at least a given dose level — the standard way to compare plans and check organ-at-risk constraints.

* Select one or several structures (the **Structures** root node must also be selected).
* Click **_Display DVH chart_** {{% badge style="red" %}}E{{% /badge %}}.
* Right-click on the chart to print or save as PNG, or as a vector file (SVG, EPS).

The horizontal axis is the dose in cGy, the vertical axis the percentage of the structure volume. A DVH stored in the RTDOSE is plotted at its real dose whatever the width of its dose bins, and the chart opens quickly even with many structures {{< since "4.8.0" >}}. Earlier versions could draw a DVH stored with bins other than 1 cGy on the wrong dose scale — 0.1 Gy bins, for example, ten times too short.

![DVH chart of the breast plan: volume in percent against dose in cGy for the breast, tumor bed, scar, nodes, heart, left lung and body](/tuto/dicom-rt-dvh.webp?classes=shadow)
<br>

{{% callout warning %}}
When one or more selected structures have no DVH stored in the RTDOSE, a **confirmation dialog** {{< since "4.7.0" >}} lists the affected structures and offers to compute the missing histograms on the fly.

The calculation algorithm (derived from [dicompyler](https://github.com/dicompyler/dicompyler-core)) is **experimental and not clinically validated**: results must not be used for medical decisions. The feature can be disabled by setting the [system preference](../basics/customize/preferences) `weasis.rt.dvh.recalculate.enable` to `false`; when disabled, only DVHs already stored in the RTDOSE are displayed.
{{% /callout %}}