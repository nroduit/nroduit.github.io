---
title: "DICOM Viewer on macOS"
linkTitle: "macOS"
description: "Install the Weasis DICOM viewer on macOS — PKG for Intel and Apple Silicon, or Homebrew — plus the requirements and the behavior specific to macOS."
keywords: [ "dicom viewer mac", "dicom viewer macos", "weasis macos", "dicom viewer apple silicon", "homebrew weasis", "dicom viewer m1 m2", "free dicom viewer mac" ]
weight: 12
---

## <center>Weasis on macOS</center>

Weasis runs natively on both Intel and Apple Silicon Macs, with nothing else to install. Everything
on this page is specific to macOS; the installers themselves are on
[Download Weasis](download-dicom-viewer).

### Ways to install

| Method | When it fits |
|---|---|
| **PKG installer** | a single machine — separate builds for Intel and Apple Silicon |
| **Homebrew** — `brew install --cask weasis` | machines you already manage with Homebrew; one cask covers both architectures |

Either way the `weasis://` scheme is registered, which is what lets a portal or an EHR open a study
in one click — see the [Weasis Web Protocol](weasis-protocol).

### Requirements

macOS 11 or later on Intel, macOS 12 or later on Apple Silicon. The
[3D viewer](../tutorials/dicom-3d-viewer/#requirements) needs **OpenGL 3.3 or later**, which every
supported Mac provides.

### What differs on macOS

- **Shortcuts use Cmd where the documentation says Ctrl.** Holding **Cmd** while drawing a line
  opens the calibration dialog, and the same substitution applies throughout the
  [shortcut list](../basics/shortcuts).
- **The 3D viewer always uses the fragment-shader backend.** macOS caps OpenGL at 4.1, so volume
  rendering runs on the FBO path (OpenGL 3.3 – 4.2) rather than the compute-shader one. In practice
  that means slightly different performance behavior: while you drag the camera the volume is
  ray-cast at the logical window resolution and upscaled {{< since "4.7.3" >}}, which on a Retina
  display is a quarter of the pixels, and the full-resolution frame is drawn as soon as you release.
  See the [3D viewer requirements](../tutorials/dicom-3d-viewer/#requirements).
- **The Dicomizer is started from the terminal.** Run the `Dicomizer` command as described in the
  [Dicomizer tutorial](../tutorials/dicomizer); if you use it often, wrap that command in a
  `Dicomizer.app` with Automator's *Run Shell Script* action.
- **Extension-less DICOM files are associated** with Weasis, unlike on Windows — media written by a
  modality usually opens by double-click.
- **Embedding the viewer in a DICOM CD is not available.** The
  [CD/DVD export](../tutorials/dicom-export/#cddvd-image) writes a DICOM CD from macOS, but only
  Windows x86-64 can add the viewer to the ISO.

### Other platforms

[Windows](windows) · [Linux](linux)
