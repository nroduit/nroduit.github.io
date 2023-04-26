---
title: Build DICOM KO and PR
weight: 400
description: How to build and export DICOM Key Object Selection and Presentation State (GSPS)
keywords: [ "Key Object Selection", "Presentation State", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
---

## <center>How to build and export DICOM KO and PR</center>

### Key Object Selection (KO)

- In order to display KO Toolbar, select in the main menu: View > Toolbars > Key Object Selection Toolbar
- When a DICOM KO is loaded then it appears in the explorer menu (1) or it can be selected from the icon on the right of the view (6).
- Click on the star icon (3) to add the key image or press 'k' to create in a new KO.
  ![Build KO](/tuto/ko-actions.jpg?classes=shadow&width=700px)
- Other actions:
 
  - Apply a KO (2)
  - Filter to obtain only the key images defined in the selected KO (4). This means only key images will be visible when scrolling into a series.
  - Create a new KO (or based on another one) or delete KO (only the ones created by Weasis) (5)


### Presentation State (PR or GSPS)
- Apply PR loaded from a DICOM file (1): Since Weasis {{< badge "v2.6.0" >}} PRs are not applied to the image by default (requires to select the right icon (2) over the image). In order to apply the most recent PR by default, change it from the main menu File > Preferences (Alt + P) and check "Apply by default the most recent Presentation State", or in the [default preferences](../../basics/customize/preferences/).
- Create a new PR: Any type of annotations (Drawings and Measurements) can be exported in a DICOM Presentation State. Image presentation actions (zoom, calibration, W/L, LUT...) are not yet possible to export into PR.
  ![Build PR](/tuto/pr-actions.jpg?classes=shadow&width=700px)
<br>
### Exporting Key Object Selection or Presentation State
- In order to export KO or PR, select the DICOM Export icon or in the menu: File > Export > DICOM
 ![Export KO locally](/tuto/export-ko-pr.png?classes=shadow)
<br>
1. Select the export type (locally or remotely)
2. Choose the exporting options (series created by Weasis have the flag "NEW")
3. Select the patient/study/series/instance to export
4. Export the selection and close the Window

