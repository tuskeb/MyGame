import game
import pygame

class BgActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('image/snow.png')