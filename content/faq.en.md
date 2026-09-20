---
title: FAQs
description: "Answers to the questions asked most often about Weasis: supported operating systems, web launch, offline use, certification status, licensing and support."
keywords: [ "weasis faq", "dicom viewer faq", "is weasis free", "weasis certified medical device", "dicom viewer questions", "weasis license" ]
hidden: true
---

## <center>Frequently Asked Questions</center>

### Table of Contents
- [What is Weasis?](#what-is-weasis)
- [Which operating systems does Weasis run on?](#which-operating-systems-does-weasis-run-on)
- [Does Weasis require Java or any other framework?](#does-weasis-require-java-or-any-other-framework)
- [Is there a portable version of Weasis?](#is-there-a-portable-version-of-weasis)
- [Does the web launch require Weasis to be installed?](#does-the-web-launch-require-weasis-to-be-installed)
- [Does Weasis need an internet connection?](#does-weasis-need-an-internet-connection)
- [Can Weasis open a DICOM CD or DVD?](#can-weasis-open-a-dicom-cd-or-dvd)
- [Can Weasis open ordinary images such as JPEG or TIFF?](#can-weasis-open-ordinary-images-such-as-jpeg-or-tiff)
- [Which DICOM object types can Weasis display?](#which-dicom-object-types-can-weasis-display)
- [Which DICOM transfer syntaxes and codecs are supported?](#which-dicom-transfer-syntaxes-and-codecs-are-supported)
- [Can Weasis query a PACS directly?](#can-weasis-query-a-pacs-directly)
- [Does Weasis support DICOMweb?](#does-weasis-support-dicomweb)
- [Does Weasis compute SUV values for PET/CT?](#does-weasis-compute-suv-values-for-petct)
- [What does the 3D viewer require?](#what-does-the-3d-viewer-require)
- [Can Weasis convert photos, videos or PDF documents into DICOM?](#can-weasis-convert-photos-videos-or-pdf-documents-into-dicom)
- [Can Weasis print DICOM images?](#can-weasis-print-dicom-images)
- [Is Weasis a certified medical device?](#is-weasis-a-certified-medical-device)
- [Does Weasis de-identify DICOM files?](#does-weasis-de-identify-dicom-files)
- [Where can I ask questions about Weasis?](#where-can-i-ask-questions-about-weasis)
- [How do I report a bug?](#how-do-i-report-a-bug)
- [How do I contribute a translation?](#how-do-i-contribute-a-translation)
- [Can Weasis be used for commercial purposes?](#can-weasis-be-used-for-commercial-purposes)
- [How to cite Weasis in a publication?](#how-to-cite-weasis-in-a-publication)
- [Why does Weasis use the Eclipse Public License?](#why-does-weasis-use-the-eclipse-public-license)
- [Can Weasis be included in DICOM CDs or other removable media?](#can-weasis-be-included-in-dicom-cds-or-other-removable-media)
- [How do I enable Weasis logging?](#how-do-i-enable-weasis-logging)
- [Can I download DICOM files without a WADO server?](#can-i-download-dicom-files-without-a-wado-server)

### What is Weasis?
Weasis is a standalone and web-based application designed for visualizing and analyzing images obtained from medical imaging equipment according to the [DICOM standard](https://www.dicomstandard.org/). To learn more, visit the [Weasis Medical Viewer](../) page.

### Which operating systems does Weasis run on?
Weasis runs on:

- **Windows** — desktop installer or portable archive.
- **macOS** — both Intel and Apple Silicon.
- **Linux** — DEB, RPM, Flatpak, or Snap.

A **web-launch** option is also available — the [Weasis Protocol](getting-started/weasis-protocol) opens the locally installed application from a portal click. See [Download Weasis](getting-started/download-dicom-viewer) for the full installation matrix and platform notes.

### Does Weasis require Java or any other framework?
**No.** The installers bundle everything Weasis needs, so there is no Java runtime to install or maintain. The only external requirement concerns 3D volume rendering, which needs a reasonably modern graphics card — see [Download Weasis](getting-started/download-dicom-viewer) and the [3D viewer requirements](tutorials/dicom-3d-viewer/#requirements).

### Is there a portable version of Weasis?
Yes, on **Windows**: a portable archive is published next to the installer, so Weasis can be unpacked on a USB drive and run without installation or administrator rights — see [Download Weasis](getting-started/download-dicom-viewer).

Getting the viewer **onto the media itself** works one way only: the [DICOM CD/DVD export](tutorials/dicom-export/#cddvd-image) can add that portable distribution to the ISO it writes, so the recipient starts Weasis straight from the disc. This is available **only on Windows x86-64** — both to produce such an ISO and to run the embedded copy. On every other platform the export still writes a DICOM CD, just without a viewer on it; see [Can Weasis be included in DICOM CDs or other removable media?](#can-weasis-be-included-in-dicom-cds-or-other-removable-media)

### Does the web launch require Weasis to be installed?
**Yes.** The web launch is not a browser-only viewer — it uses the [`weasis://` URI scheme](getting-started/weasis-protocol) to hand launch parameters to the **locally installed** Weasis application. Each user must install Weasis once from the [Download page](getting-started/download-dicom-viewer); every subsequent click on a `weasis://...` link (typically generated by a PACS portal, EHR, or [weasis-pacs-connector / ViewerHub](viewer-hub)) then reuses that local install. The previous in-browser Java Web Start distribution was discontinued in version 3.5 for security, configuration, and compatibility reasons.

### Does Weasis need an internet connection?
No — Weasis runs **fully offline** once installed. It opens DICOM files from any local source (file system, USB drive, DICOM CD / DVD, ZIP archive) without network access.

### Can Weasis open a DICOM CD or DVD?
Yes. Weasis reads the **DICOMDIR** of a DICOM CD, DVD or USB drive, and also opens a folder of DICOM files or a ZIP archive — by drag and drop, from the menu, or from the command line. Password-protected ZIP archives are supported on import. See [Import DICOM Files, CDs and Archives](tutorials/dicom-import).

### Can Weasis open ordinary images such as JPEG or TIFF?
Yes. Besides DICOM, Weasis displays TIFF, BMP, GIF, JPEG, JPEG 2000, JPEG-XL, PNG, RAS, HDR and PNM files. If you need those images stored in a PACS rather than only viewed, convert them first with the [Dicomizer](tutorials/dicomizer).

### Which DICOM object types can Weasis display?
Beyond ordinary and multi-frame images, Weasis displays **Enhanced** CT / MR / US volumes, MPEG-2 and MPEG-4, MIME-encapsulated documents such as PDF, [Structured Reports](tutorials/dicom-sr), [Presentation States and Key Object Selection](tutorials/build-ko-pr), [Segmentation](tutorials/dicom-segmentation), [Radiotherapy objects](tutorials/dicom-rt), [waveforms and ECG](tutorials/dicom-ecg), [audio](tutorials/dicom-audio) and Parametric Maps. The full list is on the [Features](features) page.

### Which DICOM transfer syntaxes and codecs are supported?
JPEG (baseline, extended and lossless), **JPEG-LS**, **JPEG 2000**, **JPEG-XL**, RLE and Deflated Explicit VR Little Endian, in addition to the uncompressed syntaxes. The [DICOM Conformance Statement](basics/dicom) lists every transfer syntax and SOP class authoritatively; the [Features](features) page gives the summary.

### Can Weasis query a PACS directly?
Yes. Weasis performs DICOM **Query / Retrieve** with C-FIND, C-GET and C-MOVE, and can also retrieve through WADO-URI. Nodes are configured in the import dialog — see [Import DICOM Files, CDs and Archives](tutorials/dicom-import).

### Does Weasis support DICOMweb?
Yes — **QIDO-RS** to search, **WADO-RS** to retrieve and **STOW-RS** to store, over HTTPS and configurable per source. See [DICOMweb Configuration](tutorials/dicomweb-config), which also lists settings known to work with common providers.

### Does Weasis compute SUV values for PET/CT?
Yes. When a PET or SPECT series is overlaid on a CT or MR base, Weasis reports SUV statistics over a region of interest. See [PET/CT Image Fusion with SUV](tutorials/fusion).

### What does the 3D viewer require?
A graphics card supporting **OpenGL 3.3 or later**: the volume is ray-cast on the GPU with GLSL shaders, and nothing extra has to be installed. From **OpenGL 4.3** a compute-shader backend is used instead, which renders at full resolution while you move the camera. The [3D viewer requirements](tutorials/dicom-3d-viewer/#requirements) section covers the capabilities involved and the settings that trade quality for fluidity.

### Can Weasis convert photos, videos or PDF documents into DICOM?
Yes, with the [Dicomizer](tutorials/dicomizer): photos, scanned reports, videos and 3D models become DICOM objects that an archive can store alongside acquisitions from imaging modalities, with the patient, study and image tags set so they stay searchable. PDF documents are supported {{< since "4.6.2" >}}.

### Can Weasis print DICOM images?
Yes, to an ordinary printer or to a DICOM printer, with a choice of layout and print mode. See [Print DICOM Images](tutorials/print).

### Is Weasis a certified medical device?
**No.** The open-source distribution of Weasis is **not** a certified medical device — it does not carry CE marking and is not FDA cleared. Any **primary diagnostic** use requires you (or your institution) to ensure full compliance with the laws and regulations applicable in your jurisdiction. The full disclaimer is displayed in a dialog **the first time Weasis is launched** and must be explicitly accepted before the application can be used; it is also reproduced on the [Download Weasis](getting-started/download-dicom-viewer) page.

**Being a medical device is a property of a product, not of a code base** — and the same code can be both. At the [University Hospital of Geneva](https://www.hug.ch/en), a variant called **Weasis HUG** is an **in-house medical device**: manufactured and used inside the institution under [article 9 of the Swiss Medical Devices Ordinance (ODim)](https://www.hug.ch/conformite-projets-si), with a quality management system following ISO 13485:2016 and conformity to the general safety and performance requirements of Annex I of the European regulation 2017/745. It is deliberately **not placed on the market and carries no CE marking** — the in-house route covers use within the hospital that manufactures it, and nothing beyond that.

### Does Weasis de-identify DICOM files?
**No — and this matters.** Weasis can hide patient identifiers *on screen* and in what it renders (screenshots, prints, image exports), which is useful for teaching and demonstrations, but that is **not de-identification**: text burned into the image pixels is not removed automatically, and DICOM files exported or sent from Weasis **keep their original attributes**. To de-identify DICOM data properly, use a tool built for it such as [Karnak](https://karnak.weasis.org/). Always review every image before sharing it.

### Where can I ask questions about Weasis?
For general questions, use the [Weasis forum](https://groups.google.com/group/dcm4che) or the [GitHub discussions](https://github.com/nroduit/Weasis/discussions).

This website is organized by audience — start with the section that matches yours:

* **Clinicians and end users** — the [Tutorials](tutorials) section walks through every viewer and feature.
* **Integrators / administrators** — see [Customizing Weasis](basics/customize) and the [PACS integration guide](basics/customize/integration/).
* **Developers** — see the [Developer documentation](getting-started/#developer-documentation).

For the vocabulary itself — MPR, SEG, SR, SUV, DICOMweb — see the [glossary](glossary).

### How do I report a bug?
Open an issue on the [Weasis GitHub issue tracker](https://github.com/nroduit/Weasis/issues). To help the maintainers reproduce the problem, please include:

- The Weasis **version** and your **operating system**.
- A short description of what you did and what happened, with a **screenshot** if relevant.
- The **log files** — set the log level to **DEBUG** or **TRACE**, restart Weasis, reproduce the issue, and attach `boot.log` and the most recent `default.log*` files. See [How to configure and view log files](tutorials/logging/) for the full procedure.

### How do I contribute a translation?
Weasis translations are managed on a community translation platform. To improve an existing language or add a new one, follow the [Translating Weasis](getting-started/translating) guide. End-user instructions for picking the active language are in the [Language & Regional Settings](tutorials/locale) tutorial.

### Can Weasis be used for commercial purposes?
Yes — Weasis is available for commercial use, provided you comply with the terms outlined in [the license](https://github.com/nroduit/Weasis/blob/master/LICENSE).

### How to cite Weasis in a publication?
Cite the software at the version you used — author Nicolas Roduit, title *Weasis DICOM Viewer*, the version, the URL https://weasis.org and the date you retrieved it. [How to cite Weasis](cite) generates ready-made BibTeX, APA, Vancouver and plain-text entries for each release.

### Why does Weasis use the Eclipse Public License?
The [Eclipse Public License (EPL)](https://www.eclipse.org/legal/epl-v20.html) is a commercially friendly open-source license approved by the [Open Source Initiative (OSI)](https://www.opensource.org). It offers several benefits:

1. **Business-friendly clauses** — compared to LGPL, EPL includes more advantageous terms around patent retaliation and reverse engineering.
2. **Flexibility for derivative works** — plugins and other extensions to Weasis can be distributed under any license (open source, freeware, or commercial). However, modifications to the **existing source code** of Weasis or its plugins must be made available to others if distributed.

Since version 3.7.0, the Weasis source code is distributed under a **dual license**: [EPL-2.0 OR Apache-2.0](https://github.com/nroduit/Weasis/blob/master/LICENSE). Users can choose the license that best fits their needs.

For more details, see the [EPL 2.0 FAQ](https://www.eclipse.org/legal/epl-2.0/faq/).

### Can Weasis be included in DICOM CDs or other removable media?
Yes. Weasis can be embedded into a DICOM CD ISO so the recipient can launch it directly from the disc — currently supported on **Windows x86-64 only**. On other platforms, you can still produce a DICOM CD **without the embedded viewer**. See the [CD/DVD Image](tutorials/dicom-export/#cddvd-image) section of the DICOM Export tutorial for the full procedure.

### How do I enable Weasis logging?

To trace Weasis activities, enable the rolling log in the application preferences. See [How to configure and view log files](tutorials/logging/) for the full configuration — including how to share the logs with the maintainers when filing a bug report.


### Can I download DICOM files without a WADO server?

Yes — a WADO server is recommended, but not strictly required. Two alternative paths are supported:

1. **Build an XML manifest file** — use the `DirectDownloadFile` and `DirectDownloadThumbnail` options described in the [integration guide](basics/customize/integration/#build-an-xml-manifest-no-wado-server).

2. **Use the `$dicom:get` command** — point at one or more files by URL:
   ```bash
   $dicom:get -r "http://external.server/images/MRIX_LUMBAR/img1.dcm http://external.server/images/img2.dcm"
   ```
   This works well for a small number of files. For larger studies or production deployments, prefer a proper WADO-RS / DICOMweb server — see [DICOMweb Configuration](tutorials/dicomweb-config).

<br>