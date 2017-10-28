#!/usr/bin/env python3

import pygame
from pygame.locals import *
from tank import Tank

import xbox360_controller

# colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = ( 48, 142, 38)
GREY = (210, 210 ,210)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

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

# Print all events
printAllEvents = False

# Show screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(screenTitle)

allSpritesList = pygame.sprite.Group()

def createTank():
    playerTank = Tank(RED, 20, 30)
    playerTank.rect.x = 200
    playerTank.rect.y = 300
    return playerTank

tank = createTank()
allSpritesList.add(tank)


# Do stuff when buttons are pressed
def buttonAPress(controllerId):
    print("Controller {} pressed A".format(controllerId))

def buttonBPress(controllerId):
    print("Controller {} pressed B".format(controllerId))

def buttonXPress(controllerId):
    print("Controller {} pressed X".format(controllerId))

def buttonYPress(controllerId):
    print("Controller {} pressed Y".format(controllerId))

def buttonYPress(controllerId):
    print("Controller {} pressed Y".format(controllerId))

def joystickButtonHandler(controllerId, event):
    # Handle events for first controller
    if event.type == pygame.JOYBUTTONDOWN:
        if event.joy == controllerId:
            if event.button == xbox360_controller.A:
                buttonAPress(controllerId)
            elif event.button == xbox360_controller.B:
                buttonBPress(controllerId)
            elif event.button == xbox360_controller.X:
                buttonXPress(controllerId)
            elif event.button == xbox360_controller.Y:
                buttonYPress(controllerId)

def joystickPadHandler(xboxController):
    pad_up, pad_right, pad_down, pad_left = xboxController.get_pad()
    padPressed = pad_up + pad_right + pad_left + pad_down
    if padPressed > 0:
        print("Up: {}, Down: {}, Left: {}, Right: {}".format(pad_up, pad_down, pad_left, pad_right))

def eventHandler():
    for event in pygame.event.get():
        if numberOfJoysticks > 0:
            controllerId = controller.get_id()
            joystickButtonHandler(controllerId, event)
            # TODO: Handle pad for multiple joysticks
            joystickPadHandler(controller)

        # Handle quit of game or any other events
        if event.type == QUIT:
            pygame.quit()
            quit()
        else:
            if event.type != pygame.MOUSEMOTION and event.type != pygame.ACTIVEEVENT:
                if printAllEvents:
                    print(event) # Debugging purposes

def keyHandler():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tank.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        tank.moveRight(5)

while True:
    eventHandler()
    keyHandler()

    # Game logic
    allSpritesList.update()

    screen.fill(GREEN)
    # Draw the sprites
    allSpritesList.draw(screen)

    # Refresh the screen
    pygame.display.update()

pygame.quit()
quit()