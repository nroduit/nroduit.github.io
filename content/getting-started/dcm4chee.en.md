---
title: Embedding in dcm4chee
description: How installing Weasis to be the default web viewer of dcm4chee web interface
keywords: [ "dcm4chee", "dcm4chee web" , "dcm4chee integration", "dcm4chee viewer", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 10
---

This page describes how installing Weasis to be the default web viewer of dcm4chee web interface.

Weasis is launched from the dcm4chee administrative web interface, as shown in the pictures below. It may also be copied to a CD (or other removable devices) with images.

{{< gallery dir="gallery-dcm4chee" hover-effect="grow" />}} {{< load-photoswipe >}}
 
### For dcm4chee-arc-light


1. <a target="_blank" href="https://github.com/dcm4che/dcm4chee-arc-light/wiki">Install dcm4chee</a>, if not already done.
2. Go <a target="_blank" href="http://sourceforge.net/projects/dcm4che/files/Weasis/">here</a> and download these Weasis files.
{{% notice warning %}}
**Download issue**: Some browsers (Internet Explorer) may rename war files to zip. If so, use the Save As option when downloading and change the name back to war.
{{% /notice %}}
    - From the folder with the latest version number:
        - weasis.war
        - weasis-i18n.war (Optional for internationalization)
    - From weasis-pacs-connector folder:
        - weasis-pacs-connector.war

3. Open the <a target="_blank" href="http://localhost:9990/">wildfly management console</a> (at `http://<your-host>:9990`).
    - Select the “Deployments” tab
    - Add the .war files using the “Add” button (Choose Upload a new deployment or select Replace when the file already exists)

4. Configure weasis-pacs-connector 6.x and superior. The default configuration is stored in two files inside weasis-pacs-connector.war . To override the default configuration:
    - Download the current <a target="_blank" href="https://raw.githubusercontent.com/nroduit/weasis-pacs-connector/master/etc/dcm4chee-arc/weasis-pacs-connector.properties" download>weasis-pacs-connector.properties</a> and <a target="_blank" href="https://raw.githubusercontent.com/nroduit/weasis-pacs-connector/master/etc/dcm4chee-arc/dicom-dcm4chee-arc.properties" download>dicom-dcm4chee-arc.properties</a> (configuration of the dcm4chee archive)
    - Edit the configuration as needed. For example, dcm4chee may be running on a different computer than Weasis, or the AE Title of dcm4chee may have been changed. If so, edit `weasis-pacs-connector.properties` or `dicom-dcm4chee-arc.properties` (Change pacs.host, pacs.port, and pacs.aet).
    - Copy the `weasis-pacs-connector.properties` or `dicom-dcm4chee-arc.properties`  into wildfly/standalone/configuration
{{% notice tip %}}
Instead of copying the files into wildfly/standalone/configuration, JBoss Command Line Interface Console can be used to override files in the war. Add the two configuration files with the deployment-overlay command:<br>
{{% /notice %}}

        ``` text
        deployment-overlay add --name=dcm4chee-arc --deployments=weasis-pacs-connector.war --content=WEB-INF/classes/weasis-connector-default.properties=/tmp/weasis-pacs-connector.properties,WEB-INF/classes/dicom-dcm4chee-arc.properties=/tmp/dicom-dcm4chee-arc.properties --redeploy-affected
        ```

    - For applying the new configuration, from the management console "Disable" weasis-pacs-connector.war and then "Enable"
    - Optional: add new properties or arguments in the JNLP file, see the <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#configuration-of-weasis-pacs-connector">configuration of weasis-pacs-connector</a>

5. To activate Weasis in dcm4chee-arc-light user interface (required 5.10.2 or superior), you need need to changes two attributes in the configuration
    - Go to the <a target="_blank" href="http://localhost:8080/dcm4chee-arc/ui2/#/device/edit/dcm4chee-arc/dcmArchiveDevice/properties.dcmArchiveDevice">configuration</a>
        or from Configuration > Devices > dcm4chee-arc > Extensions > Archive Device 
        And fill up the following properties: 

        - Invoke Image Display Patient URL: `../../weasis-pacs-connector/IHEInvokeImageDisplay?requestType=PATIENT&patientID={}`
        - Invoke Image Display Study URL: `../../weasis-pacs-connector/IHEInvokeImageDisplay?requestType=STUDY&studyUID={}`
{{% notice tip %}}
**Absolute path**: The values above starting by "../" are the default relative path when weasis-pacs-connector is installed in the same JBoss as dcm4chee. Otherwise replace the relative URL by an absolute value, ex: `http://<your-host>:8080/weasis-pacs-connector/...`
{{% /notice %}}
{{% notice note %}}
<a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#new-way-to-launch-jnlp">The new way of launching Java Westart</a> file (jnlp) will also require an absolute URL as the scheme of the URL is different:<br>
`jnlp://<your-host>:8080/weasis-pacs-connector/...`<br> `jnlps://<your-host>:8443/weasis-pacs-connector/...` (TLS connection)<br> Replace "\<your-host\>" with your server hostname
{{% /notice %}}

    - Refresh the web page and the view button should appear as in the screenshot above

    - An alternative way to configure the activation is with an LDAP manager (like Apache Directory Studio)

        1.  Connect to LDAP, see <a target="_blank" href="https://github.com/dcm4che/dcm4chee-arc-light/wiki/Installation#import-default-configuration-into-ldap-server">dcm4chee configuration</a>
        2.  Import <a target="_blank" href="/attachments/weasis.ldif" download>weasis.ldif</a>

------------------------------------------------------------------------

### For dcm4chee-web3

1. <a target="_blank" href="https://dcm4che.atlassian.net/wiki/spaces/ee2/pages/2555918/Installation">Install dcm4chee</a>, if not already done. For security see also how to limit the <a target="_blank" href="https://github.com/nroduit/openmediavault-dcm4chee/wiki/Configuration-of-dcm4chee#security">server access</a>.
    - dcm4chee-web3 is not compatible with versions of dcm4chee before 2.16.0
    - dcm4chee 2.16.0 to 2.17.0 are compatible with dcm4chee-web3, but the older dcm4chee-web is installed by default.
    - For dcm4chee 2.17.1+, dcm4chee-web3 is already installed. To check if it is the latest version, start dcm4chee-web3 (`http://<your-host>:8080/dcm4chee-web3/`), log in, and mouse over the dcm4chee.org icon in the upper right corner.

2. Go <a target="_blank" href="http://sourceforge.net/projects/dcm4che/files/Weasis/">here</a> and download these Weasis files.
{{% notice warning %}}
**Download issue**: Some browsers (Internet Explorer) may rename war files to zip. If so, use the Save As option when downloading and change the name back to war.
{{% /notice %}}
    - From the folder with the latest version number:
        - weasis.war
        - weasis-i18n.war (Optional for internationalization)
    - From weasis-pacs-connector folder:
        - dcm4chee-web-weasis.jar
        - weasis-pacs-connector.war

3. Place these files in the dcm4chee deploy folder (server/default/deploy/).

4. To activate Weasis, go to the JMX console (at `http://<your-host>:8080/jmx-console`)
    -   In *dcm4chee.web* select *service=WebConfig* and set these two values:

            WebviewerNames = weasis
            WebviewerBaseUrl = NONE

        From weasis-pacs-connector 5.0 WebviewerBaseUrl can have different values:

        - Launch Weasis as an external application (default value when NONE): WebviewerBaseUrl = `weasis:/weasis-pacs-connector/viewer`
        - Launch Weasis as an Applet in the web browser (not recommended as several browsers block Java plugin) : WebviewerBaseUrl = `weasis:/weasis-pacs-connector/viewer-applet`

        - Launching Weasis from jnlp protocol. The new way of <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#new-way-to-launch-jnlp">launching Java Westart</a> file (jnlp) will require an absolute URL:

            - weasis:jnlp://\<your-host\>:8080/weasis-pacs-connector/viewer
            - weasis:jnlps://\<your-host\>:8443/weasis-pacs-connector/viewer
{{% notice warning %}}
Replace "\<your-host\>" with your server hostname
{{% /notice %}}

            From dcm4chee 2.18.3, it possible to reuse the default host name of dcm4chee:

            - weasis:jnlp://${server.host}:8080/weasis-pacs-connector/viewer
            - weasis:jnlps://${server.host}:8443/weasis-pacs-connector/viewer

    - Click the *Apply Changes* button

5. Configure Weasis (This step is optional if you just want to keep the default configuration. It is required when the AETitle DCM4CHEE has been changed)
    The default configuration is stored in two files inside weasis-pacs-connector.war.
    To override the default configuration:

    - According to the version of  weasis-pacs-connector:
        - weasis-pacs-connector 4.x and 5.x: Download <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector/raw/58221aeed3d2abc1929c0753ebeaa53c67fcc46a/src/main/resources/weasis-connector-default.properties" download>weasis-connector-default.properties</a> and rename it `weasis-pacs-connector.properties`

        - weasis-pacs-connector 6.x and superior: Download the current <a target="_blank" href="https://raw.githubusercontent.com/nroduit/weasis-pacs-connector/master/src/main/resources/weasis-connector-default.properties" download>weasis-connector-default.properties</a> and rename it `weasis-pacs-connector.properties`, and download <a target="_blank" href="https://raw.githubusercontent.com/nroduit/weasis-pacs-connector/master/src/main/resources/dicom-dcm4chee.properties" download>dicom-dcm4chee.properties</a> (configuration of the dcm4chee archive)

    - Copy the files into a folder in the classpath of the servlet container. In JBoss (inferior to version 7), the best location would typically be server/default/conf.
    - Edit the configuration as needed.
        For example, dcm4chee may be running on a different computer than Weasis, or the AE Title of dcm4chee may have been changed.

        If so, edit *weasis-pacs-connector.properties* or *dicom-dcm4chee.properties* for weasis-pacs-connector 6.x. Edit the properties: pacs.host, pacs.port, pacs.aet...
    - Optional: add new properties or arguments in the JNLP file, see <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#configuration-of-weasis-pacs-connector">configuration of weasis-pacs-connector</a>

5.  That's all, now restart dcm4chee and launch Weasis from the dcm4chee-web3 portal.

------------------------------------------------------------------------

### For dcm4chee-web (old web interface - before 2.17.1)

1. Go <a target="_blank" href="http://sourceforge.net/projects/dcm4che/files/Weasis/">here</a> and download:
    - The last Weasis version: weasis.war
    - The Weasis internationalization (translation): weasis-i18n.war (optional)
    - The modified <a target="_blank" href="http://sourceforge.net/projects/dcm4che/files/Weasis/dcm4chee-web/">dcm4chee web interface</a> dcm4chee-web/*version*/dcm4chee-web.war)
{{% notice info %}}
**dcm4chee version**:   dcm4chee-web.war has been built only for some dcm4chee versions. For other versions see [rebuild dcm4chee-web](../../basics/customize/rebuild-dcm4chee-web) from any version.
{{% /notice %}}

2. Place these three files into the deploy folder (server/default/deploy/) of dcm4chee.

3. Modify the permission in /dcm4jboss-web/src/etc/conf/dcm4chee-web/folder.permissions or in server/default/conf/dcm4chee-web if dcm4chee is already installed:

    > folder.\*=edit,move,delete,<span style="color:red">view</span>,\*export,edit.newStudyUID,mergepat,study\_permission,study\_permission.free\_role\_action,query\_has\_issuer folder.\*export=export\_tf,export\_xds
    >
    > ...
    >
    > folder=WebUser(send,<span style="color:red">view</span>);DatacareUser(edit,move,delete,export\_xds,<span style="color:red">view</span>);WebAdmin(\*)

4. That's all, now restart dcm4chee and launch Weasis from the web portal.

------------------------------------------------------------------------

### Write weasis-portable to DICOM CDs with dcm4chee-cdw

1. Install <a target="_blank" href="http://sourceforge.net/projects/dcm4che/files/dcm4chee-cdw/">dcm4chee-cdw</a> (see doc/INSTALL.txt in the archive)
2. Extract <a target="_blank" href="http://sourceforge.net/projects/dcm4che/files/Weasis/">weasis-portable.zip</a> into the ../dcm4chee/server/default/data/mergedir directory
3. Go to the dcm4che jmx console (dcm4chee.cdw):
    - Select the MediaCreationMgtSCP item and set to `true` the value of DefaultIncludeDisplayApplication
    - Select the MakeIsoImage item and set to `4` the value of isoLevel
4. Click on the *Apply Changes* button
{{% notice tip %}}
**Embedding a Java Runtime for Windows**: The executable (viewer-win32.exe) allows to embed a JRE in the relative directory "jre/windows" (e.g. weasis-portable/jre/windows/bin/java.exe). To support 32 and 64-bit architecture, copy 32-bit Java Runtime from its installed directory.<br>
<br>Note: the embedded Java Runtime is used only when no runtime is available on the system. When Java is run from CD, it could be a little slow.
{{% /notice %}}
