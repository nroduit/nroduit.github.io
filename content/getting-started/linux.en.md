---
title: "DICOM Viewer on Linux"
linkTitle: "Linux"
description: "Install the Weasis DICOM viewer on Linux — DEB, RPM, Flatpak, Snap or AUR — plus the GLIBC requirements and what the Flatpak and Snap sandboxes restrict."
keywords: [ "dicom viewer linux", "weasis linux", "dicom viewer ubuntu", "dicom viewer fedora", "flatpak dicom viewer", "snap dicom viewer", "dicom viewer arm64", "aur weasis" ]
weight: 13
---

## <center>Weasis on Linux</center>

Weasis ships as a native package for the common distributions and as a sandboxed Flatpak or Snap.
Everything on this page is specific to Linux; the packages themselves are on
[Download Weasis](download-dicom-viewer).

### Ways to install

| Method | When it fits |
|---|---|
| **DEB / RPM** | Debian, Ubuntu, Fedora, RHEL and relatives — full access to the file system |
| **Flatpak** — `flatpak install flathub io.github.nroduit.Weasis` | any distribution, x86-64 and arm64, sandboxed |
| **Snap** — `sudo snap install weasis` | any distribution with snapd, x86-64 and arm64, sandboxed |
| **AUR** — `weasis-bin` | Arch and derivatives |

The packages ship a desktop entry that declares the `weasis://` scheme, so a link from a PACS
portal or an EHR opens the locally installed viewer — see the
[Weasis Web Protocol](weasis-protocol). You can check it from a terminal with
`xdg-open "weasis://?…"`.

### Requirements

The native packages need **GLIBC 2.17** on x86-64 and **GLIBC 2.27** on arm64. The
[GLIBC version matrix](https://repology.org/project/glibc/versions) tells you what your distribution
provides. The [3D viewer](../tutorials/dicom-3d-viewer/#requirements)
needs a graphics card with **OpenGL 3.3 or later**, and reaches its faster compute-shader path from
OpenGL 4.3 — which on Linux depends on the driver you have installed, not only on the card.

### What differs on Linux

- **Sandboxes restrict what Weasis can reach.** The Flatpak and Snap builds run confined, which
  matters for a viewer that reads removable media: the Snap has
  [limited access to removable media](https://github.com/nroduit/Weasis/issues/487#issuecomment-1826293187),
  and the Flatpak has [its own restrictions](https://github.com/nroduit/Weasis/issues/449#issuecomment-1763311969).
  If you routinely open DICOM CDs or USB drives, prefer the DEB or RPM package.
- **The Snap keeps its configuration elsewhere.** It uses
  `<user.home>/snap/weasis/current/.weasis` instead of `<user.home>/.weasis`, which is where to look
  for preferences and for [log files](../tutorials/logging).
- **Extension-less DICOM files are associated** with Weasis, as on macOS and unlike on Windows.
- **Embedding the viewer in a DICOM CD is not available.** The
  [CD/DVD export](../tutorials/dicom-export/#cddvd-image) writes a DICOM CD from Linux, but only
  Windows x86-64 can add the viewer to the ISO.

### Other platforms

[Windows](windows) · [macOS](macos)
