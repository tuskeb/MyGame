from Weathersim.FellnerMilan.Stage import *
import game


class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())
