from organisms.organism import Organism
import random

class Plant(Organism):
    def action(self) -> None:
        self.increaseAge()
        success: int = random.randint(0,2)
        if(success != 0):
            return
        move: int = random.randint(0,7)
        flag: int = 0
        while flag < 8:
            afterMove = self.pickPosition(move)
            if(self._worldI.isOrganismInBounds(afterMove) and self._worldI.getOrganism(afterMove) == None):
                self._worldI.addOrganism(self.__class__.__module__, self.__class__.__name__, afterMove)
                self._worldI.addLog(self.getMark()+" rozprzestrzenił się ")
                return
            move += 1
            move %= 8
            flag += 1
    def colision(self,attacker: Organism):
        if(attacker == self):
            return
        if(self.getStrenght() > attacker.getStrenght()):
            attacker.kill()
        else:
            self.kill()

