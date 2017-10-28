import pygame
import xbox360_controller

class Joysticks:
    def __init__(self):
        # List out joysticks and their details
        self.numberOfJoysticks = pygame.joystick.get_count()
        joysticks = [pygame.joystick.Joystick(x) for x in range(self.numberOfJoysticks)]
        print("Joystick count: " + str(self.numberOfJoysticks))
        self.printJoystickInfo()

        # Create a controller object per controller
        # TOOD: Support multiple controllers
        if self.numberOfJoysticks > 0:
            self.controller = xbox360_controller.Controller(0)

    def hasJoysticks(self):
        return self.numberOfJoysticks > 0
    def printJoystickInfo(self):
        # For each joystick:
        for i in range(self.numberOfJoysticks):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            print("\tJoystick {}".format(i))

            # Get the name from the OS for the controller/joystick
            name = joystick.get_name()
            print("\tJoystick name {}".format(name))

            # Usually axis run in pairs, up/down for one, and left/right for
            # the other.
            axes = joystick.get_numaxes()
            print("\t\tNumber of axes: {}".format(axes))

            buttons = joystick.get_numbuttons()
            print("\t\tNumber of buttons: {}".format(buttons))

            # Hat switch. All or nothing for direction, not like joysticks.
            # Value comes back in an array.
            hats = joystick.get_numhats()
            print("\t\tNumber of hats: {}".format(hats))

    # Do stuff when buttons are pressed
    def buttonAPress(self, controllerId):
        print("Controller {} pressed A".format(controllerId))

    def buttonBPress(self, controllerId):
        print("Controller {} pressed B".format(controllerId))

    def buttonXPress(self, controllerId):
        print("Controller {} pressed X".format(controllerId))

    def buttonYPress(self, controllerId):
        print("Controller {} pressed Y".format(controllerId))

    def buttonHandler(self, event):
        controllerId = self.controller.get_id()
        # Handle events for first controller
        if event.type == pygame.JOYBUTTONDOWN:
            if event.joy == controllerId:
                if event.button == xbox360_controller.A:
                    self.buttonAPress(controllerId)
                elif event.button == xbox360_controller.B:
                    self.buttonBPress(controllerId)
                elif event.button == xbox360_controller.X:
                    self.buttonXPress(controllerId)
                elif event.button == xbox360_controller.Y:
                    self.buttonYPress(controllerId)

    def padHandler(self, callback):
        pad_up, pad_right, pad_down, pad_left = self.controller.get_pad()
        padPressed = pad_up + pad_right + pad_left + pad_down
        if padPressed > 0:
            print("Controller: {} --> Up: {}, Down: {}, Left: {}, Right: {}".format(self.controller.get_id(), pad_up,
                                                                                    pad_down,
                                                                                    pad_left, pad_right))
            callback(pad_up, pad_right, pad_down, pad_left)

    def leftStickHandler(self, callback):
        leftStickX, leftStickY = self.controller.get_left_stick()

        if leftStickY != 0 or leftStickX != 0:
            print("Controller: {} ---> Left Stick: ({}, {})".format(self.controller.get_id(), round(leftStickX, 2), round(leftStickY, 2)))
            callback(leftStickX, leftStickY)
