---
title: Zoom
weight: 100
description: How to manipulate zoom and lens
keywords: [ "zoom", "lens", "dicom viewer",  "pacs viewer" ]
---

## Zoom tool

The zoom tool can be associated with one of three mouse buttons or with the mouse scroll (top left toolbar). In the image below the zoom tool is associated with the left mouse button.

The zoom factor can be modified from different locations:

* by dragging the cursor over the image with the configured mouse button
* by scrolling the mouse wheel when configured
* by selecting an item in the zoom dropdown button in the toolbar
* from the context menu: right-click on the image > Zoom
* form the slider in the image tool panel

{{% notice note %}}
The zoom function always zooms in/out to the center of the screen regardless of where the cursor is.
{{% /notice %}}

![Zoom tool](/tuto/zoom-actions.jpg?classes=shadow&width=700px)

{{% notice tip %}}
For selecting directly the zoom action of the mouse left button, enter "z" as a shortcut.
{{% /notice %}}

### Real-world zoom
The real-world zoom allows displaying the content of the image at the same size of the real objects.

The feature requires calibrating the screen where the image is displayed. From the main menu, open File > Preferences (Alt + P) > Monitors and click on "Spatial calibration". Then enter a value that matches to the line length or the diagonal length of the screen.

{{% notice note %}}
Several screens can be calibrated. Each one has its own spatial calibration factor.
{{% /notice %}}

## Magnifying lens
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

Parameters of the context menu:

* *Synchronize to parent zoom:* When this option is activated, the zoom factor of the lens is permanently adjusted to the zoom factor of the main image (meaningful when using freeze parameters).
* *Show Drawings:* Displays in the lens the visible drawings.
* *Magnify:* Allows to select a zoom magnitude.
* *Image:* `Freeze parameters` allows to keep the current image processing (c.f. Window/level, LUT or filter) and `Freeze image` allows to keep the current image and its parameters.

![Lens freeze](/tuto/lens-freeze.jpg?classes=shadow&width=700px)
