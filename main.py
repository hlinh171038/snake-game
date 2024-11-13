import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0) # right
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183,121, 122), block_rect)
    # 1. move snake:
    #  1. we need some user input to move snake
    #  2. we need the timer ( we noly want to move this snake whenever this timer trigger)
    def move_snake(self):
        # coppy list except last element
        body_copy = self.body[:-1]
        # insert new element + direction to the first of the list
        body_copy.insert(0,body_copy[0]+ self.direction)
        # return list to body again
        self.body = body_copy[:]
        # ? i dont want exercute it all the time, i want it exercute in certain interval in my case 150 ml/s
        # --> create timer ( timer un pygame work in event loop)


class FRUIT:
    def __init__(self):
        # create x,y vector (best way to control object)
        self.x = random.randint(0, cell_number -1)
        self.y = random.randint(0, cell_number -1)
        self.pos = Vector2(self.x, self.y)
    # draw fruit
    def draw_fruit(self) :
        fruit_rect = pygame.Rect(int(self.pos.x * cell_number),int(self.pos.y * cell_number),cell_size,cell_size)
        #draw rectangle
        pygame.draw.rect(screen,(126, 166,114),fruit_rect)

pygame.init() # method to start the game
#change size (w,h) 
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))

fruit = FRUIT()
snake = SNAKE()
 # 2. timmer
SCREEN_UPDATE = pygame.USEREVENT # customer event you csnt not trigger
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get() :
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # up
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN: # down
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT: # right
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT: # left
                snake.direction = Vector2(-1,0)
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update() 

