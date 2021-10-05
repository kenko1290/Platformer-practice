#Name:  Ken Ko
#Email:  ken.ko17@myhunter.cuny.edu
#This defines the platform class.

#import pygame library
import pygame

#import constants.py file
from constants import *

# Import random library for random numbers
import random

class Platforms(pygame.sprite.Sprite):     #Platform class extends Sprite
    def __init__(self, width, height, x_coord, y_coord):    #x and y are coordinates of bottom center of platform
        super(Platforms, self).__init__()
        self.width = width
        self.height = height
        self.x_coord = x_coord
        self.y_coord = y_coord
        #creates a new surface and colors it red
        self.surf = pygame.Surface((self.width,self.height))
        #self.surf = pygame.Surface((screen_width/2,500))
        self.surf.fill((255, 0, 0))

        #creates a rectangle with the size of surface and center at randomized coordinates
        self.rect = self.surf.get_rect(
                    midbottom = (x_coord, y_coord),
                    )

        #self.speed = random.randint(1, 2)  
        
    # Move the sprite based on speed
    # Remove the sprite when it passes the bottom of the screen
    def fall(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > screen_height:
            self.kill()
