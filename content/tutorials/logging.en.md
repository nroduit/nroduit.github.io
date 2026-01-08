---
title: Logging
weight: 550
description: How to configure application traces
keywords: [ "log", "logging", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Configure and View Log Files</center>

Weasis provides comprehensive logging capabilities to help troubleshoot issues and monitor application behavior. Log files are stored in a dedicated folder that can be easily accessed from the application.

### Accessing the Log Folder

Open the log folder from the menu: **Help > Open the logging folder** (available since {{% badge title="Version" %}}4.1.0{{% /badge %}})

{{% notice tip %}}
For versions prior to v4.1.0: To find the log folder path (`<user.home>/.weasis/log`), navigate to _Help > About Weasis_ and locate the `weasis.path` property in the _System Information_ tab.
{{% /notice %}}

### Types of Log Files

Weasis generates two types of log files:

#### 1. Boot Log Files (boot.log)
The boot log file (available since {{% badge title="Version" %}}3.5.0{{% /badge %}}) automatically captures the application startup sequence and is always written, regardless of your configuration. This log is essential for:
- Verifying that Weasis starts with the correct parameters
- Diagnosing startup failures or crashes
- Troubleshooting configuration issues during launch

#### 2. Rolling Log Files (default.log)
Rolling log files capture runtime application activity and must be enabled in the preferences (see configuration steps below).

Once a log file reaches its maximum size, it is automatically compressed into a ZIP archive (since {{% badge title="Version" %}}4.4.0{{% /badge %}}).

### Configuring Rolling Log Files

![Preferences](/tuto/logging.png?classes=shadow)
<br>

Follow these steps to configure rolling logs:

1. Navigate to _File > Preferences > General_ in the main menu
2. Enable _Rolling log_ to activate file logging
3. Configure the following settings:

| Setting | Description | Default Value |
|---------|-------------|---------------|
| **File numbers** | Maximum number of rolling log files to retain | 20 |
| **File size** | Maximum size of each log file before rotation | 10 MB |
| **Log level** | Verbosity of trace messages (TRACE, DEBUG, INFO, WARN, ERROR) | INFO |
| **Stacktrace limit** | Number of stacktrace lines to display | 3 |

{{% notice tip %}}
For debugging issues: Set the stacktrace limit to **no value** (or 0) to capture unlimited stacktrace lines. This provides complete error details when investigating problems.
{{% /notice %}}

### Understanding Log Levels

Choose the appropriate log level based on your needs:

- **ERROR**: Only critical errors
- **WARN**: Warnings and errors
- **INFO** (default): General information, warnings, and errors
- **DEBUG**: Detailed debugging information
- **TRACE**: Most verbose logging (for in-depth troubleshooting)

{{% notice warning %}}
Lower log levels (DEBUG, TRACE) generate significantly more data and may impact performance. Use these levels only when actively troubleshooting issues.
{{% /notice %}}

{{% notice info %}}
The default logging configuration comes from `base.json`. See [Weasis Preferences](../../basics/customize/preferences) for more details. Some default values have changed since {{% badge title="Version" %}}4.4.0{{% /badge %}}.
{{% /notice %}}
