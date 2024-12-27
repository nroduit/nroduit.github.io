---
title: Building Weasis
description: How to build Weasis from sources
keywords: [ "building", "sources", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 30
---

These instructions guide you through building Weasis directly from its GitHub repository. For IDE-based builds, refer to the [Weasis plug-in development guidelines](../guidelines).

**Prerequisites**

1. JDK {{< param jdkVersion >}} or higher
2. Maven {{< param mavenVersion >}} or higher<br>
   If your computer is behind a proxy server, refer to the [Maven proxy configuration guide](https://maven.apache.org/guides/mini/guide-proxies.html).
3. Git

### Getting the Source Code

In order to clone the repository, install Git and either use a graphical client or run the following command in a terminal:

{{< highlight shell >}}
git clone https://github.com/nroduit/Weasis.git
{{< /highlight >}}

### Building All Plug-ins
- Navigate to the root directory of the cloned `Weasis` repository, compile and install all plug-ins into the local Maven repository:
{{< highlight shell >}}
mvn clean install
{{< /highlight >}}

- Package `weasis-native.zip` (located in `target/native-dist/`), since {{% badge title="Version" %}}4.0.0{{% /badge %}} :
{{< highlight shell >}}
mvn -P compressXZ -f weasis-distributions clean package
{{< /highlight >}}
{{% notice tip %}}
**-P compressXZ**: Option for compressing the packages in [xz](https://en.wikipedia.org/wiki/XZ_Utils), only from Weasis 3.6.0. The compression pack200 is not supported anymore (removed from Java 14), before 3.6.0 the profile was **-P pack200**.<br>
{{% /notice %}}
{{% notice tip %}}
**-P purgeI18nPackage**: Option to delete the translation package in the local maven repository (active by default). To disable this option, add `-` before the profile:
{{< highlight bash >}}
mvn -P compressXZ,-purgeI18nPackage -f weasis-distributions clean package
{{< /highlight >}}
{{% /notice %}}
{{% notice warning %}}
For production, the version must not include SNAPSHOT (as packages with a SNAPSHOT are always downloaded, not cached). To remove SNAPASHOT or create your own release (use a specific name to prevent package conflicts in the cache), update the changelist property. From the Weasis root folder, execute:
{{< highlight shell >}}
mvn -Dchangelist=-mybuild-beta clean install
mvn -Dchangelist=-mybuild-beta -P compressXZ -f weasis-distributions clean package
{{< /highlight >}}
{{% /notice %}}


### Building native binaries and installers

Starting with {{% badge title="Version" %}}4.0.0{{% /badge %}}, the native installer has fully replaced the portable and Java WebStart distributions.

The [official build process](https://github.com/nroduit/Weasis/blob/master/.github/workflows/build-installer.yml) is executed via GitHub Actions using [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners) across Linux, macOS, and Windows.

However, you can also build the native binaries and installer locally using the `package-weasis.sh` script. This process is not guaranteed to work on all systems, as it requires proper configuration of multiple tools. Refer to the [jpackage prerequisites](https://docs.oracle.com/en/java/javase/20/jpackage/packaging-overview.html) for more details.


- Obtain the `weasis-native.zip` file, extract the archive, and navigate to the root folder in a Bash prompt.
- Run the following command to build the native binaries and installer:
{{< tabs groupid="build-native" >}}
{{% tab title="Bash" %}}
{{< highlight shell >}}
./build/script/package-weasis.sh --jdk "/home/.jdks/openjdk-{{< param jdkVersion >}}"
{{< /highlight >}}
{{% /tab %}}
{{< /tabs >}}

{{% notice note %}}
- Replace `--jdk` with the path to your local JDK installation.<br>
- To generate only the native binaries (without creating an installer), include the `--no-installer` flag.<br>
- For additional command options, run:
  {{< highlight shell >}}
  ./build/script/package-weasis.sh --help
  {{< /highlight >}}
  {{% /notice %}}

{{% notice tip %}}
On Windows the bash script must be executed with Git Bash or Cygwin. Avoid having spaces in the input and output paths.
{{% /notice %}}
