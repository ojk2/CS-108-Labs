"""CS 108 - Lab 8

This module runs a command-line interface that controls successive image
processing commands. The image is redisplayed after each command.

@author: OWEN KOH (ojk2)
@date: Fall, 2022

Note: The majority of this code has already been done by Prof. Vander Linden
and Prof. Kenneth Arnold.
"""

from image_processing import *


MENU = 'b - Brighten' \
       '\nd - Dim' \
       '\nfh - Flip Horizontal' \
       '\nfv - Flip Vertical' \
       '\nn - Negative' \
       '\ng - Grayscale' \
       '\nq - Quit'

image = load_image('sydney_sunset.png')

# Run a CLI loop, allowing the user to repeat commands by hitting enter.
previous_command = ''
while True:
    print('Close the image window to proceed.')
    display_image(image)
    print(MENU)
    command = input('Command: ').lower()

    if command == '':
        command = previous_command
    if command == 'b':
        image = change_brightness(image, +50)
    elif command == 'd':
        image = change_brightness(image, -50)
    elif command == 'fh':
        image = flip_horizontal(image)
    elif command == 'fv':
        image = flip_vertical(image)
    elif command == 'n':
        image = negative(image)
    elif command == 'g':
        image = gray_scale(image)
    elif command == 'q':
        break
    else:
        print('invalid command')

    previous_command = command

