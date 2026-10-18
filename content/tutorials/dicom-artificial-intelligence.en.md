---
title: "AI DICOM Viewer: Read AI-Generated Results"
weight: 339
description: "View AI results in DICOM for free: segmentations, structured reports, parametric maps, derived images. Weasis displays model output; the base version runs no model."
linkTitle: "AI DICOM Objects"
keywords: [ "ai dicom", "dicom ai", "ai dicom viewer", "ai dicom reader", "ai dicom analyzer", "ai segmentation dicom", "view ai segmentation", "derived images", "ai structured report", "totalsegmentator", "dicom ai output" ]
---

## <center>Model output packaged as standard DICOM</center>

**Weasis is a free viewer for AI results stored as DICOM.** It opens what an inference framework produced — segmentations, structured reports, parametric maps, derived images — and displays them over the study they were computed from. The base version does not run the models: the analysis happens in your own pipeline, and Weasis reads what that pipeline writes.

AI inference rarely defines its own file formats — instead, results are packaged as standard DICOM objects so any compliant PACS or viewer can ingest them. The same SOP Classes used for human-authored content (segmentations, structured reports, presentation states…) are reused to carry model outputs.

This page maps the AI-produced object types you are most likely to encounter to how Weasis displays them.

| Category                                    | Object type                                     | What AI typically uses it for                                  |
|---------------------------------------------|-------------------------------------------------|----------------------------------------------------------------|
| [Image outputs](#image-outputs)             | [Secondary Capture](#dicom-secondary-capture-sc)| Pre-rendered images with burned-in annotations or heatmaps     |
|                                             | [Enhanced Objects](#dicom-enhanced-objects)     | Denoised, super-resolved, or otherwise reconstructed images    |
|                                             | [Parametric Map](#dicom-parametric-map-pmap)    | Per-pixel probability maps, heatmaps, perfusion/diffusion maps |
| [Overlays on source images](#image-overlays)| [Segmentation (SEG)](#dicom-segmentation-seg)   | Pixel-based labels for anatomy or lesions                      |
|                                             | [RTSTRUCT](#dicom-rtstruct)                     | Vector contours for anatomy or regions of interest             |
|                                             | [Presentation State (GSPS)](#dicom-presentation-states-gsps) | Vector annotations, measurements, display settings |
| [Reports & documents](#reports--documents)  | [Structured Report (SR)](#dicom-structured-report-sr) | Findings, measurements, classification results           |
|                                             | [Encapsulated Documents](#dicom-encapsulated-documents) | PDF reports, attached non-image data                   |

## Does Weasis run AI models?

Not in the base version, and that distinction matters when choosing tools. Weasis is the **viewer** at
the end of an AI pipeline: the model runs wherever you deploy it — a research framework, a vendor
appliance, a PACS plug-in — and writes its output as DICOM. Weasis opens that output next to the
original images, so a reader can check the result against what was acquired.

A [plugin](../basics/customize/build-plugins) could still run a model inside Weasis, provided the
computer it runs on supports it (memory, GPU, runtime libraries). No such plugin is part of the
standard distribution.

Weasis can also start AI tasks and follow them {{< since "4.8.0" >}}, without running them itself. It
acts as a *User Agent*, the role defined by DICOMweb's Unified Procedure Step service (UPS-RS) and
used by the IHE **AI Workflow for Imaging** (AIW-I) profile. From the study you have open, you can ask
the server to run an AI task, see whether that task is queued, running or finished, and open its
results once they are ready.

## Image outputs

These objects carry their own pixel data and are viewed as standalone images.

#### DICOM Secondary Capture (SC)

Pre-rendered images where the AI has burned its output directly into the pixels — typically annotations, heatmaps, or side-by-side comparisons. Convenient for legacy viewers, but the overlay cannot be toggled off or recomputed.

{{% callout info %}}
Secondary Capture displays like any other image, see [DICOM 2D Viewer](dicom-2d-viewer).
{{% /callout %}}

#### DICOM Enhanced Objects

Reconstructed or post-processed images — for example denoised CTs, super-resolved MRs, or motion-corrected series. The output replaces or complements the original acquisition rather than annotating it.

{{% callout info %}}
Enhanced images display like any other image. Overlays, shutters, and pixel padding stored in the object are honored by the rendering pipeline — see [2D Viewer Display](dicom-2d-viewer/#image).
{{% /callout %}}

#### DICOM Parametric Map (PMAP)

Single- or multi-frame images whose pixel values represent a derived quantity rather than an acquisition signal — common carriers for AI probability maps, class-activation heatmaps, perfusion (rCBF, rCBV, MTT), diffusion (ADC), and PET-derived metrics.

{{% callout info %}}
Weasis renders Parametric Maps as standard images, including the float and double pixel representations that AI pipelines typically emit. Window/level and LUT controls apply normally — pick a suitable [LUT](lut) to interpret the value range.
{{% /callout %}}

## Image overlays

These objects do not contain a viewable image of their own; they reference a source series and are drawn on top of it.

#### DICOM Segmentation (SEG)

Pixel-based labels produced by segmentation models — anatomical structures, lesions, organs at risk, etc. Each segment is stored as a binary or fractional mask and is independently toggleable in the viewer.

{{% callout info %}}
See [DICOM SEG](dicom-segmentation) for displaying DICOM SEG objects in Weasis, including in MPR and the 3D Volume Renderer.
{{% /callout %}}

#### DICOM RTSTRUCT

Originally designed to describe contours for radiotherapy planning, RTSTRUCT is also used by AI tools that output **vector** geometry instead of pixel masks. Lighter to store than SEG, but inherently 2D per slice.

{{% callout info %}}
See [DICOM RT](dicom-rt) for displaying DICOM RTSTRUCT objects in Weasis.
{{% /callout %}}

[TotalSegmentator](https://github.com/wasserth/TotalSegmentator/) is a good example: starting from version 2, its automatic segmentation of 100+ anatomical structures on CT can be exported as DICOM RTSTRUCT — and, in recent releases, as DICOM SEG as well — both of which load directly in Weasis without any extra configuration.

{{< youtube id="W6MHc3hEqfk" >}}

#### DICOM Presentation States (GSPS)

Grayscale Softcopy Presentation States store the **display intent** for an image — window/level, zoom, rotation — together with vector annotations and measurements. AI tools use them to ship findings as toggleable overlays on the original images rather than baking them into pixels.

{{% callout info %}}
See [DICOM PR](build-ko-pr/#presentation-state-pr-or-gsps) for displaying DICOM Presentation States in Weasis.
{{% /callout %}}

## Reports & documents

These objects carry structured or document content rather than imagery.

#### DICOM Structured Report (SR)

Tree-structured findings: measurements, classifications, observations, and references back to the images they describe. The standard delivery format for AI tools that need to expose interpretable, machine-readable results.

{{% callout info %}}
See [DICOM SR Viewer](dicom-sr).
{{% /callout %}}

#### DICOM Encapsulated Documents

Wrappers for non-image content (PDF, STL, MPEG, plain text…). Useful when an AI pipeline produces a full report or auxiliary artifact that would otherwise live outside the imaging study.

{{% callout info %}}
Encapsulated documents are opened with the system application registered for the document MIME type. The DICOM attributes can be inspected from the thumbnail context menu.

![Open DICOM PDF tags](/tuto/dicom-attributes-pdf.webp?classes=shadow)
{{% /callout %}}