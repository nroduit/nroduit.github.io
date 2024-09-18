---
title: Third-party Launcher
weight: 360
description: How to launch a third-party application
keywords: [ "Launch", "Launcher", "external application", "dicom viewer", "free dicom viewer"]
---

Third-party application launchers allow you to run another application by transmitting information to it in the startup parameters.

In the graphical user interface, launchers appear in the _File > Launcher_ menu and optionally in the toolbar.

![Launcher](/tuto/launchers.png?classes=shadow)
<br>
In the example above, we add a button to launch the Horos software on the Mac, importing the directory containing the DICOM files downloaded by Weasis.

### How to create the third-party launcher

1. From the main menu, open _File > Preferences (Alt + P)_ and select the _Launcher_ item.
2. Click on the _Add New_ button to create a new DICOM launcher.
3. In DICOM launcher dialog, fill in the fields:
   * Name: the name of the launcher
   * Icon path: the icon to display in the menu and toolbar. The path can be absolute or relative to the Weasis resources folder. When the icon is not found, the default icon is displayed.
   * Enable: to display the launcher in the menu and toolbar
   * Button: to display the launcher in the toolbar
4. In DICOM Launcher dialog, click on _Configure_ to specify the launch context.
5. In Launcher Type, select the launcher type:
   * URI: add a URI to open a web page or a file. The URI can contain dynamic variables described below.
   * Application: run an application with parameters. The application _Parameters_ and _Environment Variables_ can contain dynamic variables described below.
     * Binary Path: the command to run the application.
     * Working Directory: the working directory of the application (optional).
     * Parameters: the parameters to pass to the application. Each line is a parameter.
     * Environment Variables: the environment variables to pass to the application. Each line is an environment variable.
     * Compatibility: the compatibility of the launcher with the current platform. This feature is useful when the launcher configuration is coming from the server side.
6. In Launcher Type, click on _Save_ to save the launcher parameters.    
7. In DICOM Launcher, click on _Save_ to save the launcher general information.

List of dynamic variables in _URI_, _Parameters_ and _Environment Variables_:
   * `{dicom:wado.folder}` the temporary folder for images downloaded from the WADO and DICOMWeb protocols.
   * `{dicom:last.folder}` the last open folder of _Local Device_ in _Import DICOM_.
   * `{dicom:selection.folder}` it will display a selection dialog (such as _Export DICOM_) and copy the result to this folder, which will be deleted when Weasis is closed.
   * `{tag::<key>}` any DICOM attribute value from the selected image, e.g. `{tag:AccessionNumber}`
   * `{pref:<key>}`  any preferences, e.g. `{pref:weasis.user}`.

{{% notice note %}}
The Other Launcher is a special launcher that allows you to display a button on [any viewers](../gui#list-of-other-viewersplayers-in-the-dicom-workspace). For this type, only `{pref:<key>}` can be used as a dynamic variable.
{{% /notice %}}

### How to run the third-party launcher

* From the main menu, open _File > Launcher_ and select the desired launcher
* From the toolbar click on the launcher button

{{% notice note %}}
The launcher must be enabled in the preferences to be displayed in the menu and toolbar.
{{% /notice %}}
