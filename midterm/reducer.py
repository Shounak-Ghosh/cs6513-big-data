#!/usr/bin/env python3
import sys
from collections import defaultdict

word_counts = defaultdict(int)
length_counts = defaultdict(int)
total_words = 0

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    
    if key == "WORD":
        word_counts[value] += 1
        total_words += 1
    elif key == "LENGTH":
        length_counts[int(value)] += 1

# Compute statistics
unique_words = len(word_counts)

# Print results
print("Word Frequencies (Top 20):")
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
    print(f"{word}: {count}")

print("\nWord Length Distribution:")
for length, count in sorted(length_counts.items()):
    print(f"length_{length}: {count}")

print("\nStatistics:")
print(f"Total words: {total_words}")
print(f"Unique words: {unique_words}")
