import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class that represents a single alien"""
    
    def __init__(self, ai_game):
        """Inicialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('D:/OneDrive - Universidad Politécnica de Madrid/Aa Universidad/4.1. Python/Python Crash Course/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        
        
    def update(self):
        """"Update alien movements"""
        # Move the alien to the right.
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        """Return True if alien is at edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    