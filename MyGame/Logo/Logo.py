import Menu.Menu
import game_framework
from MyUtile.mycoroutine import *

from mydefine import *
# 60 70
class LogoObject(Coroutine):
    image = None
    def __init__(self,x,y,n,n1):
        super(LogoObject,self).__init__()
        self.StartX = x
        self.StartY = y
        self.Color = n1
        self.W = 65
        self.H = 75
        self.FirstColor = n
        self.P = True
        if LogoObject.image == None:
            LogoObject.image = load_image("res/6x8.png")
    def __del__(self):
        self.AllStop()

    def Draw(self):
        LogoObject.image.drawRGB(self.StartX,self.StartY,self.FirstColor,self.W,self.H)
    def Update(self):
        self.RunCoroutine()
    def ChageColor(self,n = 1):
        self.FirstColor = self.Color
        self.StartCoroutine(self.__StartInitTile(n))
    def __StartInitTile(self,n):
        for i in range(0, 10):
            yield WaitForSeconds(0.002)
            self.W += 1
            self.H += 1
        self.StartCoroutine(self.__ReturnInitTile(n))
    def __ReturnInitTile(self,n):
        for i in range(0, 10):
            yield WaitForSeconds(0.001)
            self.W -= 1
            self.H -= 1
class LogoManager(Coroutine):
    def __init__(self):


        self.Now = 0
        self.Back = load_image("res/Back.png")
        Colors = [SDL_Color(218,51,64),SDL_Color(255,205,0),SDL_Color(40,170,226),SDL_Color(255,255,255)]
        super(LogoManager,self).__init__()
        self.LogoTile =  [[0 for y in range(12)] for x in range(10)]
        for i in range(0,12):
            for j in range(0,10):
                self.LogoTile[j][i] = LogoObject(30 + (j *60),665 - (i * 70),SDL_Color(0,0,0),Colors[self.CheckColor(j,i)])
        self.StartCoroutine(self.StartLogo())
    def StartLogo(self):
        yield WaitForSeconds(0.4)
        self.StartCoroutine(self.GoLose(0,0))
    def GoLose(self,x,y):
        if(self.LogoTile[x][y].Color != self.LogoTile[x][y].FirstColor):


            self.LogoTile[x][y].ChageColor()
            yield WaitForSeconds(0.035)
            if x > 0:
                self.StartCoroutine(self.GoLose(x - 1, y))
            if x < 9:
                self.StartCoroutine(self.GoLose(x + 1, y))
            if y > 0:
                self.StartCoroutine(self.GoLose(x, y - 1))
            if y < 11:
                self.StartCoroutine(self.GoLose(x, y + 1))
            self.Now+=1
            if(self.Now == 120):
                yield  WaitForSeconds(0.25)
                for i in range(0, 12):
                    for j in range(0, 10):
                        self.LogoTile[j][i].ChageColor()
                self.Now = 0
                yield WaitForSeconds(0.7)
                game_framework.change_state(Menu.Menu)

    def __del__(self):
        del(self.Back)
        del(self.LogoTile)
        del LogoObject.image
    def CheckColor(self,x,y):
        if (x,y) == (0,1) or (x,y) == (3,1) or (x,y) == (0,2) or (x,y) == (2,2) or (x,y) == (0,3) or(x,y) == (1,3) or (x,y) == (0,4) or (x,y) == (2,4) or (x,y) == (0,5) or (x,y) == (3,5):
            return 0
        elif (x,y) == (4,3) or (x,y) == (5,3) or (x,y) == (6,3) or (x,y) == (4,4) or (x,y) == (6,4) or(x,y) == (4,5) or (x,y) == (5,5) or (x,y) == (6,5) or (x,y) == (4,6) or (x,y) ==(4,7):
            return 1
        elif (x,y) == (7,5) or (x,y) == (9,5) or (x,y) == (9,6) or (x,y) == (7,7) or (x,y) == (9,7) or(x,y) == (7,8) or (x,y) == (9,8) or (x,y) == (7,6)  or (x,y) == (8,8):
            return 2
        else:
            return 3

    def Draw(self):
        self.Back.draw(300,350)
        for i in range(0, 12):
            for j in range(0, 10):
                self.LogoTile[j][i].Draw()
    def Update(self):
        self.RunCoroutine()
        for i in range(0, 12):
            for j in range(0, 10):
                self.LogoTile[j][i].Update()



def enter():

    open_canvas(600, 700, sync=True)
    global Manager
    global sound
    global time
    time = 0
    sound = load_wav("res/sound/Button/Logo_Effect.wav")
    sound.set_volume(100)
    sound.play()
    Manager = LogoManager()
def exit():
    global Manager
    global sound

    del(Manager)
    del (sound)

def update(frame_time):
    global Manager
    global sound
    global time
    time += frame_time
    if sound != None:
        if sound.get_volume()  > 0:
            if time > 0.05:
                sound.set_volume(sound.get_volume() - 1)
                time = 0

    Manager.Update()


def draw(frame_time):
    # fill here
    global Manager

    clear_canvas()
    Manager.Draw()
    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
            pass

def pause(): pass
def resume(): pass