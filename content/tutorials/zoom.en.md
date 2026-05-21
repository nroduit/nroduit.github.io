---
title: Zoom
weight: 340
description: How to use zoom controls and magnifying lens
keywords: ["zoom", "lens", "magnifier", "real-world size", "monitor calibration", "dicom viewer", "pacs viewer"]
---

## <center>Zoom Tool {{< svg-inline "static/tuto/icon/zoom.svg" >}}</center>

The zoom tool changes how much of the image fits into the view. Beyond the standard "fit to screen" / "fit to pixel" magnifications, Weasis offers a **Real-world Size** mode that displays images at their **actual physical dimensions** on a calibrated monitor — useful for visual size estimation, surgical planning, or prosthesis sizing.

### Basic zoom controls

There are several ways to adjust magnification:

* **Mouse drag** — drag with the configured mouse button (middle mouse button by default; see the [2D viewer mouse actions](dicom-2d-viewer/#toolbars) to remap it).
* **Mouse wheel** — when enabled in the preferences.
* **Toolbar dropdown** — pick a preset zoom level.
* **Context menu** — right-click → **Zoom**.
* **Image Tool panel** — drag the zoom slider.
* **[Keyboard shortcuts](../basics/shortcuts/)** — zoom in, zoom out, and reset zoom.

{{% notice tip %}}
Quick access: press **Z** to switch the left mouse button to the zoom action (default — customizable since {{< badgeC "v4.7.0" >}} in [Keyboard Shortcuts](../basics/shortcuts/)).
{{% /notice %}}

### Zoom presets

The toolbar and context menu expose three presets:

* **Actual Pixels** {{< svg-inline "static/tuto/icon/zoomOriginal.svg" >}} — 1:1 display: one image pixel maps to one screen pixel.
* **Real-world Size** {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}} — physical-size display (requires a [calibrated monitor](#real-world-size-display)).
* **Best Fit** {{< svg-inline "static/tuto/icon/zoomBestFit.svg" >}} — scale the image to fit the view area (default).

{{% notice note %}}
- Zoom operations always center on the **screen**, regardless of the cursor position.
- **Best Fit** (the default) recenters images when you scroll through a series. To keep an off-center crop while scrolling, switch to another preset or set a manual zoom factor.
- To change the **interpolation method** used for zoom, see the [2D viewer preferences](dicom-2d-viewer/#preferences).
{{% /notice %}}

![Zoom tool controls](/tuto/zoom-actions.jpg?classes=shadow&width=700px)
<br>

### Real-world Size Display {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}} {#real-world-size-display}

Real-world size means **1 mm on the image equals 1 mm on the screen**, so anatomical structures appear at their true physical dimensions. This is essential for visual size estimation, surgical planning, prosthesis sizing, or any clinical comparison done directly on the monitor.

For Weasis to compute this accurately, it needs two things:

1. The **DICOM Pixel Spacing** of the image (already stored by the modality — see the [image-level Spatial Calibration](calibration) page when it's missing).
2. The **physical size of one screen pixel** for each monitor — this is what the **Spatial Calibration** step below provides.

Without monitor calibration, the {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}} **Real-world Size** preset falls back to the operating system's DPI value, which is rarely accurate.

#### What you need

* A precise ruler — ideally a **caliper** (mm or 1/10 mm graduations).
* The monitor in its **final position and resolution** (do not change the OS scaling factor after calibrating).

#### Step-by-step monitor calibration

1. Open **_File > Preferences (Alt + P) > Monitors_**.
2. The list shows every detected monitor with its pixel resolution; once calibrated, the real width × height in mm is appended in parentheses.
3. Click **Spatial calibration** next to the monitor you want to calibrate. A fullscreen window opens on **that** monitor and draws a black background with a white horizontal line and a white vertical line.
4. Physically measure one of the three references on the screen surface:
   * the **horizontal line**,
   * the **vertical line**, or
   * the screen **diagonal** (corner to corner of the visible glass).
5. At the bottom of the dialog, pick the matching reference in the first dropdown (**Horizontal line** / **Vertical line** / **Screen size**), type the measured value, and pick its unit (mm, cm, 1/1000 in, in).
6. Click **Apply**. The dialog redraws each line with its computed real length next to it — cross-check that the displayed value matches what you measured (within ±0.5 mm). Re-measure and re-apply if needed.
7. Close the calibration window. The Monitors page now shows the screen's real size, and the value is persisted (per monitor) for the next sessions.
8. Activate the result in any 2D viewer with the {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}} **Real-world Size** preset (toolbar dropdown, context menu **Zoom**, or the image tool panel).


#### Verifying the result

Open any image whose dimensions you know — a calibration phantom, a CR/DX study with a visible ruler, or a printed test pattern displayed full screen — and switch to {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}} **Real-world Size**. Use the [length measurement tool](../draw-measure) and compare with the physical ruler — the values should match within a fraction of a millimeter.

{{% notice warning %}}
If **Real-world Size** still looks wrong after monitor calibration, check that the image itself has valid **Pixel Spacing** (or **Imager Pixel Spacing** for projection radiography). Some secondary captures and screenshots ship without spatial information and cannot be displayed at real size — see [Spatial Calibration](calibration) for the manual override.
{{% /notice %}}

## <center>Magnifying Lens {{< svg-inline "static/tuto/icon/zoomPan.svg" >}}</center>

The **magnifying lens** is a movable, resizable overlay that displays a zoomed-in view of a small area without affecting the underlying image. Useful for inspecting fine detail (small lesions, calcifications, fine vascular structures) without changing the global zoom level, or for comparing two rendering parameters side-by-side using the freeze options.

Enable / disable the lens with its toggle button in the zoom toolbar.

![Lens example](/tuto/lens-drawing.jpg?classes=shadow&width=700px)
<br>

### Key features

* Magnify a specific region without modifying the main view.
* Hide overlays inside the lens (**Show Drawings** toggle).
* Compare different Window / Level settings side-by-side (**Freeze parameters**).
* Compare different images of the same series side-by-side (**Freeze image**).

### Lens controls

* **Mouse wheel** — adjust the lens zoom factor.
* **Double-click** — match the lens zoom to the main image zoom.
* **Right-click menu options**:
  * **Hide Lens** — disables the lens.
  * **Synchronize to parent zoom** — matches the lens zoom to the main image.
  * **Show Drawings** — toggles overlay visibility inside the lens.
  * **Magnify** — pick the lens zoom level from a preset list.
  * **Image** — control image and parameter freezing:
    * **Freeze Parameters** — keeps the current image processing settings (Window / Level, LUT, filters) frozen inside the lens while you scroll through the series elsewhere. Useful for comparing the same anatomical area with different rendering settings.
    * **Freeze Image** — captures both the image **and** its processing parameters, so the lens keeps showing the frozen image while the main view moves on. Useful when comparing different slices or time points of a study.
    * **Reset Freeze** — clears the frozen state; the lens reverts to following the current image and its processing settings.

![Lens with frozen parameters](/tuto/lens-freeze.jpg?classes=shadow&width=700px)