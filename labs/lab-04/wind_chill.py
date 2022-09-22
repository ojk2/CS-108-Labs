"""CS 108 - Lab 4.1

This program will attempt to take two inputs,
temperature and wind speed to calculate
the wind chill using a formula and to determine
how many layers you should wear. 

Branches are
implemented to handle conditions and exceptions.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

# Put your solution code here, replacing this line.

# take the inputs even as integers
a = input("Temperature: ")
b = input("Wind speed: ")

# convert inputs to floats if they are integers
ta = float(a)
v = float(b)

# main formula
twc = 35.74 + 0.6215 * ta - 35.75 * (v ** 0.16) + 0.4275 * ta * (v ** 0.16)

# error message first priority if calculated value is invalid in the first place
if v < 2 or ta < -58 or ta > 41:
    print("Invalid input")
else:
    print(f"Wind chill: {twc}")
    
    # conditions
    if twc < -40:
        print("Stay home!")
    elif twc < -10:
        print("Four layers")
    elif twc < 20:
        print("Three layers")
    elif twc < 40:
        print("Two layers")
    elif twc >= 40:
        print("One layer")
