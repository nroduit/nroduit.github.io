---
title: DICOM Conformance
description: "What Weasis supports of the DICOM standard: the transfer syntaxes it can decode, the ones it can write on export, and the photometric interpretations it renders."
keywords: [ "dicom conformance statement", "supported transfer syntax", "dicom codec support", "jpeg 2000 dicom", "jpeg-ls", "jpeg-xl dicom", "photometric interpretation", "ihe" ]
weight: 70
---

## Compatibility of DICOM Transfer Syntax

This table lists the [DICOM Transfer Syntaxes](https://dicom.nema.org/medical/dicom/current/output/chtml/part06/chapter_A.html) supported by Weasis.

- **Read**: the pixel data is decoded and displayed by Weasis.
- **Write**: the syntax is offered when exporting to DICOM (see [DICOM Export](../tutorials/dicom-export)). Images in a syntax that is not offered are exported unchanged.

| Transfer Syntax UID     | Media Type | Description                                                                                                     | Read | Write |
|-------------------------|------------|-----------------------------------------------------------------------------------------------------------------|------|-------|
| 1.2.840.10008.1.2       |            | Implicit VR - Little Endian                                                                                     | yes  | No    |
| 1.2.840.10008.1.2.1     |            | Explicit VR - Little Endian                                                                                     | yes  | yes   |
| 1.2.840.10008.1.2.1.99  |            | Deflated Explicit VR Little Endian                                                                              | yes  | No    |
| 1.2.840.10008.1.2.2     |            | Explicit VR Big Endian (Retired)                                                                                | yes  | No    |
| 1.2.840.10008.1.2.5     |            | RLE (Run Length Encoding) Lossless                                                                              | yes  | No    |
| 1.2.840.10008.1.2.4.50  | image/jpeg | JPEG Baseline (Process 1): Default Transfer Syntax for Lossy JPEG 8 Bit Image Compression                       | yes  | yes   |
| 1.2.840.10008.1.2.4.51  | image/jpeg | JPEG Extended (Process 2 & 4): Default Transfer Syntax for Lossy JPEG 12 Bit Image Compression (Process 4 only) | yes  | yes   |
| 1.2.840.10008.1.2.4.53  | image/jpeg | JPEG Spectral Selection, Non-Hierarchical (Process 6 & 8) (Retired)                                             | yes  | No    |
| 1.2.840.10008.1.2.4.55  | image/jpeg | JPEG Full Progression, Non-Hierarchical (Process 10 & 12) (Retired)                                             | yes  | No    |
| 1.2.840.10008.1.2.4.57  | image/jpeg | JPEG Lossless, Non-Hierarchical (Process 14)                                                                    | yes  | No    |
| 1.2.840.10008.1.2.4.70  | image/jpeg | JPEG Lossless, Non-Hierarchical, First-Order Prediction (Process 14 [Selection Value 1])                        | yes  | yes   |
| 1.2.840.10008.1.2.4.80  | image/jls  | JPEG-LS Lossless Image Compression                                                                              | yes  | yes   |
| 1.2.840.10008.1.2.4.81  | image/jls  | JPEG-LS Lossy (Near-Lossless) Image Compression                                                                 | yes  | yes   |
| 1.2.840.10008.1.2.4.90  | image/jp2  | JPEG 2000 Image Compression (Lossless Only)                                                                     | yes  | yes   |
| 1.2.840.10008.1.2.4.91  | image/jp2  | JPEG 2000 Image Compression                                                                                     | yes  | yes   |
| 1.2.840.10008.1.2.4.92  | image/jpx  | JPEG 2000 Part 2 Multi-component Image Compression (Lossless Only)                                              | yes  | No    |
| 1.2.840.10008.1.2.4.93  | image/jpx  | JPEG 2000 Part 2 Multi-component Image Compression                                                              | yes  | No    |
| 1.2.840.10008.1.2.4.110 | image/jxl  | JPEG XL Lossless {{< since "4.6.4" >}}                                                                          | yes  | yes   |
| 1.2.840.10008.1.2.4.111 | image/jxl  | JPEG XL JPEG Recompression {{< since "4.6.4" >}}                                                                | yes  | yes   |
| 1.2.840.10008.1.2.4.112 | image/jxl  | JPEG XL {{< since "4.6.4" >}}                                                                                   | yes  | yes   |
| 1.2.840.10008.1.2.4.201 | image/jphc | High-Throughput JPEG 2000 Image Compression (Lossless Only)                                                     | yes  | No    |
| 1.2.840.10008.1.2.4.202 | image/jphc | High-Throughput JPEG 2000 with RPCL Options Image Compression (Lossless Only)                                   | yes  | No    |
| 1.2.840.10008.1.2.4.203 | image/jphc | High-Throughput JPEG 2000 Image Compression                                                                     | yes  | No    |

<br>

Video transfer syntaxes are not decoded by Weasis. The video stream is extracted to a temporary file and opened with the default video player of the operating system.

| Transfer Syntax UID       | Media Type | Description                                                          | Read | Write |
|---------------------------|------------|----------------------------------------------------------------------|------|-------|
| 1.2.840.10008.1.2.4.100   | video/mpeg | MPEG-2 Main Profile Main Level                                       | yes  | No    |
| 1.2.840.10008.1.2.4.100.1 | video/mpeg | Fragmentable MPEG-2 Main Profile Main Level                          | yes  | No    |
| 1.2.840.10008.1.2.4.101   | video/mpeg | MPEG-2 Main Profile High Level                                       | yes  | No    |
| 1.2.840.10008.1.2.4.101.1 | video/mpeg | Fragmentable MPEG-2 Main Profile High Level                          | yes  | No    |
| 1.2.840.10008.1.2.4.102   | video/mp4  | MPEG-4 AVC/H.264 High Profile / Level 4.1                            | yes  | No    |
| 1.2.840.10008.1.2.4.102.1 | video/mp4  | Fragmentable MPEG-4 AVC/H.264 High Profile / Level 4.1               | yes  | No    |
| 1.2.840.10008.1.2.4.103   | video/mp4  | MPEG-4 AVC/H.264 BD-compatible High Profile / Level 4.1              | yes  | No    |
| 1.2.840.10008.1.2.4.103.1 | video/mp4  | Fragmentable MPEG-4 AVC/H.264 BD-compatible High Profile / Level 4.1 | yes  | No    |
| 1.2.840.10008.1.2.4.104   | video/mp4  | MPEG-4 AVC/H.264 High Profile / Level 4.2 For 2D Video               | yes  | No    |
| 1.2.840.10008.1.2.4.104.1 | video/mp4  | Fragmentable MPEG-4 AVC/H.264 High Profile / Level 4.2 For 2D Video  | yes  | No    |
| 1.2.840.10008.1.2.4.105   | video/mp4  | MPEG-4 AVC/H.264 High Profile / Level 4.2 For 3D Video               | yes  | No    |
| 1.2.840.10008.1.2.4.105.1 | video/mp4  | Fragmentable MPEG-4 AVC/H.264 High Profile / Level 4.2 For 3D Video  | yes  | No    |
| 1.2.840.10008.1.2.4.106   | video/mp4  | MPEG-4 AVC/H.264 Stereo High Profile / Level 4.2                     | yes  | No    |
| 1.2.840.10008.1.2.4.106.1 | video/mp4  | Fragmentable MPEG-4 AVC/H.264 Stereo High Profile / Level 4.2        | yes  | No    |
| 1.2.840.10008.1.2.4.107   | video/H265 | HEVC/H.265 Main Profile / Level 5.1                                  | yes  | No    |
| 1.2.840.10008.1.2.4.108   | video/H265 | HEVC/H.265 Main 10 Profile / Level 5.1                               | yes  | No    |

{{% notice note %}}
For video, **Read** means that Weasis extracts the stream and hands it to the system player; the frames are not rendered in the viewer.
{{% /notice %}}

### Not supported

The following transfer syntaxes are not read: JPIP Referenced (1.2.840.10008.1.2.4.94, .95, .204, .205), Encapsulated Uncompressed Explicit VR Little Endian (1.2.840.10008.1.2.1.98), Deflated Image Frame Compression (1.2.840.10008.1.2.8.1) and the retired RFC 2557 MIME Encapsulation (1.2.840.10008.1.2.6.1).

## Supported "Photometric Interpretation" pixel format

This table lists the [Photometric Interpretation](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.3.html#sect_C.7.6.3.1.2) supported by Weasis.

| Photometric Interpretation | Description                                                        | Supported                       |
|----------------------------|--------------------------------------------------------------------|---------------------------------|
| MONOCHROME1                | grey level image description (high values=dark, low values=bright) | yes                             |
| MONOCHROME2                | grey level image description (high values=bright, low values=dark) | yes                             |
| PALETTE COLOR              | pseudo color image description                                     | yes                             |
| RGB                        | true color image description                                       | yes                             |
| YBR_FULL                   | true color image description                                       | yes                             |
| YBR_FULL_422               | true color image description                                       | yes                             |
| YBR_PARTIAL_422            | true color image description (Retired)                             | yes (uncompressed pixel data)   |
| YBR_PARTIAL_420            | true color image description                                       | yes (uncompressed pixel data)   |
| YBR_ICT                    | true color image description (JPEG-2000)                           | yes                             |
| YBR_RCT                    | true color image description (JPEG-2000)                           | yes                             |
