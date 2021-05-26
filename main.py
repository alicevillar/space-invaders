import pygame

#initialize pygame
pygame.get_init()

#creating a screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/planet-earth.png')
pygame.display.set_icon(icon)


# Game loop
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB - Red/Green/Blue
    screen.fill((0,0,0))
    # to keep updating the game window that I'm working on
    pygame.display.update()
    