---
title: Styles and themes
weight: 530
description: How to apply another style and theme
keywords: [ "theme", "style", "flatlaf", "hidpi", "scaling", "dark mode", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>Change the appearance of the user interface</center>

The **Appearance** preferences let you tailor Weasis to your environment: pick a **light** or **dark** theme to match your reading conditions, adjust the **interface scaling** to fit your monitor's pixel density, and toggle a few platform-specific UI behaviors. Open the settings from **_File > Preferences (Alt + P) > Appearance_**.

### How to apply another theme

Use the theme dropdown {{% badge style="red" %}}A{{% /badge %}} to browse the bundled themes, then click **Show** to see a partial preview before applying. The recommended theme for clinical reading is **Core Dark — Flat Weasis**, which keeps the surrounding UI low-luminance to avoid distracting from the images.

![Preferences](/tuto/theme-prefs.png?classes=shadow)
<br>

### How to scale the user interface {#how-to-scale-the-user-interface}

The scaling factor {{% badge style="red" %}}B{{% /badge %}} controls the size of every UI element (fonts, icons, graphic components, …). It is recommended to **match the operating system's scaling factor** so Weasis looks consistent with the rest of your desktop on HiDPI displays:

- **Windows** — the *Display Scaling* preference (Settings > System > Display).
- **macOS** — automatically aligned with the system **Retina** scaling.
- **Linux** — either the display scaling factor or the text scaling factor, depending on the desktop environment.

You can also increase (or decrease) the scaling factor **independently of the system** — useful for reading from a distance, or when the system value is too aggressive for the application.

### How to integrate the main menu in the window bar
Option {{% badge style="red" %}}C{{% /badge %}} forces the main menu to be integrated into the window's title bar (disabled by default). It is shown only on **Linux**, where the wide variety of window managers makes integration unreliable without an explicit opt-in.

{{% notice info %}}
On **Windows** and **macOS**, this option is not shown — menu integration is always supported by the platform.
{{% /notice %}}

### System File Chooser
Option {{% badge style="red" %}}D{{% /badge %}} swaps the Java default file dialog for the **system-native file chooser**, providing a more familiar file-browsing experience on each platform.

{{% notice tip %}}
Favorite or bookmarked folders configured in your system file explorer (Nautilus, Finder, Windows Explorer, …) appear as shortcuts inside the native file chooser, so frequently used import or export locations are one click away.
{{% /notice %}}

### Changing the default theme or scale factor

When deploying Weasis to several workstations, the default appearance settings can be set centrally instead of being chosen per user. See the [Weasis Preferences](../basics/customize/preferences) page for the lookup order Weasis uses when resolving a preference.