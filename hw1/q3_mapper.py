import sys

for line in sys.stdin:
    word, docids_str = line.strip().split('\t')
    docids = docids_str.split(',')
    print(f"{word}\t{len(set(docids))}\t{','.join(sorted(docids))}")
