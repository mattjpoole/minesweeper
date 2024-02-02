import pygame
from config import *

class Game():

    def __init__(self) -> None:
        self.level = None
        self.window_width = None
        self.window_height = None
        self.screen = None
        self.background = None
        self.icons = {}
        self.timer = 0
        self.started = False
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
        self.started = False
        return self.screen
    
    def getLevel(self) -> str:
        return self.level

    def start_game(self) -> None:
        if not self.started:
            self.timer = pygame.time.get_ticks()
            self.started = True
    
    def get_time(self) -> int:
        return pygame.time.get_ticks() - self.timer
    
    def render(self) -> None:
        self.screen.blit(self.background, (0, 0))

    def load_icons(self) -> list:
        for icon in ICONS:
            path = ICONS_PATH+icon+ICON_EXT
            self.icons[icon] = pygame.image.load(path).convert_alpha()
        return self.icons

