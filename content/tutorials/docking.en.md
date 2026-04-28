---
title: Docking
weight: 12
description: Organize the interface by docking, splitting, and pinning panels
keywords: [ "docking", "docking-framework", "panel", "split", "pin", "overlay", "tab", "central view", "tool panel", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer", "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Organizing the Interface with Docking</center>

Weasis uses the [docking-framework](https://github.com/Benoker/DockingFrames) library to offer a flexible and customizable workspace. You can rearrange the interface to suit your workflow by splitting views, relocating tool panels, or minimizing areas you do not need at the moment.

### Central View

The central area is where the viewers and players are displayed as tabs. It supports several layout operations:

#### Splitting Tabs
Tabs in the central view can be reorganized by **dragging and dropping** them:
- Drag a tab toward an edge (top, bottom, left, or right) of the central area to **split the space** and display two tabs side by side or stacked.
- Drop a tab onto another tab group to **merge** it back.

This makes it possible, for example, to compare two series simultaneously in a split-screen layout.

{{% notice tip %}}
To return to a single-tab layout, simply drag one of the split tab groups back onto the other, or close the extra view.
{{% /notice %}}

#### Maximize a Tab
A tab can be **maximized** so that it occupies the entire application window — including the space normally taken by the tool panels on the left and right. This gives the maximum viewing area for a single viewer.
- Click the **Maximize** button in the tab header (or double-click the tab) to enter full-area mode.
- Click the **Normalize** button to return to the normal split layout (or double-click the tab).

---

### Right Vertical Tool Panel

The panel on the right side of the central area contains the various tools associated with the active viewer (measurements, image adjustments, display options, etc.). Each tool panel can be managed independently with three display modes:

#### 1. Docked (inserted to the right of the central panel)
By default, tool panels are **docked** in the vertical panel to the right of the central view. In this mode they are always visible and take up a fixed portion of the screen.

#### 2. Pinned as Overlay
A tool panel can be **pinned as an overlay**: it floats on top of the central view without reducing its size. This is useful when you want the maximum viewing area while still having quick access to tools.
- Click the **pin** icon on the tool panel header to switch to overlay mode.
- The overlay panel can be repositioned by dragging its title bar.

#### 3. Minimized (vertical button)
A tool panel can be **minimized** so that it appears as a small **vertical button** on the side of the interface. Clicking the button temporarily reveals the panel without permanently occupying screen space.
- Click the **minimize** icon on the tool panel header to collapse it to a button.
- Click the button again to restore the panel.

---

### Splitting and Docking Tool Panels

Inside the right vertical panel, individual tool panels can also be **split and docked** relative to each other:
- **Drag a tool panel header** and drop it above, below, or beside another tool panel to split the tool area and display multiple tools simultaneously.
- Drop a tool panel onto another tool panel's tab bar to **group** them as tabs within the same slot.

This allows you to arrange frequently used tools exactly where you need them for a given reading workflow.

{{% notice note %}}
The docking layout is not currently saved between sessions. Panel positions and splits can depend on the displayed data as well as on the environment (screen resolution, number of screens), which makes persistent layout restoration impractical in a reliable way.
{{% /notice %}}

