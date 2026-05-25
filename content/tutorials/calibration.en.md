---
title: Spatial Calibration
weight: 380
description: How to change the spatial calibration of an image or a series
keywords: [ "image calibration", "spatial calibration", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to change the spatial calibration</center>

**Spatial calibration** is the link between a pixel and a real-world length. With a valid calibration, every [measurement](draw-measure) (distance, area, angle) reflects actual millimeters or centimeters, and the [real-world zoom](zoom/#real-world-size-display) can display images at the same size as the original objects.

For DICOM images, the calibration is normally derived from the standard attributes (_Pixel Spacing_ for cross-sectional acquisitions, _Imager Pixel Spacing_ for projection radiography). The 2D viewer indicates how the calibration was obtained — see the [calibration type label](dicom-2d-viewer/#open-the-2d-viewer) shown above the ruler.

When no calibration is available — or when you want to override an existing one — you can apply a **manual calibration** as long as the image contains a reference object of known size (a ruler, a fiducial, a calibration phantom, or any landmark whose physical length you know).

### Manual calibration procedure

1. Pick the **Line** tool from the [Measurement tools](draw-measure/#measurement-tools).
2. Draw a line along an object whose real-world length you know.
3. **Right-click** the line and choose **Manual Calibration**.
4. Enter the known distance (with its unit) in the dialog and confirm.

![Calibration](/tuto/spatial-calibration.jpg?classes=shadow&width=700px)
<br>

![Apply Calibration](/tuto/apply-calibration.png?classes=shadow)
<br>

{{% notice note %}}
The Manual Calibration dialog can apply the new scale either to the **current image only** or to **every image in the series**. Pick the right scope for your dataset (a series with consistent geometry is normally calibrated as a whole).
{{% /notice %}}

{{% notice info %}}
Once the image is calibrated, all measurement tools report values in the chosen unit and the [real-world zoom](zoom/#real-world-size-display) renders the image at its physical size. The manual calibration is kept in memory for the current session but is **not currently written back into the DICOM file**.
{{% /notice %}}

### Changing spatial calibration with Weasis 1.1.3
The procedure shown below was recorded on an older version of Weasis; the underlying workflow is unchanged.
{{< youtube id="v8CgcpYT1r8" >}}