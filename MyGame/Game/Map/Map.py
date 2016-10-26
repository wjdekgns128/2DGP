import game_framework
from Game.Map import Tiles
from Game.Map.Tiles import *
from mydefine import *
from Game.Particle.Particle import *
class FadeInOutName(Coroutine):
    def __init__(self):
        super(FadeInOutName,self).__init__()
        self.Ing = True
        self.Check = False

    def __del__(self):
        self.AllStop()

        del(self.FontText)
        del(self.Back)
    def Start(self):
        self.Ing = True
        self.Check = True
        self.Name = Sing_MapListManager.GetFileName(Sing_MapListManager.NowCh,Sing_MapListManager.NowStage)
        self.FontText = load_font("res/font/GodoB.ttf", 80)
        self.Back = load_image("res/Back.png")
        self.Back.opacify(1)
        self.StartCoroutine(self.DownCor())
    def DownCor(self):
        for i in range(0, 51):
            s = 1 - (i * 0.02)
            self.Back.opacify(s)
            yield WaitForSeconds(0.015)

        self.Ing = False
        self.Check = False
    def Update(self):
        self.RunCoroutine()
    def Draw(self):
        self.Back.draw(300,350)
        if self.Check:
            self.FontText.draw(280 - ((self.Name.__len__()-1)*20),380,self.Name,color = (255,255,255))
class Map(Coroutine):
    def __init__(self):
        super(Map,self).__init__()
        self.ParticleB = []
        for i in range(0, 4):
            self.ParticleB.append(Particle())
        self.Fade = FadeInOutName()
        self.Home = load_image("res/Home.png")
        self.Retry = load_image("Res/Retry.png")
        self.ClearColorImage = load_image("res/6x8.png")
        self.FontText1 = load_font("res/font/GodoB.ttf", 55)
        self.Back = load_image("res/Back.png")
        self.FontText = load_font("res/font/GodoB.ttf", 70)
        self.Button = [load_image("res/okbutton.png"), load_image("res/nobutton.png")]
        self.PopBackImage = load_image("res/Block_Image.png")
        self.ClearP = load_image("res/Panel.png")
        self.ClearP.opacify(0.75)
        self.ClearName = [" ","CLEAR","FAIL.."]
        self.PlayGameimage = load_image("res/Play_game.png")
        self.Icon = load_image("res/Star_Icon.png")
        self.Money = 0
    def __del__(self):
        self.AllStop()
        del (self.ParticleB)
        del(self.PlayGameimage)
        del(self.ClearColorImage)
        del(self.Back)
        del(self.MapTiles)
        del(self.Home)
        del(self.Retry)
        del(self.FontText)
        del(self.FontText1)
        del(self.Button)
        del(self.PopBackImage)
        del(self.ClearP)
        del(self.Fade )
        del(self.Icon)
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
        self.Fade.Start()
        self.AllStop()
        self.Money = 0
        self.NowPlayMapNumber = Sing_MapListManager.NowStage
        self.NowPlayChNumber = Sing_MapListManager.NowCh
        self.PopUp = False
        self.CheckCount = 0
        self.DownButton = False
        self.Chage = 0

        mylist = []
        self.MapType,self.ClearCount,self.ClearColor,mylist = Sing_MapListManager.GetFileData(self.NowPlayChNumber,self.NowPlayMapNumber)
        self.MapCount = (MapSize[self.MapType][0],MapSize[self.MapType][1])
        self.MapSize = (MapTilesSize[self.MapType][0],MapTilesSize[self.MapType][1])
        self.ClickX = 0
        self.ClickY = 0
        self.GameOverCheck = 0
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

        if self.GameOverCheck != 0:
            self.ClearP.draw(300,350,500,500)
            self.FontText.draw(190, 400,self.ClearName[self.GameOverCheck], color=(255, 255, 255))
            self.Home.draw(390,280,90,90)
            self.FontText1.draw(155,475,str(Sing_UserManager.NowMoney),color=(255,255,255))
            self.Icon.draw(130,480,55,55)
            if self.GameOverCheck == 2:
                self.Retry.draw(210,280,90,90)
            else:
                self.PlayGameimage.draw(210,280,90,90)
        if (self.PopUp == True):
            self.PopBackImage.draw(300, 350, 400, 500)
            self.FontText1.draw(225, 400, "Menu?")
            for i in range(0, 2):
                self.Button[i].draw(230 + (i * 140), 280)
        if self.Fade.Ing == True:
            self.Fade.Draw()
        for i in range(0, 4):
            self.ParticleB[i].Draw()
    def Update(self):
        if self.Fade.Ing == False:
            for y in range(0, self.MapCount[1]):
                for x in range(0, self.MapCount[0]):
                    self.MapTiles[x][y].Update()
            for i in range(0, 4):
                self.ParticleB[i].Update()
            self.RunCoroutine()
        else:
            self.Fade.Update()
    def Event(self,event):
        if self.Fade.Ing == True:
            return
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if self.PopUp == False:
                    if self.GameOverCheck == 0:
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
                                        if(not self.MapTiles[x][y].Type == 0 and self.DownButton== False):
                                            self.MapTiles[x][y].ClickDown()
                                            self.ClickX= x
                                            self.ClickY = y
                                        return  False
                    else:
                        if self.Coll(210, 280, 45, 45, event.x, 700 - event.y):
                            if self.GameOverCheck == 2:
                                self.MapSetting()
                            elif self.GameOverCheck == 1:
                                Sing_MapListManager.NowStage +=1
                                if Sing_MapListManager.NowStage >= Sing_MapListManager.GetStage(Sing_MapListManager.NowCh):
                                    if self.Money >= Sing_UserManager.NowMoney:
                                        Sing_UserManager.NowMoney = self.Money
                                        Sing_UserManager.Save()
                                    return True
                                else:
                                    if self.Money >= Sing_UserManager.NowMoney:
                                        Sing_UserManager.NowMoney = self.Money
                                        Sing_UserManager.Save()
                                    self.MapSetting()
                        elif self.Coll(390, 280, 45, 45, event.x, 700 - event.y): #홈
                            self.PopUp = True
                else:
                    for i in range(0, 2):
                        if self.Coll(230 + (i * 140), 280,45,45, event.x, 700 - event.y):
                            if i == 0:
                                if self.Money >= Sing_UserManager.NowMoney:
                                    Sing_UserManager.NowMoney = self.Money
                                    Sing_UserManager.Save()
                                    print("Dasdsa")

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
        return False
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
            self.test = True

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
            if  self.CheckCount == 0:
                if self.test == True:
                    self.GameOver()
                    self.test = False
                    yield WaitForSeconds(0.1)
                    self.DownButton = False


    def GameOver(self):
        self.GameOverCheck =self.ClearGameCheck()
        if(self.GameOverCheck == 1):
            if Sing_MapListManager.ClearNumber[Sing_MapListManager.NowCh][15-Sing_MapListManager.NowStage] != 1:
                self.StartCoroutine(self.UpMoney())
            for i in range(0, 4):
                self.ParticleB[i].ReSetting(i)
            Sing_MapListManager.ClearNumber[Sing_MapListManager.NowCh][15 - Sing_MapListManager.NowStage] = 1
            Sing_MapListManager.Save(Sing_MapListManager.NowCh)
    def UpMoney(self):
        self.Money = Sing_UserManager.NowMoney + 400
        for i in range(0,50):
            Sing_UserManager.NowMoney += 8
            yield WaitForSeconds(0.01)


    def ClearGameCheck(self): # 1클리어 , 2 낫클리어 ,0 기본
        Check = self.Clear()
        if Check:
            if self.ClearCount >= 0:
                return 1
            else:
                return 2
        else:
            if self.ClearCount <= 0:
                return 2
            else:
                return 0
    def Clear(self):
        for y in range(0, self.MapCount[1]):
            for x in range(0, self.MapCount[0]):
                if self.MapTiles[x][y].Type != self.ClearColor and self.MapTiles[x][y].Type != 0:
                    return False
        return True