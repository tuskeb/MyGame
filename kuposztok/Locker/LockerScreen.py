from kuposztok.Locker.LockerStage import *


class LockerScreen(game.scene2d.MyScreen):

    def __init__(self, money: int):
        super().__init__()
        self.set_background_color(r=0,g=0, b=0)
        self.add_stage(LockerStage(money=money))