import pygame
from particle import ParticleSystem

class AnimationManager:

    def __init__(self) -> None:
        self.ps = ParticleSystem()
        self.cell_locations = []
        self.animation_ended = False
        self.started = False
        self.particle_delay = 100
        self.current_cell = 0
        self.timer = None

    def set_cell_locations(self, cell_locations) -> None:
        self.cell_locations = cell_locations

    def animation_has_ended(self) -> bool:
        return self.animation_ended
    
    def start(self) -> None:
        self.timer = pygame.time.get_ticks()
        self.animation_ended = False
        self.started = True

    def stop(self) -> None:
        self.animation_ended = False
        self.started = False

    def render(self) -> None:
        if self.current_cell < len(self.cell_locations):
            ticks = pygame.time.get_ticks()
            if ticks - self.timer > self.particle_delay:
                self.timer = ticks
                rect = self.cell_locations[self.current_cell].get_rect()
                px = rect.centerx
                py = rect.centery
                i = 0
                mparts = 30
                while i < mparts:
                    self.ps.add_particle(px, py)
                    i += 1 
                self.current_cell += 1
        elif len(self.ps.particles) == 0:
                self.animation_ended = True
                self.current_cell = 0
        self.ps.update()
        self.ps.draw(pygame.display.get_surface())

