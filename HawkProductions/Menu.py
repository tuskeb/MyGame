import game
from HawkProductions.MenuScreen import *


class Menu(game.scene2d.MyGame):
    def __init__(self):
        super().__init__()
        self.screen = MenuScreen()


Menu().run()