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
background = 204,255,229
green = 0,255,0
red = 255,0,0

# FPS setter
clock = pygame.time.Clock()

# Initialize display
screen = pygame.display.set_mode([600,600])

# Main event loop
running = True
while running:
    # Setting screen color and window title
    screen.fill(background)
    pygame.display.set_caption('Game')
    pygame.draw.rect(screen, black,pygame.Rect(250, 250, 100, 50), width=0)
    # Event loop
    for event in pygame.event.get():
        # If window closed
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        # Checks for key input
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                pass





    # Updates window
    pygame.display.flip()

    clock.tick(60) # 60 fps
