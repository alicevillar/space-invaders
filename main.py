import pygame
import random
import math
from pygame import mixer


#initialize pygame
pygame.get_init()
pygame.font.init()

# Music and sounds
pygame.mixer.init()
pygame.mixer.music.load('SweetMelodyArtlist.mp3')
pygame.mixer.music.play()
clock = pygame.time.Clock()

#creating a screen
screen = pygame.display.set_mode((853,632)) #width, height

# background main
background = pygame.image.load('img/main_background.png')

# background 2 => you win
background2 = pygame.image.load('img/cat_you_win.png')



# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/planet-earth.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('img/spaceship.png')
playerX= 370
playerY= 500
playerX_change = 0
bullet_state = "ready"

# Comets
cometImg = []
cometX = []
cometY = []
comentX_change = []
cometY_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
    cometImg.append(pygame.image.load("img/comet.png"))
    cometX.append(random.randint(0, 200))
    cometY.append(random.randint(40, 70))
    comentX_change.append(4)
    cometY_change.append(40)

# ETs
etImg  = []
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
bulletX= 0 #I'll change the value in the loop
bulletY= 0 # I'll change the value in the loop
bulletX_change = 0 #the bullet don't move in the x
bulletY_change = 10 #speed of the bullet

#Movement dynamics of our bulltet
bulletX_state ="ready"
#ready state = you can't see the bullet on the screen
#fire state = thebullet is in motion

# SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
testY = 10

# Game over
over_font = pygame.font.Font('freesansbold.ttf',64)

# Tick
TICK_VALUE = 90


# FUNCTIONS

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def you_win():
    screen.blit(background2, (0, 0))

def player(x,y):
    screen.blit(playerImg,(x,y)) #drawing the image in the window

def comets(x,y,i):
    screen.blit(cometImg[i], (x, y)) #drawing the image in the window

def ets(x,y,i):
    screen.blit(etImg[i], (x, y)) #drawing the image in the window

def fire_bullet(x,y): # the bulletX_state has to be a global variable so that the function can access it
    global bullet_state
    bullet_state = "fire"
    #draw the bullet on the screen
    screen.blit(bulletImg,(x+43,y+50))
    # it has to appearsin the center and top of the spaceship

#distance between two points by using the distance formula, which is an application of
# the Pythagorean theorem. We can rewrite the Pythagorean theorem as d=√((x2-x1)²+(y2-y1)²)
def isCollision(cometX, cometY, bulletX, bulletY):
    distance = math.sqrt(math.pow(cometX - bulletX,2) + (math.pow(cometY - bulletY,2))) #method for square root
    if distance < 27: #if distance if less than x pixels
        return True
    else:
        return False

# Game loop

running = True
while running:
    clock.tick(TICK_VALUE)
    # The screen has to be drawn on top of everything else
    screen.blit(background, (0,0))

    player(playerX,playerY) # We have to draw the player after the screen
    show_score(textX, testY) # We have to draw score player after the screen

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
            #print("key was pressed")
            if event.key == pygame.K_LEFT:
                playerX_change =- 3
            if event.key == pygame.K_RIGHT:
                playerX_change =+ 3

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
    elif playerX >= 750: #  width - width of the spaceship 853-140
        playerX = 750


    # YOU WIN & GAME OVER

    for i in range (num_of_enemies):
        if cometY[i] > 500:
            for i in range(num_of_enemies):
                cometY[i] = 520
            game_over_text()
            break

        if et_Y[i] > 500:
            for i in range(num_of_ets):
                et_Y[i] = 520
            game_over_text()
            break

        if score_value >= 30:
            you_win()
            playerImg = pygame.image.load('img/transp.png')
            bulletImg = pygame.image.load('img/transp.png')
            for i in range(num_of_ets):
                etImg[i] = pygame.image.load('img/transp.png')
            for i in range(num_of_enemies):
                cometImg[i] = pygame.image.load('img/transp.png')
            break

        cometX[i] += comentX_change[i]
        if cometX[i] <= -0:
            cometImg[i] = pygame.transform.flip(cometImg[i], True, False)
            comentX_change[i] = 5 #when hits the left it
            cometY[i] += cometY_change[i] #we simply increase the value of Y when it hits the bounday
        elif cometX[i] >= 780:  # width - width of the rocket
            cometImg[i] = pygame.transform.flip(cometImg[i], True, False)
            comentX_change[i] = -5
            cometY[i] += cometY_change[i] #we simply increase the value of Y when it hits the bounday

        # ROCK MOVEMENT

        # Creating boundaries for the enemy
        # tell the spaceship that hey: if your x coordinate reaches less that zero, make sure it turns back to zero because I don't want you to go beyond zero. Same thing if it goes to the right, beyond 800.
    for i in range(num_of_ets):
        # Game Over
        if et_Y[i] > 520:
            for j in range(num_of_ets):
                et_Y[j] = 2000
            game_over_text()
            break

        et_X[i] += et_X_change[i]
        if et_X[i] <= 0:
            etImg[i] = pygame.transform.flip(etImg[i], True, False)
            et_X_change[i] = 5  # when hits the left it
            et_Y[i] += et_Y_change[i]  # we simply increase the value of Y when it hits the bounday
        elif et_X[i] >= 800:
            etImg[i] = pygame.transform.flip(etImg[i], True, False)

            et_X_change[i] = -5
            et_Y[i] += et_Y_change[i]  # we simply increase the value of Y when it hits the bounday

        # Collision
        collision = isCollision(cometX[i], cometY[i], bulletX, bulletY)
        collision_2 = isCollision(et_X[i], et_Y[i], bulletX, bulletY)

        if collision ^ collision_2: # bitwise XOR (^)
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 500 #reset the bullet to the starting point
            bullet_state = "ready" #because the bullet is not being shown anymore, we have to change the value to ready
            score_value += 1 # increase the score
            cometX[i] = random.uniform(0, 735)  # default position to the enemy so when the game starts or it is killed, it reloads and comes back in random places / anywhere between 0 and 800
            cometY[i] = random.uniform(50, 150)  # min and max heigh
            et_X[i] = random.uniform(0, 735)  # default position to the enemy so when the game starts or it is killed, it reloads and comes back in random places / anywhere between 0 and 800
            et_Y[i] = random.uniform(30, 150)  # min and max heigh
            # Draw samples from a uniform distribution

        comets(cometX[i], cometY[i], i)
        ets(et_X[i], et_Y[i], i)

    # Bullet movement
    # I need to reset the bullet when it reaches the top of the screen, otherwise it will keep going forever and I won't be able to shoot another bullet
    if bulletY <= -80:
        bulletY = 500
        bullet_state = "ready"

        # After firering the bullet it must have it's own path and not follwo the spaceship

    if bullet_state is "fire": # We now move the bullet
        fire_bullet(bulletX,bulletY)   # Now decrease the value of the bullet so it goes up
        bulletY -= bulletY_change


    # to keep updating the game window that I'm working on
    pygame.display.update()


