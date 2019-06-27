############################################################################
# Purpose : A very small, basic and my first game
# Usages : Learning purpose, Entertainment
# Start date : 17/05/2019
# End date :
# Author : Cleiton Pereira
# License : 
# Version : 1.0
############################################################################

import pygame
from random import randint, random
from load_images import *
from colors import *

# ========================== Tratamento de dados Módulo ========================== #
try:
    pygame.init()
except:
    print('Erro inicialização de módulos.')

# ========================== Váriaveis usadas ========================== #
size = width, height = 1300, 760
screen = pygame.display.set_mode(size)
player_pos = [width/2, height/2 + 330]
player_size = 30

enemy_size = 10
enemy_pos = [randint(0, width - enemy_size), 0]
enemy_list = [enemy_pos]

speed = 0
player_speed = 5
Font =  pygame.font.SysFont('monospace', 35)
score = 0
fps = 30
clock = pygame.time.Clock()
running = True
gameOver = False
left, rigth = False, False

# ========================== Icon e Título ========================== #
pygame.display.set_caption('Nav')
pygame.display.set_icon(icon)

# ========================== Functions ========================== #
def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False

def drop_enemy(enemy_list):
    delay = random()
    if len(enemy_list) < randint(0, 20) and delay < 0.5:
        x_pos = randint(0, width - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemy(enemy_list):
    for enemy_pos in enemy_list:
        screen.blit(stars[1], (enemy_pos[0], enemy_pos[1]))

def update_enemy_position(enemy_list, score):
    for ix, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < height:
            enemy_pos[1] += speed
    
        else:
            enemy_list.pop(ix)
            score += 1
    return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

def move():
    global player_pos
    
    x = player_pos[0]
    y = player_pos[1]

    if left:
        x -= player_speed
        player_pos[0] = x

    elif rigth:
        x += player_speed
        player_pos[0] = x


def level(score, speed):
    if score < 20:
        speed = 3
        player_speed = 5

    elif score < 40:
        speed = 5
        player_speed = 7

    elif score < 60:
        speed = 7
        player_speed = 10

    elif score > 200:
        speed = 25
        player_speed = 16
    
    else:
        speed = 15
        player_speed = 15

    return speed
# ========================== Main ========================== #
while running:
    clock.tick(fps)
    move()

    while gameOver == True:
        screen.fill(white)
        text = 'To continue press C or ESC to exit.'
        text2 = 'Your Score: ' + str(score)
        label1 = Font.render(text, 1, black)
        label2 = Font.render(text2, 1, black)
        screen.blit(label1, (width/2 - 350, height/2))
        screen.blit(label2, (width/2 - 350, height/2 - 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                       
                running = False
                gameOver = False

            if event.type == pygame.KEYDOWN:                    
                if event.key == pygame.K_ESCAPE: 
                    running = False
                    gameOver = False
                    
                elif event.key == pygame.K_c: 
                    running = True
                    gameOver = False
                    score = 0
                    speed = 3
                    player_speed = 5
                    player_pos = [width/2, height/2 + 330]
                    for ix, enemy_pos in enumerate(enemy_list):
                        enemy_list.pop(ix)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:                       
            running = False

        if event.type == pygame.KEYDOWN:                    
            if event.key == pygame.K_ESCAPE: 
                running = False

# ========================== Commands ========================== #
            
        
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                left = True
                rigth = False

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                rigth = True
                left = False

    screen.fill((0, 0, 0))

    if enemy_pos[1] >= 0 and enemy_pos[1] < height:
        enemy_pos[1] += speed
    
    else:
        enemy_pos[0] = randint(0, width - enemy_size)
        enemy_pos[1] = 0

 
    drop_enemy(enemy_list)

    score = update_enemy_position(enemy_list, score)
    speed = level(score, speed)

    text = 'Star Count: ' + str(score)
    label = Font.render(text, 1, yellow)
    screen.blit(label, (width - 350, height - 50))
    
    if collision_check(enemy_list, player_pos) or player_pos[0] > width - player_size:
        gameOver = True

    draw_enemy(enemy_list)

    screen.blit(nav, (player_pos[0], player_pos[1]))
    pygame.display.update()