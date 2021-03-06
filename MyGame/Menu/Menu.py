from collections import Coroutine
from Game.Particle import *
from pico2d import *
import game_framework
import Selete.Selete
import ColorShop
from Game.Particle.Particle import *
from MyUtile.myfadeinfadeout import *
from mydefine import *
sound = None
effsound = None
def enter():
    print("메뉴")
    global  FadeinOut
    global Menu
    global sound
    global time
    global effsound

    time = 0
    if sound== None:
        sound = load_music("res/sound/BGM/BGM.mp3")
        sound.repeat_play()
        sound.set_volume(0)
    if effsound == None:
        effsound = load_wav('res/sound/Button/ButtonDown.wav')
    Menu = MenuManager()
    FadeinOut = FadeInFadeOut()
    Sing_MapListManager.NowCh = 0



def exit():
    global FadeinOut
    global Menu
    del(Menu)
    # fill here
    del(FadeinOut)

def update(frame_time):
    global Menu
    global sound
    global time
    time += frame_time
    if sound != None:
        if sound.get_volume() < 75:
            if time > 0.05:
                sound.set_volume(sound.get_volume() +1)
                time  = 0
    FadeinOut.Update()

    Menu.Update()
def draw(frame_time):
    global FadeinOut
    global Menu

    # fill here
    clear_canvas()
    Menu.Draw()

    FadeinOut.Draw()
    update_canvas()

def handle_events(frame_time):
    global Menu
    global sound
    global effsound

    events = get_events()
    for event in events:
        if(event.type,event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            Menu.PopUp = not Menu.PopUp
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            check = Menu.Event(event)
            if(check == 1):
                events.clear()
                del sound
                sound = None
                del effsound
                effsound = None
                game_framework.quit()

            elif check == 2:
                sound.set_volume(75)
                effsound.play()
                events.clear()
                game_framework.change_state(Selete.Selete)
            elif check == 3:
                sound.set_volume(75)
                effsound.play()
                events.clear()
                Sing_ColorLisManager.ChageColorShopNumber = 0
                game_framework.change_state(ColorShop.ColorShop)

def pause(): pass
def resume(): pass


class MenuManager(Coroutine):
    def __init__(self):
        super(MenuManager,self).__init__()
        self.BackImage = load_image("res/Back.png")
        self.StarIcon = load_image("res/Star_Icon.png")
        self.StarIconBack = load_image("res/StoreButton.png")
        self.StarButtonBack = load_image("res/StartButton.png")
        self.PlayButton = load_image("res/Play_game.png")
        self.ShopImage = load_image("res/Shop.png")
        self.PlayGame = load_image("res/Play_game.png")
        self.CloseGame = load_image("res/close_game.png")
        self.FontText = load_font("res/font/GodoB.ttf", 70)
        self.FontText1 = load_font("res/font/GodoB.ttf", 25)
        self.TitLogo = load_image("res/Title_Logo.png")
        self.Button = [load_image("res/okbutton.png"), load_image("res/nobutton.png")]
        self.PopBackImage = load_image("res/Block_Image.png")

        self.PopUp= False
        self.StartCoroutine(self.SizeofDown())
        self.Wsize = 0
        self.Hsize = 0
        self.ColorCheck = True
        self.ListColorR = [255,255,255]
        self.ListCOlorNumber = 0
    def SizeofDown(self):
        for i in range(0,6):
            self.Wsize += 1
            self.Hsize += 1
            yield WaitForSeconds(0.1)

        self.StartCoroutine(self.SizeofDown1())
    def SizeofDown1(self):
        for i in range(0, 6):
            self.Wsize -= 1
            self.Hsize -= 1
            yield WaitForSeconds(0.1)

        self.StartCoroutine(self.SizeofDown())
    def __del__(self):
        self.AllStop()
        del self.FontText1
        del self.BackImage
        del self.StarIconBack
        del self.StarIcon
        del self.StarButtonBack
        del self.PlayButton
        del self.ShopImage
        del self.PlayGame
        del self.CloseGame
        del self.Button
        del self.FontText
        del self.PopBackImage
    def Update(self):
        if self.ColorCheck == True:
            self.ListColorR[self.ListCOlorNumber ] -=1
        else:
            self.ListColorR[self.ListCOlorNumber]+=1
        if(   self.ListColorR[self.ListCOlorNumber ] <= 130):
            self.ColorCheck = False
            self.ListCOlorNumber = randint(0,2)
        if(   self.ListColorR[self.ListCOlorNumber ] >= 255):
            self.ColorCheck = True
            self.ListCOlorNumber = randint(0,2)

        self.RunCoroutine()
    def Draw(self):
        self.BackImage.draw(300, 350)
        self.TitLogo.drawRGB(300,585,SDL_Color(self.ListColorR[0],self.ListColorR[1],self.ListColorR[2]),640,200)

        self.StarIconBack.draw(235,440,140,140)
        self.StarIcon.draw(235,455,75,75)
        self.FontText1.draw(180,400,str(Sing_UserManager.NowMoney),color = (255,255,255))

        self.StarButtonBack.draw(365, 440, 140, 140)
        self.ShopImage.draw(360,445,90,90)

        self.StarButtonBack.draw(300, 305, 280, 130)
        self.PlayGame.drawRGB(305,305,SDL_Color(255,223,242),120 + self.Wsize,100 + self.Hsize)

        self.StarButtonBack.draw(300, 175, 280, 130)
        self.CloseGame.drawRGB(305,175,SDL_Color(255,223,242),120,100)
        if (self.PopUp == True):
            self.PopBackImage.draw(300, 350, 400, 500)
            self.FontText.draw(235, 400, "Exit?")
            for i in range(0, 2):
                self.Button[i].draw(230 + (i * 140), 280)
    def Coll(self, x1, y1, w1, h1, x2, y2):
        left, bottom, right, top = x1 - w1, y1 - h1, x1 + w1, y1 + h1
        left1, bottom1, right1, top1 = x2 - 2, y2 - 2, x2 + 2, y2 + 2
        if left > right1:
            return False
        if right < left1:
            return False
        if top < bottom1:
            return False
        if bottom > top1:
            return False
        return True
    def Event(self,event):
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.PopUp == False:
                if (self.Coll(300,175,140,65,event.x,700-event.y)):
                    self.PopUp = True
                elif(self.Coll(300,305,140,65,event.x,700- event.y)):
                    return 2
                elif self.Coll(365,440,70,70,event.x,700-event.y):
                    return 3
            else:
                for i in range(0, 2):
                    if (self.Coll(230 + (i * 140), 280,self.Button[i].w/2,self.Button[i].h/2, event.x, 700 - event.y)):
                        self.PopUp = False
                        effsound.play()
                        if i == 0:
                            return 1
                        break
        return 0