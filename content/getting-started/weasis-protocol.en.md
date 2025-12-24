---
title: Weasis Web Protocol
description: How to launch Weasis from a web context
keywords: [ "web", "launch", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 15
---

The **Weasis Protocol** enables the launch of Weasis (starting from {{< badgeC "v3.6.0" >}}) in a web context using a specific URI scheme: `weasis://?commands`.

### How to Use the Weasis Protocol

To launch Weasis from various contexts:
1. **From a Web Page**: Create a link that begins with `weasis://?` (see below [How to build an URI](#how-to-build-a-uri)).<br>
   If certain web frameworks (e.g., WIKI) or contexts only support HTTP protocols, you can use a URL redirection starting with `https://`. A tool such as [Weasis PACS Connector](https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector) can help with this.
2. **From the Command Line**: Utilize the appropriate Weasis command from the terminal:
{{< tabs groupid="launchWeasisProtocol">}}
{{% tab title="Windows" %}}
{{< highlight shell >}}
start weasis://?%24dicom%3Aget+-w+%22https%3A%2F%2Fnroduit.github.io%2Fdemo-archive%2FLumbar%2Fmf.xml%22
{{< /highlight >}}
{{% /tab %}}
{{% tab title="Linux" %}}
{{< highlight shell >}}
xdg-open weasis://?%24dicom%3Aget+-w+%22https%3A%2F%2Fnroduit.github.io%2Fdemo-archive%2FLumbar%2Fmf.xml%22
{{< /highlight >}}
{{% /tab %}}
{{% tab title="macOS" %}}
{{< highlight shell >}}
open weasis://?%24dicom%3Aget+-w+%22https%3A%2F%2Fnroduit.github.io%2Fdemo-archive%2FLumbar%2Fmf.xml%22
{{< /highlight >}}
{{% /tab %}}
{{< /tabs >}}

### How to Build a URI
The `weasis://?` URI scheme allows you to launch Weasis directly from the system's URI handler. By constructing the correct URI path, you can execute [Weasis commands](../../basics/commands) to load images or perform other actions.

[Weasis PACS Connector](https://github.com/nroduit/weasis-pacs-connector#launch-weasis) can dynamically generate manifests (listing references for images to load) and build the required URI through an API. This tool also manages user preferences and other launch parameters.

If you're not using the Weasis PACS Connector, you can build a URI manually by following these steps:
1. **Choose Commands**: Select one or more [commands](../../basics/commands) to execute.
2. **Encode the Commands**: Use a URL encoder to format the commands correctly for URI inclusion.
3. **Prefix the Commands**: Add the `weasis://?` scheme at the beginning of the encoded command string to create the final URI.

##### Example: Loading a Remote Image
1. Use [$dicom:get](../../basics/commands/#dicomget) to load an image from URL
{{< highlight text >}}
$dicom:get -r "https://nroduit.github.io/demo-archive/us-palette.dcm"
{{< /highlight >}}
2. Format the URI path with a URL encoder
{{< highlight text >}}
%24dicom%3Aget+-r+%22https%3A%2F%2Fnroduit.github.io%2Fdemo-archive%2Fus-palette.dcm%22
{{< /highlight >}}
3. Make the final URI by adding "weasis://?" at the beginning
{{< launch title="Open the remote image" >}}
$dicom:get -r "https://nroduit.github.io/demo-archive/us-palette.dcm"
{{< /launch >}}

{{% notice tip %}}
For loading multiple images, it's recommended to use a manifest file that references all desired images instead of including each image individually in the URI. The easiest way to build this manifest dynamically is by using the [Weasis PACS Connector](https://github.com/nroduit/weasis-pacs-connector">weasis-pacs-connector). Alternatively, you can create the manifest manually following the [provided instructions](../../basics/customize/integration/#build-an-xml-manifest).
{{% /notice %}}

### Examples to Load Images

If you use weasis-pacs-connector, please refer to [Launch Weasis](https://github.com/nroduit/weasis-pacs-connector#launch-weasis).

* Use [$dicom:get](../../basics/commands/#dicomget) to load a static XML manifest containing direct links (without WADO server) {{< launch >}}$dicom:get -w "https://nroduit.github.io/demo-archive/Lumbar/mf.xml"{{< /launch >}}
{{< highlight shell >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/Lumbar/mf.xml"
{{< /highlight >}}
* Use [$dicom:rs](../../basics/commands/#dicomrs) to load DICOM files with DICOMWeb RESTful services (see [other examples](../../basics/customize/integration/#download-directly-with-dicomweb-restful-services)) {{< launch >}}$dicom:rs --url "https://demo.orthanc-server.com/dicom-web" -r "patientID=5Yp0E"{{< /launch >}}
{{< highlight shell >}}
$dicom:rs --url "https://demo.orthanc-server.com/dicom-web" -r "patientID=5Yp0E"
{{< /highlight >}}
* Use [$dicom:get](../../basics/commands/#dicomget) to load an image from URL and [remove all](../../basics/commands/#dicomclose) the previous images if Weasis is already open {{< launch >}}$dicom:close --all $dicom:get -r "https://nroduit.github.io/demo-archive/us-palette.dcm"{{< /launch >}}
{{< highlight shell >}}
$dicom:close --all $dicom:get -r "https://nroduit.github.io/demo-archive/us-palette.dcm"
{{< /highlight >}}
* Use [$dicom:get](../../basics/commands/#dicomget) to load multiple local folders and a remote image {{< launch >}}$dicom:get -l "D:/DICOM/Overlay" -l "D:/DICOM/Shutter" -r "https://nroduit.github.io/demo-archive/us-palette.dcm"{{< /launch >}}
{{< highlight shell >}}
$dicom:get -l "D:/DICOM/Overlay" -l "D:/DICOM/Shutter" -r "https://nroduit.github.io/demo-archive/us-palette.dcm"
{{< /highlight >}}
* Use [$image:get](../../basics/commands/#imageget) to load a non DICOM image {{< launch >}}$image:get -u "https://user-images.githubusercontent.com/993975/59107662-6c9ed300-8939-11e9-83ee-28f2725f4ae1.jpg"{{< /launch >}}
{{< highlight shell >}}
$image:get -u "https://user-images.githubusercontent.com/993975/59107662-6c9ed300-8939-11e9-83ee-28f2725f4ae1.jpg"
{{< /highlight >}}

### Modify the Launch Parameters

The command for modifying the configuration at launch is `$weasis:config` which can have different arguments:

* **cdb** is the Weasis web context (The URL of weasis-native.zip package in [ViewerHub](../../viewer-hub)). If the value is null, the weasis version installed from the [native installer](../) is used. In the weasis-pacs-connector [configuration](https://github.com/nroduit/weasis-pacs-connector/blob/master/src/main/resources/weasis-pacs-connector.properties), the default value is defined by `weasis.base.url`.
* **arg** is an argument for the launcher. The value must start by $, like arg="$dicom:close --all" (Note: the value can also be directly in the base URI, outside $weasis:config). Single-valued argument but can be specified multiple times.
* **pro** is a property for the launcher containing a key and a value separate by a space. Single-valued property but can be specified multiple times.
* **auth** is the web authorization parameter
* **wcfg** is the URL the remote Weasis configuration service.

Here are some examples that modify the launcher properties without using [weasis-pacs-connector](https://github.com/nroduit/weasis-pacs-connector#launch-weasis):

* Configuration for launching Weasis Dicomizer {{< launch >}}$weasis:config pro="felix.extended.config.properties file:conf/dicomizer.json" pro="gosh.port 17181"{{< /launch >}}
{{< highlight shell >}}
$weasis:config pro="felix.extended.config.properties file:conf/dicomizer.json" pro="gosh.port 17181"
{{< /highlight >}}
* Change the user, by default, is the one of the current system session. The local preferences are associated to a user. {{< launch >}}$weasis:config pro="weasis.user user2"{{< /launch >}}
{{< highlight shell >}}
$weasis:config pro="weasis.user user2"
{{< /highlight >}}

### Enterprise Deployment: Browser Protocol Configuration

By default, Weasis registers the `weasis://` protocol through standard OS mechanisms. To ensure a seamless user experience in institutional environments, administrators can suppress the browser's security confirmation dialog using central policies.

**Official Documentation**:
- [Chrome Enterprise Policy List](https://chromeenterprise.google/policies/#URLAllowlist)
- [Microsoft Edge - URLAllowlist](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/urlallowlist)
- [Mozilla Policy Templates](https://github.com/mozilla/policy-templates#websitefilter)

{{< tabs groupid="configureWeasisProtocol">}}
{{% tab title="Windows (Group Policy or Registry)" %}}
Recommended for AD environments.

1. **GPO Path**:
    * **Chrome/Edge**: `Computer Configuration` → `Admin Templates` → `[Google Chrome/Microsoft Edge]` → `Content Settings` → `Allow access to a list of URLs`
    * **Firefox**: `Computer Configuration` → `Admin Templates` → `Mozilla` → `Firefox` → `WebsiteFilter` → `Exceptions`
2. **Value**: Add `weasis://*`

**Direct Registry Deployment**:
```reg
Windows Registry Editor Version 5.00

; Chrome
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\URLAllowlist]
"1"="weasis://*"

; Chromium
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Chromium\URLAllowlist]
"1"="weasis://*"

; Microsoft Edge
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\URLAllowlist]
"1"="weasis://*"

; Firefox
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Mozilla\Firefox\WebsiteFilter\Exceptions]
"1"="weasis://*"
```

Note: The number in quotes ("1") should be incremented if you already have other entries in the list.
{{% /tab %}}
{{% tab title="Linux (JSON Policy)" %}}
Create a policy file in the managed directory.
* Chrome: /etc/opt/chrome/policies/managed/weasis.json
* Chromium: /etc/chromium/policies/managed/weasis.json
* Firefox: /etc/firefox/policies/policies.json

Example JSON (Chrome/Chromium):
``` json
{
  "URLAllowlist": ["weasis://*"]
}
```

Example JSON (Firefox):
``` json
{
  "policies": {
    "WebsiteFilter": { "Exceptions": ["weasis://*"] }
  }
}
```
{{% /tab %}}
{{% tab title="macOS (Configuration Profile)" %}}
Deploy via MDM (Jamf, Kandji, etc.) using the URLAllowlist key. Chrome/Chromium Payload:

``` xml
<key>URLAllowlist</key>
<array>
    <string>weasis://*</string>
</array>
```
PayloadType: com.google.Chrome (Chrome) or com.brave.Browser (Brave).
Firefox: Use the macOS Mozilla Policy structure.
{{% /tab %}}
{{< /tabs >}}