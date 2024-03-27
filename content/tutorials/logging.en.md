---
title: Logging
weight: 550
description: How to configure application traces
keywords: [ "log", "logging", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Configure and view log files</center>

The log folder that can be opened from the menu "_Help > Open the logging folder_" (since {{% badge title="Version" %}}4.1.0{{% /badge %}}) contains two types of log:
1. A boot log file (boot.log) is always written since {{% badge title="Version" %}}3.5.0{{% /badge %}}
2. Rolling log files (default.log) that need to be activated in the preferences dialog (see below _How to configure the rolling log files_)

{{% notice tip %}}
In order to determine the path of <user.home>/.weasis/log for versions prior to v4.1.0, go to the "_Help > About Weasis_" menu and find the property `weasis.path` in the "_System Information_" tab.
{{% /notice %}}


### Boot log files
The boot log file is used to trace the startup configuration to ensure that the application starts with the correct input parameters and configuration.
This type of logs is interesting if the application doesn't start, crash at startup, or if there is a problem with the startup preferences.

### How to configure the rolling log files
![Preferences](/tuto/logging.png?classes=shadow)
<br>

* From the main menu "_File > Preferences > General_" enable "_Rolling log_" to activate writing to files
* Enter the maximum of _File numbers_ for rolling log (by default 5)
* Enter the maximum size of each rolling file (by default 10 MB)
* Select a log level which defines the verbosity of the traces (by default DEBUG)
* Select a stacktrace limit which represents the number of lines (by default no value). No value is recommended for investigating problems (it means unlimited stacktrace lines)

{{% notice info %}}
The default logging configuration comes from config.properties or ext-config.properties, see [Weasis Preferences](../basics/customize/preferences).
{{% /notice %}}


