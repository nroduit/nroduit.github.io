---
title: "What Is a DICOM Structured Report (SR)?"
linkTitle: "DICOM SR"
description: "A DICOM Structured Report stores report content as a coded tree rather than as free text, so measurements stay machine-readable."
keywords: [ "what is dicom sr", "dicom structured report", "sr dicom", "coded measurements dicom", "scoord" ]
---

## <center>What Is a DICOM Structured Report (SR)</center>

A **DICOM Structured Report (SR)** stores the content of a report as a **tree of coded items**
instead of a block of prose. Each node pairs a concept with a value — a measurement and its unit, a
finding and its code, a piece of text, an image reference — and the nesting expresses which
observation belongs to which finding.

The point is that the content stays usable by software. A measurement recorded in an SR can be
extracted, compared across examinations and fed into a report or a database without anyone parsing
sentences.

Two kinds of node make SR useful in a viewer. **Image references** tie an observation to the exact
image it was made on, and **spatial coordinates** (SCOORD) tie it to a position within that image, so
a viewer can take you to the measurement rather than just telling you it exists.

SR is what carries the measurements produced by CAD and AI tools, ultrasound machines and dose
monitoring systems. What a reader sees is a structured document, not a rendered page: how it is laid
out is the viewer's decision, not the file's.

In Weasis, see [DICOM SR viewer](../../tutorials/dicom-sr).
