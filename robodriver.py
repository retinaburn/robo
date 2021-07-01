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
MENU_BUTTON             = 7
X_BUTTON                = 2
B_BUTTON                = 1
A_BUTTON                = 0
DPAD                    = JOYHATMOTION
LEFTSTICK_LEFTRIGHT     = 0
LEFTSTICK_UPDOWN        = 1
RIGHTSTICK_LEFTRIGHT    = 3
RIGHTSTICK_UPDOWN       = 4

# Input Loop Definitions
IS_RUNNING      = True
DPAD_DOWN       = False
CODE            = 0x00  #The last code sent to RS
NEXT_CODE       = 0x00 #The next code sent to RS

# Robosapien codes
FORWARD         = robo.CODE_RSWalkForward   #walk forward and back send 1 code and walking continues
BACKWARD        = robo.CODE_RSWalkBackward  #until you send a no-op or stop
TURN_LEFT       = robo.CODE_RSTurnLeft
TURN_RIGHT      = robo.CODE_RSTurnRight
NO_OP           = robo.CODE_RSNoOp
BURP            = robo.CODE_RSBurp
ROAR            = robo.CODE_RSRoar
KARATE          = robo.CODE_RSKarateChop
RIGHTARM_UP     = robo.CODE_RSRightArmUp    #arm codes work different than the forward and back
RIGHTARM_DOWN   = robo.CODE_RSRightArmDown  #these you can send multiple times and get different positions
RIGHTARM_OUT    = robo.CODE_RSRightArmOut
RIGHTARM_IN     = robo.CODE_RSRightArmIn
LEFTARM_UP      = robo.CODE_RSLeftArmUp
LEFTARM_DOWN    = robo.CODE_RSLeftArmDown
LEFTARM_OUT     = robo.CODE_RSLeftArmOut
LEFTARM_IN      = robo.CODE_RSLeftArmIn


# Controller Tweaks for Responsiveness Definitions
DEAD_ZONE = 0.2
LAST_LEFT_JOY_EVENT = 0
LAST_RIGHT_JOY_EVENT = 0
JOY_EVENT_DEDUP = 0.7

def log_event(event):
    try:
        print("Event Type: {}, Event Button: {}, Event: {}".format(event.type,event.button,event))
    except AttributeError:
        print("Event Type: {}, Event Value: {}, Event: {}".format(event.type,event.value,event))



while(IS_RUNNING):
    for event in pygame.event.get():

        if event.type == JOYBUTTONUP and event.button == MENU_BUTTON:
            print("Quitting...")
            IS_RUNNING = False
        if event.type == JOYAXISMOTION:# and event.axis == RIGHTSTICK_UPDOWN:
            #Joy events arrive very quickly, we dont want to pay attention to all of them
            if (event.value > DEAD_ZONE or event.value < (-1*DEAD_ZONE)):
                #print("Last Joy Event: {} + Dedup Interval {} = {} < {} is {}".format(LAST_JOY_EVENT, JOY_EVENT_DEDUP, (LAST_JOY_EVENT + JOY_EVENT_DEDUP), currentTime,((LAST_JOY_EVENT + JOY_EVENT_DEDUP) < currentTime)))
                currentTime = time.time()

                # Right Arm Control
                if event.axis == RIGHTSTICK_UPDOWN or event.axis == RIGHTSTICK_LEFTRIGHT:
                    if (LAST_RIGHT_JOY_EVENT + JOY_EVENT_DEDUP) < currentTime:
                        LAST_RIGHT_JOY_EVENT = currentTime
                        if event.value > DEAD_ZONE: 
                            log_event(event)
                            if event.axis == RIGHTSTICK_UPDOWN:
                                print("Right - Down")
                                myrobo.send_code(RIGHTARM_DOWN)
                            elif event.axis == RIGHTSTICK_LEFTRIGHT:
                                print("Right - Out")
                                myrobo.send_code(RIGHTARM_OUT)
                        elif event.value < (-1*DEAD_ZONE): 
                            log_event(event)
                            if event.axis == RIGHTSTICK_UPDOWN:
                                print("Right - Up")
                                myrobo.send_code(RIGHTARM_UP)
                            elif event.axis == RIGHTSTICK_LEFTRIGHT:
                                print("Right - In")
                                myrobo.send_code(RIGHTARM_IN)
                        else:
                            print("Zeroed")

                # Left Arm Control
                elif event.axis == LEFTSTICK_UPDOWN or event.axis == LEFTSTICK_LEFTRIGHT:
                    if (LAST_LEFT_JOY_EVENT + JOY_EVENT_DEDUP) < currentTime:
                        LAST_LEFT_JOY_EVENT = currentTime
                        if event.value > DEAD_ZONE: 
                            log_event(event)
                            if event.axis == LEFTSTICK_UPDOWN:
                                print("Left - Down")
                                myrobo.send_code(LEFTARM_DOWN)
                            elif event.axis == LEFTSTICK_LEFTRIGHT:
                                print("Left - In")
                                myrobo.send_code(LEFTARM_IN)
                        elif event.value < (-1*DEAD_ZONE): 
                            log_event(event)
                            if event.axis == LEFTSTICK_UPDOWN:
                                print("Left - Up")
                                myrobo.send_code(LEFTARM_UP)
                            elif event.axis == LEFTSTICK_LEFTRIGHT:
                                print("Left - Out")
                                myrobo.send_code(LEFTARM_OUT)

                        else:
                            print("Zeroed")
        if event.type == JOYBUTTONUP:
            if event.button == B_BUTTON:
                myrobo.send_code(BURP)
            elif event.button == A_BUTTON:
                myrobo.send_code(ROAR)
            elif event.button == X_BUTTON:
                myrobo.send_code(KARATE)
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
