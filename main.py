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
ui.initialise(game.getLevel())
ui.set_icons(game.load_icons())
field = SweeperField()
field.initialise(game.getLevel())
field.set_icons(game.load_icons())
if DEBUG_ON:
    field.reveal_all_mines()

running = True
clock = pygame.time.Clock()
while running:
    time_delta = clock.tick(CLOCK_SPEED)/ 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = pygame.mouse.get_pressed()
            cell_clicked = toggled_on = False
            if mouse_click[0]:
                cell_clicked = field.click_cell_at_coords(pygame.mouse.get_pos())
            elif mouse_click[2]:
                toggled_on = field.right_click_cell_at_coords(pygame.mouse.get_pos())
                ui.use_flag(toggled_on)
            
            if cell_clicked or toggled_on:
                game.start_game()
        elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            screen = game.setLevel(event.text)
            ui.set_level(game.getLevel())
            manager.set_window_resolution(pygame.display.get_window_size())
            field.initialise(game.getLevel())
            if DEBUG_ON:
                field.reveal_all_mines()
        manager.process_events(event)

    ui.set_time_delta(time_delta)
    if (game.started):
        ui.set_game_time(game.get_time())
    game.render()
    field.render()
    ui.render()

    pygame.display.flip()

pygame.quit()