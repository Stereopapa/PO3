from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QFont, QColor, QBrush
from PyQt5.QtWidgets import QWidget
from worlds.world import World
from gui.board import BoardFrame
from save_handling import SaveHandler
from collections import deque

class UiMainFrame(QWidget):

    BUTTON_STYLE = """
    QPushButton{
        border:2px solid white;
        color: white;
        text-align: center;
        text-decoration: none;
        border-radius: 10px;
        padding: 3px;
        font-size: 15px;
    }
    QPushButton:hover{
        background-color: rgb(135, 134, 98);
    }
    QPushButton:pressed{
        background-color: rgb(165, 164, 128);
    }
    """
    MAIN_WINDOW_STYLE = """
    background-color: rgb(115, 114, 78);
    border-color: rgb(255, 255, 255);
    color: rgb(255, 255, 255);
    """
    SAVE_BUTTON_STYLE = """
    QPushButton{
        text-align: center;
        border:1px solid white;
        font-size: 16px;
        padding: 2px;
    }
    QPushButton:hover{
        background-color: rgb(135, 134, 98);
    }
    QPushButton:checked{
        background-color: rgb(165, 164, 128);
    }
    """
    def __init__(self, MainWindow, world: World):
        super().__init__()
        self.__world = world
        self.__mainWindow = MainWindow
        self.__saveHandler = SaveHandler(world)
        self.__saves = self.__saveHandler.getSaves().split()
        self.setupUi()


    def setupUi(self):

        self.__mainWindow.setStyleSheet(self.MAIN_WINDOW_STYLE)

        self.setupCentralWidget()
        self.setupMenuFrame()
        self.setupMainGameFrame()

        self.__mainWindow.setCentralWidget(self)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(self.__mainWindow)

        self.drawTurn()
    def setupCentralWidget(self):
        # self.centralwidget = QtWidgets.QWidget(self.__mainWindow)
        # self.centralwidget.setObjectName("centralwidget")

        self.centralHorizontalLayout = QtWidgets.QVBoxLayout(self)
        self.centralHorizontalLayout.setObjectName("centralHorizontalLayout")

    def setupMenuFrame(self):
        self.menuFrame = QtWidgets.QFrame(self)
        self.menuFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.menuFrame.setObjectName("menuFrame")

        self.menuVerticalLayout = QtWidgets.QHBoxLayout(self.menuFrame)
        self.menuVerticalLayout.setObjectName("menuVerticalLayout")

        self.setupMenuWidgets()
        self.centralHorizontalLayout.addWidget(self.menuFrame)

    def setupMenuWidgets(self):
        self.turnLabel = QtWidgets.QLabel(self.menuFrame)
        self.turnLabel.setFont(QFont('Times', 11))
        self.turnLabel.setObjectName("turnLabel")
        self.menuVerticalLayout.addWidget(self.turnLabel)

        self.populationLabel = QtWidgets.QLabel(self.menuFrame)
        self.populationLabel.setFont(QFont('Times', 11))
        self.populationLabel.setObjectName("populationLabel")
        self.menuVerticalLayout.addWidget(self.populationLabel)

        self.nextTurnButton = QtWidgets.QPushButton(self.menuFrame)
        self.nextTurnButton.setStyleSheet(self.BUTTON_STYLE)
        self.nextTurnButton.setObjectName("nextTurnButton")
        self.menuVerticalLayout.addWidget(self.nextTurnButton)
        self.nextTurnButton.clicked.connect(self.nextTurn)

        self.specialAbilityButton = QtWidgets.QPushButton(self.menuFrame)
        self.specialAbilityButton.setStyleSheet(self.BUTTON_STYLE)
        self.specialAbilityButton.setObjectName("specialAbilityButton")
        self.menuVerticalLayout.addWidget(self.specialAbilityButton)
        self.specialAbilityButton.clicked.connect(self.activateSpecialAbility)

        self.loadButton = QtWidgets.QPushButton(self.menuFrame)
        self.loadButton.setStyleSheet(self.BUTTON_STYLE)
        self.loadButton.setObjectName("loadButton")
        self.menuVerticalLayout.addWidget(self.loadButton)
        self.loadButton.clicked.connect(self.switchloadMenu)

        self.saveButton = QtWidgets.QPushButton(self.menuFrame)
        self.saveButton.setStyleSheet(self.BUTTON_STYLE)
        self.saveButton.setObjectName("saveButton")
        self.menuVerticalLayout.addWidget(self.saveButton)
        self.saveButton.clicked.connect(self.save)



    def setupMainGameFrame(self):
        self.mainGameFrame = QtWidgets.QFrame(self)
        self.mainGameFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.mainGameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainGameFrame.setObjectName("mainGameFrame")

        self.mainGameVerticalLayout = QtWidgets.QHBoxLayout(self.mainGameFrame)
        self.mainGameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainGameVerticalLayout.setSpacing(25)
        self.mainGameVerticalLayout.setObjectName("mainGameVerticalLayout")

        self.boardFrame = BoardFrame(self.mainGameFrame, self.__world)
        self.boardFrame.setObjectName("boardFrame")
        self.mainGameVerticalLayout.addWidget(self.boardFrame)

        self.setupLogsAndLoadFrame()

        self.mainGameVerticalLayout.addWidget(self.logsAndLoadScroll)
        self.mainGameVerticalLayout.setStretch(0, 2)
        self.mainGameVerticalLayout.setStretch(1, 1)
        self.centralHorizontalLayout.addWidget(self.mainGameFrame)

    def setupLogsAndLoadFrame(self):
        self.logsAndLoadScroll = QtWidgets.QScrollArea(self.mainGameFrame)
        self.logsAndLoadScroll.setFrameShape(QtWidgets.QFrame.Box)
        self.logsAndLoadScroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logsAndLoadScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.logsAndLoadScroll.setObjectName("logsAndLoadScroll")
        self.logsAndLoadScroll.setWidgetResizable(True)


        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.logsAndLoadVerticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.logsAndLoadVerticalLayout.setObjectName("logsAndLoadVerticalLayout")

        # logs
        self.logsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.logsLabel.setFont(QFont('Times', 14))
        self.logsLabel.setObjectName("logsLabel")
        self.logsLabel.setWordWrap(True)  # Allow the text to wrap

        # loadMenu
        self.savesGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.savesGroupBox.setFlat(True)
        self.gridLayout = QtWidgets.QGridLayout(self.savesGroupBox)

        self.loadLoadMenuButton = QtWidgets.QPushButton(self.savesGroupBox)
        self.loadLoadMenuButton.setText("Wczytaj")
        self.loadLoadMenuButton.setStyleSheet(self.BUTTON_STYLE)
        self.loadLoadMenuButton.clicked.connect(self.load)
        self.exitLoadMenuButton = QtWidgets.QPushButton(self.savesGroupBox)
        self.exitLoadMenuButton.setText("Wyjdz")
        self.exitLoadMenuButton.setStyleSheet(self.BUTTON_STYLE)
        self.exitLoadMenuButton.clicked.connect(self.switchLogs)
        self.gridLayout.addWidget(self.loadLoadMenuButton, 0, 0)
        self.gridLayout.addWidget(self.exitLoadMenuButton, 0, 1)

        # generating saves Buttons
        self.saveButtonGroup = QtWidgets.QButtonGroup()
        self.saveButtonGroup.setExclusive(True)
        self.savesButtonsList = deque([])
        row = 1
        for save in self.__saves:
            self.addSaveToLoadMenu(save, row)
            row += 1
        self.rebuildGridLayout()
        # adding to scroll layout
        self.logsAndLoadVerticalLayout.addWidget(self.savesGroupBox)
        self.logsAndLoadVerticalLayout.addWidget(self.logsLabel)

        self.savesGroupBox.hide()
        self.logsAndLoadScroll.setWidget(self.scrollAreaWidgetContents)
        self.logsAndLoadVerticalLayout.setAlignment(QtCore.Qt.AlignTop)

    def retranslateUi(self):
        self.turnLabel.setText("Tura: ")
        self.populationLabel.setText("Populacja: ")
        self.nextTurnButton.setText("Nastepna Tura")
        self.saveButton.setText("Zapisz")
        self.loadButton.setText("Wczytaj")
        self.specialAbilityButton.setText("Tarcza: Gotowa")
        self.logsLabel.setText("Logi: \n")
    def addSaveToLoadMenu(self, name: str, row: int):
        self.savesButtonsList.appendleft(QtWidgets.QPushButton(name[:-4]))
        self.savesButtonsList[0].setCheckable(True)
        self.savesButtonsList[0].setStyleSheet(self.SAVE_BUTTON_STYLE)
        self.saveButtonGroup.addButton(self.savesButtonsList[0])


    def rebuildGridLayout(self):
        for label in self.savesButtonsList:
            if label is not None:
                label.setParent(None)
        row = 1
        for label in self.savesButtonsList:
            self.gridLayout.addWidget(label, row, 0, 1, 2)
            row += 1


    def nextTurn(self):
        self.logsLabel.setText("Logi:\n"+self.__world.getLogs())  # Example log text
        self.scrollAreaWidgetContents.repaint()
        self.__world.nextTurn()
        self.drawTurn()

    def switchloadMenu(self):
        self.logsLabel.hide()
        self.savesGroupBox.show()
    def switchLogs(self):
        self.savesGroupBox.hide()
        self.uncheckButton()
        self.logsLabel.show()

    def activateSpecialAbility(self):
        self.__world.getHuman().activateSpecialAbility()
        self.specialAbilityButton.setText(self.__world.getHuman().getSpecialAbilityState())

    def humanReact(self, direction):
        self.__world.getHuman().resetDirection()
        position = self.__world.getHuman().setDirection(direction)
        print(position)
        self.boardFrame.repaint()
    def keyPressEvent(self, event):
        key = event.key()
        if key == 81:  # Up Left(q) move
            self.humanReact((-1, -1))
        elif key == 87:  # Up(w) move
            self.humanReact((-1, 0))
        elif key == 69:  # Up Right(e) move
            self.humanReact((-1, 1))
        elif key == 68:  # Right(d) move
            self.humanReact((0, 1))
        elif key == 67:  # Down Right(c) move
            self.humanReact((1, 1))
        elif key == 88:  # down (x) move
            self.humanReact((1, 0))
        elif key == 90:  # down Left (z) move
            self.humanReact((1, -1))
        elif key == 65:  # Left (a) move
            self.humanReact((0, -1))
        elif key == 83:  # middle (s) stay move
            self.humanReact((0, 0))


    def load(self):
        clickedButton = self.saveButtonGroup.checkedButton()

        if not clickedButton:
            return
        name = clickedButton.text()+".txt"

        self.__saveHandler.load(name)
        self.switchLogs()
        self.drawTurn()

    def save(self):
        name = self.__saveHandler.save()
        self.addSaveToLoadMenu(name, len(self.__saves))
        self.rebuildGridLayout()
        self.savesGroupBox.repaint()
    def uncheckButton(self):
        checked_button = self.saveButtonGroup.checkedButton()
        if checked_button:
            self.saveButtonGroup.setExclusive(False)
            checked_button.setChecked(False)
            self.saveButtonGroup.setExclusive(True)

    def nextTurn(self):
        self.scrollAreaWidgetContents.repaint()
        self.__world.nextTurn()
        self.drawTurn()

    def drawTurn(self):
        self.turnLabel.setText("Tura: "+str(self.__world.getTurn()))
        self.populationLabel.setText("Populacja: "+str(self.__world.getPopulation()))
        self.logsLabel.setText("Logi:\n" + self.__world.getLogs())
        self.specialAbilityButton.setText(self.__world.getHuman().getSpecialAbilityState())
        self.boardFrame.repaint()


