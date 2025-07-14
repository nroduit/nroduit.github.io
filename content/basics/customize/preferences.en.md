---
title: Preferences
description: Manage the Weasis preferences
weight: 20
keywords: [ "preferences", "weasis preferences", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

[ViewerHub]() (is a separate project that will be available soon) is a tool designed for managing server-side Weasis preferences across all native client installations. The preferences are defined in each [release package](https://github.com/nroduit/Weasis/releases) (`bin-dist/weasis/conf` within `weasis-native.zip`) and can be modified either through the ViewerHub web portal or via the [Weasis protocol](../../../getting-started/weasis-protocol/#modify-the-launch-parameters) with the `pro` parameter.

Some server-side preferences are applied by Weasis only during the initial launch, as they can later be adjusted in the Weasis user interface. On the other hand, certain server-side preferences are utilized by Weasis during every launch and cannot be modified through the User Interface (client-side).

### Changing Preferences in Weasis
#### Client-Side Preferences
Local preferences can be modified in the following ways:
- **Through the Weasis User Interface:** Navigate to _File > Preferences_.
- **Using the Weasis Protocol:** Use the [weasis:config](../../../getting-started/weasis-protocol/#modify-the-launch-parameters) command with the `pro` parameter.

#### Server-Side Preferences
Server-side preferences can be updated using any of the following methods:
- **Through the [ViewerHub Web Portal]():** Manage preferences directly via the web portal for all users, for user group or for a specific hostname.
- **By Extending the Configuration File:** Create a new JSON file to extend the `base.json` configuration.

### Priority order for loading a property

Here is the priority order to set a property:
1. Java System property providing from parameters of [weasis:config](../../../getting-started/weasis-protocol/#modify-the-launch-parameters) or the [launching URI](https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters))
2. Property defined in weasis/conf/xxx.json
3. The default value of the property (see table below)

Example to change language property (It will work only during the first launch of Weasis on a user session, otherwise delete ${user.home}/.weasis/preferences/).

1. If you are using weasis-pacs-connector, add the [property](https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters) `locale.lang.code`:
{{< highlight url >}}
http://localhost:8080/weasis-pacs-connector/weasis?patientID=9702672&pro="locale.lang.code%20fr_CH"
{{< /highlight >}}
2. Add the property in weasis/conf/xxx.json:
{{< highlight ini >}}
locale.lang.code=fr_CH
{{< /highlight >}}
3. The default value is "en\_US"

## List of preferences
The preferences listed below are extracted from the `base.json` file, which is located in [the source code](https://github.com/nroduit/Weasis/tree/master/weasis-distributions/etc/config).

The properties are grouped into categories (note: not all categories are shown in the list below), and each property includes the following details:
1. **Property Key**: The name of the property, used as a key by the viewer.
2. **Default Value**: The property’s default value, provided after the arrow. If it is marked as `Null`, the property is not set by default.
3. **First Badge**: The **JavaType** of the property, indicating its type in Java (String, Integer, Boolean, etc.).
4. **Second Badge**: Represents the **Type**, defining how the viewer handles the property:
   - **F**: Processed only during the viewer's initial launch as it can be adjusted in the client-side preferences.
   - **A**: Always processed by the viewer.
   - **AP**: Always processed by the viewer but only from `base.json` or other `.json` files.
5. **Description**: A brief explanation of the property, provided on the second line.

### Base preferences

{{< render-preferences url="https://raw.githubusercontent.com/nroduit/Weasis/refs/heads/master/weasis-distributions/etc/config/base.json" categories="LOG,LAUNCH,GENERAL,DICOM,VIEWER,UI" >}}

### Dicomizer preferences

{{< render-preferences url="https://raw.githubusercontent.com/nroduit/Weasis/refs/heads/master/weasis-distributions/etc/config/dicomizer.json" categories="LOG,LAUNCH,GENERAL,DICOM,VIEWER,UI,METADATA" >}}


### Customize resources

The default resources are located:
- With ViewerHub you can upload a new package "resources.zip" for a specific release. 
- For the installed distribution in *installedPath*/app/resources

### How to add DICOM nodes or DICOM printers at the server-side

- From the graphical user interface, configure the DICOM printers from _File > Print > DICOM Print_ or DICOM nodes from _File > Preferences > Dicom node list_
- Go to the folder ${user.home}/.weasis/data/weasis-dicom-explorer
- Copy the desired configuration files: dicomNodes.xml, dicomPrinterNodes.xml, dicomWebNodes.xml and dicomCallingNodes.xml
- Paste at the root path of resources. For web distribution, unzip, place files and zip again.
- The new configurations should appear for all the users as non-editable configurations in Weasis
