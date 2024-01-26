import pygame
from config import ICON_STATE_CLOSED, ICON_FLAG, ICON_STATE_PENDING, ICON_STATE_EMPTY

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
    
    def state_is_pending(self) -> bool:
        return self.state == ICON_STATE_PENDING
    
    def has_flag(self) -> bool:
        return self.state == ICON_FLAG
    
    def set_state(self, state, icon=None) -> None:
        self.state = state
        self.icon = icon

    def set_size(self, size:tuple) -> None:
        self.size = size

    def set_field_coords(self, column, row):
        self.column = column
        self.row = row
   
    def get_column(self)->int:
        return self.column
    
    def get_row(self)->int:
        return self.row
    
    def render(self) -> None:
        if not self.is_closed() and not self.is_empty():
            pygame.display.get_surface().blit(
                pygame.transform.scale(self.icon, self.size), self.rect)
