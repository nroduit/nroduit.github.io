---
title: Proxy server
weight: 600
description: How to configure a proxy server
keywords: [ "network", "porxy", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>How to configure a proxy server</center>

### Manual configuration from the user interface
From the main menu, open _File > Preferences (Alt + P)_ and select *Proxy Server*.

The default configuration is *Direct connection (no proxy)* and by clicking on *Manual proxy configuration* you can define a custom proxy server (in the image below, a local proxy like Squid).

In order to fill in the fields, you must refer to the [Java documentation](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/doc-files/net-properties.html).

![Proxy configuration](/tuto/proxy-prefs.png?classes=shadow)
<br>
{{% notice tip %}}
In some cases it is necessary to restart Weasis.
{{% /notice %}}

### Configuration at launch
For setting JVM properties at launch, the selection in user interface must be *Direct connection (no proxy) or configuration at launch*.

{{% notice tip %}}
The Java options can be manually set in the section "[JavaOptions]" of Weasis.cfg (in the installed path).
{{% /notice %}}

Examples of configuration:

* Set the default system proxy
{{< highlight text >}}
-Djava.net.useSystemProxies=true
{{< /highlight >}}
* Set a local proxy like Squid
{{< highlight text >}}
-Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=3128
{{< /highlight >}}
* Set a proxy in specific domain
{{< highlight text >}}
-Dhttps.proxyHost="proxy.mydomain.com" -Dhttps.proxyPort="8080" -Dhttp.proxyHost="proxy.mydomain.com" -Dhttp.proxyPort="8080" -Dhttp.nonProxyHosts="\*.mydomain.com|localhost" -Dhttp.proxyUser="user" -Dhttp.proxyPassword="password"
{{< /highlight >}}

{{% notice note %}}
The Java options can also be passed in the [parameters](https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters) of the URL (e.g. http://localhost:8080/weasis-pacs-connector/weasis?patientID=9702672&pro="https.proxyHost%20127.0.0.1"&pro="https.proxyPort%203128").
{{% /notice %}}
