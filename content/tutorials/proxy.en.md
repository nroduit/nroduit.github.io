---
title: Proxy server
weight: 600
description: How to configure a proxy server
keywords: [ "network", "proxy", "http proxy", "https proxy", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>How to configure a proxy server</center>

If Weasis must reach the outside world through a corporate proxy — for example to pull updates, fetch a study from a remote DICOMweb server, or use a third-party launcher — you can either configure the proxy from the user interface or pass standard JVM proxy properties at launch.

### From the user interface

1. Open **_File > Preferences (Alt + P)_** in the main menu.
2. Select **Proxy Server** from the left panel.
3. The default is **Direct connection (no proxy)**. Switch to **Manual proxy configuration** to define a custom proxy (the screenshot below shows a local **Squid** instance).

For the meaning of each field, see the [Java networking properties reference](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/doc-files/net-properties.html) — the dialog mirrors the standard JVM proxy properties one-for-one.

![Proxy configuration](/tuto/proxy-prefs.png?classes=shadow)
<br>

{{% notice tip %}}
Some changes take effect only after **restarting Weasis**.
{{% /notice %}}

### From the launch parameters

To pass proxy settings as JVM options at launch, the UI selection must be set to **Direct connection (no proxy) or configuration at launch** so that the manual UI values do not override the command-line ones.

{{% notice tip %}}
JVM options can also be set permanently in the `[JavaOptions]` section of `Weasis.cfg` (located in the installation directory).
{{% /notice %}}

Common examples:

* **Use the operating system's default proxy:**
  {{< highlight text >}}
-Djava.net.useSystemProxies=true
  {{< /highlight >}}

* **Point to a local proxy** (e.g. a Squid running on 127.0.0.1:3128):
  {{< highlight text >}}
-Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=3128
  {{< /highlight >}}

* **Use a corporate proxy with authentication and a no-proxy list:**
  {{< highlight text >}}
-Dhttps.proxyHost="proxy.mydomain.com"
-Dhttps.proxyPort="8080"
-Dhttp.proxyHost="proxy.mydomain.com"
-Dhttp.proxyPort="8080"
-Dhttp.nonProxyHosts="\*.mydomain.com|localhost"
-Dhttp.proxyUser="user"
-Dhttp.proxyPassword="password"
  {{< /highlight >}}

{{% notice note %}}
The same JVM options can be injected from the launch URL through the `pro=` parameter — see the [weasis-pacs-connector launch parameters](https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters). Example:

```
http://localhost:8080/weasis-pacs-connector/weasis?patientID=9702672&pro="https.proxyHost%20127.0.0.1"&pro="https.proxyPort%203128"
```
{{% /notice %}}