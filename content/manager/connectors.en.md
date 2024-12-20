---
title: Connectors
description: Configuration of the connectors
keywords: [ "connector" ]
weight: 40
---

## Model

In order to be able to connect to the different PACS for the creation of the manifest, 3 types of connectors are defined in the server config: DB, dicom, dicom web.

These connectors are defined according to this model:

{{< highlight yaml >}}
# Connectors
connector:

# If value is present: use the connectors specified, if not present or wrong connector ids: use all the connectors defined in the config
default: # connectorId1, connectorId2
    # Connectors configuration
    config:
        connector-id:
            # DB,DICOM,DICOM WEB
            type:

            # ------- Search Criteria ----
            search-criteria:
                # SOP_INSTANCE_UID, SERIE_INSTANCE_UID, STUDY_INSTANCE_UID, STUDY_ACCESSION_NUMBER, PATIENT_ID
                deactivated:

             # ---------- Wado -------------
            # Used to retrieve images from manifest
            wado:
                authentication:
                    # Used to force usage of basic authentication parameters to retrieve images (even if request is authenticated)
                    force-basic: # true/false
                    # If request is authenticated,retrieve the token from the authenticated request and inject it in the manifest for Weasis to get the images
                    oauth2:
                        # Url used to retrieve images by adding authenticated request token in manifest
                        url:
                    # Retrieve the images by using this basic authentication parameters
                    basic:
                        # Url used to retrieve images by using basic authentication
                        url: 
                        # Basic credentials
                        login:
                        password:
                    transfer-syntax-uid:
                    compression-rate:
                    requireOnlySOPInstanceUID: # true/false
                    additionnalParameters:
                    overrideDicomTags:
                    httpTags:
                        X-Time:
                        X-Value:

            # -------- For database --------
            db-connector:
                user:
                password:
                uri:
                driver:
                query:
                    select:
                    accession-number-column:
                    patient-id-column:
                    study-instance-uid-column:
                    serie-instance-uid-column:
                    sop-instance-uid-column:

            # -------- For dicom ----------
            dicom-connector:
                calling-aet:
                aet:
                host:
                port:
                tls:
                    mode: # true/false
                    need-client-authentication: # true/false
                key-store:
                    url:
                    type:
                    password:
                    key-store-password:
                truststore:
                    url:
                    type:
                    password:
{{< /highlight >}}

## Database connector

This connector is used to be able to connect to the PACS database in order to find the studies, series, instances of images for the construction of the manifest.

{{< highlight yaml >}}
db-connector:
    user: # database user
    password: # encoded password
    uri: # database uri
    driver: # database driver
    query:
        select: # SQL query to retrieve patientName, patientId, patientBirthDate, patientSex, studyInstanceUid, studyDate, accessionNumber, studyId, referringPhysicianName, studyDescription, seriesInstanceUid, modality, seriesDescription, seriesNumber, sopInstanceUid, instanceNumber
        accession-number-column: # accession number column used in the SQL query above
        patient-id-column: # patient id column used in the SQL query above
        study-instance-uid-column: # study instance uid column used in the SQL query above
        serie-instance-uid-column: # serie instance uid column used in the SQL query above
        sop-instance-uid-column: # sop instance uid column used in the SQL query above
{{< /highlight >}}

## Dicom connector

This connector is used to be able to connect to the pacs in dicom in order to find the studies, series, instances of images for the construction of the manifest.

{{< highlight yaml >}}
dicom-connector:
    calling-aet: # calling aet
    aet: # aet
    host: # host
    port: # port
{{< /highlight >}}


## Dicom Web connector

Not yet implemented