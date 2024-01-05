---
title: DICOM Explorer
weight: 30
description: Structure and display of Patients/Studies/Series
keywords: [ "dicom explorer", "patient", "study", "series", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Structure and display of Patients/Studies/Series</center>

### DICOM Explorer

The DICOM Explorer is the panel on the left that displays the [Patient/Study/Series representation](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/chapter_A.html) defined in the DICOM standard.

The data displayed in the DICOM Explorer can be [imported form different ways](../dicom-import).

![DICOM EXplorer](/tuto/dicom-explorer-level.jpg?classes=shadow&width=700px)
<br>

{{% notice tip %}}
You can navigate through the Patient/Study/Series/Image structure using only [keyboard shortcuts](../../basics/shortcuts). For example:
- Open an image and, if necessary, select the view to focus on. If the layout has more than one view, you can move across the views with _Tab_ and _Shift + Tab_. The view surrounded by an orange line is the focused view.
- Navigate through images within a series with _Up_ and _Down_
- Navigate through series within a study with _Left_ and _Right_
- Navigate through studies within a patient with _Ctrl + Left_ and _Ctrl + Right_
- Navigate through patients with _Ctrl + Up_ and _Ctrl + Down_ (follow the order in the patient's combo box and select the last tab if a patient has several tabs already open). To navigate open tabs, use _Ctrl + Tab_ and _Ctrl + Shift + Tab_.
{{% /notice %}}

#### Patient Level
* Weasis allows multi-patient display. By default, when images are imported a tab with the patient's name opens in the main area.
* A tab containing a multi-view layout can only display images from a single patient.
* Changing patients can be done either through the first combobox in the DICOM Explorer (see image above) or by selecting a tab in the main area.
* In the combobox the patients are sorted in alphabetical order regardless of case and according to the [regional setting](../locale).
* Studies and Series are displayed within the same patient when the metadata Patient Name and Patient ID are the same. Otherwise, new patients are displayed.

#### Study Level
* A study contains one or more series (thumbnails) belonging to a patient. A line representing the study surrounds its series (see image above).
* By default, the studies are sorted by reverse chronology order (since {{< badge "v4.1.0" >}} "_Study data sorting_" can be changed in the menu "_File > Preferences > DICOM > DICOM Explorer_"). If there is no study date then the studies are sorted alphabetically according to the Study Description.
* By default, all the studies are displayed, however you can choose to display only one of them from the study combobox.

#### Series Level
![Thumbnails](/tuto/dicom-explorer-series.jpg?classes=shadow&width=700px)
<br>
* A series is represented by a thumbnail that contains a certain number of images (number displayed at the bottom left).
* According to [predefined rules](https://github.com/nroduit/Weasis/blob/master/weasis-distributions/resources/series-splitting-rules.xml), some series are separated into sub-series also represented by a thumbnail with a number preceded by '#' in the upper right corner. Series splitting is necessary for the consistency of some tools such as the MPR, cross-lines and synchronization of series. However, sometimes separation is not desired, and sub-series can be [re-merged using the context menu](https://www.youtube.com/watch?v=tttP__1Sbsc).
* The sorting of the series is done by the serial number and if this last one is not present then in a chronological way by the date of the series or other dates.
* To open new series:
  * Drag and drop a thumbnail in the main area (if the series is dropped in a view of the same patient then the series is replaced otherwise a new tab is created).
  * Double click or navigate with the `up/down arrow` key and press `return` on a selected thumbnail (if a view of the same patient exists then the series in the view surrounded by an orange line is replaced)
  * Select one or more thumbnails and choose an action from the "2D DICOM Viewer" context menu:
    * Open: Opens the series in the most appropriate layout (replaces the series if the patient's tab already exists)
    * Open in new tab: Opens the series in the most appropriate layout in a new tab.
    * Open in screen: Opens the series in the most appropriate layout in a specific screen.
    * Add: Adds the series to the current patient's layout if exists.

#### Preferences
From the main menu "_File > Preferences > DICOM > DICOM Explorer_":

* _Thumbnail size:_ defines the width of the thumbnails and adjusts the panel accordingly (Default: 144). It is recommended to restart the application after this change.
* _Study data sorting:_ allows sorting the studies by chronological order or inversely chronological (Default: reverse chronology order). Since {{< badge "v4.1.0" >}}.
* _Open in new tab:_ behavior to automatically open the images of a patient when [using WADO or WADO-RS](../../basics/customize/integration/) (Default: All the patients)
* _Download all series immediately:_ allows starting the download of the series immediately when [using WADO or WADO-RS](../../basics/customize/integration/) (Default: true). If unchecked then you must click on the play button on each series or globally at the bottom of the thumbnail list.