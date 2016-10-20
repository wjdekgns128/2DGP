import ColorShop.ColorShop
import Menu.Menu
import Game.Game
from MyUtile.myfadeinfadeout import *
from pico2d import *
import game_framework
from mydefine import *
class SeleteButton:
    StageImage = None
    StageClearIcon = None
    def __init__(self,x,y,n,imge,l):
        self.NowNumber = n
        self.StartX = x
        self.StartY = y
        self.Nowc = l
        self.CheckImage = imge
        if SeleteButton.StageImage == None:
            SeleteButton.StageImage = load_image("res/Selete/StageButton.png")
        if SeleteButton.StageClearIcon == None:
            SeleteButton.StageClearIcon = load_image("res/Selete/CheckIcon.png")
    def Draw(self):
        SeleteButton.StageImage.draw(self.StartX,self.StartY)
        self.CheckImage.draw(self.StartX,self.StartY,50,50)
        if Sing_MapListManager.ClearNumber[self.Nowc][15 - self.NowNumber] == 1:
            SeleteButton.StageClearIcon.draw(self.StartX-20, self.StartY+30,40,40)
    def Down(self,f):
        self.CheckImage.opacify(f)
        SeleteButton.StageImage.opacify(f)
        SeleteButton.StageClearIcon.opacify(f)
    def Coll(self,x1, y1):
        left, bottom, right, top = self.StartX - 27,self.StartY - 27,self.StartX + 27, self.StartY + 27
        left1, bottom1, right1, top1 = x1 - 2, y1 - 2, x1 + 2, y1 + 2
        if left > right1:
            return False
        if right < left1:
            return False
        if top < bottom1:
            return False
        if bottom > top1:
            return False
        return True
class SeeteList:
    def __init__(self,image,n,x,y,naem):
        self.MyFontText = load_font("res/font/GodoB.ttf", 40)
        self.MyFontText1 = load_font("res/font/GodoB.ttf", 50)

        self.ButtonList = []
        self.NowImage = image
        self.Name = naem
        self.CheckImage = [load_image("res/nobutton.png"),load_image("res/okbutton.png")]
        self.NameImage = load_image("res/Selete/Name_BG.png")
        self.Look = load_image("res/Selete/look.png")
        self.Back = load_image("res/Selete/Chapter_Lock.png")
        self.BuyImage = load_image("res/Block_Image.png")
        self.Sic = load_image("res/Star_Icon.png")
        self.Back.opacify(0.7)
        self.NowCh = n
        self.StartX = x
        self.StartY = y
        self.Check = Sing_MapListManager.ClearCh[self.NowCh]
        for i in range(0,Sing_MapListManager.GetStage(self.NowCh)):
            self.ButtonList.append(SeleteButton(self.StartX +390 - ((i%4) * 70),self.StartY -150 + ((int(i/4)) * 100),15-i,self.CheckImage[Sing_MapListManager.ClearNumber[self.NowCh][i]],self.NowCh))
    def Draw(self):
        self.NowImage.draw(self.StartX,self.StartY)
        self.NameImage.draw(self.StartX+10,self.StartY+210)
        self.MyFontText.draw(self.StartX-70,self.StartY+215,self.Name,color = (255,255,255))
        for i in range(0,self.ButtonList.__len__()):
            self.ButtonList[i].Draw()
        if self.Check == 0:
            self.Back.draw(self.StartX+150,self.StartY,1100,680)
            self.Look.draw(self.StartX+150, self.StartY+100)
            self.BuyImage.draw(self.StartX+150,self.StartY-100,220,120)
            self.Sic.draw(self.StartX+70,self.StartY-100)
            self.MyFontText1.draw(self.StartX+110,self.StartY-105,"2000")
    def __del__(self):
        del(self.MyFontText)
        del(self.NameImage)
    def Down(self,f):
        self.NowImage.opacify(f)
        if f <= 0.7:
            self.Back.opacify(f)
        self.NameImage.opacify(f)
        self.BuyImage.opacify(f)
        self.Look.opacify(f)
        self.Sic.opacify((f))
        for i in range(0, self.ButtonList.__len__()):
            self.ButtonList[i].Down(f)
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
class SeleteMain(Coroutine):
    def __init__(self):
        self.Pop1 = False
        super(SeleteMain, self).__init__()

        self.NowDraw = Sing_MapListManager.NowCh
        self.PopUp = False
        self.ChName = ["Nation","Games"]
        self.BackButton = load_image("res/Home.png")
        self.StartIcon = load_image("res/Star_Icon.png")
        self.Shop = load_image("res/Shop.png")
        self.FageFontText = load_font("res/font/GodoB.ttf", 40)
        self.FageFontText1 = load_font("res/font/GodoB.ttf", 55)
        self.StoreButton = load_image("res/StoreButton.png")
        self.StartButton = load_image("res/StartButton.png")
        self.MyFontText = load_font("res/font/GodoB.ttf", 20)
        self.ChImage = [load_image("res/Selete/ch1.png"),load_image("res/Selete/ch2.png")]
        self.FontText = load_font("res/font/GodoB.ttf", 70)
        self.Button = [load_image("res/okbutton.png"), load_image("res/nobutton.png")]
        self.PopBackImage = load_image("res/Block_Image.png")
        self.List = []
        for i in range(0,Sing_MapListManager.GetChatper()):
            self.List.append(SeeteList(self.ChImage[i],i,160 ,300,self.ChName[i]))
        self.FadeCheck = False
    def __del__(self):
        self.AllStop()

        del(self.ChImage)
        del(self.BackButton)
        del(self.StartIcon)
        del(self.Shop)
        del(self.MyFontText)
        del(self.FageFontText)
        del (self.Button)
        del (self.FontText)
        del (self.PopBackImage)
        del (self.FageFontText1)
        del (self.List)
        del (self.StartButton)
        del (self.StoreButton)

    def Update(self):
        self.RunCoroutine()
    def Down(self,c):
        if self.FadeCheck== True:
            return
        self.PopUp = False
        self.Pop1 = False
        self.FadeCheck = True
        for i in range(0,11):
            s = 1 - (i * 0.1)
            self.List[self.NowDraw].Down(s)
            yield WaitForSeconds(0.025)
        self.NowDraw +=c
        self.List[self.NowDraw].Down(0)
        self.StartCoroutine(self.Up())
    def Up(self):
        for i in range(1, 11):
            s =  (i * 0.1)
            self.List[self.NowDraw].Down(s)
            yield WaitForSeconds(0.02)
        self.FadeCheck = False
    def Draw(self):
        self.StartButton.draw(542,650)
        self.BackButton.draw(540, 650)
        self.StartButton.draw(442,650)
        self.Shop.draw(440,650)
        self.StoreButton.draw(323,650,150,90)
        self.StartIcon.draw(350, 665, 45, 45)
        self.StartIcon.draw(290, 665, 45, 45)
        self.MyFontText.draw(270, 623, str(Sing_UserManager.NowMoney), color=(255, 255, 255))
        self.List[self.NowDraw].Draw()
        self.FageFontText.draw(260,30,str(self.NowDraw+1)+" / "  + str(Sing_MapListManager.GetChatper()),color= (255,255,255))
        if (self.PopUp == True):
            self.PopBackImage.draw(300, 350, 400, 500)
            self.FontText.draw(235, 400, "Buy?")
            for i in range(0, 2):
                self.Button[i].draw(230 + (i * 140), 280)
        elif self.Pop1 == True:
            self.PopBackImage.draw(300, 350, 400, 500)
            self.FageFontText1.draw(225, 400, "Menu?")
            for i in range(0, 2):
                self.Button[i].draw(230 + (i * 140), 280)
    def Event(self,event):
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.PopUp == False and self.Pop1 == False:
                for i in range(0, self.List[self.NowDraw].ButtonList.__len__()):
                    if self.List[self.NowDraw].ButtonList[i].Coll(event.x, 700 - event.y): # 게임
                        if Sing_MapListManager.GetChClear(self.NowDraw) == 1:
                            Sing_MapListManager.NowCh = self.NowDraw
                            Sing_MapListManager.NowStage = 15 - i
                            game_framework.change_state(Game.Game)
                            return
                if self.List[self.NowDraw].Coll(self.List[self.NowDraw].StartX + 150,self.List[self.NowDraw].StartY -100,100,40,event.x,700-event.y ) and self.List[self.NowDraw].Check == 0:
                        self.PopUp = True
                elif self.Coll(440,650,self.Shop.w/2,self.Shop.h/2,event.x , 700- event.y):
                        Sing_ColorLisManager.ChageColorShopNumber = 1
                        game_framework.change_state(ColorShop.ColorShop)
                        return True
                elif self.Coll(540,650,self.BackButton.w/2,self.BackButton.h/2,event.x,700-event.y):
                        game_framework.change_state(Menu.Menu)
                        return True
                elif event.x < 300:
                    if self.NowDraw <= 0:
                        return
                    self.StartCoroutine(self.Down(-1))
                elif event.x > 300:
                    if self.NowDraw >= Sing_MapListManager.GetChatper() - 1:
                        return
                    self.StartCoroutine(self.Down(1))


            elif self.PopUp == True:
                for i in range(0, 2):
                    if self.Coll(230 + (i * 140), 280, 90,90,event.x, 700 - event.y):
                        if i == 0:
                            #돈 있는지체크
                            if Sing_UserManager.NowMoney >= 2000:
                                Sing_UserManager.NowMoney -= 2000
                                Sing_UserManager.Save()
                                self.PopUp = False
                                self.List[self.NowDraw].Check = 1
                                Sing_MapListManager.SaveCh(self.NowDraw)
                                return
                        else:
                            self.PopUp = False
                            return
            elif self.Pop1 == True:
                for i in range(0, 2):
                    if self.Coll(230 + (i * 140), 280, 90, 90, event.x, 700 - event.y):
                        if i == 0:
                            # 돈 있는지체크
                                game_framework.change_state(Menu.Menu)
                                self.Pop1 = False
                                return True
                        else:
                            self.Pop1 = False
                            return
        elif(event.type,event.key) == (SDL_KEYDOWN,SDLK_RIGHT):
            if self.NowDraw >= Sing_MapListManager.GetChatper()-1:
                return
            self.StartCoroutine(self.Down(1))
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.NowDraw <= 0:
                return
            self.StartCoroutine(self.Down(-1))
        return False
    def Coll(self, x1, y1,w1,h1, x2, y2):
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
def enter():
    print("선택창")
    global  FadeinOut
    global  SeleteManager
    global BackImage
    global check

    SeleteManager = SeleteMain()
    check = True
    BackImage = load_image("res/Back.png")
    FadeinOut = FadeInFadeOut()


def exit():
    global BackImage
    global  FadeinOut
    del(BackImage)
    del(FadeinOut)

def update(frame_time):
    global  SeleteManager
    global FadeinOut
    FadeinOut.Update()
    SeleteManager.Update()
def draw(frame_time):
    # fill here
    clear_canvas()
    BackImage.draw(300, 350)
    SeleteManager.Draw()
    FadeinOut.Draw()
    update_canvas()

def handle_events(frame_time):
    global  SeleteManager
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            SeleteManager.Pop1 = not SeleteManager.Pop1

        else:
            if SeleteManager.Event(event) == True:
                events.clear()
                return
def pause(): pass
def resume(): pass