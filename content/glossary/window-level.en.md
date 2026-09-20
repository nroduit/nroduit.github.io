---
title: "What Are Window and Level in DICOM?"
linkTitle: "Window / Level"
description: "Window and level select which range of stored pixel values is mapped to the shades of gray on screen."
keywords: [ "what is window level", "window width center dicom", "voi lut", "windowing dicom", "hounsfield window", "dicom contrast" ]
---

## <center>What Are Window and Level in DICOM</center>

A DICOM image stores far more distinct values than a display can show or an eye can separate — CT,
for instance, covers thousands of Hounsfield units. **Windowing** chooses which part of that range
becomes visible: the **window width** is how wide a band of values is mapped to the available shades
of gray, and the **window center** (the *level*) is where that band sits.

Narrow the window and small differences become visible while everything outside the band turns pure
black or white; widen it and more of the range fits on screen with less contrast between nearby
values. This is why the same CT is read at one setting for lung and another for bone or soft tissue:
the pixel data does not change, only the mapping.

The values are not arbitrary. A study often carries **VOI LUT** information — either a window
width and center chosen at acquisition, or a full lookup table — and viewers add presets per
modality so a reader can jump between the settings that matter for a body region.

Because windowing is display only, it never alters the stored pixels; what it does alter is what a
screenshot or an exported picture will show.

In Weasis, see [LUTs and window/level](../../tutorials/lut).
