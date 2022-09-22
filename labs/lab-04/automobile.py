"""CS 108 - Lab 4.0

This program will attempt to take an input
and use branches to return the appropiate
outputs.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

# Put your solution code here, replacing this line.
s = input("service: ")

if s == 'oil change':
    x = 35
elif s == 'tire rotation':
    x = 19
elif s == 'car wash':
    x = 7
else:
    print(f"error: {s} is not recognized")

print(f"cost of {s}: ${x}")
