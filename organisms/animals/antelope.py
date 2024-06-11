from organisms import Organism
from organisms.animals.animal import Animal
# from worlds.world import World
import random

class Antelope(Animal):
    def __init__(self,position: (int,int),world):
        self.name = "Turtle"
        super().__init__(world, "Antylopa", 4, 4, position)
    def action(self):
        super().action()
        super().action()

    def hasEscaped(self) -> bool:
        succsess = random.randint(0,1)
        if(succsess == 0):
            move: int = random.randint(0, 7)
            flag: int = 0
            while flag < 8:
                afterMove = self.pickPosition(move)
                if (self._worldI.isOrganismInBounds(afterMove) and self._worldI.getOrganism(afterMove) == None):
                    self.setPosition(afterMove)
                    self._worldI.addLog(self.getMark() + " udało sie uciec ")
                    return True
                move += 1
                move %= 8
                flag += 1
        self._worldI.addLog(self.getMark() + " nie udało sie uciec ")
        return False
