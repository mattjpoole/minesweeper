"""Minesweeper clone for fun"""
import pygame
import pygame_gui
from config import *
from ui import UIControls
from sweeper_field import SweeperField

# pygame setup
pygame.init()
pygame.display.set_caption(WINDOW_CAPTION)
window_width = EASY_CELL_SIZE * EASY_GRID_SIZE
window_height = window_width + UI_HEIGHT
screen = pygame.display.set_mode((window_width, window_height))
background = pygame.Surface((window_width, window_height))
background.fill(pygame.Color(UI_BG_COLOUR))
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((window_width, window_height))

#main game classes
ui = UIControls(manager)
ui.initialise()
field = SweeperField()
field.initialise()

running = True
while running:
    time_delta = clock.tick(CLOCK_SPEED)/ 1000.0
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            field.click_cell_at_coords(pygame.mouse.get_pos())
        
        manager.process_events(event)

    ui.render(time_delta)

    screen.blit(background, (0, 0))
    field.render()
    ui.draw_ui(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()