from pico2d import *
from mycoroutine import  *

class Tile(Coroutine):
    def __init__(self,n,x,y,xnumber,ynumber):
        super(Tile, self).__init__()

        imagelist = ["res/6x8.png", "res/8x10.png", "res/10x12.png"]
        imagelist1 = ["res/6x8_click.png", "res/8x10_click.png", "res/10x12_click.png"]
        self.imagetile = None
        self.selectandnotile = None
        self.imagetile = load_image(imagelist[n])
        self.selectandnotile= load_image(imagelist1[n])
        self.startX = x
        self.startY = y
        self.xnumber = xnumber
        self.ynumber = ynumber
        self.SizeW = self.imagetile.w
        self.SizeH = self.imagetile.h


    def Draw(self):
        pass
    def Update(self):
        pass
    def Coll(self,x,y):
        left,bottom,right,top = self.startX - (self.imagetile.w/2) + 10,self.startY - (self.imagetile.h/2) + 10,self.startX + (self.imagetile.w/2) - 10,self.startY + (self.imagetile.h/2) -10
        left1,bottom1,right1,top1 = x-5,y-5,x+5,y+5
        if left > right1:
            return False
        if right < left1:
            return False
        if top < bottom1:
            return False
        if bottom > top1:
            return False
        return True
