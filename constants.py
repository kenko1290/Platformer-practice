#Name:  Ken Ko
#Email:  ken.ko17@myhunter.cuny.edu
#This contains constants being used.

import pygame

# Define constants for the screen width and height
screen_width = 800
screen_height = 700

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

game_name = "Jumper Platformer"

platform_height = 20

initial_jump_velocity = 10
gravity = 2
