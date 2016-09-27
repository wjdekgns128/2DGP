from Menu.Menu import *

from mydefine import *


def enter():
    open_canvas(600, 700, sync=True)


def exit():
    pass

def update(frame_time):
    pass
def draw(frame_time):
    global FadeinOut
    # fill here
    clear_canvas()

    update_canvas()

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.change_state(Menu.Menu)

def pause(): pass
def resume(): pass