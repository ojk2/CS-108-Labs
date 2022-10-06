"""CS 108 - Lab 5.2

This program will attempt to draw a spirograph using
the guizero library by taking inputs and calculating
the appropiate values with given equations.

@author: OWEN KOH (ojk2)
@date: Fall, 2022
"""

from guizero import App, Drawing
import math

app = App('Spirograph')
drawing = Drawing(app, width='fill', height='fill')

center = app.width / 2

moving_radius = float(input("moving radius: "))
fixed_radius = float(input("fixed radius: "))
pen_offset = float(input("pen offset: "))
color = input("color: ")


app.display()
