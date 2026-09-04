---
title: Integration
weight: 10
description: How connecting Weasis to a PACS, RIS, EMR or any web interface
keywords: [ "workflow", "integration", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to launch Weasis from any environments</center>

Here we present how to launch Weasis with associated images from any context either [using weasis-pacs-connector](#use-weasis-pacs-connector) or [ViewerHub](../../viewer-hub) as its successor
or by [building your own connector](#build-your-own-connector). The launch of the application is based on the [weasis protocol](../../getting-started/weasis-protocol) available {{< since "3.5.3" >}}.

Using [weasis-pacs-connector](https://github.com/nroduit/weasis-pacs-connector) or [ViewerHub](../../viewer-hub) allows a high degree of integration and facilitates connection to a PACS. Here are some of the advantages:

- Automatically build a manifest according to a configuration with a PACS
- The initial URL starts with HTTP and is then redirected to weasis://? (useful when a custom URI scheme is not allowed by wiki, blog platforms, etc.)
- Efficiently manages to build the manifest simultaneously with the start of Weasis, optimizing loading time
- Easily handles secure manifest requests and manages tokens for the DICOMWeb services

However, it is also possible: 
- To [build your own connector](#build-your-own-connector) for custom integrations
- To let Weasis [querying DICOMWeb services](#download-directly-with-dicomweb-restful-services) directly, bypassing any connector when supported like
    - [dcm4chee-arc-light](#dcm4chee-arc-light)
    - [Orthanc WEB Server](#orthanc-web-server)
    - [Google Cloud Healthcare API](#google-cloud-healthcare-api)
    - [DICOMcloud (for Azure cloud)](#dicomcloud-for-azure-cloud)
    - [Kheops](#kheops)
    - [Amazon HealthImaging](#amazon-healthimaging)
- To configure the DICOM archive in Weasis with Dicom [Query/Retrieve](../../tutorials/dicom-import/#dicom-queryretrieve) or [DICOMWeb](../../tutorials/dicomweb-config)

These integrations provide flexibility to meet the specific needs of healthcare environments, ensuring seamless integration.

{{% notice note %}}
Requires Weasis installed on the system with the [native installer](../../getting-started/).
{{% /notice %}}


## Use weasis-pacs-connector

For connecting to dcm4chee web interface, follow the instructions in [Installing Weasis in DCM4CHEE](../../getting-started/dcm4chee). Otherwise, refer to the documentation of [weasis-pacs-connector](https://github.com/nroduit/weasis-pacs-connector#installation).

Standard workflow when connecting Weasis to a PACS, RIS, EMR, EPR or any web interface:

{{< svg "static/images/weasis-pacs-connector.svg" >}}
{{% notice note %}}
The schema above shows that the queries to the PACS are made at the same time as the viewer starts. This makes it possible to optimize the launch by simultaneously launching weasis and building the manifest.
{{% /notice %}}

{{% notice tip %}}
[weasis-pacs-connector](https://github.com/nroduit/weasis-pacs-connector) services allow either to build a manifest from a PACS via DICOM C-Find or to upload the manifest by http POST.
{{% /notice %}}

## Build your own connector

This documentation describes how to create your own connector without weasis-pacs-connector and with different DICOM archive types. The [weasis protocol](../../getting-started/weasis-protocol/#how-to-build-a-uri) allows you to build URIs to launch Weasis according to different configurations and allows to load DICOM files locally or remotely.

Here are examples with XML manifests or with DICOMWeb RESTful services.

### Build an XML manifest

Use [$dicom:get](../commands/#dicomget) to load a XML manifest returned by your service.
{{< highlight text >}}
$dicom:get -w "https://myservice/manifest?studyUID=2.16.756.5.5.100.397184556.14391.1373576413.1508"
{{< /highlight >}}

Build an XML file containing the UIDs of the images which will be retrieved from Weasis. There is [XLS](https://github.com/nroduit/Weasis/blob/master/weasis-dicom/weasis-dicom-explorer/src/main/resources/config/manifest.xsd) to validate the content of xml. This output file can be either compressed in gzip or uncompressed. Here is an example:
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
- `SeriesDescription` and `StudyDescription` allow immediately displaying the descriptions before downloading the images.
{{% /notice %}}

{{% notice tip %}}
From Weasis 2.5 it is possible to have multiple archives: several `arcQuery` tags are allowed in the same manifest.
{{% /notice %}}

### Build a JSON manifest {#json-manifest}

The manifest may also be served as **JSON** {{< since "4.7.2" >}}. The structure mirrors the 2.5 XML manifest one-for-one — same node names, same attributes — so a connector only has to change its serialization:

{{< highlight json >}}
{
  "manifest": {
    "arcQuery": [
      {
        "arcId": "1001",
        "baseUrl": "https://archive/dicom-web",
        "queryMode": "DICOM_WEB",
        "Patient": [
          {
            "PatientID": "H13885_9M",
            "PatientName": "TEST NON SQUARE PIXELS",
            "Study": [
              {
                "StudyInstanceUID": "2.16.756.5.5.100.397184556.14391.1373576413.1508",
                "Series": [
                  {
                    "SeriesInstanceUID": "2.16.756.5.5.100.397184556.7220.1373578035.1",
                    "Modality": "MR",
                    "Instance": [
                      { "SOPInstanceUID": "2.16.756.5.5.100.397184556.7220.1373578035.1.0", "InstanceNumber": "1" }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
{{< /highlight >}}

Both formats are loaded with the same [$dicom:get](../commands/#dicomget) command and both may be gzip-compressed. A few rules to be aware of:

- The format is detected from the **content**, not from the file extension or the `Content-Type`: a document starting with `{` is parsed as JSON, otherwise as XML.
- Weasis requests `Accept: application/xml` by default. XML is parsed as a **stream**, so it stays the better choice for large instance-level manifests, while JSON is fully buffered in memory. Launch Weasis with `-Dweasis.manifest.accept=json` to request JSON instead.
- A node holding a single child accepts either a JSON object or an array of objects.

### Partial DICOMweb manifest and series bulk retrieve {#partial-manifest}

An `arcQuery` in `DICOM_WEB` mode (`queryMode="DICOM_WEB"`) may stop at the **Patient**, **Study** or **Series** level instead of listing every SOP instance {{< since "4.7.2" >}}. Weasis completes the missing levels itself with QIDO-RS queries targeted by UID on the manifest `baseUrl` (`{baseUrl}/studies/{studyUID}/series`), which keeps the manifest small and shifts the enumeration cost to the moment the data is actually needed.

The new `seriesRetrieve` attribute of `arcQuery` controls how a series with no listed instance is downloaded:

| Value | Behavior |
|-------|----------|
| `true` | The series is retrieved in **bulk** — one single series-level WADO-RS request instead of one request per instance. |
| `false` | The instances are enumerated then downloaded individually. |
| *(absent)* | Falls back to the `weasis.dicom.web.series.bulk` system property. |

The attribute is ignored for non-`DICOM_WEB` manifests.

{{% notice note %}}
A manifest that already carries the `Instance` level keeps the previous behavior: listing the instances remains the way for the archive connector to control exactly which objects are loaded.
{{% /notice %}}

### Build an XML manifest (no WADO server)
This example requires only a WEB server. Weasis will download DICOM files by URLs.

Use [$dicom:get](../commands/#dicomget) to load a <a target="_blank" href="https://nroduit.github.io/demo-archive/Lumbar/mf.xml">XML manifest</a> containing direct links {{< launch >}}$dicom:get -w "https://nroduit.github.io/demo-archive/Lumbar/mf.xml"{{< /launch >}}
{{< highlight text >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/Lumbar/mf.xml"
{{< /highlight >}}

{{% notice note %}}
Required Parameters:

- `DirectDownloadFile` defines the URL of the DICOM file to download (the final URL is the combination of wadoURL + DirectDownloadFile)
- `DirectDownloadThumbnail` defines the URL of the JPEG file representing the series (the final URL is the combination of wadoURL + DirectDownloadThumbnail)
- See in the previous note above.
{{% /notice %}}


## Download directly with DICOMWeb RESTful services

This integration requires a PACS/VNA with [DICOMweb](https://www.dicomstandard.org/using/dicomweb) services (QUERY/RETRIEVE) where the requests are managed directly by Weasis. Here are some of the advantages:

- Straightforward integration
- Do not require to install weasis-pacs-connector
- Allow passing token directly in headers (not in the URL)

The following configurations allow images to be loaded by initiating the request from a WEB context. However, it is possible to access DICOMWeb services by initiating the request directly from the [Weasis import](../../tutorials/dicom-import).

Use [$dicom:rs](../commands/#dicomrs) to load DICOM files. Here are some configuration examples of DICOMweb applications:

### dcm4chee-arc-light

This configuration requires at least dcm4chee-arc-light 5.22.2 and Weasis 3.6.0. To activate Weasis in dcm4chee-arc-light user interface, you need to add the four following properties in the web portal from the left menu *Configuration > Devices > dcm4chee-arc > Extensions > Edit extension > Child Objects > Web Applications > DCM4CHEE*
{{< highlight text >}}
IID_PATIENT_URL=weasis://?$dicom:rs --url "{{qidoBaseURL}}{{qidoBasePath}}" -r "patientID={{patientID}}" --query-ext "&includedefaults=false" -H "Authorization: Bearer {{access_token}}"
IID_STUDY_URL=weasis://?$dicom:rs --url "{{qidoBaseURL}}{{qidoBasePath}}" -r "studyUID={{studyUID}}" --query-ext "&includedefaults=false" -H "Authorization: Bearer {{access_token}}"
IID_URL_TARGET=_self
{{< /highlight >}}

The properties can also be passed directly to the docker-compose.env file:
{{< highlight text >}}
IID_PATIENT_URL=weasis://?$dicom:rs --url "{{qidoBaseURL}}{{qidoBasePath}}" -r "patientID={{patientID}}" --query-ext "\&includedefaults=false" -H "Authorization: Bearer {{access_token}}"
IID_STUDY_URL=weasis://?$dicom:rs --url "{{qidoBaseURL}}{{qidoBasePath}}" -r "studyUID={{studyUID}}" --query-ext "\&includedefaults=false" -H "Authorization: Bearer {{access_token}}"
IID_URL_TARGET=_self
{{< /highlight >}}

Finally, refresh the page for having the viewer button.

{{% notice warning %}}
Configuration notes:

- See [configuration](../../getting-started/dcm4chee) for versions before 5.22.2.
- From 5.24.0 {{qidoBaseURL}} must be replaced by your base URL (e.g. https://pacs2.test.com:8443)
- The character '&' must be escaped in the Docker environment variables.
- The Authorization header is not required for unsecure service.
- URL with HTTPS requires a real valid certificate; otherwise, the certificate must be imported into the Weasis Java keystore or must be installed at [system level](https://github.com/nroduit/Weasis/issues/679) {{< since "4.6.1" >}}.
{{% /notice %}}

{{% notice note %}}
**Known issue on Windows**: Weasis cannot open the images because of the token length which is cut by the browser. It is only working with Firefox on Windows. It is recommended to use [weasis-pacs-connector](#use-weasis-pacs-connector) or [ViewerHub](../../viewer-hub) to solve this issue.
{{% /notice %}}

### Orthanc WEB Server

https://www.orthanc-server.com/static.php?page=dicomweb

{{< highlight text >}}
$dicom:rs --url "https://demo.orthanc-server.com/dicom-web" -r "patientID=ozp00SjY2xG"
{{< /highlight >}}

{{< launch >}}
$dicom:rs --url "https://demo.orthanc-server.com/dicom-web" -r "patientID=ozp00SjY2xG"
{{< /launch >}}

Currently, the DICOMWeb service of Orthanc doesn't support:

- Thumbnail service is not implemented.

### Google Cloud Healthcare API

https://cloud.google.com/healthcare/docs/how-tos/dicomweb

{{< highlight text >}}
$weasis:config pro="dicom.qido.query.multi.params true" $dicom:rs --url "https://healthcare.googleapis.com/v1beta1/projects/chc-nih-chest-xray/locations/us-central1/datasets/nih-chest-xray/dicomStores/nih-chest-xray/dicomWeb" -r "studyUID=1.3.6.1.4.1.11129.5.5.184301693334578016850836775758484230512396" -H "Authorization: Bearer <your-token>"
{{< /highlight >}}

Currently, the DICOMWeb service for getting thumbnails doesn't work in the Google API.

{{% notice note %}}
`<your-token>` must be replaced by a valid token.
{{% /notice %}}

### DICOMcloud (for Azure cloud)

https://github.com/DICOMcloud/DICOMcloud

{{< highlight text >}}
$dicom:rs --url "https://dicomcloud.azurewebsites.net/api" -r "studyUID=1.3.6.1.4.1.14519.5.2.1.4429.7055.198257099234774234268879426857"
{{< /highlight >}}

{{< launch >}}
$dicom:rs --url "https://dicomcloud.azurewebsites.net/api" -r "studyUID=1.3.6.1.4.1.14519.5.2.1.4429.7055.198257099234774234268879426857"
{{< /launch >}}

{{% notice note %}}
The demo server is no longer accessible.
{{% /notice %}}

Currently, the DICOMWeb service of DICOMcloud doesn't support:

- Thumbnail service is not implemented.

### Kheops

https://kheops.online

{{< highlight text >}}
$dicom:rs --url "https://demo.kheops.online/api" -r "studyUID=1.3.6.1.4.1.14519.5.2.1.4429.7055.198257099234774234268879426857" -H "Authorization: Bearer <your-token>"
{{< /highlight >}}

{{% notice note %}}
`<your-token>` must be replaced by a valid token.
{{% /notice %}}

### Amazon HealthImaging

https://aws.amazon.com/health/health-imaging/

Prefer to use dicomweb-proxy to manage the token and the URL of the DICOMWeb service. See Weasis configuration at the end of this [page](
https://github.com/aws-samples/aws-healthimaging-samples/tree/main/dicomweb-proxy#usage).