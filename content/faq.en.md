---
title: FAQs
disableToc: true
---

## <center>Frequently Asked Questions</center>
<br>
{{%expand "Why the Weasis license is Eclipse Public License?" %}}
The <a target="_blank" href="http://www.eclipse.org/legal/epl-v20.html">Eclipse Public License</a> is an <a target="_blank" href="http://www.opensource.org">OSI approved</a> license and a commercially friendly copyleft license.

EPL is more business-friendly about some patent retaliation and reverse engineering clauses than LGPL. With EPL, derivative work (weasis plugin) can be distributed in any license type: open source, freeware, commercial... However, if you distribute Weasis with some modifications (changing existing source code of the open source Weasis plug-ins), even if it is a free distribution, you are obligated to make your modifications available to others.

For more information about EPL, check out the <a target="_blank" href="http://www.eclipse.org/legal/epl-2.0/faq.php">EPL 2 FAQ</a>.
{{% /expand%}}

{{%expand "How to start Weasis automatically from a web page without downloading jnlp?" %}}
From  the Oracle Java Runtime 8 update 111, it is possible to launch a Java Webstart application from the jnlp protocol. See <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#new-way-to-launch-jnlp">the new way of launching Java Westart</a> with weasis-pacs-connector.
{{% /expand%}}

{{%expand "Can Weasis be incorporated in DICOM CDs or other removable media?" %}}
Yes, the Weasis portable version can be copied in DICOM CD-ROMs as a multi-platform stand-alone viewer with launchers for Mac OS X, Linux and Windows. The viewer requires that a Java Runtime Environment (JRE 8 or greater) be installed on the machine to run. If Java is not installed on Windows, a dialog will propose to install it from the Internet.

{{% notice tip %}}
The executable (viewer-win32.exe) allows to embed a JRE in the relative directory "jre/windows" (_e.g. weasis-portable/jre/windows/bin/java.exe_). To support 32 and 64-bit architecture, copy 32-bit Java Rutime from its installed directory.<br>
**Note**: the embedded Java Runtime is used only when no runtime is available on the system. When Java is run from CD, it could be a little slow.
{{% /notice %}}

The viewer loads automatically images from DICOMDIR or from directories configured in "weasis/conf/config.properties (by default `weasis.portable.dicom.directory=dicom,DICOM,IMAGES,images`).

For burning Weasis with dcm4chee-cdw, look at [Write weasis-portable to DICOM CDs with dcm4chee-cdw](../getting-started/installation/dcm4chee/#write-weasis-portable-to-dicom-cds-with-dcm4chee-cdw).
{{% /expand%}}

{{%expand "How to enable Weasis logging?" %}}
Logs are available either in the Java console or in Weasis log files.

1. By displaying the Java console:
    * <a target="_blank" href="http://www.java.com/en/download/help/javaconsole.xml">Windows</a>
    * <a target="_blank" href="http://www.java.com/en/download/help/enable_console_linux.xml">Linux</a>
    *  Mac:
        1. Navigate to the following folder: Applications > Utilities > Java.
        1. Click the Java Preferences icon and then the Advanced tab.
        1. Under the Java console section, select the Show console radio button.

2. By writing to log files:
    - From Weasis 1.1.2, logging can be activated from *File > Preferences > General*
    - The default logging configuration comes from config.properties or ext-config.properties, see [Weasis Preferences](../basics/customize/preferences).
{{% /expand%}}


{{% expand "Is it possible to download DICOM files without having a WADO server?" %}}
Yes, but a WADO server is recommended. Downloading DICOMs can be achieved by:

-   [Bulding an xml](../basics/customize/integration/#build-an-xml-manifest-no-wado-server) file by using `DirectDownloadFile` and `DirectDownloadThumbnail`:
-   Adding the following parameter in the argument tag of the JNLP or [as an argument of the weasis-portable executable file](../basics/commands):<br>
    `$dicom:get -r http://external.server/images/MRIX_LUMBAR/img1.dcm  http://external.server/images/img2.dcm`<br>
    Note: This option must be used only for a very limited number of files
{{% /expand %}}
