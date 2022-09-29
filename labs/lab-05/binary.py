"""CS 108 - Lab 5.1

This program will implement an algorithm that will
print positive integers as binary reversed.

@author: OWEN KOH (ojk2)
@date: Fall, 2022 
"""

# Put your solution code here, replacing this line.

postint = abs(int(input("integer: ")))

while postint > 0:
    print(postint % 2, end='')
    postint //= 2
print()
