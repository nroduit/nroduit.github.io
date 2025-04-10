---
title: DICOM RT Tools
weight: 220
description: How to display radiotherapy information
keywords: [ "dicom rt", "radiotherapy", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying radiotherapy information {{< svg-inline "static/tuto/icon/rt.svg" >}}</center>

The _RT Tool_ appears on the right panel when a CT exam (when linked with DICOM STRUCT, PLAN and DOSE) is displayed. Since {{% badge title="Version" %}}4.1.0{{% /badge %}} a specific configuration in config.properties is no longer required.

### How to display structure and iso-dose
In order to display the structures in overlay on the image, apply the following points (see in the image below):

1. {{% badge style="info" %}}Optional{{% /badge %}} When selected, it allows you to force the DVH calculations. Otherwise, it is calculated only if some information is not available in the DICOM files.
2. Click on "_Load RT_" button to load DICOM STRUCT, PLAN and DOSE associated the CT images. Once loaded, the button becomes inactive.
3. {{% badge style="info" %}}Optional{{% /badge %}} Select a structure if there is more than one.
4. {{% badge style="info" %}}Optional{{% /badge %}} Select a plan if there is more than one.

Try to open an RT sample {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/rt.xml"
{{< /launch >}}

![DICOM STRUCT](/tuto/dicom-rt-struct.jpg?classes=shadow)
<br>

{{% notice note %}}
The "Structures" tree has the same options as DICOM SEG regions, see [DICOM Segmentation](../dicom-segmentation/#how-to-display-dicom-seg).

See also the use of DICOM RT as [artificial intelligence output](../dicom-artificial-intelligence/#dicom-rtstruct).

{{% /notice %}}


For displaying the iso-doses, apply the following points (see in the image below):

1. Select the _Isodoses_ tab
2. Check the _Isodoses_ root node which is not activated by default
3. {{% badge style="info" %}}Optional{{% /badge %}} Adjust the graphic opacity

![DICOM DOSE](/tuto/dicom-rt-dose.jpg?classes=shadow)
<br>

{{% notice tip %}}
The "Structures" and "Isodoses" root node can be used to show or hide all graphics while the child nodes can be used independently for showing specific items.
{{% /notice %}}


### How to display DVH
* Select one or several structures. Note: the _Structures_ root node must be selected.
* Click on the button "_Display DVH chart_"
* Right-click on the chart to print or save as a PNG image or vector files such as SVG or EPS.

![DICOM DVH](/tuto/dicom-rt-dvh.jpg?classes=shadow)
<br>

