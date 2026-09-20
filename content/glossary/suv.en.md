---
title: "What Is SUV in PET/CT?"
linkTitle: "SUV"
description: "The standardized uptake value normalizes PET activity by injected dose and body size, so uptake can be compared."
keywords: [ "what is suv", "suv pet ct", "standardized uptake value", "suvbw", "suv max", "pet quantification" ]
---

## <center>What Is SUV in PET/CT</center>

The **standardized uptake value (SUV)** turns the raw activity concentration a PET scanner measures
into a number that can be compared between patients and between examinations. It divides the
measured concentration by the **injected dose** and normalizes for **body size** — by weight for
SUV~bw~, the most common form, and by lean body mass or body surface area for the variants.

A region of interest usually reports several figures: **SUV~max~**, the single hottest voxel, robust
to how the region was drawn but sensitive to noise; **SUV~mean~**, the average over the region,
steadier but dependent on where the boundary was placed; and **SUV~peak~** as a compromise.

SUV is only as good as the data behind it. It depends on the injected activity, the injection time
and the decay correction being recorded correctly in the DICOM attributes, on the uptake interval
between injection and acquisition, and on the reconstruction the scanner applied. Values from
different scanners, protocols or uptake times are not directly comparable, which is why a change in
SUV on a follow-up study is read with the acquisition parameters in hand rather than on its own.

In Weasis, see [PET/CT Image Fusion with SUV](../../tutorials/fusion).
