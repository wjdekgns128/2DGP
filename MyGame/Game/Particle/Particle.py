from random import randint
from typing import Match

from MyUtile.mycoroutine import Coroutine
from mydefine import *

class ParticleObject(Coroutine):
    Image = None
    def __init__(self,x,y):
        super(ParticleObject, self).__init__()
        self.x = x - randint(-15,15)
        self.y = y - randint(-15,15)
        self.xspeed = randint(-5,5)
        self.yspeed = randint(-5,5)

        self.DownOp = 0.015
        if( self.xspeed == 0):
            self.xspeed = 3
        self.w = randint(4,10)
        self.h = randint(4,10)
        self.StartOp = 1
        self.Color = SDL_Color(randint(0,256),randint(0,256),randint(0,256))
        if ParticleObject.Image == None:
            ParticleObject.Image = load_image("res/ParticleObject.png")
    def __del__(self):
        pass
    def Draw(self):
        ParticleObject.Image.drawRGB(self.x,self.y,self.Color,self.w,self.h)
    def Update(self):
        self.x += self.xspeed
        self.y += self.yspeed

        ParticleObject.Image.opacify(self.StartOp)
        self.StartOp -= self.DownOp;
        if( self.StartOp <= 0):
            self.StartOp = 0
    def GetOp(self):
        return self.StartOp
class Particle:
    def __init__(self):
        self.ObjectCount = 0
        self.ObjectList = []
    def ReSetting(self,n):
        self.ObjectList.clear()
        TempXY = [(200, 540), (180, 310), (430, 120), (440, 350)]
        self.ObjectCount = randint(30, 70)
        for i in range(0, self.ObjectCount):
            self.ObjectList.append(ParticleObject(TempXY[n][0], TempXY[n][1]))
    def __del__(self):
        pass
    def Draw(self):
        for i in range(0, self.ObjectList.__len__()):
            if (self.ObjectList[i].GetOp() > 0):
                self.ObjectList[i].Draw()
    def Update(self):
        for i in range(0, self.ObjectList.__len__()):
            if(self.ObjectList[i].GetOp() > 0):
                self.ObjectList[i].Update()
