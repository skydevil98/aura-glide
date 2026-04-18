# particles.py
import pygame
import random
from src.settings import *

class Particle:
    def __init__(self, x, y, color=PARTICLE_COLOR, speed_x=0, speed_y=0, shrink_rate=0.1, radius=4):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = speed_x + random.uniform(-1, 1)
        self.speed_y = speed_y + random.uniform(-1, 1)
        self.radius = radius
        self.shrink_rate = shrink_rate

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.radius -= self.shrink_rate

    def draw(self, surface):
        if self.radius > 0:
            # Prevent value errors with alpha or draw circle arguments
            r = max(1, int(self.radius))
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), r)

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def emit_trail(self, x, y, color):
        self.particles.append(Particle(x, y, color=color, speed_x=-1.5, speed_y=random.uniform(-0.5, 0.5), shrink_rate=0.3, radius=5))

    def emit_explosion(self, x, y, color, count=20):
        for _ in range(count):
            speed_x = random.uniform(-5, 5)
            speed_y = random.uniform(-5, 5)
            self.particles.append(Particle(x, y, color=color, speed_x=speed_x, speed_y=speed_y, shrink_rate=0.15, radius=random.uniform(4, 8)))

    def update(self):
        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if p.radius > 0]

    def draw(self, surface):
        for p in self.particles:
            p.draw(surface)
