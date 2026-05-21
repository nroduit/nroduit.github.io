---
title: Docking
weight: 12
description: Organize the interface by docking, splitting, and pinning panels
keywords: [ "docking", "docking-framework", "panel", "split", "pin", "overlay", "tab", "central view", "tool panel", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer", "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Organizing the Interface with Docking</center>

Almost every panel and viewer tab in Weasis can be **moved, split, pinned, or hidden** by dragging it with the mouse. This lets you arrange the workspace around the task at hand — for instance comparing two series side by side, putting the [MPR viewer](mpr) and the [3D Volume Renderer](dicom-3d-viewer) next to each other for [crosshair-driven volume cutting](dicom-3d-viewer#mpr-cut), or maximizing a single view for a focused read — without leaving the application.

### Central View

The central area is where viewers and players are displayed as tabs. It supports two main layout operations.

#### Splitting tabs
Reorganize tabs by **dragging and dropping** them:

- Drag a tab toward an **edge** (top, bottom, left, or right) of the central area to **split the space** and display two tabs side by side or stacked.
- Drop a tab onto another tab group to **merge** it back into a single area.

This makes it possible, for example, to compare two series simultaneously in a split-screen layout, or to keep an MPR tab next to a 3D rendering of the same volume.

{{% notice tip %}}
To return to a single-tab layout, drag one of the split tab groups back onto the other, or close the extra view.
{{% /notice %}}

#### Maximize a tab
A tab can be **maximized** to occupy the entire application window, including the space normally taken by the tool panels on either side — giving the largest possible viewing area for a single viewer.

- **Maximize** — click the maximize button in the tab header, or double-click the tab.
- **Restore** — click the normalize button, or double-click the tab again.

---

### Tool Panels

The strips on the right side of the central area host the tools attached to the active viewer (measurements, image adjustments, display options, segmentation, …). Each tool panel can be managed independently with one of three display modes.

#### Docked
The default mode: the tool panel is **docked** in the vertical strip next to the central view. In this mode it is always visible and takes up a fixed portion of the screen.

#### Pinned as overlay
The tool panel **floats on top** of the central view without reducing the viewer's size. Useful when you want the maximum viewing area while keeping quick access to the tools.

- Click the **pin** icon in the tool panel header to switch to overlay mode.
- The overlay can be repositioned by dragging its title bar.

#### Minimized (vertical button)
The tool panel collapses to a small **vertical button** on the side of the interface. Clicking the button temporarily reveals the panel without permanently giving up screen space.

- Click the **minimize** icon in the tool panel header to collapse it to a button.
- Click the button again to restore the panel.

#### Rearranging tool panels
Inside the vertical strip, individual tool panels can be **split and re-docked** relative to each other:

- **Drag a tool panel header** and drop it above, below, or beside another tool panel to split the tool area and display several tools at once.
- Drop a tool panel onto another tool panel's tab bar to **group** them as tabs within the same slot.

This lets you arrange the most-used tools exactly where you want them for a given reading workflow.

{{% notice note %}}
The docking layout is **not currently saved between sessions**. Panel positions and splits can depend on the displayed data and on the environment (screen resolution, number of screens), which makes reliable persistent restoration impractical for now.
{{% /notice %}}