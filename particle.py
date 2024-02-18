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
        self.radius = 2
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
        self.x += self.dx
        self.dy += self.gravity
        self.y += self.dy 
        self.lifetime -= 1
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

    def draw(self, window):
        color = (int(self.red), int(self.green), int(self.blue))
        position = (int(self.x), int(self.y))
        pygame.draw.circle(window, color, position, self.radius)

# Particle system class
class ParticleSystem:

    def __init__(self):
        self.particles = []

    def add_particle(self, x, y):
        self.particles.append(Particle(x, y, random.randrange(1, 4)))

    def update(self):
        for particle in self.particles:
            particle.update()

            if particle.lifetime <= 0:
                self.particles.remove(particle)

    def draw(self, window):
        for particle in self.particles:
            particle.draw(window)