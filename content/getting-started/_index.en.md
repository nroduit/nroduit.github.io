---
title: Getting Started
keywords: [ "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer", "clinical viewer", "radiolgical viewer", "linux dicom viewer",  "mac dicom viewer" ]
weight: 5
pre: "<b>1. </b>"
---

### Try Weasis now

These native installers below replace the weasis-portable.zip package (still available [here](https://sourceforge.net/projects/dcm4che/files/Weasis/) until version 4.0) and no longer requires Java to be installed on the system. It also serves as a basis for launching Weasis from a web context using the [weasis protocol](weasis-protocol). See below the differences between the [weasis distributions](#weasis-distributions).

{{< latest-download "deb" >}}

See this [page](download) for getting the list of all the packages to download and other Websites distibuting Weasis.<br>
For more information about [the GLIBC versions regarding the life cylcle of the different Linux distributions](https://gist.github.com/wagenet/35adca1a032cec2999d47b6c40aa45b1#file-glibc-md).

{{% notice note %}}
To manage Weasis version at the server side, it is possible to install the [Weasis web package](https://github.com/nroduit/weasis-pacs-connector#installation) which will upgrade the native installation at the client side (it works for minor releases by updating all the plug-ins except the launcher).<br>
The different possibilities for integrating Weasis with other systems are described [here](../basics/customize/integration).
{{% /notice %}}

{{% notice tip %}}
Join the [google group](http://groups.google.com/forum/#!forum/weasis) (Choose Email to read this group) to stay informed about new releases and updates.
{{% /notice %}}

### General Topics

- [Live demo](../demo) with different DICOM dataset.
- [Weasis Web Protocol](weasis-protocol)
- [Installing Weasis in DCM4CHEE](dcm4chee)
- [Tutorials](../tutorials)
- [Weasis Forum](http://groups.google.com/group/dcm4che)
- [Frequently Asked Questions (FAQs)](../faq)
- [Dicom Conformance and IHE](../basics/dicom)
- [Get Involved!](../get-involved)

### Developer Documentation

- [Building Weasis from source](building-weasis)
- [Weasis Architecture](../basics/architecture)
- [Weasis Plug-in Development Guidelines](guidelines)
- [How to build and install a plug-in](../basics/customize/build-plugins)
- [How to launch Weasis from any environments](../basics/customize/integration)
- [Translating Weasis Plug-ins](translating)
- [Weasis Preferences](../basics/customize/preferences)
- [Building weasis-pacs-connector](https://github.com/nroduit/weasis-pacs-connector#build-weasis-pacs-connector) 
- [Issues on Github](https://github.com/nroduit/Weasis/issues)


