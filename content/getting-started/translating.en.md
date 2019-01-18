---
title: Internationalization
description: How to contribute to the Weasis translation
keywords: [ "internationalization", "weasis internationalization", "development", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 80
---

The translation files are now hosted and managed on <a target="_blank" href="https://www.transifex.com/weasis/public/">Transifex</a> website. Get an account at <a target="_blank" href="https://www.transifex.com/signin">Transifex</a> and help to translate to your language! If your language is missing, just head over to Transifex and request a new language.

{{% notice warning %}}
**Text length**: The translations for many languages frequently exceed the length of the corresponding English source. It could be a problem for the layout of graphical components (e.g. buttons).
{{% /notice %}}

{{% notice tip %}}
**Special characters**: Some characters representing values (%d, %s), newline (\\n) and HTML tags must not be translated. For other translating recommendations, see <a target="_blank" href="https://docs.transifex.com/#translating">Transifex help</a><br>
For special words or particular contexts look at the "Instructions" text box (gives explanations or definitions).
{{% /notice %}}


## Building Weasis-i18n

<a target="_blank" href="https://github.com/nroduit/weasis-i18n">weasis-i18n</a> is the internationalization project (i18n) of Weasis. As a separate project, it can have its own release cycle. The <a target="_blank" href="https://www.osgi.org">OSGi</a> fragments of plug-ins contain only the translation files which are merged during runtime to the matching module of the application.

{{% notice note %}}
That means the weasis-i18n.war file can be deployed at any time, it does not need to follow the Weasis life cycle. The plug-in translation will be updated by Weasis only if the timestamp number has changed. This timestamp is set during the build phase described below.
{{% /notice %}}

{{% notice info %}}
**Additional projects to obtain a full translation of Weasis:**<br>
The <a target="_blank" href="https://www.transifex.com/organization/weasis/dashboard/java-swing-dialogs">java-swing-dialogs</a> translations must be updated manually in the weasis-launcher module and <a target="_blank" href="https://www.transifex.com/weasis/docking-frames">docking-frames</a> translations must be packaged with the library.
{{% /notice %}}

### Prerequisites

1.  JDK 8 or higher
2.  Maven 3 or higher<br>
    If your computer is behind a proxy server, <a target="_blank" href="http://maven.apache.org/guides/mini/guide-proxies.html">configure maven</a>.
3.  Git or directly download the source code from <a target="_blank" href="https://github.com/nroduit/weasis-i18n">GitHub</a>

### Getting the Source

To clone the repository, first install GIT and either clone using a graphical GIT client (such as Tortoise Git) or directly from the command line using the command:

{{< highlight bash >}}
$ git clone https://github.com/nroduit/weasis-i18n.git
{{< /highlight >}}

### Build the distribution

Go in the *weasis-i18n* directory, Compile and install all the plug-ins in the local Maven repository

{{< highlight bash >}}
$ mvn clean install -Dtransifex.credential="username:password"
{{< /highlight >}}

All of the API calls on Transifex require the user to be authenticated. So the value "username:password" must be replaced by your credential, see how to <a target="_blank" href="https://www.transifex.com/signin">create an account</a> on Transifex.

Command if you are behind a proxy server:
{{< highlight bash >}}
$ mvn clean install -DproxySet=true -DproxyHost="host" -DproxyPort="port"; -Dtransifex.credential="username:password"
{{< /highlight >}}

{{% notice info %}}
The distribution files are located in the *weasis-i18n-dist/target/dist* folder. weasis-i18n.war must be placed in the same base context as weasis.war (if in other web context, the value of the property *weasis.i18n* in JNLP file must be adapted).<br><br>
To update translation packs in weasis-portable, unzip weasis-i18n.zip and replace files in weasis-portable/weasis/bundle-i18n/.
{{% /notice %}}

{{% notice note %}}
weasis-launcher-i18n cannot be updated dynamically as the launcher is not an OSGi module. It must be imported in the Weasis source (weasis-launcher).
{{% /notice %}}
