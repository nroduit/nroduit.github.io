---
title: FAQs
description: Frequently Asked Questions about Weasis
keywords: [ "weasis faqs", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
hidden: true
---

## <center>Frequently Asked Questions</center>

### Table of Contents
- [What is Weasis?](#what-is-weasis)
- [Where can I ask questions about Weasis?](#where-can-i-ask-questions-about-weasis)
- [Can Weasis be used for commercial purposes?](#can-weasis-be-used-for-commercial-purposes)
- [How to cite Weasis in a publication?](#how-to-cite-weasis-in-a-publication)
- [Why does Weasis use the Eclipse Public License?](#why-does-weasis-use-the-eclipse-public-license)
- [Can Weasis be included in DICOM CDs or other removable media?](#can-weasis-be-included-in-dicom-cds-or-other-removable-media)
- [How do I enable Weasis logging?](#how-do-i-enable-weasis-logging)
- [Can I download DICOM files without a WADO server?](#can-i-download-dicom-files-without-a-wado-server)

### What is Weasis?
Weasis is a standalone and web-based application designed for visualizing and analyzing images obtained from medical imaging equipment according to the [DICOM standard](https://www.dicomstandard.org/). To learn more, visit the [Weasis Medical Viewer](../) page.

### Where can I ask questions about Weasis?
For general questions, you can use the [forum](https://groups.google.com/group/dcm4che) or the [GitHub discussions]().

On this website you should find help if you are:
* a person who [integrate Weasis with another system like PACS](../basics/customize/integration/)
* a [developer](../getting-started/#developer-documentation)
* a [user](../tutorials/)

### Can Weasis be used for commercial purposes?
Weasis is available for commercial use, provided that you comply with the terms outlined in [the license](https://github.com/nroduit/Weasis/blob/master/LICENSE).

### How to cite Weasis in a publication?
When citing Weasis in a publication, include the following details:
- **Author**: Nicolas Roduit
- **Title**: Weasis DICOM Viewer
- **Version**: _Mention the version of Weasis_
- **URL**: https://github.com/nroduit/Weasis
- **Access Date**: _Mention the date you accessed the URL_

**Citation Example**: Roduit, N. Weasis DICOM viewer. Version 4.1.0. https://github.com/nroduit/Weasis (accessed 5 April 2023).

### Why does Weasis use the Eclipse Public License?
The [Eclipse Public License (EPL)](https://www.eclipse.org/legal/epl-v20.html) is a commercially friendly open-source license approved by the [Open Source Initiative (OSI)](https://www.opensource.org). It offers several benefits, including:
1. **Business-friendly clauses**: Compared to LGPL, EPL includes advantageous terms for patent retaliation and reverse engineering.
2. **Flexibility for derivative works**: Plugins and other extensions to Weasis can be distributed under any license (e.g., open source, freeware, or commercial).  
   However, modifications to the existing source code of Weasis plug-ins must be made available to others if distributed.

Since version 3.7.0, Weasis' source code is distributed under a dual license mode: [EPL-2.0 OR Apache-2.0](https://github.com/nroduit/Weasis/blob/master/LICENSE). This allows users to choose the license that best suits their needs.

For more details, refer to the [EPL 2.0 FAQ](https://www.eclipse.org/legal/epl-2.0/faq.php).

### Can Weasis be included in DICOM CDs or other removable media?
Yes, Weasis can be embedded into DICOM CDs, but this feature is only supported on **Windows** platforms. On other platforms, creating a DICOM CD without the viewer is possible. Refer to the tutorial on [DICOM Export CD/DVD Image](../tutorials/dicom-export/#cddvd-image) for more details.

### How do I enable Weasis logging?

To trace Weasis activities, enable the rolling log system in the application preferences. For more details on configuration, refer to the tutorial: [How to configure and view log files](../tutorials/logging/).


### Can I download DICOM files without a WADO server?

Yes, while a WADO server is recommended, downloading DICOM files without one is possible using the following methods:

1. **Building an XML Manifest File**:  
   Use the `DirectDownloadFile` and `DirectDownloadThumbnail` options as described in the [integration guide](../basics/customize/integration/#build-an-xml-manifest-no-wado-server).

2. **Using the `$dicom:get` Command**:  
   Example command:
   ```bash
   $dicom:get -r "http://external.server/images/MRIX_LUMBAR/img1.dcm http://external.server/images/img2.dcm"
   ```
   *Note*: This method is suitable for downloading only a limited number of files and should not be heavily relied upon.
<br>
