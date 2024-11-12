import pygame, sys

pygame.init() # nethod to start the game
screen = pygame.display.set_mode((400, 500))
# crete surface
test_surface = pygame.Surface((100, 200))
#test_surface.fill(pygame.Color('blue'))
test_rect_from_test_surface = test_surface.get_rect(topright = (200,250)) # (x,y)
# create surface cannot refix position - rect(rectangle)
# pygame.Rect(x,y,w,h)
test_rect = pygame.Rect(100,200,100,200)
test_surface.fill((0,0,255)) # blue color
while True:
    for event in pygame.event.get() :
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    pygame.draw.rect(screen, pygame.Color('red'), test_rect)

    screen.blit(test_surface, test_rect_from_test_surface) # pint(x,y) in the topright
    pygame.display.update() 

