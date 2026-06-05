---
title: DICOM Attributes
weight: 300
description: How to display and compare DICOM attributes
keywords: [ "DICOM attributes", "tags", "metadata", "search attributes" ]
---

## <center>How to display DICOM attributes {{< svg-inline "static/tuto/icon/metadata.svg" >}}</center>

Every DICOM object carries a set of **attributes** (also called **tags** or metadata) that describe the patient, the study, the acquisition device, the imaging parameters, and so on. Weasis can display these attributes in two ways — a dynamic in-layout view that follows the current image, or a detached window snapshot of a single instance.

### Opening the DICOM attributes

Open the DICOM attributes either by:

* selecting the **DICOM Information** layout from the layouts dropdown {{% badge style="red" %}}A{{% /badge %}}, or
* clicking the **DICOM Information** button {{< svg-inline "static/tuto/icon/metadata.svg" >}} in the toolbar to open a detached window {{% badge style="red" %}}B{{% /badge %}}.

![Tags](/tuto/dicom-attributes.jpg?classes=shadow&width=100%)
<br>

{{% notice note %}}
The two display modes behave differently when you scroll:

- **In-layout view (A)** — the attributes are updated dynamically and reflect the currently displayed image (useful while scrolling through a series).
- **Detached window (B)** — the attributes are a snapshot of the instance that was active when the window was opened. They do **not** update when you scroll.
{{% /notice %}}

When Weasis opens certain DICOM payloads with an external application (e.g. encapsulated **PDF** or **video**), the attributes can still be inspected from the **thumbnail right-click menu**.

![Open DICOM PDF tags](/tuto/dicom-attributes-pdf.png?classes=shadow)
<br>

## How to find a specific DICOM attribute or value
The DICOM Information window has two tabs:

* **Limited DICOM attributes** — the main attributes grouped by category (a curated subset for everyday use).
* **All DICOM attributes** — every attribute present in the file. Each [data element](https://dicom.nema.org/medical/dicom/current/output/chtml/part05/chapter_7.html) is shown in four columns: **Tag ID**, **VR**, **Tag Name**, **Value**.

{{% notice note %}}
When a data element holds multiple values, they are separated by a single backslash `\`.

Data elements whose [Value Representation (VR)](https://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html) is one of **OB**, **OD**, **OL**, **OF**, **OW**, or **UN** — binary VRs used for pixel data, lookup tables, and other large byte streams — display _binary data_ in place of the actual bytes.
{{% /notice %}}

![Search DICOM tags](/tuto/dicom-attributes-search.jpg?classes=shadow)
<br>

The example above searches for the word **date**. The procedure is:

1. Switch to the **All DICOM attributes** tab so every attribute is searchable.
2. Type the search term in the search field.
3. Use the navigation arrows to jump between highlighted matches. The rightmost button **filters the list to only the matching rows** (instead of just highlighting them inside the full list).

Using {{% icon icon="filter" %}} in the toolbar applies a persistent filter on the attribute list — useful when you want to keep the focus on a specific set of attributes while scrolling through a stack of images (in-layout view {{% badge style="red" %}}A{{% /badge %}}) only).

{{% notice note %}}
Some attributes are nested inside a **sequence** element (marker (5) in the screenshot). The arrow on the left of a row shows the **nesting depth** — sequences can themselves contain sequences.
{{% /notice %}}

{{% notice tip %}}
When a value is too long to fit:

- **Resize the column** from its header — the new width is kept until the displayed image changes.
- Hover the cell to read the full value as a **tooltip** (since {{% badge title="Version" %}}4.3.0{{% /badge %}}).
{{% /notice %}}

{{% notice tip %}}
The selected DICOM attributes can be copied to the clipboard with the **standard copy shortcut** of your operating system. Paste into a spreadsheet, a text editor, or a bug report.
{{% /notice %}}