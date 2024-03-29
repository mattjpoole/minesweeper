import random
import pygame
from config import *
from sweeper_cell import SweeperCell

class SweeperField():

    def __init__(self) -> None:
        self.grid_list = []
        self.icons = []
        self.grid_size = 0
        self.num_mines = 0
        self.started = False

    def initialise(self, level) -> None:
        """Create a feild of sweeper cells ready to start the game"""
        self.grid_list = []
        self.level = level
        self.game_over = False
        if level == LEVEL_EASY:
            self.grid_size = EASY_GRID_SIZE
            cell_size = EASY_CELL_SIZE
            num_mines = NUM_MINES_EASY
        elif level == LEVEL_MEDIUM:
            self.grid_size = MEDIUM_GRID_SIZE
            cell_size = MEDIUM_CELL_SIZE
            num_mines = NUM_MINES_MEDIUM
        else:
            self.grid_size = HARD_GRID_SIZE
            cell_size = HARD_CELL_SIZE
            num_mines = NUM_MINES_HARD
        self.num_mines = num_mines
        self.started = False
        total = self.grid_size * self.grid_size
        screen = pygame.display.get_surface()
        top = UI_HEIGHT
        column = left = cell_num = row = 0
        while cell_num<total:
            if cell_num % 2 == 0:
                if row % 2 == 0:
                    colour = CELL_COLOUR
                else:   
                    colour = ALT_CELL_COLOUR
            else:
                if row % 2 == 0:
                    colour = ALT_CELL_COLOUR
                else:
                    colour = CELL_COLOUR
            rect = pygame.draw.rect(screen, colour, [left, top, cell_size, cell_size])
            cell = SweeperCell(rect, colour)
            cell.set_size((cell_size, cell_size))
            cell.set_field_coords(column, row)
            cell.set_grid_index(cell_num)
            self.grid_list.append(cell)
            # prepare for next loop
            cell_num += 1
            column = cell_num % self.grid_size
            if column == 0:
                row += 1
            left = column * cell_size
            top = row * cell_size + UI_HEIGHT

    def set_number_mines(self) -> None:
        """precalculates how many neighbouring mines each cell has"""
        mines = 0
        for cell in self.grid_list:
            neighbours = self.get_neighbours(cell)
            for neighbour in neighbours:
                if neighbour.is_mine_square():
                    mines += 1
            cell.set_num_mines(mines)
            mines = 0
 
    def set_icons(self, icons) -> None:
        self.icons = icons

    def render(self, hoverEnabled) -> None:
        for cell in self.grid_list:
            cell.render(hoverEnabled)

    def generatate_mine_locations(self, total, num_mines, excludes) -> dict:
        mine_locations = {}
        if DEBUG_ON :
            if self.level == LEVEL_EASY:
                mine_locations = DEBUG_MINE_LOCATIONS_EASY   
            elif self.level == LEVEL_MEDIUM:
                mine_locations = DEBUG_MINE_LOCATIONS_MEDIUM
            elif self.level == LEVEL_HARD:
                mine_locations = DEBUG_MINE_LOCATIONS_HARD
        else:
            while len(mine_locations) < num_mines:
                location = random.randint(0, total-1)
                excluded = False
                for cell in excludes:
                    if cell.get_grid_index() == location:
                        excluded = True
                        break
                if not excluded:
                    mine_locations[str(location)] = location
        return mine_locations
    
    def place_mines(self, start_cell) -> None:
        # place the mines avoiding where the player has clicked
        excludes = self.get_neighbours(start_cell)
        excludes.append(start_cell)
        total = self.grid_size * self.grid_size
        mine_locations = self.generatate_mine_locations(total, self.num_mines, excludes)
        for cell in self.grid_list:
            cell.set_has_mine(cell.get_grid_index() in mine_locations.values())
    
    def click_cell_at_coords(self, coords) -> bool:
        index = 0
        cell_clicked = False
        for cell in self.grid_list:
            cell_rect = cell.get_rect()
            if cell_rect.collidepoint(coords):
                if not self.started:
                    self.started = True
                    self.place_mines(cell)
                    self.set_number_mines()
                if cell.is_mine_square():
                    # end the game
                    cell.set_colour(CELL_COLOUR_MINE)
                    cell.set_state(ICON_MINE, self.icons[ICON_MINE])
                    cell.exploded = True
                    self.reveal_all_mines()
                    self.game_over = True
                else:
                    self.reveal_cells(cell, self.get_neighbours(cell))
                    cell_clicked = True
                    break
            index += 1
        return cell_clicked
    
    def right_click_cell_at_coords(self, coords, flags_left) -> int:
        change = 0
        for cell in self.grid_list:
            cell_rect = cell.get_rect()
            if cell_rect.collidepoint(coords):
                if cell.has_flag():
                    cell.set_state(ICON_STATE_CLOSED)
                    change = 1
                elif cell.is_closed():
                    if flags_left > 0:
                        cell.set_state(ICON_FLAG, self.icons[ICON_FLAG])
                        change = -1
        return change

    def get_neighbours(self, kernel) -> list:
        """Method to select neighbouring cells for given cell"""
        out_of_bounds_rect = pygame.Rect(0,0,0,0)
        top_left = top_middle = top_right = middle_left = middle_right = bottom_left = bottom_middle = bottom_right = SweeperCell(out_of_bounds_rect, None, False, ICON_STATE_OUTOFBOUNDS)
        cell_index = kernel.get_grid_index()
        try:
            # if we are not at the top edge
            if kernel.get_row()>0:
                top_middle = self.grid_list[cell_index-self.grid_size]
                # and if we are not at the left edge
                if kernel.get_column()>0:
                    top_left = self.grid_list[cell_index-self.grid_size-1]
                # and if we are not at the right edge
                if kernel.get_column()<self.grid_size-1:
                    top_right = self.grid_list[cell_index-self.grid_size+1]
            
            # if we are not on the left edge
            if kernel.get_column()>0:
                middle_left = self.grid_list[cell_index-1]
             
            # if we are not on the right edge
            if kernel.get_column()<self.grid_size-1:
                middle_right = self.grid_list[cell_index+1]
            
            # if we are not the bottom edge
            if kernel.get_row() < self.grid_size-1:
                bottom_middle = self.grid_list[cell_index+self.grid_size]
                # and we are not on the left edge
                if kernel.get_column()>0:
                    bottom_left = self.grid_list[cell_index+self.grid_size-1]
                # and we are not at the right edge
                if kernel.get_column()<self.grid_size-1:
                    bottom_right = self.grid_list[cell_index+self.grid_size+1]

        except IndexError:
            print("cell index out of bounds ====")
            print("kernel.get_column()"+str(kernel.get_column()))
            print("kernel.get_row()"+str(kernel.get_row()))
        neighbours = [top_left, top_middle, top_right, middle_left, middle_right, bottom_left, bottom_middle, bottom_right]
        return neighbours
    
    def get_mine_cells(self) -> list:
        mine_cells = []
        for cell in self.grid_list:
            if cell.is_mine_square():
                mine_cells.append(cell)
        return mine_cells
    
    def reveal_cells(self, cell, neighbours:list) -> None:
        if cell.is_closed():
            if cell.get_num_mines() == 0:
                cell.set_state(ICON_STATE_EMPTY) 
                if cell.get_colour()==CELL_COLOUR:
                    cell.set_colour(CELL_COLOUR_EMPTY)
                else:
                    cell.set_colour(ALT_CELL_COLOUR_EMPTY)
                for neighbour in neighbours:
                    if neighbour.is_in_bounds():
                        self.reveal_cells(neighbour, self.get_neighbours(neighbour))
            else:
                cell_state = ICONS[cell.get_num_mines()-1]
                cell.set_state(cell_state, self.icons[cell_state])
                if cell.get_colour()==CELL_COLOUR:
                    cell.set_colour(CELL_COLOUR_EMPTY)
                else:
                    cell.set_colour(ALT_CELL_COLOUR_EMPTY)

    def reveal_all_mines(self):
        for cell in self.grid_list:
            if cell.is_mine_square() and cell.is_closed():
                cell.set_state(ICON_MINE, self.icons[ICON_MINE])
            elif cell.has_flag() and not cell.is_mine_square():
                cell.set_state(ICON_BADFLAG, self.icons[ICON_BADFLAG])

    def is_win_condition(self) -> bool:
        flagged_mines = 0
        for cell in self.grid_list:
            if cell.is_mine_square() and cell.has_flag():
                flagged_mines += 1
        return flagged_mines == self.num_mines
    
    def is_game_over(self) -> bool:
        return self.game_over