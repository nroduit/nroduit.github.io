---
title: Lookup Tables (LUT)
weight: 330
description: How to handle Color, VOI and Presentation LUTs
keywords: [ "Lookup Tables", "LUT", "VOI LUT",  "Modality LUT", "Presentation LUT", "DICOM LUT", "DICOM VOI LUT", "DICOM Modality LUT", "DICOM Presentation LUT", "DICOM viewer", "free DICOM viewer"]
---

## <center>How to handle Color and DICOM LUTs</center>

A DICOM file can contain one or more LUTs. The [DICOM pipeline for rendering images](https://dicom.nema.org/medical/dicom/current/output/chtml/part04/sect_N.2.html) contains a number of stages where the LUTs are applied. There are 4 types of Lookup Tables (LUTs) in DICOM:
1. The [Modality LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.html) is used to transform the pixel values into the values of the modality (e.g. Hounsfield for CT).
2. The [Values of Interest (VOI) LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.2.html) is used to transform the modality values into a visible range that enhances specific anatomical structures or pathological conditions.
3. The [Presentation LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.6.html) is used to transform the intensity values into P-Values (presentation values are device-independent values related to human perception).
4. The [Palette Color LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.9.html) is used to transform the intensity gray values into color values with a pseudo color LUT.

{{% notice note %}}
The Modality LUT and the Palette Color LUT are applied automatically when they exist. There are no options in the User Interface to modify them.
{{% /notice %}}

### Windowing and Rendering
The Windowing and Rendering is a panel in the [_Image Tools_ of the DICOM 2D viewer](../dicom-2d-viewer/#image-tools). Some of the options described below are also available in the Lookup Table toolbar, in the main menu and in contextual menus.

* _Window:_ The range of pixel intensity values. The value can be changed when Window/Level is selected in [mouse actions](../dicom-2d-viewer/#toolbars) or by using the slider.
* _Level:_ The center of the range defined by Window. The value can be changed when Window/Level is selected in [mouse actions](../dicom-2d-viewer/#toolbars) or by using the slider.
* {{< svg-inline "static/tuto/icon/winLevel.svg" >}} _Preset:_ The possible items ordered according to the following list:
  * Empty item when the Window and level values are changed manually from slider or mouse actions. 
  * Window and level values or VOI LUT data from the DICOM file (ending with _[DICOM]_). The default value is the first _[DICOM]_ item if exists, otherwise _Auto Level [Image]_.
  * _Auto Level [Image]_  (always visible) which is the Window and level related to the full range of the pixel values
  * Specific values of Window and level for a modality type  (e.g. Lung for CT)
* _LUT Shape:_ The mapping ([transfer function](https://dicom.nema.org/medical/dicom/current/output/chtml/part17/chapter_Y.html)) between the input values and the display values can be linear, sigmoid and logarithmic. Default value is linear.
* {{< svg-inline "static/tuto/icon/lut.svg" >}} _LUT:_ A pseudo color LUT used to map the grayscale values to color. _Default (image)_ is the original image color model. Choosing a LUT from the toolbar or the menus is easier because the LUTs are displayed with a preview.
* {{< svg-inline "static/tuto/icon/inverseLut.svg" >}} allows you to invert the LUT.
* _Filter:_ The 2D filter is applied to the image before the LUT. The filter can be used to enhance the image quality or to highlight specific structures. The default value is _None_.

{{% notice tip %}}
In order to display the LUT on the image, select it from the [_Display_ panel](../dicom-2d-viewer/#display) on the right. The LUT color are associated to values that correspond to the Modality LUT values (e.g. Hounsfield values for CT) or to the pixel values for some imaging types.

Another way to see the windowing transformation is to display the [histogram](../histogram).
{{% /notice %}}
