---
title: Imaging Hub
description: Install all the required components
keywords: [ "install",  "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer" ]
weight: 20
---

## Overview
A Docker Compose stack for managing dcm4chee PACS, Weasis Manager, and all the related services.

Note: This stack is intended for development and testing purposes only. It allows debugging Weasis Manager and testing the integration with dcm4chee PACS. It is not intended for production use.

This stack includes the following services:
- **dcm4chee**: A PACS server that enables storing and retrieving medical images.
- **weasis-manager**: A web application that manages the resources required by the different versions of Weasis.
- **minio**: An object storage server compatible with Amazon S3 APIs. It is used to store resources required by the different versions of Weasis.
- **redis**: A cache server used to store the manifest of the resources required by the different versions of Weasis.
- **postgres**: A database server used by Weasis Manager and dcm4chee.
- **keycloak**: An open-source identity and access management server used to authenticate users.
- **config-server**: A server that provides the configuration for the different services.
- **eureka**: A server that provides service discovery for the different services.


## Prerequisites
- Docker (20.10+)
- Docker Compose CLI

## Configurations
This stack supports multiple configurations:

- **Debug (`local`)**: Includes all the required stack except weasis-manager and uses local volumes.
- **Unsecure (`unsecure`)**: Enables HTTP and uses development-grade settings. dcm4chee and weasis-manager services have no authentication.
- **Secure (`secure`)**: Enables HTTPS and uses production-grade settings. dcm4chee and weasis-manager services have authentication.

### Usage
Run the following commands based on the environment:

- **For debugging Weasis-Manager**:
  ```bash
  ./scripts/start.sh local
  ```
  And then run weasis-manager from your IDE
 

## Minio

Minio is an open-source object storage server compatible with Amazon S3 APIs. It is used to store resources required by the different versions of Weasis.

Access the Minio console at: http://localhost:9090

Use the following credentials:
- User: `weasis-manager`
- Password: `weasis-manager`

## Keycloak

Keycloak is an open-source identity and access management server used to authenticate users.

Access the Keycloak console at: http://localhost:8085

Use the following credentials:
- User: `admin`
- Password: `admin`

## Dcm4chee

Dcm4chee is a PACS server that enables storing and retrieving medical images.

Access the dcm4chee console at: http://localhost:8080/dcm4chee-arc/ui2/en/study/study

For secure mode, access the dcm4chee console at: https://localhost:8443/dcm4chee-arc/ui2/en/study/study
Use the following credentials:
- User: `admin`
- Password: `changeit`

## Weasis Manager

Weasis Manager is a web application that manages the resources required by the different versions of Weasis.

Access the Weasis Manager console at: http://localhost:8081

Use the following credentials:
- User: `weasis-manager-user`
- Password: `weasis-manager-password`


