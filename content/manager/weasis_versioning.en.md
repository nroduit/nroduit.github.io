---
title: Versioning
description: 
keywords: [ "version" , "versioning" , "package", "bundle", "plugin", "minio", "s3", "release"]
weight: 40
---

## Manual Import

A version of Weasis can be manually imported into Weasis Manager in the tab "Package".

![manual_import.png](/manager/weasis_versioning/manual_import.png)

The file to be imported must have a name in this format: "weasis-native xxx.zip".

![location_native_zip_file.png](/manager/weasis_versioning/location_native_zip_file.png)

This file corresponds to one of the Weasis release versions produced here: https://github.com/nroduit/Weasis/releases/

### Import process

The import process of a Weasis version follows these different steps:
- Retrieval of the "weasis-native xxx.zip" file, decompression and storage of the version's resources/bundles in minio/S3.
- Compression of the version's "resources" folder into a zip file (necessary for Weasis) and storage on S3.
![resource_zip_compression.png](/manager/weasis_versioning/resource_zip_compression.png)
- Update on S3 of the Weasis version compatibility file if the imported version is more recent.
![minio_mapping-minimal-version.png](/manager/weasis_versioning/minio_mapping-minimal-version.png)
- Cache update regarding Weasis version compatibility mapping.
- Loading of the version's properties into the database.

## Nexus Import

Currently not available, will be implemented later.

## Remove Weasis package version

In order to delete a version of Weasis, it is necessary to select the version to delete, then right-click and confirm the deletion.

![delete_version_right_click.png](/manager/weasis_versioning/delete_version_right_click.png)

Deleting a version whose "launch config" is "default" will result in the deletion of all versions linked to this "default".

![delete_default_version_propagation.png](/manager/weasis_versioning/delete_default_version_propagation.png)

