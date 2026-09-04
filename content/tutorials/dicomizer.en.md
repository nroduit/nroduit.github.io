---
title: Dicomizer
weight: 1000
description: How to convert standard images into DICOM files
keywords: [ "convert to dicom", "dicomizer", "dicom worklist", "jpg to dicom" ]
---

## <center>How to convert images into DICOM files {{< svg-inline "static/tuto/icon/Dicomizer.svg" >}}</center>

The **Dicomizer** converts standard files — photos, scanned reports, videos, 3D models — into DICOM objects so they can be archived in a PACS alongside acquisitions from imaging modalities. Typical use cases include adding dermatology or wound-care photos to a study, attaching a PDF report or consent form, archiving endoscopic or surgical videos, and packaging STL files used for 3D printing.

Beyond the file conversion itself, the Dicomizer also helps you set the DICOM tags at the patient, study, and image levels so the resulting objects are consistent, searchable in the archive, and recognized by every DICOM viewer.

![Dicomizer](/gallery2/Dicomizer.jpg?classes=shadow)
<br>

The sections below describe the day-to-day use of the Dicomizer. Administrators deploying the tool in a clinical workflow should also read [Integrating the Dicomizer](#integrating-the-dicomizer) at the end of this page.

### How to Launch Dicomizer

When Weasis is installed, the **Dicomizer** is also available as a standalone application with this shortcut {{< svg-inline "static/tuto/icon/Dicomizer.svg" >}} (Windows and Linux only).

On macOS, run the `Dicomizer` command from the terminal:
{{< highlight shell >}}
/Applications/Weasis.app/Contents/MacOS/Dicomizer
{{< /highlight >}}

If you use the Dicomizer frequently on macOS, use **Automator** to create a `Dicomizer.app` with a **Run Shell Script** action containing the command above.

### Import Media Files

The Dicomizer can encapsulate the following file types into DICOM objects:

- **Standard images** — TIFF, BMP, GIF, JPEG, PNG, RAS, HDR, PNM. Converted to **JPEG lossy** to comply with the DICOM standard.
- **PDF documents** (`application/pdf`) {{< since "4.6.2" >}} — convenient for archiving reports, forms, or scanned documents.
- **STL files** (`model/stl`) {{< since "4.6.2" >}} — for 3D printing and surgical planning.
- **MPEG-2 video** (`video/mpeg`) {{< since "4.6.2" >}} — for compatibility with legacy medical imaging systems.
- **MPEG-4 video** (`video/mp4`) {{< since "4.6.2" >}} — modern format for endoscopy, ultrasound, surgical recordings, and other high-quality medical videos.

{{% notice warning %}}
Only MPEG-4 videos that are [compatible with the DICOM standard](https://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_8.7.3.html) are accepted — namely **MPEG-4 AVC/H.264 High Profile (up to Level 4.2)** or **HEVC/H.265 Main and Main 10 Profile**. Videos using a different profile are rejected with a message asking you to convert them to a compatible format first.

Video files are also size-limited {{< since "4.7.0" >}}: a file larger than `weasis.acquire.video.max.size` (1024 MB by default — see the [preferences](../basics/customize/preferences)) is rejected. Set the preference to `0` to remove the limit.
{{% /notice %}}

#### Importing files

1. In the **left panel**, navigate through the file system to locate the files to convert. The button next to the combo box on the right opens a folder chooser to pick the directory containing the eligible media.
2. To organize files into separate series, select the thumbnails in the left panel and click **Import**. The dialog offers three grouping options:
   - **Do not group** — all images are imported into a single series (same as drag-and-drop).
   - **Group by date** — images are split into series based on their acquisition date. A second field controls the maximum time gap that still keeps two images in the same series.
   - **Group by name** — all images are imported into a single series with a custom name.
3. Alternatively, **drag and drop** files from the system file explorer into the central panel. The files are either added to the current series, or assigned to a default series based on their media type.

{{% notice note %}}
For image formats that carry **EXIF tags**, the following values are mapped to DICOM tags automatically:

- **Image Orientation** → adjusts the image orientation.
- **Image Description** → mapped to _Image Comments_.
- **Manufacturer Description** → mapped to _Manufacturer_.
- **Camera Model Description** → mapped to _Manufacturer Model Name_.
- **Date/Time (Original)** or, if absent, **Date/Time** → mapped to _ContentDate_ and _ContentTime_. If both are absent or invalid (date > now + 1 day, or date < now − 30 years), the file's last-modified date is used.
{{% /notice %}}

{{% notice note %}}
Series-grouping buttons cannot be deleted directly. Remove every thumbnail associated with the button first, and the button disappears.
{{% /notice %}}

{{% notice tip %}}
The combo box keeps the list of recently used folders. Connecting a USB device automatically adds the device path to the list.
{{% /notice %}}

#### Edit DICOM Tags

The **Album** panel manages DICOM tags at the patient, study, series, and image levels:

- The **left panel** lists the groups, each representing a DICOM series.
- The **central panel** shows the thumbnails of the imported media. Select one or more thumbnails to edit their DICOM tags; double-click a thumbnail to open the image in the [Photo Editor](#edit-the-images).
- The **bottom panel** displays the DICOM tags of the selected images. Image-level tags are only visible when a single image is selected.

Tags in the bottom panel are organized into a categorized tree:

- **Global tags** — applied to the patient and study levels.
- **Series level** — applied to the series level.
- **Image level** — applied to the individual image level.

{{% notice note %}}
A red dashed outline around an item means the value is **mandatory** and must be filled in before publication.
{{% /notice %}}

Person-name fields (_PatientName_, _ReferringPhysicianName_, _OperatorsName_, …) must follow the `Last^First^Middle^Prefix^Suffix` format defined by the [DICOM standard](https://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html#sect_6.2.1).

These fields are no longer edited as raw text {{< since "4.7.3" >}}: clicking the cell opens a dialog with one input per component — **Last name**, **First name**, **Middle name**, **Prefix**, and **Suffix**. The separators are inserted for you, a **DICOM value** line previews the encoded result while you type, and empty components are dropped. In the table, the value is displayed in the usual lexical order (_Smith, John_).

{{% notice note %}}
The dialog rejects the DICOM delimiter characters `^`, `=` and `\`, and the preview turns red if a name exceeds the 64-character limit of the standard.

Ideographic and phonetic component groups (the parts after `=`, used for Japanese or Korean names) are preserved unchanged; the dialog edits the alphabetic group only.
{{% /notice %}}

{{% notice warning %}}
The `Last^First^Middle^Prefix^Suffix` rule also applies to values populated automatically — from a DICOM Worklist or through the `acquire:patient` command (see [Integrating the Dicomizer](#integrating-the-dicomizer)). Those values are not reformatted by the Dicomizer.
{{% /notice %}}

{{% notice tip %}}
The thumbnail right-click menu offers:

- **Edit** (images only) — opens the Photo Editor to crop, rotate, or adjust the image. Double-clicking the thumbnail has the same effect.
- **Remove** — deletes the image from the series without touching the original file.
- **Move to…** — moves the image to a different series.
{{% /notice %}}

#### Edit the Images

The **Photo Editor** offers basic tools to crop, rotate, and adjust contrast on an imported image. You can also add annotations to highlight specific areas, and use measurement tools to indicate distances, angles, or areas. The image can be calibrated against a known distance so that the measurements reflect real-world dimensions.

### Publish DICOM Files

Click **Publish** to send the DICOM files to a remote DICOM archive, or **Export locally** {{< since "4.6.2" >}} to save them on the local file system. The **Publication** panel offers:

- **Selection** — choose which DICOM items to publish (everything selected by default).
- **Resolution** — downscale high-resolution images before sending.
- **Destination** — pick the target node from the list of configured remote DICOM nodes.
- **Calling AE Title** — pick the calling node, if your archive enforces specific sender AE titles.

{{% notice note %}}
The destination can be a specific remote node or the list of remote nodes configured under **_File > Preferences (Alt + P) > DICOM node list_** — add or edit DICOM nodes there.
{{% /notice %}}

{{% notice info %}}
A green check-mark icon on a thumbnail confirms that the image was successfully published.
{{% /notice %}}

-----

## <center>Integrating the Dicomizer</center>

This section is intended for administrators integrating the Dicomizer into a clinical workflow. It covers launching the Dicomizer from a web context and — most importantly — populating the DICOM metadata automatically so that operators do not have to enter it manually.

### Launch from a Web Context

The Dicomizer can be launched from a web context using the `weasis://` [protocol](../getting-started/weasis-protocol).

Try launching the Weasis Dicomizer {{< launch >}}$weasis:config pro="felix.extended.config.properties file:conf/dicomizer.json" pro="gosh.port 17181"{{< /launch >}} with the following parameters:
{{< highlight shell >}}
$weasis:config pro="felix.extended.config.properties file:conf/dicomizer.json" pro="gosh.port 17181"
{{< /highlight >}}

### Automatically Fill in the Metadata

Instead of being entered by hand in the **Album** panel, the Global tags (patient and study levels) can be populated automatically:

- **From a DICOM Worklist** — configured with the [preference items](../basics/customize/preferences) starting with `weasis.acquire.wkl`. Example of [configuration at launch](../getting-started/weasis-protocol/#modify-the-launch-parameters):
  {{< highlight shell >}}
  $weasis:config pro="felix.extended.config.properties file:conf/ext-dicomizer.properties" pro="gosh.port 17181" pro="weasis.acquire.wkl.host localhost" pro="weasis.acquire.wkl.aet DCM4CHEE" pro="weasis.acquire.wkl.port 11112" pro="weasis.acquire.wkl.station.aet WEASIS-MWL"
  {{< /highlight >}}

- **Via the [acquire:patient](../basics/commands/#acquirepatient) command** — pass a DICOM-style XML payload, for example:
{{< highlight xml >}}
<?xml version="1.0" encoding="UTF-8"?>
<tags>
	<PatientID>97032168</PatientID>
	<PatientName>TEST^TEST</PatientName>
	<PatientBirthDate>19580703</PatientBirthDate>
	<PatientSex>M</PatientSex>
	<OperatorsName>RODUIT^NICOLAS</OperatorsName>
	<AccessionNumber>000000003712</AccessionNumber>
	<IssuerOfAccessionNumberSequence>
		<LocalNamespaceEntityID>411713364</LocalNamespaceEntityID>
	</IssuerOfAccessionNumberSequence>
	<StudyID>411713364</StudyID>
</tags>
{{< /highlight >}}

{{% notice note %}}
Which DICOM tags appear, are editable, and are required in the **Album** panel is configured via the [preferences](../basics/customize/preferences) (items starting with `weasis.acquire.meta`).
{{% /notice %}}

### Publication Destination

When the Dicomizer destination is fixed in the [preferences](../basics/customize/preferences) (items starting with `weasis.acquire.dest`), the destination is no longer selectable in the **Publication** panel — DICOM files are sent directly to the configured node.