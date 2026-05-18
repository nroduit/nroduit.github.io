---
title: Dicomizer
weight: 1000
description: How to convert standard images into DICOM files
keywords: [ "convert to dicom", "dicomizer", "dicom worklist", "jpg to dicom" ]
---

## <center>How to convert images into DICOM files {{< svg-inline "static/tuto/icon/Dicomizer.svg" >}}</center>

The Dicomizer tool allows you to convert standard images into DICOM files. This will facilitate the integration of these images into a DICOM archive. 

Dicomizer will help you to manage the DICOM tags at the patient, study, and image levels in order to have more consistent data, easily searchable in the archive system, and compliant with DICOM viewers.

![Dicomizer](/gallery2/Dicomizer.jpg?classes=shadow)
<br>

The sections below describe the day-to-day use of the Dicomizer. Administrators deploying the tool in a clinical workflow should also read [Integrating the Dicomizer](#integrating-the-dicomizer) at the end of this page.

### How to Launch Dicomizer

When installing Weasis, `Dicomizer` is available as a standalone application with this shortcut {{< svg-inline "static/tuto/icon/Dicomizer.svg" >}} (only on Windows and Linux). 

On macOS, you need to run the `Dicomizer` command from the terminal:
{{< highlight shell >}}
/Applications/Weasis.app/Contents/MacOS/Dicomizer
{{< /highlight >}}

If you plan to use it frequently, with the Automator application you can create a new application `Dicomizer.app` with the `Run Shell Script` action containing the command.

### Import Media Files

The Dicomizer tool supports encapsulating the following file types into DICOM objects:

- **Standard images**: Includes formats such as TIFF, BMP, GIF, JPEG, PNG, RAS, HDR, and PNM. These are converted to JPEG lossy to ensure compatibility with the DICOM standard.
- **PDF documents (application/pdf)** {{% badge title="Version" %}}4.6.2{{% /badge %}}: Ideal for integrating reports, forms, or scanned documents into DICOM archives.
- **STL files (model/stl)** {{% badge title="Version" %}}4.6.2{{% /badge %}}: Used for 3D printing and surgical planning.
- **MPEG-2 video files (video/mpeg)** {{% badge title="Version" %}}4.6.2{{% /badge %}}: Maintains compatibility with legacy medical imaging systems.
- **MPEG-4 video files (video/mp4)** {{% badge title="Version" %}}4.6.2{{% /badge %}}: A modern format for high-quality medical videos, such as endoscopy, ultrasound, or surgical recordings.

{{% notice warning %}}
Only MPEG-4 video files that are [compatible with the DICOM standard](https://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_8.7.3.html) are supported, namely MPEG-4 AVC/H.264 High Profile (up to Level 4.2) or HEVC/H.265 Main and Main 10 Profile. When a video uses another profile, it is not imported and a message invites you to convert it to a compatible format before using Dicomizer.

Video files are also limited in size {{% badge title="Version" %}}4.7.0{{% /badge %}}: a file larger than the maximum defined by the `weasis.acquire.video.max.size` [preference](../basics/customize/preferences) (1024 MB by default) is rejected with a message. Set this preference to `0` to disable the limit.
{{% /notice %}}


1. Using the left panel, navigate through the file system to locate the images you want to convert. Click the button next to the combo box on the right to choose the folder containing the media files eligible for DICOM conversion.

2. you can organize images into separate series by selecting thumbnails from the left panel and clicking the **Import** button. The resulting dialog offers three grouping options:
   - **Do not group**: All images are imported into a single series (same behavior as drag-and-drop).
   - **Group by date**: Images are divided into separate series based on their acquisition date, with an option to set the maximum time difference between images to group them together.
   - **Group by name**: All images are imported into a single series and assigned a custom name.

3. Alternatively, you can drag and drop files from the system file explorer into the central panel. Images will either be grouped into the current series if applicable, or assigned to a default series based on their media type.

{{% notice note %}}
For image types containing EXIF tags, the following values are automatically mapped to DICOM tags:
- **Image Orientation** → Adjust image orientation based on this value
- **Image Description** → Maps to "Image Comments"
- **Manufacturer Description** → Maps to "Manufacturer"
- **Camera Model Description** → Maps to "Manufacturer Model Name"
- **Date/Time (Original)** or, if absent, **Date/Time** → Maps to "ContentDate" and "ContentTime". Note if both are absent or invalid (date > now + 1 day or date < now - 30 years), the file's last modified date is used.
{{% /notice %}}

{{% notice note %}}
Buttons that group series cannot be deleted directly. To remove a button, you must first remove all associated elements (thumbnails in the central panel).
{{% /notice %}}

{{% notice tip %}}
The combo box contains the list of the last folders used. Connecting a USB device will automatically add the device path to the list.
{{% /notice %}}

### Edit DICOM Tags

The **Album** panel allows you to manage the DICOM tags at the patient, study, and instance levels.

- The left panel shows the group list representing DICOM series.
- The main panel displays the thumbnails of the imported media files and allows you to select the images to edit the DICOM tags or by double-click to open the image in the Photo Editor.
- The bottom panel shows the DICOM tags of the selected images. Note that the image level tags are displayed only when a single image is selected.

The bottom panel organizes DICOM tags into categorized tree structures:
- **Global tags**: Applicable to the patient and study levels.
- **Series level**: Applicable to the series level.
- **Image level**: Applicable to the image level.

{{% notice warning %}}
If an item's dashed outline in the table is red, it indicates that the value is mandatory and must be filled in.  
{{% /notice %}}

{{% notice warning %}}
Person name fields (PatientName, OperatorsName, etc.) should be formatted as `Last^First^Middle^Prefix^Suffix` according to the [DICOM standard](https://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html#sect_6.2.1). This rule applies both when editing the DICOM tags manually and when they are filled in automatically (see [Integrating the Dicomizer](#integrating-the-dicomizer)).
{{% /notice %}}

{{% notice tip %}}
Various actions are accessible from the contextual menu of a thumbnail:
- **Edit** (only for image): Opens the Photo Editor to crop, rotate, or adjust the image. Double-clicking on the thumbnail has the same effect.
- **Remove**: Deletes the image from the series without affecting the original file.
- **Move to...**: Moves the image to a different series.  
{{% /notice %}}

### Edit the Images

The **Photo Editor** provides tools to crop, rotate, and adjust the image contrast. You can also add annotations to highlight specific areas and use measurement tools to indicate distances, angles, or areas. Additionally, the image can be calibrated using a known distance for getting real-world measurements.

### Publish DICOM Files

Click the **Publish** button to send DICOM files to a remote DICOM archive, or the **Export locally** button to save the files to your local system. The **Publication** panel provides the following options:
- Select specific DICOM items for publication (all items are selected by default).
- Adjust the resolution for images with high resolution.
- Choose the target destination for the DICOM files from a list of remote DICOM nodes.
- Choose a calling node (Sender AET Title) that complies with your archive’s restrictions, if applicable.

{{% notice note %}}
The destination can be a specific remote node or a list of remote nodes available from the main menu, open _File > Preferences (Alt + P)_ and select "DICOM node list" and edit or add a new DICOM node.
{{% /notice %}}

{{% notice tip %}}
A green-checked icon on the thumbnail indicates that the image has been successfully published.
{{% /notice %}}

-----

## <center>Integrating the Dicomizer</center>

This section is intended for administrators integrating the Dicomizer into a clinical workflow. It describes how to launch the Dicomizer from a web context and, above all, how to fill in the DICOM metadata automatically so that operators do not have to enter it manually.

### Launch from a Web Context

The Dicomizer can be launched from a web context with the `weasis://` [protocol](../getting-started/weasis-protocol).

An example for launching Weasis Dicomizer {{< launch >}}$weasis:config pro="felix.extended.config.properties file:conf/dicomizer.json" pro="gosh.port 17181"{{< /launch >}} with the following parameters:
{{< highlight shell >}}
$weasis:config pro="felix.extended.config.properties file:conf/dicomizer.json" pro="gosh.port 17181"
{{< /highlight >}}

### Automatically Fill in the Metadata

Instead of being entered manually in the **Album** panel, the Global tags (patient and study levels) can be populated automatically:

- **From a DICOM Worklist**, configured with the [preference items](../basics/customize/preferences) starting with `weasis.acquire.wkl`. Here is an example to set the [configuration at launch](../getting-started/weasis-protocol/#modify-the-launch-parameters):<br>
  {{< highlight shell >}}
  $weasis:config pro="felix.extended.config.properties file:conf/ext-dicomizer.properties" pro="gosh.port 17181" pro="weasis.acquire.wkl.host localhost" pro="weasis.acquire.wkl.aet DCM4CHEE" pro="weasis.acquire.wkl.port 11112" pro="weasis.acquire.wkl.station.aet WEASIS-MWL"
  {{< /highlight >}}

- **With the [acquire:patient](../basics/commands/#acquirepatient) command**, providing an XML encoded as a DICOM XML file, e.g.:
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
Which DICOM tags are displayed, editable and required in the **Album** panel can be configured through the [preferences](../basics/customize/preferences) (items starting with `weasis.acquire.meta`).
{{% /notice %}}

### Publication Destination

When the Dicomizer destination is specified in the [preferences](../basics/customize/preferences) (items starting with `weasis.acquire.dest`), the destination is no longer selectable in the **Publication** panel: the DICOM files are sent directly to the configured node.
