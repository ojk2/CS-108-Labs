"""CS 108 - Lab 4.2

This program will attempt to implement Zeller's
algorithm to determine the day of the week given
inputs: year, month, and day using a formula.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

# load in the days of the week in a list
wk = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

'''get the inputs as integers because there is no such thing as
float day, month, or year.'''
y = int(input("Enter year: "))
m = int(input("Enter month: "))
q = int(input("Enter day: "))

'''change up the inputs for certain exceptions so that the
formula will work.'''
if m == 1:
    m = 13
    y -= 1
elif m == 2:
    m = 14
    y -= 1

# set constants to simplify formula a bit
j = y // 100
k = y % 100

# formula to calculate day of week given day, month, year
h = (q + (((m + 1) * 26) // 10) + k + (k // 4) + (j // 4) + 5 * j) % 7

# the result has to be in ranges 1-7 -> 0-6 range index list
print(wk[h])
