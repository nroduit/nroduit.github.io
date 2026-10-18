---
title: "DICOM SR Viewer: Structured Reports"
weight: 80
description: "Read DICOM Structured Reports: the report header, the content tree, and the measurements and image references it carries."
linkTitle: "DICOM SR Viewer"
keywords: [ "dicom sr viewer", "structured report", "dicom sr tree", "sr measurements", "dicom report" ]
---

## <center>Findings as a coded tree, not free text {{< svg-inline "static/tuto/icon/text.svg" >}}</center>

A **DICOM Structured Report (SR)** carries structured findings — measurements, observations, classifications, and references back to the images they were derived from — as a hierarchical tree of content items rather than free-form text. SRs are produced by radiology reporting systems, ultrasound machines, CAD applications, and increasingly by [AI inference frameworks](dicom-artificial-intelligence#dicom-structured-report-sr) that need to expose machine-readable results.

Weasis renders the SR tree on the right and the image referenced by the currently selected item on the left, so you can read a finding and inspect the underlying image at the same time.

Try to open sample SR files {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/sr.xml"
{{< /launch >}}

![SR Viewer](/tuto/dicom-sr.webp?classes=shadow&width=100%)
<br>

### Toolbar {{% badge style="red" %}}A{{% /badge %}} {#toolbar}
Actions in the toolbar:

* {{< svg-inline "static/tuto/icon/print.svg" >}} **Print** — print the rendered SR.
* {{< svg-inline "static/tuto/icon/metadata.svg" >}} **Show DICOM metadata** — open the full [DICOM attributes](tags) of the SR object.

### Display SR Header {{% badge style="red" %}}B{{% /badge %}} {#display-sr-header}
The SR header is displayed as a three-column table summarizing the patient identification, the study context, and the report status (e.g. _Partial_, _Complete_, _Verified_, _Cancelled_). The status column also shows the **Preliminary Flag** when the report carries one, and a **Template** line with the identifier of the DICOM template the report follows {{< since "4.8.0" >}}.

### DICOM SR Tree {{% badge style="red" %}}C{{% /badge %}} {#dicom-sr-tree}
The content of the SR is displayed as a hierarchical tree. Each node is a content item with its own number, a **concept name** (what the item describes — e.g. _Finding Site_, _Length_, _CAD Output_) and a **value** (text, code, numeric measurement, date/time, image reference, or composite reference). The hierarchy and the inter-item links mirror the relationships defined in the SR object — typically following one of the standard DICOM templates (TIDs) used in radiology, ultrasound, or AI reporting.

A numeric value is shown with its unit (a unit of _1_, meaning "no unit", is omitted), falls back to the floating-point value when the report carries only that, and shows its qualifier — _Not a number_, _Measurement failure_… — in italics {{< since "4.8.0" >}}. An item that only refers to another item of the document reads _Content Item by reference_ with a link that jumps to that node, and a value type Weasis does not render is marked _is not supported!_ in italics.

Some items also carry a **link to a referenced image or region**. Clicking such a link opens the corresponding image in the [2D viewer](dicom-2d-viewer) and, when the SR contains coordinate data, draws the referenced geometry on top of it (for example, clicking the **POLYLINE** node in the screenshot above opens the source image and displays the polyline measurement at its recorded position).

Weasis renders the standard SR **graphic types** — _POINT_, _MULTIPOINT_, _POLYLINE_, _CIRCLE_, _ELLIPSE_ — and a subset of the SR **compound graphic types** {{< since "4.7.0" >}} — _MULTILINE_, _RULER_, _ARROW_, _RECTANGLE_ — for richer overlays carried by the SR Compound Graphic module.

### From the report to the image {#report-links}

Every content item that refers to something else is a link in the report {{< since "4.8.0" >}}. Its text says what the link opens:

* a **region** shows its graphic type — _POINT_, _POLYLINE_, _ELLIPSE_, _ELLIPSOID_… — followed, when relevant, by _(presentation optional)_, _(not for presentation)_ or _(no image reference)_; a 3D region adds _3D, n points_;
* an **image** reference reads **Show the image** — followed by _(frame n)_ for a multi-frame image and by _(with presentation state)_ when a presentation state applies to it — or **Show the segment** _(segment n)_ when it points at one segment of a [segmentation](dicom-segmentation);
* a **waveform** reference reads **Show the waveform**, with the channels it applies to; any other object reads **Open**; both are preceded by the type of the DICOM object (its SOP class name) and followed by its unique identifier (SOP instance UID) in small print;
* a **temporal coordinate** — a measurement placed in time on a waveform such as an ECG — shows its range type — _POINT_, _SEGMENT_, _MULTIPOINT_… — then its positions as samples, seconds or date-times, and opens the waveform like the reference above;
* a by-reference item whose target node is missing from the document is marked _unresolved reference_, in plain text. Clicking a link whose object is not loaded in Weasis says what is missing — _Cannot find the image!_, _Cannot find the referenced object!_ or _Cannot find the segmentation!_.

Hovering a link shows the number of the content item that holds it; a link to another node of the same document shows the number of that node.

#### Regions drawn on the images {#regions}

The regions of a report are drawn in **magenta** on their images, on a dedicated layer named after the report; that layer is locked, so the regions cannot be selected, moved or edited like your own drawings. Clicking a region in the report opens its image, draws that region **thicker** than the others and labels it with the name the report gives it — the tracking identifier of the measurement when there is one, otherwise the finding, otherwise the concept name. The emphasis moves with each click, in the same report or in another one, so only the last region you clicked stands out.

Not every region is meant to be shown: the report may mark one as optional, or as not for presentation. Those regions carry their suffix in italics and are drawn **only when you click them**; the regions the report requires for its presentation are drawn as soon as the image is shown.

A **3D region** — a _POINT_, _MULTIPOINT_, _POLYLINE_, _POLYGON_, _ELLIPSE_ or _ELLIPSOID_ given in patient coordinates rather than on one image — is drawn on every slice it crosses, in any series that shares the same **frame of reference** (the same patient coordinate space, typically series acquired together in one examination). Each slice shows the exact outline of the region at that level: an ellipsoid appears as the ellipse where it cuts the slice, whatever its tilt, and a polyline or polygon that only passes through the slice appears as the points where it crosses it. When such a region refers to no image but only to a frame of reference, clicking it opens the first series of that frame of reference at the slice closest to the region.

To hide or show the regions without closing anything, use the **DICOM SR** check box in the **Graphics** group of the [Display](dicom-2d-viewer#display) panel of the 2D viewer. The choice is kept for the images you display afterward.

<!-- SCREENSHOT TO ADD: /tuto/sr-region.webp (SR report on the left, its image on the right with magenta regions, the clicked one thicker and labeled). Insert as: ![Structured report region highlighted on its image](/tuto/sr-region.webp?classes=shadow) -->

#### Measurements on ECG waveforms {#waveforms}

A report on an electrocardiogram places its measurements in time rather than in space. Clicking **Show the waveform** opens the [ECG viewer](dicom-ecg) and draws each temporal coordinate as a **dashed marker** on the leads the report refers to. The markers carry no label: the measurements are listed in the [Annotations](dicom-ecg#annotations) panel of the ECG viewer, each with its name, its temporal range type and its positions; the list follows the reports you open and close.

<!-- SCREENSHOT TO ADD: /tuto/sr-ecg-markers.webp (ECG viewer with the dashed temporal markers of an SR and the Annotations panel). Insert as: ![Measurements of a report on an ECG](/tuto/sr-ecg-markers.webp?classes=shadow) -->

#### Tables {#tables}

A content item laid out as a **table** — a template such as a dose summary or an extensible measurement table — is rendered as a table in the report: the row and column concepts become the headers, with their units; coded cells show their meaning; qualifiers are in italics; and a cell that refers to another content item is a link to it inside the report.

<!-- SCREENSHOT TO ADD: /tuto/sr-table.webp (a TABLE content item rendered in the SR viewer, e.g. a dose summary). Insert as: ![Table rendered in a structured report](/tuto/sr-table.webp?classes=shadow) -->

#### Segments and presentation states {#segments}

**Show the segment** opens the segmentation series the report refers to in a new tab, selects that segment, makes it visible and locates it in the image, so a finding tied to a segmented structure is seen together with that structure. When an image reference carries a presentation state, that state — its window, its annotations, its shutters — is applied to the view once the image is shown, and the regions are drawn on top of it; the presentation state object must be loaded with the study, otherwise the image is shown without it.

#### Limitations {#limitations}

* Regions are drawn on the original images and on the reconstructions that share their frame of reference. On a whole-slide (digital pathology) image, however, a region is placed on the tile that contains it only when the report gives its coordinates in the volume of the slide.
* The content items of a report are shown as they are when the [identity masking](identity-masking) is on; only the header is masked.
