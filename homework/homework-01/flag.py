"""CS 108 - Homework 1 (Turtle Flag)

This program will attempt to draw the flag
of France, first with a rectangle, then
filling in the three sections with their
appropiate color as they're being drawn.

@author: OWEN KOH (2635799)
@date: Fall, 2022
"""

import turtle

t = turtle.Turtle()

# draw the rectangle first (3-wide by 2-high)
t.forward(300); t.left(90)
t.forward(200); t.left(90)
t.forward(300); t.left(90)
t.forward(200); t.left(90)

# draw the 1st blue sector
t.begin_fill(); t.pencolor("blue"); t.fillcolor("blue")
t.forward(100); t.left(90)
t.forward(200); t.left(90)
t.forward(100); t.left(90)
t.forward(200); t.left(90)
t.end_fill()

# draw the 2nd white sector
t.pencolor("black"); t.forward(200)

# draw the 3rd red sector
t.begin_fill(); t.pencolor("red"); t.fillcolor("red")
t.forward(100); t.left(90)
t.forward(200); t.left(90)
t.forward(100); t.left(90)
t.forward(200); t.end_fill()
