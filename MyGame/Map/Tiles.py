from mydefine import *
from pico2d import *


from MyUtile.mycoroutine import *

class Tiles(Coroutine):
    def __init__(self,n,x,y,type):
        super(Tiles,self).__init__()
        self.StartX = x
        self.StartY = y
        self.Type = type
        self.FirstType = type
        self.drawimage = load_image(n)
        self.SizeW = self.drawimage.w
        self.SizeH = self.drawimage.h
        self.ChageColor(type)
    def ToReturnGame(self): #게임 재시작시 리턴 컬러
        self.Type = self.FirstType
        self.ChageColor(self.Type)
    def ChageColor(self,n): # 넘어 오는 인자값으로 색상 변경되면서 동시에 코루틴
        if( n == NOTILE):
            self.MyColor = SDL_Color(116,116,116)
        else:
            self.MyColor = Sing_ColorLisManager.GetColorNumber(0,n-1)
        self.StartCoroutine(self.__StartInitTile())

    def Draw(self):
        self.drawimage.drawRGB(self.StartX,self.StartY,self.MyColor,self.SizeW,self.SizeH)
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
    #