import pygame.font


class Button:
    """Class creating buttons for the game"""

    def __init__(self, ai_game, msg):
        """Initialize button's attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Define button size, attributes
        self.width, self.height = 200, 60
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Arial", 48)

        # Create button rectangle and justify it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare msg that will be placed in the button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Place msg inside the button and center it"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Show empty button and then msg on it
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
