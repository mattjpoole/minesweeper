import pygame
from config import *

class Game():

    def __init__(self) -> None:
        self.level = None
        self.window_width = None
        self.window_height = None
        self.screen = None
        self.background = None
        pygame.init()
        pygame.display.set_caption(WINDOW_CAPTION)

    def setLevel(self, level) -> pygame.Surface:
        if level != self.level:
            if level == LEVEL_EASY:
                self.window_width = EASY_CELL_SIZE * EASY_GRID_SIZE   
            elif level == LEVEL_MEDIUM:
                self.window_width = MEDIUM_CELL_SIZE * MEDIUM_GRID_SIZE
            else:
                self.window_width = HARD_CELL_SIZE * HARD_GRID_SIZE
            self.window_height = self.window_width + UI_HEIGHT
            self.screen = pygame.display.set_mode((self.window_width, self.window_height))
            self.background = pygame.Surface(pygame.display.get_window_size())
            self.background.fill(pygame.Color(UI_BG_COLOUR))
            self.level = level
        return self.screen
    
    def getLevel(self) -> str:
        return self.level
    
    def render(self) -> None:
        self.screen.blit(self.background, (0, 0))

