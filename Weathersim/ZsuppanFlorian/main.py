from Weathersim.ZsuppanFlorian import *
from Weathersim.ZsuppanFlorian.mainstage import *
from Weathersim.ZsuppanFlorian.mainscreen import *

import game
import pygame

class MainStage(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = Napsutes()
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        if event.key == pygame.K_ESCAPE:
            pygame.quit()

        if event.key == pygame.K_2:
            self.screen = HoStage()

        if event.key == pygame.K_3:
            self.screen = EsoStage()

        if event.key == pygame.K_1:
            self.screen = NapStage()

        if event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()




MainStage().run()