---
title: Guidelines
description: Guidelines for Weasis plug-in development
keywords: [ "guidelines", "weasis guidelines", "development", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 50
---


## <center>Weasis Plug-in Development</center>

This page describes the necessary configurations to be able to debug Weasis using an IDE. For developers who want to create new plug-ins, you can visit [How to build and install a plug-in](../../basics/customize/build-plugins).

We recommend the use of [IntelliJ IDEA](https://www.jetbrains.com/idea/) because the following instructions are based on it. Nevertheless, it is possible to use other IDEs by configuring weasis-launcher with similar instructions described in [Add a launcher](#add-a-launcher).

{{% notice tip %}}
See also building the final [Weasis Distributions]((../building-weasis#building-weasis-distributions))
{{% /notice %}}  

### Prerequisites

1. Install [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community or Ultimate Edition)
2. In *File > Settings... > Plugins* install google-java-format plugin from Marketplace and enable it from *google-java-format Settings*

### Code style and convention

Weasis uses [google-java-format](https://github.com/google/google-java-format) as coding conventions. The format can be applied by Maven through the [Spotless plugin](https://github.com/diffplug/spotless/tree/main/plugin-maven) or a plugin in the IDE.

- From Maven command: `mvn spotless:apply`
- From the Maven panel
![Maven Spotless](/images/conf/mvn-spotless.png)

### Getting the source and building Weasis

- Getting the Source
  - For external Git client, see [Building Weasis](../building-weasis).
  - From IntelliJ IDEA: *New > Project from Version Control...*
    - In the *Get from Version Control* dialog, select the menu *Repository URL* and enter the following URL: `https://github.com/nroduit/Weasis.git` (public repository)
- Building Weasis plug-ins
  - In *File > Project Structure...* select JDK 11 or higher as *Project SDK* and 8 as *Project language level*
  - In the maven panel, select clean/install in Lifecyle of *weasis-framework (root)* to compile and to install all the plug-ins in the local Maven repository

### Add a launcher

For running or debugging Weasis, you need to create a launcher:

- Open *Run > Edit Configurations...*
- Create a new *Application*
  - Select *weasis-launcher* as a module (field starting by *-cp*)
  - Main Class: browse *org.weasis.launcher.AppLauncher*
  - Click on *Modify Options*
    - Select *Include dependencies with "Provided" scope*
    - Select *Add before launch task* and remove the task *Build*
    - Select *Add VM Options* and enter `-Xms64m -Xmx768m -Dgosh.port=17179 --illegal-access=warn`
  - Working Directory: remove the current value and add *%MODULE_WORKING_DIR%* from the Insert Macros button
![Launcher Configuration](/images/conf/launcher.png)<br>
- Examples of launching parameters by entering values in the *Program arguments* text box
  - Loading DICOM files from a local path:
{{< highlight text >}}
$dicom:get -l \"D:\images test\dicom\"
{{< /highlight >}}
{{% notice note %}}
Some command interpreters need to escape the quotes or double quotes required for paths or URLs. This is the case with IntelliJ IDEA or Eclipse.<br>
For more commands at startup see also [Weasis commands](../../basics/commands).
{{% /notice %}}
{{% notice warning %}}
In Eclipse launcher parameters, '&' within URLs needs to be escaped with a backslash.
{{% /notice %}}
- Examples of other possible VM options for overriding the default [Preferences](../../basics/customize/preferences)
  - Removing the possibility of exporting DICOM: `-Dweasis.export.dicom=false`
  - Defines a new user (for getting specific preferences): `-Dweasis.user=user1`
  - Examples with specific configuration files:
    - For launching Weasis Dicomizer: `-Dfelix.extended.config.properties=file:target/conf/ext-dicomizer.properties`
    - Configuration from an URL: `-Dfelix.extended.config.properties=https://mysite.com/weasis/conf/ext-config.properties`
{{% notice note %}}
**felix.config.properties** defines the location of config.properties (the OSGI configuration and the list of plug-ins to install/start)<br>
**felix.extended.config.properties** defines the location of ext-config.properties (extends/overrides config.properties)
{{% /notice %}}
