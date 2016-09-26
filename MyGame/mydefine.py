from Singletons.mysingletons import *
tileres = ["res/6x8.png", "res/8x10.png", "res/10x12.png"]
notileres = ["res/6x8_click.png", "res/8x10_click.png", "res/10x12_click.png"]
MapSize = [(6, 8), (8, 10), (10, 12)]
MapTilesSize = [(80, 75), (60, 60), (48, 50)]


MAPTYPE1,MAPTYPE2,MAPTYPE3 = 0,1,2

NOTILE,ONETILE,TWOTILE,THREETILE,FOURTILE,FIVETILE= 0,1,2,3,4,5


Sing_ColorLisManager = ColorManager.instance()
Sing_MapListManager = MapManager().instance()