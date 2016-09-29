from _ast import List

from builtins import range

from mydefine import *
import os

import sys
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
class UserManager(SingletonInstane):
    def __init__(self): # 현재돈, 장착중인 색상,소지하고있는 색상들갯수 ~~
        self.NowMoney = 0 #소지돈
        self.NowColor = 0 # 장착중인 컬러
        self.NowBuyColor = 1 # 산 컬러수
        self.NowBuyColorList = [] #현재산 리스트의 번호들
        self.NowBuyColorList.append(0)
        self.Name = "/res/userdata/user.txt"
        self.__Load()
    def __Load(self):
        z = os.getcwd() + "/res/userdata"
        if not os.path.isdir(z):
            os.makedirs(z)
        z = os.getcwd() + self.Name
        if not os.path.isfile(z):
            self.Save()
            return;
        self.NowBuyColorList.pop()
        f = open(os.getcwd() + self.Name, "r")
        str = f.readline()
        str = str.split(' ')
        self.NowMoney = int(str[0])
        self.NowColor = int(str[1])
        self.NowBuyColor = int(str[2])
        for i in range(0,self.NowBuyColor):
            str1 = f.readline().split(' ')
            self.NowBuyColorList.append(int(str1[0]))
        f.close()
    def Save(self):
        f = open(os.getcwd() + self.Name, "w")
        f.writelines(str(self.NowMoney) + " "  + str(self.NowColor) + " " + str(self.NowBuyColor) + "\n")
        for i in range(0, self.NowBuyColor):
            f.writelines(str(self.NowBuyColorList[i]) + "\n")
        f.close()
MapChekc = False
class MapManager(SingletonInstane):
    def __init__(self):
        global  MapChekc
        if MapChekc == True:
            return

        self.__Load()
        MapChekc = True

    def __Load(self):
        self.Dir_List = glob.glob('res/mapdata/*')
        self.File_List = []
        self.ClearNumber = []

        for i in range(0, self.Dir_List.__len__()):
            Temp = (glob.glob(self.Dir_List[i] + "/*.txt"))
            self.File_List.append(Temp)

        for i in range(0, self.Dir_List.__len__()):
            Temp = []
            for j in range(0,self.File_List[i].__len__()):
                Temp.append(0)
            self.ClearNumber.append(Temp)
        z = os.getcwd() + "/res/userdata/chapter"
        if not os.path.isdir(z):
            os.makedirs(z)
        for i in range(0,self.Dir_List.__len__()):
            z = os.getcwd()  + "/res/userdata/chapter/" + "ch" + str(i+1) + ".txt"
            if not os.path.isfile(z):
                self.Save(i)
            else:
                self.__LoadChar(i)
    def __LoadChar(self,n): # n의 텍스트파일 읽기
        f = open(os.getcwd() + "/res/userdata/chapter/" + "ch" + str(n + 1) + ".txt")
        lines = f.readlines()
        for line in lines:
            t = line.split(' ')
            for i in range(0,t.__len__()):
                self.ClearNumber[n][i] = int(t[i])
                print(self.ClearNumber[n][i])
        f.close()
    def Save(self,n): # 챕터 저장
        f = open(os.getcwd()  + "/res/userdata/chapter/" + "ch" + str(n+1) + ".txt", "w")
        for i in range(0, self.File_List[n].__len__()):
            if i == self.File_List[n].__len__()-1:
                f.writelines(str(self.ClearNumber[n][i]))
            else:
               f.writelines(str(self.ClearNumber[n][i]) + " ")
        f.close()
    def GetChatper(self):
        return self.File_List.__len__()
    def GetStage(self,n):
        return self.File_List[n].__len__()
    def GetFileName(self,c,n): # 챕터번호,숫자번호WWWW
        return self.File_List[c][n].split("res/mapdata\ch" + str(c+1) + "\\")[1]
    def GetFileData(self,c,n): # n번째에있는 텍스트 파일의 맵번호,클리어 숫자,클리어 색상,각 타일의 색상 리턴
        f = open(self.File_List[c][n])
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
