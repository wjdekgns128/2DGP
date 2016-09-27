from Game.Map import Tiles
from Game.Map.Tiles import *
from mydefine import *


class Map:
    def __init__(self):
        pass
    def MapSetting(self, n): # 스테이지 번호 넘어옴
        self.NowPlayMapNumber = n
        mylist = []
        self.MapType,self.ClearCount,self.ClearColor,mylist = Sing_MapListManager.GetFileData(n)
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
        for y in range(0, self.MapCount[1]):
            for x in range(0, self.MapCount[0]):
                self.MapTiles[x][y].Draw()
    def Update(self):
        for y in range(0, self.MapCount[1]):
            for x in range(0, self.MapCount[0]):
                self.MapTiles[x][y].Update()