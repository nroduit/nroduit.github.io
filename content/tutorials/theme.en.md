---
title: Styles and themes
weight: 530
description: How to apply another style and theme
keywords: [ "theme", "style", "flatlaf", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Change the appearance of the user interface</center>

### How to apply another theme
From the main menu, open _File > Preferences (Alt + P)_ and select the _Appearance_ tab. Use the dropdown list {{% badge style="red" %}}A{{% /badge %}} to browse the available themes, then click _Show_ to see a partial preview of the selected theme.

![Preferences](/tuto/theme-prefs.png?classes=shadow)
<br>

### How to scale the user interface
It is recommended to adapt the scale factor to the one of the system {{% badge style="red" %}}B{{% /badge %}}. In this way, Weasis will scale on HiDPI displays as the operating system. On Windows it is the *Display Scaling* preference, and on Linux it is either the display scaling factor or the text scaling factor.

However, the scaling factor can be increased (or even decreased) independently of the system. That means all the elements of the graphical interface will be adapted (fonts, icons, graphic components...).

### How to integrate the main menu in the window bar
The option {{% badge style="red" %}}C{{% /badge %}} allows you to force the integration of the main menu in the window bar (not activated by default). This option appears only on Linux because there is a wide variety of window managers.

{{% notice info %}}
On Windows and Mac this option does not appear because it is always supported.
{{% /notice %}}

### System File Chooser
The option {{% badge style="red" %}}D{{% /badge %}} allows you to enable the system native file chooser instead of the Java common one, providing a more familiar file browsing experience on each platform.

{{% notice tip %}}
If you have configured favorite or bookmarked folders in your system file explorer (e.g. Nautilus, Finder, Windows Explorer), they will automatically appear as shortcuts in the native file chooser.
{{% /notice %}}

### Changing the default theme or scale factor
See [preferences](../basics/customize/preferences)
