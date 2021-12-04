class GameStats:
    """Track statistics for ALien Invasion"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start ALien Invasion in an inactive state.
        self.game_active = False
        
        # High Score
        with open('D:/OneDrive - Universidad Politécnica de Madrid/Aa Universidad/4.1. Python/Python Crash Course/alien_invasion/scores/highscore.txt') as file_object:
            contents = file_object.read()
        self.high_score = int(contents)
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        