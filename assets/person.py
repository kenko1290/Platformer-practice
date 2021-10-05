#Name:  Ken Ko
#Email:  ken.ko17@myhunter.cuny.edu
#Date: October 3, 2021
#This program creates an image of a pixel person.

# Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

# Creates a 3D array of 1's
player_width = 40
player_height = 40
person = np.ones((player_height,player_width,3))

# Draws the head and neck of the person in black
person[:6,17:23,:] = 0
person[6:7,18:22,:] = 0

# Draws the torso of the person in black
person[7:24,14:26,:] = 0

# Draws the legs
person[24:41,15:19,:] = 0
person[24:41,21:25,:] = 0

# Draws the arms
person[10:13,8:14,:] = 0
person[10:13,26:32,:] = 0
person[2:10,8:11,:] = 0
person[13:21,29:32,:] = 0

# Loads array into pyplot to translate into an image
plt.imshow(person)

# Displays the image
plt.show()

# Saves the image
plt.imsave("person.png",person);
