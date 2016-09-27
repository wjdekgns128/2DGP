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
ColorLists = []
Count = Sing_ColorLisManager.GetColorMaxCount()
def enter():
    print("컬러샵")
    global  FadeinOut
    global BackImage
    global namelmage
    global mousey
    global mousecheck
    global mouseYPoint
    global mouseYPointTemp

    mousecheck = False
    mousey = 0
    mouseYPoint = 0
    mouseYPointTemp = 100
    for i in range(0,Count):
        ColorLists.append(ColorShopList(60,535-(i*105),i))
    namelmage = load_image("res/ColorShop_Logo.png")
    BackImage = load_image("res/Back.png")
    FadeinOut = FadeInFadeOut()

def exit():
    global FadeinOut
    global BackImage
    global namelmage

    # fill here
    del(FadeinOut)
    del(BackImage)
    del(namelmage)

def update(frame_time):
    FadeinOut.Update()
def draw(frame_time):
    global FadeinOut
    global BackImage
    global namelmage

    # fill here
    clear_canvas()
    BackImage.draw(300,350)

    for i in range(0, Count):
        ColorLists[i].Draw()
    namelmage.draw(160,655)
    FadeinOut.Draw()
    update_canvas()

def handle_events(frame_time):
    global mousey
    global mousecheck
    global mouseYPointTemp

    global mouseYPoint
    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_9):
            game_framework.change_state(Menu.Menu)
        elif(event.type,event.button) == (SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
            if(mousecheck == False):
                mousecheck = True
                mouseYPoint  = 700 - event.y
        elif (event.type) == SDL_MOUSEBUTTONUP:
             mousecheck = False
        elif (event.type == (SDL_MOUSEMOTION)):
            testcheck = True
            if mousecheck == True:
                if (700 - event.y< mouseYPoint-5):
                    if(mouseYPointTemp > 100):
                            mousey = -10
                            mouseYPointTemp -= 10
                    else:
                        testcheck = False
                elif (700 - event.y > mouseYPoint+5):
                        if mouseYPointTemp < (Count*105) - 430:
                            mousey = 10
                            mouseYPointTemp += 10
                        else:
                            testcheck = False
                else:
                    testcheck = False

                if testcheck == True:
                    for i in range(0, Count):
                        ColorLists[i].Setting(mousey)
                        mouseYPoint = 700 - event.y
def pause(): pass
def resume(): pass

