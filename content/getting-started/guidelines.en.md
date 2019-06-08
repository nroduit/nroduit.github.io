---
title: Guidelines
description: Guidelines for Weasis plug-in development
keywords: [ "guidelines", "weasis guidelines", "development", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 50
---


## <center>Weasis Plug-in Development</center>

This page is intended for developers who want to contribute to Weasis and it is a recommendation for developers who want to create their own plug-ins, see also [How to build and install a plug-in](../../basics/customize/build-plugins).

We highly recommend the use of Eclipse IDE, because all the following instructions are based on it and some settings and the coding conventions can be imported directly into Eclipse. Nevertheless, for having a better Maven integration, it is possible to use IntelliJ IDEA or Netbeans by configuring weasis-launcher with similar instructions described in [Debug or Run from Eclipse](#debug-or-run-from-eclipse).

### Prerequisites

1. JDK 8 or higher
2. Recent version of Eclipse IDE

### Install Java and Eclipse

- JDK 8 or higher (Oracle JDK is recommended for Linux)
{{% notice note %}}
JRE is not suitable for m2eclipse.
{{% /notice %}}
- <a target="_blank" href="http://www.eclipse.org/downloads/eclipse-packages/">Eclipse IDE for Java Developers</a> (at least 4.2.2)

### Configure Eclipse

-  You can edit the VM options of the <a target="_blank" href="http://wiki.eclipse.org/Eclipse.ini">eclipse.ini</a> file in your eclipse folder. For instance, the maximum memory for the JVM or the JVM location can be specified.
-  Start Eclipse and select the path of the Weasis workspace
{{% notice note %}}
It is recommended to create a new Workspace for keeping a specific Weasis configuration.
{{% /notice %}}
-  Go to *Window > Preferences > Java > Installed JREs > Execution Environments* and select the installed JDK for JavaSE-1.8
- In *Window > Preferences > General > Workspace*
    - Select UTF-8 for *Text file encoding*
    - Select Unix for *New text file line delimiter*

### Code style and convention

Weasis adheres to <a target="_blank" href="https://docs.oracle.com/javase/specs/">the Java Language Specification</a>. Here are some code style specifications:

1. Maximum line length is 120 characters.
2. Use spaces instead of tabs.
3. Indentation size is 4 spaces.
4. Do not insert a new line before opening brace. Insert a new line before closing brace.
5. Use fully qualified import statements, i.e. do not use asterisks.

Code style specifications can be imported into Eclipse:

1. Download the <a target="_blank" href="/attachments/weasis-eclipse-formatting.xml" download>Weasis code style format</a>
1. In *Window > Preferences > Java > Code Style > Formatter*, click on *Import* and select the *weasis-eclipse-formatting.xml* file
1. Press *OK* after importing

<!-- -->
1. Download the <a target="_blank" href="/attachments/weasis-eclipse-cleanup.xml" download>Weasis clean up code style</a>
1. In *Window > Preferences > Java > Code Style > Clean Up* , click on *Import* and select the *weasis-eclipse-cleanup.xml* file
1. Press *OK* after importing

<!-- -->
1. Download the <a target="_blank" href="/attachments/weasis-code-style-template.xml" download>Weasis code template</a>
1. In *Window > Preferences > Java > Code Style > Code Templates* , click on *Import* and select the *weasis-code-style-template.xml* file
1. Press *OK* after importing

### Getting the source and building Weasis from Eclipse

- Getting the Source
    - For external Git client, see [Building Weasis](../building-weasis).
    - From Eclipse Git perspective: *Window > Open Perspective > GIT Repository Exploring*. Click on button "Clone a GIT repository".
    - In the *New* dialog, Add one of the following URIs:
        - `https://github.com/nroduit/Weasis.git` (public repository)
        - `https://weasis.repositoryhosting.com/git/weasis/weasis-dev.git` (private repository for developers, enter your login)
    - Press, *Next* and then *Finnish*
    - From Eclipse menu, open *File > Import...*
    - In the *New* dialog, select *Maven > Existing Maven Projects*, click *Next* and select the "Weasis" or "weasis-dev" directory.
    - As it is generally not necessary to get all the Maven projects visible into Eclipse, *Deselect* *All* and select only the plugins you are interested in (at least weasis-launcher and weasis-framework).
{{% notice tip %}}
See <a target="_blank" href="http://wiki.eclipse.org/EGit/User_Guide">Egit documentation</a>
{{% /notice %}}

<!-- -->
- Building Weasis plug-ins
    - Select the *weasis-framework* project (or the pom.xml in the project)
    - Right click, *Run as > Maven Install* (Compiling and installing all the plug-ins in the local Maven repository)
    - Or run a custom Maven build entry in the *Run As* menu
        - Example for building Weasis
        - Select the *weasis-framework* project
        - Right click, *Run as > Run Configurations...*
![Maven configuration](/images/conf/mvn-run-cfg.png)
{{% notice warning %}}
Getting errors on the projects. Try the following instructions:

- Right-click on the project and *Maven > Update Project Configuration*
- Right-click on the project and select *Refresh*
- *Project > Update All Maven Dependencies*
- *Project > Clean all projects*
- Right-click *Close Project* and then *Open Project*
{{% /notice %}}
{{% notice note %}}
If you have Maven installed on your system or TM terminal Eclipse plugin, it is sometimes easier to type the maven commands directly in a console.
{{% /notice %}}


- Building Weasis Distributions
    - Requires to have installed all the plug-ins as described just the item above
    - If *weasis-distributions* project is not in the *Package Explorer* list, import it:
        - Open *File > Import...*
        - In the *Import* dialog, select *Maven > Existing Maven Projects*, click *Next*
        - Click on *Browse* and select the *weasis-distributions* folder (in yourWorkspace/weasis-framework)
        - Press *Select All* and *Finnish*
    - Select the *weasis-distributions* project
    - Right click, *Run as > Maven Install*
{{% notice note %}}
The distribution files are located in the *target/dist* folder of the project.<br> See [Building Weasis from source](../building-weasis) for more advanced options.
{{% /notice %}}

### Debug or Run from Eclipse

For debugging Weasis, you need to create a Debug configuration:

- Open *Run > Debug Configurations...*
- Create a new *Java Application*
- In the *Main* tab, enter:
    - Project: weasis-launcher
    - Main Class: org.weasis.launcher.WeasisLauncher
- In the *Arguments* tab
    - Program arguments, examples for loading DICOM locally:
{{< highlight text >}}
$dicom:get -l "D:\\images\\dicom"
{{< /highlight >}}
{{% notice note %}}
For more commands at startup see [Weasis commands](../../basics/commands).
{{% /notice %}}
{{% notice warning %}}
In Eclipse launcher parameters, '&' within URLs needs to be escaped with a backslash.
{{% /notice %}}
    - VM arguments, minimal configuration:
{{< highlight text >}}
-Xms64m -Xmx768m -Dgosh.args="-sc telnetd -p 17179 start"
{{< /highlight >}}
    - Other VM arguments, exemples with specific configuration files:
        - For Launching Weasis Dicomizer:
{{< highlight text >}}
-Dfelix.extended.config.properties=file:target/conf/ext-dicomizer.properties
{{< /highlight >}}
        - Configuration from an URL:
{{< highlight text >}}
-Dfelix.extended.config.properties=file:http://mysite.com/weasis/conf/ext-config.properties
{{< /highlight >}}
{{% notice note %}}
Meaning of the properties (see also [Preferences](../../basics/customize/preferences)):<br>
**felix.config.properties** defines the location of config.properties (the OSGI configuration and the list of plug-ins to install/start)<br>
**felix.extended.config.properties** defines the location of ext-config.properties (extends/overrides config.properties)
{{% /notice %}}
