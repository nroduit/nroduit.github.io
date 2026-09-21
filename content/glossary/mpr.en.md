---
title: "What Is MPR (Multiplanar Reconstruction)?"
linkTitle: "MPR"
description: "Multiplanar reconstruction rebuilds views in planes the scanner never acquired, from a stack that it did."
keywords: [ "what is mpr", "mpr meaning", "multiplanar reconstruction", "mpr dicom", "coronal sagittal reconstruction", "oblique reconstruction" ]
---

## <center>Re-slicing a volume in a plane it was never scanned in</center>

**Multiplanar reconstruction (MPR)** takes a stack of parallel images — typically axial CT or MR
slices — treats it as a volume, and re-slices that volume in another plane. From one axial
acquisition you get coronal and sagittal views, and any oblique plane in between, without scanning
the patient again.

It is useful whenever anatomy does not follow the plane of acquisition: a vessel running
head-to-foot, a fracture line crossing slices, a structure easier to follow along its own axis than
across it.

Two things decide how good the result looks. **Slice spacing** — a volume reconstructed from thick,
widely spaced slices is blurry or stepped in the other planes, because the data simply is not there.
And **geometry** — the slices must be parallel, regularly spaced and share a frame of reference;
irregular spacing, non-parallel slices or a tilted gantry distort the reconstruction unless the
viewer corrects for it.

A reconstructed plane is a computed image, not an acquired one. Measurements taken on it are only as
trustworthy as the geometry underneath.

In Weasis, see [MPR Viewer](../../tutorials/mpr).
