"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-10-2024
Homework Problem # 4_3
This script merges two constant lists of first and last names into a
dictionary, ensuring the last names list is at least as long as
the first names list.
"""
import sys

# Merging Lists into Dictionary

# Creating constant lists of first and last names
FIRST_NAMES = ['Adrian', 'Ed', 'Troy']
LAST_NAMES = ['Ortiz', 'Orsini', 'Aikman', 'Smith']

# Validating list sizes
if len(LAST_NAMES) < len(FIRST_NAMES):
    print("Error: There are fewer last names than first names.")
    sys.exit(1)

# Merging lists into a dictionary
name_dict = dict(zip(LAST_NAMES, FIRST_NAMES + [None] *
                                 (len(LAST_NAMES) - len(FIRST_NAMES))))

# Printing the lists and the dictionary
print(f"First Names: {FIRST_NAMES}")
print(f"Last Names: {LAST_NAMES}")
print(f"Name Dictionary: {name_dict}")
