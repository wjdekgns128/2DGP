from pico2d import *

import game_framework
from MapPy.map import map
from mydefine import *
check = False
name = "MapTool"
def enter():
    global Map
    global checkimage
    open_canvas(600,800,sync = True)
    Map = map(MAPTYPE1)
    checkimage = load_image("res/check.png")
def exit():
    # fill here
    close_canvas()
    pass

def update(frame_time):
    pass


def draw(frame_time):
    # fill here
    global checkimage
    clear_canvas()
    Map.Draw()
    if check == False:
        checkimage.draw(40,40)
    update_canvas()

def handle_events(frame_time):
    global check
    global Map

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type,event.key)  == (SDL_KEYDOWN,SDLK_a):
            check = not check
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if check != False:
                Map.ChageMap((Map.nowtype+1)%3)

def pause(): pass
def resume(): pass