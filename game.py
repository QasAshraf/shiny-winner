#!/usr/bin/env python3

import pygame
from pygame.locals import *

import xbox360_controller

# colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = ( 48, 142, 38)

# Start game
pygame.init()
pygame.joystick.init()

def printJoystickInfo(joystickCount):
    # For each joystick:
    for i in range(joystickCount):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        print("\tJoystick {}".format(i))

        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        print("\tJoystick name {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        print("\t\tNumber of axes: {}".format(axes))

        buttons = joystick.get_numbuttons()
        print("\t\tNumber of buttons: {}".format(buttons))

        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        print("\t\tNumber of hats: {}".format(hats))

# List out joysticks and their details
numberOfJoysticks = pygame.joystick.get_count()
joysticks = [pygame.joystick.Joystick(x) for x in range(numberOfJoysticks)]
print("Joystick count: " + str(numberOfJoysticks))
printJoystickInfo(numberOfJoysticks)

# Create a controller object per controller
# TOOD: Support multiple controllers
if numberOfJoysticks > 0:
    controller = xbox360_controller.Controller(0)

# Screen settings
screenWidth = 1024
screenHeight = 768
screenTitle = "Tank Game"

# Show screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(screenTitle)
screen.fill(GREEN)

def eventHandler():
    for event in pygame.event.get():
        # Handle events for first controller
        controllerId = controller.get_id()
        if event.type == pygame.JOYBUTTONDOWN:
            if event.joy== controllerId:
                if event.button == xbox360_controller.A:
                    print("Controller {} pressed A".format(controllerId))
                elif event.button == xbox360_controller.B:
                    print("Controller {} pressed B".format(controllerId))

        # Handle quit of game or any other events
        if event.type == QUIT:
            pygame.quit()
            quit()
        else:
            if event.type != pygame.MOUSEMOTION and event.type != pygame.ACTIVEEVENT:
                print(event) # Debugging purposes

while True:
    eventHandler()
    pygame.display.update()

pygame.quit()