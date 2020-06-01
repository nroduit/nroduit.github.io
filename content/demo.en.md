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

{{% notice warning %}}
The demo server is on a free cloud system, so sometimes it requires to launch two times the viewer because the server has to wake up (is turned "idle" after a period of inactivity).
{{% /notice %}}

### How to launch Weasis

To display the DICOM samples on this page, you need to install a [recent version Weasis](../getting-started/).

{{% notice warning %}}
The version 3.5 and superior uses the [weasis protocol](../../getting-started/weasis-protocol) instead of Java Web Start because which has been removed from <a target="_blank" href="https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html#JDK-8185077">Java 11 release</a>.
{{% /notice %}}

------------------------------------------------------------------------

<!--  init lib for dropdown button -->
{{% launch-weasis-init %}}



#### Internationalized characters

{{% launch-weasis id="st-internationalized" params="studyUID=1.3.6.1.4.1.5962.1.2.0.1175775771.5714.0&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775771.5711.0&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775772.5717.0&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775771.5708.0&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775772.5726.0&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775772.5720.0&studyUID=1.3.51.0.7.11986030739.15242.20106.39861.48967.23056.44419&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775772.5723.0&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775772.5732.0&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775771.5702.0&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775772.5729.0&studyUID=1.3.6.1.4.1.5962.1.2.0.1175775771.5705.0" %}}

Should display:
![charset samples](/images/charset.png)

------------------------------------------------------------------------

#### Pixel depth (from 9-bit to 16-bit)

{{% notice info %}}
Should always render the same image.
{{% /notice %}}

<ul>
<li style="margin-bottom:10px;">Unsigned data
{{% launch-weasis id="st-unsigned" params="studyUID=1.3.6.1.4.1.5962.1.2.10.1073676931.29447.0&studyUID=1.3.6.1.4.1.5962.1.2.11.1073676943.29651.0&studyUID=1.3.6.1.4.1.5962.1.2.12.1073676957.153.0&studyUID=1.3.6.1.4.1.5962.1.2.13.1073676974.625.0&studyUID=1.3.6.1.4.1.5962.1.2.14.1073676983.853.0&studyUID=1.3.6.1.4.1.5962.1.2.15.1073676998.1323.0&studyUID=1.3.6.1.4.1.5962.1.2.16.1073677013.1817.0&studyUID=1.3.6.1.4.1.5962.1.2.9.1073676916.29073.0" %}}
</li>
<li style="margin-bottom:10px;">Signed data
{{% launch-weasis id="st-signed" params="studyUID=1.3.6.1.4.1.5962.1.2.10.1073676936.29494.0&studyUID=1.3.6.1.4.1.5962.1.2.11.1073676947.29791.0&studyUID=1.3.6.1.4.1.5962.1.2.12.1073676968.345.0&studyUID=1.3.6.1.4.1.5962.1.2.13.1073676981.726.0&studyUID=1.3.6.1.4.1.5962.1.2.15.1073677001.1422.0&studyUID=1.3.6.1.4.1.5962.1.2.14.1073676989.1033.0&studyUID=1.3.6.1.4.1.5962.1.2.16.1073677017.1876.0&studyUID=1.3.6.1.4.1.5962.1.2.9.1073676922.29189.0" %}}
</li>
</ul>

------------------------------------------------------------------------

#### Compression

<ul>
<li style="margin-bottom:10px;">Different compression syntaxes (JPEG, JPEG-Lossless, JPEG-LS, J2K, RLE)
{{% launch-weasis id="st-compression" params="studyUID=1.3.6.1.4.1.5962.1.2.8.20031208063649.855" %}}
</li>
<li style="margin-bottom:10px;">Compression and fragments (the file contains the encoded pixel data stream fragmented into several parts, see <a target="_blank" href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_A.4.html">DICOM part5</a>)
{{% launch-weasis id="st-compression-fr" params="studyUID=1.3.6.1.4.1.5962.1.2.17.20031208063649.855" %}}
</li>
<li style="margin-bottom:10px;">Compression, multi-frame and fragments
{{% launch-weasis id="st-compression-multi" params="studyUID=1.3.6.1.4.1.5962.1.2.5000.1166546115.14677" %}}
</li>
</ul>
------------------------------------------------------------------------

#### Photometric Interpretation
{{% launch-weasis id="st-photometric" params="studyUID=1.2.840.113619.2.98.3467.1098086125.0.69" %}}

------------------------------------------------------------------------

#### Pixel Spacing
{{% launch-weasis id="st-spacing" params="studyUID=1.3.6.1.4.1.5962.1.2.65535.20090407071000.6523764" %}}

{{% notice info %}}
Select the view and press 'd' to draw a line.
{{% /notice %}}

------------------------------------------------------------------------

#### Pixel Padding Value
{{% launch-weasis id="st-padding" params="studyUID=1.3.6.1.4.1.5962.1.2.11001.1139672893.9523.0" %}}

{{% notice info %}}
Show or hide pixel padding from the "Display" right pane.
{{% /notice %}}

------------------------------------------------------------------------

#### Non-square pixels
{{% launch-weasis id="st-square" params="studyUID=2.16.756.5.5.100.397184556.14391.1373576413.1508" %}}

{{% notice info %}}
Stretch or shrink the image according to the "pixel spacing" or "pixel aspect ratio" field.
{{% /notice %}}

------------------------------------------------------------------------

#### Overlay
{{% launch-weasis id="st-overlay" params="studyUID=1.2.124.113532.10.122.1.203.20051130.122937.2950157&studyUID=2.16.840.1.113669.632.20.1211.10000999666&studyUID=1.3.12.2.1107.5.3.3.5067.2011040518455806&studyUID=2.16.840.1.113669.632.20.1211.10001557400&studyUID=1.2.276.0.7230010.3.200.12" %}}
{{% notice info %}}
Show or hide from the "Display" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### Modality LUT
{{% launch-weasis id="st-mod-lut" params="studyUID=1.2.276.0.7230010.3.200.1" %}}

{{% notice info %}}
Should always render the same image.
{{% /notice %}}

------------------------------------------------------------------------

#### VOI LUT
{{% launch-weasis id="st-voi-lut" params="studyUID=1.2.276.0.7230010.3.200.2" %}}

{{% notice info %}}
Can be changed in the "Image Tool" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### Shutter
{{% launch-weasis id="st-shutter" params="studyUID=1.3.6.1.4.1.5962.1.1.0.0.0.1168612284.20369.0.1&studyUID=1.3.6.1.4.1.21367.0.1.13.1021" %}}

{{% notice info %}}
Show or hide from the "Display" right panel.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM PDF
{{% launch-weasis id="st-pdf" params="studyUID=1.2.840.113619.2.235.142733225228202183621236780&studyUID=1.3.6.1.4.1.5962.1.2.0.1359229044.2601.0" %}}

{{% notice info %}}
Open by the default PDF viewer of the operating system.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM video
{{% launch-weasis id="st-video" params="studyUID=1.3.51.0.7.633920140505.6339234439.633987.633918098&studyUID=1.2.124.113532.10.10.10.170.20030718.74251.568242" %}}

{{% notice info %}}
Open by the default viewer (associated to the video mime type) of the operating system.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Audio (AU)
{{% launch-weasis id="st-audio" params="studyUID=1.2.826.0.1.3680043.2.1396.999.20060722.113000.1" %}}

{{% notice info %}}
Open by the embedded Java Audio Player.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM floating point pixel data
{{% launch-weasis id="st-floating" params="studyUID=1.3.6.1.4.1.5962.99.1.1839181372.1275896472.1436358291004.4.0" %}}

------------------------------------------------------------------------

#### DICOM Structured Report (SR)
{{% launch-weasis id="st-sr" params="studyUID=1.3.6.1.4.1.5962.99.1.573361952.291015276.1289063583520.3.0&studyUID=1.2.276.0.7230010.3.1.2.1787205428.166.1117461927.29SAMPLES&studyUID=1.2.840.113674.514.212.200&studyUID=1.2.276.0.7230010.3.1.4.123456&studyUID=1.2.840.113654.2.4.4.3.4.119950730134200&studyUID=1.2.840.113663.19950725.1.0&studyUID=1.2.392.200036.9125.0.198811291108.7&studyUID=1.2.276.0.7230010.3.1.2.1787205428.166.1117461927.35&studyUID=1.2.276.0.7230010.3.1.2.1787205428.166.1117461927.32&studyUID=1.2.840.113680.3.103.775.2873347909.282313&studyUID=1.3.12.2.1107.5.8.1.123456789.199507271758050705910" %}}

------------------------------------------------------------------------

#### DICOM Presentation State (PR, GSPS)

{{% notice info %}}
Click on the right icon over the image to select the Presentation State. Show or hide graphics layers from the "Display" right panel. See [How to build DICOM PR](../tutorials/build-ko-pr/#presentation-state-pr-or-gsps).
{{% /notice %}}

<ul>
<li style="margin-bottom:10px;">Shutter Test {{% launch-weasis id="st-pr-shutter" params="studyUID=1.2.276.0.7230010.3.200.11" %}}
</li>
<li style="margin-bottom:10px;">Text Annotation {{% launch-weasis id="st-pr-text" params="studyUID=1.2.276.0.7230010.3.200.10" %}}
</li>
<li style="margin-bottom:10px;">Displayed Area {{% launch-weasis id="st-pr-area" params="studyUID=1.2.276.0.7230010.3.200.8" %}}
</li>
<li style="margin-bottom:10px;">Modality LUT PState{{% launch-weasis id="st-pr-modlut" params="studyUID=1.2.276.0.7230010.3.200.3" %}}
</li>
<li style="margin-bottom:10px;">VOI LUT PState {{% launch-weasis id="st-pr-voilut" params="studyUID=1.2.276.0.7230010.3.200.4" %}}
</li>
<li style="margin-bottom:10px;">Presentation LUT PState {{% launch-weasis id="st-pr-prlut" params="studyUID==1.2.276.0.7230010.3.200.5" %}}
</li>
<li style="margin-bottom:10px;">Combined LUT PState {{% launch-weasis id="st-pr-clut" params="studyUID=1.2.276.0.7230010.3.200.6" %}}
</li>
<li style="margin-bottom:10px;">Spatial Transformation {{% launch-weasis id="st-pr-trans" params="studyUID=1.2.276.0.7230010.3.200.7" %}}
</li>
<li style="margin-bottom:10px;">Overlay {{% launch-weasis id="st-pr-overlay" params="studyUID=1.2.276.0.7230010.3.200.12" %}}
</li>
<li style="margin-bottom:10px;">Graphics Annotation {{% launch-weasis id="st-pr-graphic" params="studyUID=1.2.276.0.7230010.3.200.9" %}}
</li>
<li style="margin-bottom:10px;">Complex Combination {{% launch-weasis id="st-pr-complex" params="studyUID=1.2.276.0.7230010.3.200.13" %}}
</li>
<li style="margin-bottom:10px;">GE RA600 Test of CPI GSPS {{% launch-weasis id="st-pr-ge" params="studyUID=1.2.124.113532.3.231.29.12.20020713.160823.3427" %}}
  {{% notice note %}}
  This sample is produced by a GE workstation and contains some proprietary items (so not all PRs can be applied)
  {{% /notice %}}
</li>
</ul>
------------------------------------------------------------------------

#### DICOM Key Object Selection (KO)

{{% launch-weasis id="st-ko" params="studyUID=1.2.840.113619.2.176.2025.1499492.7409.1172755464.916" %}}

{{% notice info %}}
Click on the right icon over the image to select the Key Object Selection. See [How to build and export DICOM KO](../tutorials/build-ko-pr).
{{% /notice %}}
