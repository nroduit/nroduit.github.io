---
title: Proxy server
weight: 420
description: How to configure a proxy server
keywords: [ "network", "porxy", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>How to configure a proxy server</center>

### Manual configuration from the user interface

From the main menu, open File > Preferences (Alt + P) and select *Proxy Server*.

The default configuration is *Direct connection (no proxy)* and by clicking on *Manual proxy configuration* you can define a custom proxy server (in the image below, a local proxy like Squid).

To fill in the fields you must refer to the [Java documentation](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/net/doc-files/net-properties.html).

![dcm4chee-web3](/tuto/proxy/proxy-ui.png)

### Configuration at launch

For setting JVM properties at launch, the selection in user interface must be *Direct connection (no proxy) or configuration at launch*. The Java options can be set in the section "[JavaOptions]" of Weasis.cfg.

#### Set the default system proxy
-Djava.net.useSystemProxies=true

#### Set a local proxy like Squid
-Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=3128

#### Set a proxy in specific domain
-Dhttps.proxyHost="proxy.mydomain.com" -Dhttps.proxyPort="8080" -Dhttp.proxyHost="proxy.mydomain.com" -Dhttp.proxyPort="8080" -Dhttp.nonProxyHosts="\*.mydomain.com|localhost" -Dhttp.proxyUser="user" -Dhttp.proxyPassword="password"

{{% notice note %}}
The Java options can also be passed in the <a target="_blank" href="https://github.com/nroduit/weasis-pacs-connector#launch-weasis-with-other-parameters">parameters</a> of the URL (e.g. http://localhost:8080/weasis-pacs-connector/weasis?patientID=9702672&pro="https.proxyHost%20127.0.0.1"&pro="https.proxyPort%203128").
{{% /notice %}}
