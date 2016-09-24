from pico2d import *
from mydefine import *
class Tile:
    def __init__(self,n,x,y):
        self.imagetile = None
        if n == MAPTYPE1:
            self.imagetile = load_image("res/6x8.png")
        elif n == MAPTYPE2:
            self.imagetile = load_image("res/8x10.png")
        elif n == MAPTYPE3:
            self.imagetile = load_image("res/10x12.png")
        else:
            print("범위나감" )

        self.startX = x
        self.startY = y
        self.color =  SDL_Color(255,255,255)

    def Draw(self):
        self.imagetile.drawRGB(self.startX,self.startY,self.color)
    def Update(self):
        pass