import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0) # right
        self.newBlock = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        # import sound
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            print("block: ", block)
            #1. We still need a rect for the póitioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos, cell_size, cell_size)
            #2. what direction í the face heading
            if index == 0:
                screen.blit(self.head, block_rect)
                # 3. snake head direction is not updating
            elif index == len(self.body) -1:
                screen.blit(self.tail, block_rect)
            else:
                
                # previous_block = body[current index + 1]--> previous index block(6,10) - block(5,10) --> Vector2(1,0)
                previous_block = self.body[index +1] - block
                next_block = self.body[index -1] - block
                print(previous_block, next_block)
                if previous_block.x - next_block.x == 0: # check if both previous_block and next_block the same x
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y - next_block.y == 0: # check if both previous_block and next_block the same x
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    #corner
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1 :
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1 :
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1 :
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1 :
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0) : self.head = self.head_left
        elif head_relation == Vector2(-1,0) : self.head = self.head_right
        elif head_relation == Vector2(0,1) : self.head = self.head_up
        elif head_relation == Vector2(0,-1) : self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0) : self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0) : self.tail = self.tail_right
        elif tail_relation == Vector2(0,1) : self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1) : self.tail = self.tail_down
      
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
        #pygame.draw.rect(screen,(126, 166,114),fruit_rect)
        screen.blit(apple, fruit_rect)
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
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
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
            # add crunch sound
            self.snake.crunch_sound.play()

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

    def draw_grass(self):
        # grass color
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0 :
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col* cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col*cell_size, row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
    # draw score
    def draw_score(self) :
        score_text = str(len(self.snake.body) - 3) # - (start index 0, head, tail)
        score_surface = game_font.render(score_text, True, (56,74,12))
        score_rect = score_surface.get_rect(center=(100, 50))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))

        screen.blit(score_surface,score_rect)
        screen.blit(apple, apple_rect)


pygame.mixer.pre_init(44100, -16,2,512) # play immidetely
pygame.init() # method to start the game
#change size (w,h) 
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
apple = pygame.image.load('Graphics/apple.png').convert_alpha() # import img and convert alpha to word in pygame
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
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
                # snake can not reverse themself
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN: # down
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT: # right
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT: # left
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    screen.fill((175,215,70))
    main_game.draw_element()
    pygame.display.update() 

# add sound to game
# when snake collide with fruit
# 1. import sound (avaiable)
# sound delay --> i want sound play immidietely
