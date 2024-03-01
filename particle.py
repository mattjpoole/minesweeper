import pygame
import random

# Particle class
class Particle:

    def __init__(self, x, y, randcol):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-2, 0)
        self.lifetime = 60
        self.red = 255
        self.green = 255
        self.blue = 255
        self.radius = 2 

    def update(self):
        self.lifetime -= 1

    def draw(self, window):
        color = (int(self.red), int(self.green), int(self.blue))
        position = (int(self.x), int(self.y))
        pygame.draw.circle(window, color, position, self.radius)

class ConfettiParticle(Particle):
    
    def __init__(self, x, y, randcol):
        Particle.__init__(self, x, y, randcol)
        self.gravity = 0.05
        self.randcol = randcol
        """
        1 = yellow to red
        2 = cyan to blue
        3 = yellow to green
        """
        if randcol == 1:
            self.red = 255
            self.green = 255
            self.blue = 0
        elif randcol == 2:
            self.red = 0
            self.green = 255
            self.blue = 255
        elif randcol == 3:
            self.red = 255
            self.green = 255
            self.blue = 0
        self.fade = int(255 / self.lifetime)

    def update(self):
        Particle.update(self)
        self.x += self.dx
        self.dy += self.gravity
        self.y += self.dy 
        self.radius += 0.05

        if self.randcol == 1:
            self.red = self.red
            self.green -= self.fade
            self.blue = self.blue
        elif self.randcol == 2:
            self.red = self.red
            self.green -= self.fade
            self.blue = self.blue
        elif self.randcol == 3:
            self.red -= self.fade
            self.green = self.green
            self.blue = self.blue

class SmokeParticle(Particle):

    def __init__(self, x, y, randcol=None):
        super().__init__(x, y, randcol)
        self.lifetime = random.randrange(70, 180)
        self.dx = random.uniform(-1, 1)
        self.dy = -1
        self.frame_change = 10
        self.current_frame = 1


    def update(self):
        super().update()
        if self.current_frame % 3 == 0:
            self.radius += 0.1
            if self.current_frame % self.frame_change == 0:
                self.dx = -self.dx
            if self.current_frame >= 10:
                self.red = 255
                self.green = 255
                self.blue = 0
            if self.current_frame >= 20:
                self.red = 255
                self.green = 165
                self.blue = 0
            if self.current_frame >= 30:
                self.red = 128
                self.green = 128
                self.blue = 128
            if self.current_frame >= 100:
                self.red = 90
                self.green = 90
                self.blue = 90
            if self.current_frame >= 150:
                self.red = 50
                self.green = 50
                self.blue = 50
            self.x += self.dx
            self.y += self.dy
        self.current_frame += 1 


# Particle system class
class ParticleSystem:

    def __init__(self):
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def update(self):
        for particle in self.particles:
            particle.update()

            if particle.lifetime <= 0:
                self.particles.remove(particle)

    def draw(self, window):
        for particle in self.particles:
            particle.draw(window)