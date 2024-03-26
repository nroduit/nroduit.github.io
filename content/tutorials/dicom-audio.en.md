---
title: DICOM Audio Player
weight: 90
description: How to listen to DICOM audio data
keywords: [ "dicom au", "au", "audio", "dicom viewer", "open source dicom viewer" ]
---

## <center>Playing DICOM AU data {{< svg "static/tuto/icon/audio.svg" >}}</center>

This player is used to play audio data defined by the DICOM AU standard.

Try to open DICOM AU {{< launch >}}
$dicom:get -w "https://nroduit.github.io/demo-archive/demo/audio.xml"
{{< /launch >}}

![Audio Player](/tuto/dicom-audio.png?classes=shadow&width=780px)
<br>
### Toolbar {{< badge "A" >}}
Actions in the toolbar are:
* {{< svg "static/tuto/icon/metadata.svg" >}} Show the DICOM metadata of the DICOM AU

### Play {{< badge "B" >}}
The _Play_ button allows you to play and pause. The slicer allows you to navigate through the audio file and display the position in seconds.

### Volume {{< badge "C" >}}
This slider allows you to adjust the volume of the audio file.

### Export Audio File {{< badge "D" >}}
The _Export Audio File_ button allows you to save the audio file in the format AU or WAVE.