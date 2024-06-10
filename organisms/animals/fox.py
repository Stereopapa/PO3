from organisms import Organism
from organisms.animals.animal import Animal
# from worlds.world import World
import random

class Fox(Animal):
    def __init__(self,position: (int,int),world):
        self.name = "Fox"
        super().__init__(world, "Lis", 3, 7, position)
    def action(self):
        self.increaseAge()
        move: int = random.randint(0, 7)
        flag: int = 0
        while flag < 8:
            afterMove = self.pickPosition(move)
            if (self._worldI.isOrganismInBounds(afterMove)):
                org = self._worldI.getOrganism(afterMove)
                if org == None:
                    self.setPosition(afterMove)
                    return
                elif org != None and self.getStrenght() >= org.getStrenght():
                    self.setPosition(afterMove)
                    org.colision(self)
                    return
            move += 1
            move %= 8
            flag += 1