"""Minesweeper clone for fun"""
import pygame
import pygame_gui
from config import LEVEL_EASY, CLOCK_SPEED
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
field.set_icons(game.load_icons())

running = True
clock = pygame.time.Clock()
while running:
    time_delta = clock.tick(CLOCK_SPEED)/ 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = pygame.mouse.get_pressed()
            if mouse_click[0]:
                field.click_cell_at_coords(pygame.mouse.get_pos())
            elif mouse_click[2]:
                field.right_click_cell_at_coords(pygame.mouse.get_pos())
        elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            screen = game.setLevel(event.text)
            manager.set_window_resolution(pygame.display.get_window_size())
            field.initialise(game.getLevel())
        manager.process_events(event)

    ui.render(time_delta)
    game.render()
    field.render()
    ui.draw_ui(screen)

    pygame.display.flip()

pygame.quit()