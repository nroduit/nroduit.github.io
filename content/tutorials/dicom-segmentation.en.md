---
title: DICOM SEG
weight: 337
description: How to display the DICOM Segmentation file
keywords: [ "dicom seg", "segmentation", "SEG", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying DICOM Segmentation {{< svg-inline "static/tuto/icon/segmentation.svg" >}}</center>

Since Weasis {{% badge title="Version" %}}4.3.0{{% /badge %}}, this panel lets you display the contents of a DICOM SEG file superimposed on the image. It also lets you modify the transparency of specific regions (label defined by a color).

DICOM SEG can be generated by [AI frameworks](../dicom-artificial-intelligence) to represent the results of segmentation algorithms applied to medical images.

### How to display DICOM SEG
In order to display the DICOM SEG regions in overlay on the image, follow these steps (see in the image below):

1. Open the DICOM series with a link to a DICOM SEG object. This link is visible by the segmentation icon {{< svg-inline "static/tuto/icon/segmentation.svg" >}} in the lower right-hand corner of the thumbnail.
2. Once the image is displayed, you can click on {{< svg-inline "static/tuto/icon/normalize.svg" >}} of the vertical button {{< svg-inline "static/tuto/icon/segmentation.svg" >}} to show the _Segmentation_ panel on the right side of the viewer.
3. A DICOM SEG file is represented by a selected item in the combo box and its list of regions below. By default, all DICOM SEG files linked to an image are displayed.
4. Select one or several regions to display for the selected DICOM SEG (3). Several regions are grouped together when they share the same first name. Note: the parent node must be selected to display the child regions.
5. Adjust global graphic opacity (border and interior)

Try to open an SEG sample {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/seg.xml"
{{< /launch >}}

![DICOM SEG](/tuto/dicom-seg.jpg?classes=shadow&width=780px)
<br>

{{% notice note %}}
The region tree has context menus that allow you to:
* **Select/Unselect all the child nodes** (only for parent): Quickly toggles visibility for all subregions within a parent category. Unchecking only the parent makes all children invisible.
* **Fill opacity**: Controls the transparency of the region's interior relative to its border
    - Default value: 20%
    - Calculation: Final opacity = Line opacity × Fill opacity
    - Example: 80% line opacity + 20% fill opacity = 16% perceived interior opacity
* **Show in the image view** (only for leaf): Displays the region with the largest surface area in the image view
* **Pixel statistics from the selected view** (only for leaf): Analyzes pixel values within the region boundaries
    - Provides comprehensive statistical data for the enclosed area
    - For detailed parameter definitions, refer to [Pixel Statistics](../draw-measure/#selected-measurement)
{{% /notice %}}

{{% notice tip %}}
The region tree has tooltips on leaf elements that show the region description and the region volume.
{{% /notice %}}





