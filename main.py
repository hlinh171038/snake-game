import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0) # right
        self.newBlock = False
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
        if self.newBlock == True :
            # coppy all list element
            body_copy = self.body[:]
            # insert new element + direction to the first of the list
            body_copy.insert(0,body_copy[0]+ self.direction)
            # return list to body again
            self.body = body_copy[:]
            # ? i dont want exercute it all the time, i want it exercute in certain interval in my case 150 ml/s
            # --> create timer ( timer un pygame work in event loop) 
            self.newBlock = False
        else :
            # coppy list except last element
            body_copy = self.body[:-1]
            # insert new element + direction to the first of the list
            body_copy.insert(0,body_copy[0]+ self.direction)
            # return list to body again
            self.body = body_copy[:]
            # ? i dont want exercute it all the time, i want it exercute in certain interval in my case 150 ml/s
            # --> create timer ( timer un pygame work in event loop)

    def add_block(self):
        self.newBlock = True

class FRUIT:
    def __init__(self):
      self.randomize()
    # draw fruit
    def draw_fruit(self) :
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        #draw rectangle
        pygame.draw.rect(screen,(126, 166,114),fruit_rect)
    def randomize(self) :
          # create x,y vector (best way to control object)
        self.x = random.randint(0, cell_number -1)
        self.y = random.randint(0, cell_number -1)
        self.pos = Vector2(self.x, self.y)
class MAIN :
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    def update(self) :
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def draw_element(self) :
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    # check collision
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0] : # check if fruit position have same block of head of our snake
            # reposition the fruit
            self.fruit.randomize()
                # print('snake')
                # print('fruit position',self.fruit.pos)
                # print('snake head:', self.snake.body[0])
            # add another block to the snake
            self.snake.add_block()

    def check_fail(self) :
        # check if snake is outside of the screen]
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: # check head of snake between x,y
            self.game_over()
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init() # method to start the game
#change size (w,h) 
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))

 # 2. timmer
SCREEN_UPDATE = pygame.USEREVENT # customer event you csnt not trigger
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get() :
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
           main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # up
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN: # down
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT: # right
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT: # left
                main_game.snake.direction = Vector2(-1,0)
    screen.fill((175,215,70))
    main_game.draw_element()
    pygame.display.update() 

