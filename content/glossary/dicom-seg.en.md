---
title: "What Is a DICOM Segmentation (SEG) Object?"
linkTitle: "DICOM SEG"
description: "A DICOM Segmentation stores labeled regions as a separate object that references the images they were drawn on."
keywords: [ "what is dicom seg", "dicom segmentation object", "seg dicom", "fractional segmentation", "labelmap segmentation", "ai segmentation dicom", "seg vs rt structure set" ]
---

## <center>Which voxels belong to what, in a file of its own</center>

A **DICOM Segmentation**, usually written **SEG**, is a DICOM object that stores *which voxels
belong to what*: one or more labeled segments — an organ, a lesion, a target volume — each
referencing the frames of the source series they were derived from. The segmentation travels as its
own file, so the original images are never modified.

Every segment carries coded metadata: an anatomical category and type, and how it was produced —
manually, semi-automatically or automatically, usually with the name of the algorithm — which is how
a viewer can tell a generated segment from a hand-drawn one.

Three storage types exist. **BINARY** marks each voxel as in or out, packed one bit per voxel.
**FRACTIONAL** stores a value per voxel, expressing either the probability that the voxel belongs to
the segment or the fraction of it actually covered — which is what many AI models produce, and what
lets a viewer draw a graded overlay rather than a hard edge. **LABELMAP** packs many segments into a
single image by storing the segment number in the voxel value: compact for an object carrying dozens
of structures, but, unlike the other two, with no room for segments that overlap.

Lining a segmentation up with images is not only a matter of the references it declares. A SEG names
the series and the frames it was derived from, but it also shares a **frame of reference** with them
— the same patient coordinate system — so a viewer can place the masks by spatial position when
those references are missing or point at another reconstruction of the same acquisition. Its grid is
defined independently of the source resolution, so drawing the overlay may involve resampling.

A segmentation is not an [RT Structure Set](dicom-rt): RT stores outlines as polygons in patient
coordinates, SEG stores voxels, and converting between them loses something either way. Whichever it
is, it is an assertion *about* the images rather than a correction *of* them, and it is worth no more
than whatever produced it — which is why the algorithm is recorded alongside the segment.

In Weasis, see [DICOM SEG viewer](../../tutorials/dicom-segmentation).
