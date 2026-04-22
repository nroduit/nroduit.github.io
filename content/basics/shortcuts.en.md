---
title: Shortcuts
description: Keyboard and Mouse Shortcuts of Weasis
keywords: [ "shortcuts", "weasis shortcuts", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 20
---

## <center>Keyboard and Mouse Shortcuts</center>

Here is a list of the default keyboard and mouse shortcuts in Weasis. The shortcuts are divided into different categories for better understanding.

{{% notice note %}}
Since {{< badgeC "v4.7.0" >}}, most keyboard shortcuts can be customized in **Preferences > General > Keyboard Shortcuts**. This page documents the **default** configuration. To get the current configuration (including any customizations), use **Help > Keyboard Shortcuts** (this page is internationalized).
{{% /notice %}}

### Central panel containing viewers and editors

| Shortcut               | Action                                                                  |
|------------------------|-------------------------------------------------------------------------|
| **Ctrl + Tab**         | Select the next tab                     |
| **Ctrl + Shift + Tab** | Select the previous tab                 |
| **Ctrl + Shift + E**   | Open the docking panel list for selection                               |
| **Ctrl + M**           | Maximize/Restore the selected tab                                       |
| **Ctrl + W**           | Close the tab                                                           |
| **Ctrl + E**           | Externalize the tab (since {{< badgeC "v4.7.0" >}})                     |
| **Ctrl + N**           | Normalize the tab (since {{< badgeC "v4.7.0" >}})                       |
| Tab **Right-click**    | Open the contextual menu for more options (Close Others, All, Maximize) |

### Selected view in the 2D DICOM Viewer

| Shortcut                                                 | Action                                                                                                                                                                 |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Left Arrow**                                           | Display previous series                                                                                                                                                |
| **Right Arrow**                                          | Display next series                                                                                                                                                    |
| **Page Up**                                              | Display first series                                                                                                                                                   |
| **Page Down**                                            | Display last series                                                                                                                                                    |
| **Ctrl + Left Arrow**                                    | Display previous study                                                                                                                                                 |
| **Ctrl + Right Arrow**                                   | Display next study                                                                                                                                                     |
| **Ctrl + Page Up**                                       | Display first study                                                                                                                                                    |
| **Ctrl + Page Down**                                     | Display last study                                                                                                                                                     |
| **Up Arrow**                                             | Display previous image                                                                                                                                                 |
| **Down Arrow**                                           | Display next image                                                                                                                                                     |
| **Home**                                                 | Display first image                                                                                                                                                    |
| **End**                                                  | Display last image                                                                                                                                                     |
| **Shift + Up Arrow**                                     | Go 10 images back                                                                                                                                                      |
| **Shift + Down Arrow**                                   | Go 10 images forward                                                                                                                                                   |
| **Ctrl + Up Arrow**                                      | Display previous patient                                                                                                                                               |
| **Ctrl + Down Arrow**                                    | Display next patient                                                                                                                                                   |
| **Ctrl + Home**                                          | Display first patient                                                                                                                                                  |
| **Ctrl + End**                                           | Display last patient                                                                                                                                                   |
| **Tab**                                                  | Go to the next view when layout has more than one view                                                                                                                 |
| **Shift + Tab**                                          | Go to the previous view when layout has more than one view                                                                                                             |
| **Alt + Up Arrow**                                       | Move image up 5 pixels (with Pan action)                                                                                                                               |
| **Alt + Down Arrow**                                     | Move image down 5 pixels (with Pan action)                                                                                                                                                |
| **Alt + Left Arrow**                                     | Move image left 5 pixels (with Pan action)                                                                                                                                                |
| **Alt + Right Arrow**                                    | Move image right 5 pixels (with Pan action)                                                                                                                                               |
| **Alt + Shift + Up Arrow**                               | Move image up 10 pixels (since {{< badgeC "v4.7.0" >}}) (with Pan action)                                                                                                                 |
| **Alt + Shift + Down Arrow**                             | Move image down 10 pixels (since {{< badgeC "v4.7.0" >}}) (with Pan action)                                                                                                               |
| **Alt + Shift + Left Arrow**                             | Move image left 10 pixels (since {{< badgeC "v4.7.0" >}}) (with Pan action)                                                                                                                |
| **Alt + Shift + Right Arrow**                            | Move image right 10 pixels (since {{< badgeC "v4.7.0" >}}) (with Pan action)                                                                                                               |
| **Ctrl + NumPad +**                                      | Zoom in                                                                                                                                                                |
| **Ctrl + NumPad -**                                      | Zoom out                                                                                                                                                               |
| **Ctrl + Enter**                                         | Set zoom to best fit                                                                                                                                                   |
| **T**                                                    | Translate (pan) the image canvas                                                                                                                                       |
| **W**                                                    | Window / Level                                                                                                                                                         |
| **S**                                                    | Series scroll                                                                                                                                                          |
| **Z**                                                    | Zoom                                                                                                                                                                   |
| **R**                                                    | Rotation                                                                                                                                                               |
| **H**                                                    | Crosshair: in multiview mode synchronizes the crosshair position to all the views (Note: Ctrl + click or Ctrl + Shift + click allows changing the Window/Level values) |
| **C**                                                    | Cine Start / Stop                                                                                                                                                      |
| **M**                                                    | Measure                                                                                                                                                                |
| **D**                                                    | Distance measurement                                                                                                                                                   |
| **A**                                                    | Angle measurement                                                                                                                                                      |
| **Y**                                                    | Polyline measurement                                                                                                                                                   |
| **G**                                                    | Draw (since {{< badgeC "v4.7.0" >}})                                                                                                                                   |
| **B**                                                    | Textbox                                                                                                                                                                |
| **N**                                                    | No Action (since {{< badgeC "v4.7.0" >}})                                                                                                                              |
| **Q**                                                    | Context menu                                                                                                                                                           |
| **Ctrl + Spacebar**                                      | Change to the next action                                                                                                                                              |
| **Ctrl + mouse drag**                                    | Accelerate the current action                                                                                                                                          |
| **Ctrl + Shift + mouse drag**                            | Accelerate more the current action                                                                                                                                     |
| **Alt + R**                                              | 90° rotation (clockwise)                                                                                                                                               |
| **Alt + L**                                              | 90° rotation (counterclockwise)                                                                                                                                        |
| **Alt + F**                                              | Flip horizontally (after rotation action)                                                                                                                              |
| **0 1 2 3**...                                           | DICOM presets                                                                                                                                                          |
| **K**                                                    | Toggle key image state                                                                                                                                                 |
| **Spacebar**                                             | Show/Hide all the annotations (three states)                                                                                                                           |
| **I**                                                    | Show/Hide all the annotations (three states)                                                                                                                           |
| **Escape**                                               | Reset the selected view                                                                                                                                                |
| **P**                                                    | Print view(s) with the operating system printer                                                                                                                        |
| **Right-click**                                          | Open the contextual menu for more options                                                                                                                              |
| **Double click**  or **F11**                             | Toggle fullscreen (F11 since {{< badgeC "v4.5.2" >}})                                                                                                                  |
| **Left mouse drag**                                      | Perform the selected left mouse action (default: Window/Level)                                                                                                         |
| **Middle mouse drag**                                    | Perform the selected middle mouse action (default: Pan)                                                                                                                |
| **Mouse scroll**                                         | Perform the selected scroll action (default: Series scroll)                                                                                                            |
| **Drag files/directories**<br>(from the OS file manager) | Open DICOMs files                                                                                                                                                      |

### Selected view in the MPR Viewer
MPR view inherits the same shortcuts as the 2D viewer, with the following additional shortcuts since {{< badgeC "v4.6.0" >}} :

| Shortcut               | Action                                                |
|------------------------|-------------------------------------------------------|
| **Alt + X**            | Center crosshair of the selected view                 |
| **Alt + C**            | Show/Hide the crosshair center of the selected view   |
| **Alt + V**            | Show/Hide the crosshair of the selected view          |
| **Ctrl + Alt + X**     | Center crosshair of all views                         |
| **Ctrl + Alt + C**     | Show/Hide the crosshair center of all views           |
| **Ctrl + Alt + V**     | Show/Hide the crosshair of all views                  |
| **Ctrl + Alt + B**     | Change the MIP type (None/Min/Mean/Max)               |
| **Alt + mouse scroll** | On selected axis, increase/decrease the MIP thickness |

### DICOM explorer 

| Shortcut                                                           | Action                                         |
|--------------------------------------------------------------------|------------------------------------------------|
| **Ctrl + click on the thumbnail**                                  | Select multiple series                         |
| **Click on a thumbnail** and then **Shift + click on another one** | Select all series between                      |
| **Ctrl + A**                                                       | Select all the series                          |
| **Home** or **Page Up**                                            | Select the first series                        |
| **End** or **Page Down**                                           | Select the last series                         |
| **Up Arrow**                                                       | Select previous series                         |
| **Down Arrow**                                                     | Select next series                             |
| **Enter**                                                          | Open the selected series in the default viewer |
| **Click + drag a thumbnail** in the main view                      | Display a series                               |
| **Right-click**                                                    | Open the contextual menu for more options      |
| **Drag files/directories**<br>(from the OS file manager)           | Open DICOMs files                              |

{{% notice note %}}
**Downloading Priorities**: Selecting a thumbnail gives the best priority to download.
{{% /notice %}}


### Graphics

| Shortcut                       | Action                                                                                                                                                                |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Click on a graphic**         | Select a Graphics                                                                                                                                                     |
| **Click + mouse drag**         | In selection mode: select all the graphics inside the selection area.<br /> In drawing mode: draw the selected graphic shape.                                         |
| **Ctrl + A**                   | Select all the graphics                                                                                                                                               |
| **Ctrl + D**                   | Deselect all the graphics                                                                                                                                             |
| **Delete**                     | Delete the selected graphics                                                                                                                                          |
| **Shift + click on a graphic** | In selection mode: add or remove a graphic to the current selection.<br /> In drawing mode: force to draw on another graphic (without shift the graphic is selected). |
| **Double click**               | Stop adding points for polyline (also available in the context menu)                                                                                                  |
| **Right-click**                | Open the contextual menu for more options                                                                                                                             |


### Tips and Tricks

#### Window / Level Adjustment
- Move the mouse **horizontally to the right** to increase the window width (reduce the perceived contrast).
- Move the mouse **vertically upwards** to lower the window center (increase the perceived brightness).<br>
Tip: Use [Preferences](customize/preferences)  to reverse the direction of level adjustments.


#### Drawing a Segment
You can draw a segment in two ways:<br>
1. **Click + Drag**: Click, drag to draw, then release.
2. **Click > Release > Drag**: Click to start, release, drag to draw, and release again.
