---
title: Spatial Calibration
weight: 380
description: How to change the spatial calibration of an image or a series
keywords: [ "image calibration", "spatial calibration", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to change the spatial calibration</center>

When the image does not contain a default spatial calibration and it contains a ruler (or other element allowing to determine a known distance), then you can apply a calibration manually:

1. Select a line in the *Measurement Tool*
2. Draw a line on an object with a known distance
3. Right-click on the selected line and enter the distance on the *Manual Calibration* window

![Calibration](/tuto/spatial-calibration.jpg?classes=shadow&width=700px)
<br>
![Apply Calibration](/tuto/apply-calibration.png?classes=shadow)
<br>
{{% notice note %}}
The calibration can be applied only to the current image or to all the images belonging to the series.
{{% /notice %}}

{{% notice info %}}
Once calibrated, all measuring tools will produce results according to the calibration, and the [real-world zoom](../zoom/#real-world-zoom) will display the images at the same size of the real objects. Currently, the calibration is not saved in the DICOM file.
{{% /notice %}}

### Changing spacial calibration with Weasis 1.1.3
{{< youtube id="v8CgcpYT1r8" >}}
