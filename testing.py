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
manager = pygame_gui.UIManager(pygame.display.get_window_size())

# main game classes
ui = UIControls(manager, game.background)
ui.initialise()

field = SweeperField()
field.initialise(game.getLevel())
icons = game.load_icons()
field.set_icons(icons)
ui.set_icons(icons)

running = True
clock = pygame.time.Clock()
while running:
    time_delta = clock.tick(CLOCK_SPEED)/ 1000.0
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    

    ui.set_time(time_delta)
    game.render()
    field.render()
    ui.render(screen)

    pygame.display.flip()

pygame.quit()