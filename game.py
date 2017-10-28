#!/usr/bin/env python3

import pygame
from pygame.locals import *

# colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# Start game
pygame.init()
pygame.joystick.init()

def printJoystickInfo(joystickCount):
    # For each joystick:
    for i in range(joystickCount):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        print("Joystick {}".format(i))

        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        print("Joystick name {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        print("Number of axes: {}".format(axes))

        buttons = joystick.get_numbuttons()
        print("Number of buttons: {}".format(buttons))

        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        print("Number of hats: {}".format(hats))

# List out joysticks and their capabilities
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print("Joystick count: " + str(pygame.joystick.get_count()))
printJoystickInfo(pygame.joystick.get_count())

# Screen settings
screenWidth = 1024
screenHeight = 768
screenTitle = "Tank Game"

# Show screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(screenTitle)
screen.fill(WHITE)

def eventHandler():
    for event in pygame.event.get():
        #print(event)
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP or event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBALLMOTION or event.type == pygame.JOYHATMOTION:
            print(">>>>>>>> Joystick event")
            print(str(event.type))
        if event.type == QUIT:
            pygame.quit()
            quit()

while True:
    eventHandler()
    pygame.display.update()

pygame.quit()