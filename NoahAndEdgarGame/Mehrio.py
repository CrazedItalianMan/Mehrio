import pygame
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

gameDisplayWidth = 800
gameDisplayHeight = 600

gameDisplay = pygame.display.set_mode((gameDisplayWidth, gameDisplayHeight))

pygame.display.set_caption('Mehrio')

gameExit = False

player_x = gameDisplayHeight / 2
player_y = gameDisplayWidth / 2

player_x_change = 0
player_y_change = 0

gameClock = pygame.time.Clock()

movementSpeed = 3
xPlayerSize = 10
yPlayerSize = 10

FPS = 60

flagsound = 0
soundstop = 0


def soundplay():
    flagsound = 0
    pygame.mixer.init()
    pygame.mixer.music.load('MarioThemeSong.wav')

    pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy() and flagsound < 100:
        flagsound = flagsound + 1
        print(flagsound)
        #print("Playing", pygame.mixer.music.get_pos())


def message_to_screen(title_message, color, display_font, x_location, y_location):
    font = pygame.font.SysFont(None, display_font)
    screen_message = font.render(title_message, True, color)
    gameDisplay.blit(screen_message, [x_location, y_location])


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        # using "elif" over "if" uses less processing power. May want to check if having syntax errors
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

    if player_x <= 0:
        player_x += 5
        player_y += 0
    if player_x >= 790:
        player_x -= 5
        player_y += 0
    if player_y <= 0:
        player_x += 0
        player_y += 5
    if player_y >= 590:
        player_x += 0
        player_y -= 5

    player_x += player_x_change
    player_y += player_y_change

    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay, BLACK, [player_x, player_y, xPlayerSize, yPlayerSize])
    message_to_screen("Welcome to Mehrio", RED, 120, 15, 15)
    message_to_screen("Created By Noah Arias and Edgar Mateos-Chavez", BLACK, 15, 15, 100)
    message_to_screen("Special Thanks to Michael Acquistapace for being himself", BLACK, 15, 15, 115)

    pygame.display.update()

    gameClock.tick(FPS)
    if soundstop < 1:
        soundplay()
        soundstop = soundstop + 1
pygame.quit()
quit()
