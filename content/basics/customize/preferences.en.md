---
title: Preferences
description: "Where Weasis preferences live, the order properties load in, the preferences a site can set for all users, and the configuration documents of the resources package."
weight: 20
keywords: [ "weasis preferences", "configuration properties", "property file", "site configuration", "configuration documents", "default settings" ]
---

[ViewerHub]() (is a separate project that will be available soon) is a tool designed for managing server-side Weasis preferences across all native client installations. The preferences are defined in each [release package](https://github.com/nroduit/Weasis/releases) (`bin-dist/weasis/conf` within `weasis-native.zip`) and can be modified either through the ViewerHub web portal or via the [Weasis protocol](../../getting-started/weasis-protocol/#modify-the-launch-parameters) with the `pro` parameter.

Some server-side preferences are applied by Weasis only during the initial launch, as they can later be adjusted in the Weasis user interface. On the other hand, certain server-side preferences are utilized by Weasis during every launch and cannot be modified through the User Interface (client-side).

### Changing Preferences in Weasis
#### Client-Side Preferences
Local preferences can be modified in the following ways:
- **Through the Weasis User Interface:** Navigate to _File > Preferences_.
- **Using the Weasis Protocol:** Use the [weasis:config](../../getting-started/weasis-protocol/#modify-the-launch-parameters) command with the `pro` parameter.

#### Server-Side Preferences
Server-side preferences can be updated using any of the following methods:
- **Through the [ViewerHub Web Portal]():** Manage preferences directly via the web portal for all users, for user group or for a specific hostname.
- **By Extending the Configuration File:** Create a new JSON file to extend the `base.json` configuration.

### Priority order for loading a property

Here is the priority order to set a property:
1. Java System property providing from parameters of [weasis:config](../../getting-started/weasis-protocol/#modify-the-launch-parameters) or the [launching URI](https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters))
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


### Configuration documents {#configuration-documents}

A site ships its configuration as JSON documents in the `config/` folder of the resources package {{< since "4.8.0" >}}: `resources.zip`, uploaded in [ViewerHub](../../viewer-hub/user-guide/weasis/package/) for a release and a group, or `app/resources/config/` of a local installation. One document, one file:

| Document | Holds | User document |
|---|---|---|
| `windowPresets.json` | [Window/Level presets](window-level-presets/) | `customWindowPresets.json` in the preferences folder |
| `colormaps.json` | [color maps](../../tutorials/color-maps/) and volume presets | `customColorMaps.json` in the preferences folder |
| `identityMasking.json` | [masking](../../tutorials/identity-masking/) profiles, tag classification and device masks | `identityMasking.json` in the preferences folder |
| `measurementProfiles.json` | [measurement tool profiles](../../tutorials/draw-measure/#tool-profiles) | `measurementProfiles.json` in the preferences folder |
| `dicomNodes.json`, `dicomCallingNodes.json`, `dicomPrinterNodes.json`, `dicomWebNodes.json` | DICOM nodes, calling nodes, DICOM printers and [DICOMweb nodes](../../tutorials/dicomweb-config/) | same names, in the data folder of the DICOM explorer plugin |
| `authentication.json` | authentication methods (OAuth2 providers) | same name, in the data folder of the plugin |
| `searchTemplates.json` | the query templates of [DICOM Query/Retrieve](../../tutorials/dicom-import/#dicom-queryretrieve) | same name, in the data folder of the plugin |
| `attributesView.json` | the DICOM annotations of the viewer corners, per modality | — |
| `seriesSplittingRules.json` | the rules splitting a series into several views, per modality | — |
| `dicomLaunchers.json`, `otherLaunchers.json` | external launchers | same names, in the data folder of the plugin |

#### Three layers, one rule

Every document is merged from three layers: the **built-in** document shipped with Weasis, the **site** document of `config/`, and the **user** document. The entries are merged by `id`:

* A later layer replaces the whole entry of the same `id` and keeps its position in the list; new ids are appended in document order.
* `"hidden": true` removes the entry from the lists. Redefine a built-in id with `hidden` to take it away from every user.
* `"locked": true` on a site entry forbids the user layer from replacing or hiding it. Only the site document can lock.
* `"extends": "<id>"` starts an entry from another entry of the same document, or of a lower layer, and gives only the fields that change. A field replaces the whole field of the base, nested objects included; `extends`, `id` and `locked` are never inherited.

Ids are `<layer>.<kind>.<slug>`, prefixed `weasis.` (built-in), `site.` or `user.`; an entry without an `id` gets one derived from what identifies it (the AE title, host and port of a DICOM node, the URL of a DICOMweb node, the name of a search template). Every document is a JSON object with `"schema": 1` and an array of entries whose name depends on the document (`presets`, `maps`, `nodes`, `methods`, `templates`, `modalities`, `launchers`); a bare array is accepted when reading.

In the preference pages, a site entry is shown as read-only with *(site)* or *(site, locked)* after its name, and a user entry that overrides a site or built-in entry offers **Reset to the site …** / **Reset to the built-in …** in place of **Delete**. The **Reload configuration files** button at the bottom of the preferences dialog reads the site and user documents again without restarting Weasis. A *Scope* line under the pages that declare it says whether their settings follow **your profile**, belong to **this workstation** or come from **your site**.

#### Legacy XML files and migration

Until Weasis 5.2, the XML files placed at the root of the resources package before 4.8 — `dicomNodes.xml`, `dicomCallingNodes.xml`, `dicomPrinterNodes.xml`, `dicomWebNodes.xml`, `authenticationNodes.xml`, `searchParameters.xml`, `attributes-view.xml`, `series-splitting-rules.xml` — are still read when `config/` holds no JSON document of the same kind; when both exist, the JSON wins. The shipped package carries `config/attributesView.json` and `config/seriesSplittingRules.example.json`, the built-in splitting rules as a starting point: rename it to `seriesSplittingRules.json` to activate it.

On the user side, the XML files of a 4.7 installation (DICOM nodes, printers, DICOMweb nodes, authentication methods, search templates) are converted once into their JSON documents at the first start of 4.8 and left untouched. Going back to 4.7 finds them as they were; the changes made in 4.8 are not carried back.

#### Secrets and remote preferences

Secrets never go into the user documents: the client secret of an authentication method and the values of the custom headers of a DICOMweb node are written empty in the document and kept in `auth-secrets.json` of the preferences folder, readable by its owner only and never exported.

The user documents are not sent to the ViewerHub preference service in 4.8.0: the property `weasis.pref.sync.documents` (default `false`) keeps that mirror off until the service stores and returns such documents.

#### Add DICOM nodes, printers or DICOMweb nodes for a site {#how-to-add-dicom-nodes-or-dicom-printers-at-the-server-side}

1. Configure the nodes from the graphical user interface: DICOM nodes and DICOMweb nodes from **File > Preferences > DICOM node list**, DICOM printers from **File > Print > DICOM Print**.
2. Go to the folder `${user.home}/.weasis/data/weasis-dicom-explorer` and copy the desired documents: `dicomNodes.json`, `dicomPrinterNodes.json`, `dicomWebNodes.json`, `dicomCallingNodes.json` (and `authentication.json` for the methods a DICOMweb node refers to).
3. Rename the ids from `user.` to `site.`, add `"locked": true` to the entries the users must not replace, and fill in the header values of the DICOMweb nodes, which the user document leaves empty.
4. Paste them into the `config/` folder of the resources package. For a web distribution, unzip `resources.zip`, add the files and zip it again.
5. The nodes appear for every user as *(site)* entries, read-only.

A DICOM node (`dicomNodes.json`, same shape for the calling nodes and the printers):

``` json
{
  "schema": 1,
  "nodes": [
    {
      "id": "site.node.pacs",
      "type": "DICOM",
      "description": "Main PACS",
      "aeTitle": "PACS",
      "hostname": "pacs.example.org",
      "port": 11112,
      "usageType": "BOTH",
      "tsuid": "EXPLICIT_VR_LE",
      "locked": true
    }
  ]
}
```

`usageType` is `RETRIEVE`, `STORAGE` or `BOTH`; `tsuid` is the transfer syntax asked for a retrieve, left out to keep the original one. A DICOMweb node (`dicomWebNodes.json`) gives the service instead of the AE; `authMethod` is the `uid` of a method of `authentication.json`:

``` json
{
  "schema": 1,
  "nodes": [
    {
      "id": "site.node.dicomweb",
      "type": "WEB",
      "description": "DICOMweb archive",
      "url": "https://pacs.example.org/dicomweb",
      "webType": "DICOMWEB",
      "authMethod": "d5f0c1e2-…",
      "headers": {"X-Api-Key": "…"}
    }
  ]
}
```

`webType` is `DICOMWEB` (all RESTful services), `QIDORS`, `WADORS`, `STOWRS` or `WADO` (WADO-URI).

#### Search templates

`searchTemplates.json` holds the templates of the Query/Retrieve dialog; the tags are DICOM keywords and `period` is one of the periods of the dialog (`ALL`, `TODAY`, `YESTERDAY`…):

``` json
{
  "schema": 1,
  "templates": [
    {
      "id": "site.search.ct-today",
      "name": "CT of the day",
      "period": "TODAY",
      "params": [
        {"tag": "ModalitiesInStudy", "values": ["CT"]}
      ]
    }
  ]
}
```

#### Viewer annotations

`attributesView.json` sets, per modality, the attributes drawn in the four corners of a view. The entry `id` is the modality (`DEFAULT`, `CT`, `MG`…), `extends` starts from another modality, and each corner — `topLeft`, `topRight`, `bottomLeft`, `bottomRight` — is a list of lines numbered from 1 to 7; a corner given here replaces the whole corner of the base. A line tries its `tags` in order until one has a value, and `format` renders it: `$V` is the value, `$V:l$25$` limits it to 25 characters, `$V:f$#,##0.##$` applies a Java decimal pattern.

``` json
{
  "schema": 1,
  "modalities": [
    {
      "id": "MG",
      "extends": "DEFAULT",
      "bottomRight": [
        {"line": 2, "tags": ["SeriesNumber"], "format": "Series Nb: $V"},
        {"line": 3, "tags": ["FrameLaterality", "ImageLaterality", "Laterality"], "format": "Laterality: $V"},
        {"line": 7, "tags": ["ViewPosition"], "format": "Position: $V:l$25$"}
      ]
    }
  ]
}
```

#### Series splitting rules

`seriesSplittingRules.json` sets, per modality, the attributes whose change splits a series into several views: `splittingTags` for single-frame images and `multiframeSplittingTags` for the frames of a multi-frame image. An item is `{"tag": "Keyword"}`, with an optional `condition` that restricts the split: `allOf` or `anyOf` over leaves `{"tag", "operator", "negate", "ignoreCase", "values"}` — `operator` is `equals` or `contains` — or nested groups.

``` json
{
  "schema": 1,
  "modalities": [
    {
      "id": "CT",
      "extends": "DEFAULT",
      "splittingTags": [
        {"tag": "ImageType"},
        {"tag": "ConvolutionKernel"},
        {"tag": "ImageOrientationPlane",
         "condition": {"allOf": [
           {"tag": "ImageType", "operator": "contains", "negate": true, "ignoreCase": true, "values": ["PROJECTION"]}
         ]}}
      ]
    }
  ]
}
```
