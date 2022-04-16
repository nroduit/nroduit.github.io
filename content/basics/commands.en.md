---
title: Weasis Commands
description: List of commands at start-up and for driving Weasis
keywords: [ "commands", "weasis commands", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
weight: 50
---

The commands listed below can be applied at start-up or in a telnet session. All the commands starting with "dcmview2d:" allow to drive Weasis and are not adapted to be used at start-up.

{{% notice info %}}
This page matches to Weasis 2.5.1 or higher. The syntax of usage comes from <a target="_blank" href="http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html">POSIX</a>.
{{% /notice %}}

To obtain the list of commands, after starting Weasis, open a local telnet session of the OSGI Console and type `lb` for getting the list of bundles and their state or type `help` for getting all the available commands:

{{< highlight text >}}
telnet localhost 17179

Trying 127.0.0.1...

Connected to localhost.localdomain.

Escape character is '^]'.

____________________________

Welcome to Apache Felix Gogo

g!
{{< /highlight >}}

{{% notice tip %}}
**Modifying the default port number**: This value can be changed in the <a target="_blank" href="https://github.com/nroduit/">configuration of the launcher</a> (by overriding the property or with a new jnlp template)
{{% /notice %}}

### List of Weasis commands

#### dcmview2d:layout

{{< highlight text >}}
g! dcmview2d:layout
Select a split-screen layout
Usage: dcmview2d:layout ( -n NUMBER | -i ID )
  -n --number=NUMBER  select the best matching number of views
  -i --id=ID          select the layout from its identifier
  -? --help           show help
{{< /highlight >}}

#### dcmview2d:mouseLeftAction

{{< highlight text >}}
g! dcmview2d:mouseLeftAction
Change the mouse left action
Usage: dcmview2d:mouseLeftAction COMMAND
COMMAND is (sequence|winLevel|zoom|pan|rotation|crosshair|measure|draw|contextMenu|none)
  -? --help       show help
{{< /highlight >}}

#### dcmview2d:move

{{< highlight text >}}
g! dcmview2d:move
Pan the selected image
Usage: dcmview2d:move -- X Y
X and Y are Integer. It is mandatory to have '--' (end of options) for negative values
  -? --help       show help
{{< /highlight >}}

#### dcmview2d:reset

{{< highlight text >}}
g! dcmview2d:reset

Reset image display
Usage: dcmview2d:reset (-a | COMMAND...)
COMMAND is (winLevel|zoom|pan|rotation)
  -a --all        reset to original display
  -? --help       show help
{{< /highlight >}}

#### dcmview2d:scroll

{{< highlight text >}}
g! dcmview2d:scroll
Scroll into the images of the selected series
Usage: dcmview2d:scroll ( -s NUMBER | -i NUMBER | -d NUMBER)
  -s --set=NUMBER       set a new value from 1 to series size
  -i --increase=NUMBER  increase of some amount
  -d --decrease=NUMBER  decrease of some amount
  -? --help             show help
{{< /highlight >}}

#### dcmview2d:synch

{{< highlight text >}}
g! dcmview2d:synch
Set a synchronization mode
Usage: dcmview2d:synch VALUE
VALUE is (None|Stack|Tile)
  -? --help       show help
{{< /highlight >}}

#### dcmview2d:wl

{{< highlight text >}}
g! dcmview2d:wl
Change the window/level values of the selected image (increase or decrease into a normalized range of 4096)
Usage: dcmview2d:wl -- WIN LEVEL
WIN and LEVEL are Integer. It is mandatory to have '--' (end of options) for negative values
  -? --help       show help
{{< /highlight >}}

#### dcmview2d:zoom

{{< highlight text >}}
g! dcmview2d:zoom
Change the zoom value of the selected image
Usage: dcmview2d:zoom (set VALUE | increase NUMBER | decrease NUMBER)
  -s --set=VALUE        [decimal value]  set a new value from 0.0 to 12.0 (zoom magnitude, 0.0 => default, -200.0 => best fit, -100.0 => real size)
  -i --increase=NUMBER  increase of some amount
  -d --decrease=NUMBER  decrease of some amount
  -? --help             show help
{{< /highlight >}}

#### dicom:get

{{< highlight text >}}
g! dicom:get
Load DICOM files remotely or locally
Usage: dicom:get ([-l PATH]... [-w URI]... [-r URI]... [-p] [-i DATA]... [-z URI]...)
PATH is either a directory(recursive) or a file
  -l --local=PATH   open DICOMs from local disk
  -r --remote=URI   open DICOMs from an URI
  -w --wado=URI     open DICOMs from an XML manifest
  -z --zip=URI      open DICOM ZIP from an URI
  -p --portable     open DICOMs from configured directories at the same level of the executable
  -i --iwado=DATA   open DICOMs from an XML manifest (GZIP-Base64)
  -? --help         show help
{{< /highlight >}}

#### dicom:close

{{< highlight text >}}
g! dicom:close
Close DICOM files
Usage: dicom:close  (-a | ([-y UID]... [-s UID]...))
  -a --all           close all the patients
  -y --study=UID     close a study, UID is Study Instance UID
  -s --series=UID    close a series, UID is Series Instance UID
  -? --help          show help
{{< /highlight >}}

#### dicom:rs

{{< highlight text >}}
g! dicom:rs
Load DICOM files from DICOMWeb API (QIDO/WADO-RS)
Usage: dicom:rs -u URL -r QUERYPARAMS... [-H HEADER]... [--query-header HEADER]... [--retrieve-header HEADER]... [--query-ext EXT] [--retrieve-ext EXT] [--accept-ext EXT]
  -u --url=URL               URL of the DICOMWeb service
  -r --request=QUERYPARAMS   Query params of the URL, see weasis-pacs-connector
  -H --header=HEADER         Pass custom header(s) to all the requests
  --query-header=HEADER      Pass custom header(s) to the query requests (QIDO)
  --retrieve-header=HEADER   Pass custom header(s) to the retrieve requests (WADO)
  --query-ext=EXT            Additionnal parameters for Query URL (QIDO)
  --retrieve-ext=EXT         Additionnal parameters for Retrieve URL (WADO)
  --accept-ext=EXT           Additionnal parameters for DICOM multipart/related Accept header of the retrieve URL (WADO). Default value is: transfer-syntax=*
  --show-whole-study         when downloading a series, show all the other series (ready for download) from the same study
  -? --help                  show help
{{< /highlight >}}

#### image:get

{{< highlight text >}}
g! image:get
Load images remotely or locally
Usage: image:get ([-f file]... [-u url]...)
  -f --file=FILE     open an image from a file
  -u --url=URL       open an image from an URL
  -? --help          show help
{{< /highlight >}}

#### image close

{{< highlight text >}}
g! image:close
Close images
Usage: dicom:close (-a | ([-g UID]... [-s UID]...))
  -a --all         close all series
  -g --group=UID   close a group from its UID
  -s --series=UID   close an series/image from its UID
  -? --help        show help
{{< /highlight >}}

#### weasis:info

{{< highlight text >}}
g! weasis:info
Show information about Weasis
Usage: weasis:info (-v | -a)
  -v --version    show version
  -a --all        show weasis specifications
  -? --help       show help
{{< /highlight >}}

#### weasis:ui

{{< highlight text >}}
g! weasis:ui
Manage user interface
Usage: weasis:ui (-q | -v)
  -q --quit     shutdown Weasis
  -v --visible  set window on top
  -? --help     show help
{{< /highlight >}}

#### acquire:patient

{{< highlight text >}}
g! acquire:patient
Load Patient Context from the first argument
Usage: acquire:patient (-x | -i | -s | -u) arg
arg is an XML text in UTF8 or an url with the option '--url'
  -x --xml         open Patient Context from an XML data containing all DICOM Tags
  -i --inbound     open Patient Context from an XML data containing all DICOM Tags, decoding syntax is [Base64/GZip]
  -s --iurlsafe    open Patient Context from an XML data containing all DICOM Tags, decoding syntax is [Base64_URL_SAFE/GZip]
  -u --url         open Patient Context from an URL (XML file containing all DICOM TAGs)
  -? --help        show help
{{< /highlight >}}

#### weasis:config (only at launch)

This command can be used only at launch, see [Modify the launch parameters](../../getting-started/weasis-protocol/#modify-the-launch-parameters)


{{% notice note %}}
For identifying the commands at start-up, the symbol "$" must be added before the command (not required in the OSGI console). See examples below.
{{% /notice %}}

{{% notice warning %}}
**Special characters**:
A command containing special characters like '&' or space must be within quotes or double quotes. Example: 
dicom:get -w **"https://dicom.com/test&sopuid=322344"**
<br><br>
Depending the command line system, quotes or double quote needs to be escaped with a backslash. Ex. simple quote must be escaped in Eclipse but not in Intellij.
{{% /notice %}}

