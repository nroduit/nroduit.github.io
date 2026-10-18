---
title: "DICOM Color Maps and Pseudo-Color"
weight: 332
description: How to pick, mark as favorite, create and share the color maps used for pseudo-color 2D images, fusion overlays and 3D volume rendering
linkTitle: "Color Maps"
keywords: [ "dicom color map", "pseudo color", "color lut", "color map editor", "fusion color scale", "volume rendering color" ]
since: "4.8.0"
---

## <center>From a value to a color, and to an opacity {{< svg-inline "static/tuto/icon/lut.svg" >}}</center>

A **color map** turns a value into a color, and — where transparency matters — into an opacity. The same maps are used everywhere in Weasis:

* as the **pseudo-color LUT** of a 2D image, on top of the grayscale rendering — see [Lookup Tables](lut/);
* as the palette of a [**fusion overlay**](fusion/), where the opacity of the map decides what is painted over the anatomy;
* as a **volume preset** of the [3D viewer](dicom-3d-viewer/), where each value also carries lighting and material properties.

A map is a list of **stops** placed along a value axis. Each stop carries a color, an opacity, or both, and the values in between are interpolated. Positions are either **relative** to the displayed window — the classic behavior of a color table — or anchored to real values such as Hounsfield units, SUVbw, or a percentage of a reference. A map with a `FIXED` [domain](#quick-settings), such as _CT Tissues_, always paints a given density with the same color, whatever the window and level.

### Picking a color map {#pick}

Color maps are offered wherever a LUT can be chosen:

* in the 2D viewer, from the **Lookup Table** toolbar {{< svg-inline "static/tuto/icon/lut.svg" >}}, the right-click menu, and the **LUT** list of the [Windowing and Rendering](lut/#windowing-and-rendering) panel;
* in the [fusion](fusion/) panel, as the **LUT** of the overlay;
* in the 3D viewer, from the **LUT** toolbar and the right-click menu.

The toolbar and the menus show each map with a **preview strip**, which is usually the fastest way to choose. They all use the same sections, from top to bottom:

* the entries that are not color maps — **_Default (image)_**, which keeps the colors of the image itself, and **_Gray_**;
* **Favorites**, your own shortlist;
* the maps meant for the **modality** of the displayed image or volume;
* **General**, then one submenu per **category**;
* **Other modalities**, with one submenu per modality;
* **Imported** — the color palettes found in the loaded DICOM objects during the session;
* **User** — the maps you created.

A favorite stays at the root of the menu, followed in gray by the name of the submenu it comes from, so you always know where it belongs.

#### Favorites {#favorites}

To keep the maps you use often within reach:

* select a map, then pick **Add "…" to favorites** in the LUT dropdown or in the right-click menu (the same entry reads **Remove "…" from favorites** when it is already one);
* or check **Favorite** in the [color map editor](#editor); favorites are marked with a ★ in its list.

Favorites are saved together with your own maps.

#### The maps delivered with Weasis {#built-in}

| Category | Maps |
|---|---|
| **Clinical** | Maps anchored to real values: _PET SUV_ (SUVbw), _CT Tissues_, _CT Lung Density_, _CT Calcium_, _CT Bone Density_, _CT Body Composition_ (Hounsfield units), _Isodose_ (percentage of the prescribed dose), plus _Doppler flow_, _T1 Map (Lipari)_, _T2 Map (Navia)_, _fMRI Red-Yellow_, _fMRI Blue-Lightblue_ and _Cardiac_ |
| **DICOM** | The well-known palettes of the DICOM standard: _Hot Iron_, _PET_, _Hot Metal Blue_, _PET 20 Step_, _Spring_, _Summer_, _Fall_, _Winter_ |
| **Classic** | The historical Weasis tables: _Rainbow_, _Spectrum_, _Fire_, _Ice_, _Cool_, _Bone_, _NIH_, _GE Color_, _Stern_ |
| **Scientific** | Perceptually uniform maps, which do not invent contrast where the data has none: _Viridis_, _Magma_, _Inferno_, _Plasma_, _Cividis_, _Turbo_, _Cool to Warm_ |
| **Overlay** | Single-hue and hot ramps intended for [fusion](fusion/): _Green Overlay_, _Magenta Overlay_, _Hot Overlay_ |

The volume presets of the 3D viewer are listed in the same library, grouped by anatomical category (bone, vascular, cardiac, lung and airways, soft tissue and skin, endoscopy, projection, neuro). Most of them are CT presets; MR has its own _Default_, _MIP_, _Angiography_ and _T2-Brain_ presets, PET and NM a _Hot_ preset in SUVbw or in percent of the maximum, and US a _Fetal_ preset — see [3D Volume Renderer](dicom-3d-viewer/#windowing).

{{% callout note %}}
A map with a fixed domain keeps its colors where the values are: _CT Tissues_ paints fat, soft tissue and bone at their Hounsfield values and does not follow the window and level. _PET SUV_ is graduated in SUVbw, but its domain is absolute: its range is the starting window, and changing the window and level rescales it. A relative map is spread over the window currently displayed, so moving the window moves the colors.
{{% /callout %}}

### The color map editor {#editor}

Open it with **Edit color maps…**, at the bottom of the LUT dropdown of the toolbar or of the LUT right-click menu, in the 2D viewer as well as in the 3D viewer. The dialog is **modeless**: it can stay open while you scroll through the images, and every change is shown on the selected view as you make it.

#### The map library {#library}

The left side lists the maps and the volume presets of the library. Narrow it down with the filters above the list:

* a **Filter** text field, matching the name and the keywords of a map;
* the **modality**, preselected on the modality of the displayed image;
* the origin — **All**, **Built-in**, **Imported** or **User**;
* the **category**;
* **All**, **2D maps** or **3D presets**, preselected on what the viewer that opened the editor renders.

Selecting a map loads it in the editor and, with **Live preview** on, applies it to the view.

#### Quick settings {#quick-settings}

The upper part covers what most maps need. The colored strip right below it previews the result.

* **Name** — the name shown in the LUT lists.
* **Type** — what kind of map this is. It is mostly a declaration of intent, which tells the editor and the reader how the map is meant to be used; only `CYCLIC` changes the way values are rendered.
  * `SEQUENTIAL` — a single ordered ramp from the low end to the high end, for a quantity that grows in one direction (density, uptake, dose). The usual choice.
  * `DIVERGING` — two ramps meeting at a neutral center, for values read against a reference: the center is "no difference", and each side shows a departure from it. Typical of subtraction and difference images, or of flow read in two directions (_Doppler flow_, _Cool to Warm_).
  * `CYCLIC` — the two ends are the same color, and values wrap around instead of being clamped: a value above the top of the range comes back at the bottom. Only for quantities that are angles by nature, such as phase.
  * `QUALITATIVE` — distinct colors for classes rather than a continuum (tissue classes, labels, segments). It is normally used with the `STEP` interpolation so that nothing is blended between two classes — _CT Tissues_ and _CT Lung Density_ are built that way.
  * `TRANSFER` — color **and** opacity: the opacity curve belongs to the map, and not just to the image it is used on. This is what a [fusion](fusion/) overlay and a volume preset need, and Weasis sets it by itself as soon as you build an opacity ramp with **Transparent below / Opaque from**.
* **Modalities** — the modalities the map is offered for, separated by commas (e.g. `CT, MR`). Leave empty to offer it for every image. **Default for these modalities** makes it the map applied automatically when such a series is opened.
* **Favorite** — adds the map to the [favorites](#favorites), immediately and regardless of the other changes.
* **Domain** — how the positions of the stops are read:
  * `RELATIVE` — positions between 0 and 1 over the displayed window;
  * `ABSOLUTE` — positions in the **Unit** you enter (HU, SUVbw, Gy…); the range is the default window and window/level rescales the map;
  * `FIXED` — same, but the window and level never move the colors;
  * `PERCENT` — positions in percent of a **Reference** value: `max`, the maximum of the data (the default); `window`, the value range of the displayed volume; or `prescription`, the prescribed dose of an [RT dose grid](dicom-rt/) (_Isodose_ is built that way).
* **Range** — the lowest and the highest position of the map. Changing it rescales the stops.
* **Bits** — how finely the map is sampled: 8 bits is enough for an ordinary palette, 12 or 16 keep the gradient smooth on wide-range data such as CT or PET.
* **Blend space** — the color space in which two consecutive stops are mixed. It changes only the colors *between* the stops; each stop always keeps the color you gave it.
  * `RGB` — mixes the red, green and blue components directly. The cheapest, and the way most older color tables were built, but the middle of a ramp between two saturated hues can turn dull: halfway between blue and yellow is gray.
  * `HSL` — mixes along the color wheel, by the shorter arc, and blends saturation and brightness separately. Ramps stay vivid and pass through the hues that lie between the two stops. A gray stop has no hue of its own, so it borrows the hue of its neighbor instead of sweeping the whole wheel.
  * `LAB` — mixes in the perceptual CIE L\*a\*b\* space, where equal steps of value look like equal steps of color. Nothing in the ramp then reads as a flat stretch or as an artificial edge, which matters when the color is used to estimate a value and not only to spot a structure. Most of the **Scientific** maps (_Viridis_, _Magma_, _Cividis_, _Cool to Warm_…) and the parameter maps _T1 Map_ and _T2 Map_ are built this way.
* **Interpolation** — how the values between two stops are filled:
  * `LINEAR` — a straight blend from one stop to the next; the default.
  * `STEP` — each stop holds its color until the next one, which gives the flat bands of a qualitative map or of an isodose display (_Isodose_, _CT Body Composition_).
  * `SAMPLED` — the map comes from a flat table, a legacy `.txt` file or a DICOM color palette, where every entry of the table is a stop. It is rendered like `LINEAR`; the difference is that such a map has hundreds of stops, so it is reshaped with the **Palette**, **Bands** or **Range** actions rather than stop by stop.

  A single hard edge does not need `STEP`: two stops placed at the same position produce one, and the rest of the map stays smooth.
* **Palette** + **Apply** — replaces the colors of the map with those of another map of the library, keeping the opacity curve. **Reverse** flips the map end to end.
* **Bands** + **Apply** — turns the map into the given number of flat bands, for contour-like readings.
* **Transparent below** / **Opaque from** + **Apply** — builds the opacity ramp: everything under the first value is invisible, everything above the second is fully painted. This is what makes an overlay show only the significant uptake, or a volume preset show only bone.
* **3D** — **Volume preset** turns the map into a preset usable by the 3D viewer; it then gets lighting, and its positions are anchored to the values of the displayed data. **Shade** enables shading, **Specular power** sets how tight the highlights are, and **Edge emphasis** fades the homogeneous interiors so that the boundaries between structures stand out.

#### Stops, curve and materials {#advanced}

The **Advanced** section, collapsed by default, is where a map is shaped in detail. It shows the color strip of the map, the opacity curve above it with one node per stop, and — behind them — the **histogram** of the displayed image or volume, so stops can be placed where the tissues actually are.

On the curve:

* **double-click** to add a stop at that value, with the color the map already has there;
* **drag** a node to move a stop; moving it up or down changes its opacity;
* **right-click** a node, or select it and press **Delete**, to remove it.

The table below lists the same stops numerically — **Position**, **Color** (click to open the color picker), **Alpha** and **Group** — with three more columns for a volume preset: **Ambient**, **Diffuse** and **Specular**. The buttons beside it add a stop in the middle of the range, remove the selected one, or **Pick from image**: the next click on the view adds a stop at the real value read under the cursor — the simplest way to place a stop on the tissue you are looking at. Any other click cancels the pick. Since the picked value is a physical one, the button only works on a map anchored to values, not on a relative one.

For a volume preset, the **Material** list applies a ready-made combination of lighting coefficients (`MATTE`, `SOFT_TISSUE`, `SKIN`, `VESSEL`, `BONE`, `GLASS`, `METAL`) to the selected stop or to every stop. **Apply to all** also sets the matching specular power; **Apply to stop** keeps the specular power of a preset that already has lighting. The status line at the bottom of the dialog reports the **share of the voxels the preset leaves visible**, a quick check that a preset is neither empty nor a solid block.

#### Saving and sharing {#save}

The bottom bar holds the actions on the map as a whole:

* **Undo** / **Redo** — step through the editing history (**Ctrl + Z** and **Ctrl + Y**).
* **Duplicate** — starts a copy of the current map under a new name, leaving the original untouched. This is the usual way to build on a map delivered with Weasis.
* **Save** — stores the map among your own maps and refreshes the LUT lists of the open viewers. Saving a modified built-in map does not overwrite anything: your version takes its place in the lists, and the **Delete** button, which then reads **Reset**, brings the original back.
* **Delete** — removes one of your maps, after confirmation. For your version of a built-in or site map, the button reads **Reset** and brings that map back.
* **Import** / **Export** — exchange maps as files (see below).
* **Live preview** — applies every change to the selected view as you make it; turn it off to work on a map without disturbing the displayed image.
* **Close** — leaves the editor. What was not saved is discarded, and the view goes back to the last saved map, or to the LUT it had when the editor was opened.

{{% callout info %}}
Your maps and your favorites are stored in the `customColorMaps.json` file of the Weasis preferences folder, on this workstation. A site may also ship maps for all of its users in `config/colormaps.json` of the resources package (see [Configuration documents](../basics/customize/preferences/#configuration-documents)): they are marked *(site)* in the editor and are read-only — a map the site locked cannot be replaced or hidden by yours; duplicate it to make your own version. Volume presets created with an earlier version, in `customVolumePresets.json`, are imported once on the first start; the old file is then renamed `customVolumePresets.json.migrated`.
{{% /callout %}}

#### File formats {#formats}

| Format | Import | Export |
|---|---|---|
| **JSON color map** (`.json`) — the native format, with the stops, the domain, the opacity and, for a preset, the lighting; the only format offered by the editor of the 3D viewer | ✔ | ✔ |
| **DICOM color palette** (`.dcm`) — a Color Palette object, readable by other DICOM software (DICOM 2D viewer only); the exported object embeds an sRGB input-device ICC profile, as the standard requires {{< since "4.8.0" >}} | ✔ | ✔ |
| **Legacy color table** (`.txt`) — 256 lines of `R G B` values, the format of the older Weasis LUT files (2D viewers only) | ✔ | — |

A legacy table carries neither opacity nor anchored positions, which is why it is read but never written. An imported map is loaded in the editor: give it a name and **Save** it to keep it. When a JSON document holds several maps, only the first one is imported.

The JSON document is the same for an exported map, for `customColorMaps.json` and for the maps delivered with Weasis: an envelope with a schema version, the maps and, in the user file, the ids of the favorites. Only `name` and `stops` are required; a field left out keeps its default.

```json
{
  "schema": 1,
  "maps": [
    {
      "id": "user.pet-suv-hot",
      "name": "PET SUV Hot",
      "type": "transfer",
      "category": "Clinical",
      "tags": ["pet", "suv"],
      "modality": ["PT"],
      "default": false,
      "domain": {"kind": "absolute", "unit": "SUVbw", "min": 0, "max": 10},
      "bits": 12,
      "space": "lab",
      "interpolation": "linear",
      "stops": [
        {"pos": 0, "color": "#000000", "alpha": 0},
        {"pos": 2.5, "color": "#ff0000", "alpha": 0.8, "group": "uptake"},
        {"pos": 10, "color": "#ffff00", "alpha": 1}
      ],
      "outside": {"low": "transparent", "high": "#ffff00"},
      "lighting": {"shade": true, "specularPower": 20, "gradientOpacity": [{"magnitude": 0, "factor": 0.2}, {"magnitude": 0.3, "factor": 1}]},
      "metadata": {"dicom.contentLabel": "PET_SUV_HOT"}
    }
  ],
  "favorites": ["user.pet-suv-hot"]
}
```

| Field | Meaning |
|---|---|
| `id` | Stable identifier (`user.` for your maps); a user map with the id of a built-in map takes its place in the lists. |
| `type`, `domain`, `bits`, `space`, `interpolation` | The [quick settings](#quick-settings), written in lower case; `domain.reference` belongs to a `percent` domain. |
| `category`, `tags`, `hidden` | The submenu of the LUT menus, the keywords matched by the **Filter** field, and `true` to keep the map out of the lists. |
| `modality`, `default` | The modality codes the map is offered for, and `true` for the map applied when such a series is opened. |
| `stops[]` | `pos` is required; `color` is `#rrggbb` (or `transparent`), `alpha` goes from 0 to 1, `group` is a free label; `ambient`, `diffuse` and `specular` are the material of a volume preset. |
| `outside` | Colors for the values below the first stop (`low`), above the last one (`high`) and for `nan`; left out, the nearest stop is used. |
| `lighting` | Present for a volume preset only: `shade`, `specularPower` and the `gradientOpacity` points (`magnitude`, `factor`) behind **Edge emphasis**. |
| `metadata` | Free provenance, e.g. the UID and label of an imported DICOM palette. |

{{% callout tip %}}
The color maps of a DICOM file are used without any action on your part: a Palette Color image and the palette of a [Presentation State](build-ko-pr/) are applied when the image is opened, and the palettes met while loading appear in the **Imported** section of the LUT menus, ready to be reused on another image. A **Blending** presentation state is applied the same way {{< since "4.8.0" >}}: when you open the series it names as the underlying one and the superimposed series is loaded, that series becomes the [fusion overlay](fusion/), windowed by the state's own layer, colored with its palette and blended with its relative opacity.
{{% /callout %}}
