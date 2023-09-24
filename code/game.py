
import pygame,sys
from pygame.locals import *

from const import *

from blockGroup import *


class Game(pygame.sprite.Sprite):
    def __init__(self, surface):
        self.surface=surface
        self.fixedBlockGroup = BlockGroup(BlockGroupType.FIXED, BLOCK_SIZE_W, BLOCK_SIZE_H,[],self.getPelPos())
        self.dropBlockGroup = None

    def generateDropBlockGroup(self):
        conf = BlockGroup.GenerateBlockGroupConfig(0,GAME_COL/2-1)
        self.dropBlockGroup = BlockGroup(BlockGroupType.DROP, BLOCK_SIZE_W,BLOCK_SIZE_H,conf,self.getPelPos())


    def update(self):
        self.fixedBlockGroup.update()
        if self.dropBlockGroup:
            self.dropBlockGroup.update()
        else:
            self.generateDropBlockGroup()

        if self.willCollide():
            blocks =self.dropBlockGroup.getBlocks()
            for blk in blocks:
                self.fixedBlockGroup.addBlocks(blk)
            
            self.dropBlockGroup.clearBlocks()
            self.dropBlockGroup = None

    def draw(self):
        self.fixedBlockGroup.draw(self.surface)
        if self.dropBlockGroup:
            self.dropBlockGroup.draw(self.surface)
        else:
            self.generateDropBlockGroup()
    
    def getPelPos(self):
        return [250,0]
    
    def willCollide(self):
        hash = {}
        allIndexes = self.fixedBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            hash[idx] = 1
        dropIndexes = self.dropBlockGroup.getNextBlockIndexes()

        for dropIndex in dropIndexes:
            if hash.get(dropIndex):
                return True
            if dropIndex[0] >= GAME_ROW+1:
                return True
            
        return False
    