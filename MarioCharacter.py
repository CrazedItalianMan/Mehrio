import pygame
import sys

class Mario():

    def __init__(self, gameDisplay, width, height):
        """Initializing Mario and setting his starting position"""
        self.gameDisplay = gameDisplay

    #Now loading Mario and getting his rectangular area/hitbox
        self.image1 = pygame.image.load('WhiteArmyMario.jpg')
        self.image1 = pygame.transform.scale(self.image1, (width, height))
        self.rect1 = self.image1.get_rect()

        self.image2 = pygame.image.load('WhiteArmyMario2.jpg')
        self.image2 = pygame.transform.scale(self.image2, (width, height))
        self.rect2 = self.image2.get_rect()

        self.image3 = pygame.image.load('WhiteArmyMario3.jpg')
        self.image3 = pygame.transform.scale(self.image3, (width, height))
        self.rect3 = self.image3.get_rect()

        self.gameDisplay_rect = gameDisplay.get_rect()

    #Start Mario at the left hand side
    def blitme(self, currentX, currentY, is_moving, position):
        """Now rendering Mario and displaying him to gameDisplay"""
        self.rect1.x = currentX
        self.rect1.y = currentY
        self.rect2.x = currentX
        self.rect2.y = currentY
        self.rect3.x = currentX
        self.rect3.y = currentY

        if not is_moving:
            self.gameDisplay.blit(self.image1, self.rect1)
        else:
            if position % 3 == 0:
                self.gameDisplay.blit(self.image1, self.rect1)
            if position % 3 == 1:
                self.gameDisplay.blit(self.image2, self.rect2)
            if position % 3 == 2:
                self.gameDisplay.blit(self.image3, self.rect3)
