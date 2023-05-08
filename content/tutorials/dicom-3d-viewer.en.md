---
title: 3D Viewer
weight: 85
description: How to display volume data
keywords: [ "viewer 3D", "volume rendering", "ray casting", "3D rendering", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying volume data</center>

Since Weasis {{< badge "v4.1.0" >}} the 3D viewer allows displaying volumetric renderings with different options for adjusting the pseudo colors, the transparency, the shadows and the lighting according to the type of exam.

The volume rendering uses a [ray casting algorithm](https://en.wikipedia.org/wiki/Volume_ray_casting) and the OpenGL Shading Language (GLSL). Shader programming is used to create the necessary algorithms and data structures 
required for the ray casting computations to be executed efficiently on the graphics card. Therefore, minimal graphic resources are required.

### Requirements

Some requirements related to the specifications of your graphic card are mandatory. They can be displayed in "_OpenGL Support_" from the menu "_File > Preferences > Viewer > 3D Viewer_":

* _Driver version:_ The OpenGL version must be **at least 4.3** to support the Compute Shader
* _Max 3D texture dimension length:_ The limit of any dimension (X,Y,Z) of the volume data
* If you have other information in red, it means that the configuration is not optimal but in most cases can work (see [how to limit the size of 3D textures](#3d-viewer))

{{% notice note %}}
If the graphic card displayed in Weasis is not the right one, you must solve this problem on the side of the graphic drivers or the operating system.

OpenGL does not include specific functionality for selecting a particular graphics card. Instead, this is handled by the graphics card driver and operating system, which provide a way for users to configure which graphics card should be used by an application.
{{% /notice %}}

### Open the 3D viewer

The 3D view can be opened with {{< svg "static/tuto/icon/volume.svg" >}} in the toolbar or by right-clicking on the thumbnail in the [DICOM explorer](../dicom-explorer/).

Try to load a volume dataset (Medical Demos from data.kitware.com)
{{< launch >}}
$dicom:get -w "http://localhost:1313/samples/3d/head-neck.xml"
{{< /launch >}}

![3D Viewer](/tuto/view-3d.jpg?classes=shadow&width=780px)
<br>

### Toolbar (A)

Actions in the toolbar are:
* {{< svg "static/tuto/icon/loadVolume.svg" >}} Allows you to fully reload the volume
* {{< svg "static/tuto/icon/Orthographic.svg" >}} The orthographic projection maintains parallel lines unlike the perspective projection that provides a perception of depth. The default mode is the perspective projection.
* {{< svg "static/tuto/icon/volumeSettings.svg" >}} Opens the [3D preferences](#preferences)

### 3D Rendering Tools

This tab contains all the tools to modify the volume rendering. If you want to return to the original settings, just click on the toolbar button {{< svg "static/tuto/icon/reset.svg" >}} or from the context menu.

#### Windowing and Rendering (B)

Some of the tools described below are also available in the toolbar and in the contextual menus.

* _Window:_ The width of a range of voxels values mapped to a specific range of display values.
* _Level:_ The center of the range defined by Window.
* _Preset:_ Specific values of Window and level. _Auto Level [Image]_ is the default value when changing a LUT and provides the best visual appearance of a Volume LUT.
* _LUT Shape:_ The mapping between the input values and the display values can be linear, sigmoid and logarithmic. Default value is linear.
* _LUT (Volume LUT):_ A Volume Look-Up Table (LUT) is a 3D LUT used to map the grayscale values of a volume dataset to color, opacity and lighting values for visualization. Choosing a LUT from the toolbar or the contextual menu is easier because the LUTs are displayed in an order according to the modality and with a preview.


#### Volume Rendering (C)

This panel contains options for the rendering type and its quality, transparency, lighting, and shading settings.

* _Type:_ Composite is the classic type of volume rendering. The Maximum Intensity Projection (MIP) is the highest intensity voxels (3D pixels) along a ray path are projected onto a 2D plane. Iso surface is a technique to create a 3D representation on a specific intensity threshold.
* _Z-axis sampling:_ The sampling should be large enough to accurately capture the details of the volume data, but small enough to avoid excessive computation time. The default value is calculated according to the size of the volume.
* _Opacity:_ The opacity factor of the voxels. Can be set to more than 100% to modify initial values (lower than 100%) transmitted by the Volume LUTs.
* _Shading:_ Allows to activate the shading. Default value is defined in LUT. The additional options allow you to override the default lighting settings (comes from Volume LUT).

#### Transform (D)

Allows you to zoom and rotate along a specific axis

### Preferences

From the menu "_File > Preferences > Viewer > 3D Viewer_":

#### OpenGL Support

Information about the graphics card and OpenGL capabilities, see [Requirements](#requirements).

#### 3D Viewer

* _Default layout:_ The preferred layout used when opening the 3D viewer
* _Max 3D texture size:_ The maximum size of the volume according to X/Y (width and height of images) and according to Z (number of images in the stack composing the volume)

{{% notice note %}}
The maximum values of the default 3D textures come from the graphics card. However, it may be wise to decrease these values (e.g. 512) in order to allow a more efficient display of volumetric renderings for which the hardware resources are not sufficient.
{{% /notice %}}

#### Volume Rendering

* _Dynamic quality:_ Allows you to make the render more fluid by reducing its quality (according to the z-axis) when it is rotating or being modified. When the slider is at maximum then there is no more quality reduction.
* _Default orientation:_ The preferred orientation used when opening a volume rendering view. Default is Anterior position by turning 15 degrees to the right and 15 degrees downwards.
* _Background color:_ Defines the background color of the rendering
* _Light color:_ Defines the color of the light during the illumination of the rendering
