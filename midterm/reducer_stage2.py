#!/usr/bin/env python3
import sys
from collections import defaultdict

word_counts = defaultdict(int)
length_counts = defaultdict(int)
total_words = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue

    key_type, key_value, count_str = parts
    count = int(count_str)

    if key_type == "WORD":
        word_counts[key_value] += count
        total_words += count

    elif key_type == "LENGTH":
        length_counts[int(key_value)] += count

# Compute statistics
unique_words = len(word_counts)

# Output in readable format
print("Word Frequencies (Top 20):")
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
    print(f"{word}: {count}")

print("\nWord Length Distribution:")
for length, count in sorted(length_counts.items()):
    print(f"length_{length}: {count}")

print("\nStatistics:")
print(f"Total words: {total_words}")
print(f"Unique words: {unique_words}")
