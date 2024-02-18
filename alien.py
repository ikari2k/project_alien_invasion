import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """Class managing single alien from the fleet"""

    def __init__(self, ai_game):
        """Alien object initialization and defining its initial position"""
        super().__init__()
        self.screen = ai_game.screen

        # Loading alien image and defining its rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Place new alien objects in upper left screen corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing alien position
        self.x = float(self.rect.x)
