"""CS 108 - Lab 3.3

This program will attempt to draw a stickman
using the guizero library on a new window.

@author: OWEN KOH (2635799)
@date: Fall, 2022
"""

from guizero import App, Drawing

app = App(title = 'Stick Man')

drawing = Drawing(app, width='fill', height='fill')

unit = 50                # Change this value to rescale the drawing.

# draw head
drawing.oval(
    1 * unit, 2 * unit,  # bounding box x1, y1
    3 * unit, 4 * unit,  # bounding box x2, y2
    outline=True,
    color='white')

# draw torso
drawing.line(
    2 * unit, 4 * unit,  # x1, y1
    2 * unit, 7 * unit,  # x2, y2
    color='red')

# draw arms
drawing.line(
    1 * unit, 5 * unit, # x1, y1
    3 * unit, 5 * unit, # x2, y2
    color='black')

# draw legs
drawing.line(2 * unit, 7 * unit, 1 * unit, 9 * unit, color='black')
drawing.line(2 * unit, 7 * unit, 3 * unit, 9 * unit, color='black')

app.display()
