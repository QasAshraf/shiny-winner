#!/usr/bin/env python3

import pygame
from pygame.locals import *
from tank import Tank
from joystick import Joysticks
from tankMover import TankMover
from map import Map

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

map = Map(screenWidth, screenHeight)
allSpritesList = pygame.sprite.Group()

def createTank():
    playerTank = Tank(RED, screenWidth, screenHeight)
    playerTank.rect.x = 200
    playerTank.rect.y = 300
    return playerTank

tank = createTank()
tankMover = TankMover(tank)
allSpritesList.add(tank)

obstacles = map.createObstacles()
allSpritesList.add(obstacles)

print(allSpritesList.sprites())

def eventHandler():
    for event in pygame.event.get():
        if joysticks.hasJoysticks():
            joysticks.buttonHandler(event)

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
        tankMover.padHandler(0, 0, 0, 1)
    if keys[pygame.K_RIGHT]:
        tankMover.padHandler(0, 1, 0, 0)
    if keys[pygame.K_UP]:
        tankMover.padHandler(1, 0, 0, 0)
    if keys[pygame.K_DOWN]:
        tankMover.padHandler(0, 0, 1, 0)

def joyHandler():
    joysticks.padHandler(tankMover.padHandler)
    joysticks.leftStickHandler(tankMover.joystickHandler)

while True:
    eventHandler()
    keyHandler()
    if joysticks.hasJoysticks():
        joyHandler()

    # Game logic
    allSpritesList.update()

    screen.fill(GREEN)
    # Draw the sprites
    allSpritesList.draw(screen)

    # Refresh the screen
    pygame.display.update()

pygame.quit()
quit()