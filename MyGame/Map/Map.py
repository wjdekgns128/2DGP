from builtins import range
from pico2d import *

from Map import Tiles
from Map.Tiles import *
class Map:
    def __init__(self):
       self.MapSetting()
    def MapSetting(self):

        MapSize = [(6, 8), (8, 10), (10, 12)]
        MapTilesSize = [(80,75),(60,60),(48,50)]
        self.MapType = 0
        self.MapCount = (MapSize[self.MapType][0],MapSize[self.MapType][1])
        self.MapSize = (MapTilesSize[self.MapType][0],MapTilesSize[self.MapType][1])

        self.MapTiles = None
        if self.MapTiles != None:
            del (self.MapTiles)
            self.MapTiles = None
        if (self.MapTiles == None):
            self.MapTiles = [[0 for y in range(self.MapCount[1])] for x in range(self.MapCount[0])]
        for y in range(0, self.MapCount[1]):
            for x in range(0, self.MapCount[0]):
                    self.MapTiles[x][y] = Tiles(60 + (self.MapSize[0] / 2) + (x * self.MapSize[0]),
                                            10 + self.MapSize[1] / 2 + (y * self.MapSize[1]), 0)