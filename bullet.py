from typing import Any
import pygame
from pygame.sprite import Group, Sprite


class Bullet(Sprite):
    """Class responsible for managing ship's bullet"""

    def __init__(self, ai_game) -> None:
        # Creating bullet object in ship's position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creating bullet's rectangle in (0,0)
        # Then finding its current position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet position is defined as floating number
        self.y = float(self.rect.y)

    def update(self):
        """Moving bullet"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Display bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
