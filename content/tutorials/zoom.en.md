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
* **Keyboard Shortcuts**:
  * `Ctrl + Plus (+)`: Zoom in
  * `Ctrl + Minus (-)`: Zoom out
  * `Ctrl + Enter`: Reset zoom

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
* To change the zoom interpolation method, see the [Preferences](../dicom-2d-viewer/#preferences) section
{{% /notice %}}

![Zoom tool controls](/tuto/zoom-actions.jpg?classes=shadow&width=700px)
<br>

### Real-world Size Display {{< svg-inline "static/tuto/icon/zoomRealWorld.svg" >}}

To display images at their actual physical size:

1. Open Preferences: _File > Preferences (Alt + P) > Monitors_
2. Click _Spatial calibration_
3. Enter your screen's line length or diagonal length

{{% notice note %}}
Each monitor can have its own calibration setting
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