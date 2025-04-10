---
title: 3D cursor
weight: 48
description: How to use 3D cursor (crosshair)
keywords: [ "3d cursor", "open source dicom viewer" ]
---

## <center>3D cursor (crosshair)</center>

The 3D cursor allows you to synchronize the position of several views sharing the same 3D coordinate system.

In order to know which series sharing the same coordinate system, you can select more than one series from the DICOM explorer by right-clicking on a series and selecting "_Select related Series_". Then open the series selection by right-clicking again and selecting "_2D Viewer > Open_"

The crosshair tool {{< svg-inline "static/tuto/icon/crosshair.svg" >}} can be selected in the mouse buttons on the toolbar or by right-clicking on a view.

{{% notice tip %}}
It is possible to change the window/level with the [ctrl key](../../basics/shortcuts/) while keeping crosshair selected.
{{% /notice %}}

![3D Cursor](/tuto/3d-cursor.jpg?classes=shadow)
<br>

Try to load several series and select the 3D cursor. {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/ko.xml"
{{< /launch >}}

{{% notice info %}}
For more information on the elements related to the orientation of multiplanar views see [MPR orientation](../image-orientation/#orientation-in-multiplanar-reconstruction-mpr).
{{% /notice %}}

### Preferences

The MPR preferences share with the 3D cursor some preferences (_Auto center axes:_ and _Crosshair gap at the center_). See [MPR preferences](../mpr/#preferences) for more details.