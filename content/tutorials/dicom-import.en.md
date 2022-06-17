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

From the main menu, open File > Import > DICOM or from the first import button in the toolbar. ![Open toolbar](/tuto/dicom-open-icon.png?classes=shadow)

In order to import DICOM CD/DVD go the main menu, open File > Import > DICOM CD or from the second import button in the toolbar.

Select a way to import DICOM

* Local Device:
  * Files and/or folders: list of selected items or unique path
  * Search recursively: when this option is activated the import takes into account the subdirectories
  * Open in new tab: it allows to manage the way new tabs are opened
* DICOM ZIP:
  * Select: browse a DICOM zip file. When the archive file is encrypted, a password prompt is displayed.
  * Open in new tab: it allows to manage the way new tabs are opened.
* DICOMDIR: from a DICOM CD/DVD or a folder containing a DICOMDIR
  * Path: browse a folder containing a DICOMDIR
  * Detect CD-ROM: try to load a DICOM CD/DVD
  * Copy images into the local temporary directory: useful for slow reading device like CD-ROM
* DICOM Query/Retrieve:
  * On DICOM Source tab:
    ![DICOM import archive](/tuto/dicom-import-archive.png?classes=shadow)
    * Archive: select the archive to query
      * With DICOM nodes: classic DIMSE C-Find with C-Move, C-Get or WADO-URI for retrieving DICOM files
      * With DICOMWeb nodes: QIDO and WADO-RS for retrieving DICOM files
    * Retrieve (only with DICOM archive): the protocol to retrieve the images
      * C-MOVE: the classic DIMSE protocol (accepts all sop classes, not recommended for WEB)
      * C-GET: transfer syntaxes are negotiated by each sop classes according a configuration file
      * WADO-URI: required a WADO server (C-Find + WADO retrieve)
    * Calling Node (only with DICOM archive): select the adapted calling DICOM node
    * More options: allows to open the preferences to configure the DICOM nodes
  * On Search Criteria tab:
  ![Thumbnails](/tuto/dicom-import-search.png?classes=shadow&width=700px)
    1. Fill in one or more search criteria. Criteria can be saved and reuse later.
    2. Adapt le limit of replies (optional)
    3. Click on Search
    4. Select the exams you want to import
    5. Start importing and close the window

{{% notice tip %}}
When a query is too long, try to click on the *Clear* button in *Search Criteria* in order to cancel the request.
{{% /notice %}}

### From commands

See this [page](../../getting-started/weasis-protocol/#examples-to-load-images)
