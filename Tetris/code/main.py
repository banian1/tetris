import pygame,sys
from pygame.locals import *
import random
from const import *
from block import *
from blockGroup import *

pygame.init()

DISPLAYSURE=pygame.display.set_mode((800,600))


blockGroups=[]
for x in range(5):
    conf=BlockGroup.GenerateBlockGroupConfig(x*4,x)
    blockGroups.append(BlockGroup(32,32,conf,(240,50)))
 
   




while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    for bg in blockGroups:
        bg.update()

    DISPLAYSURE.fill((0,0,0))
    for bg in blockGroups:
        bg.draw(DISPLAYSURE)
    
    

    pygame.display.update()