from organisms.plants.plant import Plant
from worlds.world import World

class Grass(Plant):
    def __init__(self,position: (int,int),world: World):
        super().__init__(world, "Trawa", 0, 0, position)
