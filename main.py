import pygame
import random
import math
from pygame import mixer

# LINHAS 20 A 24, 107 A 111, 210
#initialize pygame
pygame.get_init()
pygame.font.init()

# Music and sounds
pygame.mixer.init()
pygame.mixer.music.load('SweetMelodyArtlist.mp3')
pygame.mixer.music.play()
clock = pygame.time.Clock()

#creating a screen
screen = pygame.display.set_mode((800,519)) #width, height

# background main
background = pygame.image.load('img/main_background.png')

# background 2 => you won this round
background2 = pygame.image.load('img/you_won_this_round.png')

# background 3 => you win
background3 = pygame.image.load('img/you_win.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/planet-earth.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('img/spaceship.png')
playerX= 370
playerY= 440
playerX_change = 0
bullet_state = "ready"

# Comets
cometImg  = []
cometX = []
cometY = []
comentX_change = []
cometY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    cometImg.append(pygame.image.load("img/comet.png"))
    cometX.append(random.randint(0, 800))
    cometY.append(random.randint(40, 70))
    comentX_change.append(4)
    cometY_change.append(40)

# Rocks
rockImg  = []
rock_X = []
rock_Y = []
rock_X_change = []
rock_Y_change = []
num_of_rocks = 3

for r in range(num_of_rocks):
    rockImg.append(pygame.image.load("img/rock.png"))
    rock_X.append(random.randint(0,800))
    rock_Y.append(random.randint(40,70))
    rock_X_change.append(4)
    rock_Y_change.append(40)


# Bullet
# ready = you can't see the bullet on the scree
# fire = the bullet is moving

bulletImg = pygame.image.load('img/bullet.png')
bulletX= 0 #I'll change the value in the loop
bulletY= 480 # I'll change the value in the loop
bulletX_change = 0 #the bullet don't move in the x
bulletY_change = 10 #speed of the bullet

#Movement dynamics of our bulltet
bulletX_state ="ready"
#ready state = you can't see the bullet on the screen
#fire state = thebullet is in motion

# SUN
sun = pygame.image.load('img/sun.png')

# EARTH
earth = pygame.image.load('img/earth.png')

# SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
testY = 10

# Game over
over_font = pygame.font.Font('freesansbold.ttf',64)

# Tick
TICK_VALUE = 90

# ALL FUNCTIONS

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# TELAS PARA FINALIZAÇAO
def you_won_this_round_bg():
    screen.blit(background2, (0, 0))

def you_win_bg():
    screen.blit(background3, (0, 0))

def player(x,y):
    screen.blit(playerImg,(x,y)) #drawing the image in the window

def enemy(x,y,i):
    screen.blit(cometImg[i], (x, y)) #drawing the image in the window

def rocks(x,y,i):
    screen.blit(rockImg[i],(x,y)) #drawing the image in the window

def fire_bullet(x,y): # the bulletX_state has to be a global variable so that the function can access it
    global bullet_state
    bullet_state = "fire"
    #draw the bullet on the screen
    screen.blit(bulletImg,(x+16,y+10))
    # 16 so that it appears in the center of the spaceship
    #10 to give the illusion that it is being fired from the top of the spaceship


#distance between two points by using the distance formula, which is an application of
# the Pythagorean theorem. We can rewrite the Pythagorean theorem as d=√((x2-x1)²+(y2-y1)²)
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX,2) + (math.pow(enemyY - bulletY,2))) #method for square root
    if distance < 27: #if distance if less than 10 pixels
        return True
    else:
        return False


# Game loop
running = True
while True:
    clock.tick(TICK_VALUE)
    # The screen has to be drawn on top of everything else
    # screen.fill((0, 0, 0)) # RGB - Red/Green/Blue
    # background
    screen.blit(background, (0,0))
    screen.blit(sun, (650, 34))
    screen.blit(earth, (483, 130))


    # To get coordinates on the screen
    #for event in pygame.event.get():
        #if event.type == pygame.MOUSEBUTTONUP:
            #pos = pygame.mouse.get_pos()
            #print(pos)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed, check whether it is right or left:
        if event.type == pygame.KEYDOWN: # a key has been pressed
            print("key was pressed")
            if event.key == pygame.K_LEFT:
                playerX_change =- 5
            if event.key == pygame.K_RIGHT:
                playerX_change =+ 5

            # the bullet
            if event.key == pygame.K_SPACE:
                # we can only fire a bullet if the state is ready:
                if bullet_state is "ready": # you can't see the bullet anymore
                    bulletSound = mixer.Sound("laser.flac")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
        # Creating boundaries for the player # tell the spaceship that hey: if your x coordinate reaches less that zero, make sure it turns back to zero because I don't want you to go beyond zero. Same thing if it goes to the right, beyond 800.
    if playerX <=0:
        playerX = 0
    elif playerX >= 736: #736 pixels because the width of the spaceship is 64x64 pixels. 800-64=736 pixels
        playerX = 736

    #ENEMY MOVEMENT

    # Creating boundaries for the enemy
    # tell the spaceship that hey: if your x coordinate reaches less that zero, make sure it turns back to zero because I don't want you to go beyond zero. Same thing if it goes to the right, beyond 800.
    for i in range (num_of_enemies):

        # GAME OVER
        if cometY[i] > 440:
            for j in range(num_of_enemies):
                cometY[j] = 2000
            game_over_text()
            break

        if score_value >= 5:
            you_won_this_round_bg()
            break

        cometX[i] += comentX_change[i]
        if cometX[i] <= 0:
            cometImg[i] = pygame.transform.flip(cometImg[i], True, False)
            comentX_change[i] = 7 #when hits the left it
            cometY[i] += cometY_change[i] #we simply increase the value of Y when it hits the bounday
        elif cometX[i] >= 736:  # 736 pixels because the width of the spaceship is 32x32 pixels. 800-32=768 pixels
            cometImg[i] = pygame.transform.flip(cometImg[i], True, False)

            comentX_change[i] = -7
            cometY[i] += cometY_change[i] #we simply increase the value of Y when it hits the bounday

        # ROCK MOVEMENT

        # Creating boundaries for the enemy
        # tell the spaceship that hey: if your x coordinate reaches less that zero, make sure it turns back to zero because I don't want you to go beyond zero. Same thing if it goes to the right, beyond 800.
    for i in range(num_of_rocks):
        # Game Over
        if rock_Y[i] > 440:
            for j in range(num_of_rocks):
                rock_Y[j] = 2000
            game_over_text()
            break

        rock_X[i] += rock_X_change[i]
        if rock_X[i] <= 0:
            rockImg[i] = pygame.transform.flip(rockImg[i], True, False)
            rock_X_change[i] = 5  # when hits the left it
            rock_Y[i] += rock_Y_change[i]  # we simply increase the value of Y when it hits the bounday
        elif rock_X[i] >= 736:  # 736 pixels because the width of the spaceship is 32x32 pixels. 800-32=768 pixels
            rockImg[i] = pygame.transform.flip(rockImg[i], True, False)

            rock_X_change[i] = -5
            rock_Y[i] += rock_Y_change[i]  # we simply increase the value of Y when it hits the bounday

        # Collision
        collision = isCollision(cometX[i], cometY[i], bulletX, bulletY)
        collision_2 = isCollision(rock_X[i], rock_Y[i], bulletX, bulletY)


        if collision ^ collision_2: # bitwise XOR (^)
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 440 #reset the bullet to the starting point
            bullet_state = "ready" #because the bullet is not being shown anymore, we have to change the value to ready
            score_value += 1 # increase the score
            cometX[i] = random.randint(0, 735)  # default position to the enemy so when the game starts or it is killed, it reloads and comes back in random places / anywhere between 0 and 800
            cometY[i] = random.randint(50, 150)  # min and max heigh
            rock_X[i] = random.randint(0, 735)  # default position to the enemy so when the game starts or it is killed, it reloads and comes back in random places / anywhere between 0 and 800
            rock_Y[i] = random.randint(50, 150)  # min and max heigh


        enemy(cometX[i], cometY[i], i)
        rocks(rock_X[i], rock_Y[i], i)

    # Bullet movement
    # I need to reset the bullet when it reaches the top of the screen, otherwise it will keep going forever and I won't be able to shoot another bullet
    if bulletY <= 0:
        bulletY = 400
        bullet_state = "ready"

        # After firering the bullet it must have it's own path and not follwo the spaceship

    if bullet_state is "fire": #we now move the bullet
        fire_bullet(bulletX,bulletY)   #nwo decrease the value of the bullet so it goes up
        bulletY -= bulletY_change


    player(playerX,playerY) #we have to draw the player after the screen
    show_score(textX, testY)


    # to keep updating the game window that I'm working on
    pygame.display.update()


