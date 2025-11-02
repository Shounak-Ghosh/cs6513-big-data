#!/usr/bin/env python3
import sys
import re
import string

# Define stop words to exclude
STOP_WORDS = {"the", "a", "an", "is", "are"}

def clean_word(word):
    """Normalize and clean each word by removing punctuation and lowering case."""
    word = word.lower()
    word = re.sub(r'[{}]'.format(string.punctuation), '', word)
    return word

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        cleaned = clean_word(word)
        if cleaned and cleaned not in STOP_WORDS:
            print(f"WORD\t{cleaned}")                # word frequency
            print(f"LENGTH\t{len(cleaned)}")         # word length distribution
