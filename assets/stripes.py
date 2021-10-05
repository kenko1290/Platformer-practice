#Name:  Ken Ko
#Email:  ken.ko17@myhunter.cuny.edu
#Date: October 3, 2021
#This program creates an image of a pixel person.

# Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

# Creates a 3D array of 1's
stripe_width = 500
stripe_height = 20
stripe = np.ones((stripe_height,stripe_width,3))

# Draws the stripes
for i in range(0, stripe_width, 10):
    for j in range(0, stripe_height):
        stripe[j,i:i+5,1:] = 0

# Loads array into pyplot to translate into an image
plt.imshow(stripe)

# Displays the image
plt.show()

# Saves the image
plt.imsave("stripe.png",stripe);
