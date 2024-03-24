"""
Adrian Ortiz
Class: CS 521 - Spring 1
Date: 02-10-2024
Homework Problem # 4_1
This script creates a list of integers from 55 to 5
(in steps of 10) and then generates a new list where each element is the
sum of its nearest neighbors and itself from the original list. Both lists
are printed with descriptions.
"""

# Creating a constant list with integers from 55 to 5, every 10th number
INPUT_LIST = list(range(55, 4, -10))

# Generating a new list with sums of nearest neighbors
result_list = [INPUT_LIST[i-1] + INPUT_LIST[i] + INPUT_LIST[i+1]
if 0 < i < len(INPUT_LIST)-1
else INPUT_LIST[i] + INPUT_LIST[i+(1 if i == 0 else -1)] for i in range(len
    (INPUT_LIST))]

# Printing both lists
print(f"Input List: {INPUT_LIST}")
print(f"Result List: {result_list}")
