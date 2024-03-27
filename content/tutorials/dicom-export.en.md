---
title: DICOM Export
weight: 20
description: How to export DICOM files
keywords: [ "dicom export", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>How to export DICOM files</center>

### Exporting the selected view {{< svg "static/tuto/icon/exportImage.svg" >}} {#export-view}
From the toolbar icon {{< svg "static/tuto/icon/exportImage.svg" >}} or from the main menu _File > Export > Exporting view_ export the selected view either to the clipboard or to image file (PNG, TIF, JPG, JPEG2000).

#### Current view
Export the view as it is (size and overlay).

Anonymize: It allows you to remove identifying information in overlay.

#### Original Image

Export the view according to the original image with some options.

![Export view](/tuto/dicom-export-view.png?classes=shadow&width=350)
<br>
* Size: Change the image size in percent
* Preserve 16-bit per channel: Option to preserve the pixel depth (e.g. 16-bit in PNG/JPEG 2000/TIFF, double values in TIFF). When this option is applied, the pixel values will match with the Modality LUT values (e.g. Hounsfield values). Exporting in JPEG Lossy is only possible when unchecked for 8-bit image.
* DICOM Pixel Padding: Apply the [DICOM pixel padding](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.5.html#sect_C.7.5.1.1.2) when checked
* DICOM Shutter: Apply the [DICOM shutters](https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.7.6.11.html) when checked
* DICOM Overlay: Apply the [DICOM overlays](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.9.2.html) when checked

### DICOM Export {{< svg "static/tuto/icon/exportDicom.svg" >}} {#dicom-exporting}

In order to open the DICOM export window click on toolbar icon {{< svg "static/tuto/icon/exportDicom.svg" >}} or from the main menu _File > Export > DICOM_

#### Local Device
![Export DICOM](/tuto/export-ko-pr.png?classes=shadow&width=500)
<br>
1. Select *Local Device* item
2. Choose the exporting options
   ![Export options](/tuto/dicom-export-options.png?classes=shadow&width=350)
   * Transcoding: It allows you to change the DICOM transfer syntax. Use this option only if you understand well what you are doing.
   * Generate new unique identifiers: Create new UIDs for some attributes. Within an export, the consistency between all the UIDs and their references is preserved.
   * Include DICOMDIR: Create DICOMDIR file
   * DICOM CD folders: Add a directory to be compliant with DICOM CD
   * Keep directory names: Preserve the name in the directory hierarchy (not compliant with DICOMDIR)
3. Select the patient/study/series/instance to export. Note: [series created by Weasis](../build-ko-pr/) have a flag "NEW"
4. Export the selection and close the Window

{{% notice tip %}}
When opening the Export DICOM window, the checkbox of the study selected in the viewer (surrounded by an orange line) is automatically checked and open series have a full-line selection.

In order to help with series selection, place the cursor on a series line, and you'll see a tooltip displaying its thumbnail.
{{% /notice %}}

{{% notice note %}}
When DICOM data is exported in a native image format (JPG, PNG, JPEG 2000 or TIFF), only the images are transformed (see [original image options](#original-image)) and the encapsulated files (video, audio and PDF) are extracted.

Multiframe images are exported by adding a number to the end of the file name.
{{% /notice %}}

#### DICOM Send
1. Select *DICOM Send* item
2. Select the destination node (either a DICOM node or a DICOMWeb node)
3. Select the patient/study/series/instance to export. Note: [series created by Weasis](../build-ko-pr/) have a flag "NEW"
4. Send the selection to the destination and close the Window

#### CD/DVD Image
![Export DICOM](/tuto/dicom-export-cd.png?classes=shadow&width=750)
<br>
1. Select the *CD/DVD Image* item
2. Choose the exporting options
   * Transcoding: It allows you to change the DICOM transfer syntax. Use this option only if you understand well what you are doing.
   * Generate new unique identifiers: Create new UIDs for some attributes. For an export, the consistency between UIDs and their references is preserved.
3. *Add JPEG images* allows extracting the images and the encapsulated files (video, audio and PDF) into a JPEG folder
4. *Add Weasis* allows embedding the viewer into the iso image. This option is only possible on Windows x86-64 (for exporting and running). Running the viewer directly on a CD/DVD ca be quite slow. To avoid that you can install the ISO on a USB stick or read the CD with a locally installed viewer as described in README.html.
5. Select the patient/study/series/instance to export
6. Export the selection and close the Window