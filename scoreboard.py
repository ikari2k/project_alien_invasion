import pygame.font


class Scoreboard:
    """Class used for showing info about score"""

    def __init__(self, ai_game):
        """Initialize attributes related to scores"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Set font for rendering scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("Arial", 48)

        # Prepare initial images with scores
        self.prep_score()

    def prep_score(self):
        """Turn score into generated image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Display score in upper right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Display score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
