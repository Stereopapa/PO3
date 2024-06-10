from organisms import Organism
from organisms.plants.plant import Plant
from worlds.world import World

class Belladona(Plant):
    def __init__(self,position: (int,int),world: World):
        super().__init__(world, "WJagody", 99, 0, position)
    def colision(self,attacker: Organism):
        attacker.kill()
        self._worldI.addLog(attacker.getMark() + " zatrul sie jedzac "+self.getMark())
        self.kill()