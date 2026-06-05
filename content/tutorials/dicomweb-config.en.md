---
title: DICOMweb Configuration
weight: 12
description: How to configure a DICOMweb node for query, retrieve, and store
keywords: [ "dicom import", "dicomweb", "qido", "wado", "stow", "oauth2", "keycloak", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer", "pacs viewer" ]
---

## <center>How to configure a DICOMweb node</center>

**DICOMweb** is the modern, HTTP-based set of DICOM services (QIDO-RS for query, WADO-RS for retrieve, STOW-RS for store, plus the legacy WADO-URI). Once a DICOMweb node is configured in Weasis, it shows up in the [DICOM Query/Retrieve](dicom-import/#dicom-queryretrieve) dialog and behaves like any other archive.

This page covers manual configuration inside Weasis. If you embed Weasis in a web portal, you can also [launch it from a web context](../basics/customize/integration/#download-directly-with-dicomweb-restful-services) so that the DICOMweb parameters are derived automatically from the launch URL — no per-user configuration required.

### General Configuration Steps {#general-configuration-steps}

1. Open **_File > Preferences_** (Alt + P).
2. Select **DICOM node list** in the left sidebar.
3. Click **Add new** to create a new node, or select an existing one and click **Edit**.

![DICOMweb nodes configuration](/tuto/dicomweb-nodes.png?classes=shadow&width=750px)

<br>

In the node dialog:

1. Give the node a descriptive **name**.
2. Pick a **service type**. The default `DICOMweb (all RESTful services)` covers query, retrieve, and store at once. To restrict the node to a specific service, pick one of:
   - **QIDO-RS** — query.
   - **STOW-RS** — store.
   - **WADO-URI (non-RS)** — legacy single-object retrieval. Combines a classic C-FIND query with a WADO-URI retrieve (see [Query/Retrieve](dicom-import/#dicom-queryretrieve)).
   - **WADO-RS (Retrieve)** — modern retrieve.
3. Enter the **service URL** of the DICOMweb server.
4. Configure **authentication** by clicking **Manager**, then **Add**:
   - Either pick a template from the list and click **Fill** to populate some fields, or fill them in manually.
   - In the **Provider** panel, every field is mandatory.
   - In the **Registration** panel, every field is optional — except for **OAuth2**, where the **Client ID**, **Client Secret**, and **Scope** must be filled. **Audience** is optional, but some providers need it.
   - The **Grant Type** selector chooses the OAuth2 flow:
     - `code` (**Authorization Code**, the default) — interactive login: Weasis opens your browser so you sign in with your account, then receives the token through a loopback redirect. Use this for user-facing access.
     - `client_credentials` (**Client Credentials**, RFC 6749 §4.4) — non-interactive, server-to-server: Weasis obtains the token directly from the token endpoint using only the Client ID and Client Secret, with **no browser login**. Use this for service/headless accounts.
   - Click **OK** to save the authentication.
5. Optionally, add **HTTP headers** that should be sent with every request to this service URL (useful for tokens or other custom auth schemes).
6. Click **OK** to save the node.

Then open the [DICOM Import](dicom-import/#dicom-queryretrieve) dialog and pick the new node. If OAuth2 is configured with the **Authorization Code** grant, the first query opens your browser to complete the sign-in; subsequent queries reuse the cached token. With the **Client Credentials** grant, no browser login is required — Weasis authenticates silently using the configured Client ID and Secret.

### Supported DICOMweb Providers (non-exhaustive list)

- [Google Cloud Healthcare API](#google-cloud-healthcare-api)
- [Orthanc WEB Server](#orthanc-web-server)
- [dcm4chee-arc-light](#dcm4chee-arc-light)
- [Amazon HealthLake](#amazon-healthlake)

#### Google Cloud Healthcare API

Google Cloud provides a comprehensive [DICOMweb implementation](https://cloud.google.com/healthcare/docs/how-tos/dicomweb) through the Healthcare API.

Configuration (see also the general steps [above](#general-configuration-steps)):

1. Create a new DICOMweb node with a descriptive name.
2. Pick **DICOMweb (all RESTful services)**.
3. Enter the Google repository URL (must end with `/dicomWeb`).
4. Configure authentication by clicking **Manager**, then **Add**:
    1. Pick the **Google Cloud Healthcare** template.
    2. Click **Fill**.
    3. Enter your **Client ID** and **Client Secret**.
    4. Click **OK** to save the authentication.
5. Optionally, add HTTP headers for the Google API.
6. Click **OK** to save the node.

![Google node](/tuto/dicomweb-google-node.png?classes=shadow&width=750px)

<br>

![Google template](/tuto/dicomweb-google-auth.png?classes=shadow&width=750px)

{{% notice note %}}
The DICOMweb thumbnail service is not currently supported by the Google API, so series thumbnails will not preview before the full retrieve.
{{% /notice %}}

#### Orthanc WEB Server

[Orthanc](https://www.orthanc-server.com/) is a lightweight DICOM server with [DICOMweb capabilities](https://www.orthanc-server.com/static.php?page=dicomweb).

The screenshot below is configured for the public demo server, which requires no authentication. For your own Orthanc instance, replace the URL and configure the authentication method as described in the [general steps](#general-configuration-steps).

{{< highlight text >}}
https://demo.orthanc-server.com/dicom-web
{{< /highlight >}}

![Orthanc node](/tuto/dicomweb-orthanc.png?classes=shadow&width=750px)

<br>

{{% notice note %}}
The DICOMweb implementation in Orthanc does not currently support the [thumbnail service](https://www.dicomstandard.org/news/supplements/view/thumbnail-service-over-dicomweb), so series thumbnails will not preview before the full retrieve.
{{% /notice %}}

#### dcm4chee-arc-light

[dcm4chee-arc-light](https://github.com/dcm4che/dcm4chee-arc-light) is a robust open-source PACS that exposes DICOMweb services out of the box.

To configure a dcm4chee-arc-light node (see also the [general steps](#general-configuration-steps)):

1. Add a new DICOMweb node.
2. Enter a description (e.g. `DCM4CHEE Archive`).
3. Pick the DICOMweb service.
4. Enter the URL of your dcm4chee-arc-light server. The default endpoint follows this pattern:
    {{< highlight text >}}
    http(s)://[server-address]:[8080|8443]/dcm4chee-arc/aets/[AE_TITLE]/rs
    (e.g. http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE/rs)
    {{< /highlight >}}

If the dcm4chee-arc-light server requires authentication, configure it on both sides:

**In Weasis**

1. Click **Manager**, then **Add** to create a new authentication.
2. Pick the **Default Keycloak** template and fill in:
   - **Name** — `dcm4chee-arc-light`
   - **Base URL** — `https://[server-address]:8843`
   - **Realm** — `dcm4che`
   - **Client ID** — `weasis`
   - **Client Secret** — the secret you copy from Keycloak (see below).
   - **Scope** — `openid`
   - **Audience** — leave empty.

**In Keycloak** — register the Weasis client for DICOMweb access:

1. Sign in to the Keycloak Admin Console (typically `https://[server-address]:8843/admin/dcm4che/console` for the secure URL).
2. In the left menu, click **Clients > Create**.
3. **General settings**:
   - **Client Type** — `OpenID Connect`
   - **Client ID** — `weasis`
4. **Capability config**:
   - **Client authentication** — ON
   - **Standard flow** — ON
   - **Direct access grants** — ON
5. **Login settings**:
   - **Root URL** — leave empty.
   - **Valid Redirect URIs** — add `http://127.0.0.1*`.
   - **Web Origins** — add `+` to allow any origin that matches a Valid Redirect URI.
   - Click **Save**.
   - Copy the **Client Secret** from the **Credentials** tab and paste it into the Weasis authentication form above.

#### Amazon HealthLake

[Amazon HealthLake](https://aws.amazon.com/healthlake/) is a fully managed service for storing, transforming, querying, and analyzing healthcare data at scale.

Imaging data is exposed through the **AHI DICOMweb Proxy**. To consume it from Weasis, create a [DICOMweb node](#general-configuration-steps) with this URL:

{{< highlight text >}}
http://[EC2 instance IP or EC2/ALB DNS]:8080/aetitle
{{< /highlight >}}

The complete Weasis configuration is documented at the end of the [AHI DICOMweb Proxy README](https://github.com/aws-samples/aws-healthimaging-samples/tree/main/dicomweb-proxy#usage).