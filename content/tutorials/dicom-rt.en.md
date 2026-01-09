---
title: DICOM RT Tools
weight: 220
description: How to display radiotherapy information
keywords: [ "dicom rt", "radiotherapy", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying radiotherapy information {{< svg-inline "static/tuto/icon/rt.svg" >}}</center>

The _RT Tool_ appears on the right panel when a CT exam (when linked with DICOM STRUCT, PLAN and DOSE) is displayed. Since {{% badge title="Version" %}}4.1.0{{% /badge %}} a specific configuration in config.properties is no longer required.

### How to display structure and isodose
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
The region tree has context menus that allow you to:
* **Select/Unselect all the child nodes** (only for parent): Quickly toggle visibility for all subregions within a parent category
* **Fill opacity**: Controls the transparency of the region's interior relative to its border
    - Default value: 20%
    - Calculation: Final opacity = Line opacity × Fill opacity
    - Example: 80% line opacity + 20% fill opacity = 16% perceived interior opacity
* **Export to clipboard as CSV**: Exports comprehensive region data including volume measurements and dose calculations to CSV format via clipboard, enabling seamless integration with external analysis tools and spreadsheet applications.
* **Pixel statistics from the selected view** (only for leaf): Analyzes pixel values within the region boundaries
    - Provides comprehensive statistical data for the enclosed area
    - For detailed parameter definitions, refer to [Pixel Statistics](draw-measure/#selected-measurement)
{{% /notice %}}


For displaying the isodoses, apply the following points (see in the image below):

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

