#!/usr/bin/env python3

import pygame
from pygame.locals import *
from tank import Tank
from joystick import Joystick
from map import Map

# colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = ( 48, 142, 38)
GREY = (210, 210 ,210)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
ORANGE    = ( 255,165,0)
BLUE    = ( 30,144,255)

# Start game
pygame.init()
pygame.joystick.init()

# List out joysticks and their details
numberOfJoysticks = pygame.joystick.get_count()
joysticks = [pygame.joystick.Joystick(x) for x in range(numberOfJoysticks)]
print("Joystick count: " + str(numberOfJoysticks))

# Screen settings
screenWidth = 1024
screenHeight = 768
screenTitle = "Tank Game"

# Print all events
printAllEvents = False

# Show screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(screenTitle)

gameMap = Map(screenWidth, screenHeight)
allSpritesList = pygame.sprite.Group()

# Need a controller to play
if numberOfJoysticks == 0:
    print("No joysticks connected")
    exit()

tankColours = [ GREEN,     # p1-tank.png
                ORANGE,    # p2-tank.png
                BLUE,      # p3-tank.png
                RED]       # p4-tank.png

def createTank(controllerId):
    joystick = Joystick(controllerId)
    playerTank = Tank(tankColours[controllerId], screenWidth, screenHeight, joystick)
    return playerTank

tankCollection = list(map(lambda controller: createTank(controller.get_id()), joysticks))
print(tankCollection)
allSpritesList.add(tankCollection)

obstacles = gameMap.createObstacles()
allSpritesList.add(obstacles)

print(allSpritesList.sprites())

def eventHandler():
    for event in pygame.event.get():
        for players in tankCollection:
            players.joystick.buttonHandler(event)

        # Handle quit of game or any other events
        if event.type == QUIT:
            pygame.quit()
            quit()
        else:
            if event.type != pygame.MOUSEMOTION and event.type != pygame.ACTIVEEVENT:
                if printAllEvents:
                    print(event) # Debugging purposes

def joyHandler():
    for players in tankCollection:
        players.joystick.padHandler(players.padHandler)
        players.joystick.leftStickHandler(players.joystickHandler)

while True:
    eventHandler()
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