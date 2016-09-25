from pico2d import *
import game_framework
from mydefine import *


def enter():
    open_canvas(600, 800, sync=True)
def exit():
    # fill here
    close_canvas()
    pass

def update(frame_time):
    pass

def draw(frame_time):
    # fill here
    clear_canvas()

    update_canvas()

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.quit()

def pause(): pass
def resume(): pass
