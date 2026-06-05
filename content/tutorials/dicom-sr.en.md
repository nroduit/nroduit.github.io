---
title: DICOM SR Viewer
weight: 80
description: How to display DICOM Structured Report
keywords: [ "dicom sr", "sr", "structured report", "dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying DICOM Structured Report {{< svg-inline "static/tuto/icon/text.svg" >}} </center>

A **DICOM Structured Report (SR)** carries structured findings — measurements, observations, classifications, and references back to the images they were derived from — as a hierarchical tree of content items rather than free-form text. SRs are produced by radiology reporting systems, ultrasound machines, CAD applications, and increasingly by [AI inference frameworks](dicom-artificial-intelligence#dicom-structured-report-sr) that need to expose machine-readable results.

Weasis renders the SR tree on the right and the image referenced by the currently selected item on the left, so you can read a finding and inspect the underlying image at the same time.

Try to open sample SR files {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/sr.xml"
{{< /launch >}}

![SR Viewer](/tuto/dicom-sr.png?classes=shadow&width=100%)
<br>

### Toolbar {{% badge style="red" %}}A{{% /badge %}} {#toolbar}
Actions in the toolbar:

* {{< svg-inline "static/tuto/icon/print.svg" >}} **Print** — print the rendered SR.
* {{< svg-inline "static/tuto/icon/metadata.svg" >}} **Show DICOM metadata** — open the full [DICOM attributes](tags) of the SR object.

### Display SR Header {{% badge style="red" %}}B{{% /badge %}} {#display-sr-header}
The SR header is displayed as a three-column table summarizing the patient identification, the study context, and the report status (e.g. _Partial_, _Complete_, _Verified_, _Cancelled_).

### DICOM SR Tree {{% badge style="red" %}}C{{% /badge %}} {#dicom-sr-tree}
The content of the SR is displayed as a hierarchical tree. Each node is a content item with its own number, a **concept name** (what the item describes — e.g. _Finding Site_, _Length_, _CAD Output_) and a **value** (text, code, numeric measurement, date/time, image reference, or composite reference). The hierarchy and the inter-item links mirror the relationships defined in the SR object — typically following one of the standard DICOM templates (TIDs) used in radiology, ultrasound, or AI reporting.

Some items also carry a **link to a referenced image or region**. Clicking such a link opens the corresponding image in the [2D viewer](dicom-2d-viewer) and, when the SR contains coordinate data, draws the referenced geometry on top of it (for example, clicking the **POLYLINE** node in the screenshot above opens the source image and displays the polyline measurement at its recorded position).

Weasis renders the standard SR **graphic types** — _POINT_, _MULTIPOINT_, _POLYLINE_, _CIRCLE_, _ELLIPSE_ — and, since {{< badgeC "v4.7.0" >}}, a subset of the SR **compound graphic types** — _MULTILINE_, _RULER_, _ARROW_, _RECTANGLE_ — for richer overlays carried by the SR Compound Graphic module.