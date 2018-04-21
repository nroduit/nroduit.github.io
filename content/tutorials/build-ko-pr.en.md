---
title: Build KO and PR
weight: 30
description: How to build and export DICOM Key Object Selection and Presentation State (GSPS)
keywords: [ "Key Object Selection", "Presentation State", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to build and export DICOM KO and PR</center>

### Key Object Selection (KO)

- To display KO Toolbar, select in menu: View > Toolbars > Key Object Selection Toolbar
- Click on the right icon over the image to select the Key Object Selection. Click on the star icon (or press 'k') to create in a new KO or to add the key image.

    ![Build KO](/tuto/ko-pr/build-ko.jpg?height=350)

### Presentation State (PR or GSPS)
- Open PR: Since Weasis 2.6.0 PRs are not applied to the image by default (requires to select the right icon over the image). To apply the most recent PR by default, change it in the [preferences](../../basics/customize/preferences/).
- Create PR: Any type of annotations can be exported in DICOM Presentation State. Image presentation (zoom, W/L, LUT...) will be exported in a future version.

    ![Build PR](/tuto/ko-pr/build-pr.jpg?height=350)

### Exporting Key Object Selection or Presentation State
- To export KO or PR, select in the menu: File > Export > DICOM
    1. Locally
      ![Export KO locally](/tuto/ko-pr/export-local.png?height=250)
    2. Remotely
      ![Export KO remotely](/tuto/ko-pr/export-remote.png?height=250)
