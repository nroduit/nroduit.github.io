---
title: Download Weasis DICOM Viewer
description: List of native installer releases
keywords: [ "download dicom viewer", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer", "clinical viewer", "radiolgical viewer", "linux dicom viewer",  "mac dicom viewer" ]
weight: 9
---

### Package management systems

Get automatic updates for Weasis by installing it via these package management systems:

#### Windows
- [Microsoft Windows store](https://www.microsoft.com/en-us/p/weasis/9nhtv46lg4nh)
- [Windows Package Manager (winget)](https://github.com/microsoft/winget-pkgs/tree/master/manifests/w/WeasisTeam/Weasis/)
- [Chocolatey Community Repository](https://community.chocolatey.org/packages/weasis) ![Chocolatey](https://img.shields.io/chocolatey/dt/weasis?classes=inline "Chocolatey release downloads")<br>
  (Ideal for Windows deployment with PowerShell, CHEF, Puppet...)

#### macOS
- [Homebrew Formulae](https://formulae.brew.sh/cask/weasis) (Supports both Intel and Apple Silicon architectures)

#### Linux
- [Flathub repository](https://flathub.org/apps/details/io.github.nroduit.Weasis) Flatpak package for x86_64 and arm64 architectures)
- [Snapcraft: The app store for Linux](https://snapcraft.io/weasis) (Snap package for x86_64 and arm64 architectures)
- [Arch Linux repository](https://aur.archlinux.org/packages/weasis-bin/)
- [Gentoo repository](https://gpo.zugaina.org/media-gfx/weasis-bin)

{{% notice warning %}}
The package management systems above can limit certain functionalities because they work in sandbox mode, especially for Flatpak (see [Fedora issue](https://github.com/nroduit/Weasis/issues/449#issuecomment-1763311969)) and Snap (see [removable media issue](https://github.com/nroduit/Weasis/issues/487#issuecomment-1826293187)). 

The Snap package installation uses a `<user.home>/snap/weasis/current/.weasis` directory instead of the `<user.home>/.weasis` directory for all other installations.
{{% /notice %}}

### List of All Installers

All the packages can be found on [Github](https://github.com/nroduit/Weasis/releases) ![Github](https://img.shields.io/github/downloads/nroduit/weasis/total?classes=inline "Github release downloads") and the legacy repository [Sourceforge](https://sourceforge.net/projects/dcm4che/files/Weasis/) ![Sourceforge](https://img.shields.io/sourceforge/dt/dcm4che/Weasis?classes=inline "Sourceforge release downloads")

For details about GLIBC versions and Linux distribution compatibility, see this [page](https://repology.org/project/glibc/versions).
{{< old-download >}}
