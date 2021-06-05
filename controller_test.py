import pygame
import os
from pygame.locals import *

os.environ["DISPLAY"] = ":0"
os.putenv('SDL_VIDEODRIVER','fbcon')
pygame.init()
#screen = pygame.display.set_mode((1,1,))
pygame.display.init()
pygame.joystick.init()

print("Found {} joysticks".format(pygame.joystick.get_count()))

joy = pygame.joystick.Joystick(0)
joy.init()

#print "GUID: {}".format(joy.get_guid())

#print "Power Level: {}".format(joy.get_power_level())

print("Name: {}".format(joy.get_name()))

while(True):
    for event in pygame.event.get():
        print("Event: {}".format(event))
