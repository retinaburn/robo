import robo
import pygame
from pygame.locals import *
import os
import time

#Set up local display so we run run pygame from ssh
os.environ["DISPLAY"] = ":0"
os.putenv('SDL_VIDEODRIVER', 'fbcon')

pygame.init()
pygame.display.init()
pygame.joystick.init()

myrobo = robo.Robo(21)


# Grab the first joystick if we have at least one defined
print("Found {} joysticks".format(pygame.joystick.get_count()))

joy = pygame.joystick.Joystick(0)
joy.init()

# Xbox Controller Definitions
MENU_BUTTON = 7
B_BUTTON = 1
A_BUTTON = 0
DPAD = JOYHATMOTION


# Input Loop Definitions
IS_RUNNING = True
DPAD_DOWN = False
CODE = 0x00  #The last code sent to RS
NEXT_CODE = 0x00 #The next code sent to RS
FORWARD = robo.CODE_RSWalkForward
BACKWARD = robo.CODE_RSWalkBackward
TURN_LEFT = robo.CODE_RSTurnLeft
TURN_RIGHT = robo.CODE_RSTurnRight
NO_OP = robo.CODE_RSNoOp
BURP = robo.CODE_RSBurp
ROAR = robo.CODE_RSRoar


while(IS_RUNNING):
    for event in pygame.event.get():

        try:
            print("Event Type: {}, Event Button: {}, Event: {}".format(event.type,event.button,event))
        except AttributeError:
            print("Event Type: {}, Event Value: {}, Event: {}".format(event.type,event.value,event))

        if event.type == JOYBUTTONUP and event.button == MENU_BUTTON:
            print("Quitting...")
            IS_RUNNING = False
        if event.type == JOYBUTTONUP and event.button == B_BUTTON:
            myrobo.send_code(BURP)
        if event.type == JOYBUTTONUP and event.button == A_BUTTON:
            myrobo.send_code(ROAR)
        if event.type == DPAD:
            if event.value == (0,0):
                DPAD_DOWN = False
                CODE = NO_OP
                NEXT_CODE = NO_OP
                myrobo.send_code(NO_OP)
            else:
                DPAD_DOWN = True

            if event.value[1] == 1: # UP
                NEXT_CODE = FORWARD
            elif event.value[1] == -1: # DOWN
                NEXT_CODE = BACKWARD
            if event.value[0] == 1: # Right
                NEXT_CODE = TURN_RIGHT
            elif event.value[0] == -1: # Left
                NEXT_CODE = TURN_LEFT
    # If the dpad is pressed down in the same direction as last time
    # We don't need to resend
    if DPAD_DOWN and CODE != NEXT_CODE:
        CODE = NEXT_CODE
        myrobo.send_code(CODE)


    
myrobo.clean_up()
