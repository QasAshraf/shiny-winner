import pygame
import math

# colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = ( 48, 142, 38)
GREY = (210, 210 ,210)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
ORANGE    = ( 255,165,0)
BLUE    = ( 30,144,255)

class Tank(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, colour, boardWidth, boardHeight, assignedJoystick):
        self.width = 64
        self.height = 78
        self.movementMultiplier = 3
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.joystick = assignedJoystick
        self.rotation = 0

        # Super random colour assignment
        if colour == GREEN:
            image = pygame.image.load('Assets/p1-tank.png').convert_alpha()
        elif colour == ORANGE:
            image = pygame.image.load('Assets/p2-tank.png').convert_alpha()
        elif colour == BLUE:
            image = pygame.image.load('Assets/p3-tank.png').convert_alpha()
        elif colour == RED:
            image = pygame.image.load('Assets/p4-tank.png').convert_alpha()

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, colour, [0, 0, self.width, self.height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()
        self.image = image

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # "randomise" location of tanks
        if colour == GREEN:          # Bottom left
            self.rect.x = 0
            self.rect.y = 0
        elif colour == ORANGE:        # Top right
            self.rect.x = boardWidth - self.width
            self.rect.y = boardHeight - self.height
        elif colour == BLUE:          # Bottom right
            self.rect.x = boardWidth - self.width
            self.rect.y = 0
        elif colour == RED:           # Top left
            self.rect.x = 0
            self.rect.y = boardHeight - self.height


    def padHandler(self, pad_up, pad_right, pad_down, pad_left):
        self.move(pad_up * self.movementMultiplier, pad_down * self.movementMultiplier, pad_left * self.movementMultiplier,
                  pad_right * self.movementMultiplier)

    def joystickHandler(self, x, y):
        if x > 0:  # Move right
            self.moveRight(abs(x) * self.movementMultiplier)
        elif x < 0:  # Move left
            self.moveLeft(abs(x) * self.movementMultiplier)

        if y > 0:  # Move down
            self.moveDown(abs(y) * self.movementMultiplier)
        elif y < 0:  # Move uop
            self.moveUp(abs(y) * self.movementMultiplier)

    def move(self, pixelsUp, pixelsDown, pixelsLeft, pixelsRight):
        self.moveUp(pixelsUp)
        self.moveRight(pixelsRight)
        self.moveLeft(pixelsLeft)
        self.moveDown(pixelsDown)

    def moveRight(self, pixels):
        print(self.rotation)
        self.rotation += pixels
        if self.rotation > 360: self.rotation = 0
        self.image = pygame.transform.rotate(self.image, self.rotation)
        self.rect = self.image.get_rect(center=self.rect.center)

    def moveLeft(self, pixels):
        self.rotation -= pixels
        if self.rotation < 0: self.rotation = 360
        self.image = pygame.transform.rotate(self.image, self.rotation)
        self.rect = self.image.get_rect(center=self.rect.center)

    def moveUp(self, pixels):
        print(self.rotation)
        # if pixels > 0:
        #     self.rect.y = pixels * math.sin(self.rotation)
        #     self.rect.x = math.sqrt(math.pow(pixels, 2) / math.pow(self.rect.y, 2))
        #     if self.rotation > 180:
        #         self.rect.y = self.rect.y * -1
        #         self.rect.x = self.rect.x * -1
        #     self.checkBoardBoundries()

    def moveDown(self, pixels):
        print(self.rotation)
        # self.rect.y += pixels

    def checkBoardBoundries(self):
        if self.rect.y < 0: self.rect.y = 0
        if self.rect.x > self.boardWidth - self.width: self.rect.x = self.boardWidth - self.width
        if self.rect.y > self.boardHeight - self.height: self.rect.y = self.boardHeight - self.height
        if self.rect.x < 0: self.rect.x = 0

    def rot_center(image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image