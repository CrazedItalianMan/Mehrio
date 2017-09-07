import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

gameDisplayWidth = 800
gameDisplayHeight = 600

gameDisplay = pygame.display.set_mode((gameDisplayWidth,gameDisplayHeight))

pygame.display.set_caption('Mehrio')

gameExit = False

player_x = gameDisplayHeight/2
player_y = gameDisplayWidth/2

player_x_change = 0
player_y_change = 0

gameClock = pygame.time.Clock()

movementSpeed = 3
xPlayerSize = 10
yPlayerSize = 10

FPS = 60

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
#using "elif" over "if" uses less processing power. May want to check if having syntax errors
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y_change = -movementSpeed
            elif event.key == pygame.K_DOWN:
                player_y_change = movementSpeed
            elif event.key == pygame.K_LEFT:
                player_x_change = -movementSpeed
            elif event.key == pygame.K_RIGHT:
                player_x_change = movementSpeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    if player_x >= gameDisplayWidth or player_x <= 0 or player_y >= gameDisplayHeight or player_y <= 0:
        player_x_change = 0
        player_y_change = 0

    player_x += player_x_change
    player_y += player_y_change

    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay, BLACK, [player_x, player_y, xPlayerSize, yPlayerSize])

    pygame.display.update()

    gameClock.tick(FPS)

pygame.quit()
quit()