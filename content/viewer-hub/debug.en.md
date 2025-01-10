---
title: Guidelines for development
description: How to develop and debug ViewerHub
keywords: [ "develop", "debug",  "dicom viewer" ]
weight: 30
---

This page provides guidelines for developing and debugging ViewerHub.

We recommend the use of [IntelliJ IDEA](https://www.jetbrains.com/idea/) because the following instructions are based on it.

## Add a Launcher

- Open _Run > Edit Configurations..._
- Aad in _VM options_ the following properties:
```
  -Duser.timezone=UTC
  -DENVIRONMENT=local
  -DEUREKA_CLIENT_SERVICE_URL_DEFAULT_ZONE=http://localhost:8761/eureka
  -DREGION=local
  -DDATACENTER=local
  -Dserver.port=8081
  -Dmanagement.server.port=19001
  -DBACKEND_URI=http://localhost:8081
  -DDB_HOST=localhost
  -DDB_PORT=45101
  -DDB_NAME=weasis-manager
  -DDB_USER=weasis-manager
  -DDB_PASSWORD=weasis-manager
  -DCONFIGSERVER_URI=http://configdecrypt:987654321@localhost:8888
  -DS3_ACCESS_KEY=access-key
  -DS3_SECRET_KEY=secret-key
  -DS3_ENDPOINT=http://localhost:9080
  -DS3_BUCKET_NAME=weasis-manager-bucket
  -DBACKEND_URI=http://localhost:8081
```
- Then clean/install + Run...

## ViewerHub

In order to access to ViewerHub:
```
http://localhost:8081
```
with

```
User: weasis-manager-user
Password: weasis-manager-password
```

## Launch Weasis

Once all the steps above completed, launch the below URL to launch Weasis and load the dicom image stored in the dcm4chee pacs:
```
http://localhost:8081/display/weasis?studyUID=1.3.12.2.1107.5.1.4.54023.30000004093013443132800000021&archive=dcm4chee-local
```
This URL works with the [Imaging Hub](../hub) stack. If you are using a different setup, you may need to adjust the URL accordingly.

For more information, refer to the [Launch APIs](../api) documentation.
