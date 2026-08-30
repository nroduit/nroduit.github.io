---
title: DICOM Export
weight: 20
description: How to export DICOM files
keywords: [ "dicom export", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>How to export DICOM files</center>

Weasis offers two complementary export workflows:

- **Export the selected view** — produces a **raster image** (PNG, TIFF, JPG, JPEG 2000) or a clipboard copy of what is currently shown on screen. Useful for slides, reports, e-mails, screenshots of measurements, and other non-DICOM consumers.
- **DICOM Export** — produces **DICOM-format output** (a directory tree, an ISO image, or a network transfer to a remote node). Use this to share studies with another DICOM-capable system without losing pixel fidelity or metadata.

---

### Exporting the selected view {{< svg-inline "static/tuto/icon/exportImage.svg" >}} {#export-view}

Open the export-view dialog from the toolbar icon {{< svg-inline "static/tuto/icon/exportImage.svg" >}} or from the main menu **_File > Export > Exporting view_**. The output can be sent to the clipboard or saved to an image file in PNG, TIFF, JPG, or JPEG 2000 format.

#### Current view
Exports the view exactly as it appears on screen, at its current size and with every overlay (annotations, measurements, DICOM annotations, rulers…) visible.

**Anonymize** — removes identifying information from the overlay, in line with the [Anonymize option](dicom-2d-viewer/#dicom-annotations) of the 2D viewer.

#### Original Image
Exports the underlying image — without on-screen overlays — with a few rendering options.

![Export view](/tuto/dicom-export-view.png?classes=shadow&width=350px)
<br>

* **Size** — scale the exported image (percentage of the original dimensions).
* **Preserve 16-bit per channel** — keep the original pixel depth (16-bit in PNG / JPEG 2000 / JPEG-XL / TIFF, double values in TIFF). When checked, the exported pixel values match the Modality LUT values (e.g. Hounsfield units for CT). JPEG Lossy is only available with this option **unchecked**, since the format requires an 8-bit image.
  When unchecked, the image is reduced to 8 bits per channel by applying the **default window/level** of the image — the first window center/width (or VOI LUT) stored in the DICOM header, or the full pixel range when the header defines none. This is *not* the rendering currently displayed in the view: the window/level you adjusted manually, the preset you picked, an applied [Presentation State](build-ko-pr/), an inverted LUT, and any pseudo-color LUT are all ignored. To export exactly what is on screen, use **Current view** instead.
* **DICOM Pixel Padding** — apply the [DICOM pixel padding](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.5.html#sect_C.7.5.1.1.2) when checked.
* **DICOM Shutter** — apply the [DICOM shutters](https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.7.6.11.html) when checked.
* **DICOM Overlay** — apply the [DICOM overlays](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.9.2.html) when checked.

---

### DICOM Export {{< svg-inline "static/tuto/icon/exportDicom.svg" >}} {#exporting}

Open the DICOM Export window from the toolbar icon {{< svg-inline "static/tuto/icon/exportDicom.svg" >}} or from the main menu **_File > Export > DICOM_**. Three destinations are available in the left panel — **Local Device**, **DICOM Send**, and **CD/DVD Image** — each with its own set of options.

{{% notice tip %}}
When the export window opens, the study selected in the viewer (orange focus border) is pre-checked, and the series that are currently open are highlighted with a full-line selection.

Hover any series row to see its thumbnail in a tooltip — useful when picking among several similar series.
{{% /notice %}}

#### Local Device
![Export DICOM](/tuto/export-ko-pr.png?classes=shadow&width=500px)
<br>

1. Select **Local Device**.
2. Choose the export options:
   ![Export options](/tuto/dicom-export-options.png?classes=shadow&width=350px)
 <br>
   * **Transcoding** — change the DICOM transfer syntax (compression / encoding) of the exported files. Leave the default unless you specifically need a different syntax.
   * **Generate new unique identifiers** — replace the Study / Series / SOP Instance UIDs with newly generated ones. Cross-references between UIDs are kept consistent **within this export session only** — running the export a second time produces a different set of UIDs that no longer matches the first.
   * **Include DICOMDIR** — write a DICOMDIR index file alongside the exported objects.
   * **DICOM CD folders** — wrap the exported tree in the standard DICOMDIR-compliant folder layout used on DICOM CDs.
   * **Keep directory names** — preserve human-readable folder names in the exported hierarchy (incompatible with the strict DICOMDIR layout).
3. Pick the patient(s), study (or studies), series, or individual instances to export. Series created inside Weasis (such as [Key Object / Presentation State](build-ko-pr/) objects) are marked with a **NEW** flag.
4. Click **Export** to write the files, then close the window.

{{% notice note %}}
When the export uses a native image format (JPG, PNG, JPEG 2000, JPEG-XL, or TIFF) instead of DICOM, only the image frames are converted (see the [Original Image options](#original-image)). Encapsulated DICOM payloads — video, audio, and PDF — are extracted as standalone files in their native format.

Multi-frame images are exported as numbered files (one frame per file).
{{% /notice %}}

#### DICOM Send
Sends the selected objects directly to a remote DICOM or DICOMweb node over the network — the same protocols used by PACS systems for inter-institutional transfer.

1. Select **DICOM Send**.
2. Choose the destination node — a classic DICOM node (C-STORE) or a DICOMweb node (STOW-RS).
3. Pick the patient(s) / study / series / instances to send. Series created inside Weasis are marked with a **NEW** flag.
4. Click **Send** to transfer, then close the window.

{{% notice tip %}}
Destination nodes are configured under **_File > Preferences > DICOM_** (see the **DICOM Node List** and **DICOMweb Node List** entries) and can be reused across export sessions.
{{% /notice %}}

#### CD/DVD Image
Produces a burnable ISO image that follows the DICOMDIR layout expected by most CD/DVD-based DICOM media.

![Export DICOM](/tuto/dicom-export-cd.png?classes=shadow&width=750px)
<br>

1. Select **CD/DVD Image**.
2. Choose the export options:
   * **Transcoding** — change the DICOM transfer syntax of the exported files. Leave the default unless you specifically need a different syntax.
   * **Generate new unique identifiers** — replace the Study / Series / SOP Instance UIDs with newly generated ones. Cross-references between UIDs are kept consistent **within this export session only** — running the export a second time produces a different set of UIDs that no longer matches the first.
3. **Add JPEG images** — also extract every image and every encapsulated payload (video, audio, PDF) into a separate JPEG folder for easy preview on systems without a DICOM viewer.
4. **Add Weasis** — embed the Weasis viewer directly into the ISO so the recipient can launch it from the media. Currently supported only on Windows x86-64 (both for producing and for running the embedded copy). Running Weasis straight off a CD/DVD is slow; for a better experience, write the ISO to a USB stick or open the disc with a locally installed copy of Weasis as described in the `README.html` on the disc.
5. Pick the patient(s) / study / series / instances to export.
6. Click **Export** to write the ISO, then close the window.