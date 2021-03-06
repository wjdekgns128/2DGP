from pico2d import *
import game_framework
from MapPy.mybuttons import mybuttons
from MapPy.map import map
from mydefine import *
from MapPy.filesave import *

check = False
Buttons = []
name = "MapTool"
def enter():
    global Map
    global imste;
    end = MYTILECOLORLIST.__len__()

    open_canvas(600,700,sync = True)
    for i in range(0,end):
        if i == 0:
            Buttons.append(mybuttons('res/8x10_click.png', 40 + (i * 70), 660, MYTILECOLORLIST[i]))
        else:
            Buttons.append(mybuttons('res/8x10.png', 40 +( i * 70), 660, MYTILECOLORLIST[i]))
    Buttons.append(mybuttons('res/loadimage.png',570,660))
    imste = load_image("res/Back.png")
    Map = map(MAPTYPE1)
def exit():
    # fill here
    global Map
    del Map
    close_canvas()
    pass

def update(frame_time):
    Map.Update()


def draw(frame_time):
    # fill here
    global imste;

    global check
    clear_canvas()
    imste.draw(300,350)

    Map.Draw()
    for i in range(0,Buttons.__len__()):
        Buttons[i].Draw()
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
            if(check == True):
                ctypes.windll.user32.MessageBoxW(0, "게임 플레이모드 (맵변경불가)", "!",0)
            else:
                ctypes.windll.user32.MessageBoxW(0, "게임 제작모드 (플레이불가)", "!",0)
            for i in range(0, Buttons.__len__()):
                Buttons[i].Hide(not check)
            Map.ReSetting()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if check == False:
                Map.ChageMap((Map.nowtype+1)%3)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            for i in range(0, Buttons.__len__()):
                if Buttons[i].Coll(event.x, 700 - event.y) == True:
                    if i == Buttons.__len__()-1:
                        check1, maptype, count, clear, mylist = fileload().loadfile()
                        if check1 == True:
                            Map.ChageMap(maptype)
                            Map.LoadSetting(clear,mylist)
                            Map.ReSetting()

                        break;
                    else:
                        Map.NowToMakeTile(i)
                        break
        if check == False:
            Map.MouseMake(event)
        else:
            Map.MousePlay(event)

def pause(): pass
def resume(): pass

