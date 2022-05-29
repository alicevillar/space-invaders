''' Space Invaders Game'''
# Standard Lib
import random
import math
# Thirdparty Lib
import pygame
from pygame import mixer

# initialize pygame
pygame.get_init()
pygame.font.init()

# Music and sounds
pygame.mixer.init()
pygame.mixer.music.load('SweetMelodyArtlist.mp3')
pygame.mixer.music.play()
clock = pygame.time.Clock()

# creating a screen
screen = pygame.display.set_mode((853, 632))  # width, height

# background main
background = pygame.image.load('img/main_background.png')

# background 2 => you win
background2 = pygame.image.load('img/cat_you_win.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/planet-earth.png')
pygame.display.set_icon(icon)

# Player
PLAYER_IMG = pygame.image.load('img/spaceship.png')
PLAYER_X = 370
PLAYER_Y = 500
PLAYER_X_CHANGE = 0
BULLET_STATE = "ready"

# Comets
COMMET_IMG = []
COMMET_X = []
COMMET_Y = []
COMMET_X_CHANGE = []
COMMET_Y_CHANGE = []
NUM_ENEMIES = 4

for i in range(NUM_ENEMIES):
    COMMET_IMG.append(pygame.image.load("img/comet.png"))
    COMMET_X.append(random.randint(0, 200))
    COMMET_Y.append(random.randint(40, 70))
    COMMET_X_CHANGE.append(4)
    COMMET_Y_CHANGE.append(40)

# ETs
etImg = []
et_X = []
et_Y = []
et_X_change = []
et_Y_change = []
num_of_ets = 4

for r in range(num_of_ets):
    etImg.append(pygame.image.load("img/et.png"))
    et_X.append(random.randint(0, 200))
    et_Y.append(random.randint(40, 70))
    et_X_change.append(4)
    et_Y_change.append(40)

# Bullet
# ready = you can't see the bullet on the scree
# fire = the bullet is moving

bulletImg = pygame.image.load('img/bullet.png')
BULLET_X = 0  # I'll change the value in the loop
BULLET_Y = 0  # I'll change the value in the loop
BULLET_X_change = 0  # the bullet don't move in the x
BULLET_Y_change = 10  # speed of the bullet

# Movement dynamics of our bulltet
BULLET_X_state = "ready"
# ready state = you can't see the bullet on the screen
# fire state = thebullet is in motion

# SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

TEXT_X = 10
TEXT_Y = 10

# Game over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Tick
TICK_VALUE = 90


# FUNCTIONS

def show_score(parameter_x, y_parameter):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (parameter_x, y_parameter))


def game_over_teparameter_xt():
    ''' drawing the image in the window '''
    over_teparameter_xt = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_teparameter_xt, (200, 250))


def you_win():
    ''' drawing the image in the window '''
    screen.blit(background2, (0, 0))


def player(parameter_x, y_parameter):
    ''' drawing the image in the window '''
    screen.blit(PLAYER_IMG, (parameter_x, y_parameter))


def comets(parameter_x, y_parameter, i_parameter):
    ''' drawing the image in the window '''
    screen.blit(COMMET_IMG[i_parameter], (parameter_x, y_parameter))


def ets(parameter_x, y_parameter, m_parameter):
    ''' drawing the image in the window '''
    screen.blit(etImg[m_parameter], (parameter_x, y_parameter))


def fire_bullet(parameter_x, y_parameter):
    ''' the BULLET_parameter_x_state has to be a global'''
    global BULLET_STATE
    BULLET_STATE = "fire"
    # draw the bullet on the screen
    screen.blit(bulletImg, (parameter_x+43, y_parameter+50))
    # it has to appearsin the center and top of the spaceship

# distance between two points by using the distance formula
# the Pythagorean theorem. Pythagorean theorem as d=√((x2-x1)²+(y2-y1)²)


def is_collision(COMMET_X, COMMET_Y, BULLET_X, BULLET_Y):
    distance = math.sqrt(math.pow(COMMET_X - BULLET_X, 2) +
                         (math.pow(COMMET_Y - BULLET_Y, 2)))  # square root
    if distance < 27:  # if distance if less than x pixels
        return True
    return False

# Game loop
RUNNING = True

while RUNNING:
    clock.tick(TICK_VALUE)
    # The screen has to be drawn on top of everything else
    screen.blit(background, (0, 0))

    player(PLAYER_X, PLAYER_Y)  # We have to draw the player after the screen
    show_score(TEXT_X, TEXT_Y)  # We have to draw score player after the screen

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        # If keystroke is pressed, check whether it is right or left:
        if event.type == pygame.KEYDOWN:  # a key has been pressed
            #print("key was pressed")
            if event.key == pygame.K_LEFT:
                PLAYER_X_CHANGE = - 3
            if event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE = + 3

            # the bullet
            if event.key == pygame.K_SPACE:
                # we can only fire a bullet if the state is ready:
                if BULLET_STATE is "ready":  # you can't see the bullet anymore
                    bulletSound = mixer.Sound("laser.flac")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    BULLET_X = PLAYER_X
                    fire_bullet(PLAYER_X, BULLET_Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE = 0

    PLAYER_X += PLAYER_X_CHANGE
    # Creating boundaries for the player # tell the spaceship that hey:
    # if your x coordinate reaches less that zero, make sure it turns back
    # to zero because I don't want you to go beyond zero.
    # Same thing if it goes to the right, beyond 800.
    if PLAYER_X <= 0:
        PLAYER_X = 0
    elif PLAYER_X >= 750:  # width - width of the spaceship 853-140
        PLAYER_X = 750

    # YOU WIN & GAME OVER

    for i in range(NUM_ENEMIES):
        if COMMET_Y[i] > 500:
            for G in range(NUM_ENEMIES):
                COMMET_Y[G] = 520

            break

        if et_Y[i] > 500:
            for V in range(num_of_ets):
                et_Y[V] = 520

            break

        if score_value >= 30:
            you_win()
            PLAYER_IMG = pygame.image.load('img/transp.png')
            bulletImg = pygame.image.load('img/transp.png')
            for K in range(num_of_ets):
                etImg[K] = pygame.image.load('img/transp.png')
            for J in range(NUM_ENEMIES):
                COMMET_IMG[J] = pygame.image.load('img/transp.png')
            break

        COMMET_X[i] += COMMET_X_CHANGE[i]
        if COMMET_X[i] <= -0:
            COMMET_IMG[i] = pygame.transform.flip(COMMET_IMG[i], True, False)
            COMMET_X_CHANGE[i] = 5  # when hits the left it
            # we simply increase the value of Y when it hits the bounday
            COMMET_Y[i] += COMMET_Y_CHANGE[i]
        elif COMMET_X[i] >= 780:  # width - width of the rocket
            COMMET_IMG[i] = pygame.transform.flip(COMMET_IMG[i], True, False)
            COMMET_X_CHANGE[i] = -5
            # we simply increase the value of Y when it hits the bounday
            COMMET_Y[i] += COMMET_Y_CHANGE[i]

        # ROCK MOVEMENT

        # Creating boundaries for the enemy
        # tell the spaceship that hey: if your x coordinate reaches less that zero,
        # make sure it turns back to zero because I don't want you to go beyond zero.
        # Same thing if it goes to the right, beyond 800.
    for i in range(num_of_ets):
        # Game Over
        if et_Y[i] > 520:
            for j in range(num_of_ets):
                et_Y[j] = 2000
            break

        et_X[i] += et_X_change[i]
        if et_X[i] <= 0:
            etImg[i] = pygame.transform.flip(etImg[i], True, False)
            et_X_change[i] = 5  # when hits the left it
            # we simply increase the value of Y when it hits the bounday
            et_Y[i] += et_Y_change[i]
        elif et_X[i] >= 800:
            etImg[i] = pygame.transform.flip(etImg[i], True, False)

            et_X_change[i] = -5
            # we simply increase the value of Y when it hits the bounday
            et_Y[i] += et_Y_change[i]

        # COLLISION
        COLLISION = is_collision(COMMET_X[i], COMMET_Y[i], BULLET_X, BULLET_Y)
        COLLISION_2 = is_collision(et_X[i], et_Y[i], BULLET_X, BULLET_Y)

        if COLLISION ^ COLLISION_2:  # bitwise XOR (^)
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            BULLET_Y = 500  # reset the bullet to the starting point
            # because the bullet is not being shown anymore,
            # we have to change the value to ready
            BULLET_STATE = "ready"
            score_value += 1  # increase the score
            # default position to the enemy so when the game starts or it is killed,
            # it reloads and comes back in random places / anywhere between 0 and 800
            COMMET_X[i] = random.uniform(0, 735)
            COMMET_Y[i] = random.uniform(50, 150)  # min and max heigh
            # default position to the enemy so when the game starts or it is killed,
            # it reloads and comes back in random places / anywhere between 0 and 800
            et_X[i] = random.uniform(0, 735)
            et_Y[i] = random.uniform(30, 150)  # min and max heigh
            # Draw samples from a uniform distribution

        comets(COMMET_X[i], COMMET_Y[i], i)
        ets(et_X[i], et_Y[i], i)

    # Bullet movement
    # I need to reset the bullet when it reaches the top of the screen,
    # otherwise it will keep going forever and I won't be able to shoot another bullet
    if BULLET_Y <= -80:
        BULLET_Y = 500
        BULLET_STATE = "ready"

    # After firering the bullet it must have it's own path and not follwo the spaceship

    if BULLET_STATE is "fire":  # We now move the bullet
        # Now decrease the value of the bullet so it goes up
        fire_bullet(BULLET_X, BULLET_Y)
        BULLET_Y -= BULLET_Y_change

    # to keep updating the game window that I'm working on
    pygame.display.update()
