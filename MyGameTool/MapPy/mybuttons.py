from sdl2.pixels import SDL_Color
from pico2d import *

from mydefine import *

class mybuttons(object):
    def __init__(self,image,x,y,color1 = SDL_Color(255,255,255)):
        self.image = load_image(image)
        self.startX = x
        self.startY = y
        self.mycolor = color1
    def Draw(self):
        self.image.drawRGB(self.startX,self.startY,self.mycolor)

    def Coll(self,x,y):
        left,bottom,right,top = self.startX - (self.image.w/2) + 10,self.startY - (self.image.h/2) + 10,self.startX + (self.image.w/2) - 10,self.startY + (self.image.h/2) -10
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
