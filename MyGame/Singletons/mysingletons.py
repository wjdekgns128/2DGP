from mydefine import *
from pico2d import *
class SingletonInstane:
  __instance = None

  @classmethod
  def __getInstance(cls):
    return cls.__instance

  @classmethod
  def instance(cls, *args, **kargs):
    cls.__instance = cls(*args, **kargs)
    cls.instance = cls.__getInstance
    return cls.__instance

class ColorManager(SingletonInstane):
    def __init__(self):
        self.Ing = False
        self.colorListName = ['color1','color2','color3','color4','color5']
        self.MaxNumber = 0
        self.Load()
    def Load(self):
        if(self.Ing):
            return
        self.Ing = True
        f = open("res/colordata/colorlist.json", 'r')
        self.js = json.loads(f.read())
        f.close()
        self.MaxNumber =int(self.js['count']['number'])
    def GetColorName(self,n):
        return self.js['colorlists'][n]['name']
    def GetColorMoney(self,n):
        return self.js['colorlists'][n]['money']
    def GetColorNumber(self,n,colornumber):
        str =  self.js['colorlists'][n][self.colorListName [colornumber]]
        temp = str.split()
        return SDL_Color(int(temp[0]),int(temp[1]),int(temp[2]))
    def GetColorMaxCount(self):
        return self.MaxNumber
    def GetColorAll(self, n):
        returncolor = []
        for i in range(0,self.colorListName.__len__()):
            str = self.js['colorlists'][n][self.colorListName[i]]
            temp = str.split(',')
            returncolor.append(SDL_Color(int(temp[0]),int(temp[1]),int(temp[2])))
        return returncolor

