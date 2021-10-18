#Name:  Ken Ko
#Email:  ken.ko17@myhunter.cuny.edu
#This defines the player class.

#import the pygame library
import pygame

#import constants.py file
from constants import *

class Player(pygame.sprite.Sprite):     #Player class extends Sprite
    def __init__(self):
        #equivalent to calling the base class pygame.sprite.Sprite._init_(self)
        super(Player, self).__init__()

        # loads person image onto a new surface
        self.surf = pygame.image.load("assets/person.png").convert()
        
        # scales the image to a custom size
        #self.surf = pygame.transform.scale(self.surf, (50,50))
        
        # if any pixel in the image is (255,255,255) i.e. white, make that pixel transparent
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        #creates a rectangle with the size of the surface and bottom at bottom center of screen
        self.rect = self.surf.get_rect(midbottom = (screen_width/2, 5*screen_height/6),)
        #reduces the player hitbox width by 10 pixels and height by 39 pixels, leaving a 14 pixel width and 1 pixel height for the hitbox
        self.rect.inflate_ip(-10,-39)

        self.canJump = False
        self.jumping = 0
    
    # Move the sprite based on user keypresses. Looks up the given keystrokes in the user_input
    # dictionary and whether that key is pressed or not
    def move(self, user_input):
        #if user_input[K_UP]:
            #self.rect.move_ip(0, -5)
        if user_input[K_LEFT]:
            self.rect.move_ip(-25, 0)
        if user_input[K_DOWN]:
            self.rect.move_ip(0, 5)
        if user_input[K_RIGHT]:
            self.rect.move_ip(25, 0)
        # continues moving up to mimic momentum of jump
        if self.jumping > 0:
            self.rect.move_ip(0,-40)
            self.jumping -= 1
        if user_input[K_SPACE]:
            if(self.canJump == True):
                self.jumping = 17
                self.canJump = False

        #keeps player within boundaries of screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            #self.kill()
        if self.rect.top < 0:
            self.rect.top = 0
        
    def fall(self):    #does not take any user input       
        self.rect.move_ip(0,20)
