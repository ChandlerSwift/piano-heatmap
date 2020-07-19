#!/usr/bin/env python3
import sys

header = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg version="1.1" baseProfile="full" width="1300" height="100" xmlns="http://www.w3.org/2000/svg">
"""

footer="""</svg>
"""

def get_nth_octave(nth: int):
	octave = ['c', 'd', 'd-flat', 'e', 'e-flat', 'f', 'g', 'g-flat', 'a', 'a-flat', 'b', 'b-flat']
	return [f"{note}-{nth}" for note in octave]

all_88_keys = ['a-0', 'b-0', 'b-flat-0']
for octave in [1,2,3,4,5,6,7]:
	all_88_keys += get_nth_octave(octave)
all_88_keys += ['c-8']

content = ""
x_position = 0
for index, key in enumerate(all_88_keys):
	if key.startswith(("a","b","d","e","g")) and not "flat" in key and key != 'a-0': 
		index += 1  # hackety hack hack: put flats before the keys they're the flat of (e.g. Bb before B)
	if "flat" in key:
		width = 15
		height = 50
		x = x_position - 32.5
		index -= 1
	else:
		width = 25
		height = 100
		x = x_position
		x_position += 25
	content += f"""	<rect style="fill:#ffffff;stroke:#000000;stroke-width:1;" id="key-{index + 21}" data-note-name="{key}" width="{width}" height="{height}" x="{x}" y="0" />
"""

output = header + content + footer

if len(sys.argv) == 2:
	dest = sys.argv[1]
else:
	dest = input("file to write to (or blank for stdout):")

if dest == "":
	print(output, end="")
else:
	with open(dest, 'w+') as f:
		f.write(output)
