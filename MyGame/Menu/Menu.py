from pico2d import *
import game_framework
import Selete.Selete
from MyUtile.myfadeinfadeout import *
from mydefine import *
def enter():
    print("메뉴")
    global  FadeinOut
    global Menu
    Menu = MenuManager()
    FadeinOut = FadeInFadeOut()
    Sing_MapListManager.NowCh = 0
def exit():
    global FadeinOut
    global Menu
    del(Menu)
    # fill here
    del(FadeinOut)

def update(frame_time):
    FadeinOut.Update()

def draw(frame_time):
    global FadeinOut
    global Menu

    # fill here
    clear_canvas()
    Menu.Draw()
    FadeinOut.Draw()
    update_canvas()

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_0):
            game_framework.change_state(Selete.Selete)


def pause(): pass
def resume(): pass


class MenuManager:
    def __init__(self):
        self.BackImage = load_image("res/Back.png")
        self.StarIcon = load_image("res/Star_Icon.png")
        self.StarIconBack = load_image("res/StoreButton.png")
        self.StarButtonBack = load_image("res/StartButton.png")
        self.PlayButton = load_image("res/Play_game.png")
        self.ShopImage = load_image("res/Shop.png")
        self.PlayGame = load_image("res/Play_game.png")
        self.CloseGame = load_image("res/close_game.png")
    def __del__(self):
        del self.BackImage
        del self.StarIconBack
        del self.StarIcon
        del self.StarButtonBack
        del self.PlayButton
        del self.ShopImage
        del self.PlayGame
        del self.CloseGame
    def Draw(self):
        self.BackImage.draw(300, 350)

        self.StarIconBack.draw(235,440,140,140)
        self.StarIcon.draw(235,455,75,75)

        self.StarButtonBack.draw(365, 440, 140, 140)
        self.ShopImage.draw(360,445,90,90)

        self.StarButtonBack.draw(300, 305, 280, 130)
        self.PlayGame.drawRGB(305,305,SDL_Color(255,223,242),120,100)

        self.StarButtonBack.draw(300, 175, 280, 130)
        self.CloseGame.drawRGB(305,175,SDL_Color(255,223,242),120,100)
