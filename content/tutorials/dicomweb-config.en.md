---
title: DICOMWeb Import
weight: 12
description: How to configure DICOMWeb node
keywords: [ "dicom import", "dicomweb", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer", "pacs viewer" ]
---

## <center>How to configure DICOMWeb node</center>

This page explains how to configure DICOMWeb nodes in Weasis for [retrieving images remotely](../dicom-import/#dicom-queryretrieve). While manual configuration in Weasis is covered here, you can also [launch Weasis from a web context](../../basics/customize/integration/#download-directly-with-dicomweb-restful-services) with automatic DICOMWeb parameters derived from the URL.

### General Configuration Steps

1. Open _File > Preferences_ (Alt + P)
2. Select "DICOM node list" from the left sidebar
3. Click the "Add new" button to create a new node or select an existing one and click "Edit"

![DICOMWeb nodes configuration](/tuto/dicomweb-nodes.png?classes=shadow&width=750)

<br>

Here are the steps for configuring a new DICOMWeb node:
1. Create a new DICOMWeb node with a descriptive name
2. Select one of the service type. The default one is `DICOMWeb (all RESTful services)` which covers all DICOMWeb services. If you want to use a specific service, select the corresponding one:
   - `QIDO-RS`: Query
   - `STOW-RS` : Store
   - `WADO-URI (non-RS)`: legacy retrieval for one DICOM object
   - `WADO-RS (Retrieve)`: Retrieve
3. Enter the service URL of the DICOMWeb server.
4. Configure authentication by clicking the "Manager" button and then "Add":
   - Either select a template from the list and click "Fill" to auto-fill some fields or fill them manually.
   - In the _Provider_ panel, all the fields are mandatory. 
   - In the _Registration_ panel, the fields are optional. However, if you want to use the OAuth2 authentication, you need to fill in the Client ID, Client Secret, and the Scope. Audience is not mandatory but can be useful for some specific providers.
   - Click "OK" to save the authentication
5. Optionally, add HTTP headers for the service URL. This can be used for authentication or other purposes.
6. Click "OK" to save the authentication

Then open the [DICOM Import](../dicom-import/#from-weasis-menu-or-toolbar) dialog and select the node just created. You can now query the DICOMWeb server after logging in with your account into your browser when using OAuth2 authentication.

### Supported DICOMWeb Providers (non-exhaustive list)

#### Google Cloud Healthcare API

Google Cloud provides a comprehensive [DICOMWeb implementation](https://cloud.google.com/healthcare/docs/how-tos/dicomweb) through their Healthcare API.

Configuration steps:
1. Create a new DICOMWeb node with a descriptive name
2. Select `DICOMWeb (all RESTful services)`
3. Enter the Google repository URL (must end with `/dicomWeb`)
4. Configure authentication by clicking the *Manager* button and then *Add*:
    1. Select "Google Cloud Healthcare" template
    2. Click "Fill"
    3. Enter your Client ID and Client Secret
    4. Click "OK" to save the authentication
5. Optionally, add HTTP headers for the Google API
6. Click "OK" to save the authentication

![Google node](/tuto/dicomweb-google-node.png?classes=shadow&width=750)

<br>

![Google template](/tuto/dicomweb-google-auth.png?classes=shadow&width=750)

{{% notice note %}}
Currently, the DICOMWeb service for getting thumbnails doesn't work in the Google API.
{{% /notice %}}

#### Orthanc WEB Server

[Orthanc](https://www.orthanc-server.com/) is a lightweight DICOM server with [DICOMWeb capabilities](https://www.orthanc-server.com/static.php?page=dicomweb).

The configuration in the image below is for the demo server without authentication. For a custom Orthanc server, you need to enter the URL of your Orthanc server and define the authentication method (see [above](#general-configuration-steps)).

{{< highlight text >}}
https://demo.orthanc-server.com/dicom-web
{{< /highlight >}}

![Orthanc node](/tuto/dicomweb-orthanc.png?classes=shadow&width=750)

<br>

{{% notice note %}}
Currently, the DICOMWeb service of Orthanc doesn't support the [thumbnail service](https://www.dicomstandard.org/news/supplements/view/thumbnail-service-over-dicomweb).
{{% /notice %}}

#### dcm4chee-arc-light

[dcm4chee-arc-light](https://github.com/dcm4che/dcm4chee-arc-light) is a robust open-source Picture Archiving and Communication System (PACS) that supports DICOMWeb services.

To configure a dcm4chee-arc-light node:
1. Add a new DICOMWeb node
2. Enter a description (e.g., "DCM4CHEE Archive")
3. Select DICOMWeb service
4. Enter the URL of your dcm4chee-arc-light server. The default endpoint typically follows this pattern:
    {{< highlight text >}}
    http(s)://[server-address]:8080/dcm4chee-arc/aets/[AE_TITLE]/rs
    {{< /highlight >}}

If authentication is required:
1. Click on the *Manager* button
2. Click *Add* to create a new authentication
3. Select "Default Keycloak" from the templates and fill in the other required fields

#### Amazon HealthLake

[Amazon HealthLake](https://aws.amazon.com/healthlake/) is a fully managed service that enables healthcare organizations to store, transform, query, and analyze health data at scale.

With AHI DICOMWeb Proxy you can use the DICOMWeb API to access your data in Amazon HealthLake. Simply create a DICOMWeb node in Weasis with the following URL:
    {{< highlight text >}}
    http://[EC2 instance IP or EC2/ALB DNS]:8080/aetitle
    {{< /highlight >}}

See also the Weasis configuration at the end of this [page](https://github.com/aws-samples/aws-healthimaging-samples/tree/main/dicomweb-proxy#usage).