from pico2d import *
import game_framework
import ColorShop.ColorShop
from MyUtile.myfadeinfadeout import *
from mydefine import *
def enter():
    print("메뉴")
    global  FadeinOut
    global BackImage
    BackImage = load_image("res/Back.png")
    FadeinOut = FadeInFadeOut()

def exit():
    global FadeinOut
    global BackImage

    # fill here
    del(BackImage)
    del(FadeinOut)

def update(frame_time):
    FadeinOut.Update()

def draw(frame_time):
    global FadeinOut
    global BackImage

    # fill here
    clear_canvas()
    BackImage.draw(300,350)
    FadeinOut.Draw()
    update_canvas()

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_0):
            game_framework.change_state(ColorShop.ColorShop)


def pause(): pass
def resume(): pass

