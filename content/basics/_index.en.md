---
title: Basics
description: "Reference documentation for Weasis administrators and integrators — shortcuts, preferences, customization, architecture, command catalog, and DICOM conformance."
weight: 10
pre: "<b>2. </b>"
keywords: [ "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer", "clinical viewer", "radiological viewer", "linux dicom viewer",  "mac dicom viewer" ]
---

The **Basics** section is the reference layer of the Weasis documentation. It targets **administrators, integrators, and power users** who deploy Weasis into a clinical or research environment and need to understand its internals — beyond what an end user needs to know to read a study.

You will find:

- **[Architecture](architecture)** — the OSGi-based plugin model, how the application boots, and how a plugin fits into the runtime.
- **[Customize](customize)** — application preferences, integration with a PACS or web portal, and plugin packaging.
- **[Shortcuts](shortcuts)** — the full keyboard-shortcut reference.
- **[Commands](commands)** — the command-line and console catalog (`$dicom:get`, `$image:close`, …) usable from scripts, the Weasis console, or remote control.
- **[System Resources](system-resources)** — heap sizing, file handles, network tuning, and other runtime knobs for large workstations or multi-user deployments.
- **[DICOM Conformance](dicom)** — the DICOM conformance statement (SOP classes, transfer syntaxes, services).

If you are deploying Weasis behind a PACS / VNA, see also the [Customize → Integration](customize/integration) guide and the [ViewerHub](../viewer-hub) launcher.

