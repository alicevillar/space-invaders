import pygame
import random
import math
from pygame import mixer

#initialize pygame
pygame.get_init()

#creating a screen
screen = pygame.display.set_mode((800,519)) #width, height

# background
background = pygame.image.load('img/SPACE INVADERS GAME-11.png')

# Music and sounds

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

# Enemy
enemyImg = pygame.image.load('img/spaceship.png')
enemyX= 370
enemyY= 440
enemyX_change = 0


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

# SCORE
score_value = 0
font = pygame.font.Font('freesandbold.ttf',32)

textX = 10
testY = 10

# Game over
over_font = pygame.font.Font('freesandbold.ttf',64)



# ALL FUNCTIONS

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x,y):
    screen.blit(playerImg,(x,y)) #drawing the image in the window

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y)) #drawing the image in the window

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
    if distance < 27: #if distance if less than 27 pixels
        return True
    else:
        return False


# Game loop
running = True
while True:
    # The screen has to be drawn on top of everything else
    # screen.fill((0, 0, 0)) # RGB - Red/Green/Blue
    # background
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed, check whether it is right or left:
        if event.type == pygame.KEYDOWN: #a key has been pressed
            print("key was pressed")
            if event.key == pygame.K_LEFT:
                playerX_change =- 5
            if event.key == pygame.K_RIGHT:
                playerX_change =+ 5

            # the bullet
            if event.key == pygame.K_SPACE:
                # we can only fire a bullet if the state is ready:
                if bullet_state is "ready": # you can't see the bullet anymore
                    bulletSound = mixer.Sound("laser.wav")
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
        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4 #when hits the left it
            enemyY[i] += enemyY_change[i] #we simply increase the value of Y when it hits the bounday
        elif enemyX[i] >= 768:  # 736 pixels because the width of the spaceship is 32x32 pixels. 800-32=768 pixels
            enemyX_change = -4
            enemyY[i] += enemyY_change[i] #we simply increase the value of Y when it hits the bounday

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 440 #reset the bullet to the starting point
            bullet_state = "ready" #because the bullet is not being shown anymore, we have to change the value to ready
            score_value += 1 # increase the score
            enemyX[i] = random.randint(0, 735)  # default position to the enemy so when the game starts or it is killed, it reloads and comes back in random places / anywhere between 0 and 800
            enemyY[i] = random.randint(50, 150)  # min and max heigh

        enemy(enemyX[i], enemyY[i], i)


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