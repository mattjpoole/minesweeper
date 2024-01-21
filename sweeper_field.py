import random
import pygame
from config import *
from sweeper_cell import SweeperCell

class SweeperField():

    def __init__(self) -> None:
        self.grid_list = []
        self.icons = []

    def initialise(self, level) -> None:
        """Create a feild of sweeper cells ready to start the game"""
        if level == LEVEL_EASY:
            grid_size = EASY_GRID_SIZE
            cell_size = EASY_CELL_SIZE
            num_mines = NUM_MINES_EASY
        elif level == LEVEL_MEDIUM:
            grid_size = MEDIUM_GRID_SIZE
            cell_size = MEDIUM_CELL_SIZE
            num_mines = NUM_MINES_MEDIUM
        else:
            grid_size = HARD_GRID_SIZE
            cell_size = HARD_CELL_SIZE
            num_mines = NUM_MINES_HARD

        self.icons = []
        total = grid_size * grid_size
        screen = pygame.display.get_surface()
        top = UI_HEIGHT
        column = left = cell_num = row = 0
        mine_locations = self.generatate_mine_locations(total, num_mines)
        while cell_num<total:
            if (cell_num % 2 == 0):
                if (row % 2 == 0):
                    colour = CELL_COLOUR
                else:   
                    colour = ALT_CELL_COLOUR
            else:
                if row % 2 == 0:
                    colour = ALT_CELL_COLOUR
                else:
                    colour = CELL_COLOUR
            rect = pygame.draw.rect(screen, colour, [left, top, cell_size, cell_size])
            has_mine = False
            for location in mine_locations:
                if cell_num == location:
                    has_mine = True
            cell = SweeperCell(rect, colour, has_mine)
            cell.set_size((cell_size, cell_size))
            self.grid_list.append(cell)
            # prepare for next loop
            cell_num += 1
            column = cell_num % grid_size
            if column == 0:
                row += 1
            left = column * cell_size
            top = row * cell_size + UI_HEIGHT
    
    def set_icons(self, icons) -> None:
        self.icons = icons

    def render(self) -> None:
        screen = pygame.display.get_surface()
        for cell in self.grid_list:
            cell_rect = cell.get_rect()
            screen.fill(cell.get_colour(), cell_rect)
            if (cell_rect.collidepoint(pygame.mouse.get_pos()) and cell.is_closed()):
                pygame.draw.rect(screen, CELL_BORDER_HOVER, cell_rect, 2)
            cell.render()

    def generatate_mine_locations(self, total, num_mines) -> list:
        # no logic yet for removing dupes
        mine_locations = []
        while len(mine_locations)< num_mines:
            location = random.randint(0, total-1)
            mine_locations.append(location)
        return mine_locations
    
    def click_cell_at_coords(self, coords) -> None:
        for cell in self.grid_list:
            cell_rect = cell.get_rect()
            if cell_rect.collidepoint(coords):
                if cell.is_mine_square():
                    # end the game
                    cell.set_colour(CELL_COLOUR_MINE)
                    cell.set_state(ICON_MINE, self.icons[ICON_MINE])
                    self.reveal_all_mines()
                else:
                    # iterate over icons based upon neighbourng cells
                    pass
    
    def reveal_all_mines(self):
        for cell in self.grid_list:
                if cell.is_mine_square() and cell.is_closed:
                    cell.set_state(ICON_MINE, self.icons[ICON_MINE])