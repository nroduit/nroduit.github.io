---
title: Download Weasis DICOM Viewer
description: List of native installer releases
keywords: [ "download dicom viewer", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer", "clinical viewer", "radiolgical viewer", "linux dicom viewer",  "mac dicom viewer" ]
weight: 9
---

## Installation Methods

* [Manual Installation (Native Installers)](#native-installers)
* [Automatic Updates (Package Managers)](#package-management-systems)

### Prerequisites
Weasis runs on Windows, macOS, and Linux without requiring additional frameworks like Java. However, certain graphics capabilities are needed for [Volume Rendering](../tutorials/dicom-3d-viewer/#requirements).

{{% notice warning %}}
The open-source distribution of Weasis is not a certified medical device (CE or FDA). Any primary diagnostic use requires you to ensure full compliance with the laws and regulations applicable in your jurisdiction.
{{% /notice %}}

### Native Installers

Download standalone installers for manual installation:

{{< latest-download >}}
Linux Compatibility: See the [compatibility matrix](https://repology.org/project/glibc/versions) for GLIBC version requirements and distribution compatibility.

For older releases, visit these repositories:
- **[GitHub Releases](https://github.com/nroduit/Weasis/releases)** ![Github](https://img.shields.io/github/downloads/nroduit/weasis/total?classes=inline "Github release downloads") - Latest releases
- **[SourceForge](https://sourceforge.net/projects/dcm4che/files/Weasis/)** ![Sourceforge](https://img.shields.io/sourceforge/dt/dcm4che/Weasis?classes=inline "Sourceforge release downloads") - Legacy repository (older than v3.5.1)

Stay Updated: Subscribe to our [Google Group](https://groups.google.com/forum/#!forum/weasis) and select "Email" to receive release notifications.


### Package Management Systems

Install via package managers to receive automatic updates.

#### Windows
- **[Microsoft Store](https://www.microsoft.com/en-us/p/weasis/9nhtv46lg4nh)**
- **[Windows Package Manager (winget)](https://github.com/microsoft/winget-pkgs/tree/master/manifests/w/WeasisTeam/Weasis/)**
  ```powershell
  winget install WeasisTeam.Weasis
  ```
- **[Chocolatey](https://community.chocolatey.org/packages/weasis)** ![Chocolatey](https://img.shields.io/chocolatey/dt/weasis?classes=inline "Chocolatey release downloads")
  ```powershell
  choco install weasis
  ```
  *Ideal for enterprise deployment with PowerShell, CHEF, or Puppet*

#### macOS
- **[Homebrew](https://formulae.brew.sh/cask/weasis)** (Intel & Apple Silicon)
  ```bash
  brew install --cask weasis
  ```

#### Linux
- **[Flathub](https://flathub.org/apps/details/io.github.nroduit.Weasis)** (x86_64 & arm64)
  ```bash
  flatpak install flathub io.github.nroduit.Weasis
  ```
- **[Snap Store](https://snapcraft.io/weasis)** (x86_64 & arm64)
  ```bash
  sudo snap install weasis
  ```
- **[Arch Linux (AUR)](https://aur.archlinux.org/packages/weasis-bin/)**
  ```bash
  yay -S weasis-bin
  ```

{{% notice note %}}
**Sandbox Limitations:** Flatpak and Snap packages run in sandboxed environments, which may restrict certain functionalities:
- **Flatpak**: See [Fedora issue](https://github.com/nroduit/Weasis/issues/449#issuecomment-1763311969)
- **Snap**: Limited removable media access ([details](https://github.com/nroduit/Weasis/issues/487#issuecomment-1826293187))

The Snap installation uses `<user.home>/snap/weasis/current/.weasis` instead of the standard `<user.home>/.weasis` directory.
{{% /notice %}}



