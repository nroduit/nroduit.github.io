---
title: Histogram
weight: 200
description: How to display histogram of real values and output LUT
keywords: [ "histogram", "LUT", "VOI LUT",  "Modality LUT" ]
---

## Displaying Histogram

Displaying the histogram allows you to view the distribution of the modality values.

{{% notice note %}}
Displaying the histogram allow to better understand the effect on the pixel distribution wen changing all the LUT parameters from the Image Tool right panel.
{{% /notice %}}

To open the histogram, select the "Histogram" layout from the Layouts dropdown button (see the image below).

General histogram parameters:

* *Channel:* With gray images only the Luminance channel is available. With color images, you can choose one of the following color models: RGB, HSV and HLS.
* *Bins:* The bins are the intervals values of pixels. By default, this number is calculated by the max value minus the min value and cannot exceed 512. The value entered must be between 64 and 4096.
* *Statistics:* Show the statistics of the histogram which allow to analyze and to compare images or image regions in a quantitative way (Pixels, Min, Max, Median, Mean, StDev, Skewness, Kurtosis, Entropy).

{{% notice note %}}
The values on the x-axis represent the modality values (e.g. Hounsfield for CT) or the pixel values for some modalities such as XA or MR. If the unit of the pixel value of the modality exists, it is visible at the end of the histogram title.
{{% /notice %}}

![Open Histogram](/tuto/histo/histo.png?height=400)

{{% notice tip %}}
To display the LUT on the image, select it from the Display panel on the right.
{{% /notice %}}


Display histogram parameters:

* *-/+:* shrink/strech the y-axis scale (the number of occurences)
* *Accumulate:* Display a cumulative histogram
* *Logarithmic:* Show the number of occurences in a logarithmic scale (y-axis).
* *Show intensity color:* Show the bin with the LUT colors, otherwise in black.
* *Reset:* Set the default parameters

{{% notice note %}}
It is possible to display the histogram of a region with the measurement tools. Simply select the region to display its histogram (see the image below).
{{% /notice %}}

![Histogram parameters](/tuto/histo/histo2.png?height=400)

{{% notice tip %}}
Clicking on the histogram bin allows displying the number of occurences and the modality range values of the selected bin.
{{% /notice %}}
