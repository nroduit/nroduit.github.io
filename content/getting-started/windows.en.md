---
title: "DICOM Viewer on Windows"
linkTitle: "Windows"
description: "Install the Weasis DICOM viewer on Windows — MSI, portable archive, Store, winget or Chocolatey — plus requirements and Windows-specific behavior."
keywords: [ "dicom viewer windows", "weasis windows", "dicom viewer windows 11", "winget weasis", "chocolatey weasis", "portable dicom viewer windows", "dicom cd viewer windows", "msi installer" ]
weight: 10
---

## <center>Weasis on Windows</center>

Weasis runs natively on Windows with nothing else to install — no Java runtime, no browser plugin.
Everything on this page is specific to Windows; the installers themselves, with their sizes and
checksums, are on [Download Weasis](download-dicom-viewer).

### Ways to install

| Method | When it fits |
|---|---|
| **MSI installer** | a single machine, or deployment through your usual software management |
| **Portable archive** | a USB drive, or a machine where you have no administrator rights |
| **Microsoft Store** | unmanaged machines that should update themselves |
| **winget** — `winget install WeasisTeam.Weasis` | scripted installs, fleets |
| **Chocolatey** — `choco install weasis` | fleets driven by PowerShell, CHEF or Puppet |

The MSI and the package managers register the `weasis://` scheme, which is what lets a PACS portal
or an EHR open a study in one click — see the [Weasis Web Protocol](weasis-protocol).

### Requirements

Windows 10 or later on x86-64. The 2D viewers need nothing more; the
[3D viewer](../tutorials/dicom-3d-viewer/#requirements) needs a graphics card with **OpenGL 3.3 or
later**, and reaches its faster compute-shader path from OpenGL 4.3.

### What differs on Windows

- **File associations cover `.dcm` only.** DICOM files without an extension — common on media
  produced by modalities — are *not* associated with Weasis on Windows, though they are on macOS and
  Linux. Open them through the [import dialog](../tutorials/dicom-import) or by drag and drop.
- **Windows is the only platform that can embed the viewer in a DICOM CD.** The
  [CD/DVD export](../tutorials/dicom-export/#cddvd-image) can write an ISO carrying the portable
  distribution, so the recipient starts Weasis from the media. Producing *and* running such an ISO
  is Windows x86-64 only; elsewhere the export writes a DICOM CD without a viewer.
- **Video playback depends on the system player.** DICOM MPEG-2 objects opened with the default
  Windows player may fail, because Windows Media Player ships without an MPEG-2 codec — install VLC
  or another player if that happens.
- **Long launch URLs can be truncated by the browser.** When a DICOMweb launch carries a long
  access token in the URL, only Firefox handles it reliably on Windows. Passing the token in a
  header, through [weasis-pacs-connector or ViewerHub](../basics/customize/dicomweb-archives),
  avoids the problem altogether.

### Other platforms

[macOS](macos) · [Linux](linux)
