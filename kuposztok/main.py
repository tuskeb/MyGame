import game


class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/my-caracter.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class Enemy2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/my-caracter.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.h1 = Enemy1Actor()
        self.h2 = Enemy2Actor()
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.h2.x = 20
        self.h2.y = 20
        self.h2.w = 200
        self.h2.hitbox_scale_w = 0.75


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 128, 0)
        self.add_stage(GameStage())


class Space(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.set_screen(GameScreen())


Space()
