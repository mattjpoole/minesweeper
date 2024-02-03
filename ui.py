import pygame
import pygame_gui
from config import *

class UIControls():

    def __init__(self, manager, bg_rect) -> None:
        self.level_drop_down = None
        self.ui_manager = manager
        self.flag_rect = None
        self.bg_rect = bg_rect
        self.icons = None
        self.game_time = 0
        self.flags_to_place = 0

    def initialise(self, starting_level, flags) -> None:                             
        self.set_level(starting_level, flags)
        
        self.level_drop_down = pygame_gui.elements.UIDropDownMenu(
            options_list=[LEVEL_EASY, LEVEL_MEDIUM, LEVEL_HARD],
            starting_option=starting_level, relative_rect=pygame.Rect((7, 7), (100, 40)),
            manager=self.ui_manager)
        self.flag_rect = pygame.draw.rect(self.bg_rect, CELL_COLOUR_EMPTY,
                                          [140, 10, 70, 35])
        self.timer_rect = pygame.draw.rect(self.bg_rect, CELL_COLOUR_EMPTY,
                                          [240, 10, 100, 35])

    def set_icons(self, icons) -> None:
        self.icons = icons
    
    def set_level(self, level, flags) -> None:
        self.level = level
        self.flags_to_place = flags
        self.game_time = 0

    def set_time_delta(self, time_delta) -> None:
        self.ui_manager.update(time_delta)

    def set_game_time(self, game_time) -> None:
        self.game_time = game_time

    def set_flags(self, flags) -> None:
        self.flags_to_place = flags
    
    def render(self) -> None:
        screen = pygame.display.get_surface()
        # draw drop down
        self.ui_manager.draw_ui(screen)
        
        # draw flags used
        font = pygame.font.SysFont(None, 24)
        num_flags_text = font.render("x "+str(self.flags_to_place), True, "black")
        screen.fill(CELL_COLOUR_EMPTY, self.flag_rect)
        screen.blit(
            pygame.transform.smoothscale(self.icons[ICON_FLAG], (30,30)), (140, 12))
        screen.blit(num_flags_text, (170, 20))
        
        # draw game timer
        total_time_in_seconds = int(self.game_time / 1000)
        seconds = int(total_time_in_seconds % 60)
        minutes = int(total_time_in_seconds / 60)
        display_seconds = str(seconds)
        if (seconds<10):
            display_seconds = "0"+display_seconds
        display_minutes = str(minutes)
        if (minutes<10):
            display_minutes = "0"+display_minutes
        display_time = display_minutes+":"+display_seconds
        timer_text = font.render(display_time, True, "black")
        screen.fill(CELL_COLOUR_EMPTY, self.timer_rect)
        screen.blit(
            pygame.transform.smoothscale(self.icons[ICON_TIMER], (30,30)), (245, 12))
        screen.blit(timer_text, (285, 20))