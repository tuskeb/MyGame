import game
from bruhmomento.bruhStage import *

class bruhScreen(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 0
        self.g = 1
        self.b = 0
        self.add_stage(bruhstage())
    def act(self, delta_time: float):
            super().act(delta_time)
            if self.elapsed_time > 1:
                self.game.screen =brruhScreen()

class brruhScreen(game.scene2d.MyScreen):

        def create(self):
            super().create()
            self.r = 50
            self.g = 41
            self.b = 40
            self.add_stage(bruhstage())

        def act(self, delta_time: float):
            super().act(delta_time)
            if self.elapsed_time > 1:
                self.game.screen = bruhScreen()