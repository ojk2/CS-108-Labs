"""CS 108 - Lab 7.3

For practice dealing with advanced string slicing
and manipulation, this program will attempt to
determine whether a string of digits is a valid
credit card number according to several implementation
of functions.

@author: OWEN KOH (ojk2)
@date:  Fall, 2022
"""
def is_valid_prefix(enter):
    if enter[0:2] != '37' and enter[0:1] not in ('4', '5', '6'):
        return False
    else:
        return True
    
def sum_of_odds(enter):
    sum = 0
    odds = []
    for i in enter[-1:0:-2]:
        add = int(i)
        odds.append(add)
    for o in range(0, len(odds)):
        sum = sum + odds[o]
    return sum
        
def sum_of_double_evens():
    pass

def is_valid_cc():
    pass

