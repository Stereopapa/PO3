from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.main_frame import UiMainFrame
from worlds.world import World
import sys

class Gui:
    def __init__(self, world: World):
        self.__world = world
    def window(self):
        app = QApplication(sys.argv)

        screen = app.primaryScreen()

        mainWindow = QMainWindow()
        mainWindow.setObjectName("Patryk Piotrowski 198398")
        mainWindow.resize(1280, 720)

        mainFrame = UiMainFrame(mainWindow, self.__world)

        mainWindow.showMaximized()
        sys.exit(app.exec_())
