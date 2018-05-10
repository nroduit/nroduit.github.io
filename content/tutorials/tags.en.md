---
title: DICOM Attributes
weight: 90
description: How to display and compare DICOM attributes
keywords: [ "DICOM attributes", "tags", "search attributes" ]
---

## How to display DICOM attributes

The DICOM attributes can be displayed either by:

* selecting the "Dicom Information" layout from the layout dropdown button (A)
* clicking on the "Dicom Information" button in the toolbar to open a detached window (B)

![Tags](/tuto/tags/dicom-tags.png?height=400)

{{% notice note %}}
Using the view in the layout (A) allows updating dynamically the DICOM attributes to the current image (e.g. scrolling into the series). The DICOM attributes won't change when opening the detached window (B).
{{% /notice %}}

When Weasis opens particular DICOM files (e.g. PDF and video) with an external viewer, the DICOM attributes can viewed from the thumbnail context menu (see image below).
![Open](/tuto/tags/open-pdf.png)

## How to find a specific DICOM attribute or value

The Dicom Information window contains two tabs:

* `Limited DICOM attributes`: List of the main attributes assembled in several groups.
* `All DICOM attributes`: List of all the attributes where each <a target="_blank" href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/chapter_7.html">data element</a> is displayed with the following pattern:<BR> (Tag) [VR] TagName: **value**

{{% notice note %}}
When the data element contains several values, each value is separated by '\'.<br><br>
Data element with a value representation (<a target="_blank" href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html">VR</a>) OB, OD, OL, OF, OW and UN shows "binary data" as value.
{{% /notice %}}

![Search](/tuto/tags/dicom-search.png?height=500)

In the image above, we are looking for the word "image". Here are the steps:

1. Select `All DICOM attributes` tab for having all the attributes.
1. Enter the word you are looking for.
1. Use the arrows to navigate into the highlighted results.
1. The navigation shows the current result in orange. Note: this data element has several values.
1. The second result here is a sequence element. Note: the left arrow shows the depth level as a sequence can contain another sequence.

{{% notice tip %}}
The DICOM attributes can be copied into the clipboard with the copy shortcut of your system.
{{% /notice %}}
