---
title: Zoom
weight: 340
description: How to use zoom controls and magnifying lens
keywords: ["zoom", "lens", "dicom viewer", "pacs viewer"]
---

## Zoom Tool {{< svg-inline "static/tuto/icon/zoom.svg" >}}

### Basic Zoom Controls

The zoom tool {{< svg-inline "static/tuto/icon/zoom.svg" >}} provides multiple ways to adjust image magnification:

* **Mouse Drag**: Drag with the configured mouse button (middle button by default)
* **Mouse Wheel**: When enabled in preferences
* **Toolbar Dropdown**: Select preset zoom levels
* **Context Menu**: Right-click > Zoom
* **Image Tool Panel**: Use the zoom slider
* **[Keyboard Shortcuts](../../basics/shortcuts/)**: zoom in, zoom out, and reset zoom

{{% notice tip %}}
Quick Access: Press `z` to instantly set zoom as the left mouse button action
{{% /notice %}}

### Zoom Presets

The toolbar and context menu offer three preset zoom options:

* **Actual Pixels** {{< svg-inline "static/tuto/icon/zoomOriginal.svg" >}}: 1:1 ratio display
* **Real-world Size** {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}}: Physical size display
* **Best Fit** {{< svg-inline "static/tuto/icon/zoomBestFit.svg" >}}: Scale to fit view area

{{% notice note %}}
* Zoom operations always center on the screen, regardless of cursor position
* Best Fit (default mode) recenters images when scrolling through a series
* To maintain off-center positioning while scrolling, change the zoom mode or factor
* To change the zoom interpolation method, see the [Preferences](dicom-2d-viewer/#preferences) section
{{% /notice %}}

![Zoom tool controls](/tuto/zoom-actions.jpg?classes=shadow&width=700px)
<br>

### Real-world Size Display {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}} {#real-world-size-display}

Real-world size means **1 mm on the image equals 1 mm on the screen**, so anatomical
structures appear at their true physical dimensions. This is essential for visual size
estimation, surgical planning, prosthesis sizing, or any clinical comparison done
directly on the monitor.

For Weasis to compute this accurately, it needs two things:

1. The **DICOM pixel spacing** of the image (already stored by the modality).
2. The **physical size of one screen pixel** for each monitor — this is what the
   *Spatial Calibration* step below provides.

Without calibration the {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}}
*Real-world Size* preset falls back to the operating system DPI, which is rarely
correct.

#### What you need

* A precise ruler or, ideally, a **caliper** (mm or 1/10 mm graduations).
* The monitor in its **final position and resolution** (do not change the OS scaling
  afterwards).

#### Step-by-step calibration

1. Open _File > Preferences (Alt + P) > Monitors_.
2. The list shows every detected monitor with its pixel resolution; once calibrated,
   the real width × height in mm is appended in parentheses.
3. Click **Spatial calibration** next to the monitor you want to calibrate. A
   fullscreen window opens on **that** monitor and draws a black background with a
   white horizontal and a white vertical line.
4. Physically measure one of the three references on the screen surface:
   * the **horizontal line**,
   * the **vertical line**, or
   * the screen **diagonal** (corner to corner of the visible glass).
5. At the bottom of the dialog, choose the matching reference in the first dropdown
   (*Horizontal line* / *Vertical line* / *Screen size*), type the measured value, and
   pick the unit (mm, cm, 1/1000 in, in).
6. Click **Apply**. The dialog redraws each line with its computed real length next to
   it; cross-check that the displayed value matches what you measured (within
   ±0.5 mm). Re-measure and re-apply if needed.
7. Close the calibration window. The Monitors page now shows the screen's real size
   and the value is persisted (per monitor) for the next sessions.
8. Activate the result in any 2D viewer with the
   {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}} *Real-world Size* preset
   (toolbar dropdown, context menu *Zoom*, or the image tool panel).


#### Verifying the result

Open any image whose dimensions you know (for example a calibration phantom, a CR/DX
study with a visible ruler, or a printed test pattern displayed full screen) and
switch to {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}} *Real-world Size*.
Use the [length measurement tool](../draw-measure) and compare with the physical
ruler — the values should match within a fraction of a millimeter.

{{% notice warning %}}
If *Real-world Size* still looks wrong after calibration, check that the image itself
has valid **Pixel Spacing** (or Imager Pixel Spacing for projection radiography). Some
secondary captures and screenshots ship without spatial information and cannot be
displayed at real size.
{{% /notice %}}

## Magnifying Lens {{< svg-inline "static/tuto/icon/zoomPan.svg" >}}

The magnifying lens provides detailed inspection of specific image areas. Access it through the zoom toolbar's toggle button.

![Lens example](/tuto/lens-drawing.jpg?classes=shadow&width=700px)
<br>

### Key Features

* Magnify specific regions
* View areas without drawings (`Show Drawings` toggle)
* Compare different Window/Level settings (`Freeze parameters`)
* Compare images from the same series (using `Freeze image`)

### Lens Controls

* **Mouse Wheel**: Adjust lens zoom
* **Double-click**: Match lens zoom to main image
* **Context Menu Options**:
  * *Hide Lens*: disable the lens
  * *Synchronize to parent zoom*: Match lens zoom to main image
  * *Show Drawings*: Toggle overlay visibility
  * *Magnify*: Select zoom level
  * *Image*: Control image and parameter freezing
    * **Freeze Parameters**: Maintains the current image processing settings (like Window/Level, LUT, or filters) while allowing you to scroll through different images. This is useful for comparing the same anatomical area with different processing settings.
    * **Freeze Image**: Captures and holds the current image and its processing parameters, letting you use it as a reference while viewing other images. This is particularly helpful when comparing different slices or time points of a study.
    * **Reset Freeze**: Clears any frozen parameters or images, allowing you to return to the default behavior where the lens reflects the current image and its processing settings.

![Lens with frozen parameters](/tuto/lens-freeze.jpg?classes=shadow&width=700px)
