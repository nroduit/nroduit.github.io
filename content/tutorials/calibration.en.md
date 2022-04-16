---
title: Spatial Calibration
weight: 450
description: How to change the spatial calibration of an image or a series
keywords: [ "image calibration", "spatial calibration", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to change the spatial calibration</center>

When the image does not contain a default spatial calibration and it contains a ruler (or other element allowing to determine a known distance) then you can apply a calibration manually:

1. Select a line in the *Measurement Tool*
2. Draw a line on an object with a known distance
3. Right-click on the selected line and enter the distance on the *Manual Calibration* window

![Calibration](/tuto/spatial-calibration.jpg?classes=shadow&width=700px)

![Apply Calibration](/tuto/apply-calibration.png?classes=shadow)

{{% notice note %}}
The calibration can be applied only to the current image or to all the images belonging to the series.
{{% /notice %}}