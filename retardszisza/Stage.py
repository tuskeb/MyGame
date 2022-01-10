import retardszisza.menu_halal.MenuStage
from retardszisza.menu_halal.MenuScreen import *
import retardszisza.menu_halal.HalalActor
import retardszisza.menu_halal.HalalStage
import retardszisza.menu_halal.HalalScreen
from retardszisza.menu_halal.HalalScreen import *
import game
from retardszisza.Actor import *
import random
import pygame
import random


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.a = UtActor()
        self.b = szisza()
        self.c = kocsi1()
        self.fal = FalActor()
        self.palyaszele = Palyaszele()

        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)
        self.add_actor(self.fal)
        self.add_actor(self.palyaszele)
        #pos
        self.b.x = 100
        self.b.y = 550

        self.c.x = 600
        self.c.y = 550

        self.fal.x = -250
        self.palyaszele.y = 720
        #hitbox
        self.b.hitbox_scale_h = 1
        self.b.hitbox_scale_w = 1

        self.c.hitbox_scale_h = 0.9
        self.c.hitbox_scale_w = 0.9

        self.b.set_on_key_down_listener(self.button_down)

    def button_down(self, sender, event):
        if event.key == pygame.K_w:
            self.b.y -= 120
            print("asd")
        if event.key == pygame.K_s:
            self.b.y += 120

    def act(self, delta_time: float):
        super().act(delta_time)
        Overlapsasd: bool = False
        kocsirespawn: bool = False
        Palyaszel: bool = False

        for ASDASD in self.actors:
                if self.c.overlaps(self.b):
                    Overlapsasd = True
                    break
                if self.c.overlaps(self.fal):
                    kocsirespawn = True
                if self.b.overlaps(self.palyaszele):
                    Palyaszel = True


        if Overlapsasd:
            self.screen.game.set_screen(retardszisza.menu_halal.HalalScreen.halalscreen()) #HALAL

        if kocsirespawn:
            self.c.x = 600

        if Palyaszel:
            self.b.y = 550
