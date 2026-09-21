---
title: "Connect Weasis to a DICOMweb Archive"
linkTitle: "DICOMweb Archives"
description: "Launch Weasis straight from a DICOMweb archive: dcm4chee-arc-light, Orthanc, Google Cloud Healthcare, DICOMcloud, Kheops or Amazon HealthImaging."
keywords: [ "weasis dicomweb", "launch weasis from orthanc", "weasis dcm4chee", "google cloud healthcare weasis", "kheops weasis", "amazon healthimaging dicom viewer", "qido-rs", "wado-rs", "dicomweb archive integration" ]
weight: 12
---

## <center>Query and retrieve straight from the archive, without a connector</center>

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
**Known issue on Windows**: Weasis cannot open the images because of the token length which is cut by the browser. It is only working with Firefox on Windows. It is recommended to use [weasis-pacs-connector](integration/#use-weasis-pacs-connector) or [ViewerHub](../../viewer-hub) to solve this issue.
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

## See also

- [Integration](integration) — the launch contexts, weasis-pacs-connector and the manifest formats.
- [DICOMweb Configuration](../../tutorials/dicomweb-config) — configuring a DICOMweb node from
  inside Weasis, for a reader who is not building the launch URL themselves.
