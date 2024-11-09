---
title: Building Weasis
description: How to build Weasis from sources
keywords: [ "building", "sources", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 30
---

These instructions describe how to build Weasis directly from the Git repository on any platform. For building Weasis from an IDE, see [Weasis plug-in development guidelines](../guidelines).

**Prerequisites**

1. JDK 22 or higher
2. Maven 3.5.3 or higher<br>
   If your computer is behind a proxy server, [configure maven](https://maven.apache.org/guides/mini/guide-proxies.html).
3. Git

### Getting the Source

In order to clone the repository, first install GIT and either clone using a graphical GIT client or directly from the command line using the command:

{{< highlight shell >}}
git clone https://github.com/nroduit/Weasis.git
{{< /highlight >}}

### Building all Plug-ins

- Go in the *Weasis* directory, compile and install all the plug-ins in the local Maven repository:
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
For production, version must not be SNAPSHOT (otherwise packages will not be kept in cache). So to remove SNAPASHOT or to make your own release (for avoiding package mix-up in cache), modify the changelist property. From the Weasis root folder, execute:
{{< highlight shell >}}
mvn -Dchangelist=-mybuild-beta clean install
mvn -Dchangelist=-mybuild-beta -P compressXZ -f weasis-distributions clean package
{{< /highlight >}}
{{% /notice %}}


### Building native binaries and installers

Since {{% badge title="Version" %}}4.0.0{{% /badge %}} the native installer has completely replaced the portable and the Java Webstart distributions.

The [official build](https://github.com/nroduit/Weasis/blob/master/.github/workflows/build-installer.yml) is done by Github actions with [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners) (Linux, macOS and Windows). 

However, it is possible to run a local script `package-weasis.sh` on most systems but without guarantee because the system must have a correct configuration of several tools (see [jpackage prerequisites](https://docs.oracle.com/en/java/javase/20/jpackage/packaging-overview.html)).

- Get `weasis-native.zip`, unzip the archive and then go to the root folder with a bash prompt. 
- Build the native binaries and the installer:
{{< tabs groupid="build-native" >}}
{{% tab title="Bash" %}}
{{< highlight shell >}}
./build/script/package-weasis.sh --jdk "/home/.jdks/openjdk-22"
{{< /highlight >}}
{{% /tab %}}
{{< /tabs >}}

{{% notice note %}}
- In the commands above, adapt the `--jdk` value to your local JDK path.<br>
- For building only the native binaries (without installer), add the parameter `--no-installer`<br>
- In order to see the use of the script and its options, run:
  {{< highlight shell >}}
  ./build/script/package-weasis.sh --help
  {{< /highlight >}}
  {{% /notice %}}

{{% notice tip %}}
On Windows the bash script must be executed with Git Bash or Cygwin. Avoid having spaces in the input and output paths.
{{% /notice %}}
