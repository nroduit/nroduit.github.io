---
title: Dicom Conformance
description: DICOM Conformance Statements of Weasis
keywords: [ "DICOM Conformance Statements", "IHE", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 70
---

### Compatibility of [DICOM Transfer Syntax](https://dicom.nema.org/medical/dicom/current/output/chtml/part06/chapter_A.html)

| Transfer Syntax UID     | Media Type | Description                                                                                                         | Reading | Writing |
|-------------------------|------------|---------------------------------------------------------------------------------------------------------------------|---------|---------|
| 1.2.840.10008.1.2       |            | Implicit VR - Little Endian                                                                                         | yes     | No      |
| 1.2.840.10008.1.2.1     |            | Explicit VR - Little Endian                                                                                         | yes     | Yes     |
| 1.2.840.10008.1.2.1.99  |            | Deflated Explicit VR Little Endian                                                                                  | yes     | No      |
| 1.2.840.10008.1.2.2     |            | Explicit VR Big Endian (Retired)                                                                                    | yes     | No      |
| 1.2.840.10008.1.2.5     |            | RLE (Run Length Encoding) Lossless                                                                                  | yes     | No      |
| 1.2.840.10008.1.2.4.50  | image/jpeg | JPEG Baseline (Process 1): Default Transfer Syntax for Lossy JPEG 8 Bit Image Compression                           | yes     | Yes     |
| 1.2.840.10008.1.2.4.51  | image/jpeg | JPEG Extended (Process 2 &amp; 4): Default Transfer Syntax for Lossy JPEG 12 Bit Image Compression (Process 4 only) | yes     | Yes     |
| 1.2.840.10008.1.2.4.53  | image/jpeg | JPEG Spectral Selection, Non-Hierarchical (Process 6 & 8) (Retired)                                                 | yes     | No      |
| 1.2.840.10008.1.2.4.55  | image/jpeg | JPEG Full Progression, Non-Hierarchical (Process 10 & 12) (Retired)                                                 | yes     | No      |
| 1.2.840.10008.1.2.4.57  | image/jpeg | JPEG Lossless, Non-Hierarchical (Process 14)                                                                        | yes     | Yes     |
| 1.2.840.10008.1.2.4.70  | image/jpeg | JPEG Lossless, Non-Hierarchical, First-Order Prediction (Process 14 [Selection Value 1])                            | yes     | Yes     |
| 1.2.840.10008.1.2.4.80  | image/jls  | JPEG-LS Lossless Image Compression                                                                                  | yes     | Yes     |
| 1.2.840.10008.1.2.4.81  | image/jls  | JPEG-LS Lossy (Near-Lossless) Image Compression                                                                     | yes     | Yes     |
| 1.2.840.10008.1.2.4.90  | image/jp2  | JPEG 2000 Image Compression (Lossless Only)                                                                         | yes     | Yes     |
| 1.2.840.10008.1.2.4.91  | image/jp2  | JPEG 2000 Image Compression                                                                                         | yes     | Yes     |
| 1.2.840.10008.1.2.4.92  | image/jpx  | JPEG 2000 Part 2 Multi-component Image Compression (Lossless Only)                                                  | yes     | No      |
| 1.2.840.10008.1.2.4.93  | image/jpx  | JPEG 2000 Part 2 Multi-component Image Compression                                                                  | yes     | No      |
| 1.2.840.10008.1.2.4.201 | image/jphc | High-Throughput JPEG 2000 Image Compression (Lossless Only)                                                         | yes     | No      |
| 1.2.840.10008.1.2.4.202 | image/jphc | High-Throughput JPEG 2000 with RPCL Options Image Compression (Lossless Only)                                       | yes     | No      |
| 1.2.840.10008.1.2.4.203 | image/jphc | High-Throughput JPEG 2000 Image Compression                                                                         | yes     | No      |

<br>

| Transfer Syntax UID     | Media Type | Description                                             | Reading | Writing |
|-------------------------|------------|---------------------------------------------------------|---------|---------|
| 1.2.840.10008.1.2.6.1   | mime type  | RFC 2557 MIME Encapsulation                             | yes     | No      |
| 1.2.840.10008.1.2.4.100 | video/mpeg | MPEG-2 Main Profile Main Level                          | yes     | No      |
| 1.2.840.10008.1.2.4.101 | video/mpeg | MPEG-2 Main Profile High Level                          | yes     | No      |
| 1.2.840.10008.1.2.4.102 | video/mp4  | MPEG-4 AVC/H.264 High Profile / Level 4.1               | yes     | No      |
| 1.2.840.10008.1.2.4.103 | video/mp4  | MPEG-4 AVC/H.264 BD-compatible High Profile / Level 4.1 | yes     | No      |
| 1.2.840.10008.1.2.4.104 | video/mp4  | MPEG-4 AVC/H.264 High Profile / Level 4.2 For 2D Video  | yes     | No      |
| 1.2.840.10008.1.2.4.105 | video/mp4  | MPEG-4 AVC/H.264 High Profile / Level 4.2 For 3D Video  | yes     | No      |
| 1.2.840.10008.1.2.4.106 | video/mp4  | MPEG-4 AVC/H.264 Stereo High Profile / Level 4.2        | yes     | No      |
| 1.2.840.10008.1.2.4.107 | video/H265 | HEVC/H.265 Main Profile / Level 5.1                     | yes     | No      |
| 1.2.840.10008.1.2.4.108 | video/H265 | HEVC/H.265 Main 10 Profile / Level 5.1                  | yes     | No      |

{{% notice note %}}
The latter groups of TSUIDs are opened by the default system application associated with the MIME type.
{{% /notice %}}

### Supported "Photometric Interpretation" pixel format

| Photometric Interpretation | Description                                                        | Supported |
|----------------------------|--------------------------------------------------------------------|-----------|
| MONOCHROME1                | grey level image description (high values=dark, low values=bright) | yes       |
| MONOCHROME2                | grey level image description (high values=bright, low values=dark) | yes       |
| PALETTE COLOR              | pseudo color image description                                     | yes       |
| RGB                        | true color image description                                       | yes       |
| YBR_FULL                   | true color image description                                       | yes       |
| YBR_FULL_422               | true color image description                                       | yes       |
| YBR_PARTIAL_422            | true color image description (Retired)                             | yes       |
| YBR_PARTIAL_420            | true color image description                                       | yes       |
| YBR_ICT                    | true color image description (JPEG-2000)                           | yes       |
| YBR_RCT                    | true color image description (JPEG-2000)                           | yes       |
