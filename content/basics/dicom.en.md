---
title: DICOM Conformance
description: "Summary conformance statement for Weasis: the DICOM objects it displays and creates, the network services it uses, the transfer syntaxes it reads and writes, the pixel formats it renders, and the IHE profiles it implements."
keywords: [ "dicom conformance statement", "sop class", "dimse", "dicomweb", "supported transfer syntax", "dicom codec support", "jpeg 2000 dicom", "jpeg-ls", "jpeg-xl dicom", "photometric interpretation", "ihe" ]
weight: 70
---

This page is a summary conformance statement for the Weasis viewer. It follows the order of a DICOM PS3.2 conformance statement but keeps one table per topic; it is not a formal PS3.2 document with association and negotiation tables. It applies to the Weasis releases documented on this site; a feature newer than the oldest documented release carries a version badge.

## DICOM objects

### Objects displayed

Weasis opens any file or network object below. A valid DICOM object that matches none of them is listed in the explorer as unsupported.

| Object                                                                      | Handling                                                                                                                                             | See                                                          |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Images: any Image Storage SOP Class with Pixel Data, including enhanced multi-frame objects and float Parametric Maps | Displayed in the 2D viewer, MPR and 3D views                                                                                                         | [2D viewer](../tutorials/dicom-2d-viewer), [MPR](../tutorials/mpr), [3D](../tutorials/dicom-3d-viewer) |
| Video objects (MPEG-2, H.264, HEVC transfer syntaxes)                       | The stream is extracted and opened with the video player of the operating system                                                                     |                                                              |
| Softcopy Presentation States (modality PR)                                  | Applied to the referenced images: window level, LUT, spatial transformation, shutter, graphic and text annotations                                    | [KO and PR](../tutorials/build-ko-pr)                        |
| Key Object Selection documents (modality KO), including IHE rejection notes | Selection of the referenced images; rejection notes hide the rejected instances                                                                      | [KO and PR](../tutorials/build-ko-pr)                        |
| Structured Reports (modality SR)                                            | Rendered as a document in the SR viewer, with links to the referenced images                                                                         | [SR viewer](../tutorials/dicom-sr)                           |
| Segmentations (modality SEG)                                                | Overlaid on the referenced images                                                                                                                    | [SEG viewer](../tutorials/dicom-segmentation)                |
| RT Structure Set, RT Dose, RT Plan                                          | Structures, isodoses and DVH in the RT viewer                                                                                                        | [RT viewer](../tutorials/dicom-rt)                           |
| Waveforms (modalities ECG and HD)                                           | Displayed in the ECG viewer                                                                                                                          | [ECG viewer](../tutorials/dicom-ecg)                         |
| Audio (modality AU)                                                         | Played in the audio player                                                                                                                           | [Audio player](../tutorials/dicom-audio)                     |
| Encapsulated documents (PDF, CDA and any other MIME type)                   | The document is extracted and opened with the application of the operating system                                                                    |                                                              |
| DICOMDIR                                                                    | Used to load a media file-set (CD, DVD, USB key)                                                                                                     | [Import](../tutorials/dicom-import)                          |
| Color Palette Storage                                                       | Imported as a color map, not displayed as an image                                                                                                   | [Color maps](../tutorials/color-maps)                        |

### Objects created

| Object                                                                                                       | Created by                                     | See                                          |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------|
| Key Object Selection Document                                                                                | The KO toolbar                                 | [KO and PR](../tutorials/build-ko-pr)        |
| Grayscale Softcopy Presentation State                                                                        | The PR toolbar                                 | [KO and PR](../tutorials/build-ko-pr)        |
| Secondary Capture Image, Multi-frame True Color Secondary Capture Image                                      | Export of screenshots and animations           | [Export](../tutorials/dicom-export)          |
| Color Palette Storage                                                                                        | Export of a color map                          | [Color maps](../tutorials/color-maps)        |
| Secondary Capture, VL Photographic, Video Photographic, Encapsulated PDF, CDA, STL, OBJ and MTL              | The Dicomizer                                  | [Dicomizer](../tutorials/dicomizer)          |
| Any loaded object, exported unchanged or transcoded, with a DICOMDIR and an optional viewer on the media      | Export to a folder, a ZIP file or a CD/DVD image | [Export](../tutorials/dicom-export)          |

## Network services

### DIMSE

Weasis acts as a Service Class User. Its only Service Class Provider role is the Storage SCP that receives the objects of a C-MOVE. DIMSE connections are not encrypted.

| Service                | SOP Class or information model                                  | Role | Notes                                                                                                                                          |
|------------------------|-----------------------------------------------------------------|------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Query                  | Study Root Query/Retrieve Information Model - FIND              | SCU  | Study and series levels; instance level when a retrieve needs it. Return keys: patient name, ID, sex, birth date and issuer; study UID, description, date, time, accession number, referring physician and study ID; series UID, modality, number and description |
| Retrieve               | Study Root Query/Retrieve Information Model - MOVE              | SCU  | The objects are received by the built-in Storage SCP, which accepts any SOP Class and any transfer syntax                                      |
| Retrieve               | Study Root Query/Retrieve Information Model - GET               | SCU  | Storage presentation contexts are offered for the common image SOP Classes                                                                     |
| Send                   | Storage Service Class                                           | SCU  | C-STORE of the loaded objects, unchanged or transcoded                                                                                         |
| Print                  | Basic Grayscale Print Management Meta, Basic Color Print Management Meta | SCU  | Basic Film Session, Basic Film Box and Basic Image Box; no Presentation LUT and no annotation box                                       |
| Modality Worklist      | Modality Worklist Information Model - FIND                      | SCU  | Used by the Dicomizer to fill in the patient and study attributes                                                                              |

Configuration: [DICOM explorer](../tutorials/dicom-explorer), [Print](../tutorials/print), [Dicomizer](../tutorials/dicomizer).

### DICOMweb

| Service  | Use                                                                    |
|----------|------------------------------------------------------------------------|
| QIDO-RS  | Search for studies, series and instances                               |
| WADO-RS  | Retrieve the instances of a series                                     |
| STOW-RS  | Send the loaded objects                                                |
| WADO-URI | Retrieve instances, typically from a manifest built by a launcher      |

HTTPS is supported, with OAuth 2.0 (Keycloak and Google templates) or custom HTTP headers for authentication. See [DICOMweb configuration](../tutorials/dicomweb-config) and [DICOMweb archives](customize/dicomweb-archives).

### Launch from an external system

Weasis can be started with a manifest that lists the studies to load and the archive to fetch them from, or with the parameters of the IHE Invoke Image Display profile. See [Integration](customize/integration) and the [ViewerHub launch APIs](../viewer-hub/api).

## Transfer syntaxes

- **Read**: the pixel data is decoded and displayed by Weasis.
- **Write**: the syntax is offered when exporting or sending (see [Export](../tutorials/dicom-export)). Images in a syntax that is not offered are exported unchanged.

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

## Pixel data

### Photometric interpretation

This table lists the [Photometric Interpretation](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.3.html#sect_C.7.6.3.1.2) values supported by Weasis.

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

### Pixel data characteristics

- Bits Allocated 8, 16 and 32, signed and unsigned; 32-bit float pixel data (Parametric Maps).
- Both planar configurations (interleaved and separate planes).
- Single-frame and multi-frame objects; encapsulated multi-frame data with one or several fragments per frame.
- Modality LUT and rescale, VOI LUT and windows, presentation LUT shape, palette color lookup tables, and overlay planes.

## Character sets

The Specific Character Set of each object is honored when decoding text attributes, including the ISO 2022 multi-byte sets and UTF-8. Text is displayed with the fonts of the operating system.

## IHE profiles

| Profile                           | Actor                    | Where it applies                                                                                                   |
|-----------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------|
| Basic Image Review (BIR)          | Image Display            | Image annotations, lossy compression and presentation state indications, the required viewing tools                |
| Portable Data for Imaging (PDI)   | Portable Media Importer, Portable Media Creator | Reading a media file-set through its DICOMDIR; writing a file-set with a DICOMDIR and a viewer on a CD/DVD image ([Import](../tutorials/dicom-import), [Export](../tutorials/dicom-export)) |
| Invoke Image Display (IID)        | Image Display            | Launching the viewer from a patient or study context ([Launch APIs](../viewer-hub/api))                            |
