---
title: Launch Weasis
description: Explore DICOM samples to test and showcase the capabilities of the Weasis viewer.
keywords: [ "weasis demo", "dicom samples", "dicom examples", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
hidden: true
---

## <center>Demo: Multiple DICOM Samples</center>

This page offers a variety of DICOM samples to test and evaluate the features and functionality of the Weasis DICOM viewer.

The datasets are sourced mainly from the [DICOM standard repository](ftp://medical.nema.org/MEDICAL/Dicom/DataSets) and the publication [DICOM Image Display Consistency: A Test Environment](https://www.researchgate.net/publication/239747992_DICOM_image_display_consistency_a_test_environment).

{{% notice tip %}}
**Naming conventions**

- **Patient Name**: Begins with "TEST^", followed by the general test purpose. Prefix "TEST-i18n-" indicates internationalization testing.
- **Study Description**: Describes the overall test specifics.
- **Series Description**: Details the specific test purpose related to the series.
{{% /notice %}}

### How to launch Weasis

In order to view the DICOM samples, ensure you’ve installed the [latest version of Weasis](../getting-started/).

{{% notice tip %}}
Clicking the **"Launch"** button will open Weasis and display the corresponding images. If Weasis is already running, the dataset will load in a new tab.
{{% /notice %}}

### DICOM Testing Categories and Samples

Below are test examples to explore the capabilities of Weasis. Click `Launch` to load the associated dataset. Here are the categories:

- [Internationalized Characters](#internationalized-characters)
- [Pixel Depth (9-bit to 16-bit)](#pixel-depth-9-bit-to-16-bit)
- [Compression Tests](#compression-tests)
- [Photometric Interpretation](#photometric-interpretation)
- [Pixel Spacing](#pixel-spacing)
- [Pixel Padding Value](#pixel-padding-value)
- [Non-Square Pixels](#non-square-pixels)
- [Overlay](#overlay)
- [Modality LUT](#modality-lut)
- [VOI LUT](#voi-lut)
- [Combined LUT](#combined-lut)
- [DICOM Shutter](#dicom-shutter)
- [DICOM PDF](#dicom-pdf)
- [DICOM video](#dicom-video)
- [DICOM Audio (AU)](#dicom-audio-au)
- [DICOM floating point pixel data](#dicom-floating-point-pixel-data)
- [DICOM Structured Report (SR)](#dicom-structured-report-sr)
- [DICOM Presentation State (PR, GSPS)](#dicom-presentation-state-pr-gsps)
- [DICOM Key Object Selection (KO)](#dicom-key-object-selection-ko)

------------------------------------------------------------------------

#### Internationalized Characters
Test international character sets in patient and study data.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/international.xml"
{{< /launch >}}

{{% notice info %}}
Expected Output:
![charset samples](/images/charset.png)
{{% /notice %}}

------------------------------------------------------------------------

#### Pixel Depth (9-bit to 16-bit)

Tests with different pixel depths to ensure correct image rendering.

{{% notice info %}}
**Expected Output**: Images rendered identically regardless of pixel depth.
{{% /notice %}}

<ul>
<li style="margin-bottom:10px;">Unsigned Data
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pixel-depth-unsigned.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Signed Data
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pixel-depth-signed.xml"
{{< /launch >}}
</li>
</ul>

------------------------------------------------------------------------

#### Compression Tests
Evaluate viewer performance with various compression types.

<ul>
<li style="margin-bottom:10px;">Different Compression Syntaxes (JPEG, JPEG-Lossless, JPEG-LS, J2K, RLE)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/compression1.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Compression and fragments (the file contains the encoded pixel data stream fragmented into several parts, see <a target="_blank" href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_A.4.html">DICOM part5</a>)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/compression2.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Compression, Multi-frame, and Fragments Combined
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/compression3.xml"
{{< /launch >}}
</li>
</ul>

------------------------------------------------------------------------

#### Photometric Interpretation
Test multiple [photometric interpretations](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.3.html#sect_C.7.6.3.1.2) (color models, monochrome, and palette).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/color.xml"
{{< /launch >}}

------------------------------------------------------------------------

#### Pixel Spacing
Test the [pixel spacing](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_10.7.html#sect_10.7.1.3) with different modalities and measure the distance between pixels.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pixel-spacing.xml"
{{< /launch >}}

{{% notice info %}}
Select the view and press 'd' to draw a line and measure the pixel spacing. Follow the procedure displayed on the image that mentions the acceptable pixel spacing.
{{% /notice %}}

------------------------------------------------------------------------

#### Pixel Padding Value
Test the pixel [padding value ](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.5.html#sect_C.7.5.1.1.2) and its effect on the image.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pixel-padding.xml"
{{< /launch >}}

{{% notice info %}}
Toggle padding through the "Display" right pane. When padding is enabled, some pixel values are not considered for rendering.
{{% /notice %}}

------------------------------------------------------------------------

#### Non-Square Pixels
Test images with non-square pixels to ensure correct rendering.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pixel-nonsquare.xml"
{{< /launch >}}

{{% notice info %}}
Stretch or shrink the image according to the "pixel spacing" or "pixel aspect ratio" tag.
{{% /notice %}}

------------------------------------------------------------------------

#### Overlay
Test the rendering of [overlays](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.9.2.html) on images.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/overlay.xml"
{{< /launch >}}

{{% notice info %}}
Show or hide overlays from the "Display" right panel. 
{{% /notice %}}

------------------------------------------------------------------------

#### Modality LUT
Test the [Modality LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.html) and its effect on image rendering. See also [Lookup Tables (LUT)](../tutorials/lut).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/mlut.xml"
{{< /launch >}}

{{% notice info %}}
Should always render the same image.
{{% /notice %}}

------------------------------------------------------------------------

#### VOI LUT
Test the [VOI LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.2.html) and its effect on image rendering. See also [Lookup Tables (LUT)](../tutorials/lut).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/vlut.xml"
{{< /launch >}}

{{% notice info %}}
VOI LUT settings can be adjusted in the "Image Tool" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### Combined LUT
Test the combined effect of Modality LUT, VOI LUT and Presentation LUT on image rendering. See [Lookup Tables (LUT)](../tutorials/lut).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/clut.xml"
{{< /launch >}}

{{% notice info %}}
Consistently renders identical output regardless of applied LUT combinations.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Shutter
Test [DICOM shutters](https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.7.6.11.html) and their effect on image rendering.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/shutter.xml"
{{< /launch >}}

{{% notice info %}}
Show or hide shutters from the "Display" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM PDF
Test the rendering of DICOM PDF files.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pdf.xml"
{{< /launch >}}

{{% notice info %}}
Open the default PDF viewer of the operating system.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM video
Test the rendering of DICOM video files with different transfer syntaxes.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/video.xml"
{{< /launch >}}

{{% notice info %}}
Open the default viewer (associated to the video mime type) of the operating system.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Audio (AU)
Test the rendering of DICOM audio files.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/audio.xml"
{{< /launch >}}

{{% notice info %}}
Plays audio using the embedded Java Audio Player.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM floating point pixel data
Test DICOM pixel data containing float or double values.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/float.xml"
{{< /launch >}}

{{% notice info %}}
Specific dicom pixel data containing float or double. Floating values must be supported by the Window/Level tools.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Structured Report (SR)
Test the rendering of DICOM structured reports.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/sr.xml"
{{< /launch >}}

{{% notice info %}}
Structured reports formatted hierarchically using tag order. It can display links to images and associated graphics.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Presentation State (PR, GSPS)
Test the rendering of various DICOM presentation states.

{{% notice info %}}
Click on the right icon over the image to select the Presentation State. See [How to build DICOM PR](../tutorials/build-ko-pr/#presentation-state-pr-or-gsps).
{{% /notice %}}

<ul>
<li style="margin-bottom:10px;">Shutter Test {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-shutter.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Text Annotation {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-text.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Displayed Area {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-area.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Modality LUT PState {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-mlut.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">VOI LUT PState {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-vlut.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Presentation LUT PState {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-plut.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Combined LUT PState {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-clut.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Spatial Transformation {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-spatial.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Overlay {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-overlay.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Graphics Annotation {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-graphics.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Complex Combination {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-commplex.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">GE RA600 Test of CPI GSPS {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pr-ge.xml"
{{< /launch >}}
  {{% notice note %}}
  This sample is produced by a GE workstation and contains some proprietary items (so not all PRs can be applied)
  {{% /notice %}}
</li>
</ul>

------------------------------------------------------------------------

#### DICOM Key Object Selection (KO)
Test the rendering of DICOM key object selections. 

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/ko.xml"
{{< /launch >}}

{{% notice info %}}
Click on the right icon over the image to select the Key Object Selection. See [How to build and export DICOM KO](../tutorials/build-ko-pr/#key-object-selection-ko).
{{% /notice %}}
