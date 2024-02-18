import pygame


class Ship:
    """Class managing ship behavior"""

    def __init__(self, ai_game) -> None:
        """Ship initialization and its initial position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loading ship's image and its rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Every new ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Ship location stored as floating number
        self.x = float(self.rect.x)

        # Option to move right
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position based on movement options and ship's x
        position and not its rectangle"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update ship's position based on self.x
        self.rect.x = self.x

    def blitme(self):
        """Display ship in its current position"""
        self.screen.blit(self.image, self.rect)
