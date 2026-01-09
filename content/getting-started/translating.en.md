---
title: Internationalization
description: How to contribute to the Weasis translation
keywords: [ "internationalization", "weasis internationalization", "development", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 80
---

Translation files are hosted and managed on the [Transifex](https://app.transifex.com/weasis/public/) website. Get an account and help to translate to your language! If your language is missing, just head over to Transifex and request a new language.

{{% notice warning %}}
**Text length**: The translations for many languages frequently exceed the length of the corresponding English source. It could be a problem for the layout of graphical components (e.g., buttons). Some elements have a character limit on the translation tool.
{{% /notice %}}

{{% notice tip %}}
**Special characters**: Some characters representing values (%d, %s), newline (\\n) and HTML tags must not be translated. For other translating recommendations, see <a target="_blank" href="https://docs.transifex.com/#translating">Transifex help</a><br>
For special words or particular contexts look at the "Instructions" text box (gives explanations or definitions).
{{% /notice %}}

## Building Weasis-i18n

[weasis-i18n](https://github.com/nroduit/weasis-i18n) is the internationalization project (i18n) of Weasis. As a separate project, it can have its own release cycle. The [OSGi](https://www.osgi.org) fragments of plugins contain only the translation files which are merged during runtime to the matching module of the application.

To obtain daily built packages, see this [page](https://github.com/nroduit/weasis-i18n).

{{% notice note %}}
That means the translation packages can be deployed at any time; it does not need to follow the Weasis life cycle. With remote packages, the plugin translation will be updated by Weasis only if the timestamp number has changed. This timestamp is set during the build phase described below.
{{% /notice %}}

{{% notice info %}}
Additional projects to obtain a full translation of Weasis:<br>
The [java-swing-dialogs](https://app.transifex.com/weasis/java-swing-dialogs) translations must be updated manually in the weasis-launcher module and [docking-frames](https://app.transifex.com/weasis/docking-frames) translations must be packaged witin the library.
{{% /notice %}}

### Prerequisites

1. JDK 11 or higher
2. Maven 3 or higher<br>
    If your computer is behind a proxy server, [configure maven](https://maven.apache.org/guides/mini/guide-proxies.html).
3. Git or directly download the source code from [GitHub](https://github.com/nroduit/weasis-i18n)

### Getting the Source

To clone the repository, first install GIT and either clone using a graphical GIT client (such as Tortoise Git) or directly from the command line using the command:

{{< highlight bash >}}
$ git clone https://github.com/nroduit/weasis-i18n.git
{{< /highlight >}}

### Build the distribution

Go in the *weasis-i18n* directory, Compile and install all the plugins in the local Maven repository

{{< highlight bash >}}
$ mvn clean install -Dtransifex.token="<your-token>"
{{< /highlight >}}

All the APIs require to be authenticated. So the value "your-token" must be replaced by your generated token, see how to [get this token](https://docs.transifex.com/account/authentication) on Transifex.

Command if you are behind a proxy server:
{{< highlight bash >}}
$ mvn clean install -DproxySet=true -DproxyHost="host" -DproxyPort="port" -Dtransifex.token="<your-token>"
{{< /highlight >}}

{{% notice info %}}
The distribution files are located in the *weasis-i18n-dist/target/dist* folder.
{{% /notice %}}

### Apply the translations

The translation package can be built manually as described below, or it is automatically built every 24 hours and can be downloaded from [here](https://github.com/nroduit/weasis-i18n#download-the-binary-package). When [Building Weasis](building-weasis), the last package is downloaded automatically.

* In order to update Weasis with new translations, unzip weasis-i18n.zip and either:
  * Pass the weasis.i18n location into the [launch command](weasis-protocol/#modify-the-launch-parameters):
{{< highlight bash >}}
$weasis:config pro="weasis.i18n <your-uri>"
$weasis:config pro="weasis.i18n file:/home/weasis-i18n-dist-4.0.0-SNAPSHOT"
$weasis:config pro="weasis.i18n https://<your-domain>/weasis-i18n-dist-4.0.0"
{{< /highlight >}}
  * Replace the files in the "bundle-i18n" folder where Weasis is installed (not possible when Weasis is distributed from an application store or the Mac signed package).

{{% notice note %}}
weasis-launcher-i18n cannot be updated dynamically as the launcher is not an OSGi module. It must be imported manually into the Weasis source (weasis-launcher).
{{% /notice %}}

{{% notice tip %}}
See [how to change the language in the Weasis preferences](../tutorials/locale).
{{% /notice %}}



