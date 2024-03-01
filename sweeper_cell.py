import pygame
from config import ICON_STATE_CLOSED, ICON_FLAG, ICON_STATE_EMPTY, ICON_STATE_OUTOFBOUNDS, CELL_BORDER_HOVER

class SweeperCell():

    def __init__(self, rect, colour, has_mine=False, state=ICON_STATE_CLOSED) -> None:
        self.rect = rect
        self.colour = colour
        self.has_mine = has_mine
        self.state = state
        self.icon = None
        self.size = None
        self.column = 0
        self.row = 0
        self.index = None
        self.num_mines = 0
        self.exploded = False

    def get_rect(self) -> pygame.Rect:
        return self.rect
    
    def get_colour(self):
        return self.colour
    
    def set_colour(self, colour) -> None:
        self.colour = colour
    
    def is_mine_square(self) -> bool:
        return self.has_mine
    
    def is_closed(self) -> bool:
        return self.state == ICON_STATE_CLOSED

    def is_empty(self) -> bool:
        return self.state == ICON_STATE_EMPTY

    def is_in_bounds(self) -> bool:
        return self.state != ICON_STATE_OUTOFBOUNDS
    
    def has_flag(self) -> bool:
        return self.state == ICON_FLAG
    
    def set_state(self, state, icon=None) -> None:
        self.state = state
        self.icon = icon

    def set_size(self, size:tuple) -> None:
        self.size = size

    def set_num_mines(self, num) -> None:
        self.num_mines = num
    
    def get_num_mines(self) -> int:
        return self.num_mines
    
    def set_grid_index(self, index) -> None:
        self.index = index
    
    def get_grid_index(self) -> int:
        return self.index

    def set_field_coords(self, column, row):
        self.column = column
        self.row = row

    def set_has_mine(self, has_mine) -> None:
        self.has_mine = has_mine
   
    def get_column(self)->int:
        return self.column
    
    def get_row(self)->int:
        return self.row
    
    def render(self, hoverEnabled) -> None:
        screen = pygame.display.get_surface()
        screen.fill(self.colour, self.rect)
        if hoverEnabled:
            if(self.rect.collidepoint(pygame.mouse.get_pos()) and self.is_closed() and not self.is_empty()):
                pygame.draw.rect(screen, CELL_BORDER_HOVER, self.rect, 2)
        if not self.is_closed() and not self.is_empty():
            screen.blit(
                pygame.transform.scale(self.icon, self.size), self.rect)
