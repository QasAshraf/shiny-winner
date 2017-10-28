import random

import pygame
from obstacle import Obstacle

SIZE_OF_TANK = 78
NUMBER_OF_OBSTACLES = 5

class Map:


    def __init__(self, screenWidth, screenHeight):
        self.width = screenWidth - SIZE_OF_TANK
        self.height = screenHeight - SIZE_OF_TANK

    def createObstacles(self):
        self.obstacles = []
        for i in range(0, NUMBER_OF_OBSTACLES):
            x = random.randint(SIZE_OF_TANK, self.width)
            y = random.randint(SIZE_OF_TANK, self.height)
            print("Creating obstacle at: " + str(x) + ", " + str(y))
            self.obstacles.append(Obstacle(x, y))
        return self.obstacles