import pygame
from pygame.locals import *
from const import *


class Block(pygame.sprite.Sprite):

    #                                                       边界
    def __init__(self,blockType,baseRowIdx,baseColIdx,blockShape,blockRot,blockGroupIdx,width,height,relPos):
        super().__init__()
        self.blockType=blockType
        self.blockShape = blockShape
        self.baseRowIdx = baseRowIdx
        self.baseColIdx = baseColIdx
        self.blockGroupIdx = blockGroupIdx
        self.blockRot = blockRot
        self.width=width
        self.height=height
        self.relPos=relPos
        self.loadImage()
        self.updateImagePos()

    def loadImage(self):
        self.image=pygame.image.load(BLOCK_RES[self.blockType])


        #调整图片分辨率
        self.image=pygame.transform.scale(self.image,(self.width,self.height))

    def updateImagePos(self):
        self.rect=self.image.get_rect()
        self.rect.left=self.relPos[0]+self.width*self.colIdx
        self.rect.top=self.relPos[1]+self.height*self.rowIdx

        
    def isLeftBound(self):
        return self.colIdx==0
    
    def isRightBound(self):
        return self.colIdx==GAME_COL-1
    
    def doLeft(self):
        self.baseColIdx -= 1

    def doRight(self):
        self.baseColIdx += 1       


    def draw(self,surface):
        surface.blit(self.image,self.rect)
 
    def drop(self):
        self.baseRowIdx+=1
        self.updateImagePos()

    def getIndex(self):
        return (int(self.rowIdx),int(self.colIdx))
    
    def getNextIndex(self):
        return (int(self.rowIdx+1),int(self.colIdx))
    
    def getBlockConfigIndex(self):
        return BLOCK_SHAPE[self.blockShape][self.blockRot][self.blockGroupIdx]
    
    @property
    def rowIdx(self):
        return self.baseRowIdx + self.getBlockConfigIndex()[0]
    
    @property
    def colIdx(self):
        return self.baseColIdx + self.getBlockConfigIndex()[1]

    def doRotate(self):
        self.blockRot += 1
        if self.blockRot >= len(BLOCK_SHAPE[self.blockShape]):
            self.blockRot = 0