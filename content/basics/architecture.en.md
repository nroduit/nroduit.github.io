---
title: Weasis Architecture
description: Modular architecture of Weasis
keywords: [ "architecture", "weasis architecture", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 10
---

Weasis is built on a **modular architecture** powered by [OSGi](https://www.osgi.org): the dynamic module system for Java. This design allows for a highly flexible, dynamic, and extendable structure. At its core, Weasis utilizes the [Apache Felix OSGi framework](https://felix.apache.org), a lightweight open-source implementation of the OSGi specification.

## Key Architectural Features
The following diagrams illustrate the main plugin types (_known as bundles in OSGi terminology_) and their relationships. These include **Viewer**, **Viewer Tool Pane**, **Tool Bar**, **Data Explorer**, and **Codec** bundles, which are dynamically registered using Declarative Services—a mechanism to seamlessly provide or consume services in the OSGi environment.

{{< svg "static/images/architecture-bundles.svg" >}}

### Understanding The Categories of Plugins
Weasis employs a modular approach, where individual plugins (or **bundles** in OSGi terminology) handle specific functionalities. Here are the plugin categories represented by layers in the diagram:
1. **Media Viewer and Editor**<br>
   This category handles the main viewing and editing functionalities. Except the [2D viewer](../../tutorials/dicom-2d-viewer/), it includes [specialized viewers](../../tutorials/gui/#list-of-other-viewersplayers-in-the-dicom-workspace) for different modalities and representations.
2. **UI Aggregator**<br>
   UI Aggregator plugins bring together various interface components to create a cohesive and user-friendly experience. They dynamically adapt the interface to include provided tools or modules, ensuring that Weasis remains customizable and modular.
3. **Data Access and Management (Data Explorer)**<br>
   This category focuses on managing how data is loaded, retrieved, and handled within the system.
4. **Codec (Media Decoding)**<br>
   Codec plugins are responsible for decoding and interpreting medical media files in the DICOM format and other supported formats. They sometimes include native libraries.
5. **Utility and Core Services**<br>
   This plugin provides essential utility functions and core services needed to support the other modules.

Each of these categories contributes to the flexibility and extensibility of Weasis, enabling it to be customized and adapted to different clinical and research workflows.

![packages](/images/architecture-packages.png?classes=border)

## Fragment Bundles
A **fragment bundle** is a special type of bundle that is attached to a host bundle to provide additional resources or classes. In Weasis, fragment bundles are used to provide **translations** and **native libraries** for codecs. This design allows for a clean separation of concerns and ensures that only the required resources are loaded at runtime.

### Bundle Translation Management
Each bundle has its **translation files** packaged in a separate bundle fragment (ending in `i18n`), an OSGi concept that merges these files dynamically during runtime. This design allows translations to be maintained independently, and they are automatically loaded by the application whenever they are available.

### Codec Support with Native Libraries
Certain Codec bundles contain fragments with **native libraries** (using JNI wrappers). The Weasis launcher dynamically loads only the required native binaries relevant to the platform on which it is running, ensuring lightweight and efficient operation.