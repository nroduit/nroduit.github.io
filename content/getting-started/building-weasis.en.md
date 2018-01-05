---
title: Building Weasis
weight: 30
---

These instructions describe how to build Weasis directly from the Git repository on any platform. For building Weasis from an IDE, see [Weasis plug-in development guidelines](../guidelines).

**Prerequisites**

1.  JDK 8 or higher
2.  Maven 3 or higher<br>
    If your computer is behind a proxy server, <a target="_blank" href="http://maven.apache.org/guides/mini/guide-proxies.html">configure maven</a>.
3.  Git or directly download source from <a target="_blank" href="https://github.com/nroduit/weasis-i18n">gitub</a>

### Getting the Source

To clone the repository, first install GIT and either clone using a graphical GIT client or directly from the command line using the command:

{{< highlight bash >}}
$ git clone https://github.com/nroduit/Weasis.git
{{< /highlight >}}

{{% notice warning %}}
The trunk is not a stable version and snapshot version is not retained in cache for the web distribution (it means the files will be every times downloaded)
{{% /notice %}}

Check out a tag version to build a stable version, see <a target="_blank" href="https://github.com/nroduit/Weasis/tags">tag list</a>.

{{< highlight bash >}}
$ git checkout <TAG_NAME>
{{< /highlight >}}

### Building all Plug-ins

- Go in the *Weasis* directory, compile and install all the plug-ins in the local Maven repository
{{< highlight bash >}}
$ mvn clean install
{{< /highlight >}}


### Building Weasis Distributions

- Requires to install all the plug-ins in the local Maven repository as described in the item above.
{{< highlight bash >}}
$ cd weasis-distributions
$ mvn clean package -Dportable=true -P pack200
{{< /highlight >}}
{{% notice tip %}}
**-P pack200**: From 1.1.2 it is possible to use the compression pack200 that reduces jar size considerably. It is recommended to use the Oracle jdk with this option (openjdk can throw packging errors).<br>
**-Dportable=true**: option for building the portable distribution (multi-platform standlone launchers)
{{% /notice %}}
{{% notice warning %}}
For the WEB distribution using Java Webstart, it is required to sign jar files with your **own certificate** (by replacing values in the command below by your **own values**). A trust-worthy certificate from a certificate authority is now  <a target="_blank" href="https://blogs.oracle.com/java-platform-group/entry/code_signing_understanding_who_and">required</a> to run Java Web Start applications. A self signed certificate generate by keytool will always display a security warning message.
{{% /notice %}}
The parameters must be placed in the maven user setting or has to be the options in the Maven command:
{{< highlight bash >}}
$ mvn clean package -Djarsigner.alias="your_alias" -Djarsigner.storepass="your_pwd" -Djarsigner.keystore="your_path/keystore" -Dportable=true -P pack200
{{< /highlight >}}


<!-- -->

-  Options for building the portable distribution.
    - By default the executable on Windows runs only a single instance (from Weasis 2.0). To disable single instance in portable version, set windowsName property empty.
{{< highlight bash >}}
$ mvn clean package -Dportable=true -DwindowsName=
{{< /highlight >}}
    -  On 64-bit system, it requires to install the 32-bit compatibility libraries to build the windows executable. On Linux you need to install **ia32-libs** package.
{{% notice warning %}}
Do not place the sources in a path that contains directories with blanks or national characters, the compilation of the win32 executable can fail.
{{% /notice %}}

- The distribution files are located in:
    - target/web-dist/
    - target/portable-dist/
