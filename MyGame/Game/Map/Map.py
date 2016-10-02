import game_framework
from Game.Map import Tiles
from Game.Map.Tiles import *
from mydefine import *


class Map(Coroutine):
    def __init__(self):
        super(Map,self).__init__()

        pass
    def __del__(self):
        del(self.ClearColorImage)
        del(self.Back)
        del(self.MapTiles)
        del(self.Home)
        del(self.Retry)
        del(self.FontText)
        del(self.FontText1)
        del(self.Button)
        del(self.PopBackImage)

    def Coll(self, x1, y1, w1, h1, x2, y2):
        left, bottom, right, top = x1 - w1, y1 - h1, x1 + w1, y1 + h1
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
    def MapSetting(self): # 챕터 스테이지 번호 넘어옴
        self.Home = load_image("res/Home.png")
        self.Retry = load_image("Res/Retry.png")
        self.ClearColorImage = load_image("res/6x8.png")
        self.FontText1 = load_font("res/font/GodoB.ttf", 55)
        self.Back = load_image("res/Back.png")
        self.NowPlayMapNumber = Sing_MapListManager.NowStage
        self.NowPlayChNumber = Sing_MapListManager.NowCh
        self.PopUp = False
        self.CheckCount = 0
        self.DownButton = False
        self.Chage = 0
        self.FontText = load_font("res/font/GodoB.ttf", 70)
        self.Button = [load_image("res/okbutton.png"), load_image("res/nobutton.png")]
        self.PopBackImage = load_image("res/Block_Image.png")
        mylist = []
        self.MapType,self.ClearCount,self.ClearColor,mylist = Sing_MapListManager.GetFileData(self.NowPlayChNumber,self.NowPlayMapNumber)
        self.MapCount = (MapSize[self.MapType][0],MapSize[self.MapType][1])
        self.MapSize = (MapTilesSize[self.MapType][0],MapTilesSize[self.MapType][1])
        self.ClickX = 0
        self.ClickY = 0
        self.MapTiles = None
        if self.MapTiles != None:
            del (self.MapTiles)
            self.MapTiles = None
        if (self.MapTiles == None):
            self.MapTiles = [[0 for y in range(self.MapCount[1])] for x in range(self.MapCount[0])]
        for y in range(0, self.MapCount[1]):
            for x in range(0, self.MapCount[0]):
                    checktype = mylist.pop()
                    if checktype == NOTILE:
                        self.MapTiles[x][y] = Tiles(notileres[self.MapType], 60 + (self.MapSize[0] / 2) + (x * self.MapSize[0]),
                                                    10 + self.MapSize[1] / 2 + (y * self.MapSize[1]), checktype,self.MapType)
                    else:
                        self.MapTiles[x][y] = Tiles(tileres[self.MapType],
                                                    60 + (self.MapSize[0] / 2) + (x * self.MapSize[0]),
                                                    10 + self.MapSize[1] / 2 + (y * self.MapSize[1]), checktype,self.MapType)

    def Draw(self):
        self.Back.draw(300,350)

        self.ClearColorImage.drawRGB(100,655,Sing_ColorLisManager.GetColorNumber(Sing_UserManager.NowColor,self.ClearColor-1),85,85)
        self.FontText.draw(270,650,str(self.ClearCount),color= (255,255,255))
        self.Retry.draw(455,650,50,50)
        self.Home.draw(515,650,50,50)
        for y in range(0, self.MapCount[1]):
            for x in range(0, self.MapCount[0]):
                self.MapTiles[x][y].Draw()
        if (self.PopUp == True):
            self.PopBackImage.draw(300, 350, 400, 500)
            self.FontText1.draw(225, 400, "Menu?")
            for i in range(0, 2):
                self.Button[i].draw(230 + (i * 140), 280)
    def Update(self):
        for y in range(0, self.MapCount[1]):
            for x in range(0, self.MapCount[0]):
                self.MapTiles[x][y].Update()
        self.RunCoroutine()
    def Event(self,event):
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.PopUp == False:
                if self.Coll(515,650,25,25,event.x,700-event.y):
                    self.PopUp = True
                    return False
                elif self.Coll(455,650,25,25,event.x,700-event.y):
                    self.MapSetting();
                    return False
                else:
                    for y in range(0, self.MapCount[1]):
                        for x in range(0, self.MapCount[0]):
                            if self.MapTiles[x][y].Coll(event.x,700-event.y):
                                    self.Chage = self.MapTiles[x][y].Type
                                    if(not self.MapTiles[x][y].Type == 0):
                                        self.MapTiles[x][y].ClickDown()
                                        self.ClickX= x
                                        self.ClickY = y
                                    break
            else:
                for i in range(0, 2):
                    if self.Coll(230 + (i * 140), 280,45,45, event.x, 700 - event.y):
                        if i == 0:
                            return True
                        self.PopUp = False
                        return False
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            if (not self.MapTiles[self.ClickX][self.ClickY].Type == 0):
                self.MapTiles[self.ClickX][self.ClickY ].ClickUp()
                for y in range(0, self.MapCount[1]):
                    for x in range(0, self.MapCount[0]):
                        if self.MapTiles[x][y].Coll(event.x, 700 - event.y):
                            self.ChageColor(x,y,self.Chage,self.MapTiles[x][y].Type)
                            break
    def ChageColor(self,x,y,ChageColor,TagerColor): # x,y,바뀔색,바꿔야할색
        if ChageColor == 0 or TagerColor == 0 or ChageColor == TagerColor or self.DownButton == True:
            return
        self.CheckCount = 0
        self.DownButton= True
        for y1 in range(0, self.MapCount[1]):
            for x1 in range(0, self.MapCount[0]):
                self.MapTiles[x1][y1].ChageCheck = False
        self.ChageClearCheckCount(x,y,ChageColor,TagerColor)
        self.ClearCount -= 1
        self.StartCoroutine(self.ChageDrawImageChage(x,y,ChageColor))
    def ChageClearCheckCount(self,x,y,ChagerColor,TagerColor):
        if self.MapTiles[x][y].Type == TagerColor and  self.MapTiles[x][y].ChageCheck == False:
            self.MapTiles[x][y].ChageCheck = True
            self.CheckCount = self.CheckCount +1
            if x > 0:
                self.ChageClearCheckCount(x-1,y,ChagerColor,TagerColor)
            if x < self.MapCount[0]-1:
                self.ChageClearCheckCount(x+1,y,ChagerColor,TagerColor)
            if y > 0 :
                self.ChageClearCheckCount(x,y-1,ChagerColor,TagerColor)
            if y < self.MapCount[1]-1:
                self.ChageClearCheckCount(x,y+1,ChagerColor,TagerColor)
    def ChageDrawImageChage(self,x,y,TagerColor):
        if self.MapTiles[x][y].ChageCheck == True:
            self.MapTiles[x][y].ChageColor(TagerColor)
            self.MapTiles[x][y].ChageCheck = False
            self.CheckCount -= 1
            yield WaitForSeconds(0.035)

            if x > 0:
                self.StartCoroutine(self.ChageDrawImageChage(x - 1, y, TagerColor))
            if x < self.MapCount[0] - 1:
                self.StartCoroutine( self.ChageDrawImageChage(x + 1, y, TagerColor))
            if y > 0:
                self.StartCoroutine( self.ChageDrawImageChage(x, y - 1, TagerColor))
            if y < self.MapCount[1] - 1:
                self.StartCoroutine(self.ChageDrawImageChage(x, y + 1, TagerColor))
            if (self.CheckCount == 0):
                self.DownButton = False
                print("check")
    def ClearGameCheck(self):
        pass
