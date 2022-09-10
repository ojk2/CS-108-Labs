"""CS 108 - Lab 2.2

Draw stick figure by using turtle.

@author: OWEN KOH (2635799)
@author: Yewon Jeon (10002120)
@date: Fall, 2022
"""

import turtle

# Start the turtle window in the corner of the screen (helpful for dual monitor).
# turtle.setup(width=800, height=600, startx=100, starty=100)
turtle.setup(width = 800, height = 600, startx = 100, starty = 100)
window = turtle.Screen()
pen = turtle.Turtle()

# Put your solution code here, replacing this line and the sample code.
# Draw a line segment.
UNIT = 50
pen.circle(UNIT)
pen.right(90)
pen.forward(UNIT)
pen.left(90); pen.forward(UNIT)
pen.right(180); pen.forward(UNIT * 2)
pen.right(180); pen.forward(UNIT)
pen.right(90); pen.forward(UNIT)
# 70.71 because a^2+b^2=c^2 since a, b=50, c= 70.71
# by using the pythagorean theorem, we can find that the angle is 45 degrees
pen.right(45); pen.forward(70.71)
pen.left(180); pen.forward(70.71)
pen.right(90); pen.forward(70.71)

# window.mainloop() # Needed for some IDEs.
