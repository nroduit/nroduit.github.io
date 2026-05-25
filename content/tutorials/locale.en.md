---
title: Language & Regional Settings
weight: 540
description: How to change the language and regional settings
keywords: [ "languages", "locale", "region", "translation", "regional format", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "pacs viewer" ]
---

## <center>How to change the language and regional settings</center>

Weasis separates two locale-related choices:

- **Language** — the language of the user interface (menus, tooltips, dialogs).
- **Regional format** — the rules used to display **dates**, **times**, and **numbers** (decimal separator, thousands separator, calendar conventions…). These also drive how patient lists are sorted, see the [DICOM Explorer](dicom-explorer).

The two are independent, so you can run the UI in English while keeping the regional format you prefer.

### Switching from the user interface

From the main menu, open **_File > Preferences (Alt + P)_** and pick the desired **Language** and **Regional format** in the **General** tab.

![Preferences](/tuto/language-prefs.png?classes=shadow)
<br>

{{% notice tip %}}
Only languages with at least **30 % translation coverage** are listed. If a language you need is missing or incomplete, you can help fill the gaps — see the [translation contribution guide](../getting-started/translating).
{{% /notice %}}

{{% notice note %}}
Dates and numbers throughout the user interface are formatted according to the selected regional format.
{{% /notice %}}

### Changing the default locale at deployment

When deploying Weasis to multiple workstations, the default language and regional format can be set centrally via the property files instead of being chosen per user. See the [preferences overview](../basics/customize/preferences/#priority-order-for-loading-a-property) for the lookup order Weasis uses when resolving a preference.