from tkinter import filedialog
from tkinter import  *
import ctypes
import os
class filesave: #크기,클리어카운터,클리어색상 ,순 (배열이 반대로 되있어가지고 밑에부터참)
    def __init__(self):

        self.filesaveing = False
    def Save(self,mpanumber,clearcount,clearcolor,SaveMap,x,y):
        if self.filesaveing == True:
            return
        mysave = SaveMap[:]
        ctypes.windll.user32.MessageBoxW(0, "클리어!! 파일을 저장합니다..", "!", 0)
        Tk().withdraw()
        self.filesaveing = True
        z = os.getcwd() + "/res\mapdata"
        if not os.path.isdir(z):
            os.mkdir(z)
        f = filedialog.asksaveasfile( mode='w',initialdir = os.getcwd() + "/res/mapdata", filetypes=[('c_p_maptooldata', ".txt")])
        if f is None:
            print("error file save")
            return
        savefile1= None
        savefile = str(mpanumber) + " "  + str(clearcount) + " "  + str(clearcolor)
        f.write(savefile + "\n")
        for i in range(0,y):
            for j in range(0,x):
                if( j != x-1):
                    savefile1 = str(mysave.pop()) + " "
                else:
                    savefile1 = str(mysave.pop())
                f.write(savefile1)
            if(i != y-1):
                f.write("\n")
        f.close()
class fileload:
    def __int__(self):
        pass
    def loadfile(self):
        z = os.getcwd() + "/res\mapdata"
        if not os.path.isdir(z):
            os.mkdir(z)
        count,clear,maptype = 0,0,0
        Tk().withdraw()
        filename = filedialog.askopenfilename(initialdir = os.getcwd() + "/res/mapdata",filetypes=(("c_p_maptooldata", "*.txt"), ("txt", "*.txt*")))
        if not filename:
            print("file load error")
            return False,-1,-1,-1,None
        mylist = []
        f = open(filename)
        lines = f.readlines()
        for line in lines:
            strline = line.split()
            if(strline.__len__() == 3):
                maptype = int(strline[0])
                count = int(strline[1])
                clear = int(strline[2])
            else:
                for i in range(0,strline.__len__()):
                    mylist.append(int(strline[i]))
        f.close()
        return True,maptype,count,clear,mylist  # 맵번호,클리어 숫자,클리어 색상,각 타일의 색상
