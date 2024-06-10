from abc import ABC, abstractmethod

class Organism(ABC):
    def __init__(self, worldI , mark: str, strenght: int, initiative: int, position: (int, int)):
            # self._worldI = World();
            from worlds.world import World
            self._worldI: World = worldI
            self.__strenght = strenght
            self.__mark = mark
            self.__initiative = initiative
            self._position = position
            self._previousPosition = position
            self.__age = 0

    @abstractmethod
    def action(self) -> None:
        pass

    @abstractmethod
    def colision(self, attacker) -> None:
        pass

    def kill(self) -> None:
        self._position = (-1, -1)
        self.__strenght = -1

    def increaseStrenght(self, value: int) -> None:
        self.__strenght += value

    def increaseAge(self) -> None:
        self.__age += 1

    def pickPosition(self, move: int) -> (int,int):
        return (self._position[0]+self._worldI.getAlovedMoves()[move][0], self._position[1]+self._worldI.getAlovedMoves()[move][1])

    def undoMove(self) -> None:
        self.setPosition(self._previousPosition)

    def toSave(self) -> str:
        result = ""
        result += self.__class__.__name__+";"
        result += self.__class__.__module__+";"
        result += str(self.__age)+";"
        result += str(self.__strenght)+";"
        result += str(self._position[0])+";"
        result += str(self._position[1])+";"
        result += "\n"
        return result


    def setPosition(self, position: (int, int)) -> None:
        self._previousPosition = self._position
        self._position = position

    def setAge(self, age: int) -> None:
        self.__age = age

    def getMark(self) -> str:
        return self.__mark

    def getStrenght(self) -> int:
        return self.__strenght

    def getInitiative(self) -> int:
        return self.__initiative

    def getAge(self) -> int:
        return self.__age

    def getPosition(self) -> (int, int):
        return self._position








