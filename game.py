#!/usr/bin/env python3

import pygame
from pygame.locals import *

# colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# Start game
started = pygame.init()

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
        print(event)
        if event.type == QUIT:
            pygame.quit()
            quit()

while True:
    eventHandler()
    pygame.display.update()

pygame.quit()