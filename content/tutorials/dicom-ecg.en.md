---
title: DICOM ECG Viewer
weight: 70
description: How to display electrocardiography data
keywords: [ "dicom ecg", "ecg", "electrocardiography", "dicom viewer", "open source dicom viewer" ]
---

## <center>Displaying electrocardiography data {{< svg-inline "static/tuto/icon/ecg.svg" >}}</center>

The ECG viewer displays and analyzes electrocardiogram waveforms stored as DICOM Waveform objects — resting and stress 12-lead ECGs, ambulatory recordings, and rhythm strips. It also provides simple on-screen calipers for measuring intervals and amplitudes, with support for the common lead layouts (12-lead, 3-lead, rhythm strip).

Try to open an ECG sample {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/ecg.xml"
{{< /launch >}}

![ECG Viewer](/tuto/ecg.png?classes=shadow&width=100%)
<br>

### Toolbar {{% badge style="red" %}}A{{% /badge %}} {#toolbar}
Actions in the toolbar are:
* {{< svg-inline "static/tuto/icon/print.svg" >}} **Print** the ECG as displayed, with basic patient and study identification.
* {{< svg-inline "static/tuto/icon/metadata.svg" >}} **Show DICOM metadata** of the waveform object — opens the full [DICOM attributes](tags).
* {{< svg-inline "static/tuto/icon/selectionDelete.svg" >}} **Clear all measurements** (the yellow caliper bands in the image above), see [Markers](#markers).

### Zoom and Display Format {{% badge style="red" %}}B{{% /badge %}} {#zoom-and-display-format}
Three controls govern how the traces are drawn:

* **Time scale (X-axis)** — millimeters per second; defaults to _auto mm/s_, which fits the recording to the available width.
* **Voltage scale (Y-axis)** — millimeters per millivolt; defaults to _auto mm/mV_, which fits the dynamic range vertically.
* **Aspect-preserving zoom slider** — scales both axes together so the visual aspect ratio is preserved.

The **Display Format** menu chooses the lead layout (e.g. 12 × 1, 6 × 2, 3 × 4 + rhythm strip), independent of the zoom.

### Lead and Cursor information {{% badge style="red" %}}C{{% /badge %}} {#lead-and-cursor-information}
Moving the cursor over the traces updates two readouts:

* **Lead label** — minimum and maximum voltage observed on that lead across the whole recording.
* **Cursor readout** — time and voltage at the cursor position.

### Markers {{% badge style="red" %}}D{{% /badge %}} {#markers}
Markers are on-screen calipers (yellow bands above) defined by a start and an end point on the same lead. Each marker reports:

| Field          | Meaning                                                                  |
|----------------|--------------------------------------------------------------------------|
| _Start Time_   | Time in seconds at the first point                                       |
| _Start Value_  | Voltage in millivolts at the first point                                 |
| _Stop Time_    | Time in seconds at the second point                                      |
| _Stop Value_   | Voltage in millivolts at the second point                                |
| _Duration_     | Elapsed time between the two points                                      |
| _Difference_   | Signed voltage difference (_Stop Value_ − _Start Value_)                 |
| _Amplitude_    | Maximum voltage variation observed between the two points                |

Mouse actions:

* **Add a start point** — click
* **Add an end point** — Ctrl + click, or right-click
* **Delete the measurement on a lead** — middle-click, or Shift + click
* **Delete every measurement** — the toolbar button above

{{% notice note %}}
Only one measurement can be active per lead. Placing a new start point on a lead that already has one replaces it.
{{% /notice %}}

### Annotations {{% badge style="red" %}}E{{% /badge %}} {#annotations}
The annotations panel surfaces two related groups of DICOM metadata stored with the waveform:

* **Acquisition Context** — conditions present during recording (patient state, electrode placement, device settings, etc.).
* **Waveform Annotations** — measurements, classifications, regions of interest, or events that may affect interpretation (for example, the timestamp at which the subject coughed or moved).