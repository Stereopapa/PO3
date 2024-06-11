from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.main_frame import UiMainFrame
from gui.main_window import MainWindow
from worlds.world import World
import sys


class KeyPressFilter(QtCore.QObject):
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            print("Key pressed:", key)
        return False
class Gui:
    def __init__(self, world: World):
        self.__world = world



    def window(self):
        app = QApplication(sys.argv)

        screen = app.primaryScreen()
        mainWindow = MainWindow()


        mainFrame = UiMainFrame(mainWindow, self.__world)

        mainWindow.showMaximized()
        sys.exit(app.exec_())
