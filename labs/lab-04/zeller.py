"""CS 108 - Lab 4.2

This program will attempt to implement Zeller's
algorithm to determine the day of the week given
inputs: year, month, and day using a formula.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

wk = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

y = int(input("Enter year: "))
m = int(input("Enter month: "))
d = int(input("Enter day: "))

if m == 1:
    m = 13
    y -= 1
elif m == 2:
    m = 14
    y -= 1

j = y // 100
k = y % 100

h = (m + (((d + 1) * 26) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7
print(wk[h])
