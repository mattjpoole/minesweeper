import random
import pygame
from config import *
from sweeper_cell import SweeperCell

class SweeperField():

    def __init__(self) -> None:
        self.grid_list = []
        self.icons = []
        self.grid_size = 0
        self.rn = 0

    def initialise(self, level) -> None:
        """Create a feild of sweeper cells ready to start the game"""
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

        self.icons = []
        total = self.grid_size * self.grid_size
        screen = pygame.display.get_surface()
        top = UI_HEIGHT
        column = left = cell_num = row = 0
        mine_locations = self.generatate_mine_locations(total, num_mines)
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
            has_mine = False
            for location in mine_locations:
                if cell_num == location:
                    has_mine = True
            cell = SweeperCell(rect, colour, has_mine)
            cell.set_size((cell_size, cell_size))
            cell.set_field_coords(column, row)
            self.grid_list.append(cell)
            # prepare for next loop
            cell_num += 1
            column = cell_num % self.grid_size
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
            if (cell_rect.collidepoint(pygame.mouse.get_pos()) and cell.is_closed() and not cell.is_empty()):
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
        index = 0

        for cell in self.grid_list:
            cell_rect = cell.get_rect()
            if cell_rect.collidepoint(coords):
                if cell.is_mine_square():
                    # end the game
                    cell.set_colour(CELL_COLOUR_MINE)
                    cell.set_state(ICON_MINE, self.icons[ICON_MINE])
                    self.reveal_all_mines()
                else:
                    self.count_adjacent_mines(cell, self.get_neighbours(index))
                    self.reset_cell_pending_state()
                    break
            index += 1
    
    def right_click_cell_at_coords(self, coords) -> None:
        for cell in self.grid_list:
            cell_rect = cell.get_rect()
            if cell_rect.collidepoint(coords):
                if cell.has_flag():
                    cell.set_state(ICON_STATE_CLOSED)
                elif cell.is_closed():
                    cell.set_state(ICON_FLAG, self.icons[ICON_FLAG])

    def get_neighbours(self, cell_index) -> list:
        """Method to select neighbouring cells for give cell"""
        out_of_bounds_rect = pygame.Rect(0,0,0,0)
        top_left = top_middle = top_right = middle_left = middle_right = bottom_left = bottom_middle = bottom_right = SweeperCell(out_of_bounds_rect, None, False, ICON_STATE_OUTOFBOUNDS)
        kernel = self.grid_list[cell_index]
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
    
    def count_adjacent_mines(self, cell, neighbours:list) -> None:
        mines = 0
        new_neighbours = []
        for neighbour in neighbours:
            if neighbour.is_mine_square():
                mines += 1
            elif neighbour.is_closed():
                # the pending state means it wont be checked more than once.
                neighbour.set_state(ICON_STATE_PENDING)
                new_neighbours.append(neighbour)

        if mines > 0:
            # set the number icon for this cell
            cell_state = ICONS[mines-1]
            cell.set_state(cell_state, self.icons[cell_state])
        else:
            cell.set_state(ICON_STATE_EMPTY)
            cell.set_colour(CELL_COLOUR_EMPTY)
            for neighbour in new_neighbours:
                n_index = self.get_grid_index_from_cell(neighbour)
                self.count_adjacent_mines(neighbour, self.get_neighbours(n_index))

    def count_adjacent_mines_p(self, cell, neighbours:list) -> None:
        new_neighbours = self.set_num_mines(cell, neighbours)
        if len(new_neighbours) > 0:
            # check the neightbours of this cell for the number of adjacent mines
            for neighbour in new_neighbours:
                # the pending state means it wont be checked more than once.
                n_index = self.get_grid_index_from_cell(neighbour)
                next_neighbours = self.set_num_mines(neighbour, self.get_neighbours(n_index))
                for n in next_neighbours:
                    self.set_num_mines(n, next_neighbours)
    
    def set_num_mines(self, cell, neighbours) -> list:
        mines = 0
        new_neighbours = []
        cell.set_state(ICON_STATE_PENDING)
        for neighbour in neighbours:
            if neighbour.is_mine_square():
                mines += 1
            elif neighbour.is_closed():
                neighbour.set_state(ICON_STATE_PENDING)
                new_neighbours.append(neighbour)

        if mines > 0:
            # set the number icon for this cell
            cell_state = ICONS[mines-1]
            cell.set_state(cell_state, self.icons[cell_state])
        return new_neighbours

    def get_grid_index_from_cell(self, cell) -> int:
        index = cell.get_column() + (cell.get_row() * self.grid_size) 
        return index       
    
    def reveal_all_mines(self):
        for cell in self.grid_list:
            if cell.is_mine_square() and cell.is_closed:
                cell.set_state(ICON_MINE, self.icons[ICON_MINE])
    
    def reset_cell_pending_state(self) -> None:
        for cell in self.grid_list:
            if cell.state_is_pending():
                cell.set_state(ICON_STATE_CLOSED)
