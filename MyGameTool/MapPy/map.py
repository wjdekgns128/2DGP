
from pico2d import *

from MapPy.Tile.NoTile import *
from MapPy.Tile.OneTile import *
from MapPy.Tile.TwoTile import *
from MapPy.Tile.TheerTile import *
from MapPy.Tile.FourTile  import *
from MapPy.Tile.FiveTile import *

from mydefine import *
class NowDrawCheck:
    def __init__(self,xSize,ySize):
        self.x = 0
        self.y = 0
        self.xSize = xSize
        self.ySize = ySize
        self.NowNumber = -1
        self.NowDrawIng = False
        self.NowDrawTiles = [load_image("res/6x8_click.png"), load_image("res/6x8.png"),NOTILECOLOR]
    def Draw(self):
        if(self.NowDrawIng != True or self.NowNumber == -1):
            return
        if(self.NowNumber == 0):
            self.NowDrawTiles[0].drawRGB(self.x,self.y,self.NowDrawTiles[2],self.xSize,self.ySize)
        else:
            self.NowDrawTiles[1].drawRGB(self.x,self.y,self.NowDrawTiles[2],self.xSize,self.ySize)

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
        for y in range(0, self.yCount):
            for x in range(0, self.xCount):
                self.MapTiles[x][y].Update()
    def Draw(self):
        for y in range(0, self.yCount):
            for x in range(0, self.xCount):
                self.MapTiles[x][y].Draw()

        self.NowDraw.Draw()
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
                    self.MapTiles[x][y] = NoTile(n,60 + (self.xSize/2) + (x * self.xSize),100 + self.ySize/2 + (y * self.ySize),x,y)

        #
        self.NowDraw = NowDrawCheck(self.xSize,self.ySize)
        self.DrawIng = False
        #
    def MouseMake(self,event):   # nowmoad 펄스면 맨들기 #트루면 게임

        if (event.type,event.button) == (SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
             tempx,tempy,temp  = self.MouseToTile(event.x,800 - event.y)
             if temp == True and self.NowDraw.NowNumber != -1:
                self.DrawIng = True
        elif (event.type) == SDL_MOUSEBUTTONUP:
            self.DrawIng = False
        elif (event.type) == SDL_MOUSEMOTION:
            if  self.NowDraw.NowNumber != -1:
                tempx,tempy, temp = self.MouseToTile(event.x, 800 - event.y)
                if(temp ):
                    self.NowDraw.x = int(60 + (self.xSize/2) + (tempx * self.xSize))
                    self.NowDraw.y = int(100 + self.ySize/2 + (tempy * self.ySize))
                    self.NowDraw.NowDrawIng = True
                    if self.DrawIng == True:
                        self.NewCreateTile(tempx,tempy)
                else:
                    self.NowDraw.NowDrawIng = False

    def MousePlay(self, event):
        pass
    def MouseToTile(self,mx,my):
        for y in range(0, self.yCount):
            for x in range(0, self.xCount):
                 if self.MapTiles[x][y].Coll(mx,my) == True:
                     return x,y,True
        return -1,-1,False

    def NowToMakeTile(self,now):
        self.NowDraw.NowDrawTiles[2] = MYTILECOLORLIST[now]
        self.NowDraw.NowNumber = now
    def NewCreateTile(self,tempx,tempy):
        if self.MapTiles[tempx][tempy].Type == self.NowDraw.NowNumber:
            return;
        if self.NowDraw.NowNumber == NOTILE:
            self.MapTiles[tempx][tempy] = NoTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
        elif self.NowDraw.NowNumber == ONETILE:
            self.MapTiles[tempx][tempy] = OneTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx,tempy)
        elif self.NowDraw.NowNumber == TWOTILE:
            self.MapTiles[tempx][tempy] = TwoTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
        elif self.NowDraw.NowNumber == THREETILE:
            self.MapTiles[tempx][tempy] = TheerTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
        elif self.NowDraw.NowNumber == FOURTILE:
            self.MapTiles[tempx][tempy] = FourTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
        elif self.NowDraw.NowNumber == FIVETILE:
            self.MapTiles[tempx][tempy] = FiveTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
