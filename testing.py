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
ui = UIControls(manager)
ui.initialise()
field = SweeperField()
field.initialise(game.getLevel())
icons = game.load_icons()
field.set_icons(icons)

new_surface = pygame.Surface((100,100))
new_surface.blit(icons[ICON_ONE], (0,0))
screen.blit(new_surface, (0,0))

running = True
clock = pygame.time.Clock()
while running:
    time_delta = clock.tick(CLOCK_SPEED)/ 1000.0
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    

    ui.render(time_delta)
    field.render()
    ui.draw_ui(screen)

    pygame.display.get_surface().blit(icons[ICON_TWO], (0,0))

    pygame.display.flip()

pygame.quit()