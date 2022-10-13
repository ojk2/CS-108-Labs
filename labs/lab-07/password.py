"""CS 108 - Lab 7.2

This program will implement a function that
will determine whether a given password input is
valid or not based on some guidelines.

@author: OWEN KOH (ojk2)
@date: Fall, 2022 
"""

# Put your solution code here, replacing this line.


def count_digits(enter):
    digitcount = 0
    for i in enter:
        if i.isdigit():
            digitcount += 1
    return digitcount

def is_valid_password(enter):
    if len(enter) >= 8:
        if enter.isalnum() == True:
            if count_digits(enter) >= 2:
                return True
            else:
                return False
        else:
            return False
