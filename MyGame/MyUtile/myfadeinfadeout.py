from pico2d import *
from MyUtile.mycoroutine import *


class FadeObject(Coroutine):
    def __init__(self,x,y):
        super(FadeObject,self).__init__()
        self.drawimage = load_image("res/fadeobject.png")
        self.x = x
        self.y = y
        self.angle = 0
        self.PlayIng = False
    def Draw(self):
        self.drawimage.rotate_draw(self.angle,self.x,self.y)
    def ChageCheck(self):
        self.StartCoroutine(self.StartChage())
    def StartChage(self):
        for i in range(0,11):
            self.drawimage.opacify(1 - (i*0.1))
            self.angle += 0.15

            yield WaitForSeconds(0.025)

    def Update(self):
        self.RunCoroutine()
class FadeInFadeOut(Coroutine):
    def __init__(self):
        super(FadeInFadeOut,self).__init__()
        self.FadeTile = [[0 for y in range(7)] for x in range(7)]
        for y in range(0, 7):
            for x in range(0, 7):
                    self.FadeTile[x][y] = FadeObject(  x * 100, 50 + (y*100))
        self.StartCoroutine(self.PlayObject(3, 3))
    def PlayObject(self,x,y):
        if(self.FadeTile[x][y].PlayIng == False):
            self.FadeTile[x][y].ChageCheck()
            self.FadeTile[x][y].PlayIng = True
            yield WaitForSeconds(0.046)
            if(x < 6):
                self.StartCoroutine(self.PlayObject(x+1,y))
            if (x > 0):
                self.StartCoroutine( self.PlayObject(x - 1, y))
            if (y < 7):
                self.StartCoroutine( self.PlayObject( x, y+1))
            if (y > 0):
                self.StartCoroutine(self.PlayObject(x, y - 1))
    def Draw(self):
        for y in range(0, 7):
            for x in range(0, 7):
                self.FadeTile[x][y].Draw()
    def Update(self):
        self.RunCoroutine()
        for y in range(0, 7):
            for x in range(0, 7):
                self.FadeTile[x][y].Update()
