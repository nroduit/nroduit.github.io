---
title: "DICOM LUTs: Color, VOI and Presentation"
weight: 330
description: "How color, VOI and presentation lookup tables are applied, how windowing and rendering interact, and how to use window/level presets."
linkTitle: "Lookup Tables (LUT)"
keywords: [ "dicom lut", "voi lut", "presentation lut", "modality lut", "windowing", "window level preset" ]
---

## <center>Each step of the rendering pipeline</center>

A **Lookup Table (LUT)** maps each input pixel value to an output value used somewhere along the rendering pipeline — turning raw acquisition numbers into the contrast, the color, and the brightness you actually see on screen. The [DICOM rendering pipeline](https://dicom.nema.org/medical/dicom/current/output/chtml/part04/sect_N.2.html) chains four kinds of LUT, each applied at a different stage:

1. **[Modality LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.html)** — converts raw pixel values into physical modality values (e.g. Hounsfield units for CT).
2. **[Values of Interest (VOI) LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.2.html)** — maps the modality values into a visible intensity range, enhancing specific anatomical structures or pathological conditions (this is what the **Window / Level** controls).
3. **[Presentation LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.6.html)** — converts the intensity values into **P-Values**: device-independent values calibrated to human perception (used to render consistently across monitors).
4. **[Palette Color LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.9.html)** — replaces grayscale intensity values with colors, producing a pseudo-color rendering. The palettes carried by the files, and the ones delivered with Weasis, are gathered in the same library — see [Color Maps](color-maps/).

{{% callout note %}}
The **Modality LUT** and the **Palette Color LUT** are applied automatically when present in the DICOM file — there are no controls in the user interface to override them.
{{% /callout %}}

### Windowing and Rendering {#windowing-and-rendering}

**Windowing and Rendering** is a panel in [Image Tools](dicom-2d-viewer/#image-tools) of the 2D viewer, exposing the user-controllable parts of the LUT pipeline. The same controls are also accessible from the **Lookup Table** toolbar, the main menu, and the right-click menu.

* **Window** — width of the input range mapped to the displayed values. Change it via the slider, or by selecting **Window / Level** in the [mouse actions](dicom-2d-viewer/#toolbars).
* **Level** — center of the range defined by **Window**. Same input options as above.
* **Lower level** and **Upper level** {{< since "4.8.0" >}} — for Nuclear Medicine (NM) images, the panel shows these two sliders instead of **Window** and **Level**: they set the lowest and the highest displayed value, each one without moving the other, as usual in NM practice. They act on the same Window / Level, so presets, synchronization and pseudo-color LUTs keep working.
* {{< svg-inline "static/tuto/icon/winLevel.svg" >}} **Preset** — picks a predefined Window / Level pair. The dropdown is ordered as:
  * An empty entry, shown while Window and Level are being adjusted manually (slider or mouse drag).
  * Window / Level pairs or VOI LUT data carried by the DICOM file (suffixed with **_[DICOM]_**); those of an applied [Presentation State](build-ko-pr/) come first. The default selection is the first **_[DICOM]_** entry when present, otherwise a preset marked as default for images without window values, otherwise **_Auto Level [Image]_**.
  * **_Auto Level [Image]_** (always shown) — Window and Level computed from the full pixel-value range of the current image.
  * The configured presets of the modality — for CT: _Brain_, _Stroke_, _Subdural_, _Temporal bones_, _Head and neck soft tissue_, _Mediastinum_, _Lung_, _Abdomen_, _Liver_, _Angio_, _Spine soft tissue_ and _Bone_, with the usual radiology values {{< since "4.8.0" >}}. The presets that fit the anatomy of the image come first: a chest CT lists _Mediastinum_ and _Lung_ at the top, a head CT _Brain_ and _Stroke_.

  Press a digit in the viewer to apply a preset: **0** for _Auto Level_, **1** and **2** for the first two **_[DICOM]_** entries, **3** to **9** for the configured presets that have a shortcut (e.g. **7** for _Lung_).
* **LUT Shape** — the [transfer function](https://dicom.nema.org/medical/dicom/current/output/chtml/part17/chapter_Y.html) used between input and display. **Linear** (default), **Linear Exact** {{< since "4.8.0" >}} and **Sigmoid** are the functions defined by DICOM; **Sigmoid Normalize**, **Logarithmic** and **Logarithmic Inverse** are additional Weasis shapes.
* {{< svg-inline "static/tuto/icon/lut.svg" >}} **LUT** — pseudo-color LUT applied on top of the grayscale image. **_Default (image)_** keeps the original image color model. Picking a LUT from the toolbar or the menus is usually easier because each entry is shown with a preview. The menu lists the LUTs of the current modality at its root and groups the others in submenus (category, other modalities, imported, user), with your **favorites** at the top {{< since "4.8.0" >}}. Maps such as _CT Tissues_ are anchored to fixed Hounsfield values, so their colors stay on the tissues instead of following the window and level {{< since "4.8.0" >}}. A color image has no gray level to map, so a LUT is not applied to it; only **Invert LUT** acts on such an image {{< since "4.8.0" >}}. See [Color Maps](color-maps/) for the whole library, the favorites, and the editor that creates and modifies maps.
* {{< svg-inline "static/tuto/icon/inverseLut.svg" >}} **Invert LUT** — flips the LUT direction (dark↔bright, or reversed color mapping).
* **Filter** — 2D image filter applied **before** the LUT, useful for enhancing image quality or highlighting specific structures. Default: **None**.

### Window / Level presets {#window-level-presets}

Besides the presets delivered with Weasis, you can keep your own Window / Level settings {{< since "4.8.0" >}}:

{{% version since="4.8" %}}

* **Save the current Window / Level** — adjust the image, then click the **+** button next to the **Preset** list in **Windowing and Rendering**, or choose **Save current W/L as preset…** in the Window / Level toolbar dropdown or in the preset menu of the right-click menu. Give a name, the modality (filled in from the series) and optionally a shortcut digit from **3** to **9**; the current **LUT Shape** is saved with it. Weasis asks before replacing one of your presets that has the same name and modality. The preset is available right away in the open viewers.
* **Manage the presets** — **Preferences > Viewer > Window/Level presets** lists every preset with its origin. The presets delivered with Weasis, and those shared by your administrator, are read-only: **Duplicate** one to make your own version. A shared preset is marked _(site)_, or _(site, locked)_ when your administrator does not allow replacing it; one of yours that reuses the id of a shared or delivered preset takes its place, and its **Delete** item becomes **Reset to the site preset** (or **…built-in preset**) to bring that definition back. For your presets you can change:
  * the name, the modalities and the shortcut — a digit already used by a built-in or a site preset goes to yours;
  * the values: in **Modality values** (e.g. Hounsfield units for CT), or in **Percent of the range** for images without calibrated values (MR, PET…), computed on the range of the image or of the series;
  * the LUT shape;
  * **Listed first for** — the anatomy for which the preset moves to the top of the list (e.g. _CHEST_), while staying available for other images. **Only for** hides the preset for other anatomies; as many images do not record their anatomy, prefer **Listed first for**. The **⋯** buttons list the areas (head, chest, abdomen…) and the common body parts.
  * whether the preset is the default for images that carry no window values;
  * **Min. bits stored** and **Only with a Modality LUT** — conditions that keep the preset off 8-bit captures (the default, 9, leaves them out) or off images without calibrated values.

  Use **⋯ > Export…** and **Import…** to share presets as a JSON file; the export holds your own presets only. They are stored in `customWindowPresets.json` in the Weasis preferences folder, on this workstation.

Administrators can also share presets with all the users of a site: see [Window/Level presets configuration](../../basics/customize/window-level-presets/).

{{% /version %}}

{{% callout tip %}}
To overlay the active LUT bar on the image, enable it from the [Display panel](dicom-2d-viewer/#display) on the right. The values labeled on the bar correspond to the **Modality LUT values** (e.g. Hounsfield units for CT) when one is defined, or to raw pixel values otherwise. On a fused view, the [fusion color scale](fusion#color-scale) is drawn beside it with the values of the overlay.

To inspect how the current Window / Level reshapes the pixel distribution, switch to the [Histogram](histogram) layout.
{{% /callout %}}