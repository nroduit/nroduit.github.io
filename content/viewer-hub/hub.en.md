---
title: Imaging Hub
description: Install all the required components for testing or debugging
keywords: [ "install",  "dicom viewer" ]
weight: 20
---

This page describes how to install the Imaging Hub, a Docker Compose stack for managing dcm4chee PACS, ViewerHub, and related services.

{{% notice warning %}}
This stack is designed for development and testing purposes only. It enables debugging ViewerHub and testing integration with dcm4chee PACS. It is **not suitable for production use**.
{{% /notice %}}

## Included Services

This stack comprises the following components:
- **dcm4chee**: PACS server for storing and retrieving medical images.
- **ViewerHub**: Manages resources for different versions of Weasis.
- **MinIO**: Object storage server compatible with Amazon S3 APIs.
- **Redis**: Cache service storing manifest data for Weasis resources.
- **Postgres**: Database backend for ViewerHub and dcm4chee.
- **Keycloak**: Manages user authentication and access.
- **Config-server**: Manages configuration of all services.
- **Eureka**: Provides service discovery for stack components.

## Prerequisites
- Docker
- Docker Compose CLI

## Configurations
This stack supports multiple configurations:

- **Debug (`local`)**: Includes all the required stack except ViewerHub and uses local volumes.
- **Unsecure (`unsecure`)**: Enables HTTP and uses development-grade settings. dcm4chee and ViewerHub services have no authentication.
- **Secure (`secure`)** [<span style="color:red">Not yet available</span>]: Enables HTTPS and uses production-grade settings. dcm4chee and ViewerHub services have authentication.

### Usage
Run the following commands based on the environment:

- **For debugging ViewerHub**:
  ```bash
  ./scripts/start.sh local
  ```
  And then run ViewerHub from your IDE

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

## ViewerHub

ViewerHub is a web application that manages the resources required by the different versions of Weasis.

Access the ViewerHub console at: http://localhost:8081

Use the following credentials:
- User: `weasis-manager-user`
- Password: `weasis-manager-password`


