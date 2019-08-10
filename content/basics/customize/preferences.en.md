---
title: Preferences
description: Manage the Weasis preferences
weight: 20
keywords: [ "preferences", "weasis preferences", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

The WEB distribution (weasis.war) allows to deliver preferences from the server side to the client side. Some preferences on the server side are used by Weasis only during the first launch, because they can be changed lately in the Weasis user interface. The other preferences at server side are used by Weasis at every launch.

Local preferences can be modified:

- in the Weasis user interface: File > Preferences
- in files stored in ${user.home}/.weasis/preferences/ (not recommended)

Preferences on the server side can be modified:

- in the jnlp file (see how to configure weasis-jnlp.xml at [Installing Weasis in DCM4CHEE](../../../getting-started/dcm4chee))
- in ext-config.properties which extends (override) the configuration of config.properties.

{{% notice tip %}}
How to modify ext-config.properties:

- Unzip weasis.war, modify the file and zip it again.
- It is also possible to change the default location of ext-config.properties with the Java property "felix.extended.config.properties" with the parameter `cdb-ext` of the <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#launch-weasis">weasis service</a>. The ext-config.properties file can also be placed in a plugin package, see [How to build and install a plug-in](../build-plugins).
{{% /notice %}}

### Priority order for loading a property

Here is the priority order to set a property:

1. Java System property (can be passed as parameter in the <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters">launching URI</a>)
2. Property defined in weasis/conf/ext-config.properties or in weasis/conf/config.properties
3. Default value of the property (see table below)

Example to change language property (It will work only during the first launch of Weasis on a user session, otherwise delete ${user.home}/.weasis/preferences/).

1.  If you are using weasis-pacs-connector, add the <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters">property</a> `locale.lang.code`:
{{< highlight url >}}
http://localhost:8080/weasis-pacs-connector/weasis?patientID=9702672&pro="locale.lang.code%20fr_CH"
{{< /highlight >}}
2.  Add the property in weasis/conf/ext-config.properties:
{{< highlight ini >}}
locale.lang.code=fr_CH
{{< /highlight >}}
3.  The default value is "en\_US"

## List of preferences

- **GUI**: if **yes**, the property can be modified in the Weasis user interface.
- **Type**: **F**: only caught at the first launch of the viewer. **A**: always caught by the viewer. **AP**: always caught by the viewer but only from ext-config.properties or config.properties .
<font size="2">

| Property | Default value | GUI | Type | Description|
|----------|---------------|-----|------|------------|
| weasis.language                            | en                                     | yes | F    | Language code defined by [ISO 639](http://lcweb.loc.gov/standards/iso639-2/langcodes.html). Replaced by locale.lang.code in Weasis 2 |
| weasis.country                             | US                                     | yes | F    | Country or region code defined by [ISO 3166](http://www.iso.org/iso/en/prods-services/iso3166ma/02iso-3166-code-lists/list-en1.html). Replaced by locale.lang.code in Weasis 2 |
| weasis.variant                             |                                        | yes | F    | Optional variant code. Replaced by locale.lang.code in Weasis 2  |
| weasis.confirm.closing                     | false (from 2.0.0)                     | yes | F    | Show a message of confirmation when closing the application. |
| weasis.look                                | SubstanceTwilight  AquaLookAndFeel (Mac) | yes | F    | Look and feel, if the Substance library is not loaded, Nimbus will be used by default. |
| weasis.look.${system}                      | SubstanceTwilight  AquaLookAndFeel (Mac) | yes | F    | Look and feel, specific to the platform (macosx, linux, windows). |
| weasis.show.disclaimer                     | true                                   | no  | A    | Show a disclaimer (requires to be accepted to start the application) during the first launch of Weasis. |
| weasis.show.release                        | true (from 2.0.0)                      | no  | A   | Show a message when the release has changed |
| weasis.export.dicom                        | true (from 1.2.5)                      | no  | A    | Allows exporting DICOM files. |
| weasis.portable.dicom.cache                | true                                   | no  | A    | Cache the images imported from directories defined in weasis.portable.dicom.directory. If true, it is similar to the WEB import. |
| org.apache.sling.commons.log.level         | INFO                                   | yes | F    | Sets the logging level of the loggers. This may be any of the defined logging levels TRACE, DEBUG, INFO, WARN, ERROR.|
| org.apache.sling.commons.log.file.activate | false                                  | yes | F    | Activate the log file. If this property is false, log messages are written to System.out. Since Weasis 2.0.4 |
| org.apache.sling.commons.log.file.number   | 5                                      | yes | F    | The number of rotated files to keep. |
| org.apache.sling.commons.log.file.size     | 10MB                                   | yes | F    | Defines how the log file is rotated by size. |
| org.apache.sling.commons.log.pattern       | {0,date,dd.MM.yyyy HH:mm:ss.SSS} \*{4}\* \[{2}\] {3} {5} | no  | F    | Formatting log messages. java.util.MessageFormat pattern supporting up to six arguments: {0} The timestamp of type java.util.Date, {1} the log marker, {2} the name of the current thread, {3} the name of the logger, {4} the debug level and {5} the actual debug message. |
| **ONLY from Weasis 2.0**                   |                                        |     |      |           |
| locale.lang.code                           | en                                     | yes | F    | Language code (see [Java Locale](http://www.oracle.com/technetwork/java/javase/locales-137662.html)). If the value is "system" then the locale of the operating system will be used (client-side). |
| locale.format.code                         | system                                 | yes | F    | Format code for number and date (see [Java Locale](http://www.oracle.com/technetwork/java/javase/locales-137662.html)). If the value is "system" then the locale of the operating system will be used (client-side). |
| weasis.name                                | Weasis                                 | no  | AP   | Change the name of the application everywhere in UI |
| weasis.profile                             | default                                | no  | AP   | Application profile, it allows having a custom preferences directory on the client side (will not shared preferences with other Weasis instances) |
| weasis.resources.url                       | ${weasis.codebase.url}/resources.zip   | no  | A    | Application resource files (logo, presets, LUTs...). "resources.zip" is downloaded again only when the last modified date has changed. |
| weasis.download.immediately                | true                                   | yes | F    | Start to download series immediately   |
| download.concurrent.series                 | 3                                      | no  | A    | The number of concurrent series downloads |
| download.concurrent.series.images          | 4                                      | no  | A    | The number of concurrent image downloads in a series |
| audit.log                                  | false                                  | no  | A    | Audit log for giving statistics about usage of Weasis |
| weasis.color.wl.apply                      | true                                   | yes | F    | Allow to apply Window/Level on color images |
| weasis.dicom.root.uid                      | [2.25](http://www.oid-info.com/get/2.25) | no  | A    | Set value for dicom root UID when creating DICOM objects (KO or PR). See [company list](http://www.iana.org/assignments/enterprise-numbers).                                                                                                                                 |
| {ui keys}                                  | true                                   | no  | A    | Make visible or not the Toolbars, Tools, some buttons, main menu and context menu items (see ext-config.properties file) |
| weasis.aet                                 | WEASIS\_AE                             | no  | A    | Calling AETitle for DICOM send and DICOM print |
| **ONLY from Weasis 2.5.3**                 |                                        |     |      |                |
| org.apache.sling.commons.log.stack.limit   | 3                                      | yes | F    | Defines the maximum number of lines for stack trace (0 => NONE, -1 => ALL) |
| weasis.export.dicom.send                   | true                                   | no  | A    | Allows DICOM send. Is always false when weasis.export.dicom=false. |
| weasis.import.dicom                        | true                                   | no  | A    | Allows importing DICOMs |
| weasis.import.dicom.qr                     | true                                   | no  | A    | Allows DICOM Q/R. Is always false when weasis.import.dicom=false.  |
| weasis.acquire.meta.global.display         | PatientID,PatientName, PatientBirthDate, PatientSex, AccessionNumber, StudyDescription  | no  | A    | Global tags at the patient or study level that are visible in Dicomizer   |
| weasis.acquire.meta.global.edit            | StudyDescription                       | no  | A    | Global tags which are editable |
| weasis.acquire.meta.global.required        | PatientID, PatientName, AccessionNumber, StudyDescription  | no  | A    | Global tags which are required for publication  |
| weasis.acquire.meta.series.display         | Modality, OperatorsName, ReferringPhysicianName, BodyPartExamined, SeriesDescription  | no  | A    | Tags at the series level that are visible in Dicomizer |
| weasis.acquire.meta.series.edit            | ReferringPhysicianName, BodyPartExamined, SeriesDescription  | no  | A    | Series tags which are editable  |
| weasis.acquire.meta.series.required        | Modality, SeriesDescription             | no  | A    | Series tags which are required for publication |
| weasis.acquire.meta.image.display          | ImageComments, ContentDate, ContentTime  | no  | A    | Tags at the image level that are visible in Dicomizer |
| weasis.acquire.meta.image.edit             | ImageComments, ContentDate, ContentTime  | no  | A    | Image tags which are editable  |
| weasis.acquire.meta.image.required         | ContentDate                            | no  | A    | Image tags which are required for publication |
| weasis.acquire.dest.host                   | localhost                              | no  | A    | Hostname of DICOM send destination for Dicomizer. If no value, the list of DICOM nodes for storage is displayed. |
| weasis.acquire.dest.aet                    | DCM4CHEE                               | no  | A    | AETitle of DICOM send destination for Dicomizer |
| weasis.acquire.dest.port                   | 11112                                  | no  | A    | Port of DICOM send destination for Dicomizer |
| weasis.acquire.meta.study.description      | Pictures of follow-up,Pictures of observation,Pictures preoperative,Pictures intraoperative,Pictures postoperative | no  | A    | Comma-separated list of study description elements. Comment this property to have a free text field.|
| weasis.acquire.meta.series.description     |                                        | no  | A    | Comma-separated list of series description elements. Comment this property to have a free text field. |
| **ONLY from Weasis 2.6.0**                 |                                        |     |      |       |
| weasis.level.inverse                       | true                                   | yes | F    | Inverse level direction (moving the cursor down to increase brightness) |
| weasis.apply.latest.pr                     | false                                  | yes | F    | Apply by default the most recent Presentation State to the related image |
| **ONLY from Weasis 3.5.3**                 |                                        |     |      |       |
| weasis.pref.store.local.session            | false                                  | no  | A    | Store user preferences when weasis.user is not specified (only with remote preferences service) |

</font>
{{% notice info %}}
Preferences of the portable distribution (weasis-portable.zip)

- ext-config.properties is located in weasis/conf
- file resources are located in weasis/resources
{{% /notice %}}



### Examples of properties in ext-config.properties

Changing the default Look and feel

{{< highlight ini >}}
# Define the Look an Feel for the first launch according to the platform (macosx, linux, windows)
weasis.look=org.pushingpixels.substance.api.skin.SubstanceSaharaLookAndFeel
weasis.look.macosx=com.apple.laf.AquaLookAndFeel
weasis.look.linux=org.pushingpixels.substance.api.skin.SubstanceGraphiteAquaLookAndFeel
{{< /highlight >}}

### Customize resources

The resources are located:

- in web distribution: in "resources.zip" at root of weasis.war (see above how to set a new URL for resources)
- in portable distribution:  in ./weasis/resources

### How to add DICOM node or DICOM printers configuration at the server side (only from Weasis 2.5.0)

- From the graphical user interface, configure the DICOM printers (File > Print > DICOM Print) or DICOM nodes (File > Preferences > Dicom node list)
- Go to he folder ${user.home}/.weasis/data/weasis-dicom-explorer
- Copy the desired configuration files: dicomNodes.xml, dicomPrinterNodes.xml, dicomWebNodes.xml and dicomCallingNodes.xml
- Paste at the root path of ressources. For web distribution, unzip, place files and zip again.
- The new configurations should appear for all the users as non-editable configurations.
