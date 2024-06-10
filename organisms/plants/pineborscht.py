from organisms.plants.plant import Plant
from worlds.world import World
from organisms.animals.animal import Animal

class pineBorscht(Plant):
    def __init__(self,position: (int,int),world: World):
        super().__init__(world, "BarszczSos", 0, 0, position)
    def action(self) -> None:
        move: int = 0
        flag: int = 0
        while flag < 8:
            afterMove = self.pickPosition(move)
            if (self._worldI.isOrganismInBounds(afterMove) and self._worldI.getOrganism(afterMove) != None ):
                org = self._worldI.getOrganism(afterMove)
                if(isinstance(org, Animal)):
                    org.kill()
                    self._worldI.addLog(self.getMark()+" zabil "+org.getMark())
            move += 1
            move %= 8
            flag += 1
        super().action()