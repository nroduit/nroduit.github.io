---
title: Weasis Architecture
description: Modular architecture of Weasis
keywords: [ "architecture", "weasis architecture", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 10
---


Weasis has a modular architecture based on <a target="_blank" href="https://www.osgi.org">OSGi</a>: the dynamic module system for Java. It uses the [Apache Felix OSGi framework](https://felix.apache.org) which is an open source implementation of the OSGi specification.

The following schemas show the main different plug-in types (bundle in OSGi language) and their relationships. *Viewer*, *Viewer Tool Pane*, *Tool Bar*, *Data Explorer* and *Codec* bundles are registered dynamically by the Declarative Services (a way to push or to consume services in OSGi environment).

{{< svg "static/images/architecture-bundles.svg" >}}

![packages](/images/architecture-packages.png?classes=border)

For each bundle, translation files are packaging in a separated bundle ending by “i18n” called a bundle fragment (OSGi concept) which is merged during runtime to the application. In this way, translation can be handled separately and they are automatically loaded by the application when they are available.

Some Codec bundles also have bundle fragments. Those fragments contain native libraries (JNI wrapping). The Weasis launcher enables downloading and loading only the native binaries related to the running platform.
