# ui.py
import pygame
from settings import *

def draw_panel(surface, rect, radius, alpha=150):
    """Draws a glassmorphism style rounded panel."""
    # Ensure rect is a pygame.Rect
    if not isinstance(rect, pygame.Rect):
        rect = pygame.Rect(rect)
        
    panel = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(panel, (*PANEL_COLOR[:3], alpha), panel.get_rect(), border_radius=radius)
    # Highlight border for glass feel
    pygame.draw.rect(panel, (255, 255, 255, 50), panel.get_rect(), width=1, border_radius=radius)
    surface.blit(panel, rect.topleft)

class Button:
    def __init__(self, x, y, width, height, text, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.is_hovered = False

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def draw(self, surface):
        alpha = 220 if self.is_hovered else 150
        draw_panel(surface, self.rect, radius=12, alpha=alpha)
        
        text_surf = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

class TextRenderer:
    def __init__(self):
        pygame.font.init()
        # Fallback fonts
        try:
            self.title_font = pygame.font.SysFont('avenirnext, sans-serif', 64, bold=True)
            self.menu_font = pygame.font.SysFont('avenirnext, sans-serif', 32, bold=True)
            self.score_font = pygame.font.SysFont('avenirnext, sans-serif', 56, bold=True)
        except:
            self.title_font = pygame.font.Font(None, 64)
            self.menu_font = pygame.font.Font(None, 36)
            self.score_font = pygame.font.Font(None, 56)

    def draw_text(self, surface, text, font, pos, center=True, shadow=True):
        if shadow:
            shadow_surf = font.render(text, True, (0, 0, 0))
            shadow_offset_y = 3
            shadow_rect = shadow_surf.get_rect(center=(pos[0], pos[1]+shadow_offset_y)) if center else shadow_surf.get_rect(topleft=(pos[0], pos[1]+shadow_offset_y))
            surface.blit(shadow_surf, shadow_rect)

        text_surf = font.render(text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=pos) if center else text_surf.get_rect(topleft=pos)
        surface.blit(text_surf, text_rect)
