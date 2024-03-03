class Settings:
    """Class managing game configuration"""

    def __init__(self) -> None:
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # Easy way to change game speed
        self.speedup_scale = 1.1

        # Easy way to change points for each alien hit
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializing dynamic settings in the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # Value 1 in fleet_direction means 'right', -1 means 'left'
        self.fleet_direction = 1

        # Score
        self.alien_points = 50

    def increase_speed(self):
        """Change game speed and score values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
