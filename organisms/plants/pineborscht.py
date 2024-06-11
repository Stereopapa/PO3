from organisms import Organism
from organisms.plants.plant import Plant
from worlds.world import World
from organisms.animals.animal import Animal
from organisms.animals.cybersheep import CyberSheep

class PineBorscht(Plant):
    def __init__(self,position: (int,int),world: World):
        super().__init__(world, "BarszczSos", 0, 0, position)
    def action(self) -> None:
        move: int = -1
        flag: int = 0
        while flag < 8:
            afterMove = self.pickPosition(move)
            move += 1
            flag += 1
            if (self._worldI.isOrganismInBounds(afterMove) and self._worldI.getOrganism(afterMove) != None ):
                org = self._worldI.getOrganism(afterMove)
                if(isinstance(org, Animal)):
                    if(isinstance(org, CyberSheep)):
                        continue
                    org.kill()
                    self._worldI.addLog(self.getMark()+" zabil "+org.getMark())
        super().action()

    def colision(self, attacker: Organism):
        if(isinstance(attacker, CyberSheep)):
            self.kill()
            return
        super().colision()