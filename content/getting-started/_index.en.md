---
title: Getting Started
keywords: [ "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer", "clinical viewer", "radiolgical viewer", "linux dicom viewer",  "mac dicom viewer" ]
weight: 5
pre: "<b>1. </b>"
---

### Try Weasis now

This new package replaces weasis-portable and no longer requires Java to be installed on the system. It also serves as a basis for launching Weasis from a web context using the [weasis protocol](weasis-protocol).

{{< latest-download "deb" >}}

The easiest way to launch Weasis from a web context is to use <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a>.

{{% notice note %}}
To manage Weasis version at the server side, it is possible to install the [Weasis web package](https://github.com/nroduit/weasis-pacs-connector#installation) which will update the local installation at the client side (it works for minor releases by updating all the plug-ins except the launcher).
{{% /notice %}}

{{% notice tip %}}
Join the <a target="_blank" href="http://groups.google.com/forum/#!forum/weasis">google group</a> (Choose Email to read this group) to stay informed about new releases and updates.
{{% /notice %}}



### General Topics

- [Live demo](../demo) with different DICOM dataset.
- [Weasis Web Protocol](weasis-protocol)
- [Installing Weasis in DCM4CHEE](dcm4chee)
- [Tutorials](../tutorials)
- <a target="_blank" href="http://groups.google.com/group/dcm4che">Weasis Forum</a>
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
- <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#build-weasis-pacs-connector">Building weasis-pacs-connector</a>
- <a target="_blank" href="https://github.com/nroduit/Weasis/issues">Issues on Github</a>
