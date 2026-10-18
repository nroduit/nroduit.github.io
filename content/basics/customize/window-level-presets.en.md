---
title: Window/Level presets
weight: 25
description: "Ship a shared set of Window/Level presets to every user of a site: where the JSON document is declared, its format, and how it combines with the other presets."
keywords: [ "window level presets", "window width", "window center", "voi lut", "site configuration", "shared presets", "ct presets" ]
since: "4.8.0"
---

## <center>Share Window/Level presets with all users</center>

Weasis combines three sets of Window/Level presets {{< since "4.8.0" >}}:

| Set | Where it comes from | Editable by users |
|---|---|---|
| **Built-in** | delivered with Weasis (the CT presets _Brain_, _Lung_, _Bone_…) | no |
| **Site** | `config/windowPresets.json` of the resources package, see [Configuration documents](../customize/preferences/#configuration-documents) | no |
| **User** | saved by each user in `customWindowPresets.json` of the preferences folder; see [Window / Level presets](../../tutorials/lut/#window-level-presets) | yes |

The three sets are merged by preset **id**: a site preset with the id of a built-in preset replaces it, and a user preset replaces a site one — unless the site locked it. Users see the site presets as read-only, marked *(site)* or *(site, locked)*, in **Preferences > Viewer > Window/Level presets** and can duplicate them to make their own version; a user preset that overrides a site or built-in one offers **Reset to the site preset** instead of **Delete**.

### Ship the site document

The site document is `config/windowPresets.json` of the resources package — `resources.zip` uploaded in ViewerHub for a release and a group, or `app/resources/config/` of a local installation — like the other [configuration documents](../customize/preferences/#configuration-documents). The package is fetched and cached by the launcher, so the document is always a local file: reading it never waits for the network. A document that cannot be parsed leaves the built-in and user presets available and is reported in the log. The **Reload configuration files** button of the preferences dialog reads it again without restarting.

{{% callout tip %}}
The easiest way to write the document is to create the presets in **Preferences > Viewer > Window/Level presets**, then export them with **⋯ > Export…** (the export holds the user presets only). Rename the ids from `user.` to `site.` before publishing the file.
{{% /callout %}}

### Document format

The document is a JSON object with a schema version and a list of presets:

``` json
{
  "schema": 1,
  "presets": [
    {
      "id": "site.ct.liver-portal",
      "name": "Liver portal phase",
      "modality": ["CT"],
      "window": 180,
      "level": 60,
      "domain": {"kind": "absolute", "unit": "HU"},
      "key": "9",
      "when": {"preferBodyPart": ["ABDOMEN"]}
    },
    {
      "id": "site.mr.bright",
      "name": "Bright",
      "modality": ["MR"],
      "window": 60,
      "level": 45,
      "domain": {"kind": "percent", "reference": "series"}
    }
  ]
}
```

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Stable identifier, prefixed `site.`. Reuse the id of a built-in preset (e.g. `weasis.ct.lung`) to change it for everyone. |
| `name` | yes | Name shown in the preset list. |
| `modality` | no | [DICOM modality](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.3.html#sect_C.7.3.1.1.1) codes (`CT`, `MR`, `PT`…), as a list or a single string; absent means every modality. |
| `category`, `tags` | no | A category name and a list of keywords, kept in the document for your own organization; the viewer does not show them. |
| `window`, `level` | yes | Window width (greater than 0) and center, in the values given by `domain`. |
| `domain.kind` | no | `absolute` (default): modality values after the Modality LUT, e.g. Hounsfield units for CT. `percent`: percentages of a value range, for images without calibrated values (MR, PET, CR…). |
| `domain.unit` | no | Unit shown with absolute values, e.g. `HU`. |
| `domain.reference` | no | For `percent`: `image` (default), the range of each image, or `series`, the range given by the series (_Smallest / Largest Pixel Value in Series_, otherwise the image range). |
| `shape` | no | LUT shape: `linear` (default), `linear-exact`, `sigmoid` (defined by DICOM), `sigmoid-norm`, `log`, `log-inv` (Weasis shapes). |
| `key` | no | Shortcut digit from `3` to `9` (`0`, `1` and `2` are used by _Auto Level_ and the windows of the image). When two presets offered for an image share a digit, the one of the latest set gets it — user over site over built-in — and the other is reported in the log. The built-in CT presets use `3` to `7`. |
| `when.minBitsStored` | no | Offer the preset only from this _Bits Stored_ value; default `9`, which leaves out 8-bit secondary captures. |
| `when.requiresRescale` | no | `true` to offer the preset only for images with a Modality LUT (rescale slope / intercept). |
| `when.bodyPart` | no | Offer the preset **only** for this anatomy (see below). |
| `when.preferBodyPart` | no | List the preset **first** for this anatomy; it stays available for other images. |
| `default` | no | `true`: applied first to images that carry no window values of their own (neither in the file nor in a presentation state). |
| `hidden` | no | `true`: kept out of the lists. Redefine a built-in id with `hidden` to remove that preset for everyone (the preset must still have a name, a window and a level). |
| `locked` | no | `true` in the site document: the user layer can neither replace nor hide the preset. Only the site document can lock. |
| `extends` | no | The `id` of a preset to start from — another preset of the same document or one of a lower layer, e.g. a built-in id — giving only the fields that change. A field replaces the whole field of the base (`when` and `domain` included); `extends`, `id` and `locked` are never inherited. |

#### Anatomy

`bodyPart` and `preferBodyPart` accept a list of:

* an **area**: `HEAD`, `NECK`, `CHEST`, `BREAST`, `ABDOMEN`, `PELVIS`, `EXTREMITY`, `UPPER_EXTREMITY`, `LOWER_EXTREMITY`, `WHOLE_BODY` — the _Region imaged_ values of the [LOINC/RSNA Radiology Playbook](https://loinc.org/kb/radiology/loinc-rsna-radiology-playbook-user-guide) — and `SPINE`. An area includes all its regions: `CHEST` also matches a lung, a heart or a chest-abdomen-pelvis image.
* a [Body Part Examined](https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html) term, e.g. `LIVER`;
* a code, e.g. `SCT:10200004` (SNOMED CT).

The anatomy of an image comes from its _Anatomic Region Sequence_, otherwise from its _Body Part Examined_. Many images record neither: prefer `preferBodyPart`, which never hides a preset. A value that is none of the above is compared with the _Body Part Examined_ of the image as written, and reported in the log in case it is a typo.
