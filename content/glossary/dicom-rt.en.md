---
title: "What Are DICOM RT Objects?"
linkTitle: "DICOM RT"
description: "Radiotherapy DICOM objects describe the contours, the plan and the delivered dose of a treatment."
keywords: [ "what is dicom rt", "rtstruct", "rt dose", "dvh", "radiotherapy dicom", "dose volume histogram" ]
---

## <center>What Are DICOM RT Objects</center>

Radiotherapy uses a family of DICOM objects that describe a treatment rather than an image.

An **RT Structure Set** (RTSTRUCT) holds the contours drawn on the planning images: the target
volumes and the organs at risk, each as a named set of outlines with a frame of reference tying it to
the CT it was drawn on. An **RT Plan** describes how the treatment is to be delivered — beams,
segments, fractions. An **RT Dose** carries the computed dose as a three-dimensional grid, displayed
as isodose lines over the anatomy or as a color wash.

The **dose-volume histogram (DVH)** summarizes that grid against the contours: for each structure,
how much of its volume receives at least a given dose. It is the standard way to check that a plan
covers the target while sparing what surrounds it, and it can be stored in the RT Dose object or
recomputed from the dose grid and the structures.

Read together, these objects let a viewer show contours, isodoses and the DVH against the planning
images — which is a different task from reading a diagnostic study, and why viewers treat them
separately.

In Weasis, see [DICOM RT viewer](../../tutorials/dicom-rt).
