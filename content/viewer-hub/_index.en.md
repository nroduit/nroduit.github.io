---
title: ViewerHub
weight: 15
pre: "<b>3. </b>"
keywords: [ "viewer-hub", "weasis-viewer-hub", "launcher", "dicom viewer", "pacs", "dicom", ]
---

[**ViewerHub**](https://github.com/nroduit/viewer-hub) is the successor to [weasis-pacs-connector](https://github.com/nroduit/weasis-pacs-connector). It allows to launch different viewers (such as Weasis, Ohif, 3D Slicer, MicroDicom) depending on search criteria.

This is a server component with an administration interface for managing viewers selection, preferences, plugins, and versions of Weasis with DICOM archives.

Essentially, it simplifies the management of viewers in IT environments and facilitates connections to DICOM archives.

The main features of ViewerHub are:
- Viewers launch selection depending on modalities and archives
- Management of Weasis user preferences
- Control of launch contexts and profiles by user, group, or host
- Handling of live minor version updates of Weasis at the client side
- Management of Weasis translation packages
- Integration with connectors for DICOM archives
- Configuration of Keycloak clients and token transmission for DICOMWeb or WADO URI calls

Here is a list of pages related to ViewerHub documentation:
{{% children description="true" %}}




