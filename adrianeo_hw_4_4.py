"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-10-2024
Homework Problem # 4_4
This script performs various tasks with a predefined dictionary,
including sorting and printing key-value pairs in different formats.
"""

# Predefined dictionary
MY_DICT = {'a': 14, 'c': 18, 'b': 21}

# a. Printing all keys as a list
print(f"Keys: {list(MY_DICT.keys())}")

# b. Printing all values as comma-separated data
print("Values:", ', '.join(str(value) for value in MY_DICT.values()))

# c. Printing key-value pairs
print("Key-value pairs:", ' '.join(f"{key}: {value}" for key, value in
    MY_DICT.items()))

# d. Sorting by key and printing tuples
print("Key-value pairs ordered by key:", sorted(MY_DICT.items()))

# e. Sorting by value and printing
sorted_by_value = sorted(MY_DICT.items(), key=lambda x: x[1])
print("Key-value pairs ordered by value:", ' '.join(f"{key}: {value}"
    for key, value in sorted_by_value))
