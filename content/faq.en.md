---
title: FAQs
description: Weasis Frequently Asked Questions
keywords: [ "weasis faqs", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
disableToc: true
---

## <center>Frequently Asked Questions</center>
<br>
{{%expand " Why is the Weasis license Eclipse Public License?" %}}
The <a target="_blank" href="http://www.eclipse.org/legal/epl-v20.html">Eclipse Public License</a> is an <a target="_blank" href="http://www.opensource.org">OSI approved</a> license and a commercially friendly copyleft license.

EPL is more business-friendly about some patent retaliation and reverse engineering clauses than LGPL. With EPL, derivative work (weasis plugin) can be distributed in any license type: open source, freeware, commercial... However, if you distribute Weasis with some modifications (changing existing source code of the open source Weasis plug-ins), even if it is a free distribution, you are obligated to make your modifications available to others.

For more information about EPL, check out the <a target="_blank" href="http://www.eclipse.org/legal/epl-2.0/faq.php">EPL 2 FAQ</a>.
{{% /expand%}}
<br>
{{%expand "Can Weasis be incorporated in DICOM CDs or other removable media?" %}}
Yes, the Weasis portable version can be copied in DICOM CD-ROMs as a multi-platform stand-alone viewer with launchers for Mac OS X, Linux and Windows. The viewer requires that a Java Runtime Environment (JRE 8 or greater) be installed on the machine to run. If Java is not installed on Windows, a dialog will propose to install it from the Internet.

{{% notice tip %}}
The executable (viewer-win32.exe) allows to embed a JRE in the relative directory "jre/windows" (_e.g. weasis-portable/jre/windows/bin/java.exe_). To support 32 and 64-bit architecture, copy 32-bit Java Runtime from its installed directory.<br>
**Note**: the embedded Java Runtime is used only when no runtime is available on the system. When Java is run from CD, it could be a little slow.
{{% /notice %}}

The viewer loads automatically images from DICOMDIR or from directories configured in "weasis/conf/config.properties (by default `weasis.portable.dicom.directory=dicom,DICOM,IMAGES,images`).

For burning studies with Weasis, and additionnal plugin must be activated. In the web distribution, add weasis-ext.war. In the portable distribution, 1) uncompress weasis-ext.war, 2) copy weasis-isowriter-x.x.x.jar into weasis-portable/weasis/, 3) replace the file conf/ext-config.properties, 4) edit ext-config.properties and modify ${weasis.codebase.ext.url} by ${weasis.codebase.url}

For burning Weasis with dcm4chee-cdw, look at [Write weasis-portable to DICOM CDs with dcm4chee-cdw](../old/dcm4chee/#write-weasis-portable-to-dicom-cds-with-dcm4chee-cdw).
{{% /expand%}}
<br>
{{%expand "How to enable Weasis logging?" %}}
Logs are available either in Weasis log files (in ${user.home}/.weasis/log) or in the Java console (only with Java Webstart).

1. By displaying the Java console (not compatible with the Weasis native installer):
    * <a target="_blank" href="http://www.java.com/en/download/help/javaconsole.xml">Windows</a>
    * <a target="_blank" href="http://www.java.com/en/download/help/enable_console_linux.xml">Linux</a>
    *  Mac:
        1. Navigate to the following folder: Applications > Utilities > Java.
        1. Click the Java Preferences icon and then the Advanced tab.
        1. Under the Java console section, select the Show console radio button.

2. By writing to log files:
    - Logging can be activated in Weasis from *File > Preferences > General*
    - The default logging configuration comes from config.properties or ext-config.properties, see [Weasis Preferences](../basics/customize/preferences).

{{% /expand%}}
<br>
{{% expand "Is it possible to download DICOM files without having a WADO server?" %}}
Yes, but a WADO server is recommended. Downloading DICOMs can be achieved by:

- [Building an XML](../basics/customize/integration/#build-an-xml-manifest-no-wado-server) file by using `DirectDownloadFile` and `DirectDownloadThumbnail`:
- Adding the following [command](../basics/commands/#dicom-get):<br>
    `$dicom:get -r http://external.server/images/MRIX_LUMBAR/img1.dcm  http://external.server/images/img2.dcm`<br>
    Note: This option must be used only for a very limited number of files.
{{% /expand %}}
<br>
