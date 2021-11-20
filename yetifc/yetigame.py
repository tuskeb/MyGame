from yetifc.yetiscreen import MenuScreen
from yetifc import *
import game


class Yeti(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        print(event)


Yeti().run()