---
title: "Weasis vs OsiriX, Horos, RadiAnt, 3D Slicer, OHIF"
linkTitle: "Comparison"
description: "How Weasis differs from OsiriX, Horos, 3D Slicer, OHIF, RadiAnt and MicroDicom on platforms, licensing and regulatory status — and when another one fits better."
keywords: [ "dicom viewer comparison", "weasis vs osirix", "osirix alternative windows", "osirix alternative linux", "horos alternative", "3d slicer alternative", "ohif viewer alternative", "radiant dicom viewer alternative", "microdicom alternative", "free dicom viewer comparison", "open source dicom viewer", "web dicom viewer" ]
weight: 45
hidden: true
updated: 2026-09-20
---

## <center>How Weasis compares with other DICOM viewers</center>

People usually arrive at this question with a constraint rather than a preference: a Linux
workstation, a budget of zero, a need for a cleared device, a viewer to hand to a patient. This page
compares the facts that follow from such constraints. It does not rank the viewers — they are built
for different situations, and the one that fits yours may well not be this one.

**What is in the table, and why.** Viewers you can obtain and run **without paying**, that come up in
the same searches and decisions as Weasis, and that are actively maintained. So it mixes open-source
projects with free editions and trials of commercial products — on purpose, because that is what a
reader weighing "free" actually has in front of them, and because what each one costs you in
limitations differs sharply. Subscription-only products are discussed below but not tabulated: their
prices change faster than this page does, and a row that can only say "no" answers nothing.

Every cell below comes from the vendor's or project's own site, checked on 17 September 2026.
Software changes; the links are there so you can re-check rather than take our word for it.

| | Platforms | Licence | Free for professional use |
|---|---|---|---|
| **Weasis** | Windows, macOS, Linux | [EPL-2.0 OR Apache-2.0](https://github.com/nroduit/Weasis/blob/master/LICENSE) | yes |
| **[3D Slicer](https://www.slicer.org/)** | Windows, macOS, Linux (x86-64 and ARM64) | BSD-style | yes |
| **[OHIF Viewer](https://ohif.org/)** | any browser (web) | [MIT](https://ohif.org/), free | yes |
| **[OsiriX Lite](https://www.osirix-viewer.com/)** | macOS | free demo of OsiriX MD | no — capped and feature-limited, see below |
| **[Horos](https://horosproject.org/)** | macOS | [LGPL-3.0](https://horosproject.org/), free and open source | yes |
| **[RadiAnt](https://www.radiantviewer.com/)** | Windows | commercial, time-based licence; the trial is session-limited — see below | no — licence required |
| **[MicroDicom](https://www.microdicom.com/)** | Windows | free for non-commercial use; licence required otherwise | no |

### What each one is built for

A grid of feature checkboxes is the obvious thing to put here, and we deliberately do not maintain one.
Weasis's own capabilities we can state from its documentation; for other people's software we would be
inferring absence from silence on a marketing page, and a wrong "no" about someone else's product is the
worst mistake this page could make. Feature depth for Weasis lives on [Features](features).

What is stable enough to compare is what each project is *for*, in its own terms:

- **Weasis** — reading studies, launched by a PACS, an EHR or a web portal, on all three desktop
  systems.
- **3D Slicer** — analyzing image data: segmentation, registration, Python-driven research pipelines.
- **OHIF** — visualization, analysis and custom workflows that run entirely in a browser.
- **Horos** — free, open-source Mac-native viewing, continuing the OsiriX line.
- **OsiriX Lite** — reviewing your own images on a Mac, and trying what OsiriX MD does.
- **RadiAnt** — Windows desktop reading, licensed per installation.
- **MicroDicom** — opening DICOM files on Windows, free for non-commercial use.

Two of these overlap with Weasis far less than a feature list would suggest. 3D Slicer is the stronger
research platform and the weaker clinical reader; OHIF answers "no installation" rather than "more
capability". Neither is trying to be the other.

### What "free" means in each case

The word covers four different things here, and the difference decides whether a viewer is usable for
real work. Each limitation below is documented by the vendor.

- **Weasis** — free for any use, commercial included, with no feature gate and no session limit. The
  dual licence also permits derivative commercial products.
- **3D Slicer** — free and open source under a BSD-style licence that "does not impose restrictions on
  the use of the software"; its own site invites commercial use. No gate, no limit.
- **OHIF** — free and open source under MIT, and it runs in a browser, so there is nothing to install
  on the workstation at all.
- **OsiriX Lite** — a demo of OsiriX MD. It opens
  [about 800 images of a 512 × 512 series at a time](https://www.osirix-viewer.com/support/faq/), and
  the advanced post-processing belongs to MD. That is enough to look at a study, not to work through a
  large one: a single thin-slice CT will exceed it.
- **Horos** — free and open source under LGPL-3.0, with no feature gate and no time limit.
- **RadiAnt** — the trial has every feature of the paid version, but it is bounded three ways:
  **sessions in unlicensed mode are limited to five minutes**, a red banner sits across the images and
  also appears on anything exported, and the trial period itself expires and has to be reactivated.
  Documented on their
  [forum](https://www.radiantviewer.com/dicom-viewer-forum/use-radiant-without-a-session-limit/1563/)
  and in the [trial documentation](https://www.radiantviewer.com/dicom-viewer-manual/trial-license.html).
- **MicroDicom** — free for non-commercial use only; any professional use needs a licence.

### Choosing between them

Three constraints decide this, and none of them is a feature:

- **Your operating system.** OsiriX and Horos are macOS-only, RadiAnt and MicroDicom Windows-only, OHIF
  runs in a browser. Among desktop viewers only Weasis and 3D Slicer cover
  [Windows](getting-started/windows), [macOS](getting-started/macos) and
  [Linux](getting-started/linux) — irrelevant if your department is on one platform, decisive if it is
  not.
- **What launches it.** If a PACS portal, an EHR or a script has to open the viewer, that is what
  Weasis is shaped around: the [`weasis://` protocol](getting-started/weasis-protocol),
  [PACS and DICOMweb integration](basics/customize/integration), a
  [command interface](basics/commands) for scripting, and a [server-side launcher](viewer-hub).
- **Whether you may modify it.** The dual EPL-2.0 OR Apache-2.0 licence permits derivative commercial
  products, certification included; Horos is LGPL-3.0, which carries different obligations; the
  commercial viewers cannot be modified at all.

**Clearance is the fourth constraint, and deliberately not a column** — none of the viewers compared
here is cleared for primary diagnosis, Weasis included. What that implies for a deployment, and how a
hospital build can be a certified device while this distribution is not, is explained in
[Is Weasis a certified medical device?](faq#is-weasis-a-certified-medical-device)

### See also

- [Features](features) — the full capability list, which this page deliberately does not duplicate.
- [Download Weasis](getting-started/download-dicom-viewer) — if you want to try it against your own
  studies, which beats any table.
