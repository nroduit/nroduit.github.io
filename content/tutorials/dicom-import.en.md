---
title: DICOM Import
weight: 10
description: How to import DICOM files
keywords: [ "dicom import", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>How to import DICOM files</center>

Weasis can ingest DICOM data from many sources:

- **Drag and drop** files, folders, or DICOM ZIP archives from the system file explorer.
- **Double-click** a DICOM file in the system file explorer (file association).
- **Local Device** — browse files, folders, or DICOM ZIP archives from inside Weasis.
- **DICOMDIR** — load a DICOM CD/DVD or any folder that contains a DICOMDIR index.
- **DICOM Query/Retrieve** — query a remote PACS over classic DICOM (C-FIND / C-MOVE / C-GET) or [DICOMweb](dicomweb-config) (QIDO / WADO-RS) and retrieve selected studies.
- **Commands** — local or remote commands launching Weasis with a target series (see the [Weasis Protocol](../getting-started/weasis-protocol/#examples-to-load-images)).

To send data the other way — out of Weasis to a file, a PACS node, or a CD/DVD — see [DICOM Export](dicom-export).

{{% notice note %}}
Whatever the import method, a popup may appear at the end of an import in any of these cases:

* **Error** — one or more DICOM files cannot be read because they are corrupted or malformed (since {{% badge title="Version" %}}4.3.0{{% /badge %}}).
* **Information** — since {{% badge title="Version" %}}4.7.0{{% /badge %}}, one or more valid DICOM files were skipped because their SOP Class has no viewer available (e.g. Raw Data Storage). These files are not corrupted, they are simply not displayable. The notification can be silenced with the **Don't show this again** checkbox in the dialog, or from the DICOM Explorer preferences (**Notify when DICOM files with an unsupported SOP Class are skipped**).
* **Network error** — when a network error occurs during a retrieve (DICOMweb or WADO), a message offers to download the missing files again.
{{% /notice %}}

### From the system file explorer

#### Drag and drop
Files, folders, or DICOM ZIP archives selected in the system file explorer can be opened by dragging and dropping them into the central area of Weasis. The accepted drop target depends on the central panel state:

* **Empty central panel** — any file a Weasis viewer can open, including standard images such as TIFF, PNG, and JPEG.
* **DICOM Explorer or any DICOM viewer** (2D, MPR, 3D, SR, AU…) — only DICOM files and DICOM ZIP archives. Weasis opens each series in the most appropriate viewer.

#### File association
DICOM files can be opened by double-clicking them from the system file explorer.

{{% notice note %}}
On Windows, only files with the `.dcm` extension are associated with Weasis. On other operating systems, DICOM files without an extension are also associated with Weasis.
{{% /notice %}}

### From the Weasis menu or toolbar

Two import entry points sit next to each other in the toolbar (and under **_File > Import_** in the main menu):

![Open toolbar](/tuto/dicom-open-icon.png?classes=shadow)

- The **first** button opens the standard DICOM import dialog described below (**_File > Import > DICOM_**).
- The **second** button is a shortcut for the DICOMDIR / CD-ROM workflow (**_File > Import > DICOM CD_**).

#### Local Device
Since {{% badge title="Version" %}}4.7.0{{% /badge %}}, DICOM ZIP is also accepted in the local-import workflow:

* **Files** — browse and select one or more DICOM files or DICOM ZIP archives via the file chooser. If a ZIP archive is password-protected, a password prompt is shown.
* **Folders** — browse and select one or more folders via the file chooser. Folders containing DICOM ZIP archives are also supported.
* **Search recursively** — when enabled, the import also descends into subdirectories.

#### DICOMDIR
Loads a DICOMDIR-based study from a CD/DVD or any folder that already contains a `DICOMDIR` index file:

* **Path** — browse to a folder containing a DICOMDIR.
* **Detect CD-ROM** — try to load a DICOM CD/DVD directly.
* **Copy images into the local temporary directory** — useful for slow reading devices such as CD-ROM drives.

#### DICOM Query/Retrieve
Queries a remote PACS and retrieves selected studies into the DICOM Explorer. The dialog has two tabs — **DICOM Source** and **Search Criteria**.

##### DICOM Source tab
![DICOM import archive](/tuto/dicom-import-archive.png?classes=shadow)
<br>

* **Archive** — pick the remote node to query:
  * **DICOM nodes** — classic DIMSE (C-FIND for the query, plus C-MOVE, C-GET, or WADO-URI for retrieval).
  * **[DICOMweb nodes](dicomweb-config)** — QIDO for the query, WADO-RS for the retrieval (no additional options needed).
* **Retrieve** (DICOM archives only) — the protocol used to transfer the images:
  * **C-MOVE** — the classic DIMSE retrieve. Accepts all SOP Classes but is not recommended over the web.
  * **C-GET** — transfer syntaxes are negotiated per SOP Class through a configuration file.
  * **WADO-URI** — C-FIND for the query plus WADO-URI retrieve; requires a WADO server.
* **Calling Node** (DICOM archives only) — pick the calling DICOM node that matches the remote AE.
* **More options** — opens the preferences so you can add or edit DICOM nodes.

##### Search Criteria tab
![Thumbnails](/tuto/dicom-import-search.png?classes=shadow&width=700px)
<br>

1. Pick a pre-registered search (combo box at the bottom-right of the **Search Criteria** panel) or fill in your own criteria. Saved criteria can be reused later; since {{% badge title="Version" %}}4.1.0{{% /badge %}}, the item selected in the combo box is re-applied automatically the next time the window opens (the default is **Empty**).
2. Adjust the **limit** — the maximum number of studies returned by the query. Set the limit to **0** to remove the cap. For DICOMweb, the limit is the page size; use the spinner buttons to move between pages.
3. Click **Search**.
4. Select the studies you want to import.
5. Click **Import** and close the window.

{{% notice note %}}
Tracking the download progress and pausing the download of a series is supported only with [DICOMweb nodes](dicomweb-config) and with the combination **DICOM C-FIND + WADO-URI**.

![Download Manager](/images/DownloadManager.jpg?width=150px)

A paused series can be resumed by clicking the green play button or via its right-click menu.
{{% /notice %}}

{{% notice tip %}}
If a query runs for too long, click **Clear** in the **Search Criteria** panel to cancel the request.

When using a DICOMweb node, an external login may be required (for instance signing in to a Google account in your web browser). If the login fails, Weasis can freeze for up to a minute waiting for the authorization code.
{{% /notice %}}

### From commands
Weasis can be started — or asked to load a specific study — through commands launched locally or remotely. See [Examples to load images](../getting-started/weasis-protocol/#examples-to-load-images) on the Weasis Protocol page.