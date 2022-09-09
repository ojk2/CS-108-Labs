"""CS 108 - Lab 1.2

Describe the module here. Fix the lab number above and the name/date below.
Delete the second @author line if working solo.

@author: OWEN KOH (2635799)
@author: YEWON JEON (10002021)
@date: Fall, 2022
"""

import turtle

# Start the turtle window in the corner of the screen (helpful for dual monitor).
turtle.setup(width=800, height=600, startx=100, starty=100)

window = turtle.Screen()
pen = turtle.Turtle()

# Put your solution code here, replacing this line and the sample code.
# Draw a line segment.

for i in range(0,2):
    pen.forward(250); pen.right(30)
    i += 1
    

# window.mainloop() # Needed for some IDEs.
