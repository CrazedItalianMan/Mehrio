import pygame
import sys
from

class Mario():

    def __init__(self, gameDisplay):
        """Initializing Mario and setting his starting position"""
        self.gameDisplay = gameDisplay

    #Now loading Mario and getting his rectangular area/hitbox
        self.image = pygame.image.load('MarioStandingStillSprite.png')
        self.image = pyg
        self.rect = self.image.get_rect()
        self.gameDisplay_rect = gameDisplay.get_rect()

    #Start Mario at the left hand side

    def blitme(self):
        """Now rendering Mario and displaying him to gameDisplay"""
        self.gameDisplay.blit(self.image, self.rect)