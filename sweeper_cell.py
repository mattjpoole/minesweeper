import pygame
from config import ICON_STATE_CLOSED

class SweeperCell():

    def __init__(self, rect, colour, has_mine=False, state=ICON_STATE_CLOSED) -> None:
        self.rect = rect
        self.colour = colour
        self.has_mine = has_mine
        self.state = state
        self.icon = None
        self.size = None

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
    
    def set_state(self, state, icon) -> None:
        self.state = state
        self.icon = icon

    def set_size(self, size:tuple) -> None:
        self.size = size
    
    def render(self) -> None:
        if not self.is_closed():
            pygame.display.get_surface().blit(
                pygame.transform.scale(self.icon, self.size), self.rect)
