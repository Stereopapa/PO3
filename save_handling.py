from worlds.world import World
from organisms.organism import Organism
from datetime import datetime

class SaveHandler:
    def __init__(self, world: World):
        self.__world = world

    def getSaves(self):
        savesFile = open("saves.txt", 'r')
        print(savesFile.read())
    def save(self):
        now = datetime.now()
        d1 = now.strftime("%Y_%m_%d_%H_%M_%S")
        name: str = "save_"+str(d1)+".txt"
        saveString = ""
        saveString += self.__world.toSave()
        for org in self.__world.getOrganisms():
            saveString += org.toSave()

        path: str = ""+name
        saveFile = open(path, "w")
        saveFile.write(saveString)
        saveFile.close()

        savesfile = open("saves.txt", "a")
        savesfile.write(name+"\n")
        savesfile.close()

        self.__world.addLog("Człowiek utworzył nowy zapis")

    def load(self, name: str):
        path: str = "saves/"+name
        try:
            saveFile = open(path, "r")
            line = saveFile.readline()
            while line:
                print(line)
                line = line.split(";")
                if line[0] == "World":
                    self.__world.initWorld(int(line[1]), int(line[2]), int(line[3]))
                else:
                    position: (int, int) = (int(line[4]), int(line[5]))
                    org = self.__world.addOrganism(line[1], line[0], position)
                    org.setAge(int(line[2]))
                    org.increaseStrenght(int(line[3])- org.getStrenght())
                line = saveFile.readline()
            saveFile.close()
        except FileNotFoundError:
            print("The file does not exist.")
            return

