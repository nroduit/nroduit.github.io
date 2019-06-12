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

* From a web page, just make a [link](weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FLumbar%2Fmf.xml) starting with weasis://
{{% notice note %}}
Some web frameworks such as the wiki or the URL field of some browsers only support standard protocols (http, ftp...). To solve this problem, it is necessary to use a URL redirection starting with http like the one proposed in <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a>: `http://<your-host>:8080/weasis-pacs-connector/weasis?patientID=TESTS`
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

### How to build an URI

The URI scheme "weasis://" allows you to launch Weasis from the system's URI handler while the URI path allows you to build [Weasis commands](../../basics/commands).

To load multiple remote images, it is recommended to use a manifest listing the references of the images to be loaded. The easiest way to dynamically build this manifest is to use <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector</a>. However, it is possible to build it differently by following the [following instructions](../../basics/customize/integration/#build-an-xml-manifest).

#### Command with a manifest containing direct links (without WADO server)

1. Write a [command](../../basics/commands) to load remotely the XML manifest
{{< highlight text >}}
$dicom:get -w https://nroduit.github.io/samples/Lumbar/mf.xml
{{< /highlight >}}
2. Format the URI path with a URL encoder
{{< highlight text >}}
%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FLumbar%2Fmf.xml
{{< /highlight >}}
3. Make a link by adding "weasis://" at the beginning
<a  href="weasis://%24dicom%3Aget%20-w%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FLumbar%2Fmf.xml" class="btn btn-default">Open the manifest</a>

#### Command loading directly an image
1. Write a [command](../../basics/commands) to load an URL
{{< highlight text >}}
$dicom:get -r https://nroduit.github.io/samples/CT0081.dcm
{{< /highlight >}}
2. Format the URI path with a URL encoder
{{< highlight text >}}
%24dicom%3Aget%20-r%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FCT0081.dcm
{{< /highlight >}}
3. Make a link by adding "weasis://" at the beginning
<a  href="weasis://%24dicom%3Aget%20-r%20https%3A%2F%2Fnroduit.github.io%2Fsamples%2FCT0081.dcm" class="btn btn-default">Open the remote image</a>

{{% notice tip %}}
When first used in a browser, a popup appears to confirm the opening of the weasis protocol. On Windows, it is possible to make sure that this message never appears:<br>- With IE/Edge set the WarnOnOnOpen value to 0 in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ProtocolExecute\weasis.<br>- With Chrome add an entry (key=1  value=weasis://\*) in HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\URLWhitelist, see how to manage <a target="_blank" href="https://www.chromium.org/administrators/policy-list-3#URLWhitelist">URLWhitelist</a>.
{{% /notice %}}
