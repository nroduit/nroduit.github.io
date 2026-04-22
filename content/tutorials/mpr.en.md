---
title: MPR Viewer
weight: 50
description: How to use Multiplanar reconstruction (MPR) and 3D cursor (crosshair)
keywords: [ "mpr", "multiplanar reconstruction", "3d cursor", "open source dicom viewer" ]
---

## <center>Multiplanar reconstruction (MPR) {{< svg-inline "static/tuto/icon/mpr.svg" >}}</center>

The multiplanar reconstruction (MPR) allows you to create, from the original plane (usually axial), images in the two other planes of the Euclidean space. Only planes along the 3 axes (x,y,z) can be displayed. The oblique plane can be obtained only from {{% badge title="Version" %}}4.6.0{{% /badge %}}.

The MPR view inherits most properties and actions of the [DICOM 2D viewer](dicom-2d-viewer), except for the crosshair tool, which remains active regardless of the selected action (from {{% badge title="Version" %}}4.6.0{{% /badge %}}). You can open the MPR view by clicking the {{< svg-inline "static/tuto/icon/mpr.svg" >}} icon in the toolbar or by right-clicking a thumbnail in the [DICOM explorer](dicom-explorer/).

{{% notice note %}}
The menu and the toolbar button will only be active if the series contains at least **5 images**.
{{% /notice %}}

{{% notice tip %}}
If the series is a **multi-phase 4D acquisition** (e.g., a cardiac CT with several temporal phases), Weasis will automatically split it into individual phase sub-series when 2–7 phases are detected. For series with 8 or more phases, a confirmation dialog is shown first. Open any resulting phase sub-series to use it in the MPR viewer. See [4D Series Sub-Series Splitting](dicom-explorer#4d-splitting) for details.
{{% /notice %}}

The crosshair actions in the MPR are synchronized with the other views and include:
- {{< svg-inline "static/tuto/icon/mpr-move.svg" >}} **Move**: Move the cursor in 3D space by dragging the center of the crosshair.
- {{< svg-inline "static/tuto/icon/mpr-hand.svg" >}} **Move Axis**: Adjust the crosshair along the axes by selecting and dragging one of the lines.
- {{< svg-inline "static/tuto/icon/mpr-rotate.svg" >}} **Rotate**: Rotate the crosshair around its center by dragging the points along the axes.

By default, zoom and window/level are also synchronized between the three views. The synchronization of these actions can be deactivated by setting the synchronization drop-down button {{< svg-inline "static/tuto/icon/synch.svg" >}} (on the right of the layout button) to **None**.
The MRR views can be displayed in different layouts {{< svg-inline "static/tuto/icon/layout.svg" >}}.

To configure the MPR view, you can access settings by clicking the settings icon {{< svg-inline "static/tuto/icon/viewSettings.svg" >}} in the top-right corner. The available options include:
- **Center**: Center the crosshair in the view.
- **Show Center of Crosshair**: Show or hide the center point of the crosshair.
- **Show Crosshair**: Show or hide the crosshair lines. When hidden, the crosshair actions become inactive.
- **MIP Thickness**: Modify the thickness of the MIP in terms of pixel extension. You can also adjust it using _Alt + mouse scroll_ on an axis. Please note that the change in thickness may be delayed, as the MIP is computed in the background and doesn't use 3D acceleration.
- **MIP Type**:
  - **None**: No MIP applied.
  - **Min**: Minimum intensity projection.
  - **Mean**: Average intensity projection.
  - **Max**: Maximum intensity projection.

{{% notice note %}}
Most MPR settings can also be accessed using shortcuts. Refer to the [MPR shortcuts](../basics/shortcuts/#selected-view-in-the-mpr-viewer) for more details.
{{% /notice %}}

![QuMPR](/tuto/mpr.png?classes=shadow)
<br>

Try to load a volume dataset and open the MPR viewer. {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/3d/head-neck.xml"
{{< /launch >}}


### Crosshair Line Colors {#crosshair-colors}

Each crosshair line represents the intersection of one of the other two planes with the current view. The line color identifies which plane it belongs to:

| Color | Plane | Anatomical axis | Visible in |
|-------|-------|-----------------|------------|
| **Red** | Coronal | Anterior → Posterior | Axial, Sagittal |
| **Green** | Axial | Inferior → Superior | Coronal, Sagittal |
| **Blue** | Sagittal | Right → Left | Axial, Coronal |

For oblique planes, line colors blend proportionally based on the contribution of the primary axes.

### Orientation Axes {#orientation-axes}

The patient orientation axes are shown in the top-left corner of each MPR view, indicating how the current slice is oriented in 3D space:

| Color | Direction |
|-------|-----------|
| **Red arrow** | Anterior → Posterior |
| **Green arrow** | Inferior → Superior |
| **Blue arrow** | Right → Left |

For details on the orientation of multiplanar views and their associated colors, refer to [MPR Orientation](image-orientation/#orientation-in-multiplanar-reconstruction-mpr).

### Volume Geometry Handling {#volume-geometry}

Since {{% badge title="Version" %}}4.7.0{{% /badge %}}, when Weasis detects that a volume cannot be reconstructed as a perfect rectilinear grid, a confirmation dialog is displayed before the MPR views are built. Conditions are evaluated in the following priority order — only the first matching condition triggers the dialog:

| Condition | Dialog message |
|-----------|----------------|
| Slices are not parallel | _Slice orientations are not parallel!_ |
| Slice spacing is irregular | _Space between slices is not regular!_ |
| Too few slices relative to the gantry tilt | _There are too few slices compared to the geometric deformation!_ |

In all three cases, the following is appended to the message:

> _The images may be displayed incorrectly._
> _Do you want to rectify the images anyway?_

#### Dialog choices

* **Yes — Rectify geometry**: Re-slices the volume to align it with the patient's anatomical orientation. This ensures correct spatial proportions and enables accurate measurements and ratios across planes, but involves interpolation which may slightly affect image sharpness.
* **No — Stack images**: Stacks the original images directly without any geometric correction. This preserves the full original image quality and avoids interpolation, but distances, ratios, and measurements may not reflect true anatomical values.

{{% notice tip %}}
Choose **Yes** when accurate measurements are required. Choose **No** when image quality and the avoidance of interpolation artifacts are the priority.
{{% /notice %}}

#### Status indicator

After the choice is made, a persistent red text is displayed in the **bottom-left corner** of every MPR view to indicate the active geometry mode:

| Choice | Bottom-left indicator |
|--------|-----------------------|
| Yes (rectify) | _Geometry aligned to patient orientation_ |
| No (stack) | _Patient geometry correction skipped — spatial accuracy may be reduced_ |

### Preferences
From the main menu "_File > Preferences > Viewer > MPR_" (Since {{% badge title="Version" %}}4.1.0{{% /badge %}}):

* _Auto center axes:_ Allows you to choose a behavior to recenter the cursor in the different views. The position can be returned to the center systematically with the "Always" option or with the 2nd option only when the position is almost no longer visible (the default value).
* _Crosshair gap at the center:_ Defines the size of the empty space in the center of the crosshair
* _Default layout:_ The preferred layout used when opening the MPR viewer
