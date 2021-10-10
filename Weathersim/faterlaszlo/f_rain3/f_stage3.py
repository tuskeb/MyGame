import game
import random
from Weathersim.faterlaszlo.Arial import *
#from Weathersim.faterlaszlo.f_menu_m.f_screen_m import *
from Weathersim.faterlaszlo.f_actors import *

class f_stage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor()
        self.felho = felhos_actor()
        self.add_actor(self.bg)
        self.add_actor(self.felho)
        self.felho.z_index = 0

        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("Vissza_n")
        self.t.x = 0
        self.t.y = 0
        #self.t.set_on_mouse_down_listener(self.click)

        for i in range(12):
            self.eso = eso()
            self.add_actor(self.eso)
            self.eso.h = 25
            self.eso.w = 50
            self.eso.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso.w)
            self.eso.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.eso.h)

    ##def click(self, sender, event):
        #if event.button == 1:
         #   self.screen.game.get_screen(f_screen_m())
