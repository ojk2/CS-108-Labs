"""CS 108 - Lab 7.0

This program will take a name as input and output it
in British English style.

@author: OWEN KOH (ojk2)
@date: Fall, 2022 
"""

# Put your solution code here, replacing this line.

fullname = input("Full Name: ")

namelist = fullname.split()
if len(namelist) > 3 or len(namelist) == 0:
    print(f"'{fullname}' is a non-standard name.")

elif len(namelist) == 3:
    firstInitial = f"{namelist[0][0]}."
    lastName = namelist[2]
    middle = namelist[1][0]
    britname = f"{lastName}, {firstInitial}{middle}."
elif len(namelist) == 2:
    firstInitial = f"{namelist[0][0]}."
    lastName = namelist[1]
    britname = f"{lastName}, {firstInitial}"


print(britname)

