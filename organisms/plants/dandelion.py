from organisms.plants.plant import Plant
from worlds.world import World

class Dandelion(Plant):
    def __init__(self,position: (int,int),world: World):
        super().__init__(world, "Mlecz", 0, 0, position)
    def action(self) -> None:
        super().action()
        super().action()
        super().action()