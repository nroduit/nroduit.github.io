---
title: "What Is a DICOM Segmentation (SEG) Object?"
linkTitle: "DICOM SEG"
description: "A DICOM Segmentation stores labeled regions as a separate object that references the images they were drawn on."
keywords: [ "what is dicom seg", "dicom segmentation object", "seg dicom", "fractional segmentation", "ai segmentation dicom" ]
---

## <center>What Is a DICOM Segmentation (SEG) Object</center>

A **DICOM Segmentation**, usually written **SEG**, is a DICOM object that stores *which voxels
belong to what*: one or more labeled segments — an organ, a lesion, a target volume — each
referencing the frames of the source series they were derived from. The segmentation travels as its
own file, so the original images are never modified.

Every segment carries coded metadata: an anatomical category and type, and often the algorithm that
produced it, which is how a viewer can tell an automatically generated segment from a manually drawn
one.

SEG objects come in two flavors. A **binary** segmentation marks each voxel as in or out. A
**fractional** one stores a value per voxel, expressing either the fraction of the voxel occupied by
the structure or a probability — which is what many AI models produce, and what lets a viewer show a
soft, thresholded overlay rather than a hard edge.

Because a segmentation references its source frames, it is displayed over the series it belongs to.
Its geometry is defined independently of the source resolution, so a viewer may have to resample it
to draw the overlay.

In Weasis, see [DICOM SEG viewer](../../tutorials/dicom-segmentation).
