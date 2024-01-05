---
title: DICOM 2D Viewer
weight: 40
description: How to display an image or a stack of images
keywords: [ "viewer 2D", "dicom data", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying DICOM images {{< svg "static/tuto/icon/view2d.svg" >}}</center>

The 2D viewer is the default viewer when opening a DICOM series containing images.

### Open the 2D viewer
The 2D view can be opened with {{< svg "static/tuto/icon/view2d.svg" >}} in the toolbar or by right-clicking on the thumbnail in the [DICOM explorer](../dicom-explorer/).

![DICOM 2DViewer](/tuto/dicom-viewer2d.jpg?classes=shadow&width=780px)
<br>

The rulers{{< badge "K" >}} show a real size when it can be calculated from the DICOM file. When a text {{< badge "M" >}} above the calibration is displayed, it gives information about the calibration type. Here are some examples:
* _At dector:_ The calibration of the projection radiographic image is done at the detector level 
* _Magnified:_ The calibration of the projection radiographic image is corrected using the magnification factor (e.g. mammography)
* _Used fiducials:_ The calibration is based on fiducials (e.g. manual calibration with a ruler in the image)
* _At scanner:_ The calibration comes from a media which has been digitized (e.g. film digitizer)

### Toolbars {{< badge "A" >}}

#### Viewer Main Bar

![Main Toolbar](/tuto/main-toolbar.png?classes=shadow)

Select the preferred actions for the three mouse buttons and the mouse wheel:

* Mouse left button: The default value is Window/Level. Action can also be changed from the context menu {{< badge "F" >}} and the [key shortcuts](../../basics/shortcuts).
* Mouse right button: The default value is _Context Menu_
* Mouse wheel: The default value is _Series Scroll_
* Mouse middle button: The default value is _Pan_

Where the possible actions are:
* Pan: Move the image position. _T_ key to select the action. _Alt + Arrows_ keys to pan when another action is selected.
* [Window/Level](../lut): Change the contrast of the image. _W_ key to select the action.
* Series Scroll: Scroll through the images of the current series. _S_ key to select the action.
* [Zoom](../zoom): Zoom in/out the image. _Z_ key to select the action.
* Rotation: Rotate the image with a free angle. _R_ key to select the action.
* [Measure](../draw-measure/#measurement-tools-hahahugoshortcodes3hbhb): Draw a graphic for measuring something. _M_ key to select the action.
* [Draw](../draw-measure/#drawings-hahahugoshortcodes7hbhb): Draw a graphic for annotating. _G_ key to select the action.
* Context Menu: Display the context menu. _Q_ key to select the action.
* [Crosshair](../mpr/#3d-cursor-crosshair): 3D cursor. _H_ key to select the action. _Ctrl + click_ or _Ctrl + Shift + click_ allows changing Window/Level.
* No Action: Do nothing. _N_ key to select the action.

{{% notice tip %}}
When dragging, accelerate the action by pressing the _Ctrl_ key and _Ctrl + Shift_ to accelerate more.
{{% /notice %}}

* {{< svg "static/tuto/icon/layout.svg" >}} _Default layout:_ Change the layout of the view. [DICOM Information](../tags) and [Histogram](../histogram) are specific layouts where information is automatically updated when scrolling through the series.
* Synchronize: The synchronization feature lets you apply the same settings to other images.
  * _None:_ No synchronization is applied between series.
  * _Default Stack:_ When selected, the layout is synchronized (window/level, scrolling, zoom) only with the series sharing the same Frame of Reference UID (0020,0052). This is the default behavior.
  * _Default Tile:_ When selected, the layout is applied in tiled mode (image mosaic of the current series) and is synchronized (window/level, scrolling, zoom) with the image of the same series.
* {{< svg "static/tuto/icon/reset.svg" >}} _Reset:_ Reset the image rendering (see [below](#reset)). _Escape_ key to select the action.

#### Toolbars available in the DICOM 2D viewer
* [DICOM Import](../dicom-import/#from-weasis-menu-or-toolbar)
* [DICOM Export](../dicom-export/#dicom-export-hahahugoshortcodes2hbhb)
* [Screenshot](../dicom-export/#dicom-export)
* Viewer Main Bar (see above)
* [Measurement](../draw-measure/)
* [Zoom](../zoom)
* Rotation: Rotate the image by 90° clockwise or flip it horizontally. Note visible by default.
* [DICOM Header](../tags)
* [Lookup Table](../lut)
* Basic 3D: [MPR](../mpr) and [MIP](../mip) (disabled if the series has less than 5 images)
* [3D Viewer](../dicom-3d-viewer) (disabled if the series has less than 5 images)
* [Cine](#cine)
* [Key Object Selection](../build-ko-pr/#key-object-selection-ko)

{{% notice tip %}}
Toolbars can be shown or hidden from the _View_ top menu.
{{% /notice %}}

### Viewer's tools
Here is a list of the tools which are associated to the DICOM 2D viewer.

The mini-tool is always visible and the other tools are displayed by clicking on the vertical button. The normalize button {{< svg "static/tuto/icon/normalize.svg" >}} allows you to insert the panel into the main layout. Otherwise, the panel is displayed as a popup window with the pin option {{< svg "static/tuto/icon/holdon.svg" >}} (which is not recommended, as it hides other panels).

#### Mini-tool {{< badge "B" >}}
Allows you by default to scroll through the images of the selected series (surrounded by an orange line). From the combobox at the top, the mini-tool can also be configured to change the zoom or the rotation of the image.  

#### Display {{< badge "C" >}}

It lets you control the display of the image and the graphic objects. 

The _Apply to all views_ option allows you to apply the same display settings to all the views within the selected tab. If unchecked, the display settings are only applied to the selected view (surrounded by an orange line).

##### Image
Display options for the image. Unchecking the _Image_ option will hide the image and display only the annotations and the graphic objects. The other options are related to DICOM specifications:
* Dicom Image Overlay: Apply the [DICOM overlays](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.9.2.html) when checked. The [overlay color](#other) can be changed.
* Shutter: Apply the [DICOM shutters](https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.7.6.11.html) when checked
* Pixel Padding: Apply the [DICOM pixel padding](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.5.html#sect_C.7.5.1.1.2) when checked

##### Dicom Annotations
Display transformation properties and DICOM information on the image.

* Annotations: Display DICOM information on the image corners:
  * {{< badge "G" >}} The top left: Patient information 
  * {{< badge "H" >}} The top right: Study information
  * {{< badge "I" >}} The bottom right: Series information (related to the modality type)
  * {{< badge "J" >}} The bottom left: Image information and its position in the series
* Minimal Annotations: Reduce the number of annotations. Use _space_ or _i_ key to toggle between the 3 states (minimal, none, all).
* Anonymize: Hide identifying information only in the views not in other places of the GUI like the tab title. Must be used with the [screenshot tool](../dicom-export) when exporting image.
* Scale: Display the rulers on the left and the bottom of the image {{< badge "K" >}}
* Lookup Table: Display the [LUT](../lut) on the image
* Orientation: Display the [orientation of the image](../image-orientation) {{< badge "N" >}}
* Window/Level: Display the [window and level](../lut/#windowing-and-rendering) values {{< badge "J" >}}
* Zoom: Display the zoom value {{< badge "J" >}}
* Rotation: Display the rotation value {{< badge "J" >}}
* Frame Value: Display the frame number {{< badge "J" >}}
* Pixel (Value/Position): Display the pixel value and the position of the cursor {{< badge "J" >}}

##### Drawings
Check/uncheck to show/hide the graphic objects (see [Draw & Measure](../draw-measure/)).

#### Image Tools {{< badge "D" >}}
_Image Tools_ contains all the tools to modify the image rendering.

##### [Windowing and Rendering](../lut/) 

##### Transform
Allows you to zoom, rotate and flip the image. [Zoom](../zoom) and rotation can also be configured with the [mini-tool](#mini-tool) or the [mouse actions](#toolbars-hahahugoshortcodes3hbhb).

##### Cine
The _Cine start_ button {{< svg "static/tuto/icon/execute.svg" >}} lets you scroll through the images in a series at a certain speed (frame per second). The speed values comes from the DICOM file if exists.
Click on _Cine stop_ button {{< svg "static/tuto/icon/suspend.svg" >}} to end the animation.

{{% notice note %}}
A _Cine_ toolbar is also available. It is not visible by default, but can be displayed from the _View_ menu.
{{% /notice %}}

##### Reset
It allows you to return to the default image rendering for all or specific parameters. Also available from the toolbar button {{< svg "static/tuto/icon/reset.svg" >}} or from the context menu.

#### [Draw & Measure](../draw-measure/) {{< badge "E" >}}

#### Other specific tools
* [DICOM RT tools](../dicom-rt) (for radiotherapy studies)
* DICOM Segmentation tools (not yet available)

### Preferences
From the menu "_File > Preferences > Viewer > "2D Viewer_":

#### Mouse Action Sensitivity
The sensitivity of the mouse drag can be changed according to your preferences for the following actions: _Window_, _Level_, _Zoom_, _Rotation_ and _Series Scroll_.

#### Zoom
Zoom interpolation is the process of creating new pixels between existing pixels in an image when it is zoomed in or out.

* The _Nearest neighbor_ interpolation is the simplest method. Basically, it extends the pixel value.
* The _Bilinear_ method averages the values of the four nearest existing pixels to the new pixel. This produces slightly sharper results than nearest-neighbor interpolation, but it is also slightly slower.
* The _Bicubic_ method is similar to bilinear interpolation, but it uses a 16-point kernel instead of a 4-point kernel. This produces even sharper results than bilinear interpolation, but it is also the slowest method.
* The _Lanczos_ method uses a sinc kernel to resample the image producing the sharpest results. It is moderately fast, between bilinear and bicubic.

The default value is _Bilinear_. The _Nearest neighbor_ interpolation is faster but produces aliasing artifacts.

#### Other
* _Apply Window/Level on color images:_ When checked, the window/level is applied on the RGB channels of the image. Otherwise, the window/level has no effect when unchecked.
* _Inverse level direction:_ When checked, the level direction with mouse actions is inverted (dragging down will increase the brightness) according to the [Basic Image Review profile](https://wiki.ihe.net/index.php?title=Basic_Image_Review). Otherwise, dragging down will decrease the brightness when unchecked.
* _Apply by default the most recent Presentation State:_ When checked, the most recent [Presentation State](../build-ko-pr/#presentation-state-pr-or-gsps) Object is applied on the related image. Otherwise, it is required to select it from {{< svg "static/tuto/icon/imagePresentation.svg" >}}.
* _Overlay color:_ change the color and the opacity of DICOM overlay. The default color is white. The opacity can be changed from the transparency or alpha slider of the different color models in the color picker.