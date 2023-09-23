import pygame
from pygame.locals import *
from const import BLOCK_RES



class Block(pygame.sprite.Sprite):

    #                                                       边界像素
    def __init__(self,blockType,rowIdx,colIdx,width,height,relPos):
        super().__init__()
        self.blockType=blockType
        self.rowIdx=rowIdx
        self.colIdx=colIdx
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

        
    def update(self):
        pressed=pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.rect.move_ip(-1,0)
        elif pressed[K_RIGHT]:
            self.rect.move_ip(1,0)
        elif pressed[K_UP]:
            self.rect.move_ip(0,-1)
        elif pressed[K_DOWN]:
            self.rect.move_ip(0,1)

    def draw(self,surface):
        surface.blit(self.image,self.rect)
 
    def drop(self):
        self.rowIdx+=1
        self.updateImagePos()