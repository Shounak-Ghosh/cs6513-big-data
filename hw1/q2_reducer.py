# Basic Inverted Index Construction
# Reducer
import sys

current_word = None
docids = set()

for line in sys.stdin:
    word, docid = line.strip().split('\t')
    if word != current_word:
        if current_word:
            print(f"{current_word}\t{','.join(sorted(docids))}")
        current_word = word
        docids = set()
    docids.add(docid)

# Output last word
if current_word:
    print(f"{current_word}\t{','.join(sorted(docids))}")
