---
title: DICOM 3D Viewer
weight: 60
description: How to display volume data
keywords: [ "viewer 3D", "volume rendering", "ray casting", "3D rendering", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying volume data {{< svg-inline "static/tuto/icon/volume.svg" >}}</center>

Since Weasis {{% badge title="Version" %}}4.1.0{{% /badge %}} the 3D viewer allows displaying volumetric renderings with different options for adjusting the pseudo colors, the transparency, the shadows, and the lighting according to the type of exam.

The volume rendering uses a [ray casting algorithm](https://en.wikipedia.org/wiki/Volume_ray_casting) and the OpenGL Shading Language (GLSL). Shader programming is used to create the necessary algorithms and data structures 
required for the ray casting computations to be executed efficiently on the graphics card. Therefore, minimal graphic resources are required.

### Requirements
Some requirements related to the specifications of your graphic card are mandatory. They can be displayed in "_OpenGL Support_" from the menu "_File > Preferences > Viewer > 3D Viewer_":

* _Driver version:_ Requires OpenGL **3.3+** since {{% badge title="Version" %}}4.7.0{{% /badge %}}. Two rendering backends are used depending on the available OpenGL version:
  * **OpenGL 4.3+** — uses a **Compute Shader** for optimal performance.
  * **OpenGL 3.3–4.2** — uses an **FBO-based Fragment Shader** fallback (fully functional, but may be less performant than the Compute Shader path). macOS is capped at OpenGL 4.1 and therefore uses this path.
* _Max 3D texture dimension length:_ The limit of any dimension (X,Y,Z) of the volume data
* If you have other information in red, it means that the configuration is not optimal but in most cases can work (see [how to limit the size of 3D textures](#3d-viewer))

{{% notice note %}}
If the graphic card displayed in Weasis is not the right one, you must solve this problem on the side of the graphic drivers or the operating system.

OpenGL does not include specific functionality for selecting a particular graphics card. Instead, this is handled by the graphics card driver and operating system, which provide a way for users to configure which graphics card should be used by an application.

To force the FBO-based fragment shader path on any platform (e.g., for testing), add the JVM argument `-Dweasis.3d.force.fbo=true` to the Weasis launcher.
{{% /notice %}}

### Open the 3D viewer
The 3D view can be opened with {{< svg-inline "static/tuto/icon/volume.svg" >}} in the toolbar or by right-clicking on the thumbnail in the [DICOM explorer](dicom-explorer).

{{% notice tip %}}
If the series is a **multi-phase 4D acquisition** (e.g., a cardiac CT with several temporal phases), Weasis will automatically split it into individual phase sub-series when 2–7 phases are detected. For series with 8 or more phases, a confirmation dialog is shown first. Open any resulting phase sub-series to use it in the 3D viewer. See [4D Series Sub-Series Splitting](dicom-explorer#4d-splitting) for details.
{{% /notice %}}

Try to load a volume dataset (Medical Demos from data.kitware.com)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/3d/head-neck.xml"
{{< /launch >}}

![3D View](/tuto/view-3d.jpg?classes=shadow&width=780px)
<br>

Patient orientation axes are displayed directly in the 3D view since {{% badge title="Version" %}}4.7.0{{% /badge %}}, using the same LPS color coding as the [MPR viewer orientation axes](mpr#orientation-axes).

### Toolbar {{% badge style="red" %}}A{{% /badge %}} {#toolbar}
Actions in the toolbar are:
* {{< svg-inline "static/tuto/icon/loadVolume.svg" >}} Allows you to fully reload the volume
* {{< svg-inline "static/tuto/icon/orthographic.svg" >}} The orthographic projection maintains parallel lines unlike the perspective projection that provides a perception of depth. The default mode is the perspective projection.
* {{< svg-inline "static/tuto/icon/volumeCut.svg" >}} Opens the [MPR crosshair cut mode](#mpr-cut) to interactively clip the rendered volume along the anatomical planes defined by the MPR crosshair position and orientation.
* {{< svg-inline "static/tuto/icon/volumeSettings.svg" >}} Opens the [3D preferences](#preferences)

For other buttons see below.

### MPR Crosshair Cut Mode {#mpr-cut}

Since {{% badge title="Version" %}}4.7.0{{% /badge %}}, the 3D viewer can display an MPR crosshair overlay synchronized with the [MPR viewer](mpr#crosshair-colors), allowing you to interactively clip the rendered volume along the anatomical planes defined by the crosshair position and orientation. This bridges the 2D MPR viewer and the 3D volume viewer by keeping the crosshair position and rotation synchronized in real time.

#### Recommended workflow

1. Open the [MPR viewer](mpr) from a series view.
2. In the MPR toolbar, click {{< svg-inline "static/tuto/icon/volume.svg" >}} — this splits the current tab into a side-by-side layout with the MPR views on one side and the 3D volume rendering on the other.
3. In the 3D view, activate a cut mode using the toolbar button {{< svg-inline "static/tuto/icon/volumeCut.svg" >}} or by right-clicking and selecting _MPR Crosshair Cut_.

#### Alternative workflow

Open the 3D viewer first, then activate a cut mode from the toolbar {{< svg-inline "static/tuto/icon/volumeCut.svg" >}} or the contextual menu. The MPR viewer will open automatically for the same series, but it will appear in a separate tab. To obtain the side-by-side layout, drag the MPR tab and [dock](docking) it next to the 3D view using the docking handles.

#### Cut modes

* _None_: No clipping applied — the full volume is rendered.
* _18 directional modes_: Clip the volume in halves, quarters, or eighths relative to the MPR crosshair position, along each anatomical axis (Left/Right, Anterior/Posterior, Superior/Inferior).

The crosshair overlay uses the same LPS axis color coding as the MPR viewer.

### 3D Rendering Tools
This tab contains all the tools to modify the volume rendering. If you want to return to the original settings, just click on the toolbar button {{< svg-inline "static/tuto/icon/reset.svg" >}} or from the context menu.

#### Windowing and Rendering {{% badge style="red" %}}B{{% /badge %}} {#windowing}
Some of the options described below are also available in the toolbar and in the contextual menus.

* _Window:_ The width of a range of voxels values mapped to a specific range of display values.
* _Level:_ The center of the range defined by Window.
* _LUT Shape:_ The mapping (transfer function) between the input values and the display values can be linear, sigmoid, and logarithmic. Default value is linear.
* {{< svg-inline "static/tuto/icon/lut.svg" >}} _LUT (Volume LUT):_ A Volume Lookup Table (LUT) is a 3D LUT used to map the grayscale values of a volume dataset to color, opacity, and lighting values for visualization. Choosing a LUT from the toolbar or the contextual menu is easier because the LUTs are displayed in an order according to the modality and with a preview.
* {{< svg-inline "static/tuto/icon/inverseLut.svg" >}} allows you to invert the LUT.


#### Volume Rendering {{% badge style="red" %}}C{{% /badge %}} {#volume-rendering}
This panel contains options for the rendering type and its quality, transparency, lighting, and shading settings.

* _Type:_ Defines the rendering algorithm applied to the volume:
  * _Composite_: Classic volume rendering. Each voxel contributes colour and opacity along the ray, blended front-to-back to produce the final image.
  * _MIP Max_: Maximum Intensity Projection — projects the highest-intensity voxel encountered along each ray. Useful for highlighting bright structures such as contrast-enhanced vessels or bones.
  * _MinIP_: Minimum Intensity Projection — projects the lowest-intensity voxel along each ray. Useful for visualising air-filled structures such as airways.
  * _MIP Mean_: Mean Intensity Projection — projects the average intensity along each ray, providing a smoother representation of the volume.
  * _Iso Surface_: Renders a 3D surface at a specific intensity threshold, representing structures of a uniform density (e.g., bone segmentation).
* _Z-axis sampling:_ The sampling should be large enough to accurately capture the details of the volume data, but small enough to avoid excessive computation time. The default value is calculated according to the size of the volume.
* _Opacity:_ The opacity factor of the voxels. Can be set to more than 100% to modify initial values (lower than 100%) transmitted by the Volume LUTs.
* _Shading:_ Allows to activate the shading. Default value is defined in LUT. The additional options allow you to override the default lighting settings (comes from Volume LUT).

#### Transform {{% badge style="red" %}}D{{% /badge %}} {#transform}
Allows you to zoom and rotate along a specific axis

### Preferences
From the menu "_File > Preferences > Viewer > 3D Viewer_":

#### OpenGL Support
Information about the graphics card and OpenGL capabilities, see [Requirements](#requirements).

#### 3D Viewer
* {{< svg-inline "static/tuto/icon/layout.svg" >}} _Default layout:_ The preferred layout used when opening the 3D viewer
* _Max 3D texture size:_ The maximum size of the volume according to X/Y (width and height of images) and according to Z (number of images in the stack composing the volume)

{{% notice note %}}
The maximum values of the default 3D textures come from the graphics card. However, it may be wise to decrease these values (e.g., 512) in order to allow a more efficient display of volumetric renderings for which the hardware resources are not enough.
{{% /notice %}}

#### Volume Rendering
* _Dynamic quality:_ Allows you to make the render more fluid by reducing its quality (according to the z-axis) when it is rotating or being modified. When the slider is at maximum, then there is no more quality reduction.
* _Default orientation:_ The preferred orientation used when opening a volume rendering view. Default is Anterior position by turning 15 degrees to the right and 15 degrees downwards.
* _Background color:_ Defines the background color of the rendering
* _Light color:_ Defines the color of the light during the illumination of the rendering

### Video tutorials
* Display an MR scan with an angiography-specific protocol by creating a volume rendering. Then either use the MIP type or choose a 3D LUT and adjust the win/level values.
{{< youtube id="waPx_-35zps" >}}