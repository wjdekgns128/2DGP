import ColorShop.ColorShop
from MyUtile.myfadeinfadeout import *
from pico2d import *
import game_framework
from mydefine import *

class SeleteMain:
    def __init__(self):
        self.BackButton = load_image("res/Home.png")
        self.StartIcon = load_image("res/Star_Icon.png")
        self.Shop = load_image("res/Shop.png")

        self.MyFontText = load_font("res/font/GodoB.ttf", 20)
    def Update(self):
        pass
    def Draw(self):
        self.BackButton.draw(530, 650)
        self.Shop.draw(440,650)

        self.StartIcon.draw(350, 665, 45, 45)
        self.StartIcon.draw(290, 665, 45, 45)
        self.MyFontText.draw(270, 625, str(Sing_UserManager.NowMoney), color=(255, 255, 255))
    def Event(self,event):
        pass
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
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.change_state(ColorShop.ColorShop)

def pause(): pass
def resume(): pass