import pygame
from pygame.locals import *

started = pygame.init()
print(started)

displayWidth = 1024
displayHeight = 768
displayTitle = "Tank Game"

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption(displayTitle)

def eventHandler():
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            quit()

while True:
    eventHandler()
    pygame.display.update()

