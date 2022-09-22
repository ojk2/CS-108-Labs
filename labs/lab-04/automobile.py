"""CS 108 - Lab 4.0

This program will attempt to take an input
and use branches to return the appropiate
outputs.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

# take the input as string
s = input("service: ")

# all conditions are in string form

# branches to test if input is equal to the set services
if s == 'oil change':
    x = 35
    print(f"cost of {s}: ${x}")
elif s == 'tire rotation':
    x = 19
    print(f"cost of {s}: ${x}")
elif s == 'car wash':
    x = 7
    print(f"cost of {s}: ${x}")
# if input failed all tests, then error
else:
    print(f"error: {s} is not recognized")

'''
i originally wanted to have a single variable and a single
print statement to print the variable at the end for the end result
but it led to bugs.
'''
