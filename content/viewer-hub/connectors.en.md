---
title: Connectors
description: Configuration of the connectors used by Weasis to connect to the different PACS
keywords: [ "connector", "pacs"]
weight: 40
---

This page outlines the configuration of connectors used by ViewerHub to connect to DICOM archives.

## Model

In order to create the Weasis manifest, connectors are configured to enable connections to various PACS or VNA systems. <br/>
Three types of connectors are defined in the configuration server: DB, DICOM, and DICOM_WEB.

These connectors are defined according to this model: [connector_model.yml](/viewer-hub/connectors/connector_model.yml)

## Global connector configuration

The global connector configuration is defined as follows:

{{< highlight yaml >}}
connector:
    # If value is present: use the connectors specified, if not present or wrong connector ids: use all the valid connectors defined in the config
    default: # connectorId1, connectorId2
    
    config:
        connector-id:
            type:  # Type of connector used => DB, DICOM, DICOM_WEB
            
            # ------- Search Criteria ----
            search-criteria:
                deactivated: # If a search criteria needs to be deactivated=> SOP_INSTANCE_UID, SERIE_INSTANCE_UID, STUDY_INSTANCE_UID, STUDY_ACCESSION_NUMBER, PATIENT_ID
{{< /highlight >}}

## WADO configuration

WADO configuration is used by Weasis to retrieve images from manifest

{{< highlight yaml >}}
WADO:
    authentication:
        # Used to force usage of basic authentication parameters to retrieve images (even if request is authenticated)
        force-basic: # true/false
        
        # If request is authenticated,retrieve the token from the authenticated request and inject it in the manifest for Weasis to get the images
        oauth2:
            url: # Url used to retrieve images by adding authenticated request token in manifest
        
        # Retrieve the images by using this basic authentication parameters
        basic:
            url: # Url used to retrieve images by using basic authentication
            login:  # Basic credential login 
            password: # Basic credential password
{{< /highlight >}}

## Database connector

This connector is used to be able to connect to the PACS database in order to find the studies, series, instances of images for the construction of the manifest.

{{< highlight yaml >}}
db-connector:
    user: # Database user
    password: # Encoded password
    uri: # Database uri
    driver: # Database driver
    query:
        select: # SQL query to retrieve patientName, patientId, patientBirthDate, patientSex, studyInstanceUid, studyDate, accessionNumber, studyId, referringPhysicianName, studyDescription, seriesInstanceUid, modality, seriesDescription, seriesNumber, sopInstanceUid, instanceNumber
        accession-number-column: # Accession number column used in the SQL query above
        patient-id-column: # Patient id column used in the SQL query above
        study-instance-uid-column: # Study instance uid column used in the SQL query above
        serie-instance-uid-column: # Serie instance uid column used in the SQL query above
        sop-instance-uid-column: # Sop instance uid column used in the SQL query above
{{< /highlight >}}

## DICOM connector

This connector is used to be able to connect to the pacs in DICOM in order to find the studies, series, instances of images for the construction of the manifest.

{{< highlight yaml >}}
dicom-connector:
    calling-aet: # Calling aet
    aet: # Aet
    host: # Host
    port: # Port
{{< /highlight >}}


## DICOM Web connector

Not implemented yet