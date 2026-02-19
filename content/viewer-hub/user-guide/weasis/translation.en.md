---
title: Internationalization
description: How to manage translation packages in ViewerHub
keywords: [ "translation" , "i18n" ]
weight: 30
---

## Import

It is possible to import the translations that will be used by Weasis depending on the version of Weasis launched and the correspondence of this version with the compatibility file.

The name of the file to import must have the format "weasis-i18n-dist-X.X.X-SNAPSHOT.zip".

The translation zip files to import are present at this address: https://github.com/nroduit/weasis-i18n

In ViewerHub, management of translation packages is located in the "Translation" tab.

![manual_import.png](/viewer-hub/translation/manual_import.png)

The import will decompress the zip file and load the translation resources into the MinIO S3.

![s3_i18n_package.png](/viewer-hub/translation/s3_i18n_package.png)

## Removal

Deleting a translation version is done by selecting the version and right-clicking on this version and then confirming the deletion.

![delete_i18n_package.png](/viewer-hub/translation/delete_i18n_package.png)