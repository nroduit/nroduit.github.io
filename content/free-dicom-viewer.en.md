---
title: "Weasis: a free DICOM Viewer"
Description: "Documentation of Weasis - A free application for displaying medical images"
keywords: [ "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer", "clinical viewer", "radiolgical viewer", "linux dicom viewer",  "mac dicom viewer" ]
hidden: true
---


Weasis is a multipurpose standalone and web-based DICOM viewer designed with a highly [modular architecture](../basics/architecture). It is a very popular clinical viewer used in healthcare by hospitals, health networks, multicenter research trials, and by patients.

As free/libre and open source software ([FLOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software)), Weasis is cross-platform, [multi-language](https://explore.transifex.com/weasis/weasis/), and supports [flexible integration with PACS, RIS, HIS, or PHR systems](../basics/customize/integration). The viewer is compatible with Windows, Linux, and macOS across various processor architectures (see the [available download packages](../getting-started/download-dicom-viewer)).

Leveraging the [OpenCV](https://opencv.org) library, Weasis delivers high-performance and high-quality medical imaging renderings.

From version 4 onwards, Weasis features [a responsive user interface](../tutorials/theme/#how-to-scale-the-user-interface) aligned with operating system options, offering an enhanced experience on high-resolution screens.


{{< image-gallery gallery_dir="gallery1" >}}

Weasis has been designed to meet the evolving needs of clinical information systems in medical imaging. Its features focus on providing web-based access to radiological images, supporting a wide range of DICOM types, and offering multimedia capabilities.

### Key Viewer Features (see also [Tutorials](../tutorials))

- **Data type support**
    - Weasis provides a highly detailed implementation of the DICOM standard, enabling effortless display and interaction with most types of DICOM files.
    - Display most DICOM files including multi-frame, enhanced, MPEG-2, MPEG-4, MIME Encapsulation, DOC, SR, PR, KOS, SEG, AU, RT, and ECG
    - Display DICOM image containing float or double data (Parametric Map)
    - Import DICOM files with DICOM Query/Retrieve (C-GET, C-MOVE, and WADO-URI) and DICOMWeb (QUERY and RETRIEVE)
    - Import and export DICOM CD/DVD with DICOMDIR
    - Import and export DICOM ZIP files
    - Viewer for common image formats (TIFF, BMP, GIF, JPEG, PNG, RAS, HDR, and PNM)

- **Exporting data**
    - Export DICOM files locally with several options (DICOMDIR, ZIP, ISO image file with Weasis, TIFF, JPEG, PNG...)
    - Send DICOM files to a remote PACS or DICOMWeb server (C-STORE or STOW-RS)
    - Save measurements and annotations in DICOM Presentation States or XML file

- **Viewing and image rendering**
    - Support of several screens with different calibration, support of HiDPI (High Dots Per Inch) monitors, full-screen mode
    - Image manipulation with mouse buttons  (pan, zoom, windowing, rotation, scroll, crosshair)
    - Support of DICOM Modality LUTs, VOI LUTs, LUT Shapes, and Presentation LUTs (even non-linear)
    - Apply DICOM Presentation States (GSPS) and display graphics as overlays
    - Support DICOM Overlays, Shutters, and DICOM Pixel Padding
    - Volume rendering with 3D presets
    - Layouts for comparing series or studies
    - Advanced series synchronization options
    - Display cross-lines
    - 3D cursor
    - Oblique Multi-planar Reconstruction (MPR)
    - Maximum Intensity Projection
    - Persistent magnifier glass

- **Measurement and annotation tools**
    - Length, area, and angle measurement
    - Region statistics of pixels (Min, Max, Mean, StDev, Skewness, Kurtosis, Entropy)
    - Histogram of modality values
    - SUV measurement

- **Specific viewers**
    - DICOM ECG: display all the DICOM waveforms and allow to make some measurements
    - DICOM SR: structured report viewer with hyperlinks to images and associated graphics
    - DICOM AU: audio player (allow to export to WAV files)

- **Other tools**
    - Dicomizer module to convert standard images into DICOM
    - Printing views to DICOM and system printers
    - Apply and Create DICOM Key Object Selection by selecting images with the star button
    - Display and search into all DICOM attributes
    - DICOM RT tools for radiotherapy: display RT structure set, dose, and DVH chart

{{< image-gallery gallery_dir="gallery2" >}}
