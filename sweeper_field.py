import pygame
from config import *
from sweeper_cell import SweeperCell

class SweeperField():

    def __init__(self) -> None:
        pass

    def initialise(self) -> None:
        """Create a feild of sweeper cells ready to start the gane"""
        total = EASY_GRID_SIZE * EASY_GRID_SIZE
        screen = pygame.display.get_surface()
        grid_list = []
        top = UI_HEIGHT
        column = left = cell_num = row = 0
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
            cell = SweeperCell(rect)
            grid_list.append(cell)
            # prepare for next loop
            cell_num += 1
            column = cell_num % EASY_GRID_SIZE
            if column == 0:
                row += 1
            left = column * EASY_CELL_SIZE
            top = row * EASY_CELL_SIZE + UI_HEIGHT

    def render(self) -> None:
        pass