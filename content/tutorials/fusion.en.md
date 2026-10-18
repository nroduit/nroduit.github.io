---
title: "PET/CT Image Fusion with SUV"
weight: 58
description: How to overlay a PET or SPECT series on a CT/MR base (PET/CT fusion) and read SUV statistics
linkTitle: "Image Fusion"
keywords: [ "pet ct fusion", "image fusion", "suv statistics", "spect fusion", "pet viewer", "fusion color scale", "suv window", "pet scale maximum" ]
since: "4.7.1"
---

## <center>Functional series over anatomy, without registration</center>

**Image fusion** overlays a functional series — **PET** (`PT`) or **SPECT** (`NM`) — on top of an anatomical **CT** or **MR** base, so metabolic uptake can be read against the underlying anatomy. The overlay is a **registration-free geometric fusion**: Weasis aligns the two series from their DICOM spatial metadata alone, with no manual or algorithmic registration step. Available {{< since "4.7.1" >}}.

{{% callout note %}}
Fusion is a pure spatial overlay driven by each image's position in the patient coordinate system. It does **not** deform or re-register the images, so it is only offered when the two series are genuinely co-located (see [Requirements](#requirements) below).
{{% /callout %}}

### Requirements {#requirements}

A series can be fused onto the displayed base only when **all** of the following hold:

| Condition | Detail |
|-----------|--------|
| **Modality pairing** | A functional overlay (`PT`, `NM`) on an anatomical base (`CT`, `MR`). |
| **Same study** | Both series share the same `StudyInstanceUID`. |
| **Volume geometry** | Both are cross-sectional volumes (≥ 2 slices with Image Position / Orientation Patient and Pixel Spacing). |
| **Same coordinate system** | Either the `FrameOfReferenceUID` matches, or — as is common for separately reconstructed PET/CT — the two volumes **overlap in patient space**. |

When no compatible overlay is found in the study, the fusion controls stay disabled.

### Enable fusion {#enable}

The fusion controls live in the **Fusion** section of the **Image tool** {{< svg-inline "static/tuto/icon/imageEdit.svg" >}} panel. The section is collapsed by default — click its header to expand it.

- **Enable Fusion** — turns the overlay on or off. The other controls become active only while fusion is enabled.
- **Series** — the functional series to overlay. The list contains every compatible overlay found in the current study (see [Requirements](#requirements)).
- **LUT** — the color lookup table applied to the overlay. **PET** (a hot-metal palette tuned for functional data) is the default; {{< since "4.8.0" >}} a PET or SPECT overlay starts with **PET SUV**, the same ramp graduated in SUVbw, and an RT dose overlay with **Isodose**. The list gathers the maps meant for overlays and those tied to `PT`, `NM` and `RTDOSE`; see [Color Maps](color-maps/) for the whole library and for the editor that creates your own {{< since "4.8.0" >}}. The values are mapped to it through a series-wide [display window](#color-scale), not through the window/level of the functional series.
- **Opacity** — two sliders control the blend at composite time: `result = baseOpacity·base·(1 − a) + overlay·a`, where `a` is the overlay's own transparency at that pixel — it grows with the value and reaches the **Opacity** setting within the lower tenth of the [display window](#color-scale), so background stays invisible while everything above it is blended at the chosen opacity. Each slider is labeled with the modality of the layer it controls (e.g. **CT** for the base, **PT** for the overlay). Defaults are **100 %** base and **50 %** overlay. Setting the base to **0 %** leaves the colorized overlay alone over a black background.
- **Scale maximum** {{< since "4.8.0" >}} — the top of the overlay's [display window](#color-scale), in its display unit (`SUVbw` for a PET with SUV). It moves the top only, the bottom stays fixed; dragging the color bar on the view does the same. See [Adjust the scale maximum](#scale-max).

The overlay follows the base view as you scroll, zoom, window, or reslice it. Because the fusion is resampled from the functional **volume**, it stays correct on **oblique, coronal and sagittal** planes, not only the native acquisition plane.

{{% callout note %}}
The [Reset](dicom-2d-viewer#reset) action turns fusion **off** and returns to the plain base image, like any other display setting it restores.
{{% /callout %}}

### Display window and color scale {#color-scale}

Available {{< since "4.7.2" >}}.

The overlay is mapped to its LUT through a window derived from the whole functional series, so a given uptake keeps the same color on every slice. Its initial value is measured from the data; its top can then be [adjusted](#scale-max) {{< since "4.8.0" >}}:

| Overlay | Window |
|---------|--------|
| **PET whose SUV factor can be computed** | **0 SUVbw** to the next whole SUVbw above the series maximum, the top kept between **4** and **30**. Before 4.8.0 the scale started at **1 SUVbw**. |
| **Overlay with a DICOM pixel value unit** | **0** to the series maximum, in that unit (`BQML`, `CNTS`, …). |
| **Overlay without any unit** | **0 to 100 %** of the series maximum {{< since "4.8.0" >}}. |

{{% version since="4.8" %}}
A [color map](color-maps/) anchored to physical values carries its own scale, and then it is the map that sets the window: **PET SUV** displays **0 to 10 SUVbw**, and **Isodose** **0 to 120 % of the prescribed dose** when the RT plan gives one. The measured window of the table above applies to every other map — the maps that are relative to the displayed window, and the anchored maps whose unit cannot be expressed for the series (no SUV factor, a different pixel value unit, an unknown prescription).
{{% /version %}}

The upper bound is a high percentile of the active voxels rather than the plain maximum: physiologic excretion (bladder) and the injection site are several times hotter than any diagnostic structure, so they saturate at the top of the palette instead of pushing the rest of the study into its first tenth. The lower bound is **0**: the scale is read from zero, with no background subtraction. The lowest activity is still kept off the anatomy, because the overlay only fades in over the first tenth of the window (see **Opacity** above).

The resulting scale is drawn as a **color bar** on the fused view, beside the [LUT bar](lut) of the base image when both are shown:

- The value at the top of the bar is the window maximum, the one at the bottom its minimum.
- The unit written above it is **`SUVbw`** when SUV could be computed, the **DICOM pixel value unit** (`BQML`, `CNTS`, …) otherwise, or a **percentage** of the series maximum when the series carries no unit. Only `SUVbw` values can be compared with another acquisition: the others depend on the injected dose, the patient weight and the uptake time.
- The band the overlay paints as fully transparent is left blank, so the activity that is deliberately not shown reads as such instead of being mistaken for a color.

The bar is toggled with **Fusion Color Scale** in the [Display panel](dicom-2d-viewer#display) and is enabled by default. It is not drawn on views shorter than 350 pixels, where it would overlap the corner annotations.

### Adjust the scale maximum {#scale-max}

Available {{< since "4.8.0" >}}.

The top of the overlay scale can be changed while reading, independently of the window/level of the base image. The bottom stays where it is (0 SUVbw for a PET), so the scale is always read from zero:

- **Drag the color bar** — press the left mouse button on the color bar of the fused view and drag **up** to raise the maximum, **down** to lower it. The cursor turns into a vertical arrow over the bar. The drag works whatever action the left button carries elsewhere on the image, so the CT or MR keeps its usual [window/level](dicom-2d-viewer#toolbars) with the mouse while the PET is adjusted on the bar. The change is relative: each 128 pixels of drag doubles (or halves) the scale, so it feels the same on a 0–5 scale as on a 0–20 one.
- **Scale maximum slider** — in the **Fusion** section of the Image tool, for a precise value. It shows the maximum in the display unit and follows the drag.

The maximum can go up to the series maximum and, for a PET in SUVbw, to at least **30 SUVbw**, so a fixed tracer scale can be kept on a quieter study.

{{% callout tip %}}
For scales you use every day, create a [color map](color-maps/) with an absolute `SUVbw` range — for example FDG **0–5**, DOTATOC **0–10**, PSMA **0–20** — and mark it as a favorite. Selecting the map applies its scale; you can then still raise or lower the maximum for the study at hand. To return to a map's scale after an adjustment, select another map and then that one again.
{{% /callout %}}

{{% callout note %}}
The adjustment applies to the selected view (to all three planes in the [MPR viewer](#mpr)). When fusion is enabled, the window is first measured on a single slice and refined once the whole series is loaded; a maximum you set in the meantime is kept.
{{% /callout %}}

### SUV statistics on a region of interest {#suv}

When the overlay is a PET series carrying the required metadata, a **closed measurement** drawn on the fused base image also reports the overlay's **SUV** values inside the region — **Min**, **Max** and **Mean**, in `SUVbw, g/ml`. These rows are sampled from the **original PET voxels** (no resampling loss on the maximum) and are tagged with the overlay's modality — for example `Max (PT)` — so they read alongside the base-image statistics.

{{% callout tip %}}
SUV is computed with the body-weight method (SUVbw), following the [vendor-neutral QIBA definition](https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)). The same values can be read directly on the PET series itself — see [SUV measurements](draw-measure#selected-measurement).
{{% /callout %}}

### Fusion in the MPR viewer {#mpr}

![Fusion on MPR](/tuto/fusion-mpr.webp?classes=shadow)
<br>

Opening the [MPR viewer](mpr) from a fused 2D view **carries the fusion over**: the three MPR planes start with the same overlay series, LUT, opacities and [scale](#color-scale) you set in the 2D view. The three planes are views of one volume, so they share **one** fusion setting: a change made from any plane — enabling or disabling fusion, another series or LUT, an opacity, the [scale maximum](#scale-max) — applies to all three at once, and the overlay reads the same on every plane. The MPR fusion is independent of the 2D view it came from: changing one does not affect the other.

{{% callout note %}}
Inheritance only applies when the overlay is still compatible with the reconstructed MPR base. If you open MPR from a non-fused view, the planes start with fusion off, and you can enable it from the same **Fusion** section as in the 2D viewer.
{{% /callout %}}

### See also

- [DICOM 2D Viewer](dicom-2d-viewer) — the base viewer hosting the Image tool.
- [View Synchronization](synch-view#frame-of-reference) — displaying a PET and its CT side by side instead of overlaid.
- [Draw & Measure](draw-measure#selected-measurement) — SUV and other measurements.
- [MPR Viewer](mpr) — multiplanar reconstruction.
