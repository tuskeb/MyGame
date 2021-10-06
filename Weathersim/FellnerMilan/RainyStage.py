import  game
from random import Random
import pygame
from Weathersim.FellnerMilan.InActors import *
import Weathersim.FellnerMilan.InScreen
from game.scene2d import MyTickTimer, MyOneTickTimer, MyIntervalTimer
from random import Random
class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.l = LandScape()
        self.add_actor(self.l)
        self.l.z_index = 2


        self.cloud = Rainy()
        self.add_actor(self.cloud)
        self.cloud.z_index = 0

        self.rain = Rain()
        self.add_actor(self.rain)
        self.rain.z_index = 3

        self.cloudreal = Cloud()
        self.add_actor(self.cloudreal)
        self.cloudreal.z_index = 1

        self.r = Random()

        self.set_on_key_down_listener(self.keylistener)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.t = MyTickTimer(interval=1,func=self.timerhandler)
        self.add_timer(self.t)
        print(self.rain.x)
        print(self.rain.y)


    def timerhandler(self,sender):
            self.rain2 = Rain()
            self.add_actor(self.rain2)
            self.remove_timer(self.t)
    def keylistener(self,sender,event):
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(Weathersim.FellnerMilan.InScreen.InScreen())