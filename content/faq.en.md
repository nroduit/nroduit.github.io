---
title: FAQs
description: Weasis Frequently Asked Questions
keywords: [ "weasis faqs", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
hidden: true
---

## <center>Frequently Asked Questions</center>

 - [What is Weasis?](#what-is-weasis)
 - [I have questions, what can I do?](#i-have-questions-what-can-i-do)
 - [Can Weasis be used for commercial purposes?](#can-weasis-be-used-for-commercial-purposes)
 - [How to Cite Weasis in a publication?](#how-to-cite-weasis-in-a-publication)
 - [Why is the Weasis license Eclipse Public License?](#why-is-the-weasis-license-eclipse-public-license)
 - [Can Weasis be incorporated in DICOM CDs or other removable media?](#can-weasis-be-incorporated-in-dicom-cds-or-other-removable-media)
 - [How to enable Weasis logging?](#how-to-enable-weasis-logging)
 - [Is it possible to download DICOM files without having a WADO server?](#is-it-possible-to-download-dicom-files-without-having-a-wado-server)

### What is Weasis? ###
Weasis is a standalone and web-based software for visualizing and analyzing images obtained from medical imaging equipment according to the [DICOM standard](https://www.dicomstandard.org/), see [Weasis Medical Viewer](../).

### I have questions, what can I do? ###

For general questions, you can use the [forum](https://groups.google.com/group/dcm4che) or the [GitHub discussions]().

On this website you should find help if you are:
* a person who [integrate Weasis with another system like PACS](../basics/customize/integration/)
* a [developer](../getting-started/#developer-documentation)
* a [user](../tutorials/)

### Can Weasis be used for commercial purposes? ### 
Weasis can be used for commercial purposes as long as the terms of [the license](https://github.com/nroduit/Weasis/blob/master/LICENSE) are respected.

### How to cite Weasis in a publication? ###
Items to include in the citation:
* Author: Nicolas Roduit
* Title: Weasis DICOM viewer
* Version of Weasis
* URL: https://github.com/nroduit/Weasis
* Access Date

Example: Roduit, N. Weasis DICOM viewer. Version 4.1.0. https://github.com/nroduit/Weasis (accessed 5 April 2023).

### Why is the Weasis license Eclipse Public License? ###
The [Eclipse Public License](https://www.eclipse.org/legal/epl-v20.html) is an [OSI approved](https://www.opensource.org) license and a commercially friendly copyleft license.

EPL is more business-friendly about some patent retaliation and reverse engineering clauses than LGPL. With EPL, derivative work (weasis plugin) can be distributed in any license type: open source, freeware, commercial... However, if you distribute Weasis with some modifications (changing existing source code of the open source Weasis plug-ins), even if it is a free distribution, you are obligated to make your modifications available to others.

For more information about EPL, check out the [EPL 2 FAQ](https://www.eclipse.org/legal/epl-2.0/faq.php).

Note that since version 3.7.0 the source code is released in dual license mode ([EPL-2.0 OR Apache-2.0](https://github.com/nroduit/Weasis/blob/master/LICENSE)). This allows the user to choose one of these two licenses.

### Can Weasis be incorporated in DICOM CDs or other removable media? ###

Yes, Weasis can be embedded in a DICOM CD but only on Windows. On other platforms it is possible to create a DCOM CD but without the viewer. See [DICOM Export CD/DVD Image](../tutorials/dicom-export/#cddvd-image).

### How to enable Weasis logging? ###

The rolling log system must be enabled in the preferences to trace all Weasis activities. For more details, see [How to configure and view log files](../tutorials/logging/).


### Is it possible to download DICOM files without having a WADO server? ###

Yes, but a WADO server is recommended. Downloading DICOMs can be achieved by:

- [Building an XML](../basics/customize/integration/#build-an-xml-manifest-no-wado-server) file by using `DirectDownloadFile` and `DirectDownloadThumbnail`:
- Adding the following [command](../basics/commands/#dicomget):<br>
    `$dicom:get -r "http://external.server/images/MRIX_LUMBAR/img1.dcm  http://external.server/images/img2.dcm"`<br>
    Note: This option must be used only for a very limited number of files.
<br>
