import pygame, sys

pygame.init() # nethod to start the game
screen = pygame.display.set_mode((400, 500))

while True:
    for event in pygame.event.get() :
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() 

