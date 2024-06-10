from organisms.organism import Organism
import random

class Animal(Organism):
    def action(self):
        self.increaseAge()
        move = random.randint(0,7)
        flag = 0
        while flag < 8:
            afterMove = self.pickPosition(move)
            if(self._worldI.isOrganismInBounds(afterMove)):
                other = self._worldI.getOrganism(afterMove)
                self.setPosition(afterMove)
                if(other != None):
                    other.colision(self)
                return
            move += 1
            move %= 8
            flag += 1
    def colision(self,attacker: Organism):
        if(attacker == self):
            return
        # if(isinstance(self, attacker)):

        if(self.getStrenght() > attacker.getStrenght()):
            attacker.kill()
        else:
            self.kill()


