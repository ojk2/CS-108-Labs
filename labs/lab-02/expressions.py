"""CS 108 - Lab 2.0

This lab will execute several
mathematical expressions.

@author: OWEN KOH (2635799)
@author: YEWON JEON (10002120)
@date: Fall 2022
"""
# python follows the order of operations
3 + 4
# multiplication goes first, then addition -> 17
2 + 3 * 5
# left to right -> 2
8 - 4 - 2
# the addition goes first due to the (parenthesis) -> 20
(3 + 7) * 2
# modulus % returns the remainder of the division -> 1
13 % 4
# floor division returns float rounded to smallest digit -> 2.0
8.2 // 4
# two to the power of ten -> 1024
2 ** 10
# modulus returns the remainder of 5.1 / 2 -> 1.0999999999999996
5.1 % 2

x = int(input("Please enter an integer: "))
