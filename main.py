# Imports
import sys
import pygame
from pygame import *
from time import sleep

# Initialize Pygame library
pygame.init()

# Define colors
white = 255,255,255
black = 0,0,0
blue = 204,255,229

# FPS setter
clock = pygame.time.Clock()

# Initialize display
screen = pygame.display.set_mode([600,600])

# Main event loop
running = True
while running:
    for event in pygame.event.get(): # Checks for events
        # If window closed
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        # Checks for key input
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                print("Left")
            if event.key == K_RIGHT:
                print("Right")
            if event.key == K_DOWN:
                print("Down")
            if event.key == K_UP:
                print("Up")






    # Updates window
    pygame.display.flip()

    clock.tick(60) # 60 fps
