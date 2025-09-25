# Only works if num reducers = 1
import sys

word_info = []
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) < 3:
        continue
    word, count, docids_str = parts[0], int(parts[1]), parts[2]
    word_info.append((word, count, docids_str))

# Sort: highest count, then lexicographically
top_10 = sorted(word_info, key=lambda x: (-x[1], x[0]))[:10]
for word, count, docids_str in top_10:
    print(f"{word}\t{count}\t{docids_str}")
