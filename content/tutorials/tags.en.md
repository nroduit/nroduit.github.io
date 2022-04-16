---
title: DICOM Attributes
weight: 150
description: How to display and compare DICOM attributes
keywords: [ "DICOM attributes", "tags", "search attributes" ]
---

## How to display DICOM attributes

The DICOM attributes can be displayed either by:

* selecting the "Dicom Information" layout from the layout dropdown button (A)
* clicking on the "Dicom Information" button in the toolbar to open a detached window (B)

![Tags](/tuto/dicom-attributes.jpg?classes=shadow&width=700px)

{{% notice note %}}
Using the view in the layout (A) allows updating dynamically the DICOM attributes to the current image (e.g. scrolling into the series). The DICOM attributes won't change when opening the detached window (B).
{{% /notice %}}

When Weasis opens particular DICOM files (e.g. PDF and video) with an external viewer, the DICOM attributes can viewed from the thumbnail context menu (see image below).
![Open DICOM PDF tags](/tuto/dicom-attributes-pdf.png?classes=shadow)

## How to find a specific DICOM attribute or value

The Dicom Information window contains two tabs:

* `Limited DICOM attributes`: List of the main attributes assembled in several groups.
* `All DICOM attributes`: List of all the attributes where each [data element](https://dicom.nema.org/medical/dicom/current/output/chtml/part05/chapter_7.html) is displayed within four columns (Tag ID, VR, Tag Name and Value)

{{% notice note %}}
When the data element contains several values, each value is separated by '\\'.<br><br>
Data element with a [value representation (VR)](https://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html) OB, OD, OL, OF, OW and UN shows "binary data" as value.
{{% /notice %}}

![Search DICOM tags](/tuto/dicom-attributes-search.jpg?classes=shadow)

In the image above, we are looking for the word "date". Here are the steps:

1. Select `All DICOM attributes` tab for having all the attributes. 
2. Enter the word you are looking for.
3. Use the arrows to navigate into the highlighted results. The button on the far right allows you to limit the results to positive ones.
4. The navigation shows the current result in highlight mode.

{{% notice note %}}
Some attributes can be into a sequence element (5). Note: the left arrow shows the depth level as a sequence can contain another sequence.
{{% /notice %}}

{{% notice tip %}}
The DICOM attributes can be copied into the clipboard with the copy shortcut of your system.
{{% /notice %}}
