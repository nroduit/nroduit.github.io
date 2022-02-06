---
title: Getting Started
keywords: [ "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer", "clinical viewer", "radiolgical viewer", "linux dicom viewer",  "mac dicom viewer" ]
weight: 5
pre: "<b>1. </b>"
---

### Try Weasis now

These native installers below replace the weasis-portable.zip package (still available [here](https://sourceforge.net/projects/dcm4che/files/Weasis/) until version 4.0) and no longer requires Java to be installed on the system. It also serves as a basis for launching Weasis from a web context using the [weasis protocol](weasis-protocol). See below the differences between the [weasis distributions](#weasis-distributions).

{{< latest-download "deb" >}}

See this [page](download) for getting the list of all the packages to download and other Websites distibuting Weasis.<br>
For more information about [the GLIBC versions regarding the life cylcle of the different Linux distributions](https://gist.github.com/wagenet/35adca1a032cec2999d47b6c40aa45b1#file-glibc-md).

{{% notice note %}}
To manage Weasis version at the server side, it is possible to install the [Weasis web package](https://github.com/nroduit/weasis-pacs-connector#installation) which will upgrade the native installation at the client side (it works for minor releases by updating all the plug-ins except the launcher).<br>
The different possibilities for integrating Weasis with other systems are described [here](../basics/customize/integration).
{{% /notice %}}

{{% notice tip %}}
Join the [google group](http://groups.google.com/forum/#!forum/weasis) (Choose Email to read this group) to stay informed about new releases and updates.
{{% /notice %}}

### General Topics

- [Live demo](../demo) with different DICOM dataset.
- [Weasis Web Protocol](weasis-protocol)
- [Installing Weasis in DCM4CHEE](dcm4chee)
- [Tutorials](../tutorials)
- [Weasis Forum](http://groups.google.com/group/dcm4che)
- [Frequently Asked Questions (FAQs)](../faq)
- [Dicom Conformance and IHE](../basics/dicom)
- [Get Involved!](../get-involved)

### Developer Documentation

- [Building Weasis from source](building-weasis)
- [Weasis Architecture](../basics/architecture)
- [Weasis Plug-in Development Guidelines](guidelines)
- [How to build and install a plug-in](../basics/customize/build-plugins)
- [How to launch Weasis from any environments](../basics/customize/integration)
- [Translating Weasis Plug-ins](translating)
- [Weasis Preferences](../basics/customize/preferences)
- [Building weasis-pacs-connector](https://github.com/nroduit/weasis-pacs-connector#build-weasis-pacs-connector) 
- [Issues on Github](https://github.com/nroduit/Weasis/issues)

### Weasis distributions

The table below shows the differences between the distributions (the answer yes is the best):

- **Weasis native installer**: Windows MSI, macOS PKG, and Linux RPM and DEB. Can be used as a standalone application or connected to the web distribution (allows you to launch the defined version remotely)
- **Weasis portable**: weasis-portable.zip. Can be used in removable devices.
- **Weasis web with Java Webstart**: weasis.war and using Java Webstart as launcher (JNLP). Java Webstart has been removed from Java 11.

<font size="2">

| Description of features | Weasis native installer | Weasis portable | Weasis web with Java Webstart |
| --------------- | ------ | ------ | ------ |
| Does not require a Java installation | Yes | No but a JRE related to the system can be placed in the package (e.g. jre/windows) | No |
| Does not require admin permissions to install | No | Yes (except on recent Mac OS X versions) | No (requires Java installation) |
| Supported Java 11 or superior | Yes | Yes but only from Weasis 3.5 | No (JWS has been removed from Java 11) |
| Start from web page | Yes | N/A | Yes but directly only with JNLP protocol, otherwise required to download and execute jnlp file |
| Start from any software | Yes | No | Yes but only with JNLP protocol |
| Start from command line | Yes (use weasis protocol without additional information) | Yes (required to know the script location) | Yes with javaws (required a third-party software to build the JNLP file dynamically) |
| Single instance mechanism | Yes (smart rules based on profile) | Partially (only on Windows without smart rules) | Yes but contains several issues
| Supports HiDPI monitors | Yes | Yes but only when running Java 13 or superior | No |
| Shortcut to launch from the OS | Yes | No | No |
| Running on recent Mac OS X | Yes (supports sandboxing) | No | Yes but it requires to have Java 8 as default Java version |
| Menu integration on Mac OS X | Yes | Yes from Weasis 3.5 but only when running Java 9 or superior | No |
| OS integration for all the machine users | Yes | No | No |
| DICOM files association at the system level with Weasis | Yes | No | No |
| Register weasis protocol at the system level | Yes | No | No |
| Loading studies with DICOMWeb RESTful archive from a web context | Yes (can be done directly without weasis-pacs-connector) | N/A | No (not implement in weasis-pacs-connector) |
| Launch by weasis-pacs-connector | Yes (required weasis-pacs-connector 7.1.1) | N/A | Yes but weasis-pacs-connector 7.1.1 must be called by the deprecated service http://hostname/weasis-pacs-connector/viewer |
| Integration with dcm4chee-2.x web portal | Yes (required weasis-pacs-connector 6.1.5) | N/A | Yes (required weasis-pacs-connector 6.x) |
| Integration with dcm4chee-arc-light web portal | Yes | N/A | Yes |
| Weasis automatic remote update | Yes (except Java and the launcher) | N/A | Yes |
| Handle preferences at server-side | Yes | N/A | Yes |
| API to manage user remote preferences | Yes | N/A | Yes from Weasis 3.5 |
| API to manage launcher configuration | Yes | N/A | Yes from Weasis 3.5 (not implement in weasis-pacs-connector and not fully compliant) |

</font>
