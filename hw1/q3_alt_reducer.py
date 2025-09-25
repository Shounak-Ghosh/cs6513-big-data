import sys

top_10 = []
for line in sys.stdin:
    count_str, word, docids_str = line.strip().split('\t')
    count = int(count_str)
    top_10.append((count, word, docids_str))

# Sort by doc count descending, then word lex ascending
top_10 = sorted(top_10, key=lambda x: (-x[0], x[1]))[:10]

for count, word, docids_str in top_10:
    print(f"{word}\t{count}\t{docids_str}")
