
from pico2d import *
from MapPy.Tile.NoTile import *
from MapPy.Tile.OneTile import *
from MapPy.Tile.TwoTile import *
from MapPy.Tile.TheerTile import *
from MapPy.Tile.FourTile  import *
from MapPy.Tile.FiveTile import *
from mycoroutine import  *
from mydefine import *
from MapPy.filesave import *
# 드로우 되는중인지,체크
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
# 게임에 필요한 UI (세이브 할떄 데이터 접근쉽게하기위해)
class GameUI:
    def __init__(self):
        self.Font = load_font("res/font.ttf",50)
        self.image = load_image("res/6x8.png")
        self.Number = 1
        self.ClearCount = 10
        self.Playing = False

    def ClickClearColor(self):
            self.Number += 1
            self.Number %= MYTILECOLORLIST.__len__()
            if(self.Number == 0):
                self.Number +=1
    def Draw(self):
        self.image.drawRGB(560,760,MYTILECOLORLIST[self.Number])
        if(self.Playing):
            self.Font.draw(50,760,str(self.ClearCount))
    def Coll(self,x,y):
        left,bottom,right,top = 560 - (self.image.w/2) + 10,760 - (self.image.h/2) + 10,560 + (self.image.w/2) - 10,760 + (self.image.h/2) -10
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
class ClickTile:
    def __init__(self):
        self.GamePlayClickimage = load_image("res/6x8_click.png")
        self.w = 0
        self.h = 0
        self.x = 0
        self.y = 0
        self.chagecheck = False
    def Setting(self,w,h):
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h
    def Draw(self):
        if self.chagecheck == True:
            self.GamePlayClickimage.draw(self.x,self.y,self.w,self.h)
class map(Coroutine): #
    def __init__(self,n):
        super(map, self).__init__()
        self.ClearCount = 0
        self.name= ["type1","type2","type3"]
        self.TempMapTiles = []
        self.MapTiles = None
        self.UI = GameUI()
        self.TileCick = ClickTile()
        self.LoadJson()
        self.savefile = filesave()
        self.ChageMap(n)

    def LoadJson(self):
        f = open("test.json", 'r')
        self.js = json.loads(f.read())
        f.close()
    def Update(self):
        for y in range(0, self.yCount):
            for x in range(0, self.xCount):
                self.MapTiles[x][y].Update()

        self.RunCoroutine()
    def Draw(self):
        for y in range(0, self.yCount):
            for x in range(0, self.xCount):
                self.MapTiles[x][y].Draw()
        if self.UI.Playing:
            self.TileCick.Draw()
        self.UI.Draw()
        self.NowDraw.Draw()
    def LoadSetting(self,clear,mylist):
        self.UI.Number = clear
        for y in range(0, self.yCount):
            for x in range(0, self.xCount):
                self.NewCreateTile(x, y, mylist.pop())
    def ReSetting(self):
        self.ClearCount = 0
        self.NowDraw = NowDrawCheck(self.xSize, self.ySize)
        self.DrawIng = False
        self.UI.ClearCount = 0
        self.savefile.filesaveing = False
        self.TileCick.Setting(self.xSize,self.ySize)
        if self.UI.Playing == False:
            self.TempMapTiles.clear()
            for y in range(0, self.yCount):
                for x in range(0, self.xCount):
                    self.TempMapTiles.append(self.MapTiles[x][y].Type)
        else:
            self.TempMapTiles.reverse()
            for y in range(0, self.yCount):
                for x in range(0, self.xCount):
                    self.NewCreateTile(x,y,self.TempMapTiles.pop())

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

        self.ReSetting();
        #

        #
    def MouseMake(self,event):   # nowmoad 펄스면 맨들기 #트루면 게임
        self.UI.Playing = False
        if (event.type,event.button) == (SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
            if(self.UI.Coll(event.x,800-event.y) == True):
                self.UI.ClickClearColor()
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
                        self.NewCreateTile(tempx,tempy,self.NowDraw.NowNumber)
                else:
                    self.NowDraw.NowDrawIng = False

    def MousePlay(self, event):
        self.UI.Playing = True
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            tempx, tempy, temp = self.MouseToTile(event.x, 800 - event.y)
            if (temp):
                self.TileCick.x = int(60 + (self.xSize / 2) + (tempx * self.xSize))
                self.TileCick.y = int(100 + self.ySize / 2 + (tempy * self.ySize))
                self.mx = tempx
                self.my = tempy
                self.TileCick.chagecheck = True
                if self.MapTiles[tempx][tempy].Type != NOTILE:
                    self.MapTiles[tempx][tempy].ClickUpTile()

            else:
                self.mx = -1
                self.my = -1
        elif (event.type) == SDL_MOUSEBUTTONUP:
            self.TileCick.chagecheck = False
            if(self.mx != -1 or self.my != -1):
                if self.MapTiles[self.mx][self.my].Type != NOTILE:
                    self.MapTiles[self.mx][self.my].ClickTile() #누른타일
                tempx, tempy, temp = self.MouseToTile(event.x, 800 - event.y) # 땐 타일
                if temp == True:
                    self.MoveColl(self.MapTiles[self.mx][self.my],self.MapTiles[tempx][tempy],tempx,tempy)

    def MouseToTile(self,mx,my):
        for y in range(0, self.yCount):
            for x in range(0, self.xCount):
                 if self.MapTiles[x][y].Coll(mx,my) == True:
                     return x,y,True
        return -1,-1,False

    def NowToMakeTile(self,now):
        self.NowDraw.NowDrawTiles[2] = MYTILECOLORLIST[now]
        self.NowDraw.NowNumber = now
    def NewCreateTile(self,tempx,tempy,number):
        if self.MapTiles[tempx][tempy].Type == number:
            return;
        if number == NOTILE:
            self.MapTiles[tempx][tempy] = NoTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
        elif number == ONETILE:
            self.MapTiles[tempx][tempy] = OneTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx,tempy)
        elif number == TWOTILE:
            self.MapTiles[tempx][tempy] = TwoTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
        elif number == THREETILE:
            self.MapTiles[tempx][tempy] = TheerTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
        elif number == FOURTILE:
            self.MapTiles[tempx][tempy] = FourTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
        elif number == FIVETILE:
            self.MapTiles[tempx][tempy] = FiveTile(self.nowtype, 60 + (self.xSize / 2) + (tempx * self.xSize),100 + self.ySize / 2 + (tempy * self.ySize), tempx, tempy)
    def MoveColl(self,DownTile,UpTile,x,y):
        if UpTile.Type == NOTILE or DownTile.Type == NOTILE or UpTile.Type == DownTile.Type:
            return
        else:
            self.UI.ClearCount += 1
            self.StartCoroutine(self.StartColl(DownTile,x,y,UpTile.Type,False))

    def StartColl(self,PivTile,x,y,chagecolor,clear): # 누른타일 # 바껴야할 타일 # 바껴야할타일x,y #바껴야할타일의 처음 색상

        if PivTile.Type != self.MapTiles[x][y].Type and chagecolor == self.MapTiles[x][y].Type and self.MapTiles[x][y].Type != NOTILE:
            self.NewCreateTile(x,y,PivTile.Type)
            yield WaitForSeconds(0.035)
            if x > 0:
                self.StartCoroutine(self.StartColl(PivTile,x-1,y,chagecolor,clear))
            if x < self.xCount:
                self.StartCoroutine(self.StartColl(PivTile,x+1,y,chagecolor,clear))
            if y > 0:
                self.StartCoroutine(self.StartColl(PivTile,x,y-1,chagecolor,clear))
            if y < self.yCount:
                self.StartCoroutine(self.StartColl(PivTile,x,y+1,chagecolor,clear))
            if clear == False:
               yield  WaitForSeconds(1)
               if self.ClearCheck() == True:
                   self.savefile.Save(self.nowtype,self.UI.ClearCount,self.UI.Number,self.TempMapTiles,self.xCount,self.yCount)
               clear = True

    def ClearCheck(self):
        for y in range(0, self.yCount):
            for x in range(0, self.xCount):
                if self.UI.Number != self.MapTiles[x][y].Type and self.MapTiles[x][y].Type != NOTILE:
                    return False
        return True

