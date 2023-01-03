import pygame
import random
import sys
from enum import Enum
from collections import namedtuple

#colors
green = (0,255,0)
light_green = (0,153,0)
blue = (0,0,50)
black= (0,0,0)
red = (255,0,0)
white = (255,255,255)
#Variables
w = 600
h= 600
BLOCK_SIZE =20
SPEED = 20
#path
game_caption = 'Madiou\'s Snake ' #Change caption here
icon_path = 'snake/assets/anaconda.png'#Change icon here
loser_sound_path = 'snake/assets/loser.wav'
crunch_sound_path = 'snake/assets/crunch.wav'
#Score list
scores =[]
pygame.init()
font = pygame.font.SysFont('arial', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point','x,y')

class SnakeGame:
    def __init__(self,w=w,h=h):
        self.w = w
        self.h = h
        #display
        self.display = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption(game_caption)
        icon = icon_path
        pygame.display.set_icon(pygame.image.load(icon))   
        self.clock = pygame.time.Clock()

        #game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2,self.h/2)
        self.snake = [self.head, 
                    Point(self.head.x-BLOCK_SIZE,self.head.y),
                    Point(self.head.x-(2*BLOCK_SIZE),self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
    
    def _place_food(self):
        x= random.randint(0,(self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y= random.randint(0,(self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()

    def move(self):
        #Collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
                elif event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
        #Move Snake
        self._move(self.direction)
        self.snake.insert(0,self.head) #Updates head
        #Check if game over
        game_over =  False
        if self._is_collision():
            game_over = True
            return game_over, self.score
        #Place food or move
        if self.head == self.food:
            crunch_sound = pygame.mixer.Sound(crunch_sound_path)
            crunch_sound.play()
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        #Update ui
        self._update_ui()
        self.clock.tick(SPEED)
        #return game over and score
        game_over = False
        return game_over,self.score
    
    def _is_collision(self):
        #Boundary collision
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y<0:
            return True
        #Self collision   
        if self.head in self.snake[1:]:
            return True
        return False  
    
    def _update_ui(self):
        self.display.fill(black)
        for pt in self.snake:
            pygame.draw.rect(self.display,green,pygame.Rect(pt.x,pt.y,BLOCK_SIZE,BLOCK_SIZE))
            pygame.draw.rect(self.display,green,pygame.Rect(pt.x+4,pt.y+4,12,12))
        pygame.draw.rect(self.display,red,pygame.Rect(self.food.x,self.food.y,BLOCK_SIZE,BLOCK_SIZE))
        text = font.render('Score: ' + str(self.score),True,white)
        self.display.blit(text,[0,0])
        pygame.display.flip()

    def _move(self,direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x+= BLOCK_SIZE
        elif direction == Direction.LEFT:
            x-= BLOCK_SIZE
        elif direction == Direction.UP:
            y-= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y+= BLOCK_SIZE

        self.head = Point(x,y)

def End():  
        x = w/6
        y= h/3
        pygame.display.set_caption(game_caption) #change caption here
        icon =  icon_path #change icon here
        pygame.display.set_icon(pygame.image.load(icon))   
        while True:
            screen = pygame.display.set_mode((w, h), 0, 32)
            #Fills the screen black
            screen.fill(black)
            myfont = pygame.font.SysFont('ds-digital',30)
            text = myfont.render("GAME OVER PRESS C TO PLAY AGAIN",True,(red))
            screen.blit(text, (x,y)) #20,200
            pygame.display.update()
            loser_sound = pygame.mixer.Sound(loser_sound_path) #change sound file here
            loser_sound.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    EndText()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        main()
def EndText():
    print('****'*30)
    print('GAME ENDED')
    print(f'Final Score: {scores[-1]}')
    print(f'Highscore: {max(scores)}')

def main():
    game = SnakeGame()
# GAME LOOP
    while(True):
        game_over,score = game.move()
        if game_over == True:
            scores.append(score)
            print(f'Game#{len(scores)} Score: {score}')
            End()
            
main()
