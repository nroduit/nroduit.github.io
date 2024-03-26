---
title: DICOM SR Viewer
weight: 80
description: How to display DICOM Structured Report
keywords: [ "dicom sr", "sr", " structured report", "dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying DICOM Structured Report {{< svg "static/tuto/icon/text.svg" >}} </center>

The DICOM Structured Report (SR) viewer is used to display and analyze DICOM SR data. The SR object is a structured collection of content items that represent a report of a diagnostic or therapeutic procedure. The content items are organized in a tree structure, and each item has a relationship with other items. 

The viewer displays the content of the SR object in a structured way, allowing the user to navigate through the tree and visualize the content of each item.

![SR Viewer](/tuto/dicom-sr.png?classes=shadow&width=780px)
<br>

### Toolbar {{< badge "A" >}}
Actions in the toolbar are:
* {{< svg "static/tuto/icon/print.svg" >}} Allows you to print the rendering of the SR
* {{< svg "static/tuto/icon/metadata.svg" >}} Show the DICOM metadata of the SR

### Display SR Header {{< badge "B" >}}
The header of the SR object is displayed in a table format with 3 columns containing information about the patient, the study, and the report status.

### DICOM SR Tree {{< badge "C" >}}
The content of the SR object is displayed in a tree structure. Each node in the tree represents a content item with hierarchical numbering, and the tree structure reflects the relationships between the items.

Some items can have a link to other content items, and the viewer provides a way to navigate through the tree by clicking on the links. 

This link can also open a related image which can contain measurements defined in the SR object (e.g. in the image above, clicking on _POLYLINE_ will open the image and display the polyline).
