---
title: View Synchronization
weight: 45
description: How to synchronize views manually or automatically
keywords: [ "synchronization", "synch", "stack", "tile", "frame of reference", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Synchronizing Views {{< svg-inline "static/tuto/icon/synch.svg" >}}</center>

View synchronization lets you apply the same image settings (window/level, zoom, scrolling position) across multiple views simultaneously. Weasis provides several synchronization modes that can be selected manually as well as an automatic mode that activates itself based on shared DICOM geometry — specifically the **Frame of Reference UID** (DICOM tag 0020,0052), abbreviated **FoR** throughout this page.

---

### Synchronization Modes

The synchronization mode is controlled by the drop-down button {{< svg-inline "static/tuto/icon/synch.svg" >}} located to the right of the layout button {{< svg-inline "static/tuto/icon/layout.svg" >}} in the toolbar.

| Mode | Description |
|------|-------------|
| **Default Stack** | Synchronizes views across series that share the same **Frame of Reference UID** (0020,0052). By default only *Scroll* is propagated; every other per-action toggle (Pan, Zoom, W/L, Rotation, Flip, …) starts disabled and the user opts them in explicitly. This is the default mode. |
| **Default Tile** | Displays consecutive images of the **same series** in a mosaic layout (n, n+1, n+2, …). By default **every per-action setting is propagated** between tiles — the seven user-toggleable actions (Scroll, Pan, Zoom, Rotation, Flip, Window/Level, Spatial unit) plus the always-on settings (Preset, LUT, LUT shape, Invert LUT, Filter, Inverse stack, Sort stack) — so the whole tile group behaves as a single coherent display. |

The drop-down popup also contains a master **Synchronize** checkbox that turns synchronization on or off globally for the container — uncheck it to make every view fully independent without changing the active mode. Below the checkbox, per-action toggles (*Scroll*, *Pan*, *Zoom*, *Rotation*, *Flip*, *Window/Level*, *Spatial unit*) mirror the **selected view**'s configuration. An **Apply to all views** entry — decorated with the selected view's FoR color chip — propagates that configuration to every other sync-active view in the container, regardless of FoR (this is broader than the same-named entry in the per-view popup, which is restricted to the selected view's FoR group). See [Per-view sync controls](#per-view-sync) for the per-action semantics and the chip system.

{{% notice note %}}
The synchronization mode can also be set programmatically with the command:
```
dcmview2d:synch VALUE
```
where `VALUE` is `Stack` or `Tile`. See [Commands](../basics/commands/#dcmview2d-synch) for details.
{{% /notice %}}

---

### Default Stack Mode (Auto Synchronization) {#stack-mode}

**Default Stack** is the most common synchronization mode. When two or more series share the same **Frame of Reference UID** (DICOM tag 0020,0052), they share the same 3D coordinate system, and Weasis can synchronize their views automatically.

By default, **only Scroll** is propagated — navigating to a slice in one view moves the other views to the closest matching anatomical position. Every other action (*Pan*, *Zoom*, *Rotation*, *Flip*, *Window/Level*, *Spatial unit*) starts disabled, and you opt them in explicitly through the per-action toggles in either:

- the **toolbar drop-down popup** (applies to the selected view; use **Apply to all views** to propagate the change to its FoR group), or
- the **per-view auto-sync popup** opened from the {{< svg-inline "static/tuto/icon/synch.svg" >}} button on the view itself.

See [Per-view sync controls](#per-view-sync) for the full list of toggles and the FoR color-chip system.

**Typical use case:** Display a CT series and its corresponding PET series side by side. Because both series share the same Frame of Reference UID, scrolling through slices in the CT view will automatically scroll the PET view to the matching anatomical level. If you also want *Window/Level* or *Zoom* to follow the active view, enable those actions on **every** view you want coupled — toggle them on one view and use **Apply to all views**, since an action is synced only between views that both have it enabled.

{{% notice tip %}}
To find which series share the same frame of reference, right-click a thumbnail in the [DICOM explorer](dicom-explorer/) and choose **Select related Series**. Then open all selected series together in the 2D viewer.
{{% /notice %}}

---

### Per-view Sync Controls {#per-view-sync}

Beyond the global toolbar drop-down, each 2D view carries small overlay buttons that drive its sync behaviour independently. They appear in the bottom-right corner of the view when the view is eligible for synchronization with one of its peers.

#### Auto-sync button {{< svg-inline "static/tuto/icon/synch.svg" >}} {#auto-sync-button}

The {{< svg-inline "static/tuto/icon/synch.svg" >}} button toggles **Default Stack** auto-synchronization for *this* view only. Its appearance encodes two pieces of information:

- **Outer tint** — *red* when auto-sync is OFF for the view, *green* when ON.
- **Center color chip** — a small colored square shown when the current container holds **two or more views with different Frame of Reference UIDs**. The color identifies the FoR group; views sharing the same UID share the same chip color, so groupings are visible at a glance. When the container has only one FoR (nothing to disambiguate), the chip is hidden.

Clicking the button opens a per-view sync popup with:

- **Synchronize this view** — master on/off toggle for auto-sync on this view (closes the popup on click).
- **Per-action toggles** — independent checkboxes for *Scroll*, *Pan*, *Zoom*, *Rotation*, *Flip*, *Window/Level* and *Spatial unit*. The popup stays open while you flip several options, so you can configure the whole set in one pass.
- **Apply to all views** — copies this view's effective sync options to every other view sharing the same Frame of Reference UID. The item is decorated with the view's FoR color chip, matching the chip drawn on the auto-sync button so you can confirm at a glance which group will be affected.
- **Close** — explicit dismiss (the per-action toggles do not auto-close on click; *Esc* and clicks outside also dismiss the popup as usual).

{{% notice note %}}
A per-action toggle only declares whether **this** view takes part in syncing that action. An action is propagated between two views **only when both of them have it enabled** — sharing the same Frame of Reference UID is not enough on its own. Enabling *Zoom* on a single view therefore has no visible effect until at least one peer also has *Zoom* enabled. To couple an action across a whole FoR group in one step, enable it on one view and use **Apply to all views**.
{{% /notice %}}

#### Manual sync button {{< svg-inline "static/tuto/icon/hand.svg" >}} {#manual-sync-button}

Some series cannot be auto-synced because they have no — or a different — Frame of Reference UID (typical for unrelated CT scans, or legacy series with missing DICOM geometry). The **manual-sync button** {{< svg-inline "static/tuto/icon/hand.svg" >}} (shown in the same bottom-right corner) lets you link such a view to a peer by relative slice index.

A view is an **eligible candidate** for manual sync with the current view when it has the **same orientation** and a **different (or absent) FoR**. Clicking the {{< svg-inline "static/tuto/icon/hand.svg" >}} button on a view that is currently OFF picks the link target according to how many candidates exist:

- **A manual-sync group already exists in the container** — the new view joins it directly (bidirectional links are added to every member). No picker is shown.
- **Exactly one candidate** — the link is established immediately, no picker.
- **Multiple candidates and no existing group** — a multi-select picker is shown so you can pick the views to sync with.

Once active:

- *Scroll* propagation is **forced on and locked** in the per-view sync popup — manual sync is built on top of scroll. All other per-action toggles (Pan, Zoom, W/L, …) remain freely configurable.
- The manual-sync button turns green to indicate that a manual link is established; clicking it again removes this view from the group.

{{% notice tip %}}
The auto-sync {{< svg-inline "static/tuto/icon/synch.svg" >}} and manual-sync {{< svg-inline "static/tuto/icon/hand.svg" >}} buttons coexist on the same view. Auto-sync is preferred whenever a shared FoR is available; manual sync is the fallback for views that fall outside any spatial group.
{{% /notice %}}

---

### Default Tile Mode {#tile-mode}

**Default Tile** mode fills all views in the current layout with consecutive images from the **same series**. It is useful for reviewing a series at a glance, comparing adjacent slices, or preparing a print layout with multiple images per page.

When this mode is active:
- Each view shows a different image of the same series (n, n+1, n+2, …).
- **Scroll** advances the entire tile group by one image at a time.
- **Every other per-action setting** is enabled by default — the user-toggleable actions Pan, Zoom, Rotation, Flip, Window/Level and Spatial unit, plus the always-on internal actions Preset, LUT, LUT shape, Invert LUT, Filter, Inverse stack and Sort stack — so the tile group behaves as a single coherent display. Use the [per-action toggles](#per-view-sync) to disable any of the user-toggleable ones if you want a tile-by-tile divergence (e.g. independent zoom for cropped previews).

**Typical use case:** Print or export a multi-image layout where each cell contains a different slice of the same series. See [Print](print) for more details.

{{% notice note %}}
This is the opposite default from [Default Stack](#stack-mode), where only *Scroll* propagates and every other action starts off. Tile mode assumes you want everything in lock-step (same series, multi-cell view); Stack mode assumes you want surgical control (different series, cross-modality comparison).
{{% /notice %}}

---

### 3D Cursor Synchronization {#crosshair-sync}

The {{< svg-inline "static/tuto/icon/crosshair.svg" >}} **3D cursor (crosshair)** is a special synchronization mechanism that links the cursor **position** in 3D space across views that share the same Frame of Reference UID.

Unlike the stack mode which only synchronizes near the same anatomical depth, the crosshair lets you click precisely in one view and see that exact 3D point highlighted in all other views simultaneously — regardless of the slice or plane orientation.

See the [3D cursor](cursor-3d) tutorial for full details.

---

### MPR Synchronization {#mpr-sync}

In the [MPR viewer](mpr), the three reconstruction planes (axial, coronal, sagittal) are always cross-synchronized by the crosshair. In addition, **Default Stack** mode propagates *Scroll* between the MPR views and any other 2D view sharing the same Frame of Reference UID — and any further action (*Zoom*, *Window/Level*, …) that the user has explicitly enabled through the per-action toggles described below.

To disable synchronization in the MPR, use the per-action toggles in each MPR view's [Synchronize submenu](#mpr-sync-options) to opt individual actions out (Zoom, Window/Level, …) while keeping the crosshair coupling intact.

#### Per-view sync options in the MPR {#mpr-sync-options}

MPR views do **not** show the auto-sync / manual-sync overlay buttons described in [Per-view sync controls](#per-view-sync) — synchronization between MPR planes is structural (driven by the crosshair) and cannot be turned off per view. Instead, the per-view sync configuration is reached through a **Synchronize** submenu in the MPR configuration popup (settings icon {{< svg-inline "static/tuto/icon/viewSettings.svg" >}} in the top-right corner of the view — listed alongside the other [MPR settings](mpr)).

The submenu is the same as the one opened by the auto-sync button on a regular 2D view, **minus the master "Synchronize" toggle** (you cannot disable synchronization for a single MPR plane — see above). It contains:

- **Per-action toggles** for *Scroll*, *Pan*, *Zoom*, *Rotation*, *Flip*, *Window/Level* and *Spatial unit*. The submenu stays open while you flip several options.
- **Apply to all views** — propagates the current selection to every other view sharing the same Frame of Reference UID. Decorated with the FoR color chip identifying the target group.
- **Close** — closes the popup.

{{% notice note %}}
When manual synchronization is active on the view, *Scroll* is forced on and locked — manual sync is built on top of scroll propagation.
{{% /notice %}}

---

### Cine and Synchronization {#cine-sync}

When the [cine](dicom-2d-viewer/#cine) animation is active on a series, all other series currently synchronized with it (via **Default Stack** or **Default Tile**) are animated as well. The cine remains active across series until the **Cine stop** button {{< svg-inline "static/tuto/icon/suspend.svg" >}} is clicked.
