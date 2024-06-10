from organisms.organism import Organism
import importlib

import random

class World:

    def __init__(self, width: int, height: int):
        self.__logs = ""
        self.__organisms = [Organism]
        self.__alovedMoves = ((0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1))
        self.initWorld(width, height, 0)
        self.populateWorld()

    def initWorld(self, width: int, height: int, turn: int):
        self.__width = width
        self.__height = height
        self.__turn = turn
        self.__organisms.clear()
        self.__logs = ""

    def toSave(self) -> str:
        result: str = "World;"
        result += str(self.__width)+";"
        result += str(self.__height)+";"
        result += str(self.__turn)+";"
        result += "\n"
        return result

    def populateWorld(self):
        # self.addOrganism("organisms.animals.turtle", "Turtle", self.genererateRandomPosition())
        # self.addOrganism("organisms.animals.sheep", "Sheep", self.genererateRandomPosition())
        # self.addOrganism("organisms.animals.sheep", "Sheep",self.genererateRandomPosition())
        # self.addOrganism("organisms.animals.wolf", "Wolf", self.genererateRandomPosition())
        # self.addOrganism("organisms.animals.fox", "Fox", self.genererateRandomPosition())
        # self.addOrganism("organisms.animals.wolf", "Wolf", self.genererateRandomPosition())
        # self.addOrganism("organisms.plants.dandelion", "Dandelion", self.genererateRandomPosition())
        # self.addOrganism("organisms.plants.guarana", "Guarana", self.genererateRandomPosition())
        # self.addOrganism("organisms.plants.belladona", "Belladona", self.genererateRandomPosition())
        # self.addOrganism("organisms.plants.pineborscht", "pineBorscht", self.genererateRandomPosition())
        # self.addOrganism("organisms.plants.guarana", "Guarana", self.genererateRandomPosition())
        # self.addOrganism("organisms.plants.grass", "Grass", self.genererateRandomPosition())
    def genererateRandomPosition(self) -> (int, int):
        flag = 0
        position = (-1,-1)
        while flag<500:
            position = (random.randint(0,self.__width-1),random.randint(0,self.__height-1))
            if self.getOrganism(position) == None:
                break
            flag += 1
        return position
    def nextTurn(self):
        self.__logs = ""
        self.__turn += 1
        self.__organisms.sort(key= lambda x : (x.getInitiative(), x.getAge()), reverse=True)
        for org in self.__organisms:
            if org.getStrenght() >= 0:
                org.action()
        self.__organisms = [org for org in self.__organisms if org.getStrenght() >= 0]

    def isOrganismInBounds(self, position: (int,int)):
        return position[0] >=0 and position[0] < self.__width and position[1] >=0 and position[1] < self.__height

    def addLog(self,message: str):
        self.__logs += message+"\n"

    def addOrganism(self, modulePath: str, name: str, position: (int, int)) -> Organism:
        module = importlib.import_module(modulePath)
        org: Organism = getattr(module, name)(position, self)
        self.__organisms.append(org)
        return org

    def getOrganism(self, Position: (int, int)):
        for org in self.__organisms:
            if org.getPosition() == Position:
                return org
        return None

    def getAlovedMoves(self) -> ((int, int),(int, int),(int, int),(int, int),(int, int),(int, int),(int, int),(int, int)):
        return self.__alovedMoves

    def getTurn(self) -> int:
        return self.__turn

    def getWidth(self) -> int:
        return self.__width

    def getHeight(self) -> int:
        return self.__height

    def getOrganisms(self) -> [Organism]:
        return self.__organisms

    def getPopulation(self) -> int:
        return len(self.__organisms)

    def getLogs(self) -> str:
        return self.__logs





