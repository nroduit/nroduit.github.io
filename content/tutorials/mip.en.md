---
title: MIP Viewer
weight: 55
description: How to use the Maximum Intensity Projection (MIP) viewer
keywords: [ "MIP", "Maximum Intensity Projection", "dicom", "free dicom viewer" ]
---

## <center>Maximum Intensity Projection (MIP) {{< svg "static/tuto/icon/mip.svg" >}}</center>

The MIP viewer is a simple 3D viewer that allows to display the maximum intensity projection of a volume defined by a number of slice of the image stack. 

The MIP viewer is also available in the [3D viewer](../dicom-3d-viewer) with more advanced options of the volume rendering, but some [minimal hardware requirements](../dicom-3d-viewer/#requirements) is necessary.


### Open the MIP viewer
The MIP viewer can be opened with {{< svg "static/tuto/icon/mip.svg" >}} in the Basic 3D toolbar of the [DICOM 2D viewer](../dicom-2d-viewer).

{{% notice note %}}
If the button is grayed out, it means that the current series has less than 5 images which the minimal number of images for using the MIP viewer. 
{{% /notice %}}

### The MIP Options

This dialog is a modal window that allows you to change the MIP settings and build a new MIP series. 

Try to load a volume dataset and open the MIP viewer. {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/3d/head-neck.xml"
{{< /launch >}}

![MIP Options](/tuto/mip-options.png?classes=shadow)
<br>

{{% notice note %}}
In MIP mode, the volume is displayed as a 2D projection of the maximum intensity along the perpendicular axis of the image plane. This change in geometry means that overlay graphics are no longer displayed.
{{% /notice %}}

#### Projection type
The projection type defines the way the MIP is calculated. The options are:
* **Min**: Minimum Intensity Projection
* **Mean**: Mean Intensity Projection
* **Max**: Maximum Intensity Projection (the default value)


#### Slice position
The slice position is used to move around the series to apply the projection and display the result. The _Image_ value represents the position in the series stack.

#### Slice thickness
The _Image Extension_ value represents the number of slices to use for the MIP calculation. If the images are calibrated and contains the 3D position, the thickness is also displayed in millimeters.

#### Rebuild Series
It allows you to build a new MIP series according to the MIP options. In this new series the slice position and thickness are modified. 

The new MIP series is added to the [DICOM explorer](../dicom-explorer/) and can be [exported](../dicom-export/#dicom-exporting).