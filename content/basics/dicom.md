---
title: Dicom Conformance
weight: 70
---

### Compatibility of DICOM Transfer Syntax

| Transfer Syntax UID | Description | Supported |
| ------ | ------ | --- |
| 1.2.840.10008.1.2 | Implicit VR - Little Endian | yes |
| 1.2.840.10008.1.2.1 | Explicit VR - Little Endian | yes |
| 1.2.840.10008.1.2.2 | Explicit VR - Big Endian | yes |
| 1.2.840.10008.1.2.5 | RLE (Run Length Encoding) Lossless | yes |
| 1.2.840.10008.1.2.4.50 | JPEG Baseline (Process 1): Default Transfer Syntax for Lossy JPEG 8 Bit Image Compression | yes |
| 1.2.840.10008.1.2.4.51 | JPEG Extended (Process 2 &amp; 4): Default Transfer Syntax for Lossy JPEG 12 Bit Image Compression (Process 4 only) | yes |
| 1.2.840.10008.1.2.4.57 | JPEG Lossless, Non-Hierarchical (Process 14) | yes |
| 1.2.840.10008.1.2.4.70 | JPEG Lossless, Non-Hierarchical, First-Order Prediction (Process 14 [Selection Value 1]): Default Transfer Syntax for Lossless JPEG Image Compression | yes |
| 1.2.840.10008.1.2.4.80 | JPEG-LS Lossless Image Compression | yes |
| 1.2.840.10008.1.2.4.81 | JPEG-LS Lossy (Near-Lossless) Image Compression | yes |
| 1.2.840.10008.1.2.4.90 | JPEG 2000 Image Compression (Lossless Only) | yes |
| 1.2.840.10008.1.2.4.91 | JPEG 2000 Image Compression | yes |

{{% notice note %}}
These TSUIDs are available with Weasis 2.5 and later for Windows, Mac OS X and Linux.
{{% /notice %}}

| Transfer Syntax UID | Description | Supported |
| ------ | ------ | ------ |
| 1.2.840.10008.1.2.6.1 | RFC 2557 MIME Encapsulation | yes |
| 1.2.840.10008.1.2.4.100 | MPEG-2 Main Profile Main Level | yes |
| 1.2.840.10008.1.2.4.101 | MPEG-2 Main Profile High Level | yes |
| 1.2.840.10008.1.2.4.102 | MPEG-4 AVC/H.264 High Profile / Level 4.1 | yes |
| 1.2.840.10008.1.2.4.103 | MPEG-4 AVC/H.264 BD-compatible High Profile / Level 4.1 | yes |

{{% notice note %}}
These TSUIDs are open by the default system application associated to the MIME type.
{{% /notice %}}

### Supported "Photometric Interpretation" pixel format


| Photometric Interpretation | Description | Supported |
| ------ | ------ | --- |
| MONOCHROME1 | grey level image description (high values=dark, low values=bright) | yes |
| MONOCHROME2 | grey level image description (high values=bright, low values=dark) | yes |
| PALETTE COLOR | pseudo color image description | yes |
| RGB | true color image description | yes |
| YBR_FULL | true color image description | yes |
| YBR_FULL_422 | true color image description | yes |
