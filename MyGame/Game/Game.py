import game_framework
from mydefine import *
from Game.Map.Map import *



def enter():
    print("게임")
    global GameMapManager
    GameMapManager = Map()
    GameMapManager.MapSetting()
def exit():
    global GameMapManager
    del(GameMapManager)
def update(frame_time):
    global GameMapManager
    GameMapManager.Update()

def draw(frame_time):
    # fill here
    global GameMapManager

    clear_canvas()
    GameMapManager.Draw()
    update_canvas()

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            GameMapManager.PopUp = not GameMapManager.PopUp
        else:
            if(GameMapManager.Event(event) == True):
                events.clear()
                game_framework.pop_state()

def pause(): pass
def resume(): pass

