---
title: Integration
weight: 10
description: How connecting Weasis to a PACS, RIS, EMR or any web interface
keywords: [ "workflow", "integration", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to launch Weasis from any environments</center>

Here we present how to launch Weasis with associated images from any context either [using weasis-pacs-connector](#use-weasis-pacs-connector) or by [building your own connector](#build-your-own-connector). The launch of the application is based on the [weasis protocol](../../../getting-started/weasis-protocol) available since version 3.5. However, it is still possible to use weasis 3.5 with Java Webstart (but only with Java 8 to 10), see the [old documentation](../../../old/integration).

Using <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a> allows a high degree of integration and facilitates connection to a PACS. Here are some of the advantages:

- The initial URL starts with http and is then redirected to weasis:// (as weasis:// is not allowed by wiki, blog…)
- Manages to build the manifest simultaneously with the start of Weasis
- The URL returns a manifest ID which can be requested only once (and must be <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector/blob/master/etc/dcm4chee-arc/weasis-pacs-connector.properties#L17">consumed within 5 min</a>)

However, it is possible to build your own connector for particular integrations or when a DICOMWeb service is available.

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

{{% notice tip %}}
<a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a> services allow either to build a manifest from a PACS via DICOM C-Find or to upload the manifest by http POST.
{{% /notice %}}

## Build your own connector

This documentation describes how to create your own connector without weasis-pacs-connector and with different DICOM archive types. The [weasis protocol](../../../getting-started/weasis-protocol/#how-to-build-an-uri) allows to build URIs to launch Weasis according to different configurations and allows to load DICOM files locally or remotely.

Here are examples with XML manifests or with DICOMWeb RESTful services.

###  Build an XML manifest

Use [$dicom:get](../../commands/#dicom-get) to load a XML manifest returned by your service.
{{< highlight text >}}
$dicom:get -w https://myservice/manifest?studyUID=2.16.756.5.5.100.397184556.14391.1373576413.1508
{{< /highlight >}}

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
This example requires only a WEB server. Weasis will download DICOM files by URLs.

Use [$dicom:get](../../commands/#dicom-get) to load a <a target="_blank" href="https://nroduit.github.io/samples/Lumbar/mf.xml">XML manifest</a> containing direct links <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FLumbar%2Fmf.xml" class="btn btn-default">Launch</a>
{{< highlight text >}}
$dicom:get -w https://nroduit.github.io/samples/Lumbar/mf.xml
{{< /highlight >}}

{{% notice note %}}
Required Parameters:

- `DirectDownloadFile` defines the URL of the DICOM file to download (the final URL is the combination of wadoURL + DirectDownloadFile)
- `DirectDownloadThumbnail` defines the URL of the JPEG file representing the series (the final URL is the combination of wadoURL + DirectDownloadThumbnail)
- See in the previous note above.
{{% /notice %}}


### Download directly with DICOMWeb RESTful services

This integration requires a PACS/VNA with <a target="_blank" href="https://www.dicomstandard.org/dicomweb/">DICOMweb™</a> services (QUERY/RETRIEVE) where the requests are managed directly by Weasis. Here are some of the advantages:

- Very simple integration
- Do not required to install weasis-pacs-connector
- Allow to pass token directly in headers (not in the URL)

Use [$dicom:rs](../../commands/#dicom-rs) to load DICOM files. Here are some configurations of open source systems:

#### dcm4chee-arc-light

To activate Weasis in dcm4chee-arc-light user interface (see the <a target="_blank" href="https://github.com/dcm4che/dcm4chee-arc-light/wiki/Weasis-Viewer-Integration">matrix of the required versions</a>, you need need to changes two attributes in the configuration. For this purpose, go to the <a target="_blank" href="http://localhost:8080/dcm4chee-arc/ui2/#/device/edit/dcm4chee-arc/dcmArchiveDevice/properties.dcmArchiveDevice">configuration</a> or from Configuration > Devices > dcm4chee-arc > Extensions > Archive Device 

- dcm4chee-arc unsecure (http):
    - Invoke Image Display Patient URL: `weasis://$dicom:rs --url "http://<your-host>:8080/dcm4chee-arc/aets/DCM4CHEE/rs" -r "&patientID={}"  --query-ext "&includedefaults=false"`
    - Invoke Image Display Study URL: `weasis://$dicom:rs --url "http://<your-host>:8080/dcm4chee-arc/aets/DCM4CHEE/rs" -r "&studyUID={}"  --query-ext "&includedefaults=false"`
- dcm4chee-arc secure (https):
    - Invoke Image Display Patient URL: `weasis://$dicom:rs --url "http://<your-host>:8080/dcm4chee-arc/aets/DCM4CHEE/rs" -r "&patientID={}"  --query-ext "&includedefaults=false" -H "Authorization: &access_token={}`
    - Invoke Image Display Study URL: `weasis://$dicom:rs --url "http://<your-host>:8080/dcm4chee-arc/aets/DCM4CHEE/rs" -r "&studyUID={}"  --query-ext "&includedefaults=false" -H "Authorization: &access_token={}`

{{% notice warning %}}
`<your-host>` must be replaced by the hostname of your dcm4che installation.
{{% /notice %}}

#### Orthanc WEB Server

https://www.orthanc-server.com/static.php?page=dicomweb

{{< highlight text >}}
$dicom:rs --url "https://demo.orthanc-server.com/dicom-web" -r "patientID=5Yp0E" --accept-ext=";"
{{< /highlight >}}

<a  href="weasis://%24dicom%3Ars%20--url%20%22https%3A%2F%2Fdemo.orthanc-server.com%2Fdicom-web%22%20-r%20%22patientID%3D5Yp0E%22%20--accept-ext%3D%22%3B%22" class="btn btn-default">Launch</a>


Currently the DICOMWeb service of Orthanc doesn't support:

- transfer-syntax=* doesn’t work (always get uncompressed image). Once this issue will be fixes `--accept-ext=";"` can be removed.
- Thumbnail service is not implemented.

#### Google Cloud Healthcare API

https://cloud.google.com/healthcare/docs/how-tos/dicomweb

{{< highlight text >}}
$weasis:config pro="dicom.qido.query.multi.params true" $dicom:rs --url "https://healthcare.googleapis.com/v1beta1/projects/chc-nih-chest-xray/locations/us-central1/datasets/nih-chest-xray/dicomStores/nih-chest-xray/dicomWeb" -r "studyUID=1.3.6.1.4.1.11129.5.5.184301693334578016850836775758484230512396" -H "Authorization: Bearer <your-token>"
{{< /highlight >}}

Currently the DICOMWeb service for getting thumnails doesn't work in the Google API.

{{% notice warning %}}
`<your-token>` must be replaced by the hostname of your dcm4che installation.
{{% /notice %}}
