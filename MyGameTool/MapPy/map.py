
from pico2d import *

from MapPy.Tile.Tile import Tile
from mydefine import *

class map:
    def __init__(self,n):
        self.name= ["type1","type2","type3"]
        self.MapTiles = None
        self.LoadJson()
        self.ChageMap(n)
    def LoadJson(self):
        f = open("test.json", 'r')
        self.js = json.loads(f.read())
        f.close()
    def Update(self):
        pass
    def Draw(self):
        for y in range(0, self.yCount):
            for x in range(0, self.xCount):
                self.MapTiles[x][y].Draw()
    def ChageMap(self,n):
        self.nowtype = n
        self.xSize = int(self.js[self.name[self.nowtype]]["x"])
        self.ySize = int(self.js[self.name[self.nowtype]]["y"])
        self.xCount = int(self.js[self.name[self.nowtype]]["xcount"])
        self.yCount = int(self.js[self.name[self.nowtype]]["ycount"])
        if self.MapTiles != None:
            del(self.MapTiles)
            self.MapTiles = None
        if(self.MapTiles == None):
            self.MapTiles = [[0 for y in range(self.yCount)] for x in range(self.xCount)]
            for y in range(0,self.yCount):
                for x in range(0,self.xCount):
                    self.MapTiles[x][y] = Tile(n,60 + (self.xSize/2) + (x * self.xSize),100 + self.ySize/2 + (y * self.ySize))

