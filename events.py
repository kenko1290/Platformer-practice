#Name:  Ken Ko
#Email:  ken.ko17@myhunter.cuny.edu
#This defines custom events in the game.

#import and initialize the pygame library
import pygame
from constants import *     #imports all constants from constants.py

pygame.init()

# Create a custom event for adding a new platform nd creates an event signal for that event every 4 seconds
# This event signal will be detected inside the main while loop of the game file.
ADDPLATFORM = pygame.USEREVENT + 1
pygame.time.set_timer(ADDPLATFORM, 4000)

