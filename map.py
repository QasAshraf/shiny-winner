import random

import pygame
from obstacle import Obstacle

class Map:
    def __init__(self, screenWidth, screenHeight):
        self.width = screenWidth
        self.height = screenHeight
        self.numberOfObstacles = 5

    def createObstacles(self):
        self.obstacles = []
        for i in range(0, self.numberOfObstacles):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            print("Creating obstacle at: " + str(x) + ", " + str(y))
            self.obstacles.append(Obstacle(x, y))
        return self.obstacles