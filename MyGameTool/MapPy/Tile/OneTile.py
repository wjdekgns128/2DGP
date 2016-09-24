
from MapPy.Tile.Tile import Tile
from sdl2.pixels import SDL_Color
from mydefine import *


class OneTile(Tile):
    def __init__(self,n,x,y,xnumber,ynumber):
        super(OneTile, self).__init__(n, x, y, xnumber, ynumber)
        self.color = ONETILECOLOR
        self.Type = ONETILE
    def Draw(self):
        self.imagetile.drawRGB(self.startX, self.startY, self.color)
    def Update(self):
        pass
