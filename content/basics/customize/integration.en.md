---
title: Integration
weight: 10
description: How connecting Weasis to a PACS, RIS, EMR or any web interface
keywords: [ "workflow", "integration", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to launch Weasis from any environments</center>

Here we present how to launch Weasis with associated images from any context either [using weasis-pacs-connector](#use-weasis-pacs-connector) or by [building its own connector](#build-your-own-connector). The launch of the application is based on the [weasis protocol](../../../getting-started/weasis-protocol) available since version 3.5. However, it is still possible to use weasis 3.5 with Java Webstart (but only with Java 8 to 10), see the [old documentation](../../../old/integration).

The easiest way to launch Weasis from a web context is to use <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a>.
{{% notice note %}}
Requires Weasis 3.5 (or superior) installed on the system with a [native installer](../../../getting-started/).
{{% /notice %}}


## Use weasis-pacs-connector

For connecting to dcm4chee web interface, follow the instructions in [Installing Weasis in DCM4CHEE](../../../getting-started/dcm4chee). Otherwise, refer to the documentation of <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a>.

Standard workflow when connecting Weasis to a PACS, RIS, EMR, EPR or any web interface:

{{< svg "static/images/weasis-pacs-connector.svg" >}}
{{% notice note %}}
The schema above shows that the queries to the PACS are made at the same time as the viewer starts. This makes it possible to optimize the launch by simultaneously launching weasis and creating the manifest.
{{% /notice %}}

## Build your own connector

This documentation describes how to create your own connector without weasis-pacs-connector and without having an archive with a WADO-URI service. There are two parts:

1. Building an URI for launching Weasis
2. Building a XML manifest to download images

###  Build an URI

Build an URI using the [weasis protocol](../../../getting-started/weasis-protocol/#how-to-build-an-uri) that will launch Weasis with a specific configuration.

{{% notice tip %}}
<a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a> services are based on jnlp templates and they allow either to build a manifest from a PACS via DICOM C-Find or to upload the manifest by http POST.
{{% /notice %}}

###  Build an XML manifest
Build an XML file containing the UIDs of the images which will be retrieved from Weasis. There is <a target="_blank" href="https://github.com/nroduit/Weasis/blob/master/weasis-dicom/weasis-dicom-explorer/src/main/resources/config/manifest.xsd">XLS</a> to validate the content of xml. This output file can be either compressed in gzip or uncompressed. Here is an example:
{{< highlight xml >}}
<?xml version="1.0" encoding="UTF-8" ?>
<manifest xmlns="http://www.weasis.org/xsd/2.5" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <arcQuery additionnalParameters="" arcId="1001" baseUrl="http://archive-weasis.rhcloud.com/archive/wado" requireOnlySOPInstanceUID="false">
        <Patient PatientID="H13885_9M" PatientName="TEST NON SQUARE PIXELS" PatientSex="F">
            <Study AccessionNumber="" ReferringPhysicianName="" StudyDate="20130711" StudyDescription="TEST NON SQUARE PIXELS" StudyID="PKD" StudyInstanceUID="2.16.756.5.5.100.397184556.14391.1373576413.1508" StudyTime="170013">
                <Series Modality="US" SeriesDescription="NON SQUARE PIXELS: PIXEL ASPECT RATIO" SeriesInstanceUID="1.2.40.0.13.1.1.87878503032592846377547034671833520632" SeriesNumber="2">
                    <Instance InstanceNumber="107" SOPInstanceUID="1.2.40.0.13.1.1.126082073005720329436273995268222863740"/>
                </Series>
                <Series Modality="MR" SeriesDescription="NON SQUARE PIXELS: PIXEL SPACING" SeriesInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1" SeriesNumber="40001">
                    <Instance InstanceNumber="1" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1.0"/>
                    <Instance InstanceNumber="2" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1.1"/>
                    <Instance InstanceNumber="3" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1.2"/>
                    <Instance InstanceNumber="4" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1.3"/>
                </Series>
                <Series Modality="MR" SeriesDescription="NON SQUARE PIXELS: PIXEL SPACING" SeriesInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2" SeriesNumber="50001">
                    <Instance InstanceNumber="1" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2.0"/>
                    <Instance InstanceNumber="2" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2.1"/>
                    <Instance InstanceNumber="3" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2.2"/>
                    <Instance InstanceNumber="4" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2.3"/>
                </Series>
            </Study>
        </Patient>
    </arcQuery>
</manifest>
{{< /highlight >}}
{{% notice note %}}
Important Parameters (except mandatory parameters defined in xsd):

- `PatientBirthDate` helps to identify a patient.
- `StudyDate,` `StudyTime`, `Modality`, `SeriesNumber` and `InstanceNumber` help to sort data before downloading images.
- `SeriesDescription` and `StudyDescription` allow to immediately display the descriptions before downloading the images.
{{% /notice %}}

{{% notice tip %}}
From Weasis 2.5 it is possible to have multiple archives (allows to have several arcQuery tags) and the <a target="_blank" href="https://github.com/nroduit/Weasis/blob/master/weasis-dicom/weasis-dicom-explorer/src/main/resources/config/presentations.xsd">presentations</a> tag which contains the image annotations.
{{% /notice %}}

###  Build an XML manifest (no WADO server)
This example requires only a WEB server. Weasis will download files by URLs.
{{< highlight xml >}}
<?xml version="1.0" encoding="utf-8" ?>
<manifest xmlns="http://www.weasis.org/xsd/2.5" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <arcQuery additionnalParameters="" arcId="1001" baseUrl="http://archive-weasis.rhcloud.com/archive/wado" requireOnlySOPInstanceUID="false">
    <Patient PatientBirthDate="20010901" PatientID="017589" PatientName="Validate WADAKOKOA">
      <Study StudyDate="20100421" StudyDescription="胸部立位 Ｖ→Ｄ犬4" StudyInstanceUID="1.2.392.200036.9107.500.11141010042100073" StudyTime="113836">
        <Series DirectDownloadThumbnail="thumb_4563173729424544.jpg" Modality="CR" SeriesDescription="Ｖ→Ｄ犬4" SeriesInstanceUID="1.2.392.200036.9107.500.305.1410.141010042100073.121" SeriesNumber="1">
          <Instance DirectDownloadFile="image_4563173729424543.dcm" InstanceNumber="1" SOPInstanceUID="1.2.392.200036.9107.500.305.1410.20100421.114831.109.101410"/>
          <Instance DirectDownloadFile="image_4563173729424544.dcm" InstanceNumber="2" SOPInstanceUID="1.2.392.200036.9107.500.305.1410.20100421.114828.234.101410"/>
          <Instance DirectDownloadFile="image_4563173729424545.dcm" InstanceNumber="3" SOPInstanceUID="1.2.392.200036.9107.500.305.1410.20100421.114823.421.101410"/>
        </Series>
      </Study>
    </Patient>
  </arcQuery>
</manifest>
{{< /highlight >}}
{{% notice note %}}
Required Parameters:

- `DirectDownloadFile` defines the URL of the DICOM file to download (the final URL is the combination of wadoURL + DirectDownloadFile)
- `DirectDownloadThumbnail` defines the URL of the JPEG file representing the series (the final URL is the combination of wadoURL + DirectDownloadThumbnail)
- See in the previous note above.
{{% /notice %}}
