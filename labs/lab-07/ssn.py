"""CS 108 - Lab 7.1

This program will determine if a string is a
SSN with a function using string methods.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

# Put your solution code here, replacing this line.
def is_valid_ssn(enter):
    if enter.isdigit() == False:
        if enter[0:2].isdigit() == True:
            new = enter.replace('-', '')
            if len(new) == 9:
                return True
            else:
                return False
    else:
        if len(new) == 9:
            return True
        else:
            return False