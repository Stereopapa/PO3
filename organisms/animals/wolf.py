from organisms.animals.animal import Animal
from worlds.world import World

class Wolf(Animal):
    def __init__(self,position: (int,int),world: World):
        super().__init__(world, "Wilk", 9, 5, position)
