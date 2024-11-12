import pygame, sys

pygame.init() # nethod to start the game
screen = pygame.display.set_mode((400, 500))
# crete surface
test_surface = pygame.Surface((100, 200))
#test_surface.fill(pygame.Color('blue'))
test_surface.fill((0,0,255)) # blue color
while True:
    for event in pygame.event.get() :
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    # hanve two way to fill color argument 
     # 1. RGB tuple (red, green, blue )
     # 2. color name
    screen.blit(test_surface, (200, 250))
    pygame.display.update() 

