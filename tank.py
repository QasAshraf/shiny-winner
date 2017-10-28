import pygame
import spritesheet

WHITE = (255, 255, 255)


class Tank(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, boardWidth, boardHeight):
        self.width = 16
        self.height = 16
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        ss = spritesheet.spritesheet('tanks.png')
        # Sprite is 16x16 pixels at location 0,0 in the file...
        image = ss.image_at((0, 0, self.width, self.height))
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, self.width, self.height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()
        self.image = image

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def move(self, pixelsUp, pixelsDown, pixelsLeft, pixelsRight):
        self.moveUp(pixelsUp)
        self.moveRight(pixelsRight)
        self.moveLeft(pixelsLeft)
        self.moveDown(pixelsDown)

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > self.boardWidth - self.width: self.rect.x = self.boardWidth - self.width

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0: self.rect.x = 0

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0: self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > self.boardHeight - self.height: self.rect.y = self.boardHeight - self.height