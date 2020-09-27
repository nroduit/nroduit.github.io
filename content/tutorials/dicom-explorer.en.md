---
title: DICOM Explorer
weight: 20
description: Structure and display of Patients/Studies/Series
keywords: [ "dicom explorer", "patient", "study", "series", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Structure and display of Patients/Studies/Series</center>

### DICOM Explorer

The DICOM Explorer is the panel on the left that displays the [Patient/Study/Series representation](http://dicom.nema.org/medical/dicom/current/output/chtml/part03/chapter_A.html) defined in the DICOM standard.

The data displayed in the DICOM Explorer can be imported locally (from the Import/Open menu or by drag and drop) or [remotely](../../basics/customize/integration).

![DICOM EXplorer](/tuto/explorer/structure.png)

#### Patient Level

* Weasis allows multi-patient display. By default, when images are imported a tab with the patient's name opens in the main area.
* A tab containing a multi-view layout can only display images from a single patient.
* Changing patients can be done either through the first combobox in the DICOM Explorer (see image above) or by selecting a tab in the main area.
* In the combobox the patients are sorted in alphabetical order regardless of case and according to the [regional setting](../locale).
* Studies and Series are displayed within the same patient when the metadata Patient Name and Patient ID are the same. Otherwise new patients are displayed.

#### Study Level

* An study contains one or more series (thumbnails) belonging to a patient. A line representing the study surrounds its series (see image above).
* The studies are sorted by reverse chronology (most recent first). If there is no study date then the studies are sorted alphabetically according to the Study Description.
* By default all the studies are displayed, however you can choose to display only one of them from the study combobox.

#### Series Level

![Thumbnails](/tuto/explorer/thumbnail.png)

* A series is represented by a thumbnail that contains a certain number of images (number displayed at the bottom left).
* According to [predefined rules](https://github.com/nroduit/Weasis/blob/master/weasis-distributions/resources/series-splitting-rules.xml), some series are separated into sub-series also represented by a thumbnail with a number preceded by '#' in the upper right corner. Series splitting is necessary for the consistency of some tools such as the MPR, cross-lines and synchronization of series.
* The sorting of the series is done by the serial number and if this last one is not present then in a chronological way by the date of the series or other dates.
* To open new series:
  * Drag and drop a thumbnail in the main area (if the series is dropped in a view of the same patient then the series is replaced otherwise a new tab is created).
  * Double click or press return on an selected thumbnail (if a view of the same patient exists then the series in the view surrounded by an orange line is replaced)
  * Select one or more thumbnails and choose an action from the "2D DICOM Viewer" context menu:
    * Open: Opens the series in the most appropriate layout (replaces the series if the patient's tab already exists)
    * Open in new tab: Opens the series in the most appropriate layout in a new tab.
    * Open in screen: Opens the series in the most appropriate layout in a specific screen.
    * Add: Adds the series to the current patient's layout if exists.
