---
title: Manager
weight: 30
pre: "<b>4. </b>"
keywords: [ "manager", "weasis-manager", "launcher", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", ]
---

## <center>Weasis Manager</center>

weasis-manager is the successor to [weasis-pacs-connector](https://github.com/nroduit/weasis-pacs-connector). This is a server component with an administration interface for managing preferences, plugins and versions of Weasis with DICOM archives.

In short, it simplifies the management of Weasis in an IT environment and its link with a DICOM archive.

The main features are:
- Itinerant management of user preferences
- Launch context management (plugin configuration, menu and toolbar management) by user, group or host machine
- Management of minor version updates based on this compatibility file and by importing weasis-native.zip (since weasis 3.6.0)
- Management of the translation packages (built every day)
- Several types of connectors for interfacing with a DICOM archive
- Allows you to configure a client in Keycloack and transmit the token to Weasis for DICOMWeb or WADO URI calls (solves the problem of limiting URIs to 2048 characters under Windows, where the token is truncated when passed through the weasis:// uri)

{{% children %}}

