"""CS 108 - Lab 5.0

This program will attempt to demonstrate loops and
ranges by printing output subsequent increments of
10 from the first input as long as it is <= to the
second input.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

x1 = int(input()); x2 = int(input())

if x1 > x2:
    print("Second integer can't be less than the first.")
else:
    # order of statements in the loop body matters, if not then
    # will present a bug even though it runs correctly.
    while x1 <= x2:
        print(x1)
        x1 += 10
    
