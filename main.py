############################################################################
# Purpose : A very small, basic and my first game
# Usages : Learning purpose, Entertainment
# Start date : 17/05/2019
# End date :
# Author : Cleiton Pereira
# License : 
# Version : 1.0
############################################################################

import pygame, sys
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
player_pos = [width/2, height/2 + 300]
running = True
gameOver = False
fps = 30
clock = pygame.time.Clock()

# ========================== Icon e Título ========================== #
pygame.display.set_caption('Nav')
pygame.display.set_icon(icon)

# ========================== Main ========================== #
while running: 
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:                       
            running = False

        if event.type == pygame.KEYDOWN:                    
            if event.key == pygame.K_ESCAPE: 
                running = False

# ========================== Commands ========================== #
            x = player_pos[0]
            y = player_pos[1]
        
            if event.key == pygame.K_LEFT or event.key == K_a:
                x -= 5
            
            if event.key == pygame.K_RIGHT or event.key == K_d:
                x += 5


    pygame.draw.rect(screen, red, (player_pos[0], player_pos[1], 50, 50))
    pygame.display.update()