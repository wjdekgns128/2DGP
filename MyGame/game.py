from pico2d import *
import game_framework
from Map.Map import *
from MyUtile.myfadeinfadeout import *
from mydefine import *


def enter():
    global  FadeinOut
    global  DrawMap
    DrawMap = Map()
    FadeinOut = FadeInFadeOut()

def exit():
    global FadeinOut
    global DrawMap
    del (DrawMap)
    del (FadeinOut)
def update(frame_time):
    FadeinOut.Update()

def draw(frame_time):
    global FadeinOut
    global DrawMap

    # fill here
    clear_canvas()
    FadeinOut.Draw()
    update_canvas()

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.quit()


def pause(): pass
def resume(): pass

