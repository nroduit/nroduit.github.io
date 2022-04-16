---
title: Launch Weasis
description: Various DICOM samples for testing the viewer capabilities
keywords: [ "weasis demo", "dicom sammples", "dicom examples", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>Demo with multiple DICOM Samples</center>

This page shows a list of DICOM samples for testing viewer capabilities.

{{% notice tip %}}
**Naming convention**

- Patient name starting with "TEST^" and then the general test purpose. "TEST-i18n-" prefix is for internationalization test.
- In study description: general test description
- In series description: test description
{{% /notice %}}

### How to launch Weasis

To display the DICOM samples on this page, you need to install a [recent version of Weasis](../getting-started/).

{{% notice tip %}}
Clicking on the "Launch" button launches Weasis and displays the selected images, or if Weasis is already open then the images are added to a new tab in the main view.
{{% /notice %}}

------------------------------------------------------------------------

#### Internationalized characters
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Finternational.xml" class="btn btn-default">Launch</a>

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
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpixel-depth-unsigned.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Signed data
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpixel-depth-signed.xml" class="btn btn-default">Launch</a>
</li>
</ul>

------------------------------------------------------------------------

#### Compression

<ul>
<li style="margin-bottom:10px;">Different compression syntaxes (JPEG, JPEG-Lossless, JPEG-LS, J2K, RLE)
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fcompression1.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Compression and fragments (the file contains the encoded pixel data stream fragmented into several parts, see <a target="_blank" href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_A.4.html">DICOM part5</a>)
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fcompression2.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Compression, multi-frame and fragments
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fcompression3.xml" class="btn btn-default">Launch</a>
</li>
</ul>
------------------------------------------------------------------------

#### Photometric Interpretation
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fcolor.xml" class="btn btn-default">Launch</a>

------------------------------------------------------------------------

#### Pixel Spacing
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpixel-spacing.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Select the view and press 'd' to draw a line.
{{% /notice %}}

------------------------------------------------------------------------

#### Pixel Padding Value
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpixel-padding.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Show or hide pixel padding from the "Display" right pane.
{{% /notice %}}

------------------------------------------------------------------------

#### Non-square pixels
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpixel-nonsquare.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Stretch or shrink the image according to the "pixel spacing" or "pixel aspect ratio" field.
{{% /notice %}}

------------------------------------------------------------------------

#### Overlay
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Foverlay.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Show or hide from the "Display" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### Modality LUT
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fmlut.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Should always render the same image.
{{% /notice %}}

------------------------------------------------------------------------

#### VOI LUT
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fvlut.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Can be changed in the "Image Tool" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### Combined LUT
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fclut.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Should always render the same image.
{{% /notice %}}

------------------------------------------------------------------------

#### Shutter
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fshutter.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Show or hide from the "Display" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM PDF
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpdf.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Open by the default PDF viewer of the operating system.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM video
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fvideo.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Open by the default viewer (associated to the video mime type) of the operating system.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Audio (AU)
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Faudio.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Open by the embedded Java Audio Player.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM floating point pixel data
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Ffloat.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
 Specific dicom pixel data containing float or double.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Structured Report (SR)
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fsr.xml" class="btn btn-default">Launch</a>

------------------------------------------------------------------------

#### DICOM Presentation State (PR, GSPS)

{{% notice info %}}
Click on the right icon over the image to select the Presentation State. Show or hide graphics layers from the "Display" right panel. See [How to build DICOM PR](../tutorials/build-ko-pr/#presentation-state-pr-or-gsps).
{{% /notice %}}

<ul>
<li style="margin-bottom:10px;">Shutter Test <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-shutter.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Text Annotation <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-text.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Displayed Area <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-area.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Modality LUT PState <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-mlut.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">VOI LUT PState <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-vlut.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Presentation LUT PState <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-plut.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Combined LUT PState <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-clut.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Spatial Transformation <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-spatial.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Overlay <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-overlay.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Graphics Annotation <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-graphics.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">Complex Combination <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-commplex.xml" class="btn btn-default">Launch</a>
</li>
<li style="margin-bottom:10px;">GE RA600 Test of CPI GSPS <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fpr-ge.xml" class="btn btn-default">Launch</a>
  {{% notice note %}}
  This sample is produced by a GE workstation and contains some proprietary items (so not all PRs can be applied)
  {{% /notice %}}
</li>
</ul>
------------------------------------------------------------------------

#### DICOM Key Object Selection (KO)
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fdemo%2Fko.xml" class="btn btn-default">Launch</a>

{{% notice info %}}
Click on the right icon over the image to select the Key Object Selection. See [How to build and export DICOM KO](../tutorials/build-ko-pr).
{{% /notice %}}
