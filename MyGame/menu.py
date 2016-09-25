from pico2d import *
import game_framework
import menu
from MyUtile.myfadeinfadeout import *
from mydefine import *


def enter():

    global  FadeinOut
    global  drawimage
    open_canvas(600, 800, sync=True)
    FadeinOut = FadeInFadeOut()
    drawimage = load_image("res/back.png")


def exit():
    global FadeinOut
    global  drawimage

    # fill here
    del(FadeinOut)
    del(drawimage)
    close_canvas()

def update(frame_time):
    FadeinOut.Update()

def draw(frame_time):
    global FadeinOut
    global  drawimage

    # fill here
    clear_canvas()
    drawimage.draw(300,400)
    FadeinOut.Draw()
    update_canvas()

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.change_state(menu)

def pause(): pass
def resume(): pass

