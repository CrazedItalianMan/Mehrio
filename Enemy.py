import pygame
import random

class Enemy():

    gameDisplay = "potato"
    width = "potato"
    height = "potato"
    moveSpeed = "potato"
    startX = "potato"
    currentX = "potato"
    currentY = "potato"
    image1 = "potato"
    rect1 = "potato"

    def __init__(self, gameDisplay, gameDisplayWidth, gameDisplayHeight, width, height, moveSpeed, startScrolliness, fileName):
        """Initializing Mario and setting his starting position"""
        self.gameDisplay = gameDisplay
        self.width = width
        self.height = height
        self.moveSpeed = moveSpeed
        if random.random() < 0.5:
            self.startX = 0 - startScrolliness
        else:
            self.startX = gameDisplayWidth - startScrolliness

        self.currentX = self.startX
        self.currentY = gameDisplayHeight - self.height

        self.image1 = pygame.image.load(fileName)
        self.image1 = pygame.transform.scale(self.image1, (self.width, self.height))
        self.rect1 = self.image1.get_rect()

        self.gameDisplay_rect = gameDisplay.get_rect()

    # Start Mario at the left hand side
    def blitme(self, scrolliness):
        self.currentX -= self.moveSpeed * 0.1
        self.rect1.x = self.currentX + scrolliness
        self.rect1.y = self.currentY

        print(str(self.rect1.x) + " , " + str(self.rect1.y))

        self.gameDisplay.blit(self.image1, self.rect1)