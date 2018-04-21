---
title: Integration
weight: 10
description: How connecting Weasis to a PACS, RIS, EMR or any web interface
keywords: [ "workflow", "integration", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to launch Weasis from any environments</center>

There are two Weasis distributions: the WEB distribution (weasis.war) and the portable distribution (weasis-portable.zip). Here we are presenting how to connect the WEB distribution with any web application. This documentation is adapted for Weasis 2.5 and superior.

The easiest way to launch Weasis from a web context is to use <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a>.

{{% notice info %}}
For connecting to dcm4chee web interface, follow the instructions in [Installing Weasis in DCM4CHEE](../../../getting-started/dcm4chee).<br><br>
See also the new way of launching <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#new-way-to-launch-jnlp">Java Westart</a>.
{{% /notice %}}


## Use weasis-pacs-connector

Standard workflow when connecting Weasis to a PACS, RIS, EMR or any web interface:
![standard usage workflow](/images/connector-wk-std.png?classes=border "Standard workflow")
{{% notice note %}}
The schema above shows that the queries to the PACS are made at the same time the viewer starting.
{{% /notice %}}
Workflow where the manifest is embedded in the jnlp file (synchrone processes):
![embedding the XML manifest](/images/connector-wk-emb.png?classes=border "Embedding the xml manifest")

## Build your connector
This method has two requirements:

1. Building a JNLP file for launching Weasis
2. Building a XML manifest to download images

###  Build a JNLP
Build a <a target="_blank" href="https://docs.oracle.com/javase/8/docs/technotes/guides/javaws/developersguide/contents.html">Java Webstart</a> file (.jnlp) for launching Weasis. This file has at least one dynamic parameter (`<argument>$dicom:get ... </argument>`) to download images. Generally, it is the [XML file](#build-an-xml-manifest) containing the UIDs.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE jnlp PUBLIC "-//Sun Microsystems, Inc//DTD JNLP Descriptor 6.0//EN" "http://java.sun.com/dtd/JNLP-6.0.dtd">
  <jnlp spec="1.6+" codebase="http://localhost:8080/weasis" href="">
  <information>
    <title>Weasis</title>
    <vendor>Weasis Team</vendor>
    <description>DICOM images viewer</description>
    <description kind="short">An application to visualize and analyze DICOM images.</description>
    <description kind="one-line">DICOM images viewer</description>
    <description kind="tooltip">Weasis</description>
  </information>
  <security>
    <all-permissions />
  </security>

  <resources>
    <!-- Requires Java SE 8 for Weasis 2.5 and superior -->
	<java version="9+" href="http://java.sun.com/products/autodl/j2se" java-vm-args="--add-modules java.xml.bind --add-exports=java.base/sun.net.www.protocol.http=ALL-UNNAMED --add-exports=java.base/sun.net.www.protocol.https=ALL-UNNAMED --add-exports=java.base/sun.net.www.protocol.file=ALL-UNNAMED --add-exports=java.base/sun.net.www.protocol.ftp=ALL-UNNAMED --add-exports=java.base/sun.net.www.protocol.jar=ALL-UNNAMED --add-exports=jdk.unsupported/sun.misc=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.security=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.desktop/javax.imageio.stream=ALL-UNNAMED --add-opens=java.desktop/javax.imageio=ALL-UNNAMED --add-opens=java.desktop/com.sun.awt=ALL-UNNAMED" initial-heap-size="128m" max-heap-size="768m" />
	<java version="9+" java-vm-args="--add-modules java.xml.bind --add-exports=java.base/sun.net.www.protocol.http=ALL-UNNAMED --add-exports=java.base/sun.net.www.protocol.https=ALL-UNNAMED --add-exports=java.base/sun.net.www.protocol.file=ALL-UNNAMED --add-exports=java.base/sun.net.www.protocol.ftp=ALL-UNNAMED --add-exports=java.base/sun.net.www.protocol.jar=ALL-UNNAMED --add-exports=jdk.unsupported/sun.misc=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.security=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.desktop/javax.imageio.stream=ALL-UNNAMED --add-opens=java.desktop/javax.imageio=ALL-UNNAMED --add-opens=java.desktop/com.sun.awt=ALL-UNNAMED" initial-heap-size="128m" max-heap-size="768m" />
    <j2se version="1.8+" href="http://java.sun.com/products/autodl/j2se" initial-heap-size="128m" max-heap-size="768m" />
    <j2se version="1.8+" initial-heap-size="128m" max-heap-size="768m" />

    <jar href="http://localhost:8080/weasis/weasis-launcher.jar" main="true" />
    <jar href="http://localhost:8080/weasis/felix.jar" />

    <!-- Optional library (Substance Look and feel, only since version 1.0.8). Requires the new Java Plug-in introduced in the Java SE 6 update 10 release.For previous JRE 6, substance.jnlp needs a static codebase URL -->
    <extension href="http://localhost:8080/weasis/substance.jnlp" />

    <!-- Allows to get files in pack200 compression, only since Weasis 1.1.2 -->
    <property name="jnlp.packEnabled" value="true" />

    <!-- ================================================================================================================= -->
    <!-- Security Workaround. Add prefix "jnlp.weasis" for having a fully trusted application without signing jnlp (only since weasis 1.2.9), http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6653241 -->
    <!-- Required parameter. Define the location of config.properties (the OSGI configuration and the list of plug-ins to install/start) -->
    <property name="jnlp.weasis.felix.config.properties" value="http://localhost:8080/weasis/conf/config.properties" />
    <!-- Optional parameter. Define the location of ext-config.properties (extend/override config.properties) -->
    <property name="jnlp.weasis.felix.extended.config.properties" value="http://localhost:8080/weasis-ext/conf/ext-config.properties" />
    <!-- Required parameter. Define the code base of Weasis for the JNLP -->
    <property name="jnlp.weasis.weasis.codebase.url" value="http://localhost:8080/weasis" />
    <!-- Optional parameter. Define the code base ext of Weasis for the JNLP -->
    <property name="jnlp.weasis.weasis.codebase.ext.url" value="http://localhost:8080/weasis-ext" />
    <!-- Required parameter. OSGI console parameter -->
    <property name="jnlp.weasis.gosh.args" value="-sc telnetd -p 17179 start" />
    <!-- Optional parameter. Allows to have the Weasis menu bar in the top bar on Mac OS X (works only with the native Aqua look and feel) -->
    <property name="jnlp.weasis.apple.laf.useScreenMenuBar" value="true" />
    <!-- Optional parameter. Allows to get plug-ins translations -->
    <property name="jnlp.weasis.weasis.i18n" value="http://localhost:8080/weasis-i18n" />
    <!-- Optional Weasis Documentation -->
    <!-- <property name="jnlp.weasis.weasis.help.url" value="${cdb}/../weasis-doc" /> -->
    <!-- ================================================================================================================= -->
  </resources>

  <application-desc main-class="org.weasis.launcher.WebstartLauncher">
    <!-- Example for opening dicom files from remote xml file -->
    <argument>$dicom:get -w "http://localhost:8080/dcm4chee-web/wadoQueries/wado_query3888637380.xml.gz"</argument>

    <!-- Example for opening dicom files from a local folder -->
        <argument>$dicom:get -l "/home/Images/MRIX LUMBAR/"</argument>

    <!-- Example for opening dicom files by embedding the xml file encoded in gzip and then in base64, it must be in one line without space at the beginning -->
    <argument>$dicom:get -i "H4sIAAAAAAAAALVV7Y+aMBz+vr+i6XdLXwDBHHdxpy4mvgX0dvtkOqnaBOGO1qn//RUQnW5uy3JHCC2/1+d5Wsrdw36TgB8iVzJLA0gQhkCkiyyW6SqAW71seBA83H+62/E4m79uR..."</argument>

    <!-- Example for opening dicom files from URLs -->
    <argument>$dicom:get -r "http://server/images/img1.dcm http://server/images/img2.dcm"</argument>
  </application-desc>
  </jnlp>
```

{{% notice note %}}
Replace `http://localhost:8080/weasis` with your server location and `<argument>...</argument>` with your data to load. Adapt other parameters if necessary.
{{% /notice %}}

{{% notice tip %}}
<a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a> services are based on jnlp templates and they allow either to build a manifest from a PACS via DICOM C-Find or to upload the manifest by http POST.
{{% /notice %}}

###  Build an XML manifest
Build an XML file containing the UIDs of the images which will be retrieved from Weasis. There is <a target="_blank" href="https://github.com/nroduit/Weasis/blob/master/weasis-dicom/weasis-dicom-explorer/src/main/resources/config/manifest.xsd">XLS</a> to validate the content of xml. This file can be either compressed in gzip or uncompressed. Here is an example (required Weasis 2.5 and superior):

``` xml
<?xml version="1.0" encoding="UTF-8" ?>
<manifest xmlns="http://www.weasis.org/xsd/2.5" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <arcQuery additionnalParameters="" arcId="1001" baseUrl="http://archive-weasis.rhcloud.com/archive/wado" requireOnlySOPInstanceUID="false">
        <Patient PatientID="H13885_9M" PatientName="TEST NON SQUARE PIXELS" PatientSex="F">
            <Study AccessionNumber="" ReferringPhysicianName="" StudyDate="20130711" StudyDescription="TEST NON SQUARE PIXELS" StudyID="PKD" StudyInstanceUID="2.16.756.5.5.100.397184556.14391.1373576413.1508" StudyTime="170013">
                <Series Modality="US" SeriesDescription="NON SQUARE PIXELS: PIXEL ASPECT RATIO" SeriesInstanceUID="1.2.40.0.13.1.1.87878503032592846377547034671833520632" SeriesNumber="2">
                    <Instance InstanceNumber="107" SOPInstanceUID="1.2.40.0.13.1.1.126082073005720329436273995268222863740"/>
                </Series>
                <Series Modality="MR" SeriesDescription="NON SQUARE PIXELS: PIXEL SPACING" SeriesInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1" SeriesNumber="40001">
                    <Instance InstanceNumber="1" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1.0"/>
                    <Instance InstanceNumber="2" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1.1"/>
                    <Instance InstanceNumber="3" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1.2"/>
                    <Instance InstanceNumber="4" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578035.1.3"/>
                </Series>
                <Series Modality="MR" SeriesDescription="NON SQUARE PIXELS: PIXEL SPACING" SeriesInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2" SeriesNumber="50001">
                    <Instance InstanceNumber="1" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2.0"/>
                    <Instance InstanceNumber="2" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2.1"/>
                    <Instance InstanceNumber="3" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2.2"/>
                    <Instance InstanceNumber="4" SOPInstanceUID="2.16.756.5.5.100.397184556.7220.1373578664.2.3"/>
                </Series>
            </Study>
        </Patient>
    </arcQuery>
</manifest>
```

{{% notice note %}}
Important Parameters (except mandatory parameters):

- `PatientBirthDate` helps to identify a patient.
- `StudyDate,` `StudyTime`, `Modality`, `SeriesNumber` and `InstanceNumber` help to sort data before downloading images.
- `SeriesDescription` and `StudyDescription` allow to immediately display the descriptions before downloading the images.
{{% /notice %}}

{{% notice tip %}}
From Weasis 2.5 it is possible to have multiple archives (allows to have several arcQuery tags) and the <a target="_blank" href="https://github.com/nroduit/Weasis/blob/master/weasis-dicom/weasis-dicom-explorer/src/main/resources/config/presentations.xsd">presentations</a> tag which contains the image annotations.
{{% /notice %}}

###  Build an XML manifest (no WADO server)
This example requires only a WEB server and Weasis 2.5 and superior. Weasis will download files by URLs.

``` xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest xmlns="http://www.weasis.org/xsd/2.5" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <arcQuery additionnalParameters="" arcId="1001" baseUrl="http://archive-weasis.rhcloud.com/archive/wado" requireOnlySOPInstanceUID="false">
    <Patient PatientBirthDate="20010901" PatientID="017589" PatientName="Validate WADAKOKOA">
      <Study StudyDate="20100421" StudyDescription="胸部立位 Ｖ→Ｄ犬4" StudyInstanceUID="1.2.392.200036.9107.500.11141010042100073" StudyTime="113836">
        <Series DirectDownloadThumbnail="thumb_4563173729424544.jpg" Modality="CR" SeriesDescription="Ｖ→Ｄ犬4" SeriesInstanceUID="1.2.392.200036.9107.500.305.1410.141010042100073.121" SeriesNumber="1">
          <Instance DirectDownloadFile="image_4563173729424543.dcm" InstanceNumber="1" SOPInstanceUID="1.2.392.200036.9107.500.305.1410.20100421.114831.109.101410"/>
          <Instance DirectDownloadFile="image_4563173729424544.dcm" InstanceNumber="2" SOPInstanceUID="1.2.392.200036.9107.500.305.1410.20100421.114828.234.101410"/>
          <Instance DirectDownloadFile="image_4563173729424545.dcm" InstanceNumber="3" SOPInstanceUID="1.2.392.200036.9107.500.305.1410.20100421.114823.421.101410"/>
        </Series>
      </Study>
    </Patient>
  </arcQuery>
</manifest>
```

{{% notice note %}}
Important Parameters:

- `DirectDownloadFile` defines the URL of the DICOM file to download (the final URL is the combination of wadoURL + DirectDownloadFile)
- `DirectDownloadThumbnail` defines the URL of the JPEG file representing the series (the final URL is the combination of wadoURL + DirectDownloadThumbnail)
- The same ones as above.
{{% /notice %}}
