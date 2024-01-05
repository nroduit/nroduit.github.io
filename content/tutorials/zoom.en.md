---
title: Zoom
weight: 340
description: How to manipulate zoom and lens
keywords: [ "zoom", "lens", "dicom viewer",  "pacs viewer" ]
---

## <center>Zoom tool {{< svg "static/tuto/icon/zoom.svg" >}}</center>

The zoom tool can be associated with one of three mouse actions  . In the image below the zoom tool {{< svg "static/tuto/icon/zoom.svg" >}} is associated with the middle mouse button. See also [zoom preferences](../dicom-2d-viewer/#preferences).

The zoom factor can be modified from different locations:

* By dragging the cursor over the image with the configured mouse button
* By scrolling the mouse wheel when configured
* By selecting an item in the zoom dropdown button in the toolbar
* From the context menu: right-click on the image > Zoom
* Form the slider in the image tool panel
* Using [Keyboard Shortcuts](../../basics/shortcuts) (_Ctrl + Plus (+)_, _Ctrl + Minus (-)_ and _Ctrl + Enter_) on the selected view

The context menu and the toolbar button allows you to select different zoom factor:

* Actual pixel size {{< svg "static/tuto/icon/zoomOriginal.svg" >}}: display the image at a 1:1 ratio, where each pixel in the image corresponds to one pixel on the screen
* Real world (see [below](#real-world-zoom-hahahugoshortcodes7hbhb)) {{< svg "static/tuto/icon/zoomRealWorld.svg" >}}
* Resize to best fit {{< svg "static/tuto/icon/zoomBestFit.svg" >}}: scaling the image to make it fit the view area as closely as possible

{{% notice note %}}
The zoom function always zooms in/out to the center of the screen regardless of where the cursor is. This mode provides greater positional accuracy in particular situations.

Since "Resize to best fit" is the default mode for a view, the image will be centered when scrolling to the next image. You need to change the mode or the zoom factor to keep the image off center when scrolling.
{{% /notice %}}

![Zoom tool](/tuto/zoom-actions.jpg?classes=shadow&width=700px)
<br>
{{% notice tip %}}
For selecting directly the zoom action of the mouse left button, enter "z" as a shortcut.
{{% /notice %}}

### Real-world zoom {{< svg "static/tuto/icon/zoomRealWorld.svg" >}}
The real-world zoom allows displaying the content of the image at the same size of the real objects.

The feature requires calibrating the screen where the image is displayed. From the main menu, open _File > Preferences (Alt + P) > Monitors_ and click on _Spatial calibration_. Then enter a value that matches to the line length or the diagonal length of the screen.

{{% notice note %}}
Several screens can be calibrated. Each one has its own spatial calibration factor.
{{% /notice %}}

## Magnifying lens {{< svg "static/tuto/icon/zoomPan.svg" >}}
The magnifying lens can be activated from the toggle button of the zoom toolbar (see the image below). It has several parameters accessible from the context menu.

This lens can be used in many situations, for instance:

* to magnify a specific area
* to compare two images from the same series (select `Freeze image`)
* to display a specific area without the drawings (Unselect `Show Drawings`)
* to compare different values of Window/Level (select `Freeze parameters` - see image below)

{{% notice note %}}
Using the mouse wheel on the lens changes the zoom factor. Double-clicking on the lens adjusts the zoom factor of the lens to the one of the main image.
{{% /notice %}}

![Lens](/tuto/lens-drawing.jpg?classes=shadow&width=700px)
<br>
Parameters of the context menu:

* *Synchronize to parent zoom:* When this option is activated, the zoom factor of the lens is permanently adjusted to the zoom factor of the main image (meaningful when using freeze parameters).
* *Show Drawings:* Displays in the lens the visible drawings.
* *Magnify:* Allows to select a zoom magnitude.
* *Image:* `Freeze parameters` allows you to keep the current image processing (c.f. Window/level, LUT or filter) and `Freeze image` allows you to keep the current image and its parameters.

![Lens freeze](/tuto/lens-freeze.jpg?classes=shadow&width=700px)
