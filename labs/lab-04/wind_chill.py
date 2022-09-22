"""CS 108 - Lab 4.1

This program will attempt to take two inputs,
temperature and wind speed to calculate
the wind chill using a formula. Branches are
implemented to handle exceptions.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

# Put your solution code here, replacing this line.

a = input("Temperature: ")
b = input("Wind speed: ")

ta = float(a)
v = float(b)
twc = 35.74 + 0.6215 * ta - 35.75 * (v ** 0.16) + 0.4275 * ta * (v ** 0.16)

if v < 2 or ta < -58 or ta > 41:
    print("Invalid input")
else:
    print(f"Wind chill: {twc}")

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