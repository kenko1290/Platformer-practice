#Name:  Ken Ko
#Email:  ken.ko17@myhunter.cuny.edu
#Date: September 27, 2021
#This program takes a .png file and prints dimensions of the file in pixels.

# Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

# gets the two image file names
#first = input("Enter first image file name: ")

# reads the first file using plt.imread and counts white pixels
img1 = plt.imread("player_jump.png")

print("Pixel rows:",img1.shape[0])
print("Pixel columns:",img1.shape[1])
