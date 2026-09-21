---
title: "What Is MIP (Maximum Intensity Projection)?"
linkTitle: "MIP"
description: "Maximum intensity projection collapses a slab of a volume into one image by keeping the brightest voxel along each ray."
keywords: [ "what is mip", "maximum intensity projection", "mip dicom", "thin slab mip", "angiography projection" ]
---

## <center>Bright structures survive, everything dimmer disappears</center>

**Maximum intensity projection (MIP)** casts a ray through a slab of the volume for every pixel of
the output image and keeps the **highest value** it meets. Bright structures therefore survive and
everything dimmer disappears.

That makes it the natural way to look at anything bright and thin spread over many slices:
contrast-filled vessels, calcifications, a lung nodule that is hard to spot slice by slice.

The trade-off is depth. Because only the maximum along each ray is kept, a MIP says nothing about
which of two bright structures lies in front of the other, and a single very bright voxel — metal, a
clip, contrast in an adjacent vessel — can hide what is behind it. This is why a **thin slab** is
usually more informative than projecting the whole volume: it limits how much anatomy is flattened
into one image.

A MIP is a projection, not a rendering: it has no lighting and no surfaces, and it is not a
substitute for reading the source slices.

In Weasis, see [MIP Viewer](../../tutorials/mip).
