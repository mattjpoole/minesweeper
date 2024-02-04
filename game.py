import pygame
import json
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
        self.data = {}
        pygame.init()
        pygame.display.set_caption(WINDOW_CAPTION)

    def setLevel(self, level) -> pygame.Surface:
        if level == LEVEL_EASY:
            self.window_width = EASY_CELL_SIZE * EASY_GRID_SIZE
            self.flags_to_place = NUM_MINES_EASY  
        elif level == LEVEL_MEDIUM:
            self.window_width = MEDIUM_CELL_SIZE * MEDIUM_GRID_SIZE
            self.flags_to_place = NUM_MINES_MEDIUM
        elif level == LEVEL_HARD:
            self.window_width = HARD_CELL_SIZE * HARD_GRID_SIZE
            self.flags_to_place = NUM_MINES_HARD
        if level != self.level:
            self.window_height = self.window_width + UI_HEIGHT
            self.screen = pygame.display.set_mode((self.window_width, self.window_height))
            self.background = pygame.Surface(pygame.display.get_window_size())
            self.background.fill(pygame.Color(UI_BG_COLOUR))
            self.level = level
        self.started = False
        return self.screen
    
    def load_game_data(self) -> None:
        try: 
            # the file already exists 
            with open(GAME_DATA_LOCATION) as load_file: 
                self.data = json.load(load_file) 
        except: 
            # create the file and store initial values 
            with open(GAME_DATA_LOCATION, 'w') as store_file: 
                json.dump(GAME_DATA, store_file)
    
    def getLevel(self) -> str:
        return self.level

    def start_game(self) -> None:
        if not self.started:
            self.timer = pygame.time.get_ticks()
            self.started = True
    
    def game_over(self) -> None:
        self.started = False
    
    def win_game(self) -> None:
        self.started = False
        self.data[self.level] = self.get_time()
        with open(GAME_DATA_LOCATION, 'w') as store_file: 
                json.dump(self.data, store_file)
    
    def get_time(self) -> int:
        return pygame.time.get_ticks() - self.timer
    
    def use_flag(self, change) -> None:
        self.flags_to_place += change

    def get_flags(self) -> int:
        return self.flags_to_place
    
    def render(self) -> None:
        self.screen.blit(self.background, (0, 0))

    def load_icons(self) -> list:
        for icon in ICONS:
            path = ICONS_PATH+icon+ICON_EXT
            self.icons[icon] = pygame.image.load(path).convert_alpha()
        return self.icons

