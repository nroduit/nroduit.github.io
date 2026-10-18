---
title: "Measurements and Annotations"
weight: 205
description: "Draw and measure on images: the drawing tools, the values each one reports, and the preferences that control how they look and behave."
linkTitle: "Draw & Measure"
keywords: [ "dicom measurement", "annotate dicom", "draw on dicom image", "distance measurement", "angle measurement", "roi" ]
---

## <center>What each tool draws, and what it reports {{< svg-inline "static/tuto/icon/measure.svg" >}}</center>

The **Draw & Measure** panel lets you annotate and measure on DICOM and standard images: distances, angles, areas, regions of interest, free-hand shapes and text labels.

- Lengths and areas use the image's spatial [calibration](calibration) when available.
- Closed shapes also report statistics of the pixels they enclose.

![Draw & Measure](/tuto/measure.jpg?classes=shadow&width=100%)
<br>

Where the results are persisted depends on the image type:

* **For DICOM images** — saved into a [DICOM Presentation State](build-ko-pr/#presentation-state-pr-or-gsps) (GSPS) object that travels with the study.
* **For standard images** — saved into an XML file in the same directory as the image (when the image is exported in a non-DICOM format). The XML file is loaded automatically the next time the image is opened in the 2D viewer.


### Draw & Measure Panel
Click {{< svg-inline "static/tuto/icon/normalize.svg" >}} on the vertical button {{< svg-inline "static/tuto/icon/measure.svg" >}} to dock the panel on the right side of the viewer. The panel is divided into four parts:

- [Measurement tools](#measurement-tools) {{% badge style="red" %}}A{{% /badge %}}
- [Drawings](#drawings) {{% badge style="red" %}}B{{% /badge %}}
- [Graphic Options](#graphic-options) {{% badge style="red" %}}C{{% /badge %}}
- [Selected Measurement](#selected-measurement) {{% badge style="red" %}}D{{% /badge %}}

#### Measurement tools {{% badge style="red" %}}A{{% /badge %}} {#measurement-tools}
Click a measurement tool, then draw on the image. The tool you pick also becomes the action of the [left mouse button](dicom-2d-viewer/#toolbars).

The first button is the **selection** tool: it selects, resizes and moves existing graphics.

##### Working with selected graphics {#selected-graphics}

Right-click a selection to change its properties (color, line width…) or to edit it:

| Action | Shortcut |
|---|---|
| **Cut** | **Ctrl + X** |
| **Copy** | **Ctrl + C** |
| **Paste Drawings** — centered on the cursor | **Ctrl + V** |
| **Paste in place** — at the original position | **Ctrl + Shift + V** |
| **Duplicate** | **Ctrl + Shift + D** |
| **To Front** / **To Back** — change the stacking order | |
| Delete | **Delete** key or {{< svg-inline "static/tuto/icon/selectionDelete.svg" >}} |

- On macOS, use **Cmd** instead of **Ctrl**.
- A graphic pasted outside the image is reported by a short notice on the view {{< since "4.8.0" >}}.
- A confirmation dialog is shown before deleting. Turn it off with its *Don't ask me again* checkbox or in the **Draw & Measure** [preferences](#preferences).
- Every tool of the two palettes can get its own key in **Preferences > General > Keyboard Shortcuts** {{< since "4.8.0" >}}. See also the full list of [graphic shortcuts](../basics/shortcuts/#graphics).

{{% callout note %}}
A segment can be drawn in two equivalent ways:

1. **Click + Drag** — click, drag to draw, release.
2. **Click > Release > Drag** — click to set the start point, release, drag to draw, click again to set the end point.

To keep the same tool active for several draws in a row, uncheck **Draw only once** (see [Graphic Options](#graphic-options)).
{{% /callout %}}

##### Polylines and polygons {#polylines}

- **Finish** an open polyline with a double-click.
- **Close** it into a polygon by clicking the first point. When the cursor is on that point, a ring and a dashed closing segment show that the next click closes the path.
- While drawing, **Escape** cancels the path and **Backspace** removes the last vertex. The context menu offers **Stop drawing** and **Cancel the drawing in progress**.

To edit a finished path:

- Right-click a vertex for the add / delete actions on that point.
- Every segment has a handle on its middle: click it to insert a vertex there, or drag it to insert one and place it {{< since "4.8.0" >}}.
- **Alt + click** a vertex to remove it.
- **Alt + drag** from the first or last point of an open path to continue drawing from that end.
- The context menu also offers **Insert a point here**, **Remove this point**, **Continue drawing** and **Simplify…**. **Simplify…** thins a dense trace, with a tolerance slider in image pixels {{< since "4.8.0" >}}.

There is no separate polygon button any more {{< since "4.8.0" >}}. On a finished path, **Close path** / **Open path** in the context menu switches between the two, keeping the shape's style and position. A freehand region can be opened the same way into a traced line.

##### Rectangles and ellipses {#rectangles-ellipses}

- They can be drawn at any angle. The external control points rotate and resize the shape; the single control point on the opposite side only resizes it.
- Hold **Shift** while dragging to draw a classic upright rectangle or ellipse, from corner to corner in one go {{< since "4.8.0" >}}.
- **Shift** also keeps a line, arrow, ruler or parallel line horizontal or vertical {{< since "4.8.0" >}}.
- If you mostly draw upright shapes, the [preferences](#preferences) can swap the two: a plain drag then draws the upright shape, and **Shift** the oblique one.

##### New measurement tools {#new-tools}

New tools {{< since "4.8.0" >}}:

* **Circle** — the quickest way to read pixel values (HU, SUV, signal).
  - Press on the center, drag to the radius and release, in one gesture.
  - A simple **click** drops a circle of a default radius (5 mm, see the [preferences](#preferences)).
  - The center control point moves the circle; the one on its edge resizes it.
  - The three-point circle remains the tool to fit a circle onto a round structure. Both now show a small cross on their center.
* **Bidirectional** — draw the long axis; the short axis is placed automatically, perpendicular to it, and its two ends can then be moved. The table reports both lengths and their ratio, as used for RECIST-style lesion measurement.
* **Parallel lines** now also report the length of each line and their **ratio** (shorter over longer), shown on the image by default.
* **Cardiothoracic ratio (CTR)** — a dedicated tool for the frontal chest radiograph, see [below](#cardiothoracic-ratio).
* **Freehand** — trace a path in one drag.
  - Release on the start point (a ring appears on it) to close it into a region, with area and pixel statistics.
  - Release elsewhere to keep an open line, with its length.
  - The trace is simplified so it stays editable.
  - Hold **Shift** while tracing to make the path magnetic: it follows the strongest edge of the image between the points you pass. This makes outlining a lesion or an organ border much easier.

**Calibration** needs no tool of its own. Hold **Ctrl** (**Cmd** on macOS) while drawing a **line** over an object of known length: the calibration dialog opens when the line is finished. The same dialog is available:

- in the context menu of any line (**Change Spatial Calibration**);
- from the **Calibrate…** button shown under the table when a line is selected.

Its **Restore original** button brings back the calibration of the file or of the Presentation State. See [spatial calibration](calibration).

##### Cardiothoracic ratio (CTR) {#cardiothoracic-ratio}

The CTR is the maximal transverse diameter of the heart divided by the maximal internal diameter of the thorax, measured on a **PA** chest radiograph {{< since "4.8.0" >}}.

The two heart borders are rarely widest at the same height. So the tool does not ask for horizontal lines: it records where each border is and measures the distances **across the midline**.

1. Pick **Cardiothoracic ratio** in the measurement tools (it is part of the *Radiography* [profile](#tool-profiles)).
2. Draw a first stroke from one heart border to the other, each end at the height where that border is widest. The stroke does not need to be horizontal.
3. Draw a second stroke between the inner rib margins at the widest level of the thorax (usually at the right hemidiaphragm).
4. Read the **CTR** label. On a PA view a value above 0.50 suggests an enlarged cardiac silhouette; the ratio is never shown as a percentage.

Adjusting the result:

- The dashed **midline** is placed upright through the middle of the thorax. If the patient is rotated, drag one of its ends to align it with the spinous processes: the widths are always measured perpendicular to it.
- Each of the four border points can be moved on its own afterwards.

The table also gives:

- the cardiac and thoracic widths;
- when the heart borders lie on either side of the midline, the distances from the midline to the right and to the left heart border.

The [tool panel](#tool-panel) shows the current step, and warns on an **AP** view, where the heart is magnified and the 0.50 threshold does not apply.

#### Drawings {{% badge style="red" %}}B{{% /badge %}} {#drawings}
The drawing buttons add **text** and **graphic** annotations. These objects are purely decorative: they do not display measurement values and do not appear in the [Selected Measurement](#selected-measurement) table.

New drawings {{< since "4.8.0" >}}:

* **Arrow** — the head is at the second point.
* **Ruler** — a graduated bar. On a calibrated image it has one tick per centimeter, every fifth tick longer; otherwise one tick per fifty pixels.
* **Freehand** pencil.

#### Tool profiles {#tool-profiles}

The **Profile** list at the top of the panel chooses which tools the two palettes show, with their defaults {{< since "4.8.0" >}}.

**Automatic (by modality)** picks a profile from the modality of the selected series:

| Profile | Series | Tools |
|---|---|---|
| **Cross-sectional (CT, MR, PET)** | CT, MR, PT, NM | region tools and pixel statistics |
| **Radiography (CR, DX)** | CR, DX, RF, XA | angles, Cobb, cardiothoracic ratio; no pixel statistics |
| **Ultrasound** | US | distances and traced areas; no pixel statistics |
| **Default** | any other | every tool |

How profiles combine with your settings:

- A profile is laid over your own settings. What it does not set shows your choice again as soon as another profile takes over.
- A profile never replaces the preferences saved for you.
- Choosing a profile by name keeps it, whatever the series.

Where profiles come from:

- Your own profiles are created in the [preferences](#preferences).
- An administrator can ship profiles for a site in `config/measurementProfiles.json` of the resources package (see [Configuration documents](../basics/customize/preferences/#configuration-documents)). They are marked *(site)* in the list and are read-only.

#### Tool panel {#tool-panel}

Some tools need more than an icon. A collapsible section opens between the tool buttons and the table {{< since "4.8.0" >}} when such a tool is selected in the palette, or when one of its graphics is selected on the image.

- The **cardiothoracic ratio** tool shows its drawing steps there.
- The **Intensity profile** section, below it, plots the pixel values along any selected open measurement: a line, or a polyline through each of its vertices. It follows the graphic as you move it.
- Move the mouse over the curve to read a sample — its distance from the start of the path and its value. A small crosshair marks the corresponding pixel on the image.


#### Graphic Options {{% badge style="red" %}}C{{% /badge %}} {#graphic-options}
* **Line color** — default color for new graphics (default: cyan {{< since "4.8.0" >}}, yellow before). The transparency / alpha slider in the color picker controls opacity. A dark color triggers a reminder that it will be hard to see on the dark areas of an image.
* **Line width** — default line width.
* **Draw only once** — when checked, the tool reverts to the selection mode after each draw. Uncheck to keep the same tool active for successive draws.
* **Pixel statistics** — compute and display statistics of the pixel values inside the shape. Only meaningful for closed shapes (rectangle, ellipse, circle, closed polyline or freehand).
* **Unit** — unit of the image's spatial calibration. When the image has no calibration, the unit falls back to pixels. See [How to change the spatial calibration](calibration).
* **More options** — opens the Draw & Measure [preferences](#preferences) for the deeper display options.

{{% callout tip %}}
Graphics can be shown or hidden from the **Graphics** group of the [_Display_ panel](dicom-2d-viewer/#display), which has one check box per layer {{< since "4.8.0" >}}: **Measurements**, **Drawings**, **Annotations**, **DICOM PR** and **DICOM SR**.
{{% /callout %}}

#### Selected Measurement {{% badge style="red" %}}D{{% /badge %}} {#selected-measurement}
The graphic {{% badge style="red" %}}E{{% /badge %}} currently selected on the image is summarized in this table. The reported properties depend on the measurement type. Units are shown in square brackets when present (see the [calibration type](dicom-2d-viewer/#open-the-2d-viewer) at {{% badge style="blue" %}}M{{% /badge %}}).

{{% callout note %}}
For **polygons**, length, width, and orientation are computed with the **OMBB (Oriented Minimum Bounding Box)** method — a tighter bounding box than the axis-aligned one, giving a more accurate approximation of the polygon's real dimensions.
{{% /callout %}}

When **Pixel statistics** is checked, the table also reports descriptors computed from the pixels enclosed by the (closed) shape:

* **Pixels** — number of pixels inside the shape.
* **Min** — minimum modality value.
* **Max** — maximum modality value.
* **Median** — median modality value.
* **Mean** — mean modality value.
* **StDev** — standard deviation; a measure of how dispersed the values are.
* **Skewness** — asymmetry of the value distribution.
* **Kurtosis** — "tailedness" of the value distribution.
* **Sum** — sum of the modality values, i.e. the total counts of a region on a nuclear medicine image {{< since "4.8.0" >}}.

{{% callout note %}}
**SUV** (Standardized Uptake Value) measurements are added to the table on **PET** images when the required metadata is present (patient weight, decay correction, radiopharmaceutical dose, acquisition time, …). Min / Max / Mean SUV are computed with the body-weight method (**SUVbw**), following the [vendor-neutral QIBA definition](https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)).
{{% /callout %}}

{{% callout tip %}}
The table can be exported by **copy / paste**. The copied values use the full numerical precision, not the rounded values shown on screen. Right-click the table {{< since "4.8.0" >}} for:

- **Copy value** — one row;
- **Copy table** — every row with its header, as tab-separated text ready for a spreadsheet.
{{% /callout %}}

Under the table, a short note {{< since "4.8.0" >}} gives two things worth a look before trusting a length:

- where the pixel size comes from, when the image tells it — for instance *At Detector* or *Magnified* on a projection radiograph, *Modified by user* after a manual [calibration](calibration);
- the slice thickness.

A **line** also reports its horizontal and vertical extent, which gives a height difference directly.

{{% callout note %}}
In the [MPR viewer](mpr), a measurement drawn on one plane stays attached to its position in the patient {{< since "4.8.0" >}}. It reappears when you come back to that plane, and small marks on the other two planes show where it crosses them.
{{% /callout %}}

### Preferences {#preferences}
From the main menu **_File > Preferences > Draw & Measure_**.

* **Ask for confirmation before deleting a drawing** — when checked (default), a confirmation dialog is shown before deleting the selected graphics. Unchecking it (or ticking *Don't ask me again* in that dialog) deletes them without confirmation {{< since "4.7.1" >}}.
* **Show a handle on the middle of each segment** — when checked (default), polylines, polygons and freehand paths show a handle on the middle of every segment. Click it to insert a vertex there, drag it to insert one and place it {{< since "4.8.0" >}}.
* **Hide the handles closer than (handle sizes)** — a midpoint handle is not drawn on a segment shorter than this many handle sizes on screen (default: 2), so it never covers the vertices of a dense trace {{< since "4.8.0" >}}.
* **Paste the drawings** — where **Ctrl + V** puts the pasted graphics: **At the cursor position** (default) or **At the original position**. **Ctrl + Shift + V** always pastes at the original position {{< since "4.8.0" >}}.

#### Drawings
Default graphic properties applied when drawing new objects {{< since "4.3.0" >}}.

* **Line color** — default color (default: cyan {{< since "4.8.0" >}}). The transparency / alpha slider in the color picker controls opacity.
  - Why cyan: yellow, the former default, is close to white on a bright radiograph and blends into the hot, PET and Doppler color maps. Cyan stays apart from all of them.
  - Upgrade: on the first start of 4.8.0, a yellow line color becomes cyan, whether it was the default or chosen, because earlier versions do not record the difference. Any other color you picked is kept, and so is yellow chosen again after the upgrade. Graphics already saved keep their own color.
* **Dark outline** — draws a thin dark halo under the lines of measurements and drawings (default: on) {{< since "4.8.0" >}}.
  - No line color is visible on every image. The halo gives each line its own dark surround, so it stays readable over bone, air, a bright radiograph or a color image.
  - Graphics coming from a DICOM Presentation State are shown as their author styled them.
  - When saved to a Presentation State, the halo is written as the standard *outlined* shadow style, so other viewers can render it too.
* **Line width** — default line width.
* **Fill shape** — when checked, the interior of the shape is filled with the line color.
* **Fill opacity** — opacity of the interior, relative to the line color's opacity. Default: 100 %. Example: line opacity 80 % × fill opacity 20 % → perceived interior opacity 16 %.
* **Upright by drag (rectangle and ellipse)** — when checked, a plain drag draws the classic upright shape from corner to corner and **Shift** the oblique one; unchecked (default) it is the reverse {{< since "4.8.0" >}}.
* **Circle radius on click** — the radius of the circle dropped by a simple click, without dragging (default: 5 mm) {{< since "4.8.0" >}}. It is the quickest way to read the mean value of a small region. Normally, the circle tool is drawn by pressing on the center and dragging to the radius. On an image without pixel size, the circle has a fixed size on screen.

#### Tool profiles
Manage the profiles of the [profile list](#tool-profiles) {{< since "4.8.0" >}}.

* **Profile bar** — choose the profile to edit.
  - **New…** captures the palettes, defaults, statistics and labels as they are now.
  - **Duplicate** copies any profile.
  - The **⋯** button deletes one of your profiles, and imports or exports profiles as JSON files — for example to share a practice's palette.
  - Built-in profiles, marked *(built-in)* in the list, are read-only: duplicate one to change it.
* **Name and modalities** — the modalities the profile applies to in *Automatic* mode, separated by commas (`CT, MR, PT`). When several profiles name the same modality:
  - one of yours wins over a site profile, which wins over a built-in one;
  - between two of yours, the first one in your profile file wins.
* **Tools** — the two palettes side by side. Check the tools to show, and order them with **Up** / **Down**, **Alt + arrow** or by dragging a row. **All tools** keeps every tool, including the ones a plugin adds later.
* **New graphics** — three blocks, as on the *Drawings* page: *Line* (color, width), *Closed shape* (fill and its opacity, upright by drag) and *Measured values* (decimals).
* **Statistics and labels** — the pixel statistics to compute and, for each tool, the measurements shown on the image.
  - *Set the labels of this tool* unchecked leaves that tool as it is.
  - **Copy current** takes the labels of every tool from what is displayed now.

Each section has a *Keep the current settings* choice, so a profile only changes what it is meant to change.

#### Labels on image
Display options for the labels attached to measurement graphics.

* **Font type** — default font size for the on-image labels (default: _Small semibold_). The size is not absolute — it adjusts automatically with the [interface scale factor](theme/#how-to-scale-the-user-interface).
* **Decimals of the measured values** — applies to the labels on the image and to the table {{< since "4.8.0" >}}.
  - **Automatic** (default) shows each value with the precision it can honestly have (see the table below).
  - **0 to 4** forces that number of decimals instead.
  - Thousands are never grouped, so a value cannot be misread between locales.
  - Copied values always keep the full precision.
  - The statistics tables of the [histogram](histogram) and of the segmentation regions follow the same rule, and offer the same **Copy value** / **Copy table** menu.
* **Geometric measurement** — which geometric measurements are displayed on the image for each graphic type.
* **Pixel statistics** — which pixel statistics are displayed on the image for closed shapes (rectangle, ellipse, circle, closed polyline or freehand).

Precision in **Automatic** mode:

| Value | Decimals |
|---|---|
| Length | one digit finer than the pixel size — 12.3 mm on a 0.7 mm pixel, 12.35 mm on a 0.05 mm mammography pixel; one more digit when the unit is cm |
| Area | one digit less than a length |
| Angle | one |
| Ratio | always two (0.50) |
| Pixel count | none |
| Hounsfield values | none; one for their mean or standard deviation |
| Other values, such as SUV | four significant digits |
