---
title: Guidelines
description: Guidelines for Weasis plugin development
keywords: [ "guidelines", "weasis guidelines", "development", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 50
---


## <center>Weasis Plugin Development</center>

This page describes the necessary configurations to be able to debug Weasis using an IDE. For developers who want to create new plugins, you can visit [How to build and install a plugin](../../basics/customize/build-plugins).

We recommend the use of [IntelliJ IDEA](https://www.jetbrains.com/idea/) because the following instructions are based on it. Nevertheless, it is possible to use other IDEs by configuring weasis-launcher with similar instructions described in [Add a launcher](#add-a-launcher).
### Prerequisites

1. Install [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community or Ultimate Edition 2024.3 or higher)
2. Use JDK {{< param jdkVersion >}} or higher and set the language level to `SDK Default` in *File > Project Structure... >*.<br>Required Maven version is {{< param mavenVersion >}} or higher.
3. In _File > Settings... > Plugins_ install google-java-format plugin from Marketplace and enable it from *google-java-format Settings*

### Code style and convention

Weasis uses [google-java-format](https://github.com/google/google-java-format) as coding conventions. The format can be applied by Maven through the [Spotless plugin](https://github.com/diffplug/spotless/tree/main/plugin-maven) or from the [IDE](https://github.com/google/google-java-format#intellij-android-studio-and-other-jetbrains-ides) (by importing the IntelliJ Java Google Style file). Formatting code with an IDE is not 100% compatible with Spotless, so it is better to use the latter before submitting new commits. This guarantees identical code formatting regardless of the system or code editor used.

- From Maven command: `mvn spotless:apply`
- From the Maven panel
![Maven Spotless](/images/conf/mvn-spotless.png)

### Getting the source and building Weasis

- Getting the Source
  - For external Git client, see [Building Weasis](../building-weasis).
  - From IntelliJ IDEA: *New > Project from Version Control...*
    - In the *Get from Version Control* dialog, select the menu *Repository URL* and enter the following URL: `https://github.com/nroduit/Weasis.git` (public repository)
- Building Weasis plugins
  - In the maven panel, select clean/install in Lifecycle of *weasis-framework (root)* to compile and to install all the plugins in the local Maven repository.

{{% notice tip %}}
* It is possible to use a JVM Option (e.g. `-Dweasis.arch=linux-x86-64`) to limit the build of native plugins only to the architecture of the current system (do not use this option when building the distribution).
* See also building the final [Weasis Distributions](../building-weasis#building-native-binaries-and-installers)
{{% /notice %}}  

### Add a launcher

For running or debugging Weasis, you need to create a launcher:

- Open *Run > Edit Configurations...*
- Create a new *Application*
  - Select *weasis-launcher* as a module (field starting by *-cp*)
  - Main Class: browse *org.weasis.launcher.AppLauncher*
  - Click on *Modify Options*
    - Select *Add dependencies with "Provided" scope to classpath*
    - Select *Do not build before run*
    - Select *Add VM Options* and enter `-Xms64m -Xmx768m -Dgosh.port=17179`
  - Working Directory: remove the current value and add *%MODULE_WORKING_DIR%* from the Insert Macros button
![Launcher Configuration](/images/conf/launcher.png)
{{% notice note %}}
As the default build task has been removed it is necessary to apply the Maven command *install* on modules with modified code before launching the *Run* or *Debug* mode.<br>
Keeping the build task and delegating the build to Maven does not seem configurable for a multi-module project, see this [issue](https://youtrack.jetbrains.com/issue/IDEA-198358).
{{% /notice %}}

- Examples of launching parameters by entering values in the *Program arguments* text box
  - Loading DICOM files from a local path:
{{< highlight text >}}
$dicom:get -l \"D:\images test\dicom\"
{{< /highlight >}}
{{% notice note %}}
Some command interpreters need to escape the quotes or double quotes required for paths or URLs. This is the case with IntelliJ IDEA or Eclipse.<br>
For more commands at startup see also [Weasis commands](../../basics/commands).
{{% /notice %}}
{{% notice warning %}}
In Eclipse launcher parameters, '&' within URLs needs to be escaped with a backslash.
{{% /notice %}}
- Examples of other VM options for overriding the default [Preferences](../../basics/customize/preferences)
  - Removing the possibility of exporting DICOM: `-Dweasis.export.dicom=false`
  - Defines a new user (for getting specific preferences): `-Dweasis.user=user1`
  - Examples with specific configuration files:
    - For launching Weasis Dicomizer: `-Dfelix.extended.config.properties=file:target/conf/dicomizer.json`
    - Configuration from an URL: `-Dfelix.extended.config.properties=https://mysite.com/weasis/conf/config.json`
{{% notice note %}}
**felix.config.properties** defines the location of base.json (the OSGI configuration and the list of plugins to install/start)<br>
**felix.extended.config.properties** defines the location of a json file (extends/overrides base.json)
{{% /notice %}}
