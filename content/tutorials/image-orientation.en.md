---
title: Image orientation
weight: 50
description: How to interpret the orientation
keywords: [ "orientation", "dicom viewer", "free dicom viewer", "open source dicom viewer" ]
---

## <center>Interpretation of the orientation</center>

The orientation of the DICOM images is displayed by one or more uppercase letters in the middle on the top and left of the view.

If _Anatomical Orientation Type (0010,2210)_ [attribute](../tags/) is absent or has a value of BIPED, anatomical direction is:

* A: anterior
* P: posterior
* R: right
* L: left
* H: head
* F: foot

If _Anatomical Orientation Type (0010,2210)_ [attribute](../tags/) has a value of QUADRUPED (since Weasis {{< badge "v4.1.0" >}}), anatomical direction is designated by:
* LE: Left
* RT: Right
* D: Dorsal
* V: Ventral
* CR: Cranial
* CD: Caudal
* R: Rostral
* M: Medial
* L: Lateral
* PR: Proximal
* DI: Distal
* PA: Palmar
* PL: Plantar
![Quadruped orientation](/tuto/quadruped-orientation.jpg?classes=shadow)
<br>

{{% notice info %}}
If the orientation is not perfectly aligned according to the 3 axes of the referential then there can be a secondary and tertiary orientation (in subscript) separated by "-".
{{% /notice %}}

{{% notice info %}}
For some modalities such as CR or DX, the orientation comes from the _Patient Orientation (0020,0020)_ attribute and is not displayed when using the rotation tools because it cannot be recalculated dynamically.

For other modalities such as CT and MRI, the orientation is always displayed because it is dynamically calculated.
{{% /notice %}}

{{% notice tip %}}
To display or hide the orientation on the image, select it from the _Display_ panel on the right (DICOM Annotations > Orientation).
{{% /notice %}}


### Orientation in 2D multiplanar reconstruction (MPR)

The image below shows the 3 views of the orthogonal MPR. The uppercase letter at the left or at the top designates the orientation of each multiplanar view whose type (axial, coronal, sagittal) is defined at the bottom.

![MPR orientation](/tuto/mpr-orientation.jpg?classes=shadow)
<br>

{{% notice info %}}
The color of the axes used comes from the one defined in [DICOM Patient Orientation](https://dicom.nema.org/medical/dicom/current/output/chtml/part17/chapter_A.html). Blue corresponds to the left-right axis, the red axis to anterior-posterior, and the green axis to foot-head.

The colored square in the MPR view above corresponds to the plane that is perpendicular to one of the axes.
{{% /notice %}}


