"""Minesweeper clone for fun"""
import pygame
from config import *
from ui import UIControls
from sweeper_field import SweeperField

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill(WINDOW_BG_COLOUR)
clock = pygame.time.Clock()
running = True

#main game classes
ui = UIControls()
ui.initialise()
field = SweeperField()
field.initialise()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    ui.render()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(CLOCK_SPEED)  # limits FPS to 60

pygame.quit()