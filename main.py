"""Minesweeper clone for fun"""
import pygame
import pygame_gui
from config import *
from game import Game
from ui import UIControls
from sweeper_field import SweeperField

# game setup
game = Game()
screen = game.setLevel(LEVEL_EASY)

background = pygame.Surface(pygame.display.get_window_size())
background.fill(pygame.Color(UI_BG_COLOUR))
clock = pygame.time.Clock()

manager = pygame_gui.UIManager(pygame.display.get_window_size())

# main game classes
ui = UIControls(manager)
ui.initialise()
field = SweeperField()
field.initialise(game.getLevel())

running = True
while running:
    time_delta = clock.tick(CLOCK_SPEED)/ 1000.0
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            field.click_cell_at_coords(pygame.mouse.get_pos())
        elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            screen = game.setLevel(event.text)
            background = pygame.Surface(pygame.display.get_window_size())
            background.fill(pygame.Color(UI_BG_COLOUR))
            manager.set_window_resolution(pygame.display.get_window_size())
            field.initialise(game.getLevel())
        manager.process_events(event)

    ui.render(time_delta)
    screen.blit(background, (0, 0))
    field.render()
    ui.draw_ui(screen)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()