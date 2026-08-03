---
title: Features
description: The full list of features supported by the Weasis DICOM viewer.
weight: 3
keywords: [ "dicom viewer features", "weasis features", "mpr", "3d", "mip", "seg", "segmentation", "fusion", "pet/ct", "suv", "rt", "sr", "ecg", "dicomweb", "wado", "stow", "qido", "free dicom viewer" ]
hidden: true
---

## <center>Weasis features</center>

This page lists the features supported by Weasis. For a step-by-step walkthrough of each tool, see the [Tutorials](tutorials).

{{< image-gallery gallery_dir="gallery1" >}}

### Data type support

- Display every common DICOM file, including multi-frame, **Enhanced** (CT / MR / US Volume), MPEG-2, MPEG-4, MIME-encapsulated documents, **[SR](tutorials/dicom-sr)**, **[PR](tutorials/build-ko-pr)**, **[KOS](tutorials/build-ko-pr)**, **[SEG](tutorials/dicom-segmentation)**, **[AU](tutorials/dicom-audio)**, **[RT](tutorials/dicom-rt)**, **[ECG](tutorials/dicom-ecg)**, and **[Parametric Map](tutorials/dicom-artificial-intelligence#dicom-parametric-map-pmap)** (float / double pixels).
- Modern transfer-syntax codecs — JPEG (baseline, extended, lossless), **JPEG-LS**, **JPEG 2000**, **JPEG-XL**, RLE, Deflated Explicit VR Little Endian.
- [Import](tutorials/dicom-import) and [export](tutorials/dicom-export) DICOM CD/DVD with **DICOMDIR**.
- [Import](tutorials/dicom-import) and [export](tutorials/dicom-export) DICOM **ZIP** archives (password-protected supported on import).
- Viewer for common image formats: TIFF, BMP, GIF, JPEG, JPEG 2000, JPEG-XL, PNG, RAS, HDR, PNM.

### Importing & exporting

- **[DICOM Query / Retrieve](tutorials/dicom-import)** — C-FIND, C-GET, C-MOVE, WADO-URI.
- **[DICOMweb](tutorials/dicomweb-config)** — QIDO-RS, WADO-RS, STOW-RS over HTTPS, configurable per source.
- **[Send / Export](tutorials/dicom-export#exporting)** — store to a PACS or DICOMweb server (C-STORE or STOW-RS); export locally as DICOMDIR ZIP, ISO image (with Weasis embedded on Windows x86-64), TIFF, JPEG, PNG, AVI / MP4.
- **[Manifest-driven loading](basics/customize/integration)** — supports XML manifests including `DirectDownloadFile` / `DirectDownloadThumbnail` for environments without a WADO server.
- **`weasis://` [protocol](getting-started/weasis-protocol)** — single-click launch from web portals, EHR / RIS / HIS systems.
- Save measurements and annotations as **[DICOM Presentation States (GSPS)](tutorials/build-ko-pr)** or XML files.

### Viewing & image rendering

- Multi-monitor support with **[per-monitor calibration](tutorials/zoom#real-world-size-display)**, **[HiDPI](tutorials/theme#how-to-scale-the-user-interface)** awareness, full-screen mode.
- Image manipulation with the mouse (pan, zoom, windowing, rotation, scroll, crosshair) and **[customizable keyboard shortcuts](basics/shortcuts)**.
- Full **[DICOM rendering pipeline](tutorials/lut)**: Modality LUT, VOI LUT, LUT Shape (linear / sigmoid / logarithmic / non-linear), Presentation LUT.
- **[Pseudo-color](tutorials/lut)** LUTs ordered by modality with preview.
- **[DICOM Presentation States (GSPS)](tutorials/build-ko-pr)** with graphic overlays.
- **[DICOM Overlays](tutorials/dicom-2d-viewer#display)**, **Shutters**, and **Pixel Padding**.
- **Lossy-compression indicator** in the [information layer](tutorials/dicom-2d-viewer#display); visible warnings when the volume has geometry issues (irregular slice spacing, non-parallel slices, gantry tilt).
- **[Per-view synchronization](tutorials/synch-view)** with explicit per-action overrides; **[FrameOfReferenceUID-aware](tutorials/synch-view#frame-of-reference)** grouping (orphan views are excluded from auto-sync to prevent comparing unrelated anatomy).
- **[Manual synchronization](tutorials/synch-view#manual-sync-button)** as a fallback for views that don't share a Frame of Reference, linked by relative slice index.

### Advanced imaging

- **[Oblique Multi-Planar Reconstruction (MPR)](tutorials/mpr)** with **gantry-tilt correction** (backward mapping + trilinear interpolation) and 3D matrix transformations for non-standard patient positioning.
- **[Curved MPR (CPR)](tutorials/mpr-curved)** — trace a curve on the **axial** plane, typically the dental arch on a cone-beam CT, to build a **panoramic** view and **cross-sectional** slices.
- **[Maximum Intensity Projection](tutorials/mip) (MIP / MinIP / Mean IP)** available in the 2D, MPR and 3D views.
- **[3D Volume Rendering](tutorials/dicom-3d-viewer)** with presets, an **editor for custom Volume LUTs**, and five [segmentation modes](tutorials/dicom-segmentation#segmentation-overlay-in-the-3d-volume-renderer) — overlay, segmentation only, and two **masks** that keep or remove the voxels inside the visible regions.
- **[DICOM Segmentation (SEG)](tutorials/dicom-segmentation)** overlaid in 2D, MPR, and 3D — **BINARY**, **FRACTIONAL**, and **LABELMAP** types, with per-region visibility, color, opacity, volume and statistics, **Show all / Hide all** (**Alt + S**), and non-diagnostic segments (table, couch) hidden on load.
- **[PET/CT fusion](tutorials/fusion)** — overlay a **PET** or **SPECT** series on its **CT** / **MR** base, in the 2D and MPR viewers, with a SUV display window and an on-image [color scale](tutorials/fusion#color-scale).
- **[DICOM RT](tutorials/dicom-rt)** — RTSTRUCT contours, RTDOSE isodose grid, and DVH chart (with optional on-the-fly DVH computation for missing structures).
- **[4D / multi-phase series](tutorials/dicom-explorer#4d-splitting)** — automatic split into per-phase sub-series, with a confirmation dialog beyond 8 phases, ready for MPR / MIP / VR.
- **[3D cursor (crosshair)](tutorials/cursor-3d)** and **cross-lines** linked through the Frame of Reference.
- **[Persistent magnifier glass](tutorials/zoom)** with freeze options for side-by-side parameter comparison.
- [Layouts](tutorials/docking) for comparing series, studies, or modalities side-by-side.

### Measurement & annotation tools

- **[Measurement tools](tutorials/draw-measure#measurement-tools)** — line, polyline, perpendicular and parallel lines, angle (incl. **Cobb angle**), rectangle, ellipse, polygon and free-hand shapes, drawn at any angle and editable point by point.
- **[Region statistics](tutorials/draw-measure#selected-measurement)** of pixels (Min, Max, Mean, StDev, Skewness, Kurtosis, Entropy).
- **[OMBB](tutorials/draw-measure#measurement-tools)** (Oriented Minimum Bounding Box) for polygon length / width / orientation.
- **[Histogram](tutorials/histogram)** of modality values, including per-region histograms.
- **SUV** measurement (PET / nuclear medicine), body-weight method (SUVbw), QIBA-compliant — also on a [fused](tutorials/fusion#suv) PET/CT view.
- **[Volume and voxel count](tutorials/dicom-segmentation#region-info)** of segmented regions, with pixel statistics inside a region.
- **[Pixel-info inspector](tutorials/dicom-2d-viewer#display)** (raw value, modality value, presentation value).

### Specific viewers

- **[DICOM ECG](tutorials/dicom-ecg)** — display all DICOM waveforms with interactive measurements.
- **[DICOM SR](tutorials/dicom-sr)** — Structured Report viewer with hyperlinks to images and associated graphics; standard graphic types (POINT, MULTIPOINT, POLYLINE, CIRCLE, ELLIPSE) plus compound types (MULTILINE, RULER, ARROW, RECTANGLE).
- **[DICOM AU](tutorials/dicom-audio)** — audio player with export to WAV.
- **[DICOM RT tools](tutorials/dicom-rt)** for radiotherapy: RTSTRUCT, RTPLAN, RTDOSE, DVH chart.

### AI / quantitative imaging

- Renders every common AI-produced DICOM object — **SEG**, **RTSTRUCT**, **PR / GSPS**, **SR**, **Parametric Maps** — with consistent overlays across 2D, MPR, and 3D. See the [AI DICOM Objects](tutorials/dicom-artificial-intelligence) page for the complete map of AI outputs to Weasis displays.
- Float and double pixel data supported throughout the windowing / LUT pipeline.

### Security & quality

- **Authentication & transport** — Basic auth, OAuth 2.0, and **OpenID Connect** (Authorization Code with PKCE and loopback redirect, RFC 8252) — works against Keycloak, Google Cloud Healthcare, and any compliant OIDC provider; HTTPS for transport; **code-signed installers**.
- **Supply chain** — SBOM-tracked dependencies, continuous CVE monitoring.
- **Static analysis** — every build scanned by [SonarCloud](https://sonarcloud.io/dashboard?id=org.weasis%3Aweasis-framework) for reliability, maintainability, and security ratings; quality gate enforced on the main branch.
- **Upstream libraries** — `weasis-core-img` and `weasis-dicom-tools` maintain their own ISO 14971-style risk-coverage matrices.
- See [Is Weasis a certified medical device?](faq#is-weasis-a-certified-medical-device) for the certification disclaimer.

### Other tools

- **[Dicomizer](tutorials/dicomizer)** — convert standard images, videos, PDFs, and STL meshes into DICOM, with worklist-driven metadata, video-size validation, and per-modality presets.
- **[DICOM printing](tutorials/print)** — both standard printers and DICOM film printers.
- **[Key Object Selection](tutorials/build-ko-pr)** — flag key images with the star button, filter scrolling to those images, export as a standard KO object.
- **[DICOM attributes](tutorials/tags)** — display and full-text search across every tag in the file.
- **[Third-party launcher](tutorials/launcher-external)** — hand off the current study (or its downloaded folder) to any external application, with dynamic placeholders such as `{tag:AccessionNumber}` or `{dicom:wado.folder}`.
- **[Multi-language UI](tutorials/locale)** with 20+ translations contributed by the community.
- **Plugin architecture** — the OSGi-based plug-in model lets vendors and research groups ship their own viewers and tools alongside Weasis (see [Build plug-ins](basics/customize/build-plugins)).

{{< image-gallery gallery_dir="gallery2" >}}