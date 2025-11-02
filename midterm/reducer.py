#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
current_length = None
length_count = 0

word_mode = False
length_mode = False

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)

    if key == "WORD":
        word_mode = True
        length_mode = False
        word = value

        if current_word == word:
            current_count += 1
        else:
            if current_word:
                print(f"WORD\t{current_word}\t{current_count}")
            current_word = word
            current_count = 1

    elif key == "LENGTH":
        word_mode = False
        length_mode = True
        length = value

        if current_length == length:
            length_count += 1
        else:
            if current_length:
                print(f"LENGTH\t{current_length}\t{length_count}")
            current_length = length
            length_count = 1

# Emit last keys
if current_word:
    print(f"WORD\t{current_word}\t{current_count}")
if current_length:
    print(f"LENGTH\t{current_length}\t{length_count}")
