import pygame
import xbox360_controller

class Joystick:
    def __init__(self, controllerId):
        self.controller = xbox360_controller.Controller(controllerId)
        self.controllerId = controllerId
        self.printJoystickInfo()

    def printJoystickInfo(self):
        joystick = pygame.joystick.Joystick(self.controllerId)
        joystick.init()

        print("\tJoystick {}".format(self.controllerId))

        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        print("\tJoystick name {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        print("\t\tNumber of axes: {}".format(axes))

        buttons = joystick.get_numbuttons()
        print("\t\tNumber of buttons: {}".format(buttons))

    # Do stuff when buttons are pressed
    def buttonAPress(self, controllerId):
        print("Controller {} pressed A".format(controllerId))

    def buttonBPress(self, controllerId):
        print("Controller {} pressed B".format(controllerId))

    def buttonXPress(self, controllerId):
        print("Controller {} pressed X".format(controllerId))

    def buttonYPress(self, controllerId):
        print("Controller {} pressed Y".format(controllerId))

    def buttonStartPress(self, controllerId):
        print("Controller {} pressed START".format(controllerId))

    def buttonBackPress(self, controllerId):
        print("Controller {} pressed BACK".format(controllerId))

    def buttonHandler(self, event):
        # Handle events for first controller
        if event.type == pygame.JOYBUTTONDOWN and event.joy == self.controllerId:
            if event.button == xbox360_controller.A:
                self.buttonAPress(self.controllerId)
            elif event.button == xbox360_controller.B:
                self.buttonBPress(self.controllerId)
            elif event.button == xbox360_controller.X:
                self.buttonXPress(self.controllerId)
            elif event.button == xbox360_controller.Y:
                self.buttonYPress(self.controllerId)
            elif event.button == xbox360_controller.START:
                self.buttonStartPress(self.controllerId)
            elif event.button == xbox360_controller.BACK:
                self.buttonBackPress(self.controllerId)

    def padHandler(self, callback):
        pad_up, pad_right, pad_down, pad_left = self.controller.get_pad()
        padPressed = pad_up + pad_right + pad_left + pad_down
        if padPressed > 0:
            #print("Controller: {} --> Up: {}, Down: {}, Left: {}, Right: {}".format(self.controller.get_id(), pad_up,
                                                                                    #pad_down,
                                                                                    #pad_left, pad_right))
            callback(pad_up, pad_right, pad_down, pad_left)

    def leftStickHandler(self, callback):
        leftStickX, leftStickY = self.controller.get_left_stick()

        if leftStickY != 0 or leftStickX != 0:
            #print("Controller: {} ---> Left Stick: ({}, {})".format(self.controller.get_id(), round(leftStickX, 2), round(leftStickY, 2)))
            callback(leftStickX, leftStickY)
