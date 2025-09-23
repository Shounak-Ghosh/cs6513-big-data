# Basic Inverted Index Construction
# Mapper
import sys
import os
import re

def normalize(line):
    # Used ChatGPT for regex to remove non alphanumeric characters
    return re.sub(r'[^a-z0-9 ]', '', line.lower())

pathname = os.environ.get('mapreduce_map_input_file')
if pathname:
    filename = os.path.basename(pathname)

for line in sys.stdin:
    line = normalize(line).strip()
    words = line.split()
    if len(words) < 1:
        continue
    for word in set(words):  # Emit each word once per doc
        print(f"{word}\t{filename}")
