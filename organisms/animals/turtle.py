from organisms import Organism
from organisms.animals.animal import Animal
# from worlds.world import World
import random

class Turtle(Animal):
    def __init__(self,position: (int,int),world):
        self.name = "Turtle"
        super().__init__(world, "Żółw", 2, 1, position)
    def action(self):
        success = random.randint(0, 3)
        if success == 0:
            super().action()
    def colision(self, attacker: Organism):
        if attacker.getStrenght() < 5 and type(self) != type(attacker):
            self._worldI.addLog(self.getMark()+" Odparł atak "+attacker.getMark())
            attacker.undoMove()
            return
        super().colision(attacker)

