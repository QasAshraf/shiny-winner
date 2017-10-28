#!/usr/bin/env python3

import pygame
from pygame.locals import *
from tank import Tank
from joystick import Joysticks

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

# Screen settings
screenWidth = 1024
screenHeight = 768
screenTitle = "Tank Game"

# Print all events
printAllEvents = False

# Show screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(screenTitle)
joysticks = Joysticks()

allSpritesList = pygame.sprite.Group()

def createTank():
    playerTank = Tank(RED, screenWidth, screenHeight)
    playerTank.rect.x = 200
    playerTank.rect.y = 300
    return playerTank

tank = createTank()
allSpritesList.add(tank)

MOVEMENT_MULTIPLIER = 3

def joystickPadHandler(pad_up, pad_right, pad_down, pad_left):
    tank.move(pad_up * MOVEMENT_MULTIPLIER, pad_down * MOVEMENT_MULTIPLIER, pad_left * MOVEMENT_MULTIPLIER,
                  pad_right * MOVEMENT_MULTIPLIER)

def tankMovementHandler(x, y):
    if x > 0: # Move right
        tank.moveRight(abs(x) * MOVEMENT_MULTIPLIER)
    elif x < 0: # Move left
        tank.moveLeft(abs(x) * MOVEMENT_MULTIPLIER)

    if y > 0: # Move down
        tank.moveDown(abs(x) * MOVEMENT_MULTIPLIER)
    elif y < 0: # Move uop
        tank.moveUp(abs(x) * MOVEMENT_MULTIPLIER)

def eventHandler():
    for event in pygame.event.get():
        if joysticks.hasJoysticks():
            joysticks.buttonHandler(event)
            joysticks.padHandler(joystickPadHandler)
            joysticks.leftStickHandler(tankMovementHandler)

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