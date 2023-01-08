import pygame, sys, random

#color variables
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

def ball_animation():
    global ball_speed_x,ball_speed_y,player_score,opp_score,score_time,player2_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()
    if ball.right >= screen_width:
        opp_score += 1 #You put the opponent's score here
        score_time = pygame.time.get_ticks()



    if ball.colliderect(player) and ball_speed_x >0:
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y >10:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y >0:
            ball_speed_y *= -1
    
    if ball.colliderect(opp) and ball_speed_x < 0:
        if abs(ball.left - opp.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opp.top) < 10 and ball_speed_y >10:
            ball_speed_y *= -1
        elif abs(ball.top - opp.bottom) < 10 and ball_speed_y >0:
            ball_speed_y *= -1

def player_animation():
    
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def player2_animation():
    player2.y += player_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def opp_animation():
    if opp.top < ball.y:
        opp.top += opp_speed
    if opp.bottom > ball.y:
        opp.bottom -= opp_speed
    if opp.top <= 0:
        opp.top = 0
    if opp.bottom >= screen_height:
        opp.bottom = screen_height

def ball_reset():
    global ball_speed_x,ball_speed_y,score_time
    
    current_time = pygame.time.get_ticks()
    ball.center = ((screen_width/2),(screen_height/2))
    if current_time - score_time < 700:
        num_three = game_font.render('3',True, light_grey)
        screen.blit(num_three,(screen_width/2 -10,screen_height/2 +40))
    
    if 700 < current_time - score_time < 1400:
        num_two = game_font.render('2',True, light_grey)
        screen.blit(num_two,(screen_width/2 -10,screen_height/2 +40))
    
    if 1400<current_time - score_time < 2100:
        num_one = game_font.render('1',True, light_grey)
        screen.blit(num_one,(screen_width/2 -10,screen_height/2 +40))
    
    if current_time - score_time < 2100:
        ball_speed_x,ball_speed_y = 0,0
    else:
        ball_speed_y = 7*random.choice((1,-1))
        ball_speed_x = 7*random.choice((1,-1))
        score_time = None

    
    
#setup
pygame.init()
clock = pygame.time.Clock()

#Settin main window
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')
icon = pygame.image.load("stuff/ping-pong.png")
pygame.display.set_icon(icon)
#rectangles

ball = pygame.Rect(screen_width/2 -15,screen_height/2 -15,30,30)
player = pygame.Rect(screen_width-20,screen_height/2 -70,10,140)
opp = pygame.Rect(10,screen_height/2 -70,10,140)
player2  = pygame.Rect(10,screen_height/2 -70,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x =7 *random.choice((1,-1))
ball_speed_y = 7 *random.choice((1,-1))
player_speed = 0
player2_speed  = 0
opp_speed = 7

#Text variables
player_score = 0
opp_score = 0
player2_score = 0
game_font = pygame.font.Font('freesansbold.ttf',32)

#Score Timer
score_time = True

while True:
    #closing the window and handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_LALT:
                player2_speed += 7
            if event.key == pygame.K_x:
                player2_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_LALT:
                player2_speed -= 7
            if event.key == pygame.K_x:
                player2_speed += 7

    
    ball_animation()
    player_animation()
    opp_animation()
    
    
    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opp) #You put the opp variable here
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))

    if score_time:
        ball_reset()
    player_text = game_font.render(f'{player_score}', False,light_grey)
    screen.blit(player_text,(515,360))
    opp_text = game_font.render(f'{opp_score}', False,light_grey)
    screen.blit(opp_text,(470,360))


    #Updating window
    pygame.display.flip()
    clock.tick(60)