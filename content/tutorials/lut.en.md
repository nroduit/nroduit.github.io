---
title: Lookup Tables (LUT)
weight: 330
description: How to handle Color, VOI and Presentation LUTs
keywords: [ "Lookup Tables", "LUT", "VOI LUT",  "Modality LUT", "Presentation LUT", "DICOM LUT", "DICOM VOI LUT", "DICOM Modality LUT", "DICOM Presentation LUT", "DICOM viewer", "free DICOM viewer"]
---

## <center>How to handle Color and DICOM LUTs</center>

A **Lookup Table (LUT)** maps each input pixel value to an output value used somewhere along the rendering pipeline — turning raw acquisition numbers into the contrast, the color, and the brightness you actually see on screen. The [DICOM rendering pipeline](https://dicom.nema.org/medical/dicom/current/output/chtml/part04/sect_N.2.html) chains four kinds of LUT, each applied at a different stage:

1. **[Modality LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.html)** — converts raw pixel values into physical modality values (e.g. Hounsfield units for CT).
2. **[Values of Interest (VOI) LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.2.html)** — maps the modality values into a visible intensity range, enhancing specific anatomical structures or pathological conditions (this is what the **Window / Level** controls).
3. **[Presentation LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.6.html)** — converts the intensity values into **P-Values**: device-independent values calibrated to human perception (used to render consistently across monitors).
4. **[Palette Color LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.9.html)** — replaces grayscale intensity values with colors, producing a pseudo-color rendering.

{{% notice note %}}
The **Modality LUT** and the **Palette Color LUT** are applied automatically when present in the DICOM file — there are no controls in the user interface to override them.
{{% /notice %}}

### Windowing and Rendering {#windowing-and-rendering}

**Windowing and Rendering** is a panel in [Image Tools](dicom-2d-viewer/#image-tools) of the 2D viewer, exposing the user-controllable parts of the LUT pipeline. The same controls are also accessible from the **Lookup Table** toolbar, the main menu, and the right-click menu.

* **Window** — width of the input range mapped to the displayed values. Change it via the slider, or by selecting **Window / Level** in the [mouse actions](dicom-2d-viewer/#toolbars).
* **Level** — center of the range defined by **Window**. Same input options as above.
* {{< svg-inline "static/tuto/icon/winLevel.svg" >}} **Preset** — picks a predefined Window / Level pair. The dropdown is ordered as:
  * An empty entry, shown while Window and Level are being adjusted manually (slider or mouse drag).
  * Window / Level pairs or VOI LUT data carried by the DICOM file (suffixed with **_[DICOM]_**). The default selection is the first **_[DICOM]_** entry when present, otherwise **_Auto Level [Image]_**.
  * **_Auto Level [Image]_** (always shown) — Window and Level computed from the full pixel-value range of the current image.
  * Modality-specific presets (e.g. _Lung_, _Bone_, _Soft Tissue_ for CT).
* **LUT Shape** — the [transfer function](https://dicom.nema.org/medical/dicom/current/output/chtml/part17/chapter_Y.html) used between input and display: **linear** (default), **sigmoid**, or **logarithmic**.
* {{< svg-inline "static/tuto/icon/lut.svg" >}} **LUT** — pseudo-color LUT applied on top of the grayscale image. **_Default (image)_** keeps the original image color model. Picking a LUT from the toolbar or the menus is usually easier because each entry is shown with a preview.
* {{< svg-inline "static/tuto/icon/inverseLut.svg" >}} **Invert LUT** — flips the LUT direction (dark↔bright, or reversed color mapping).
* **Filter** — 2D image filter applied **before** the LUT, useful for enhancing image quality or highlighting specific structures. Default: **None**.

{{% notice tip %}}
To overlay the active LUT bar on the image, enable it from the [Display panel](dicom-2d-viewer/#display) on the right. The values labeled on the bar correspond to the **Modality LUT values** (e.g. Hounsfield units for CT) when one is defined, or to raw pixel values otherwise. On a fused view, the [fusion color scale](fusion#color-scale) is drawn beside it with the values of the overlay.

To inspect how the current Window / Level reshapes the pixel distribution, switch to the [Histogram](histogram) layout.
{{% /notice %}}