---
title: Weasis Package Versioning
description: How to manage Weasis versions in ViewerHub
keywords: [ "version" , "versioning" , "package", "bundle", "plugin", "minio", "s3", "release"]
weight: 40
---

## Manual Import

A version of Weasis can be manually imported into ViewerHub in the tab "Package".

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

## Group-specific versions

It is possible to create a version of Weasis that will only be launched for certain groups of users or hosts.

In the "package" view, click on "Create new group config".

![create_new_package_version_location.png](/manager/weasis_versioning/create_new_package_version_location.png)

Then select the desired Weasis version (package version + launch config) and the new group to associate then press "Create".

![create_new_package_version.png](/manager/weasis_versioning/create_new_package_version.png)

The new version will thus be displayed in the list of versions already present.

If the user or host belongs to the group, the previously created configuration will be used to launch Weasis.

## Configuring version properties

The manager allows to modify the properties of versions on-the-fly.

To modify a property, it is necessary to open a version and double-click on the property to modify.

For example to modify the name of the viewer for a package/launch config/group:

- modification of the property "weasis.name"

![rename_weasis_name_property.png](/manager/weasis_versioning/rename_weasis_name_property.png)

- launching the viewer after modification: the label corresponds to the modified property

![result_rename_property.png](/manager/weasis_versioning/result_rename_property.png)

