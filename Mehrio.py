import pygame
import sys

from MarioCharacter import Mario
from Enemy import Enemy
import random

pygame.init()

MARIO_HEIGHT = 35
MARIO_WIDTH = 25

ENEMY_HEIGHT = 50
ENEMY_WIDTH = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

gameDisplayWidth = 800
gameDisplayHeight = 600

G = 0.1

gameDisplay = pygame.display.set_mode((gameDisplayWidth, gameDisplayHeight))
menuDisplay = pygame.display.set_mode((gameDisplayWidth, gameDisplayHeight))

backgroundImage = pygame.image.load('Dave Background.jpg')

pygame.display.set_caption('Mehrio')

gameExit = False

player_x = gameDisplayHeight / 2
player_y = gameDisplayWidth / 2

player_x_change = 0
player_y_change = 0

#Zach Walravens named this variable
scrolliness = 0

is_running = False

enemies = []

gameClock = pygame.time.Clock()

XmovementSpeed = 3
YmovementSpeed = 5
xPlayerSize = 10
yPlayerSize = 10

FPS = 60

flagsound = 0
soundstop = 0

i = 0
counter = 0

#Zach Walravens named this function
def memeAttackModeActivatedOneMemeOnTheRocksEsketit():
    enemies.append(Enemy(gameDisplay, gameDisplayWidth, gameDisplayHeight, ENEMY_WIDTH, ENEMY_HEIGHT,
                         random.randint(-100, 100), scrolliness, "Dab Emoji.png"))

def detectCollisions(thisEnemy):
    px = player_x
    py = player_y
    pw = xPlayerSize
    ph = yPlayerSize

    mx = thisEnemy.currentX
    my = thisEnemy.currentY
    mw = thisEnemy.width
    mh = thisEnemy.height

    if (px + pw > mx) and (px < mx + mw) and (py + ph > my) and (py < my + mh):

        print("player_x: " + str(px))
        print(str("player_y: ") + str(py))
        print(str("xPlayerSize: ") + str(pw))
        print(str("yPlayerSize: ") + str(ph))

        print(str("thisEnemy.currentX: ") + str(mx))
        print(str("thisEnemy.currentY: ") + str(my))
        print(str("thisEnemy.width: ") + str(mw))
        print(str("thisEnemy.height: ") + str(mh))

        pygame.quit()
        quit()

def soundplay():
    flagsound = 0
    pygame.mixer.init()
    pygame.mixer.music.load('MarioThemeSong.wav')

    pygame.mixer.music.play(-1)

    while pygame.mixer.music.get_busy() and flagsound < 1:
        flagsound = flagsound + 1
        print(flagsound)

def message_to_screen(title_message, color, display_font, x_location, y_location):
    font = pygame.font.SysFont(None, display_font)
    screen_message = font.render(title_message, True, color)
    gameDisplay.blit(screen_message, [x_location, y_location])

while not gameExit:
    counter += 1
    if counter % 10 == 0:
        i += 1

    if counter % 100/(100 + 100*counter) == 0:
        memeAttackModeActivatedOneMemeOnTheRocksEsketit()

    #makes gravity exist
    if player_y < gameDisplayHeight + MARIO_HEIGHT:
        player_y_change += G

    if player_y >= gameDisplayHeight - MARIO_HEIGHT:
        player_y_change = 0
        player_y = gameDisplayHeight - MARIO_HEIGHT

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        # using "elif" over "if" uses less processing power. May want to check if having syntax errors

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player_y_change == 0:
                    player_y_change = -YmovementSpeed
            if event.key == pygame.K_DOWN:
                player_y_change = YmovementSpeed
            if event.key == pygame.K_LEFT:
                player_x_change = -XmovementSpeed
                is_running = True
            if event.key == pygame.K_RIGHT:
                player_x_change = XmovementSpeed
                is_running = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
                is_running = False

    if player_x <= 0:
        player_x += 5
        scrolliness += 5
        player_y += 0
    if player_x >= gameDisplayWidth - MARIO_WIDTH:
        player_x -= 5
        scrolliness -= 5
        player_y += 0
    if player_y <= 0:
        player_x += 0
        player_y += 5
    if player_y >= gameDisplayHeight:
        player_x += 0
        player_y -= 5

    #player_x += player_x_change
    scrolliness -= player_x_change
    player_y += player_y_change

    gameDisplay.fill(WHITE)
    MarioCharacter = Mario(gameDisplay, MARIO_WIDTH, MARIO_HEIGHT)

    backgroundImage = pygame.transform.scale(backgroundImage, (gameDisplayWidth, gameDisplayHeight))
    gameDisplay.blit(backgroundImage, pygame.Rect(scrolliness, 0, gameDisplayWidth, gameDisplayHeight))

    MarioCharacter.blitme(player_x, player_y, is_running, i)

    for each in enemies:
        each.blitme(scrolliness)

    message_to_screen("Welcome to Mehrio", RED, 120, 15, 15)
    message_to_screen("Created By Noah Arias and Edgar Mateos-Chavez", BLACK, 15, 15, 100)
    message_to_screen("Special Thanks to Michael Acquistapace for being himself", BLACK, 15, 15, 145)

    pygame.display.update()

    gameClock.tick(FPS)
    if soundstop < 1:
        soundplay()
        soundstop = soundstop + 1

    for each in enemies:
        detectCollisions(each)

pygame.quit()
quit()