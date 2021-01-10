---
title: Weasis Web Protocol
description: How to launch Weasis from a web context
keywords: [ "web", "launch", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 15
---

The web protocol allows to launch Weasis in a web context from a specific URI scheme: weasis://parameters

{{% notice warning %}}
Requires Weasis 3.5 (or superior) installed on the system with a [native installer](../).
{{% /notice %}}

### How to use the weasis protocol

* From a web page, just make a link starting with weasis:// (see below [How to build an URI](#how-to-build-an-uri))
{{% notice note %}}
Some web frameworks such as the wiki or the URL field of some browsers only support the standard protocols (http, ftp...). To solve this problem, it is necessary to use a URL redirection starting with http like the one proposed in <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a>: `http://<your-host>:8080/weasis-pacs-connector/weasis?patientID=TESTS`
{{% /notice %}}
* From the command line:
{{< highlight bash >}}
# Windows
$ start weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FLumbar%2Fmf.xml

# Linux
$ xdg-open weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FLumbar%2Fmf.xml

# Mac OS X
$ open weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FLumbar%2Fmf.xml
{{< /highlight >}}

{{% notice tip %}}
When first used in a browser, a popup appears to confirm the opening of the weasis protocol. On Windows, it is possible to make sure that this message never appears by adding a browser policy which allows the URI weasis://\*<br>- With IE/Edge the policy is applied by the native installer.<br>- With Chrome the policy is applied by the native installer (Windows and Linux), see how to manage <a target="_blank" href="https://support.google.com/chrome/a/answer/7532419?hl=en">URLWhitelist</a> (d).
{{% /notice %}}

### How to build an URI

The URI scheme "weasis://" allows you to launch Weasis from the system's URI handler while the URI path allows you to build [Weasis commands](../../basics/commands).

<a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#launch-weasis">weasis-pacs-connector</a> will help to build dynamically the manifest (the references of the images to be loaded) and the launch parameters (user, profile, plugins...). It will also manage user preferences.

To build an URI (weasis://path) without weasis-pacs-connector, you must choose one or more commands, encode the commands, and add the scheme `weasis://` as prefix. Here is an example of loading an image:

1. Use [$dicom:get](../../basics/commands/#dicomget) to load an image from URL
{{< highlight text >}}
$dicom:get -r https://nroduit.github.io/samples/us-palette.dcm
{{< /highlight >}}
2. Format the URI path with a URL encoder
{{< highlight text >}}
%24dicom%3Aget%20-r%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fus-palette.dcm
{{< /highlight >}}
3. Make a link by adding "weasis://" at the beginning
<a  href="weasis://%24dicom%3Aget%20-r%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fus-palette.dcm" class="btn btn-default">Open the remote image</a>

{{% notice tip %}}
To load multiple remote images, it is recommended to use a manifest listing the references of the images to be loaded. The easiest way to dynamically build this manifest is to use <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a>. However, it is possible to build it differently with the [following instructions](../../basics/customize/integration/#build-an-xml-manifest).
{{% /notice %}}

#### Examples to load images

If you use weasis-pacs-connector, please refer to <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#launch-weasis">Launch Weasis</a>.

* Use [$dicom:get](../../basics/commands/#dicomget) to load a static XML manifest containing direct links (without WADO server) <a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FLumbar%2Fmf.xml" class="btn btn-default">Launch</a>
{{< highlight text >}}
$dicom:get -w https://nroduit.github.io/samples/Lumbar/mf.xml
{{< /highlight >}}
* Use [$dicom:rs](../../basics/commands/#dicomrs) to load DICOM files with DICOMWeb RESTful services (see [other examples](../../basics/customize/integration/#download-directly-with-dicomweb-restful-services)) <a  href="weasis://%24dicom%3Ars%20--url%20%22https%3A%2F%2Fdemo.orthanc-server.com%2Fdicom-web%22%20-r%20%22patientID%3D5Yp0E%22%20--accept-ext%3D%22%3B%22" class="btn btn-default">Launch</a>
{{< highlight text >}}
$dicom:rs --url "https://demo.orthanc-server.com/dicom-web" -r "patientID=5Yp0E"
{{< /highlight >}}
* Use [$dicom:get](../../basics/commands/#dicomget) to load an image from URL and [remove all](../../basics/commands/#dicomclose) the previous images if Weasis is already open <a  href="weasis://%24dicom%3Aclose%20--all%20%24dicom%3Aget%20-r%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fus-palette.dcm" class="btn btn-default">Launch</a>
{{< highlight text >}}
$dicom:close --all $dicom:get -r https://nroduit.github.io/samples/us-palette.dcm
{{< /highlight >}}
* Use [$dicom:get](../../basics/commands/#dicomget) to load multiple local folders and a remote image <a  href="weasis://%24dicom%3Aget%20-l%20%22D%3A%2FDICOM%2FOverlay%22%20-l%20%22D%3A%2FDICOM%2FShutter%22%20-r%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2Fus-palette.dcm" class="btn btn-default">Launch</a>
{{< highlight text >}}
$dicom:get -l "D:/DICOM/Overlay" -l "D:/DICOM/Shutter" -r https://nroduit.github.io/samples/us-palette.dcm
{{< /highlight >}}
* Use [$image:get](../../basics/commands/#imageget) to load a non DICOM image <a  href="weasis://%24image%3Aget%20-u%20https%3A%2F%2Fuser-images.githubusercontent.com%2F993975%2F59107662-6c9ed300-8939-11e9-83ee-28f2725f4ae1.jpg" class="btn btn-default">Launch</a>
{{< highlight text >}}
$image:get -u https://user-images.githubusercontent.com/993975/59107662-6c9ed300-8939-11e9-83ee-28f2725f4ae1.jpg
{{< /highlight >}}

#### Modify the launch parameters

The command for modifying the configuration at launch is `$weasis:config` which can have different arguments:

* **cdb** is the Weasis web context (The URL of weasis.war). If the value is null, the weasis version installed from the [native installer](../) is used. In the weasis-pacs-connector <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector/blob/master/src/main/resources/weasis-pacs-connector.properties">configuration</a>, the default value is defined by `weasis.base.url`.
* **cdb-ext** is the extension web context of Weasis (The URL of weasis-ext.war containing additionnal plugins). In the weasis-pacs-connector <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector/blob/master/src/main/resources/weasis-pacs-connector.properties">configuration</a>, the default value is defined by `weasis.ext.url`.
* **arg** is an argument for the launcher. The value must start by $, like arg="$dicom:close --all" (Note: the value can also be directly in the base URI, outside $weasis:config). Single-valued argument but can be specified multiple times.
* **pro** is a property for the launcher containing a key and a value separate by a space. Single-valued property but can be specified multiple times.
* **auth** is the web authorization parameter
* **wcfg** is the URL the remote Weasis configuration service.

Here are some examples that modify the launcher properties without using <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#launch-weasis">weasis-pacs-connector</a>:

* Configuration for launching Weasis Dicomizer <a  href="weasis://%24weasis%3Aconfig%20pro%3D%22felix.extended.config.properties%20file%3Aconf%2Fext-dicomizer.properties%22%20pro%3D%22gosh.port%2017181%22" class="btn btn-default">Launch</a>
{{< highlight text >}}
$weasis:config pro="felix.extended.config.properties file:conf/ext-dicomizer.properties" pro="gosh.port 17181"
{{< /highlight >}}
* Change the user, by default is the one of the current system session. The local preferences are associated to a user. <a  href="weasis://%24weasis%3Aconfig%20pro%3D%22weasis.user%20user2%22" class="btn btn-default">Launch</a>
{{< highlight text >}}
$weasis:config pro="weasis.user user2"
{{< /highlight >}}
