from sdl2.pixels import SDL_Color
from MapPy.Tile.Tile import Tile
from mydefine import *

class NoTile(Tile):
    def __init__(self,n,x,y,xnumber,ynumber):
        super(NoTile,self).__init__(n,x,y,xnumber,ynumber)
        self.color = NOTILECOLOR
        self.Type = NOTILE

    def Draw(self):
        self.selectandnotile.drawRGB(self.startX,self.startY,self.color)
    def Update(self):
        pass



#from MapPy.Tile.Tile import Tile
#from sdl2.pixels import SDL_Color
#from mydefine import *


#class BlueTlie(Tile):
    #def __init__(self,n,x,y,xnumber,ynumber):
       # super(BlueTlie, self).__init__(n, x, y, xnumber, ynumber)
      #  self.color = ONETILECOLOR
     #   self.Type = BLUE
   # def Draw(self):
   #     self.imagetile.drawRGB(self.startX, self.startY, self.color)
   # def Update(self):
   #     pass
