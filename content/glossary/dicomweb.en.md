---
title: "What Is DICOMweb?"
linkTitle: "DICOMweb"
description: "DICOMweb is the set of RESTful web services for DICOM: query, retrieve and store over HTTP."
keywords: [ "what is dicomweb", "dicomweb explained", "qido-rs", "wado-rs", "stow-rs", "dicom rest api" ]
---

## <center>What Is DICOMweb</center>

**DICOMweb** is the part of the DICOM standard that defines web services over HTTP, as an
alternative to the classic DIMSE network protocol. Instead of a dedicated port and association
negotiation, a client makes ordinary HTTP requests — which is what makes a browser, a portal or a
firewalled viewer able to talk to an archive at all.

Three services carry most of the traffic. **QIDO-RS** searches for studies, series or instances and
answers with metadata, typically JSON. **WADO-RS** retrieves — the instances themselves, their
metadata, rendered frames or bulk pixel data. **STOW-RS** stores, sending instances to the archive.
A fourth, **UPS-RS**, manages worklist items.

Practically, DICOMweb means an archive is reachable with a URL, standard HTTP status codes and an
`Authorization` header — so a token can travel in a header instead of being pasted into a query
string, and access can be brokered by the same infrastructure as the rest of a hospital's web
traffic.

It does not replace DIMSE everywhere: C-FIND, C-GET, C-MOVE and C-STORE remain how most archives and
modalities talk to each other inside the network.

In Weasis, see [DICOMweb configuration](../../tutorials/dicomweb-config).
