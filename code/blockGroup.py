import random
import pygame,sys
from pygame.locals import *
from const import *
from block import * 
from utils import *

class BlockGroup(object):

    #给定坐标,生成一种方块组
    def GenerateBlockGroupConfig(rowIdx,colIdx):

        shapeIdx = random.randint(0,len(BLOCK_SHAPE)-1)
        bType=random.randint(0,BlockType.BLOCKMAX-1)

        configList=[]
        rotIdx = 0

        for x in range(len(BLOCK_SHAPE[shapeIdx][rotIdx])):
            config={
                'blockType':bType,
                'blockShape':shapeIdx,
                'blockRot':rotIdx,
                'blockGroupIdx':x,
                'rowIdx':rowIdx,
                'colIdx':colIdx

            }
            configList.append(config)
        #      每个方块的坐标
        return configList
    


    def __init__(self,blokGroupType,width,height,blockConfigList,relPos):
        super().__init__()
        #存下每个方块的信息
        self.blocks=[]
        self.time=0
        self.pressTime = {}
        self.blockGroupType = blokGroupType
        self.dropInterval = 0
        for config in blockConfigList:
            blk=Block(config['blockType'],config['rowIdx'],config['colIdx'],config['blockShape'],config['blockRot'],config['blockGroupIdx'],width,height,relPos)
            self.blocks.append(blk)

    def draw(self,surface):
        for b in self.blocks:
            b.draw(surface) 

    def update(self):
        oldTime = self.time
        curTime = getCurrentTime()
        diffTime = curTime - oldTime
        if self.blockGroupType == BlockGroupType.DROP:
            if diffTime>=self.dropInterval:
                self.time = curTime
                for b in self.blocks:
                    b.drop()

            self.keyDownHandler()

    def getBlockIndexes(self):
        return [block.getIndex() for block in self.blocks]
    
    def getNextBlockIndexes(self):
        return [block.getNextIndex() for block in self.blocks]
    
    def getBlocks(self):
        return self.blocks
    
    def clearBlocks(self):
        self.blocks =[]
    
    def addBlocks(self,blk):
        self.blocks.append( blk )
    
    def checkAndSetPressTime(self,key):
        ret =False
        if getCurrentTime()- self.pressTime.get(key,0)>30:
            ret = True
        self.pressTime[key] = getCurrentTime()

        return ret
    
    def keyDownHandler(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT] and self.checkAndSetPressTime(K_LEFT):
            b = True
            for blk in self.blocks:
                if blk.isLeftBound():
                    b = False
                    break
            if b:
                for blk in self.blocks:
                    blk.doLeft()

        elif pressed[K_RIGHT] and self.checkAndSetPressTime(K_RIGHT):
            b = True
            for blk in self.blocks:
                if blk.isRightBound():
                    b = False
                    break
            if b:
                for blk in self.blocks:
                    blk.doRight()

        if pressed[K_DOWN]:
            self.dropInterval = 30
        else:
            self.dropInterval = 300

        if pressed[K_UP] and self.checkAndSetPressTime(K_UP):
            for blk in self.blocks:
                blk.doRotate()


