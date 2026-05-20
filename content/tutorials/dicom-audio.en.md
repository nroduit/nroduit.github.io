---
title: DICOM Audio Player
weight: 90
description: How to listen to DICOM audio data
keywords: [ "dicom au", "au", "audio", "dicom viewer", "open source dicom viewer" ]
---

## <center>Playing DICOM AU data {{< svg-inline "static/tuto/icon/audio.svg" >}}</center>

The DICOM Audio SOP Class (commonly referred to as DICOM AU) stores waveform audio inside a DICOM object. It is most often used for **voice annotations** dictated by the technologist or radiologist, **Doppler ultrasound** audio, **phonocardiography**, and other acoustic signals captured alongside an imaging study.

Weasis opens these objects in a dedicated player launched by double-clicking the audio thumbnail in the [DICOM Explorer](dicom-explorer).

Try to open a DICOM AU sample {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/audio.xml"
{{< /launch >}}

![Audio Player](/tuto/dicom-audio.png?classes=shadow&width=780px)
<br>

### Toolbar {{% badge style="red" %}}A{{% /badge %}} {#toolbar}
* {{< svg-inline "static/tuto/icon/metadata.svg" >}} **Show DICOM metadata** — opens the [DICOM attributes](tags) of the audio object.

### Play {{% badge style="red" %}}B{{% /badge %}} {#play}
The _Play_ button toggles between playback and pause. The slider lets you scrub through the recording; the current position is displayed in seconds.

### Volume {{% badge style="red" %}}C{{% /badge %}} {#volume}
Adjusts playback volume independently of the system mixer.

### Export Audio File {{% badge style="red" %}}D{{% /badge %}} {#export-audio-file}
Saves the embedded waveform to disk as either:
* **AU** — the format used by the DICOM payload itself, preserved as-is.
* **WAVE (.wav)** — re-encoded for broad compatibility with consumer audio players and editors.