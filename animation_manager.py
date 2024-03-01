import random
import pygame
from particle import ParticleSystem, ConfettiParticle, SmokeParticle
from config import GAME_STATE_GAMEOVER, GAME_STATE_WIN

class AnimationManager:

    def __init__(self) -> None:
        self.ps = ParticleSystem()
        self.cell_locations = []
        self.animation_ended = False
        self.started = False
        self.confetti_delay = 100
        self.smoke_duration = 3000
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

    def render(self, game_state) -> None:    
        if game_state == GAME_STATE_WIN:
            self.render_confetti()
        elif game_state == GAME_STATE_GAMEOVER:
            self.render_smoke()
        self.ps.update()
        self.ps.draw(pygame.display.get_surface())

    def render_confetti(self) -> None:
        ticks = pygame.time.get_ticks()
        if self.current_cell < len(self.cell_locations):
            if ticks - self.timer > self.confetti_delay:
                self.timer = ticks
                rect = self.cell_locations[self.current_cell].get_rect()
                px = rect.centerx
                py = rect.centery   
                i = 0
                mparts = 30
                while i < mparts:
                    self.ps.add_particle(ConfettiParticle(px, py, random.randrange(1, 4)))
                    i += 1   
                self.current_cell += 1
        elif len(self.ps.particles) == 0:
            self.animation_ended = True
            self.current_cell = 0
    
    def render_smoke(self) -> None:
        ticks = pygame.time.get_ticks()
        if ticks - self.timer < self.smoke_duration:
            for cell in self.cell_locations:
                if cell.exploded:
                    rect = cell.get_rect()
                    px = rect.centerx
                    py = rect.centery
                    self.ps.add_particle(SmokeParticle(px, py))
                    break
        else:
            self.ps.particles.clear()
            self.animation_ended = True