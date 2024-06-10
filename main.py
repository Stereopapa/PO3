from gui.gui import Gui
from worlds import World

world = World(5, 5)
gui = Gui(world)
gui.window()
