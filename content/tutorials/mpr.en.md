---
title: MPR Viewer
weight: 50
description: How to use Multiplanar reconstruction (MPR) and 3D cursor (crosshair)
keywords: [ "mpr", "multiplanar reconstruction", "3d cursor", "open source dicom viewer" ]
---

## <center>Multiplanar reconstruction (MPR) {{< svg-inline "static/tuto/icon/mpr.svg" >}}</center>

The multiplanar reconstruction (MPR) allows you to create, from the original plane (usually axial), images in the two other planes of the Euclidean space. Only planes along the 3 axes (x,y,z) can be displayed. The oblique plane can be obtained only from {{% badge title="Version" %}}4.6.0{{% /badge %}}.

The MPR view inherits most properties and actions of the [DICOM 2D viewer](../dicom-2d-viewer), except for the crosshair tool, which remains active regardless of the selected action (from {{% badge title="Version" %}}4.6.0{{% /badge %}}). You can open the MPR view by clicking the {{< svg-inline "static/tuto/icon/mpr.svg" >}} icon in the toolbar or by right-clicking a thumbnail in the [DICOM explorer](../dicom-explorer/).


{{% notice note %}}
The menu and the toolbar button will only be active if the series contains at least **5 images**.
{{% /notice %}}

The crosshair actions in the MPR are synchronized with the other views and include:
- {{< svg-inline "static/tuto/icon/mpr-move.svg" >}} **Move**: Move the cursor in 3D space by dragging the center of the crosshair.
- {{< svg-inline "static/tuto/icon/mpr-hand.svg" >}} **Move Axis**: Adjust the crosshair along the axes by selecting and dragging one of the lines.
- {{< svg-inline "static/tuto/icon/mpr-rotate.svg" >}} **Rotate**: Rotate the crosshair around its center by dragging the points along the axes.

By default, zoom and window/level are also synchronized between the 3 views. The MRR views can be displayed in different layouts {{< svg-inline "static/tuto/icon/layout.svg" >}}.

To configure the MPR view, you can access settings by clicking the settings icon {{< svg-inline "static/tuto/icon/viewSettings.svg" >}} in the top-right corner. The available options include:
- **Center**: Center the crosshair in the view.
- **Show Center of Crosshair**: Show or hide the center point of the crosshair.
- **Show Crosshair**: Show or hide the crosshair lines. When hidden, the crosshair actions becomes inactive.
- **MIP Thickness**: Modify the thickness of the MIP in terms of pixel extension. You can also adjust it using _Alt + mouse scroll_ on an axis. Please note that the change in thickness may be delayed, as the MIP is computed in the background and doesn’t utilize 3D acceleration.
- **MIP Type**:
  - **None**: No MIP applied.
  - **Min**: Minimum intensity projection.
  - **Mean**: Average intensity projection.
  - **Max**: Maximum intensity projection.

{{% notice note %}}
Most MPR settings can also be accessed using shortcuts. Refer to the [MPR shortcuts](../../basics/shortcuts/#selected-view-in-the-mpr-viewer) for more details.
{{% /notice %}}

![QuMPR](/tuto/mpr.png?classes=shadow)
<br>

Try to load a volume dataset and open the MPR viewer. {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/3d/head-neck.xml"
{{< /launch >}}

{{% notice info %}}

The color of the crosshair lines corresponds to the orientation of the other two planes:
- **Red Line**: Represents the anterior-posterior axis of the coronal plane.
- **Green Line**: Represents the inferior-superior axis of the axial plane.
- **Blue Line**: Represents the right-left axis of the sagittal plane.

For oblique planes, the crosshair line colors blend proportionally based on the contribution of the primary axes.

The orientation axes of the slice image in 3D space are shown in the top-left corner of the MPR view. They are defined as follows:
- **Red arrow**: Increases from anterior to posterior
- **Green arrow**: Increases from inferior to superior
- **Blue arrow**: Increases from right to left

For details on the orientation of multiplanar views and their associated colors, refer to [MPR Orientation](../image-orientation/#orientation-in-multiplanar-reconstruction-mpr).
{{% /notice %}}

### Preferences
From the main menu "_File > Preferences > Viewer > MPR_" (Since {{% badge title="Version" %}}4.1.0{{% /badge %}}):

* _Auto center axes:_ Allows you to choose a behavior to recenter the cursor in the different views. The position can be returned to the center systematically with the "Always" option or with the 2nd option only when the position is almost no longer visible (the default value).
* _Crosshair gap at the center:_ Defines the size of the empty space in the center of the crosshair
* _Default layout:_ The preferred layout used when opening the MPR viewer
