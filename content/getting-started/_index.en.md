---
title: Getting Started
keywords: [ "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer", "clinical viewer", "radiological viewer", "linux dicom viewer",  "mac dicom viewer" ]
weight: 5
pre: "<b>1. </b>"
---

### Try Weasis now

Visit the [Download Page](download-dicom-viewer) for a comprehensive list of installation options adapted to your system.<br>

Since version 4, only the distribution with a native installer is maintained to ensure a better user experience in terms of installation, configuration and compatibility. This distribution also supports launching **Weasis from a web context** via the [weasis protocol](weasis-protocol).

{{< latest-download "deb" >}}

For details about GLIBC versions and Linux distribution compatibility, see this [page](https://repology.org/project/glibc/versions).

{{% notice note %}}
To manage Weasis version at the server side, it is possible to install the [Weasis web package](https://github.com/nroduit/weasis-pacs-connector#installation) which will upgrade the native installation at the client side (it works for minor releases by updating all the plugins except the launcher).<br>
Explore more integration possibilities with other systems [here](../basics/customize/integration).
{{% /notice %}}

{{% notice tip %}}
Stay informed about new releases and updates by joining our [Google Group](https://groups.google.com/forum/#!forum/weasis). Choose "Email" to get updates directly to your inbox.
{{% /notice %}}

### General Topics

Get started with these links to learn more about Weasis and its features:
- **[Live Demo](../demo):** Explore Weasis with a variety of DICOM datasets.
- **[Weasis Web Protocol](weasis-protocol):** Learn how to launch Weasis directly from web links or network-based workflows.
- **[Installing Weasis in DCM4CHEE](dcm4chee):** Step-by-step guide to integrating Weasis with DCM4CHEE PACS.
- **[Tutorials](../tutorials):** Comprehensive tutorials to help you get the most out of Weasis.
- **[Weasis Forum](https://groups.google.com/group/dcm4che):** Join discussions and get support directly from the community.
- **[Frequently Asked Questions (FAQs)](../faq):** Find quick answers to common questions about using Weasis.
- **[Dicom Conformance and IHE](../basics/dicom):** Understand how Weasis aligns with DICOM standards and IHE integration.
- **[Get Involved!](../get-involved):** Learn how to contribute to the Weasis project.

### Developer Documentation
Dive into advanced topics and technical resources for developers:
- **[Building Weasis from source](building-weasis)**
- **[Weasis Architecture](../basics/architecture)**
- **[Weasis Plugin Development Guidelines](guidelines)**
- **[How to build and install a plugin](../basics/customize/build-plugins)**
- **[How to launch Weasis from any environments](../basics/customize/integration)**
- **[Translating Weasis Plugins](translating)**
- **[Weasis Preferences](../basics/customize/preferences)**
- **[Building weasis-pacs-connector](https://github.com/nroduit/weasis-pacs-connector#build-weasis-pacs-connector)**
- **[Report Issues on GitHub](https://github.com/nroduit/Weasis/issues)**


