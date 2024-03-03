class GameStats:
    """Monitor game stats"""

    def __init__(self, ai_game):
        """Initialize game stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize games stats that can change in the course of the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
