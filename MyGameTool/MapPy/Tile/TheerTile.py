
from MapPy.Tile.Tile import Tile
from sdl2.pixels import SDL_Color
from mydefine import *
from mycoroutine import  *


class TheerTile(Tile):
    def __init__(self,n,x,y,xnumber,ynumber):
        super(TheerTile, self).__init__(n, x, y, xnumber, ynumber)
        self.color = THERRTILECOLOR
        self.Type = THREETILE
        self.StartCoroutine(self.InitTile(True))

    def InitTile(self,check):
        for i in range(0, 18):
            yield WaitForSeconds(0.002)
            self.SizeH += 1
            self.SizeW += 1
        if(check == True):
            self.StartCoroutine(self.ReturnInitTile())
    def ReturnInitTile(self):
        for i in range(0, 18):
            yield WaitForSeconds(0.001)
            self.SizeH -= 1
            self.SizeW -= 1

    def ClickTile(self):
        self.StartCoroutine(self.InitTile(False))
    def ClickUpTile(self):
        self.StartCoroutine(self.ReturnInitTile())

    def Draw(self):
        self.imagetile.drawRGB(self.startX, self.startY, self.color,self.SizeW,self.SizeH)

    def Update(self):
        self.RunCoroutine()

