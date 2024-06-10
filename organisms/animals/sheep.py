from organisms.animals.animal import Animal
# from worlds.world import World

class Sheep(Animal):
    def __init__(self,position: (int,int),world):
        self.name = "Sheep"
        super().__init__(world, "Owca", 4, 4, position)
