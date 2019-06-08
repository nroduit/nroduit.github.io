---
title: Rebuild dcm4chee-web
decription: How to rebuild dcm4chee-web 2.15-2.17 to incorporate Weasis
keywords: [ "dcm4chee web", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 70
---

### Build dcm4chee-web 2.15.0, 2.16.2 or 2.17.0

#### Prerequisites

1.  Subversion (SVN), one of the following client:
    -   Subversion - The core system (server, client, libs)
    -   Subversive - SVN Team Client (Eclipse plugin)
    -   TortoiseSVN - Handy SVN client for Windows systems
2.  JDK 6 or higher
3.  Ant 1.6 or higher

#### Getting the Source

To check out the code, first install Subversion and either checkout the trunk branch using a graphical Subversion client (such as TortoiseSVN) or directly from the command line using the command:

{{< highlight bash >}}
$ svn co https://svn.code.sf.net/p/dcm4che/svn/weasis/weasis_dcm4chee/trunk/2.17.0 weasis-dcm4chee-2.17.0
{{< /highlight >}}

This command will copy the current development code (the "trunk") into a local directory named weasis-dcm4chee-2.17.0.

#### Building dcm4chee-web.war

1. Go in the weasis-dcm4chee directory
2. Compile and make the dcm4chee-web.war (in weasis-dcm4chee/dist folder)
{{< highlight bash >}}
$ ant dist
{{< /highlight >}}
3. Modify the permission in /dcm4jboss-web/src/etc/conf/dcm4chee-web/folder.permissions or in server/default/conf/dcm4chee-web if dcm4chee is already installed:

    > folder.\*=edit,move,delete,<span style="color:red">view</span>,\*export,edit.newStudyUID,mergepat,study\_permission,study\_permission.free\_role\_action,query\_has\_issuer folder.\*export=export\_tf,export\_xds
    >
    > ...
    >
    > folder=WebUser(send,<span style="color:red">view</span>);DatacareUser(edit,move,delete,export\_xds,<span style="color:red">view</span>);WebAdmin(\*)

4. Place the dcm4chee-web.war and the weasis.war to the deploy folder of dcm4chee

------------------------------------------------------------------------

### Rebuild dcm4chee-web from any version (Draft)

1. Make a project to rebuild dcm4chee-web
  - Download a dcm4chee package (any db package, ex. dcm4chee-2.14.7-mysql.zip)
  - Create new Java project (see example of dcm4chee-web 2.17.0, Eclipse project)
  - Extract dcm4chee-web.war
  - Link required binaries (commons-codec.jar,dcm4che.jar,dcm4chee-ejb-client.jar,jboss-j2ee.jar,servlet-api.jar,slf4j-api-1.6.1.jar) to the project from default/lib/ or from jboss 4.2.3 (if not installed in dcm4chee)
  - Link required binaries (maverick.jar and dcm4chee-web.jar) from ddcm4chee-web/WEB-INF/lib/
  - Add viewer.gif in dcm4chee-web/images
  - Add launcher.properties in dcm4chee-web/viewer
  - Add java sources in src folder
  - Move the content of the WEB-INF/classes in etc/message
  - Copy build.xml and modify it if necessary

2. Replace in maverick.xml:

    `<controller class="org.dcm4chex.archive.web.maverick.FolderSubmitCtrl" />` by `<controller class="org.dcm4chex.archive.web.maverick.FolderSubmitCtrl2" />`

3. Add text for Weasis button

    - in dcm4chee-web/translate.dtd `<!ENTITY ViewSelectedEntities "View selected Entities in Weasis">`
    - in dcm4chee-web/de/translate.dtd `<!ENTITY ViewSelectedEntities "Ausgewählte Entitäten in Weasis sehen">`
    - in dcm4chee-web/fr/translate.dtd `<!ENTITY ViewSelectedEntities "Visualiser la sélection dans Weasis">`
    - in dcm4chee-web/jp/translate.dtd `<!ENTITY ViewSelectedEntities "View selected Entities in Weasis">`

4. Modify dcm4chee-web/folder-tpl.xsl

    - Add after <xsl:param name="folder.delete" select="'false'" />
{{< highlight xml >}}
<xsl:param name="folder.view" select="'false'" />
{{< /highlight >}}
    - Add after `<xsl:if test="$folder.delete='true'"> … </xsl:if>`
{{< highlight xml >}}
<xsl:if test="$folder.view='true'">
   <td width="40">
       <input type="image" value="View" name="view" src="images/view.gif"
           alt="view" border="0" title="&ViewSelectedEntities;"
           onclick="return confirm('&ViewSelectedEntities;?')">
           <xsl:if test="total <= 0">
               <xsl:attribute name="disabled">disabled </xsl:attribute>
           </xsl:if>
       </input>
   </td>
</xsl:if>
{{< /highlight >}}
5. Rebuild WAR with "ant dist" and get dcm4chee-web.war in dist folder

6. Modify the permission in /dcm4jboss-web/src/etc/conf/dcm4chee-web/folder.permissions or in server/default/conf/dcm4chee-web if dcm4chee is already installed:

    > folder.\*=edit,move,delete,<span style="color:red">view</span>,\*export,edit.newStudyUID,mergepat,study\_permission,study\_permission.free\_role\_action,query\_has\_issuer folder.\*export=export\_tf,export\_xds
    >
    > ...
    >
    > folder=WebUser(send,<span style="color:red">view</span>);DatacareUser(edit,move,delete,export\_xds,<span style="color:red">view</span>);WebAdmin(\*)

7. Place the dcm4chee-web.war and the weasis.war to the deploy folder of dcm4chee
