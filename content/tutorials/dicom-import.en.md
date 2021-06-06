---
title: DICOM Import
weight: 10
description: How to import DICOM files
keywords: [ "dicom import", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>How to import DICOM files</center>

### From the system file explorer

#### Drag and drop

Files or folders selected from the system file explorer can be opened by dragging and dropping into the central area of Weasis (any files into empty area or specific files related to the view which is already open).

#### File association

Dicom files can be opened by double-clicking them from the system file explorer.
{{% notice note %}}
On Windows only the files with the extension ".dcm" are associated with Weasis. With other systems DICOM without extension are associated with Weasis.
{{% /notice %}}

### From Weasis menu or toolbar

From the main menu, open File > Import > DICOM or from the first import button in the toolbar.

![DICOM EXplorer](/tuto/import/ImportDICOM.png)

Select a way to import DICOM

* Local Device: from a path (file or folder)
* DICOM ZIP: from a DICOM ZIP file
* DICOMDIR: from a DICOM CD/DVD or a folder containing a DICOMDIR
* DICOM Query/Retrieve:
  * With DICOM nodes: classic DIMSE C-Find with C-Move, C-Get or WADO-URI for retrieving DICOM files
  * With DICOMWeb nodes: QIDO and WADO-RS for retrieving DICOM files

{{% notice tip %}}
When a query is too long, try to click on the "Clear" button to cancel the request.
{{% /notice %}}

### From commands

See this [page](../../getting-started/weasis-protocol/#examples-to-load-images)
