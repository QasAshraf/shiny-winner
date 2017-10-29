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

MOVED_UP = 0
MOVED_DOWN = 1
MOVED_LEFT = 2
MOVED_RIGHT = 3

class Tank(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, colour, boardWidth, boardHeight, assignedJoystick, obstacles):
        self.width = 64
        self.height = 78
        self.movementMultiplier = 3
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.joystick = assignedJoystick
        self.listOfObstacles = obstacles
        self.lastMovement = -1 # 0 = Up, 1 = Down, 2 = Left, 3 = Right
        self.rotation = 0

        # Super random colour assignment
        if colour == GREEN:
            image = pygame.image.load('Assets/p1-tank.png').convert_alpha()
            self.filename = 'Assets/p1-tank.png'
        elif colour == ORANGE:
            image = pygame.image.load('Assets/p2-tank.png').convert_alpha()
            self.filename = 'Assets/p2-tank.png'
        elif colour == BLUE:
            image = pygame.image.load('Assets/p3-tank.png').convert_alpha()
            self.filename = 'Assets/p3-tank.png'
        elif colour == RED:
            image = pygame.image.load('Assets/p4-tank.png').convert_alpha()
            self.filename = 'Assets/p4-tank.png'

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

    def hasCollidedWithObstacle(self):
        collided = pygame.sprite.spritecollide(self, self.listOfObstacles, False)
        if collided:
            #print("Collision detected! Controller {} and last movement was {}".format(self.joystick.controllerId, self.lastMovement))
            return True
        else:
            return False

    def padHandler(self, pad_up, pad_right, pad_down, pad_left):
        self.move(pad_up * self.movementMultiplier, pad_down * self.movementMultiplier, pad_left,
                  pad_right)

    def joystickHandler(self, x, y):
        if x > 0:  # Move right
            self.moveRight(abs(x))
        elif x < 0:  # Move left
            self.moveLeft(abs(x))

        if y > 0:  # Move down
            self.moveDown(abs(y) * self.movementMultiplier)
        elif y < 0:  # Move up
            self.moveUp(abs(y) * self.movementMultiplier)

    def move(self, pixelsUp, pixelsDown, pixelsLeft, pixelsRight):
        self.moveUp(pixelsUp)
        self.moveRight(pixelsRight)
        self.moveLeft(pixelsLeft)
        self.moveDown(pixelsDown)

    def moveRight(self, pixels):
        if self.hasCollidedWithObstacle() and self.lastMovement == MOVED_RIGHT:
            print("Can't move right more")
        else:
            self.lastMovement = MOVED_RIGHT

            oldCenter = self.rect.center
            self.rotation += pixels
            self.image = pygame.transform.rotate(pygame.image.load(self.filename).convert_alpha(), self.rotation)
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter

            self.checkBoardBoundries()


    def moveLeft(self, pixels):
        if self.hasCollidedWithObstacle() and self.lastMovement == MOVED_LEFT:
            print("Can't move left more")
        else:
            self.lastMovement = MOVED_LEFT
            oldCenter = self.rect.center
            self.rotation -= pixels
            self.image = pygame.transform.rotate(pygame.image.load(self.filename).convert_alpha(), self.rotation)
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter

            self.checkBoardBoundries()


    def moveUp(self, pixels):
        if self.hasCollidedWithObstacle() and self.lastMovement == MOVED_UP:
            print("Can't move up more")
        else:
            self.rect.y -= pixels
            self.lastMovement = MOVED_UP

            self.checkBoardBoundries()


    def moveDown(self, pixels):
        if self.hasCollidedWithObstacle() and self.lastMovement == MOVED_DOWN:
            print("Can't move down more")
        else:
            self.rect.y += pixels
            self.lastMovement = MOVED_DOWN

            self.checkBoardBoundries()


    def checkBoardBoundries(self):
        if self.rect.y < 0: self.rect.y = 0
        if self.rect.x > self.boardWidth - self.width: self.rect.x = self.boardWidth - self.width
        if self.rect.y > self.boardHeight - self.height: self.rect.y = self.boardHeight - self.height
        if self.rect.x < 0: self.rect.x = 0