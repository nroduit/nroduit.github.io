---
title: "What Is a DICOM Structured Report (SR)?"
linkTitle: "DICOM SR"
description: "A DICOM Structured Report stores report content as a coded tree rather than as free text, so measurements stay machine-readable."
keywords: [ "what is dicom sr", "dicom structured report", "sr dicom", "coded measurements dicom", "scoord", "comprehensive sr", "sr template tid" ]
---

## <center>A report software can read, not only display</center>

A **DICOM Structured Report (SR)** stores the content of a report as a **tree of coded items**
instead of a block of prose. Each item pairs a concept with a value — a measurement and its unit, a
finding and its code, a piece of text, a reference to an image — and declares how it relates to the
item above it: *contains*, *has properties*, *inferred from*. The nesting therefore carries meaning
of its own, expressing which observation belongs to which finding and what each one was derived
from.

What makes the content usable by software is that the concepts and most of the values are **coded**
rather than written out. They are drawn from controlled vocabularies — DICOM's own, SNOMED CT for
anatomy and findings, UCUM for units — and standard **templates**, each identified by a TID, fix
which items a given kind of report is expected to contain. A measurement recorded that way can be
extracted, compared across examinations and fed into a database without anyone parsing sentences.

Two kinds of item make an SR useful in a viewer. **Image references** tie an observation to the exact
image it was made on, and **spatial coordinates** — SCOORD within the plane of an image, SCOORD3D in
the frame of reference — tie it to a position, so a viewer can take you to the measurement rather
than just telling you it exists.

SR comes in several flavors, from the deliberately limited **Basic Text SR** to **Comprehensive 3D
SR**, which differ in the value types and references they are allowed to use, alongside specialized
ones for CAD findings and radiation dose. Every SR also records how far it got: a **completion** flag
(*partial* or *complete*) and a **verification** flag, which says whether a responsible observer has
signed off on the content — worth a glance before a finding is acted upon.

SR is what carries the measurements produced by CAD and AI tools, ultrasound machines and dose
monitoring systems. What a reader sees is a structured document, not a rendered page: the layout is
the viewer's decision, not the file's, so two viewers may legitimately present the same SR
differently, or surface less of it, depending on the templates they recognize. A report encapsulated
as a PDF is not an SR — it displays, but nothing inside it can be read by software.

In Weasis, see [DICOM SR viewer](../../tutorials/dicom-sr).
