import pygame,sys
from pygame.locals import *
import random
from const import *
from block import *
from blockGroup import *
from game import *

pygame.init()

DISPLAYSURE=pygame.display.set_mode((800,600))

game = Game(DISPLAYSURE)




while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    


    game.update()
    DISPLAYSURE.fill((0,0,0))
    game.draw()

    pygame.display.update()