from mydefine import *
from pico2d import *
import glob
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
class MapManager(SingletonInstane):
    def __init__(self):
        self.File_List = glob.glob('res/mapdata/*.txt')
    def GetFileName(self,n):
        return self.File_List[n]
    def GetFileData(self,n): # n번째에있는 텍스트 파일의 맵번호,클리어 숫자,클리어 색상,각 타일의 색상 리턴
        f = open(self.File_List[n])
        mylist = []
        lines = f.readlines()
        for line in lines:
            strline = line.split()
            if (strline.__len__() == 3):
                maptype = int(strline[0])
                count = int(strline[1])
                clear = int(strline[2])
            else:
                for i in range(0, strline.__len__()):
                    mylist.append(int(strline[i]))
        f.close()
        return maptype,count,clear,mylist
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
        temp = str.split(',')
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

