---
title: DICOM 2D Viewer
weight: 40
description: How to display an image or a stack of images
keywords: [ "viewer 2D", "dicom data", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying DICOM images {{< svg-inline "static/tuto/icon/view2d.svg" >}}</center>

The 2D viewer is the default viewer for any DICOM series that contains images — CT, MR, US, CR / DX, mammography, color photographs, and so on. It handles both single images and stacks (volumetric series), and is the entry point for the more specialized viewers such as [MPR](mpr), the [3D Volume Renderer](dicom-3d-viewer), and the [MIP](mip) projection.

### Open the 2D viewer
The viewer can be opened with {{< svg-inline "static/tuto/icon/view2d.svg" >}} in the toolbar, or by double-clicking a thumbnail (or right-clicking it and choosing **_2D Viewer > Open_**) in the [DICOM Explorer](dicom-explorer/).

![DICOM 2DViewer](/tuto/dicom-viewer2d.jpg?classes=shadow&width=780px)
<br>

The rulers {{% badge style="blue" %}}K{{% /badge %}} display a real-world size whenever Weasis can derive one from the DICOM file. When a small label {{% badge style="blue" %}}M{{% /badge %}} is shown above the calibration, it indicates how that calibration was obtained:

* _At detector:_ projection radiography calibration taken at the detector plane.
* _Magnified:_ projection radiography calibration corrected by the magnification factor (e.g. mammography, as in the screenshot above).
* _Used fiducials:_ calibration derived from fiducials (e.g. a manually placed ruler in the image).
* _At scanner:_ calibration taken from a digitized medium (e.g. film digitizer).

### Toolbars {{% badge style="red" %}}A{{% /badge %}} {#toolbars}

#### Viewer Main Bar

![Main Toolbar](/tuto/main-toolbar.png?classes=shadow)

Choose the action assigned to each of the three mouse buttons and the mouse wheel. Defaults are:

* **Left button** — Window / Level. Can also be changed from the context menu {{% badge style="blue" %}}F{{% /badge %}} or the [keyboard shortcuts](../basics/shortcuts).
* **Right button** — Context Menu.
* **Wheel** — Series Scroll.
* **Middle button** — Pan.

Available actions:

* **Pan** — move the image position. _T_ key to select. _Alt + Arrows_ to pan while another action is selected.
* **[Window / Level](lut)** — change image contrast. _W_ key to select.
* **Series Scroll** — navigate through the images of the current series. _S_ key to select.
* **[Zoom](zoom)** — zoom in / out. _Z_ key to select.
* **Rotation** — rotate the image by a free angle. _R_ key to select.
* **[Measure](draw-measure/#measurement-tools)** — draw a graphic to measure something. _M_ key to select.
* **[Draw](draw-measure/#drawings)** — draw a graphic to annotate. _G_ key to select.
* **Context Menu** — open the context menu. _Q_ key to select.
* **[Crosshair](cursor-3d)** — 3D cursor. _H_ key to select. _Ctrl + click_ or _Ctrl + Shift + click_ adjusts Window / Level without leaving crosshair mode.
* **No Action** — do nothing. _N_ key to select.

{{% notice tip %}}
While dragging, hold _Ctrl_ to accelerate the action and _Ctrl + Shift_ to accelerate more.

The single-key shortcuts above are the **defaults** — most are customizable since {{< badgeC "v4.7.0" >}} in **Preferences > General > Keyboard Shortcuts**. See [Keyboard Shortcuts](../basics/shortcuts).
{{% /notice %}}

* {{< svg-inline "static/tuto/icon/layout.svg" >}} **Default layout** — change the layout of the view. [DICOM Information](tags) and [Histogram](histogram) are special layouts that update automatically as you scroll through the series.
* **Synchronize** — apply the same settings (window/level, scroll, zoom, …) to multiple views simultaneously. Two modes are available: _Default Stack_ (the default — couples series sharing the same Frame of Reference UID) and _Default Tile_ (mosaic display of a single series). A master **Synchronize** checkbox at the top of the drop-down turns synchronization on or off globally without changing the active mode. Each 2D view also exposes its own **auto-sync** {{< svg-inline "static/tuto/icon/synch.svg" >}} and **manual-sync** {{< svg-inline "static/tuto/icon/hand.svg" >}} overlay buttons in its bottom-right corner. See [View Synchronization](synch-view) for the full mechanics, the [per-view controls](synch-view#per-view-sync), and the FoR color-chip system.
* {{< svg-inline "static/tuto/icon/reset.svg" >}} **Reset** — restore the default image rendering (see [Reset](#reset)). _Escape_ key to select.

#### Toolbars available in the DICOM 2D viewer
* [DICOM Import](dicom-import/#from-weasis-menu-or-toolbar)
* [DICOM Export](dicom-export/#exporting)
* [Screenshot](dicom-export/#export-view)
* Viewer Main Bar (see above)
* [Measurement](draw-measure)
* [Zoom](zoom)
* Rotation — rotate the image by 90° clockwise or flip it horizontally. Not visible by default.
* [DICOM Header](tags)
* [Lookup Table](lut)
* Basic 3D — [MPR](mpr) and [MIP](mip) (disabled when the series has fewer than 5 images).
* [3D Viewer](dicom-3d-viewer) (disabled when the series has fewer than 5 images).
* [Cine](#cine)
* [Key Object Selection](build-ko-pr/#key-object-selection-ko)

{{% notice tip %}}
Toolbars can be shown or hidden from the **View** top menu.
{{% /notice %}}

### Viewer tools
The right-side panel groups all the tools tied to the 2D viewer.

The **mini-tool** is always visible; the other panels open by clicking the corresponding vertical button. The normalize button {{< svg-inline "static/tuto/icon/normalize.svg" >}} docks a panel into the main layout — otherwise it opens as a pop-up that can be kept in front with the pin button {{< svg-inline "static/tuto/icon/holdon.svg" >}} (not recommended, as a pinned pop-up hides other panels).

#### Mini-tool {{% badge style="red" %}}B{{% /badge %}} {#mini-tool}
By default the mini-tool scrolls through the images of the selected series (the one surrounded by the orange focus border). The combobox at the top can switch it to control zoom or rotation instead.

#### Display {{% badge style="red" %}}C{{% /badge %}} {#display}

Controls how the image and graphic objects are displayed in the view.

The **Apply to all views** option propagates the chosen display settings to every view in the selected tab. When unchecked, settings apply only to the focused view (orange border).

##### Image
Display options for the image itself. Unchecking **Image** hides the image and leaves only the annotations and graphic objects visible. The other options expose DICOM-specific behavior:

* **DICOM Image Overlay** — apply the [DICOM overlays](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.9.2.html) when checked. The [overlay color](#other) is configurable.
* **Shutter** — apply the [DICOM shutters](https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.7.6.11.html) when checked.
* **Pixel Padding** — apply the [DICOM pixel padding](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.5.html#sect_C.7.5.1.1.2) when checked.

##### DICOM Annotations
Display transformation values and DICOM information directly on the image.

* **Annotations** — DICOM information shown in the image corners:
  * {{% badge style="blue" %}}G{{% /badge %}} Top left — patient information.
  * {{% badge style="blue" %}}H{{% /badge %}} Top right — study information.
  * {{% badge style="blue" %}}I{{% /badge %}} Bottom right — series information (depends on the modality).
  * {{% badge style="blue" %}}J{{% /badge %}} Bottom left — image information and the position of the image in the series.
* **Minimal Annotations** — reduce the number of annotations shown. Press **Space** or _I_ to cycle through the three states (minimal, none, all).
* **Anonymize** — hide identifying information **only inside the views** (not in other parts of the GUI such as the tab title). Combine with the [screenshot tool](dicom-export) when exporting an image.
* **Scale** — display the rulers on the left and bottom of the image {{% badge style="blue" %}}K{{% /badge %}}.
* **Lookup Table** — display the [LUT](lut) on the image {{% badge style="blue" %}}L{{% /badge %}}.
* **Orientation** — display the [orientation of the image](image-orientation) {{% badge style="blue" %}}N{{% /badge %}}.
* **Window / Level** — display the [window and level](lut/#windowing-and-rendering) values {{% badge style="blue" %}}J{{% /badge %}}.
* **Zoom** — display the zoom value {{% badge style="blue" %}}J{{% /badge %}}.
* **Rotation** — display the rotation value {{% badge style="blue" %}}J{{% /badge %}}.
* **Frame Value** — display the frame number {{% badge style="blue" %}}J{{% /badge %}}.
* **Pixel (Value / Position)** — display the pixel value and the cursor position {{% badge style="blue" %}}J{{% /badge %}}.

##### Drawings
Check / uncheck to show or hide the graphic objects (see [Draw & Measure](draw-measure)).

#### Image Tools {{% badge style="red" %}}D{{% /badge %}} {#image-tools}
**Image Tools** groups every control that affects how the image is rendered.

##### [Windowing and Rendering](lut/)

##### Transform
Zoom, rotate, and flip the image. Zoom and rotation can also be driven from the [mini-tool](#mini-tool) or the [mouse actions](#toolbars).

##### Cine
The **Cine start** button {{< svg-inline "static/tuto/icon/execute.svg" >}} plays the series at a fixed speed (frames per second). The default speed is taken from the DICOM file when present. Cine options are also accessible from the context menu.

* Click **Cine stop** {{< svg-inline "static/tuto/icon/suspend.svg" >}} to end the animation.
* Click the **Loop / Sweep** toggle {{< svg-inline "static/tuto/icon/loop.svg" >}} to switch between looping and sweeping playback.

{{% notice note %}}
When cine is active, every series currently synchronized with the playing series is animated too. Selecting another series keeps the cine running on it until the **Cine stop** button is pressed.

For series with a variable frame rate, the playback speed is adjusted automatically, so a value entered manually is not preserved.
{{% /notice %}}

{{% notice tip %}}
A dedicated **Cine** toolbar is also available — hidden by default; enable it from the **View** menu.
{{% /notice %}}

##### Reset
Returns the image to its default rendering, either for every parameter or for a specific one. Also available from the toolbar button {{< svg-inline "static/tuto/icon/reset.svg" >}} and from the context menu.

#### [Draw & Measure](draw-measure) {{% badge style="red" %}}E{{% /badge %}} {#draw-measure}

#### Other specific tools
* [DICOM RT tools](dicom-rt) — for radiotherapy studies (RTSTRUCT, RTPLAN, RTDOSE).
* [DICOM Segmentation](dicom-segmentation) — for pixel-based SEG overlays (binary, fractional, label-map).

### Preferences
From the menu **_File > Preferences > Viewer > 2D Viewer_**.

#### Mouse Action Sensitivity
Adjust how strongly a mouse drag translates into action for: _Window_, _Level_, _Zoom_, _Rotation_, and _Series Scroll_.

#### Zoom
Zoom interpolation controls how new pixels are computed when the image is zoomed in or out:

* **Nearest neighbor** — the simplest method: extends the nearest pixel value as-is.
* **Bilinear** — averages the four neighboring pixels. Slightly sharper than nearest neighbor, slightly slower.
* **Bicubic** — uses a 16-point kernel. Sharper than bilinear, but the slowest of the four.
* **Lanczos** — uses a sinc kernel; produces the sharpest results, with performance between bilinear and bicubic.

The default is **Bilinear**. **Nearest neighbor** is the fastest option but produces aliasing artifacts.

#### Other
* **Apply Window / Level on color images** — when checked, the window / level is applied to the RGB channels. Unchecked, window / level has no effect on color images.
* **Inverse level direction** — when checked, the level direction with mouse drag is inverted (dragging down increases brightness), matching the [Basic Image Review profile](https://wiki.ihe.net/index.php?title=Basic_Image_Review). Unchecked, dragging down decreases brightness.
* **Apply by default the most recent Presentation State** — when checked, the most recent [Presentation State](build-ko-pr/#presentation-state-pr-or-gsps) object is applied automatically. Otherwise it has to be selected manually via {{< svg-inline "static/tuto/icon/imagePresentation.svg" >}}.
* **Overlay color** — color and opacity of the DICOM overlay. The default is white; the opacity is the transparency / alpha slider of the color picker.