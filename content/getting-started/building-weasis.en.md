---
title: Building Weasis
description: How to build Weasis from sources
keywords: [ "building", "sources", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 30
---

These instructions describe how to build Weasis directly from the Git repository on any platform. For building Weasis from an IDE, see [Weasis plug-in development guidelines](../guidelines).

**Prerequisites**

1. JDK 17 or higher
2. Maven 3.5.3 or higher<br>
   If your computer is behind a proxy server, [configure maven](https://maven.apache.org/guides/mini/guide-proxies.html).
3. Git or directly download source from [github](https://github.com/nroduit/Weasis)

### Getting the Source

To clone the repository, first install GIT and either clone using a graphical GIT client or directly from the command line using the command:

{{< highlight shell >}}
git clone https://github.com/nroduit/Weasis.git
{{< /highlight >}}

{{% notice warning %}}
The trunk is not a stable version and snapshot version is not retained in the cache for the web distribution (it means the files will be downloaded every time)
{{% /notice %}}

Check out a tag version to build a stable version, see the <a target="_blank" href="https://github.com/nroduit/Weasis/tags">tag list</a>.

{{< highlight shell >}}
git checkout <TAG_NAME>
{{< /highlight >}}

### Building all Plug-ins

- Go in the *Weasis* directory, compile and install all the plug-ins in the local Maven repository
{{< highlight shell >}}
mvn clean install
{{< /highlight >}}


### Building Weasis Distributions

{{% notice note %}}
The native installer will progressively replace the portable and the web distribution. It uses the [weasis protocol](../../getting-started/weasis-protocol) (which not requires jar signing) instead of Java Web Start which has been removed from <a target="_blank" href="https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html#JDK-8185077">Java 11 release</a> and because the end of public Oracle Java 8 updates from April 2019.<br>
The documentation for building the native installer we be available from Weasis 4.
{{% /notice %}}

- Requires installing all the plug-ins in the local Maven repository as described in the item above.
{{< highlight shell >}}
cd weasis-distributions
mvn clean package -Dportable=true -P compressXZ
{{< /highlight >}}
{{% notice tip %}}
**-P compressXZ**: Option for compressing the packages in <a target="_blank" href="https://en.wikipedia.org/wiki/XZ_Utils">xz</a>, only from Weasis 3.6.0. The compression pack200 is not supported anymore (removed from Java 14), before 3.6.0 the profile was **-P pack200**.<br>
**-Dportable=true**: Option for building the portable distribution (multi-platform standalone launchers)
{{% /notice %}}
{{% notice warning %}}
For the WEB distribution using Java Webstart, it is required to sign jar files with your **own certificate** (by replacing values in the command below with your **own values**). A trust-worthy certificate from a certificate authority is  <a target="_blank" href="https://blogs.oracle.com/java-platform-group/entry/code_signing_understanding_who_and">required</a> to run Java Web Start applications. A self-signed certificate generate by keytool will always display a security warning message.
{{% /notice %}}
The parameters must be placed in the maven user setting or has to be the options in the Maven command:
{{< highlight bash >}}
$ mvn clean package -Djarsigner.alias="your_alias" -Djarsigner.storepass="your_pwd" -Djarsigner.keystore="your_path/keystore" -Dportable=true -P compressXZ
{{< /highlight >}}
{{% notice tip %}}
For production, version must not end with SNAPSHOT (otherwise packages will not be kept in cache). So to remove SNAPASHOT or to make your own release (for avoiding package mix-up in cache), modify the changelist property. From the Weasis root folder, execute:
{{% /notice %}}
{{< highlight shell >}}
$ mvn clean install -Dchangelist=-mybuild
$ mvn clean package -Dchangelist=-mybuild -Dportable=true -P compressXZ -f weasis-distributions
{{< /highlight >}}


<!-- -->

-  Options for building the portable distribution.
    - By default, the executable on Windows runs only a single instance (from Weasis 2.0). To disable single instance in the portable version, set windowsName property empty.
{{< highlight shell >}}
$ mvn clean package -Dportable=true -DwindowsName=
{{< /highlight >}}
    -  On 64-bit system, it requires installing the 32-bit compatibility libraries to build the windows executable. On Linux, you need to install **ia32-libs** package.
{{% notice warning %}}
Do not place the sources in a path that contains directories with blanks or national characters, the compilation of the win32 executable can fail.
{{% /notice %}}

- The distribution files are located in:
    - target/web-dist/
    - target/portable-dist/
