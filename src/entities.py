# entities.py
import pygame
import random
from src.settings import *

class Player:
    def __init__(self):
        self.radius = 15
        self.x = WIDTH // 3
        self.y = HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        if self.velocity > MAX_FALL_SPEED:
            self.velocity = MAX_FALL_SPEED
        self.y += self.velocity
        self.rect.centery = int(self.y)

    def draw(self, surface):
        # Glow outer effect
        glow_surf = pygame.Surface((self.radius*4, self.radius*4), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (*PLAYER_COLOR, 80), (self.radius*2, self.radius*2), self.radius + 6)
        surface.blit(glow_surf, (self.x - self.radius*2, self.y - self.radius*2))
        
        # Hard core
        pygame.draw.circle(surface, PLAYER_COLOR, (int(self.x), int(self.y)), self.radius)
        # White inner gleam
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x - 3), int(self.y - 3)), 4)

class Obstacle:
    def __init__(self, x):
        self.x = float(x)
        self.width = OBSTACLE_WIDTH
        self.passed = False
        
        min_y = 150
        max_y = HEIGHT - 150 - GAP_SIZE
        self.gap_y = random.randint(min_y, max_y)

        self.top_rect = pygame.Rect(int(self.x), 0, self.width, self.gap_y)
        self.bottom_rect = pygame.Rect(int(self.x), self.gap_y + GAP_SIZE, self.width, HEIGHT - (self.gap_y + GAP_SIZE))

    def update(self):
        self.x -= OBSTACLE_SPEED
        self.top_rect.x = int(self.x)
        self.bottom_rect.x = int(self.x)

    def draw(self, surface):
        # Ensure we only use valid border radius options for pygame.draw.rect
        try:
            # Rounded bottom for top pipe
            pygame.draw.rect(surface, OBSTACLE_COLOR, self.top_rect, border_bottom_left_radius=12, border_bottom_right_radius=12)
            pygame.draw.rect(surface, (255, 255, 255, 100), self.top_rect, width=2, border_bottom_left_radius=12, border_bottom_right_radius=12)
            
            # Rounded top for bottom pipe
            pygame.draw.rect(surface, OBSTACLE_COLOR, self.bottom_rect, border_top_left_radius=12, border_top_right_radius=12)
            pygame.draw.rect(surface, (255, 255, 255, 100), self.bottom_rect, width=2, border_top_left_radius=12, border_top_right_radius=12)
        except TypeError:
             # Fallback if pygame version is old
             pygame.draw.rect(surface, OBSTACLE_COLOR, self.top_rect)
             pygame.draw.rect(surface, OBSTACLE_COLOR, self.bottom_rect)
