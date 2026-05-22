---
title: Launch Weasis
description: Explore DICOM samples to test and showcase the capabilities of the Weasis viewer.
keywords: [ "weasis demo", "dicom samples", "dicom examples", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
hidden: true
---

## <center>Demo: Multiple DICOM Samples</center>

This page collects a curated set of DICOM samples designed to exercise the rendering pipeline, the input formats, and the headline features of the Weasis DICOM viewer. Each sample loads in one click and is annotated with the test it is meant to demonstrate, along with the expected viewer behavior.

The datasets are sourced mainly from the [DICOM standard repository](ftp://medical.nema.org/MEDICAL/Dicom/DataSets) and the publication [DICOM Image Display Consistency: A Test Environment](https://www.researchgate.net/publication/239747992_DICOM_image_display_consistency_a_test_environment).

{{% notice tip %}}
**Sample naming conventions**

- **Patient Name** — begins with `TEST^`, followed by the general test purpose. A `TEST-i18n-` prefix indicates an internationalization test.
- **Study Description** — describes the overall test focus.
- **Series Description** — details the specific test purpose of that series.
{{% /notice %}}

### How to launch Weasis

To view a DICOM sample, make sure you have installed the [latest version of Weasis](getting-started/).

{{% notice tip %}}
Clicking a **Launch** button opens Weasis and displays the sample. If Weasis is already running, the dataset loads in a new tab.
{{% /notice %}}

### DICOM testing categories and samples

The samples below exercise specific parts of the DICOM standard and the Weasis rendering pipeline. Click **Launch** to load a dataset.

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
- [DICOM Video](#dicom-video)
- [DICOM Audio (AU)](#dicom-audio-au)
- [DICOM Floating-Point Pixel Data](#dicom-floating-point-pixel-data)
- [DICOM Structured Report (SR)](#dicom-structured-report-sr)
- [DICOM Presentation State (PR, GSPS)](#dicom-presentation-state-pr-gsps)
- [DICOM Key Object Selection (KO)](#dicom-key-object-selection-ko)

------------------------------------------------------------------------

#### Internationalized Characters
Test international character sets in patient and study identifiers.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/international.xml"
{{< /launch >}}

{{% notice info %}}
**Expected output**:
![charset samples](/images/charset.png)
{{% /notice %}}

------------------------------------------------------------------------

#### Pixel Depth (9-bit to 16-bit)

Verify that images render identically regardless of the underlying pixel depth (signed or unsigned, 9 to 16 bits per sample).

{{% notice info %}}
**Expected output**: images render identically regardless of the pixel depth.
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
Exercise the decoder against the main DICOM transfer syntaxes and fragmentation scenarios.

<ul>
<li style="margin-bottom:10px;">Different compression syntaxes (JPEG, JPEG-Lossless, JPEG-LS, J2K, RLE)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/compression1.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Compression with fragments (the encoded pixel-data stream is split into several fragments, see <a target="_blank" href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_A.4.html">DICOM Part 5</a>)
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/compression2.xml"
{{< /launch >}}
</li>
<li style="margin-bottom:10px;">Compression + multi-frame + fragments combined
{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/compression3.xml"
{{< /launch >}}
</li>
</ul>

------------------------------------------------------------------------

#### Photometric Interpretation
Test multiple [photometric interpretations](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.3.html#sect_C.7.6.3.1.2) (color models, monochrome, and palette color).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/color.xml"
{{< /launch >}}

------------------------------------------------------------------------

#### Pixel Spacing
Test the [pixel spacing](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_10.7.html#sect_10.7.1.3) on different modalities by measuring the distance between known landmarks. See also [Spatial Calibration](tutorials/calibration).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pixel-spacing.xml"
{{< /launch >}}

{{% notice info %}}
Select the view and press **D** (default — see [Keyboard Shortcuts](basics/shortcuts) to customize) to draw a line and measure the distance. Follow the on-image procedure that lists the acceptable pixel-spacing range.
{{% /notice %}}

------------------------------------------------------------------------

#### Pixel Padding Value
Test the [pixel padding value](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.5.html#sect_C.7.5.1.1.2) and its effect on the image.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pixel-padding.xml"
{{< /launch >}}

{{% notice info %}}
Toggle padding from the **Display** right-side panel. When padding is enabled, the marked pixel values are excluded from rendering.
{{% /notice %}}

------------------------------------------------------------------------

#### Non-Square Pixels
Test images with non-square pixels to verify correct stretching.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pixel-nonsquare.xml"
{{< /launch >}}

{{% notice info %}}
The viewer should stretch or shrink the image according to the **Pixel Spacing** or **Pixel Aspect Ratio** tag.
{{% /notice %}}

------------------------------------------------------------------------

#### Overlay
Test the rendering of [DICOM overlays](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.9.2.html) on top of the image.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/overlay.xml"
{{< /launch >}}

{{% notice info %}}
Show or hide overlays from the **Display** right-side panel.
{{% /notice %}}

------------------------------------------------------------------------

#### Modality LUT
Test the [Modality LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.html) and its effect on image rendering. See also [Lookup Tables (LUT)](tutorials/lut).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/mlut.xml"
{{< /launch >}}

{{% notice info %}}
**Expected output**: every variant should render the same image.
{{% /notice %}}

------------------------------------------------------------------------

#### VOI LUT
Test the [VOI LUT](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.2.html) and its effect on image rendering. See also [Lookup Tables (LUT)](tutorials/lut).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/vlut.xml"
{{< /launch >}}

{{% notice info %}}
VOI LUT settings can be adjusted in the **Image Tools** right-side panel.
{{% /notice %}}

------------------------------------------------------------------------

#### Combined LUT
Test the combined effect of Modality LUT, VOI LUT, and Presentation LUT on image rendering. See [Lookup Tables (LUT)](tutorials/lut).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/clut.xml"
{{< /launch >}}

{{% notice info %}}
**Expected output**: identical rendering regardless of which LUT combination is applied.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Shutter
Test [DICOM shutters](https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.7.6.11.html) and their effect on image rendering.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/shutter.xml"
{{< /launch >}}

{{% notice info %}}
Show or hide shutters from the **Display** right-side panel.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM PDF
Test the handling of DICOM-encapsulated PDF files.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/pdf.xml"
{{< /launch >}}

{{% notice info %}}
Opens with the default PDF viewer of the operating system.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Video
Test the rendering of DICOM video files with different transfer syntaxes.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/video.xml"
{{< /launch >}}

{{% notice info %}}
Opens with the default viewer associated with the video MIME type. On Windows, this is Windows Media Player, which does **not** ship with an MPEG-2 codec by default — install VLC or another video player if playback fails.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Audio (AU)
Test the handling of DICOM audio files. See also [DICOM Audio Player](tutorials/dicom-audio).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/audio.xml"
{{< /launch >}}

{{% notice info %}}
Plays audio with the embedded Java Audio Player.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Floating-Point Pixel Data
Test DICOM pixel data carrying **float** or **double** values (used by parametric maps, AI probability maps, perfusion / diffusion maps).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/float.xml"
{{< /launch >}}

{{% notice info %}}
**Expected output**: the float / double pixel values are supported by the Window / Level tools.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Structured Report (SR)
Test the rendering of DICOM Structured Reports. See also [DICOM SR Viewer](tutorials/dicom-sr).

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/sr.xml"
{{< /launch >}}

{{% notice info %}}
Structured reports are formatted hierarchically following the SR tag order. Links to images and associated graphics are clickable.
{{% /notice %}}

------------------------------------------------------------------------

#### DICOM Presentation State (PR, GSPS)
Test the rendering of various DICOM Presentation States.

{{% notice info %}}
Click the icon at the top-right of the image to select a Presentation State to apply. See [How to build DICOM PR](tutorials/build-ko-pr/#presentation-state-pr-or-gsps).
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
  This sample is produced by a GE workstation and contains some proprietary items, so not every PR can be applied.
  {{% /notice %}}
</li>
</ul>

------------------------------------------------------------------------

#### DICOM Key Object Selection (KO)
Test the rendering of DICOM Key Object Selections.

{{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/ko.xml"
{{< /launch >}}

{{% notice info %}}
Click the icon at the right of the image to select a Key Object Selection. See [How to build and export DICOM KO](tutorials/build-ko-pr/#key-object-selection-ko).
{{% /notice %}}