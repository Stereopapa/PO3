from PyQt5 import QtCore, QtGui, QtWidgets
from worlds.world import World
from organisms.organism import Organism
from organisms.animals.animal import Animal
from organisms.plants.plant import Plant

class BoardFrame(QtWidgets.QFrame):
    def __init__(self, parent, world: World):
        super().__init__(parent)
        self.__world = world
        self.__rectWidth: int = self.width()/self.__world.getWidth()
        self.__rectHeight: int = self.height()/self.__world.getHeight()
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        self.__rectWidth = int(self.width()/self.__world.getWidth())
        self.__rectHeight = int(self.height()/self.__world.getHeight())

        rtemp = []
        self.__r = []
        for x in range(self.__world.getWidth()):
            rtemp = []
            for y in range(self.__world.getHeight()):
                rtemp.append(QtCore.QRect(self.__rectWidth*y, self.__rectHeight*x, self.__rectWidth, self.__rectHeight))
            self.__r.append(rtemp)
        for x in range(self.__world.getWidth()):
            for y in range(self.__world.getHeight()):
                painter.drawRect(self.__r[x][y])

        organisms = self.__world.getOrganisms()

        for org in organisms:
            x: int = org.getPosition()[0]
            y: int = org.getPosition()[1]
            if isinstance(org, Animal):
                brush = QtGui.QBrush(QtGui.QColor(130, 72, 1))
                painter.setBrush(brush)
                painter.drawRect(self.__r[x][y])
            elif isinstance(org, Plant):
                brush = QtGui.QBrush(QtGui.QColor(33, 150, 12))
                painter.setBrush(brush)
                painter.drawRect(self.__r[x][y])
            text = org.getMark();
            text_width = painter.fontMetrics().width(text)
            text_height = painter.fontMetrics().height()
            text_x = int(self.__r[x][y].x() + (self.__r[x][y].width() - text_width) / 2)
            text_y = int(self.__r[x][y].y() + (self.__r[x][y].height() + text_height) / 2)

            painter.drawText(text_x, text_y, text)



