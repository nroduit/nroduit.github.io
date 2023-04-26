---
title: DICOMWeb Import
weight: 12
description: How to configure DICOMWeb node
keywords: [ "dicom import", "dicomweb", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer", "pacs viewer" ]
---

## <center>How to configure DICOMWeb node</center>

This page explains how to configure a remote archive in DICOMWeb and then use this DICOMWeb node to [retrieve exams remotely](../dicom-import/#dicom-queryretrieve). However, it is also possible, without any prior configuration, to [launch Weasis from a web context](../../basics/customize/integration/#download-directly-with-dicomweb-restful-services) by passing it some parameters to retrieve images in DICOMWeb.

From the main menu, open File > Preferences (Alt + P) and select DICOM node list.
![DICOMWeb nodes](/tuto/dicomweb-nodes.png?classes=shadow&width=750)
<br>
### Google Cloud Healthcare API

Google provides a [Cloud Healthcare API's implementation of DICOMweb](https://cloud.google.com/healthcare/docs/how-tos/dicomweb).

1. Add a new DICOMWeb node and enter a description
2. Select DICOMWeb service
3. Enter the URL of a Google repository (must ends with /dicomWeb)
4. Add an authentication by clicking on the *Manager* button and then click on *Add*

![Google node](/tuto/dicomweb-google-node.png?classes=shadow&width=750)
<br>
1. Select the Google Cloud Healthcare template
2. Click on *Fill* and optionally edit the name
3. Enter your *Client ID* and *Client Secret*, Click on OK and close the other windows. Then open the [DICOM Import](../dicom-import/#from-weasis-menu-or-toolbar) dialog and select the node.

![Google template](/tuto/dicomweb-google-auth.png?classes=shadow&width=750)

Currently, the DICOMWeb service for getting thumbnails doesn't work in the Google API.

### Orthanc WEB Server

[Orthanc](https://www.orthanc-server.com/) is a lightweight DICOM server with [DICOMWeb capabilities](https://www.orthanc-server.com/static.php?page=dicomweb).

Currently, the DICOMWeb service of Orthanc doesn't support the [thumbnail service](https://www.dicomstandard.org/news/supplements/view/thumbnail-service-over-dicomweb).

Create a new DICOMWeb node with the following URL (example with the demo server without authentication):

{{< highlight text >}}
https://demo.orthanc-server.com/dicom-web
{{< /highlight >}}

![Orthanc node](/tuto/dicomweb-orthanc.png?classes=shadow&width=750)
<br>
### dcm4chee-arc-light

### Kheops

