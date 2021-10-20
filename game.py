#Name:  Ken Ko
#Email:  ken.ko17@myhunter.cuny.edu
#This program makes a platform game. Progress by jumping on platforms

#import and initialize the pygame library
import pygame
from pygame import *
from player import Player
from constants import *     #imports all constants from constants.py
from platforms import Platforms
from events import *
import random
from score import *

pygame.init()

# Create the screen object
# The size is determined by the int screen_width and screen_height
# Screen name is determined by string game_name
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_name)

#instantiates a Player object and initial platforms
player = Player()
platform1 = Platforms(screen_width/2, screen_height/6,screen_width/2,screen_height)
platform2 = Platforms(screen_width/5, platform_height,screen_width/4,3*screen_height/5)
platform3 = Platforms(screen_width/5, platform_height,2*screen_width/3,screen_height/4)

player_sprites = pygame.sprite.Group()
platform_sprites = pygame.sprite.Group()

player_sprites.add(player)     #adds Player to player_sprites Sprite Group
platform_sprites.add(platform1, platform2, platform3)

# Set running to true to enter main loop
running = True

score = 0;

# Main game loop. Checks if player has tried to quit with ESC key or pressing
# window close button. Also checks if Player belongs to any sprite groups. Player
# class calls self.kill() if it falls off the bottom of the screen and removes
# itself from all sprite groups. If this happens, game ends.
while running and player.alive():
    
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
            pygame.quit()   #closes the window if close button is pressed

        elif event.type == ADDPLATFORM:
            # platform width will randomly be screen_width/6 to screen_width/4
            # platform height will always be constant platform_height, defined in constants.py
            rand_width = random.randint(screen_width//6, screen_width//4)
            # platform will spawn anywhere within the screen width
            rand_x = random.randint(rand_width//2, screen_width - rand_width//2)
            # platform will spawn above the top of the screen
            rand_y = random.randint(0, 0)
            #creates a new platform with randomized width and location
            new_platform = Platforms(rand_width, platform_height, rand_x, rand_y)
            platform_sprites.add(new_platform)

        # gets a dictionary consisting of all keys paired with true/false
        # depending on if the key is pressed or not

    score = score+10
    user_input = pygame.key.get_pressed()

    player.fall()
    player.move(user_input)
    
    collide_list = pygame.sprite.spritecollide(player, platform_sprites, False)
    for collide in collide_list:
        player.left_vel = 0
        player.right_vel = 0
        player.fall_vel = 0
        player.canJump = True
        #if there's any collisions, player will stay on top of platform as long as player was
        #already above the top of platform when collision occurred
        if(player.rect.bottom >= collide.rect.top and player.rect.top - 30 <= collide.rect.top):
            player.rect.bottom = collide.rect.top
        #stops players from passing through the sides of platforms
        if(player.rect.left <= collide.rect.right and player.rect.right >= collide.rect.right and player.rect.top >= collide.rect.top):
            player.rect.left = collide.rect.right
        if(player.rect.right >= collide.rect.left and player.rect.left <= collide.rect.left and player.rect.top >= collide.rect.top):
            player.rect.right = collide.rect.left

    screen.fill((135,206,250))
    draw_text(screen, "SCORE", 20, screen_width/ 2, 2)
    draw_text(screen, str(score), 20, screen_width/ 2, 15)

    #draws the player rectangle at updated top left corner coordinates (coordinates updated due to smaller hitbox)
    screen.blit(player.surf, (player.rect.left-5,player.rect.top - 33))

    for platforms in platform_sprites:
        platforms.fall()
        screen.blit(platforms.surf, platforms.rect)
        pygame.display.flip()
    
        clock = pygame.time.Clock()
        clock.tick(60)

main()
#draw_text(screen, "FINAL SCORE", 50, screen_width/2, screen_height/2 - 25)
#draw_text(screen, str(score), 50, screen_width/2, screen_height/2 + 25)
#pygame.quit()
