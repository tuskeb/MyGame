import game
import random

class erdo(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')

class naposeg(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/sunny.png')

class felhoseg(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/cloudy.png')

class esocsepp(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * random.randint(200, 400)
        if self.y > 720:
            self.y = random.randint(-500, 0)

class hopehely(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(2)
        self.y += delta_time * random.randint(90, 250)
        if self.y > 720:
            self.y = random.randint(-500, 0)


class nap(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/sun.png')
        self.x += 1000
        self.y += -200

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.2)

class menubutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/menubutton.png')
