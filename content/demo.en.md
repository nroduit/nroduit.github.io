---
title: Launch Weasis
description: Various DICOM samples for testing the viewer capabilities
keywords: [ "weasis demo", "dicom samples", "dicom examples", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
hidden: true
---

## <center>Demo with multiple DICOM Samples</center>

This page provides a list of DICOM samples to test the capabilities of the viewer.

{{% notice tip %}}
**Naming convention**

- Patient name starting with "TEST^" and then the general test purpose. "TEST-i18n-" prefix is for internationalization test.
- In study description: general test description
- In series description: test description
{{% /notice %}}

### How to launch Weasis

In order to display the DICOM samples on this page, you must install a [recent version of Weasis](../getting-started/).

{{% notice tip %}}
By clicking on the "Launch" button, Weasis starts and displays the related images, or if Weasis is already open, the images are added to a new tab in the main view.
{{% /notice %}}

------------------------------------------------------------------------

#### Internationalized characters
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/international.xml"
{{< /launch >}}

{{% notice info %}}
Should display:
![charset samples](/images/charset.png)
{{% /notice %}}

------------------------------------------------------------------------

#### Pixel depth (from 9-bit to 16-bit)

{{% notice info %}}
Should always render the same image.
{{% /notice %}}

<ul>
<li style="margin-bottom:10px;">Unsigned data
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pixel-depth-unsigned.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Signed data
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pixel-depth-signed.xml"
{{< /launch >}}
</li>
</ul>

------------------------------------------------------------------------

#### Compression

<ul>
<li style="margin-bottom:10px;">Different compression syntaxes (JPEG, JPEG-Lossless, JPEG-LS, J2K, RLE)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/compression1.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Compression and fragments (the file contains the encoded pixel data stream fragmented into several parts, see <a target="_blank" href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_A.4.html">DICOM part5</a>)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/compression2.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Compression, multi-frame and fragments
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/compression3.xml"
{{< /launch >}}
</li>
</ul>

------------------------------------------------------------------------

#### Photometric Interpretation
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/color.xml"
{{< /launch >}}

------------------------------------------------------------------------

#### Pixel Spacing
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pixel-spacing.xml"
{{< /launch >}}

{{% notice info %}}
Select the view and press 'd' to draw a line.
{{% /notice %}}

------------------------------------------------------------------------

#### Pixel Padding Value
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pixel-padding.xml"
{{< /launch >}}

{{% notice info %}}
Show or hide pixel padding from the "Display" right pane.
{{% /notice %}}

------------------------------------------------------------------------

#### Non-square pixels
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pixel-nonsquare.xml"
{{< /launch >}}

{{% notice info %}}
Stretch or shrink the image according to the "pixel spacing" or "pixel aspect ratio" field.
{{% /notice %}}

------------------------------------------------------------------------

#### Overlay
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/overlay.xml"
{{< /launch >}}

{{% notice info %}}
Show or hide from the "Display" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### Modality LUT
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/mlut.xml"
{{< /launch >}}

{{% notice info %}}
Should always render the same image.
{{% /notice %}}

------------------------------------------------------------------------

#### VOI LUT
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/vlut.xml"
{{< /launch >}}

{{% notice info %}}
VOI LUT can be changed in the "Image Tool" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### Combined LUT
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/clut.xml"
{{< /launch >}}

{{% notice info %}}
Should always render the same image.
{{% /notice %}}

------------------------------------------------------------------------

#### Shutter
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/shutter.xml"
{{< /launch >}}

{{% notice info %}}
Show or hide from the "Display" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM PDF
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pdf.xml"
{{< /launch >}}

{{% notice info %}}
Open the default PDF viewer of the operating system.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM video
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/video.xml"
{{< /launch >}}

{{% notice info %}}
Open the default viewer (associated to the video mime type) of the operating system.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Audio (AU)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/audio.xml"
{{< /launch >}}

{{% notice info %}}
Open the embedded Java Audio Player.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM floating point pixel data
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/float.xml"
{{< /launch >}}

{{% notice info %}}
Specific dicom pixel data containing float or double. Floating values must be supported by the Window/Level tools.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Structured Report (SR)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/sr.xml"
{{< /launch >}}

{{% notice info %}}
The DICOM SR is formatted according to the order and hierarchy of the tags.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Presentation State (PR, GSPS)

{{% notice info %}}
Click on the right icon over the image to select the Presentation State. See [How to build DICOM PR](../tutorials/build-ko-pr/#presentation-state-pr-or-gsps).
{{% /notice %}}

<ul>
<li style="margin-bottom:10px;">Shutter Test {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-shutter.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Text Annotation {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-text.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Displayed Area {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-area.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Modality LUT PState {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-mlut.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">VOI LUT PState {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-vlut.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Presentation LUT PState {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-plut.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Combined LUT PState {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-clut.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Spatial Transformation {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-spatial.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Overlay {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-overlay.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Graphics Annotation {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-graphics.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Complex Combination {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-commplex.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">GE RA600 Test of CPI GSPS {{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/pr-ge.xml"
{{< /launch >}}
  {{% notice note %}}
  This sample is produced by a GE workstation and contains some proprietary items (so not all PRs can be applied)
  {{% /notice %}}
</li>
</ul>

------------------------------------------------------------------------

#### DICOM Key Object Selection (KO)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/samples/demo/ko.xml"
{{< /launch >}}

{{% notice info %}}
Click on the right icon over the image to select the Key Object Selection. See [How to build and export DICOM KO](../tutorials/build-ko-pr).
{{% /notice %}}
