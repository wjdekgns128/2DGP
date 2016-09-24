
from MapPy.Tile.Tile import Tile
from sdl2.pixels import SDL_Color
from mydefine import *
from mycoroutine import  *


class FiveTile(Tile):
    def __init__(self,n,x,y,xnumber,ynumber):
        super(FiveTile, self).__init__(n, x, y, xnumber, ynumber)
        self.color = FIVETILECOLOR
        self.Type = FIVETILE
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

