---
title: Cryptography
description: "Encrypt the URL search parameters that launch Weasis, so identifiers such as the patient ID never travel in plain text."
keywords: [ "cryptography", "viewerhub", "url encryption", "query parameters", "patient identifier", "weasis launch" ]
weight: 90
aliases:
  # The file used to be named " cryptography.en.md", with a leading space, which
  # Hugo published at /viewer-hub/-cryptography/. Keep that address working for
  # anything that already links to it.
  - /viewer-hub/-cryptography/
---

When launching the Weasis viewer with ViewerHub, a URL containing search criteria in "query parameters" is used.

It is possible to encrypt these search parameters when launching the Weasis viewer in order to not transmit certain sensitive data in plain text (e.g. patient identifier).

To enable this feature, the application-cryptography.yml file in the config-server must be modified by setting the "enabled" field below to true.

{{< highlight yaml >}}
# - Cryptography
cryptography:
    enabled: false
    password: '{cipher}'
    salt: '{cipher}'
{{< /highlight >}}

Defining a password and a salt is also necessary to encode/decode the search parameters.

The same encryption algorithm must be used on the client side (encryption) and on the ViewerHub side (decryption).