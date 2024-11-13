import pygame, sys
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        # create x,y vector (best way to control object)
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x, self.y)
    # draw fruit
    def draw_fruit(self) :
        fruit_rect = pygame.Rect(self.pos.x,self.pos.y,cell_size,cell_size)
        #draw rectangle
        pygame.draw.rect(screen,(126, 166,114),fruit_rect)

pygame.init() # method to start the game
#change size (w,h) 
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))

fruit = FRUIT()

while True:
    for event in pygame.event.get() :
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update() 

