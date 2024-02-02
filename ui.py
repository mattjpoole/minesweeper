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

    def initialise(self, starting_level=LEVEL_EASY) -> None:                             
        self.level = starting_level
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
    
    def set_level(self, level) -> None:
        self.level = level

    def set_time(self, time_delta) -> None:
        self.ui_manager.update(time_delta)
    
    def render(self) -> None:
        screen = pygame.display.get_surface()
        self.ui_manager.draw_ui(screen)
        screen.fill(CELL_COLOUR_EMPTY, self.flag_rect)
        screen.fill(CELL_COLOUR_EMPTY, self.timer_rect)

        screen.blit(
            pygame.transform.smoothscale(self.icons[ICON_FLAG], (30,30)), (140, 12))
        
        screen.blit(
            pygame.transform.smoothscale(self.icons[ICON_TIMER], (30,30)), (245, 12))
        
        font = pygame.font.SysFont(None, 24)
        num_flags_text = font.render("x 10", True, "black")
        timer_text = font.render("00:00", True, "black")
        screen.blit(num_flags_text, (170, 20))
        screen.blit(timer_text, (285, 20))