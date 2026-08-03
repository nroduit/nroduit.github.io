---
title: DICOM 3D Viewer
weight: 60
description: How to display volume data
keywords: [ "viewer 3D", "volume rendering", "ray casting", "3D rendering", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying volume data {{< svg-inline "static/tuto/icon/volume.svg" >}}</center>

The 3D viewer reconstructs a CT, MR, PET, or other volumetric series into an interactive volume rendering that can be rotated, sliced, recolored, and lit in real time. Typical uses include reviewing CT angiography, inspecting bone or vascular anatomy, surgical-planning views, and quickly conveying findings to colleagues or patients. Available since {{% badge title="Version" %}}4.1.0{{% /badge %}}, with major rendering and synchronization improvements in {{% badge title="Version" %}}4.7.0{{% /badge %}}.

Internally, the volume is rendered on the graphics card using a [ray-casting algorithm](https://en.wikipedia.org/wiki/Volume_ray_casting) implemented in GLSL shaders, so a modern GPU is required (see [Requirements](#requirements)) but no extra installation step is necessary.

### Requirements {#requirements}
The graphics-card capabilities used by Weasis are reported under **OpenGL Support** in **_File > Preferences > Viewer > 3D Viewer_**:

* **Driver version** — requires OpenGL **3.3+** since {{% badge title="Version" %}}4.7.0{{% /badge %}}. Two rendering backends are used depending on the available OpenGL version:
  * **OpenGL 4.3+** — uses a **Compute Shader** for optimal performance.
  * **OpenGL 3.3 – 4.2** — uses an **FBO-based Fragment Shader** fallback (fully functional, but may be less performant than the Compute Shader path). macOS is capped at OpenGL 4.1 and therefore always uses this path.
* **Max 3D texture dimension length** — the upper limit, in voxels, of any X / Y / Z dimension of the volume.
* Any other entry shown in **red** indicates a non-optimal configuration. The viewer often still works — see [how to limit the size of 3D textures](#3d-viewer) if performance becomes an issue.

{{% notice note %}}
If Weasis reports a graphics card that is not the one you expected, the choice is made by the graphics driver and the operating system, not by Weasis. OpenGL itself has no API to select a specific card; consult your OS's GPU-selection settings for the application.
{{% /notice %}}

### Open the 3D viewer
Open the viewer by clicking {{< svg-inline "static/tuto/icon/volume.svg" >}} in the toolbar of a series view, by double-clicking the series thumbnail, or by right-clicking the thumbnail in the [DICOM Explorer](dicom-explorer) and choosing the 3D viewer.

{{% notice tip %}}
If the series is a **multi-phase 4D acquisition** (e.g. a cardiac CT with several temporal phases), Weasis automatically splits it into individual phase sub-series when 2–7 phases are detected. For series with 8 or more phases, a confirmation dialog is shown first. Open any resulting phase sub-series to render it in the 3D viewer. See [4D Series Sub-Series Splitting](dicom-explorer#4d-splitting) for details.
{{% /notice %}}

Try it on a volume dataset (Medical Demos from data.kitware.com)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/3d/head-neck.xml"
{{< /launch >}}

![3D View](/tuto/view-3d.jpg?classes=shadow&width=100%)
<br>

The same [patient orientation axes](mpr#orientation-axes) as the MPR views are drawn in the 3D view since {{% badge title="Version" %}}4.7.0{{% /badge %}}.

{{% notice info %}}
DICOM SEG segmentations linked to the series are rendered in the 3D viewer too — see [Segmentation overlay in the 3D Volume Renderer](dicom-segmentation#segmentation-overlay-in-the-3d-volume-renderer).
{{% /notice %}}

### Toolbar {{% badge style="red" %}}A{{% /badge %}} {#toolbar}
Actions in the toolbar:

* {{< svg-inline "static/tuto/icon/loadVolume.svg" >}} **Reload volume** — fully reloads the volume from the source series.
* {{< svg-inline "static/tuto/icon/orthographic.svg" >}} **Orthographic / Perspective projection** — toggles between orthographic projection (parallel lines preserved, no foreshortening — useful for measurements) and perspective projection (depth cues, more natural-looking view). Perspective is the default.
* {{< svg-inline "static/tuto/icon/volumeCut.svg" >}} **MPR Crosshair Cut** — opens the [cut mode](#mpr-cut) to interactively clip the rendered volume along the anatomical planes defined by the MPR crosshair.
* {{< svg-inline "static/tuto/icon/volumeSettings.svg" >}} **3D preferences** — opens the [Preferences](#preferences).

Other toolbar buttons (LUT, reset, layout, synchronize…) are documented in the sections below.

### MPR Crosshair Cut Mode {#mpr-cut}

Since {{% badge title="Version" %}}4.7.0{{% /badge %}} the 3D viewer can display an MPR crosshair overlay synchronized with the [MPR viewer](mpr#crosshair-colors), allowing you to clip the rendered volume along the anatomical planes defined by the crosshair position and orientation. The crosshair position and rotation stay synchronized in real time between the 2D MPR planes and the 3D rendering.

#### Recommended workflow

1. Open the [MPR viewer](mpr) from a series view.
2. In the MPR toolbar, click {{< svg-inline "static/tuto/icon/volume.svg" >}} — this splits the current tab into a side-by-side layout with the MPR views on one side and the 3D volume rendering on the other.
3. In the 3D view, activate a cut mode using the toolbar button {{< svg-inline "static/tuto/icon/volumeCut.svg" >}} or by right-clicking and selecting **MPR Crosshair Cut**.

#### Alternative workflow

Open the 3D viewer first, then activate a cut mode from the toolbar {{< svg-inline "static/tuto/icon/volumeCut.svg" >}} or the right-click menu. The MPR viewer opens automatically for the same series, but in a separate tab. To obtain the side-by-side layout, drag the MPR tab and [dock](docking) it next to the 3D view using the docking handles.

#### Cut modes

* **No cut** — no clipping; the full volume is rendered.
* **18 directional modes** — clip the volume in halves, quarters, or eighths relative to the MPR crosshair position, along each anatomical axis (Left / Right, Anterior / Posterior, Superior / Inferior).

The crosshair overlay uses the same LPS axis color coding as the MPR viewer.

### 3D View Synchronization {#3d-synch}

Since {{% badge title="Version" %}}4.7.0{{% /badge %}} the 3D viewer can host multiple side-by-side views of the same volume and keep them coordinated. Because every 3D view in the container shows the **same volume**, the auto-sync button {{< svg-inline "static/tuto/icon/synch.svg" >}} is always visible. A single synchronization profile bundles a per-action toggle list with camera-level actions enabled by default and photometric / rendering actions left opt-in.

#### Toolbar "Synchronize" checkbox

The {{< svg-inline "static/tuto/icon/synch.svg" >}} **Synchronize** checkbox in the toolbar drives the **global on/off** state for the 3D container. It defaults to ON. Toggling it propagates the new state to every per-view auto-sync button on the next refresh.

#### Per-view auto-sync button {{< svg-inline "static/tuto/icon/synch.svg" >}} {#3d-auto-sync-button}

When the layout has **two or more views**, a small auto-sync button appears in the bottom-right corner of each view. Its tint reflects the per-view state — *red* when sync is OFF for the view, *green* when ON. Clicking the button opens a popup with:

- **Synchronize this view** — master on/off toggle for auto-sync on this view (also mirrored into the toolbar **Synchronize** checkbox so the toolbar state always reflects the active view).
- **Per-action toggles** — independent checkboxes that decide which actions this view propagates to (and receives from) the other 3D views. The popup stays open while you flip several options.
- **Apply to all views** — copies this view's effective per-action map to every other 3D view in the container. Unlike the 2D variant of this entry, no FoR filtering is applied because all 3D views share the same volume.

#### Right-click "Synchronize" submenu

The view's right-click context menu also exposes a **Synchronize** submenu with the same per-action toggles and the same **Apply to all views** entry, useful when you want to adjust the sync map without first enabling/disabling the master toggle.

#### Per-action defaults

| Group       | Action                                       | Default |
|-------------|----------------------------------------------|---------|
| Camera      | Pan                                          | ON      |
| Camera      | Zoom                                         | ON      |
| Camera      | Rotation (slider rotation + axis selection)  | ON      |
| Photometric | Window / Level                               | OFF     |
| Photometric | Preset                                       | OFF     |
| Photometric | LUT Shape                                    | OFF     |
| Photometric | Invert LUT                                   | OFF     |
| Photometric | LUT                                          | OFF     |
| Rendering   | Rendering Type                               | OFF     |
| Rendering   | Volume Opacity                               | OFF     |
| Rendering   | Volume Shading                               | OFF     |
| Rendering   | Orthographic projection                      | OFF     |
| Rendering   | MPR Crosshair Cut                            | OFF     |

Camera-level actions are on by default because keeping multiple 3D views framed identically is the common workflow when comparing rendering types or LUT presets side by side. Photometric and rendering actions are opt-in because the typical reason to open a second 3D view is to **diverge** on those settings (e.g. one view in Composite with a soft-tissue LUT, the other in MIP).

{{% notice note %}}
The view you are actively interacting with always applies its own changes locally, even when the corresponding action is unchecked in its sync map. Only **other** views gate on the per-action toggle. This keeps sliders and mouse drags responsive while letting you decide which actions propagate to the rest of the container.
{{% /notice %}}

### 3D Rendering Tools
This tab groups every control that affects how the volume is rendered. To return to the original settings, click the toolbar button {{< svg-inline "static/tuto/icon/reset.svg" >}} or pick **Reset** from the context menu.

#### Windowing and Rendering {{% badge style="red" %}}B{{% /badge %}} {#windowing}
Some of the options below are also accessible from the toolbar and the right-click menu.

* **Window** — width of the voxel-value range mapped to the displayed value range.
* **Level** — center of the range defined by Window.
* **LUT Shape** — transfer function applied between input and display values: linear, sigmoid, or logarithmic. Default is linear.
* {{< svg-inline "static/tuto/icon/lut.svg" >}} **LUT** — a 3D Lookup Table that maps grayscale voxel values to color, opacity, and lighting for visualization. Picking a LUT from the toolbar or the right-click menu is usually easier: LUTs there are ordered by modality and shown with a preview. Custom LUTs can be created and modified with the [Volume LUT Editor](#lut-editor).
* {{< svg-inline "static/tuto/icon/inverseLut.svg" >}} **Invert LUT** — flips the LUT direction.


#### Volume Rendering {{% badge style="red" %}}C{{% /badge %}} {#volume-rendering}
Controls for the rendering algorithm, quality, transparency, lighting, and shading.

* **Type** — defines the rendering algorithm applied to the volume:
  * **Composite** — classic volume rendering. Each voxel contributes color and opacity along the ray, blended front-to-back to produce the final image.
  * **MIP Max** — Maximum Intensity Projection. Keeps the highest-intensity voxel encountered along each ray. Useful for highlighting bright structures such as contrast-enhanced vessels or bones.
  * **MinIP** — Minimum Intensity Projection. Keeps the lowest-intensity voxel along each ray. Useful for visualizing air-filled structures such as airways.
  * **MIP Mean** — Mean Intensity Projection. Averages intensities along each ray, producing a smoother representation of the volume.
  * **Iso Surface** — renders a 3D surface at a given intensity threshold, representing structures of a uniform density (e.g. bone segmentation).
* **Z-axis sampling** — distance between successive samples along each ray. Smaller values capture more detail at the cost of compute time; the default is derived from the volume size.
* **Opacity** — global opacity factor for the voxels. Can be pushed above 100 % to compensate for the lower-than-100 % values defined by some Volume LUTs.
* **Shading** — enables shading on the rendered surface. The default is taken from the Volume LUT; the additional options let you override the inherited lighting settings.

#### Transform {{% badge style="red" %}}D{{% /badge %}} {#transform}
Zoom the volume and rotate it around the three patient axes:

* **Zoom slider** — scales the rendering.
* **Rotation sliders** — rotate around the Left / Right, Anterior / Posterior, and Superior / Inferior axes (LPS coordinate system).

### Volume LUT Editor {#lut-editor}

Since {{% badge title="Version" %}}4.7.2{{% /badge %}} custom Volume LUTs can be created and edited directly in the 3D viewer. A Volume LUT (also called a *preset*) defines, for each voxel intensity, the color, the opacity, and the lighting coefficients used by the volume rendering.

Open the editor from the LUT list in the toolbar {{< svg-inline "static/tuto/icon/lut.svg" >}} or in the right-click menu: the **Edit Volume LUT…** entry is located at the bottom of the list.

{{% annotate src="/tuto/3d-lut-editor.png" viewbox="0 0 2552 1520" alt="Volume LUT Editor dialog with the preset list, preset properties and transfer function" class="shadow" %}}
A | | 645,270 | 60
B | | 1400,150 | 60
C | | 1020,980 | 60
{{% /annotate %}}
<br>

#### Preset list {{% badge style="red" %}}A{{% /badge %}} {#preset-list}

The left side of the dialog lists all the available presets. A **search field** and two filters (**modality** and **All / Editable / Built-in**) help to locate a preset in a long list.

Built-in presets cannot be modified. Use the buttons below the list to create an editable one:

* **New** — creates an empty custom preset.
* **Copy** — duplicates the selected preset. Copying a built-in preset is the easiest way to start from a working configuration and adjust it.
* **Delete** — removes the selected custom preset (with confirmation).

#### Preset properties {{% badge style="red" %}}B{{% /badge %}} {#preset-properties}

* **Name** — the name displayed in the LUT lists (required).
* **Modality** — the modality group under which the preset is listed (e.g. CT, MR, PET). Choose **Default** to make it available for all modalities.
* **Default** — makes this preset the one selected automatically when a volume of that modality is opened.
* **Shading** and **Specular Power** — default lighting behavior of the preset, which can still be overridden afterward from the [Volume Rendering](#volume-rendering) panel.

#### Transfer function {{% badge style="red" %}}C{{% /badge %}} {#transfer-function}

A preset contains one or more **groups**, and each group is a list of **points** placed along the voxel-intensity axis. Every point defines an opacity, a color, and the **Ambient / Diffuse / Specular** lighting coefficients; values between two points are interpolated linearly.

The points of the selected group can be edited in two ways:

* **Graphically**, in the transfer-function graph: **double-click** on the curve to add a point, **drag** a point to change its intensity and opacity, **double-click a point** to pick its color, and press **Delete** to remove the selected point.
* **Numerically**, in the point table (**Intensity**, **Opacity**, **Color**, **Specular**, **Ambient**, **Diffuse** columns), together with the **Add Point** / **Remove Point** buttons.

The resulting color bar is previewed under the graph, and every change is also applied live to the current 3D view after a short delay (the **Apply Preview** button forces an immediate update).

* **Save** — validates and persists the preset, then closes the dialog.
* **Cancel** — discards the unsaved changes and restores the LUT that was active before opening the editor.

{{% notice info %}}
Custom presets are stored in the `customVolumePresets.json` file inside the Weasis preferences directory. When a remote preference service is configured (e.g. with weasis-pacs-connector), the file is also uploaded so the custom LUTs follow the user profile across workstations.
{{% /notice %}}

### Preferences
From the menu **_File > Preferences > Viewer > 3D Viewer_**.

#### OpenGL Support
Information about the graphics card and OpenGL capabilities, see [Requirements](#requirements).

#### 3D Viewer
* {{< svg-inline "static/tuto/icon/layout.svg" >}} **Default layout** — preferred layout used when opening the 3D viewer. Available layouts: **1×1** (single view, default), **1×2**, **2×1**, **1×3**, **2×2**.
* **Max 3D texture size** — maximum volume dimensions, both in X / Y (image width and height) and in Z (number of images in the stack composing the volume).

{{% notice note %}}
The maximum 3D texture defaults come from the graphics card. Lowering them (e.g. to 512) can produce a more fluid rendering on hardware that struggles with the full-size texture.
{{% /notice %}}

#### Volume Rendering
* **Dynamic quality** — reduces the rendering quality along the Z axis while you rotate or modify the view, for a smoother interaction. At the maximum slider position there is no quality reduction.
* **Default orientation** — preferred starting orientation. Default: anterior view rotated 15° to the right and 15° downward.
* **Background color** — background color of the rendered scene.
* **Light color** — color of the light used to illuminate the rendering.

### Video tutorials
Display an MR angiography series as a volume rendering, then switch to a MIP projection or pick a 3D LUT and adjust the window / level values:
{{< youtube id="waPx_-35zps" >}}