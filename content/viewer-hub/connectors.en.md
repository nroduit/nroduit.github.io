---
title: Connectors
description: Configuration of the connectors used to connect to the different PACS
keywords: [ "connector", "pacs"]
weight: 40
---

This page outlines the configuration of connectors used by Viewer-Hub to connect to DICOM archives.

## Model

In order to retrieve the metadata used to identify the studies to display, connectors are configured to enable connections to various PACS or VNA systems. <br/>
Three types of connectors are defined in the configuration server: DB, DICOM, and DICOM_WEB.

These connectors are defined according to this model: <a href="/viewer-hub/connectors/connector_model.yml" download>connector_model.yml</a>

## Global connector configuration

The global connector configuration is defined as follows:

{{< highlight yaml >}}
connector:
    # If value is present: use the connectors specified, if not present or wrong connector ids: use all the valid connectors defined in the config
    default: # connectorId1, connectorId2

    # Limit the dicom-web connector when retrieving metadata at study or serie level
    dicom-web-level-limit: # STUDY, SERIE

    config:
        connector-id:
            type:  # Type of connector used => DB, DICOM, DICOM_WEB
            
            # ------- Search Criteria ----
            search-criteria:
                deactivated: # If a search criteria needs to be deactivated=> SOP_INSTANCE_UID, SERIE_INSTANCE_UID, STUDY_INSTANCE_UID, STUDY_ACCESSION_NUMBER, PATIENT_ID

            # ------- Specific parameters for Weasis manifest----
            weasis:
                manifest:
                    transfer-syntax-uid:
                    compressionRate:
                    requireOnlySOPInstanceUID:  # true/false
                    additionnalParameters:
                    overrideDicomTags:
                    httpTags: 

{{< /highlight >}}

## Database connector

This connector is used to connect to the PACS database in order to find the metadata of studies, series, instances to retrieve.

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
    wado: 
        authentication:
            ... => described below in the section "Authentication configuration"
{{< /highlight >}}

## DICOM connector

This connector is used to connect to the PACS in Dicom in order to find the metadata of studies, series, instances to retrieve.

{{< highlight yaml >}}
dicom-connector:
    dimse:
        calling-aet: # Calling aet
        aet: # Aet
        host: # Host
        port: # Port
        # Specific configuration for dicom connector when using CFind
        tls:
            mode:
            need-client-authentication:
        keyStore:
            url:
            type:
            password:
            keyStorePassword:
        truststore:
            url:
            type:
            password:
    wado: 
        authentication:
            ... => described below in the section "Authentication configuration"
{{< /highlight >}}


## DICOM Web connector

This connector is used to connect to the PACS in Dicom Web in order to find the metadata of studies, series, instances to retrieve.

{{< highlight yaml >}}
dicom-web-connector:
    qido-rs:
        authentication:
            ... => described below in the section "Authentication configuration"
    wado-rs:
        authentication:
            ... => described below in the section "Authentication configuration"
{{< /highlight >}}

## Authentication configuration

Authentication configuration is used to build the web clients for Dicom Web connectors which will get the metadata from the archive 
or used to handle Weasis authentication when building the manifest in order for Weasis to retrieve the images

{{< highlight yaml >}}
    authentication:
        type: # BASIC, OAUTH2
        oauth2:
            oidc-id: # Id of the oidc configuration (defined in application-oidc.yml)
            server:
                url:  # Url 
                port: # Port 
                context: # Context 
        basic:
            login: # Basic credential login 
            password: # Basic credential password
            server:
                url: # Url 
                port: # Port 
                context:  # Context 
{{< /highlight >}}