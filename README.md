# piano-heatmap

Tracks keystrokes played on MIDI keyboards, renders into a heatmap.

[Writeup on my website](https://chandlerswift.com/2020/07/19/piano-heatmap-part-2.html)

[motivation](https://chandlerswift.com/2015/09/10/piano-heatmap-part-1.html)

### Running piano-heatmap
I use a few web technologies that aren't universal. WebMIDI is the least common,
and, unfortunately the most essential to this application. Chromium and derived
browsers (Google Chrome, current Edge, etc) do support the technology. Firefox
does as well, with the
[Web MIDI API extension](https://addons.mozilla.org/en-US/firefox/addon/web-midi-api/)
from Jazz-Soft.

IndexedDB is used for longer-term per-machine storage. All current browsers
support this.
