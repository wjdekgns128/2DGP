from pico2d import *
import game_framework
from Map.Map import *
from MyUtile.myfadeinfadeout import *
from mydefine import *


def enter():
    global  DrawMap
    DrawMap = Map()
    DrawMap.MapSetting(0)

def exit():
    global DrawMap
    del (DrawMap)
def update(frame_time):
    global DrawMap

    DrawMap.Update()
def draw(frame_time):
    global DrawMap
    # fill here
    clear_canvas()
    DrawMap.Draw()
    update_canvas()

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.quit()


def pause(): pass
def resume(): pass

