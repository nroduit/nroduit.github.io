---
title: MPR Viewer and 3D cursor
weight: 50
description: How to use Multiplanar reconstruction (MPR) and 3D cursor (crosshair)
keywords: [ "mpr", "multiplanar reconstruction", "3d cursor", "open source dicom viewer" ]
---

## <center>MPR Viewer and 3D cursor (crosshair)</center>

### Orthogonal multiplanar reconstruction (MPR) {{< svg "static/tuto/icon/mpr.svg" >}} {#mpr}
The orthogonal multiplanar reconstruction (MPR) allows you to create, from the original plane (usually axial), images in the two other planes of the Euclidean space. Only planes along the 3 axes (x,y,z) can be displayed, an oblique plane cannot be obtained with this tool.

The MPR view inherits most of the [DICOM 2D viewer](../dicom-2d-viewer) properties. It can be opened with {{< svg "static/tuto/icon/mpr.svg" >}} in the toolbar or by right-clicking on the thumbnail in the [DICOM explorer](../dicom-explorer/).
{{% notice note %}}
The menu and the button are only active if the series contains at least 5 images.
{{% /notice %}}

When the tab containing the MPR views is selected, the crosshair tool {{< svg "static/tuto/icon/crosshair.svg" >}} is automatically applied on the left mouse button. Note that it is possible to change the window/level with the [ctrl key](../../basics/shortcuts/) while keeping crosshair selected.

By default, zoom and window/level are synchronized between the 3 views. The MRR views can be displayed in different layouts {{< svg "static/tuto/icon/layout.svg" >}}.

{{% notice tip %}}
Once the 2 new plans are created, they also appear in the [DICOM explorer](../dicom-explorer/) and can be [exported](../dicom-export/#dicom-exporting).
{{% /notice %}}

![QuMPR](/tuto/mpr.jpg?classes=shadow)
<br>

Try to load a volume dataset and open the MPR viewer. {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/3d/head-neck.xml"
{{< /launch >}}

{{% notice info %}}
For more information on the elements related to the orientation of multiplanar views see [MPR orientation](../image-orientation/#orientation-in-2d-multiplanar-reconstruction-mpr).
{{% /notice %}}

### 3D cursor (crosshair)
The 3D cursor allows you to synchronize the position of several views sharing the same 3D coordinate system.

In order to know which series sharing the same coordinate system, you can select more than one series from the DICOM explorer by right-clicking on a series and selecting "_Select related Series_". Then open the series selection by right-clicking again and selecting "_2D Viewer > Open_"

The crosshair tool {{< svg "static/tuto/icon/crosshair.svg" >}} can be selected in the mouse buttons on the toolbar or by right-clicking on a view.

![3D Cursor](/tuto/3d-cursor.jpg?classes=shadow)
<br>

Try to load several series and select the 3D cursor. {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/ko.xml"
{{< /launch >}}

### Preferences
From the main menu "_File > Preferences > Viewer > MPR_" (Since {{% badge title="Version" %}}4.1.0{{% /badge %}}):

* _Auto center axes:_ Allows you to choose a behavior to recenter the cursor in the different views. The position can be returned to the center systematically with the "Always" option (see the image above) or with the 2nd option only when the position is almost no longer visible (the default value).
* _Crosshair gap at the center:_ Defines the size of the empty space in the center of the crosshair
* _Default layout:_ The preferred layout used when opening the MPR viewer

{{% notice info %}}
The preferences apply to both the MPR and the 3D cursor.
{{% /notice %}}