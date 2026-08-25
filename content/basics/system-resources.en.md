---
title: System Resources
description: Understand the System resources panel and its hardware recommendations
keywords: [ "system resources", "memory", "performance", "hardware recommendation", "weasis dicom viewer", "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 60
---

Weasis routinely handles studies far larger than its memory: a CT or MR series is
hundreds of slices, a digital mammography image is tens of megabytes, a 3D volume
is hundreds of megabytes. The **System resources** panel shows, in real time, how
much of the machine Weasis is using, whether the hardware matches your daily
practice, and — when it does not — what to upgrade.

Open it from the menu **Help > System resources**.

The panel does not change anything by itself. It is a diagnostic view: it observes,
measures across all your sessions, and gives a verdict you can act on.

## How memory works in Weasis

To read the panel, it helps to know that Weasis uses memory in two separate pools:

- **JVM heap** — holds the user interface, the DICOM metadata and temporary
  copies of pixels. Its maximum size is fixed when Weasis starts.
- **Native image memory** — holds the *decoded pixel data* of images. This is the
  pool that grows when you open large studies. It is **not** part of the heap; it
  is sized from the physical memory of the machine.

A third pool, **GPU memory (VRAM)**, is used only by the 3D viewer.

This separation is why a single "memory" number is not enough — and why the panel
shows both pools side by side.

## Reading the panel

The dialog refreshes every two seconds while it is open. It has five sections.

### Hardware

A static description of the machine:

| Row | Meaning |
|---|---|
| Operating system | OS name, version and architecture |
| CPU cores | Number of processor cores available to Weasis |
| Physical memory | Total RAM of the machine |
| JVM heap maximum | Upper bound of the heap pool |
| Native memory budget | Upper bound of the decoded-image pool |
| Graphics processor | The GPU detected by the 3D viewer, and its OpenGL version |

{{% notice note %}}
The graphics processor row stays **not assessed** until a 3D view has been opened
at least once — Weasis only learns the GPU when the 3D engine starts. If it reports
**software rendering**, the 3D viewer is running without GPU acceleration and will
be slow; install or enable a proper graphics driver.
{{% /notice %}}

### Live pressure

Three bars showing current use, each with its peak value for the session:

- **JVM heap** — interface and metadata memory.
- **Native image memory** — decoded images currently cached.
- **CPU load** — processor use by Weasis.

A bar turning **red** above 90 % means that pool is close to its limit. Native
image memory reaching its limit is normal and harmless: Weasis simply drops the
least-recently-seen images from the cache and reloads them transparently when you
scroll back. A heap bar staying near 100 %, on the other hand, is a real warning
sign.

### Assessment

The verdict — the heart of the panel. Each line is rated with one of four levels:

| Level | Color | Meaning |
|---|---|---|
| **Collecting…** | neutral | Not enough activity yet to judge — keep using Weasis |
| **Sub-optimal** | red | The resource limited Weasis; the machine should have more |
| **Optimal** | green | The resource matched the workload well |
| **Abundant** | blue | The resource was barely used; the machine has spare capacity |

- **Overall** — the worst of the rows below.
- **Memory** — based on real failure signals, not on raw usage: out-of-memory
  errors, a 3D volume that had to spill to disk, or sustained garbage-collection
  overhead. A rare event is tolerated; a *recurring* one turns the verdict red.
- **CPU** — sub-optimal on 2 cores or fewer; abundant on 8+ cores left mostly idle.
- **Recommended upgrade** — see below.

{{% notice info %}}
The verdict is **cumulative across all your sessions**, not just the current one.
It stays **Collecting…** until Weasis has run long enough and done enough work to
judge fairly, so a fresh installation will not show a verdict immediately.
{{% /notice %}}

### Workload

What the heaviest study you opened actually demanded: the **largest image** (in
megabytes) and the **largest volume** (in number of slices). These explain *why*
a verdict came out the way it did.

### Events (all sessions)

The counters behind the memory verdict, accumulated over every session:

| Counter | What it means |
|---|---|
| Session uptime | This session, then total time and number of sessions |
| Cache evictions | Images dropped from the cache and reloaded — informational, not a problem |
| Out-of-memory errors | The heap ran out — turns red when it is driving a sub-optimal verdict |
| Volume disk spills | A 3D volume did not fit in memory and was written to disk — slow |
| Garbage-collection overhead | Share of time spent reclaiming heap memory; above ~10 % the heap is too small |

A non-zero count is not necessarily a problem — the panel colors a counter red
**only** when it is the signal currently causing a sub-optimal memory verdict.

## Acting on the recommendation

When **Memory** or **CPU** is sub-optimal, the **Recommended upgrade** line gives a
concrete target. Weasis distinguishes a *configuration* problem from a *hardware*
one:

- **A larger heap (`-Xmx`)** — shown when the machine has free RAM but Weasis was
  not allowed to use enough of it. This is fixed by changing a setting, not by
  buying hardware.
- **More RAM** — shown when the heap is already a fair share of physical memory:
  the machine itself is the limit.
- **More CPU cores** — shown when too few cores slowed image decoding and
  reconstruction.

### Increasing the memory limits

The heap maximum and the native-memory budget are controlled by start-up options.
The simplest way to raise the heap is the `-Xmx` option; the native-image pool is
controlled by a Weasis property:

| Option / property | Effect | Default |
|---|---|---|
| `-Xmx<size>` | Absolute maximum of the JVM heap, e.g. `-Xmx4g` | 25 % of RAM |
| `weasis.native.memory.percent` | Native image memory as a percentage of RAM (1–90) | 50 |

For an installed Weasis, edit the `java-options` of the application configuration
(for example `app/Weasis.cfg` next to the installation). For a study workstation
that opens large studies, raising the native-memory percentage keeps more images
cached and avoids reloads:

{{< highlight ini >}}
weasis.native.memory.percent=70
{{< /highlight >}}

{{% notice warning %}}
The heap and the native pool share the same physical RAM, so keep their combined
share comfortably below 100 %. Raising the heap *reduces* the room left for the
image cache. On a machine with little RAM, raising one means lowering the other.
{{% /notice %}}

The full set of memory parameters is described in the
[Memory Management developer guide](https://github.com/nroduit/Weasis/blob/master/weasis-core/docs/Memory-Management.md).

## Resetting the statistics

The **Reset statistics** button clears the measured history — total uptime, peaks
and event counters — so the verdict is rebuilt from the current run. The
**workload** (largest image and volume) and the graphics processor are kept, so
the panel still has something to judge from right away.

Peaks and counters only ever grow, and they reflect how a *given version* of
Weasis used memory, so an installed Weasis starts a fresh measurement after an
update:

| Property | Effect | Default |
|---|---|---|
| `weasis.resource.stats.clean.previous.version` | Clear the measured statistics when the Weasis version has changed from the previous launch | `true` |

## Exporting the report

The **Copy report** button places a plain-text summary of the whole panel on the
clipboard — hardware, verdict, recommendation and event counters. Paste it into a
[bug report](https://github.com/nroduit/Weasis/issues) or a message to your IT
department when asking for a hardware upgrade.

{{% notice tip %}}
The verdict and the limiting events are also written to the Weasis log files in
`<user home>/.weasis/log/`, and the cumulative statistics are kept in
`<user home>/.weasis/resource-stats.properties`. You do not need the panel open
for Weasis to keep measuring.
{{% /notice %}}