
from MapPy.Tile.Tile import Tile
from mydefine import *
from mycoroutine import  *


class OneTile(Tile):
    def __init__(self,n,x,y,xnumber,ynumber):
        super(OneTile, self).__init__(n, x, y, xnumber, ynumber)
        self.color = ONETILECOLOR
        self.Type = ONETILE
        self.StartCoroutine(self.InitTile())
    def InitTile(self):
        for i in range(0, 15):
            yield WaitForSeconds(0.005)
            self.SizeH += 1
            self.SizeW += 1
        for i in range(0, 15):
            yield WaitForSeconds(0)
            self.SizeH -= 1
            self.SizeW -= 1
    def Draw(self):
        self.imagetile.drawRGB(self.startX, self.startY, self.color,self.SizeW,self.SizeH)
    def Update(self):
        self.RunCoroutine()

