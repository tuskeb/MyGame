import game

from Impostorsus.Game.WarioActor import *
from Impostorsus.Game.WarioScreen import *
import Impostorsus.Game.WarioScreen

class Wario(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = ASDSCR2()

Wario().run()



