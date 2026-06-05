---
title: Image Fusion
weight: 58
description: How to overlay a PET or SPECT series on a CT/MR base (PET/CT fusion) and read SUV statistics
keywords: [ "fusion", "pet/ct", "pet ct fusion", "spect", "suv", "overlay", "nuclear medicine", "dicom viewer", "open source dicom viewer" ]
---

## <center>Image Fusion</center>

**Image fusion** overlays a functional series — **PET** (`PT`) or **SPECT** (`NM`) — on top of an anatomical **CT** or **MR** base, so metabolic uptake can be read against the underlying anatomy. The overlay is a **registration-free geometric fusion**: Weasis aligns the two series from their DICOM spatial metadata alone, with no manual or algorithmic registration step. Available since {{% badge title="Version" %}}4.7.1{{% /badge %}}.

{{% notice note %}}
Fusion is a pure spatial overlay driven by each image's position in the patient coordinate system. It does **not** deform or re-register the images, so it is only offered when the two series are genuinely co-located (see [Requirements](#requirements) below).
{{% /notice %}}

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
- **LUT** — the color lookup table applied to the overlay. **PET** (a hot-metal palette tuned for functional data) is selected by default. The overlay is colorized through the functional series' own **window/level**, so it shows exactly the colors the overlay would have if displayed directly with that LUT.
- **Opacity** — two sliders set a flat blend (cross-fade) at composite time: `result = baseOpacity·base + overlayOpacity·overlay`. Each is labelled with the modality of the layer it controls (e.g. **CT** for the base, **PT** for the overlay). Defaults are **100 %** base and **75 %** overlay. Setting base **0 %** and overlay **100 %** shows the pure colorized overlay, identical to the functional series viewed on its own with the same LUT.

The overlay follows the base view as you scroll, zoom, window, or reslice it. Because the fusion is resampled from the functional **volume**, it stays correct on **oblique, coronal and sagittal** planes, not only the native acquisition plane.

{{% notice note %}}
The [Reset](dicom-2d-viewer#reset) action turns fusion **off** and returns to the plain base image, like any other display setting it restores.
{{% /notice %}}

### SUV statistics on a region of interest {#suv}

When the overlay is a PET series carrying the required metadata, a **closed measurement** drawn on the fused base image also reports the overlay's **SUV** values inside the region — **Min**, **Max** and **Mean**, in `SUVbw, g/ml`. These rows are sampled from the **original PET voxels** (no resampling loss on the maximum) and are tagged with the overlay's modality — for example `Max (PT)` — so they read alongside the base-image statistics.

{{% notice tip %}}
SUV is computed with the body-weight method (SUVbw), following the [vendor-neutral QIBA definition](https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)). The same values can be read directly on the PET series itself — see [SUV measurements](draw-measure#selected-measurement).
{{% /notice %}}

### Fusion in the MPR viewer {#mpr}

![Fusion on MPR](/tuto/fusion-mpr.png?classes=shadow)
<br>

Opening the [MPR viewer](mpr) from a fused 2D view **carries the fusion over**: the three MPR planes start with the same overlay series, LUT and opacities you set in the 2D view. Each plane keeps its **own** fusion settings, so you can fine-tune — or disable — the overlay independently per plane afterwards, without affecting the 2D view or the other planes.

{{% notice note %}}
Inheritance only applies when the overlay is still compatible with the reconstructed MPR base. If you open MPR from a non-fused view, the planes start with fusion off, and you can enable it from the same **Fusion** section as in the 2D viewer.
{{% /notice %}}

### See also

- [DICOM 2D Viewer](dicom-2d-viewer) — the base viewer hosting the Image tool.
- [View Synchronization](synch-view#frame-of-reference) — displaying a PET and its CT side by side instead of overlaid.
- [Draw & Measure](draw-measure#selected-measurement) — SUV and other measurements.
- [MPR Viewer](mpr) — multiplanar reconstruction.
