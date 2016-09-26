from MyUtile.myfadeinfadeout import *
from MyUtile.mycoroutine import *

class Tiles(Coroutine):
    def __init__(self,x,y,type):
        super(Tiles,self).__init__()
        self.StartX = x
        self.StartY = y
        self.Type = type
        self.FirstType = type

