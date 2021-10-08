import game
import random


class Bg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/landscape.png")


class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/sunny.png")


class Sun (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 30)


class FSun (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 15)


class Rain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/rain.png")

    def act(self, delta_time: float):
        self.y += 300 * delta_time
        if self.y > 720:
            self.y = -100
            self.x = random.randint(a=0, b=1280)


class FRain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/rain.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 15)


class Snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 30)
        self.y += 100 * delta_time
        if self.y > 720:
            self.y = -100
            self.x = random.randint(a=0, b=1280)


class FSnow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 15)


class Cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/cloudy.png")


class Cloud(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/cloudy.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 15)


class Back(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/back.png")