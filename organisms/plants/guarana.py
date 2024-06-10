from organisms import Organism
from organisms.plants.plant import Plant
from worlds.world import World

class Guarana(Plant):
    def __init__(self,position: (int,int),world: World):
        super().__init__(world, "Guarana", 0, 0, position)
    def colision(self,attacker: Organism):
        attacker.increaseStrenght(3)
        self._worldI.addLog(attacker.getMark() + " Wzmocnił się jedząc "+ self.getMark())
        self.kill()