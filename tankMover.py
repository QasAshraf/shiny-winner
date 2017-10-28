class TankMover:
    def __init__(self, tank):
        self.tank = tank
        self.MOVEMENT_MULTIPLIER = 3

    def padHandler(self, pad_up, pad_right, pad_down, pad_left):
        self.tank.move(pad_up * self.MOVEMENT_MULTIPLIER, pad_down * self.MOVEMENT_MULTIPLIER, pad_left * self.MOVEMENT_MULTIPLIER,
                  pad_right * self.MOVEMENT_MULTIPLIER)

    def joystickHandler(self, x, y):
        if x > 0:  # Move right
            self.tank.moveRight(abs(x) * self.MOVEMENT_MULTIPLIER)
        elif x < 0:  # Move left
            self.tank.moveLeft(abs(x) * self.MOVEMENT_MULTIPLIER)

        if y > 0:  # Move down
            self.tank.moveDown(abs(y) * self.MOVEMENT_MULTIPLIER)
        elif y < 0:  # Move uop
            self.tank.moveUp(abs(y) * self.MOVEMENT_MULTIPLIER)