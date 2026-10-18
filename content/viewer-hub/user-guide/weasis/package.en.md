---
title: Version Compatibility
description: "Handle compatibility between Weasis releases in ViewerHub with the compatibility file, the cache and Minio or S3 storage."
keywords: [ "weasis package compatibility", "version compatibility", "minio", "s3 storage", "package cache" ]
weight: 60
---

## Compatibility file

A compatibility file named "version-compatibility.json" is present in each Weasis release. <br/>

{{< highlight text >}}
weasis-native.zip
    └── bin-dist/
        └── weasis/
            └── conf/
                └── version-compatibility.json
{{< /highlight >}}

This file contains the mapping between the release version ("release-version") and the minimum version of Weasis that should be installed on the client workstation ("minimal-version").

This file also indicates which translation version should be used ("i18n-version").

{{< version-compatibility >}}

## Site configuration

The resources package (`resources.zip`, uploaded per release and group) may hold a `config/` folder with the site configuration documents {{< since "4.8.0" >}}: Window/Level presets, color maps, masking, measurement profiles, DICOM and DICOMweb nodes, authentication methods, search templates, viewer annotations and series splitting rules, one JSON file each. Their names, the three-layer merge rules and the legacy XML files are described in [Configuration documents](../../../basics/customize/preferences/#configuration-documents).

## Cache

When uploading a new version in ViewerHub or when starting the application (in case the compatibility file is already present in the S3), ViewerHub will construct the different possible combinations from the compatibility file between the versions installed in ViewerHub and the Weasis releases.

These combinations will be stored in a redis cache. This cache is currently refreshed every 24 hours.

So when a client launches Weasis via ViewerHub, it will directly know which version, i18n, resources to use when launching Weasis on the user computer.

## Minio/S3

By importing a new version of Weasis into ViewerHub, if the compatibility file is more recent, ViewerHub will replace the compatibility file present on the S3. 

This compatibility file will be renamed in the S3 bucket "mapping-minimal-version.json"

In order to compare if this mapping file is more recent, ViewerHub will compare the version number of the latest release.