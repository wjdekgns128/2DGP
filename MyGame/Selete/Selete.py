import ColorShop.ColorShop
import Menu.Menu
from MyUtile.myfadeinfadeout import *
from pico2d import *
import game_framework
from mydefine import *
class SeleteButton:
    def __init__(self,x,y,n,imge):
        self.NowNumber = n
        self.StartX = x
        self.StartY = y
        self.CheckImage = imge
        self.StageImage = load_image("res/Selete/StageButton.png")
    def Draw(self):
        self.StageImage.draw(self.StartX,self.StartY)
        self.CheckImage.draw(self.StartX,self.StartY,50,50)
class SeeteList:
    def __init__(self,image,n,x,y,naem):
        self.MyFontText = load_font("res/font/GodoB.ttf", 40)
        self.ButtonList = []
        self.NowImage = image
        self.Name = naem
        self.CheckImage = [load_image("res/nobutton.png"),load_image("res/okbutton.png")]
        self.NameImage = load_image("res/Selete/Name_BG.png")
        self.NowCh = n
        self.StartX = x
        self.StartY = y
        for i in range(0,Sing_MapListManager.GetStage(self.NowCh)):
            self.ButtonList.append(SeleteButton(self.StartX +180 + ((i%4) * 70),self.StartY -150 + ((int(i/4)) * 100),i,self.CheckImage[Sing_MapListManager.ClearNumber[self.NowCh][i]]))
    def Draw(self):
        self.NowImage.draw(self.StartX,self.StartY)
        self.NameImage.draw(self.StartX+10,self.StartY+210)
        self.MyFontText.draw(self.StartX-70,self.StartY+215,self.Name,color = (255,255,255))
        for i in range(0,self.ButtonList.__len__()):
            self.ButtonList[i].Draw()
    def __del__(self):
        del(self.MyFontText)
        del(self.NameImage)
class SeleteMain:
    def __init__(self):
        self.NowDraw = 0
        self.ChName = ["Nation","Games"]
        self.BackButton = load_image("res/Home.png")
        self.StartIcon = load_image("res/Star_Icon.png")
        self.Shop = load_image("res/Shop.png")
        self.MyFontText = load_font("res/font/GodoB.ttf", 20)
        self.ChImage = [load_image("res/Selete/ch1.png"),load_image("res/Selete/ch2.png")]
        self.List = []
        for i in range(0,Sing_MapListManager.GetChatper()):
            self.List.append(SeeteList(self.ChImage[i],i,160 ,300,self.ChName[i]))
    def __del__(self):
        del(self.List)
        del(self.ChImage)
        del(self.BackButton)
        del(self.StartIcon)
        del(self.Shop)
        del(self.MyFontText)
    def Update(self):
        pass
    def Draw(self):
        self.BackButton.draw(530, 650)
        self.Shop.draw(440,650)
        self.StartIcon.draw(350, 665, 45, 45)
        self.StartIcon.draw(290, 665, 45, 45)
        self.MyFontText.draw(270, 625, str(Sing_UserManager.NowMoney), color=(255, 255, 255))
        self.List[self.NowDraw].Draw()
    def Event(self,event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(Menu.Menu)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.Coll(440,650,self.Shop.w/2,self.Shop.h/2,event.x , 700- event.y):
                game_framework.change_state(ColorShop.ColorShop)
            elif self.Coll(530,650,self.BackButton.w/2,self.BackButton.h/2,event.x,700-event.y):
                game_framework.change_state(Menu.Menu)

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
    BackImage = load_image("res/Back.png")
    FadeinOut = FadeInFadeOut()
    SeleteManager = SeleteMain()


def exit():
    global BackImage
    global  FadeinOut
    global  SeleteManager
    del(BackImage)
    del(SeleteManager)
    del(FadeinOut)

def update(frame_time):
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
    events = get_events()
    for event in events:
        SeleteManager.Event(event)

def pause(): pass
def resume(): pass