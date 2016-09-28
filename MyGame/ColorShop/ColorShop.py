from pico2d import *
import game_framework
import Menu.Menu
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

class ColorShopMain:
    def __init__(self):
        self.ColorLists = []
        self.UpOnDown = 0
        self.DownClickCheck = False
        self.DownmouseYPoint = 0
        self.Len = 0
        self.Count = Sing_ColorLisManager.GetColorMaxCount()
        for i in range(0, self.Count):
            self.ColorLists.append(ColorShopList(60, 535 - (i * 105), i))
        self.namelmage = load_image("res/ColorShop_Logo.png")
        self.BackImage = load_image("res/Back.png")
    def Draw(self):
        self.BackImage.draw(300, 350)
        for i in range(0, self.Count):
            self.ColorLists[i].Draw()
        self.namelmage.draw(160, 655)
    def Update(self):

       if self.DownClickCheck == False and not self.Len == 0:
           if self.UpOnDown == 1:
               for i in range(0, self.Count):
                   self.ColorLists[i].Setting(10)
           elif self.UpOnDown == 2:
                for i in range(0, self.Count):
                  self.ColorLists[i].Setting(-10)
           self.Len -= 1


    def Mouse(self,event):
        if(event.type,event.button) == (SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
            self.DownClickCheck = True
            self.DownmouseYPoint = 700 - event.y
            self.UpOnDown = 0
            self.Len = 0
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
                    self.UpOnDown = 1
                    check = 13
                elif (700 - event.y < self.DownmouseYPoint-5):
                    self.UpOnDown = 2
                    check = -13
                else:
                    self.UpOnDown = 0
                    self.Len = 0
                    return
                self.DownmouseYPoint = 700 - event.y
                for i in range(0, self.Count):
                    self.ColorLists[i].Setting(check)

    def GetLen(self,y,y1):
        return (int(math.fabs(y - y1)%100))

def enter():
    print("컬러샵")
    global  FadeinOut
    global ColorManager
    ColorManager = ColorShopMain()
    FadeinOut = FadeInFadeOut()

def exit():
    global FadeinOut

    # fill here
    del(FadeinOut)

def update(frame_time):
    global ColorManager
    FadeinOut.Update()
    ColorManager.Update()
def draw(frame_time):
    global FadeinOut
    global ColorManager

    # fill here
    clear_canvas()

    FadeinOut.Draw()
    ColorManager.Draw()
    update_canvas()

def handle_events(frame_time):
    global ColorManager
    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_9):
            game_framework.change_state(Menu.Menu)
        else:
            ColorManager.Mouse(event)
def pause(): pass
def resume(): pass

