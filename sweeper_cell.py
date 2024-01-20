import pygame

class SweeperCell():

    def __init__(self, rect, colour, has_mine=False) -> None:
        self.rect = rect
        self.colour = colour
        self.has_mine = has_mine

    def get_rect(self) -> pygame.Rect:
        return self.rect
    
    def get_colour(self):
        return self.colour
    
    def is_mine_square(self) -> bool:
        return self.has_mine