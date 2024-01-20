import random
import pygame
from config import *
from sweeper_cell import SweeperCell

class SweeperField():

    def __init__(self) -> None:
        self.grid_list = []

    def initialise(self) -> None:
        """Create a feild of sweeper cells ready to start the gane"""
        total = EASY_GRID_SIZE * EASY_GRID_SIZE
        screen = pygame.display.get_surface()
        top = UI_HEIGHT
        column = left = cell_num = row = 0
        mine_locations = self.generatate_mine_locations(total)
        while cell_num<total:
            if (cell_num % 2 == 0):
                if (row % 2 == 0):
                    colour = CELL_COLOUR
                else:   
                    colour = ALT_CELL_COLOUR
            else:
                if (row % 2 == 0):
                    colour = ALT_CELL_COLOUR
                else: 
                    colour = CELL_COLOUR
            rect = pygame.draw.rect(screen, colour, [left, top, EASY_CELL_SIZE, EASY_CELL_SIZE])
            has_mine = False
            for location in mine_locations:
                if cell_num == location:
                    has_mine = True
            cell = SweeperCell(rect, colour, has_mine)
            self.grid_list.append(cell)
            # prepare for next loop
            cell_num += 1
            column = cell_num % EASY_GRID_SIZE
            if column == 0:
                row += 1
            left = column * EASY_CELL_SIZE
            top = row * EASY_CELL_SIZE + UI_HEIGHT

    def render(self) -> None:
        screen = pygame.display.get_surface()
        for cell in self.grid_list:
            cell_rect = cell.get_rect()
            screen.fill(cell.get_colour(), cell_rect)
            if (cell_rect.collidepoint(pygame.mouse.get_pos())):
                pygame.draw.rect(screen, CELL_BORDER_HOVER, cell_rect, 2)

    def generatate_mine_locations(self, total) -> list:
        # no logic yet for removing dupes
        mine_locations = []
        while len(mine_locations)< NUM_MINES_EASY:
            location = random.randint(0, total-1)
            mine_locations.append(location)
        return mine_locations
    
    def click_cell_at_coords(self, coords) -> None:
        for cell in self.grid_list:
            cell_rect = cell.get_rect()
            if (cell_rect.collidepoint(pygame.mouse.get_pos())):
                if cell.is_mine_square():
                    print("BOOM!")
