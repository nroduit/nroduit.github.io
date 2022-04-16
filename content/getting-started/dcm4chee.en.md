---
title: Embedding in dcm4chee
description: How installing Weasis to be the default web viewer of dcm4chee web interface
keywords: [ "dcm4chee", "dcm4chee web" , "dcm4chee integration", "dcm4chee viewer", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 10
---

This page describes how installing Weasis to be the default web viewer of dcm4chee web interface. See [How to launch Weasis from any environments](../../basics/customize/integration) to integrate Weasis into your own user interface.

Weasis is launched from the dcm4chee administrative web interface with the [weasis protocol](../weasis-protocol), as shown in the pictures below.
{{% notice note %}}
The documentation where Weasis was launched with Java Webstart is still available [here](../../old/dcm4chee).
{{% /notice %}}

### For dcm4chee-arc-light

![dcm4chee-arc-light](/gallery-dcm4chee/1Weasis%20in%20dcm4chee-arc-light.png?classes=border "dcm4chee-arc-light")

For a simpler and faster installation without server components, please follow these [instructions](../../basics/customize/integration/#download-directly-with-dicomweb-restful-services); no need to consider the following points on this page. Otherwise if you need more advanced configurations then follow these steps:

1. [Install dcm4chee](https://github.com/dcm4che/dcm4chee-arc-light/wiki), if not already done (Installation with Docker is straightforward).

2. Go [here](https://sourceforge.net/projects/dcm4che/files/Weasis/) and download these following files:
{{% notice warning %}}
**Download issue**: Some browsers (like Internet Explorer) may rename war files to zip. If so, use the Save As option when downloading and change the name back to war.
{{% /notice %}}
    - From weasis-pacs-connector folder:
        - [weasis-pacs-connector.war] Requires at least the version 7.1.2
    - From the folder with the latest version number (Optional if you want to run only the [native version](../) installed on the client system):
        - [weasis.war] requires at least Weasis 3.5.3
        - [weasis-i18n.war] Optional for [internationalization](../translating)
        - [weasis-ext.war] Optional package for additional plug-ins (e.g. exporting the images to build an ISO image for CD/DVD)
    - From the folder with the latest version number:

3. Open the <a target="_blank" href="http://localhost:9990/">wildfly management console</a> (at `http://<your-host>:9990`).
    - Select the “Deployments” tab
    - Add the .war files using the “Add” button (Choose Upload a new deployment or select Replace when the file already exists)
{{% notice note %}}
Alternatively one may deploy .war files using JBoss Command Line Interface Console.
{{% /notice %}}

4. Configure weasis-pacs-connector (This step is optional if you just want to keep the default configuration).<br>
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
    - For applying the new configuration, from the management console "Disable" weasis-pacs-connector.war and then "Enable"

5. To activate Weasis in the dcm4chee-arc-light user interface (see the matrix of the required versions in the table below):
 you need to add attributes by either editing docker-compose.env (from 5.22.0) or from the left menu Configuration > Devices > dcm4chee-arc > Extensions > Edit extension > Child Objects > Web Applications > DCM4CHEE (add `&cdb` to the URL if weasis.war has not been deployed on the server-side):
     - Configure the URL for having a view button for the patient or study level.
        - From dcm4chee-arc-light 5.10.2 to 5.19.0 the left menu Configuration > Devices > dcm4chee-arc > Extensions > Archive Device
        - From dcm4chee-arc-light 5.19.1 the left menu Configuration > Devices > dcm4chee-arc > Extensions > Edit extension > Child Objects > Web Applications > DCM4CHEE
        - From dcm4chee-arc-light 5.22.0 by editing docker-compose.env (It allows you to directly apply the properties when deploying, then the can be edited in the web portal). Note: the character ‘&’ must be escaped (e.g. IID_STUDY_URL=../../weasis-pacs-connector/weasis?studyUID={{studyUID}}\\&access_token={{access_token}})
{{% notice note %}}
**URL parameters**

- `access_token` is necessary in secure mode (secured RESTful services) from dcm4chee-arc-light 5.15.1
- `_self` avoids to open a new empty window in the web browser<br>
- `cdb` [cdb parameter](https://nroduit.github.io/en/getting-started/weasis-protocol/#modify-the-launch-parameters) to override the URL of the Weasis web context to null (when you want only the native local version or when weasis.war has not be deployed with weasis-pacs-connector)<br>
- See also <a target="_blank" href="https://github.com/dcm4che/dcm4chee-arc-light/wiki/Invoke-Image-Display">Invoke Image Display in dcm4chee</a>
{{% /notice %}}
{{% notice tip %}}
**Absolute path**: The values above starting by "../" are the default relative path when weasis-pacs-connector is installed in the same JBoss as dcm4chee. Otherwise replace the relative URL by an absolute value, ex: `http://<your-host>:<port>/weasis-pacs-connector/...`
{{% /notice %}}
    - Optional: add <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters">other properties</a> in the URL.
    - Refresh the web page and the view button should appear as in the screenshot above
    - To launch the viewer from the web portal, the client computer must have installed the [Weasis package](../).

<font size="2">

| Mode | dcm4chee version | Configuration |
| ---- | ---------------- | --------------|
| Unsecured | from 5.10.2 to 5.19.0 | ../../weasis-pacs-connector/weasis?&patientID={}&target=_self<br>../../weasis-pacs-connector/weasis?&studyUID={}&target=_self |
| Unsecured* | from 5.10.2 to 5.19.0 | ../../weasis-pacs-connector/weasis?&patientID={}&cdb&target=_self<br>../../weasis-pacs-connector/weasis?&studyUID={}&cdb&target=_self |
| Secured | from  5.15.1 to 5.19.0 | ../../weasis-pacs-connector/weasis?&patientID={}&target=_self&access_token={}<br>../../weasis-pacs-connector/weasis?&studyUID={}&target=_self&access_token={} |
| Secured* | from  5.15.1 to 5.19.0 | ../../weasis-pacs-connector/weasis?&patientID={}&cdb&target=_self&access_token={}<br>../../weasis-pacs-connector/weasis?&studyUID={}&cdb&target=_self&access_token={} |
| Unsecured | from 5.19.1 to 5.22.1 | IID_PATIENT_URL=../../weasis-pacs-connector/weasis?&patientID={}&target=_self<br>IID_STUDY_URL=../../weasis-pacs-connector/weasis?&studyUID={}&target=_self |
| Unsecured* | from 5.19.1 to 5.22.1 | IID_PATIENT_URL=../../weasis-pacs-connector/weasis?&patientID={}&cdb&target=_self<br>IID_STUDY_URL=../../weasis-pacs-connector/weasis?&studyUID={}&cdb&target=_self |
| Secured | from 5.19.1 to 5.22.1 | IID_PATIENT_URL=../../weasis-pacs-connector/weasis?&patientID={}&target=_self&access_token={}<br>IID_STUDY_URL=../../weasis-pacs-connector/weasis?&studyUID={}&target=_self&access_token={} |
| Secured* | from 5.19.1 to 5.22.1 | IID_PATIENT_URL=../../weasis-pacs-connector/weasis?&patientID={}&cdb&target=_self&access_token={}<br>IID_STUDY_URL=../../weasis-pacs-connector/weasis?&studyUID={}&cdb&target=_self&access_token={} |
| Secured | from 5.22.2 | IID_PATIENT_URL=../../weasis-pacs-connector/weasis?patientID={{patientID}}&access_token={{access_token}}<br>IID_STUDY_URL=../../weasis-pacs-connector/weasis?studyUID={{studyUID}}&access_token={{access_token}} <br>IID_URL_TARGET=_self |
| Secured* | from 5.22.2 | IID_PATIENT_URL=../../weasis-pacs-connector/weasis?patientID={{patientID}}&cdb&access_token={{access_token}}<br>IID_STUDY_URL=../../weasis-pacs-connector/weasis?studyUID={{studyUID}}&cdb&access_token={{access_token}} <br>IID_URL_TARGET=_self |

</font>

\* Running only the local native version of Weasis (when not connected to a remote version - weasis.war -)


------------------------------------------------------------------------

### For dcm4chee-web3

![dcm4chee-web3](/gallery-dcm4chee/2Weasis%20in%20dcm4chee-web3.png?classes=border "dcm4chee-web3")

1. <a target="_blank" href="https://dcm4che.atlassian.net/wiki/spaces/ee2/pages/2555918/Installation">Install dcm4chee</a> (2.18.3 recommended), if not already done. For security see also how to limit the <a target="_blank" href="https://github.com/nroduit/openmediavault-dcm4chee/wiki/Configuration-of-dcm4chee#security">server access</a>.

2. Go <a target="_blank" href="http://sourceforge.net/projects/dcm4che/files/Weasis/">here</a> and download these following files.
{{% notice warning %}}
**Download issue**: Some browsers (like Internet Explorer) may rename war files to zip. If so, use the Save As option when downloading and change the name back to war.
{{% /notice %}}
    - From weasis-pacs-connector folder:
        - [weasis-pacs-connector.war] Requires the latest version 6.x, the version 7.x is not supported
        - [dcm4chee-web-weasis.jar]
    - From the folder with the latest version number (Optional if you want to run only the [native version](../) installed on the client system):
        - [weasis.war] requires at least Weasis 3.5.3
        - [weasis-i18n.war] Optional for [internationalization](../translating)
        - [weasis-ext.war] Optional package for additional plug-ins (e.g. exporting the images to build an ISO image for CD/DVD)

3. Place these files in the dcm4chee deploy folder (server/default/deploy/).

4. To activate Weasis, go to the JMX console (at `http://<your-host>:8080/jmx-console`)
    -   In *dcm4chee.web* select *service=WebConfig* and set these two values:
{{< highlight ini >}}
WebviewerNames = weasis
WebviewerBaseUrl = weasis:/weasis-pacs-connector/weasis
{{< /highlight >}}
{{% notice note %}}
This configuration allows launching Weasis with the [weasis protocol](../weasis-protocol) that requires the installation of the [native client](../)..
{{% /notice %}}
    - Click the *Apply Changes* button

5. Configure Weasis (This step is optional if you just want to keep the default configuration. It is required when the AETitle DCM4CHEE has been changed)
    The default configuration is stored in two files inside weasis-pacs-connector.war.
    To override the default configuration:

    - Download the current [download>weasis-connector-default.properties](https://raw.githubusercontent.com/nroduit/weasis-pacs-connector/6.x/src/main/resources/weasis-connector-default.properties) and rename it `weasis-pacs-connector.properties`, and download <a target="_blank" href="https://raw.githubusercontent.com/nroduit/weasis-pacs-connector/6.x/src/main/resources/dicom-dcm4chee.properties" download>dicom-dcm4chee.properties</a> (configuration of the dcm4chee archive)
    - Copy the files into a folder in the classpath of the servlet container. In JBoss (inferior to version 7), the best location would typically be server/default/conf.
    - Edit the configuration as needed.
        For example, dcm4chee may be running on a different computer than Weasis, or the AE Title of dcm4chee may have been changed.

        If so, edit *weasis-pacs-connector.properties* or *dicom-dcm4chee.properties* (e.g. pacs.host, pacs.port, pacs.aet...)
5.  That's all, now restart dcm4chee. To launch the viewer from the dcm4chee-web3 portal, the client computer must have installed the [Weasis package](../) on the operating system.
