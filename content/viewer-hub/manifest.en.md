---
title: Weasis Manifest
description: Creation of manifest for Weasis
keywords: [ "manifest" , "cache" , "redis"]
weight: 80
---


## Manifest

The manifest contains the list of exams, series, and instances to retrieve when loading images by Weasis. 

The manifest is represented in this [format](../basics/customize/integration/#build-an-xml-manifest). It can also be served as [JSON](../basics/customize/integration/#json-manifest) {{< since "4.7.2" >}}; Weasis asks for XML by default and detects the returned format from its content.

The creation of the manifest occurs when a client calls ViewerHub to launch Weasis through the launch URL using the [Launch APIs](api).  

## Construction

According to the search criteria of the request, ViewerHub constructs the manifest through connectors.

There are 3 types of connectors:
- DB (database)
- DICOM (DICOM DIMSE)
- DICOM_WEB (DICOMweb)

DB queries or DICOM calls are made to retrieve the necessary information to populate the manifest according to the search criteria.

With a DICOM_WEB connector, the manifest may be truncated at the patient, study or series level: Weasis completes the missing levels itself through QIDO-RS {{< since "4.7.2" >}} and can retrieve a whole series in a single request — see [partial manifest and series bulk retrieve](../basics/customize/integration/#partial-manifest).

The connectors are defined according to a model in the config server.

## Cache Redis

Once the manifest built, it will be stored in a Redis cache for a defined period (TTL currently 3 minutes).

This mechanism allows multiple instances of ViewerHub, as the retrieval of the manifest by Weasis is asynchronous.

It is also useful when the user requests the visualization of the same study within the TTL period: the manifest will be retrieved directly from the Redis cache.

The key for retrieving the manifest corresponds to the hash of the search criteria.

