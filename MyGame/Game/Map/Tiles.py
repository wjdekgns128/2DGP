from mydefine import *
from pico2d import *


from MyUtile.mycoroutine import *

class Tiles(Coroutine):
    def __init__(self,n,x,y,type,c):
        super(Tiles,self).__init__()
        Tilet = ["res/6x8_click.png","res/8x10.click.png","res/10x12_click.png"]
        self.StartX = x
        self.StartY = y
        self.Type = type
        self.FirstType = type
        self.drawimage = load_image(n)
        self.SeleteDraw = load_image(Tilet[c])

        self.SizeW = self.drawimage.w
        self.SizeH = self.drawimage.h
        self.ClickCheck = False
        self.ChageColor(type)
        self.ChageCheck = False
    def __del__(self):
        del (self.drawimage)
    def ToReturnGame(self): #게임 재시작시 리턴 컬러
        self.Type = self.FirstType
        self.ChageColor(self.Type)
    def ChageColor(self,n): # 넘어 오는 인자값으로 색상 변경되면서 동시에 코루틴
        if( n == NOTILE):
            self.MyColor = SDL_Color(116,116,116)
        else:
            self.MyColor = Sing_ColorLisManager.GetColorNumber(Sing_UserManager.NowColor,n-1)
        self.Type = n
        self.StartCoroutine(self.__StartInitTile())
    def ClickDown(self):
        self.StartCoroutine(self.__StartInitTile())
        self.ClickCheck = True

    def ClickUp(self):
        self.ClickCheck = False
    def Draw(self):
        self.drawimage.drawRGB(self.StartX,self.StartY,self.MyColor,self.SizeW,self.SizeH)
        if self.ClickCheck:
            self.SeleteDraw.draw(self.StartX,self.StartY)
    def Update(self):
        self.RunCoroutine()
    # 코루틴함수들....
    def __StartInitTile(self):
        for i in range(0, 9):
            yield WaitForSeconds(0.002)
            self.SizeH += 1
            self.SizeW += 1
        self.StartCoroutine(self.__ReturnInitTile())
    def __ReturnInitTile(self):
        for i in range(0, 9):
            yield WaitForSeconds(0.001)
            self.SizeH -= 1
            self.SizeW -= 1
    def Coll(self ,x2, y2):
        left, bottom, right, top = self.StartX - self.SizeW/2, self.StartY - self.SizeH/2, self.StartX + self.SizeW/2, self.StartY + self.SizeH/2
        left1, bottom1, right1, top1 = x2 - 2, y2 - 2, x2 + 2, y2 + 2
        if left > right1:
            return False
        if right < left1:
            return False
        if top < bottom1:
            return False
        if bottom > top1:
            return False
        return True