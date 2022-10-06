"""CS 108 - Lab 6.0

This program will implement several functions:
    a) returns cost to drive given miles and miles/gallon
    b) returns the number of spaces in a string

@author: OWEN KOH (ojk2)
@author: YEWON YEON (yj228)
@date: Fall, 2022 
"""

# Put your solution code here, replacing this line.

def compute_cost(miles, miles_per_gallon, dollars_per_gallon):
    total = (miles / miles_per_gallon) * dollars_per_gallon
    return total

def count_spaces(s):
    count = 0
    for c in s:
        if c == ' ':
            count += 1
    return count
