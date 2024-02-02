import pygame
import pygame_gui
from config import *

class UIControls():

    def __init__(self, manager) -> None:
        self.level_drop_down = None
        self.ui_manager = manager
        self.bg_rect = None
        self.bg_surface = None

    def initialise(self, starting_level=LEVEL_EASY) -> None:                             
        self.level_drop_down = pygame_gui.elements.UIDropDownMenu(
            options_list=[LEVEL_EASY, LEVEL_MEDIUM, LEVEL_HARD],
            starting_option=starting_level, relative_rect=pygame.Rect((7, 7), (100, 40)),
            manager=self.ui_manager)


    def render(self, time_delta) -> None:
       self.ui_manager.update(time_delta)


    def draw_ui(self, surf) -> None:
        self.ui_manager.draw_ui(surf)