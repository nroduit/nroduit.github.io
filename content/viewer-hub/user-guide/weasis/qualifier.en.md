---
title: Package Qualifier
description: Qualifier usage
keywords: [ "qualifier" ]
weight: 40
---

## Default values

When calling the ViewerHub, Weasis will send in an Http header the version installed on the client workstation (User-Agent header).

If the corresponding Weasis version has not been installed on ViewerHub and/or when no qualifier has been associated with the user/host/group making the request, a version and/or a qualifier are used by default to retrieve the resources to launch Weasis.

These default values are defined in the config-server in the application-package.yml file.

## Qualifier mapping to user/host/group

In order to be able to test specific versions or to be able to launch a version of Weasis different from the default one for a group, it is possible to specify the version to launch for a user/host/group by mapping a particular qualifier.

![group_config_creation.png](/viewer-hub/qualifier/group_config_creation.png)

In order to use this feature:
- the weasis-native.zip file containing the specific version must be loaded into ViewerHub and associated with a group.
- the "qualifier" property must be defined in the launch_preferred table and must be of type "qualifier".

![launch_preferred_qualifier.png](/viewer-hub/qualifier/launch_preferred_qualifier.png)

- the mapping of the qualifier to use this version must be done at the launch table level for the target/launch_config/launch_preferred association. <br/>
If this mapping is not done, the default qualifier defined in ViewerHub configuration will be taken into account (see previous paragraph). <br/>
In order to do this mapping, you must define a configuration in the launch table associating the desired group/launch_config, the previous launch_preferred "qualifier" and for the "selection" column specify the qualifier to launch.

![launch_qualifier.png](/viewer-hub/qualifier/launch_qualifier.png)