---
title: DICOM Explorer
weight: 30
description: Structure and display of Patients/Studies/Series
keywords: [ "dicom explorer", "patient", "study", "series", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Structure and display of Patients/Studies/Series</center>

### DICOM Explorer

The DICOM Explorer is the panel on the left side of the application. It displays everything you have loaded into Weasis as the [Patient / Study / Series / Image hierarchy](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/chapter_A.html) defined by the DICOM standard, and is the starting point for opening a viewer on any series.

Data can be added to the Explorer in [several different ways](dicom-import) — drag-and-drop, the import dialog, a PACS query, or the Weasis Protocol.

![DICOM Explorer](/tuto/dicom-explorer-level.jpg?classes=shadow&width=700px)
<br>

{{% notice tip %}}
You can navigate through the Patient / Study / Series / Image structure using only [keyboard shortcuts](../basics/shortcuts) (the bindings below are the defaults — customizable since {{< badgeC "v4.7.0" >}}). For example:
- Open an image and, if necessary, select the view to focus on. If the layout has more than one view, you can move across the views with _Tab_ and _Shift + Tab_. The view surrounded by an orange line is the focused view.
- Navigate through images within a series with _Up_ and _Down_.
- Navigate through series within a study with _Left_ and _Right_.
- Navigate through studies within a patient with _Ctrl + Left_ and _Ctrl + Right_.
- Navigate through patients with _Ctrl + Up_ and _Ctrl + Down_ (follow the order in the patient's combo box and select the last tab if a patient has several tabs already open). To navigate open tabs, use _Ctrl + Tab_ and _Ctrl + Shift + Tab_.
{{% /notice %}}

#### Patient Level
* Weasis can display several patients at the same time. By default, when images are imported, a tab with the patient's name opens in the main area.
* A tab containing a multi-view layout can only display images from a **single** patient.
* You can switch between patients either through the first combobox in the DICOM Explorer (see image above) or by selecting a tab in the main area.
* In the combobox, patients are sorted alphabetically — case-insensitive, and according to the active [regional setting](locale).
* Studies and series are grouped under the **same patient** when their _Patient Name_ and _Patient ID_ both match. Otherwise, a new patient entry is created.

#### Study Level
* A study contains one or more series (thumbnails) that belong to a single patient. A surrounding line groups the series of one study (see the image above).
* Studies are sorted in reverse chronological order by default. Since {{% badge title="Version" %}}4.1.0{{% /badge %}} the sort order can be changed in **_File > Preferences > DICOM > DICOM Explorer_** under **Study data sorting**. If a study has no study date, it is sorted alphabetically by _Study Description_.
* All studies are shown by default; the study combobox can restrict the view to a single one.

#### Series Level
![Thumbnails](/tuto/dicom-explorer-series.jpg?classes=shadow&width=700px)
<br>

* A series is represented by a thumbnail with the image count shown in the bottom-left corner.
* According to [predefined rules](https://github.com/nroduit/Weasis/blob/master/weasis-distributions/resources/series-splitting-rules.xml), some series are split into sub-series — also represented as thumbnails, identified by a `#` number in the upper-right corner. Splitting is needed for the consistency of tools such as the [MPR viewer](mpr), [MIP](mip), the [3D cursor (cross-lines)](cursor-3d) and [view synchronization](synch-view). When the split is not desired, sub-series can be [re-merged from the context menu](https://www.youtube.com/watch?v=tttP__1Sbsc).

{{% notice tip %}}
**Select related Series** — right-click a series and choose **_Select related Series_** to highlight every series in the study that shares its [Frame of Reference UID](synch-view#frame-of-reference) (the DICOM coordinate system). Open them together (right-click again → **_2D Viewer > Open_**) to get cross-coupled views that auto-synchronize and that the [3D cursor](cursor-3d) can drive.
{{% /notice %}}

#### 4D Series Sub-Series Splitting {#4d-splitting}

When a DICOM series is loaded, Weasis automatically analyzes it to detect multi-phase acquisitions (e.g. cardiac phases, contrast phases, 4D volumes). If multiple phases are detected, the series is split — automatically or with a confirmation step — into separate sub-series, one per phase. Each sub-series can then be used independently in the [MPR](mpr), [MIP](mip), or [3D Volume Renderer](dicom-3d-viewer).

##### Splitting behavior by number of detected phases

| Phases    | Behavior |
|-----------|----------|
| **1**     | No split — treated as a standard single-phase series. |
| **2 – 7** | **Automatic split** — the series is immediately divided into one sub-series per phase, without any user interaction. |
| **≥ 8**   | **Manual split** — Weasis stores the phase count but leaves the series intact. A confirmation dialog is shown before splitting to prevent unintended fragmentation of large datasets. |


##### Manual split confirmation dialog (≥ 8 phases)

When 8 or more phases are detected, a dialog asks you to confirm the split. Once confirmed, the series is divided exactly as in the automatic case. Canceling leaves the series intact as a single entry in the DICOM Explorer.

##### Sub-series structure after splitting

After splitting, each phase becomes a separate thumbnail in the DICOM Explorer. The first sub-series reuses the original series entry; the additional sub-series are added to the study tree, identified by a `#` number in the upper-right corner of the thumbnail.

{{% notice tip %}}
Open any individual phase sub-series in the [MPR](mpr), [MIP](mip), or [3D viewer](dicom-3d-viewer) for accurate volumetric analysis — each sub-series contains only the images of a single phase and can be reconstructed as a coherent 3D volume.
{{% /notice %}}

If the split is not needed, or was triggered unintentionally, the sub-series can be merged back. Select the thumbnails you want to merge (all or a subset) and choose **_Merge Selected Series_** from the context menu — the selected sub-series are recombined into a single series entry.

{{% notice note %}}
Phase detection is based on the spatial position of each image. If multiple images share the same slice position, they are assumed to belong to different temporal phases. If no such overlap is found, the series is treated as a standard single-phase acquisition and is never split.
{{% /notice %}}

#### Series Display and Opening

* By default, series are sorted by series number; if that is missing, they are sorted chronologically by series date or another available date.
* To open a series:
  * **Drag and drop** a thumbnail into the main area. If the drop lands in a view of the same patient, that view's series is replaced; otherwise, a new tab is created.
  * **Double-click** a thumbnail (or navigate with the **Up / Down** arrows and press **Return**). If a view of the same patient already exists, the series in the focused view (orange border) is replaced.
  * Select one or more thumbnails and pick an action from the **2D DICOM Viewer** context menu:
    * **Open** — opens the series in the most appropriate layout (replaces the series if a patient tab already exists).
    * **Open in new tab** — same, but always in a new tab.
    * **Open in screen** — same, but on a specific screen.
    * **Add** — appends the series to the current patient's layout, if one exists.

{{% notice note %}}
Since {{% badge title="Version" %}}4.7.0{{% /badge %}}, tab opening and focus behavior is handled automatically, replacing the old configurable _opening mode_ preference.

**When is a new tab opened?**
A new viewer tab is opened for every patient whose studies are loaded via an import action. If the patient already has an open tab, the new studies are added to that existing tab instead of opening a new one. This keeps each patient organized in a single tab and prevents fragmentation of the workspace.

**How is focus managed?**
Focus follows an automatic policy based on loading duration:
- If the study finishes loading **quickly** (within ~3 seconds), the new tab comes to the **foreground** — the expected behavior for a direct open action.
- If the study is still loading when the threshold is exceeded (for example a slow network import in the background), the **current tab keeps focus** — Weasis will not interrupt your work by stealing focus for a slow background load.

In practice: fast loads surface immediately, slow background loads stay out of the way.
{{% /notice %}}

#### Preferences
From the main menu **_File > Preferences > DICOM > DICOM Explorer_**:

* **Thumbnail size** — width of the thumbnails; the panel adjusts accordingly. Default: 144. Restart the application after changing this value.
* **Study data sorting** — sorts studies in reverse chronological order (default) or chronological order. Since {{% badge title="Version" %}}4.1.0{{% /badge %}}.
* **Download all series immediately** — when checked, series start downloading as soon as they are queued via [WADO or WADO-RS](../basics/customize/integration/). When unchecked, you must click the play button on each series, or the global play button at the bottom of the thumbnail list. Default: checked.