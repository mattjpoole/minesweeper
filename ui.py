import pygame
from config import *

class UIControls():

    def __init__(self) -> None:
        pass

    def initialise(self) -> None:
        screen = pygame.display.get_surface()
        width = pygame.display.get_window_size()[0]
        rect = pygame.draw.rect(screen, UI_BG_COLOUR, [0, 0, width, UI_HEIGHT])

    def render(self) -> None:
        pass