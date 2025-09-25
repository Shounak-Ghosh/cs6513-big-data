import sys

for line in sys.stdin:
    word, docids_str = line.strip().split('\t')
    docids = set(docids_str.split(','))
    doc_count = len(docids)
    # Emit doc count (zero-padded for sort consistency), word, and docids
    print(f"{doc_count:03d}\t{word}\t{','.join(sorted(docids))}")
