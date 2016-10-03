from pico2d import *
import game_framework
import Selete.Selete
import Menu.Menu
import mydefine
from MyUtile.myfadeinfadeout import *
from mydefine import *
class ColorShopList:
    def __init__(self,x,y,n): # x,y,칼라 넘버
        self.BackImage = load_image("res/Block_Image.png")
        self.FontText = load_font("res/font/GodoB.ttf",30)
        self.FontText1 = load_font("res/font/GodoB.ttf",22)
        self.BuyImage = [load_image("res/Star_Icon.png"),load_image("res/Tick.png"),load_image("res/Tick_Click.png")]
        self.x = x
        self.y = y
        self.Number = n
        self.Name = Sing_ColorLisManager.GetColorName(n)
        self.Money = Sing_ColorLisManager.GetColorMoney(n)
        self.ColorList = Sing_ColorLisManager.GetColorAll(n)

        self.ColorImage = load_image("res/6x8.png")
        self.state = BUY  #사야되는 상황 # 가지고있는상황, # 장착중인 상황 BUY,GET,SELETE
    def __del__(self):
        del(self.ColorImage)
        del(self.BackImage)
        del(self.FontText)
        del(self.FontText1)
        del(self.BuyImage)
    def Draw(self):
        if( self.y < 550):
            self.BackImage.draw(self.x + 130, self.y)
            for i in range(0,self.ColorList.__len__()):
                self.ColorImage.drawRGB(self.x+ (65 * i),self.y,self.ColorList[i],65,65)
            self.FontText.draw(self.x-27,self.y+50,self.Name,color = (255,255,255))
            self.BuyImage[self.state].draw(self.x+340,self.y+5)
            if self.state == BUY:
                self.FontText1.draw(self.x+315,self.y+2,self.Money)
            else:
                self.BuyImage[0].draw(self.x+290,self.y+35,25,25)
    def Setting(self,y):
        self.y += y
    def SetBuy(self):
        self.state = GET
        #Sing_UserManager.NowM
    def RealBuy(self):
        if(Sing_UserManager.NowMoney < int(Sing_ColorLisManager.GetColorMoney(self.Number))):
            return True
        self.SetBuy()
        Sing_UserManager.NowMoney -= (int(Sing_ColorLisManager.GetColorMoney(self.Number)))
        Sing_UserManager.NowBuyColor += 1
        Sing_UserManager.NowBuyColorList.append(self.Number)
        Sing_UserManager.Save()
        return False
    def SetColor(self): #칼라 장착시
        self.state = SELETE
    def Coll(self,x1,y1):
        left, bottom, right, top = self.x + 340 - (self.BuyImage[0].w / 2) , self.y + 5 - (self.BuyImage[0].h / 2) , self.x + 340 + (self.BuyImage[0].w / 2) , self.y  + 5+ (self.BuyImage[0].h / 2)
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
    def CollCheck(self): # return 0 ,1 , 2
        if self.state == BUY:

            return 0
        elif self.state == GET:
            self.state = SELETE
            Sing_UserManager.NowColor = self.Number
            Sing_UserManager.Save()
            return 1
        else:
            return 2
class ColorShopMain:
    def Coll(self,x1,y1,x2,y2):
        left, bottom, right, top = x1-40,y1-40,x1+40,y1+40
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
    def __init__(self):
        self.ColorLists = []
        self.UpOnDown = 0
        self.DownClickCheck = False
        self.DownmouseYPoint = 0
        self.Len = 0
        self.PopUp = False
        self.NowNumber = 0

        self.StoreButton = load_image("res/StoreButton.png")
        self.StartButton = load_image("res/StartButton.png")
        self.BackButton = load_image("res/Home.png")
        self.StartIcon = load_image("res/Star_Icon.png")
        self.MyFontText = load_font("res/font/GodoB.ttf", 20)
        self.FontText = load_font("res/font/GodoB.ttf", 70)
        self.Button = [load_image("res/okbutton.png"), load_image("res/nobutton.png")]
        self.PopBackImage = load_image("res/Block_Image.png")
        self.Count = Sing_ColorLisManager.GetColorMaxCount()
        for i in range(0, self.Count):
            self.ColorLists.append(ColorShopList(60, 535 - (i * 105), i))
        for i in range(0,Sing_UserManager.NowBuyColor):
            self.ColorLists[Sing_UserManager.NowBuyColorList[i]].SetBuy()
        self.Check = Sing_UserManager.NowColor
        self.ColorLists[self.Check].SetColor()
        self.namelmage = load_image("res/ColorShop_Logo.png")
        self.BackImage = load_image("res/Back.png")
    def __del__(self):
        self.AllStop()

        del(self.ColorLists)

        del(self.BackButton)
        del(self.StartIcon)
        del(self.MyFontText)
        del (self.Button)
        del (self.FontText)
        del(self.PopBackImage)
        del( self.namelmage)
        del(self.BackImage )
    def Draw(self):
        self.BackImage.draw(300, 350)
        self.StartButton.draw(551, 650)
        self.BackButton.draw(550,650)
        self.StoreButton.draw(430, 650, 150, 90)
        self.StartIcon.draw(460,665,45,45)
        self.StartIcon.draw(400,665,45,45)

        self.MyFontText.draw(380,622,str(Sing_UserManager.NowMoney),color = (255,255,255))
        for i in range(0, self.Count):
            self.ColorLists[i].Draw()
        if (self.PopUp == True):
            self.PopBackImage.draw(300, 350, 400, 500)
            self.FontText.draw(235,400,"Buy?")
            for i in range(0,2):
                self.Button[i].draw(230 + (i * 140),280)
        self.namelmage.draw(160, 655)
    def Update(self):
        if self.PopUp == False:
            if self.DownClickCheck == False and not self.Len == 0:
                if self.UpOnDown == 1:
                    if self.ColorLists[0].y < self.Count * 105:
                        for i in range(0, self.Count):
                            self.ColorLists[i].Setting(10)
                elif self.UpOnDown == 2:
                    if self.ColorLists[0].y > 535:
                        for i in range(0, self.Count):
                            self.ColorLists[i].Setting(-10)
                self.Len -= 1
        else:
            pass

    def Mouse(self,event):


        if(event.type,event.button) == (SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
            if self.Coll(550,650,event.x,700-event.y):
                if Sing_ColorLisManager.ChageColorShopNumber == 0:
                    game_framework.change_state(Menu.Menu)
                else:
                    game_framework.change_state(Selete.Selete)

                return True
            elif self.PopUp == False:
                for i in range(0, self.Count):
                    if self.ColorLists[i].Coll(event.x , 700-event.y):
                        if self.ColorLists[i].CollCheck() == 1:
                                self.ColorLists[self.Check].SetBuy()
                                self.Check = i
                                break
                        elif self.ColorLists[i].CollCheck() == 0:
                            self.PopUp = True # 팝업창등장
                            self.NowNumber = i
                            break
                        return
                self.DownClickCheck = True
                self.DownmouseYPoint = 700 - event.y
                self.UpOnDown = 0
                self.Len = 0
            else:
                testcheck = False
                for i in range(0, 2):
                    if self.Coll(230 + (i * 140),280,event.x,700-event.y):
                        if i == 0:
                            testcheck = self.ColorLists[self.NowNumber].RealBuy()
                        self.PopUp = testcheck
                        self.NowNumber = 0
                        break

        elif (event.type) == SDL_MOUSEBUTTONUP:
            self.DownClickCheck = False
            if self.UpOnDown == 1:
                self.Len = (self.GetLen(700 - event.y, self.DownmouseYPoint + 5)) + 7
            elif self.UpOnDown == 2:
                self.Len = (self.GetLen(700 - event.y, self.DownmouseYPoint - 5)) + 7


        elif (event.type == (SDL_MOUSEMOTION)):
            check = 0
            if self.DownClickCheck == True:
                if (700 - event.y> self.DownmouseYPoint+5):
                   if self.ColorLists[0].y < self.Count * 105:
                       self.UpOnDown = 1
                       check = 13
                   else:
                      self.UpOnDown = 0
                elif (700 - event.y < self.DownmouseYPoint-5):
                   if self.ColorLists[0].y > 535:
                       self.UpOnDown = 2
                       check = -13
                   else:
                      self.UpOnDown = 0
                else:
                  self.UpOnDown = 0
                  self.Len = 0
                  return
                self.DownmouseYPoint = 700 - event.y
                for i in range(0, self.Count):
                    self.ColorLists[i].Setting(check)

        return False
    def GetLen(self,y,y1): # 850 , 535
        return (int(math.fabs(y - y1)%100))

    def Coll(self, x1, y1, x2, y2):
        left, bottom, right, top = x1 - 40, y1 - 35, x1 + 40, y1 + 35
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
    print("컬러샵")
    global  ColorManager
    ColorManager = ColorShopMain()

def exit():
    pass
    # fill here

def update(frame_time):
    global ColorManager
    ColorManager.Update()
def draw(frame_time):
    global ColorManager

    # fill here

    clear_canvas()
    ColorManager.Draw()

    update_canvas()

def handle_events(frame_time):
    global ColorManager
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            if ColorManager.PopUp == False:
                if Sing_ColorLisManager.ChageColorShopNumber == 0:
                    game_framework.change_state(Menu.Menu)
                else:
                    game_framework.change_state(Selete.Selete)
                events.clear()
                return
            else:
                ColorManager.PopUp = False
        else:
            if ColorManager.Mouse(event) == True:
                events.clear()
                return
def pause(): pass
def resume(): pass

