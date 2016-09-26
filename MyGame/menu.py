from pico2d import *
import game_framework
import game
from MyUtile.myfadeinfadeout import *
from mydefine import *


def enter():

    global  FadeinOut
    open_canvas(600, 700, sync=True)
    FadeinOut = FadeInFadeOut()


def exit():
    global FadeinOut

    # fill here
    del(FadeinOut)

def update(frame_time):
    FadeinOut.Update()

def draw(frame_time):
    global FadeinOut

    # fill here
    clear_canvas()
    FadeinOut.Draw()
    update_canvas()

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.change_state(game)

def pause(): pass
def resume(): pass

