---
title: Print
weight: 350
description: How to print images
keywords: [ "print", "view", "dicom viewer" ]
---


## <center>Build the image selection to print {{< svg-inline "static/tuto/icon/print.svg" >}}</center>

The image selection to print must be prepared before calling the print function. If you need to print more than one image per page, choose a layout from the dropdown button in the toolbar (1).

{{% notice note %}}
The layout list is built dynamically according to the window size. So changing the window size ratio will provide other layouts. For instance, with a panoramic screen, you can choose a horizontal layout and then print with a landscape orientation.
{{% /notice %}}

![Print Layout](/tuto/print/layout.jpg?height=400&classes=shadow)

To fill the layout with images you can change the synchronized mode of series (2):

* with *Default Tile* selected, all the views will be filled with the same series. Each view has a new image of the series stack (n + 1).
* with *Default Stack* selected, drag and drop a series into each view and select independently which image you want to display.

## Select a print mode

### Standard Printer {{< svg-inline "static/tuto/icon/print.svg" >}} {#standard-printer}
From the main menu, open _File > Print > Print 2D viewer layout (P)_.

![standard](/tuto/print/standard.png?classes=shadow)

The meaning of the standard print parameters:

* *Image position:* the position of the image in the print area.
* *Image DPI:* the print resolution in dot per inch (Default value is 150). Higher DPI means higher resolution.
* *Print image with annotations:* Allows to print the annotations defined in the [Display]() panel.
* *Print only the selected view:* When this option is checked, only the selected view is printed (view with an orange border). Otherwise, all the views of the layout are printed.


### DICOM Print
From the main menu, open _File > Print > DICOM Print_.

In the DICOM Print dialog, you can manage several configurations. For the options meaning, you can refer to the above parameters and <a target="_blank" href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.13.3.html">the DICOM print pages</a>.

![DICOM](/tuto/print/dicom.png?classes=shadow)
<br>
{{% notice note %}}
The DICOM printer configurations can be distributed at the server side for all the clients, see [preferences](../../basics/customize/preferences/#how-to-add-dicom-nodes-or-dicom-printers-at-the-server-side).
{{% /notice %}}
