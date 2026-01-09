---
title: Embedding in dcm4chee
description: How to install and configure Weasis as the default web viewer in the dcm4chee web interface
keywords: [ "dcm4chee", "dcm4chee web" , "dcm4chee integration", "dcm4chee viewer", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 10
---

This page explains how to integrate Weasis with dcm4chee-arc-light using weasis-pacs-connector. To launch Weasis without the connector, follow the alternative [instructions](../basics/customize/integration/#download-directly-with-dicomweb-restful-services).


![dcm4chee-arc-light](/gallery-dcm4chee/1Weasis%20in%20dcm4chee-arc-light.png?classes=border "dcm4chee-arc-light")

Follow these steps for the integration with `weasis-pacs-connector`:


1. [Install dcm4chee](https://github.com/dcm4che/dcm4chee-arc-light/wiki), if not already done (Installation with Docker is straightforward).

2. Go [here](https://sourceforge.net/projects/dcm4che/files/Weasis/) and download `weasis-pacs-connector.war` — See [Configuration Matrix](#configuration-matrix) below for the recommended version according to your dcm4chee-arc-light version.

3. Open the <a target="_blank" href="http://localhost:9990/">WildFly management console</a> (at `http://<your-host>:9990`). Note: with some Keycloak versions, the [management console may not be accessible](https://groups.google.com/g/dcm4che/c/UeNKzgijfqo).
    - Select the “Deployments” tab
    - Add `weasis-pacs-connector.war` using the “Add” button (Choose Upload a new deployment or select Replace when the file already exists)
{{% notice note %}}
Alternatively one may deploy the `.war` using JBoss Command Line Interface Console.
{{% /notice %}}

4. Configure weasis-pacs-connector (optional if default settings are sufficient).<br>
The default configuration is stored in two files inside weasis-pacs-connector.war. To override the default configuration:
    - Download the current [download>weasis-pacs-connector.properties](https://raw.githubusercontent.com/nroduit/weasis-pacs-connector/master/src/main/resources/weasis-pacs-connector.properties) and [download>dicom-dcm4chee-arc.properties](https://raw.githubusercontent.com/nroduit/weasis-pacs-connector/master/src/main/resources/dicom-dcm4chee-arc.properties) (configuration of the dcm4chee archive)
    - Edit the configuration as needed. For example, dcm4chee may be running on a different computer than Weasis, or the AE Title of dcm4chee may have been changed. If so, edit `weasis-pacs-connector.properties` or `dicom-dcm4chee-arc.properties` (Change pacs.host, pacs.port, and pacs.aet).
    - Copy `weasis-pacs-connector.properties` and `dicom-dcm4chee-arc.properties` into $WILDFLY_HOME/standalone/configuration (where $WILDFLY_HOME is the path of the running Wildfly).<br>
    With the docker installation use the docker copy command ($ docker cp ...)
{{% notice tip %}}
Instead of copying the files into $WILDFLY_HOME/standalone/configuration, JBoss Command Line Interface Console can be used to override files in the war. Add the two configuration files with the deployment-overlay command:<br>
{{% /notice %}}
{{< highlight bash >}}
deployment-overlay add --name=dcm4chee-arc --deployments=weasis-pacs-connector.war --content=WEB-INF/classes/weasis-pacs-connector.properties=/tmp/weasis-pacs-connector.properties,WEB-INF/classes/dicom-dcm4chee-arc.properties=/tmp/dicom-dcm4chee-arc.properties --redeploy-affected
{{< /highlight >}}
    - To apply the new configuration, from the management console "Disable" `weasis-pacs-connector.war` then "Enable"

5. To activate Weasis in the dcm4chee-arc-light user interface (See also [Invoke Image Display in dcm4chee](https://github.com/dcm4che/dcm4chee-arc-light/wiki/Invoke-Image-Display)):
 you need to add attributes by either editing `docker-compose.env` (from 5.22.0) or from the left menu Configuration > Devices > dcm4chee-arc > Extensions > Edit extension > Child Objects > Web Applications > DCM4CHEE:
     - Configure the URL for a view button at patient or study level and then copy the properties from [Configuration Matrix](#configuration-matrix).
        - From dcm4chee-arc-light 5.10.2 to 5.19.0, the left menu: Configuration > Devices > dcm4chee-arc > Extensions > Archive Device
        - From dcm4chee-arc-light 5.19.1 the left menu: Configuration > Devices > dcm4chee-arc > Extensions > Edit extension > Child Objects > Web Applications > DCM4CHEE
        - From dcm4chee-arc-light 5.22.0 by editing `docker-compose.env` (allows applying properties at deploy time). Note: the character `&` must be escaped (e.g., `IID_STUDY_URL=../../weasis-pacs-connector/weasis?studyUID={{studyUID}}\\&access_token={{access_token}}`)
{{% notice note %}}
**URL parameters**

- `access_token` is necessary in secure mode (secured RESTful services) from dcm4chee-arc-light 5.15.1
- `_self` avoids opening a new empty window in the browser<br>
{{% /notice %}}
    - {{% badge style="info" %}}Optional{{% /badge %}} Add <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters">other properties</a> in the URL.
    - Refresh the web page and the view button should appear as in the screenshot above
    - To launch the viewer from the web portal, the client computer must have installed the [Weasis package](download-dicom-viewer).

## Configuration Matrix

{{% notice note %}}
The list below maps dcm4chee-arc-light versions to the recommended `weasis-pacs-connector`, and gives the properties to add in dcm4chee-arc-light configuration to enable Weasis launching.

Older versions pass _self via query parameter (target=_self); newer versions (5.22.2+) use the dedicated property IID_URL_TARGET=_self.
{{% /notice %}}

### dcm4chee-arc-light 5.10.2 to 5.19.0

{{% badge style="info" title="weasis-pacs-connector" %}}7.x{{% /badge %}}

#### Unsecured Mode
<div style="font-size: 0.80em;">

* `../../weasis-pacs-connector/weasis?&patientID={}&cdb&target=_self`
* `../../weasis-pacs-connector/weasis?&studyUID={}&cdb&target=_self`

</div>

#### Secured Mode (from 5.15.1)
<div style="font-size: 0.80em;">

* `../../weasis-pacs-connector/weasis?&patientID={}&cdb&target=_self&access_token={}`
* `../../weasis-pacs-connector/weasis?&studyUID={}&cdb&target=_self&access_token={}`

</div>

---

### dcm4chee-arc-light 5.19.1 to 5.22.1

{{% badge style="info" title="weasis-pacs-connector" %}}7.x{{% /badge %}}

#### Unsecured Mode
<div style="font-size: 0.80em;">

* `IID_PATIENT_URL=../../weasis-pacs-connector/weasis?&patientID={}&cdb&target=_self`
* `IID_STUDY_URL=../../weasis-pacs-connector/weasis?&studyUID={}&cdb&target=_self`

</div>

#### Secured Mode
<div style="font-size: 0.80em;">

* `IID_PATIENT_URL=../../weasis-pacs-connector/weasis?&patientID={}&cdb&target=_self&access_token={}`
* `IID_STUDY_URL=../../weasis-pacs-connector/weasis?&studyUID={}&cdb&target=_self&access_token={}`

</div>

---

### dcm4chee-arc-light 5.22.2 to 5.30.x

{{% badge style="info" title="weasis-pacs-connector" %}}7.x{{% /badge %}}

#### Unsecured Mode
<div style="font-size: 0.80em;">

* `IID_PATIENT_URL=../../weasis-pacs-connector/weasis?patientID={{patientID}}&cdb`
* `IID_STUDY_URL=../../weasis-pacs-connector/weasis?studyUID={{studyUID}}&cdb`
* `IID_URL_TARGET=_self`

</div>

#### Secured Mode
<div style="font-size: 0.80em;">

* `IID_PATIENT_URL=../../weasis-pacs-connector/weasis?patientID={{patientID}}&cdb&access_token={{access_token}}`
* `IID_STUDY_URL=../../weasis-pacs-connector/weasis?studyUID={{studyUID}}&cdb&access_token={{access_token}}`
* `IID_URL_TARGET=_self`

</div>

---

### dcm4chee-arc-light 5.31.0+

{{% badge style="info" title="weasis-pacs-connector" %}}8.x{{% /badge %}}

{{% notice warning %}}
**Requirements**: Java 17+ and Jakarta EE 10 (WildFly 29.0.1.Final or later)<br>
**Note**:the context path has changed from ../../ to ../../../
{{% /notice %}}

#### Unsecured Mode
<div style="font-size: 0.80em;">

* `IID_PATIENT_URL=../../../weasis-pacs-connector/weasis?patientID={{patientID}}&cdb`
* `IID_STUDY_URL=../../../weasis-pacs-connector/weasis?studyUID={{studyUID}}&cdb`
* `IID_URL_TARGET=_self`

</div>

#### Secured Mode

<div style="font-size: 0.80em;">

* `IID_PATIENT_URL=../../../weasis-pacs-connector/weasis?patientID={{patientID}}&cdb&access_token={{access_token}}`
* `IID_STUDY_URL=../../../weasis-pacs-connector/weasis?studyUID={{studyUID}}&cdb&access_token={{access_token}}`
* `IID_URL_TARGET=_self`

</div>

---

