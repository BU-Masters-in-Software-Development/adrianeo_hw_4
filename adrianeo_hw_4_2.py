"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-10-2024
Homework Problem # 4_2
This script assigns a sentence to a string constant, counts the frequency
of each letter (ignoring case), and identifies the most frequent letter(s).
The results are printed in a formatted manner.
"""

# Example sentences
sentences = ["WAS IT A RAT I SAW?", "Wwwas it a rat I saw?"]

for SENTENCE in sentences:
# Counting the frequency of each letter, ignoring case and non-alpha chars
    from collections import Counter
    filtered_sentence = ''.join(filter(str.isalpha, SENTENCE))
    letter_counts = Counter(filtered_sentence.upper())

    # Finding the most frequent letter(s)
    max_count = max(letter_counts.values())
    most_frequent = [char for char, count in letter_counts.items()
        if count == max_count]

    # Sorting the most frequent letters
    most_frequent.sort()

    # Printing results
    print(f"The string being analyzed is: \"{SENTENCE}\"")
    print("1. Dictionary of letter counts:",
        dict(sorted(letter_counts.items())))
    if len(most_frequent) == 1:
        print(f"2. Most frequent letter \"{most_frequent[0]}\""
              f" appears {max_count} times.")
    else:
        print(f"2. Most frequent letters "
              f"{most_frequent} appear {max_count} times.")
