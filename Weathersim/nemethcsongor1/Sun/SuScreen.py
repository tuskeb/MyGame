from Weathersim.nemethcsongor1.Sun.SuStage import *


class SuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(SuStage())


"""class SuGame(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = SuScreen()


SuGame().run()"""