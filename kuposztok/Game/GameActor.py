import game
import random
import pygame


class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500
        if self.y > 1080:
            self.y = -1080

class BgActor2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500
        if self.y > 1080:
            self.y = -1080



class Visszagomb(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/back_to_menu_button.png')


class Joseph(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')


class Enemy(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/tree.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500
        if self.y > 1200:
            self.y = -200
            self.x = random.Random().randint(200, 1080)

class Ski(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Ski.png')
        self.width = 100
        self.height = 100

class SnowBoard(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/SnowBoard.png')
        self.width = 100
        self.height = 100

class SnowMobile(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/SnowMobile.png')
        self.width = 200
        self.height = 200


class Sledge(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Sledge.png')
        self.width = 200
        self.height = 200
