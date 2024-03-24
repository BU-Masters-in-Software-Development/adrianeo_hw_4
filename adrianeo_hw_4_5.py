"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-10-2024
Homework Problem # 4_5
This script performs various tasks with a predefined dictionary,
including sorting and printing key-value pairs in different formats.
"""

# Creating a constant dictionary for character to word conversion
CHAR_TO_WORD = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
    '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero',
    '-': 'Negative', '.': 'Point'}

# Infinite loop for user input
while True:
    num_input = input ("Enter a number: ")
    
    # Validating input
    if (num_input.replace ('.', '', 1).replace
        ('-', '', 1).isdigit ()):
        break
    elif ',' in num_input:
        print ("Please try again without entering commas.")
    else:
        print (f"\"{num_input}\" is not a valid number. Please try again")

# Converting the number to words
num_in_words = ' '.join (CHAR_TO_WORD.get (char, '') for char in num_input)

# Printing the converted number
print (f"As Text: {num_in_words}")
