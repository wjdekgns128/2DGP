from Game.Map import Tiles
from Game.Map.Tiles import *
from mydefine import *


class Map:
    def __init__(self):
        pass
    def __del__(self):
        del(self.ClearColorImage)
        del(self.Back)
        del(self.MapTiles)
    def MapSetting(self): # 챕터 스테이지 번호 넘어옴
        self.Home = load_image("res/Home.png")
        self.Retry = load_image("Res/Retry.png")
        self.ClearColorImage = load_image("res/6x8.png")
        self.FontText = load_font("res/font/GodoB.ttf", 85)
        self.Back = load_image("res/Back.png")
        self.NowPlayMapNumber = Sing_MapListManager.NowStage
        self.NowPlayChNumber = Sing_MapListManager.NowCh
        mylist = []
        self.MapType,self.ClearCount,self.ClearColor,mylist = Sing_MapListManager.GetFileData(self.NowPlayChNumber,self.NowPlayMapNumber)
        self.MapCount = (MapSize[self.MapType][0],MapSize[self.MapType][1])
        self.MapSize = (MapTilesSize[self.MapType][0],MapTilesSize[self.MapType][1])
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
                                                    10 + self.MapSize[1] / 2 + (y * self.MapSize[1]), checktype)
                    else:
                        self.MapTiles[x][y] = Tiles(tileres[self.MapType],
                                                    60 + (self.MapSize[0] / 2) + (x * self.MapSize[0]),
                                                    10 + self.MapSize[1] / 2 + (y * self.MapSize[1]), checktype)

    def Draw(self):
        self.Back.draw(300,350)
        self.ClearColorImage.drawRGB(100,655,Sing_ColorLisManager.GetColorNumber(Sing_UserManager.NowColor,self.ClearColor-1),85,85)
        self.FontText.draw(270,650,str(self.ClearCount),color= (255,255,255))
        self.Retry.draw(510,665,50,50)
        self.Home.draw(570,665,50,50)
        for y in range(0, self.MapCount[1]):
            for x in range(0, self.MapCount[0]):
                self.MapTiles[x][y].Draw()
    def Update(self):
        for y in range(0, self.MapCount[1]):
            for x in range(0, self.MapCount[0]):
                self.MapTiles[x][y].Update()