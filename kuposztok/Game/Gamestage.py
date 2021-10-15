import game
import pygame
from kuposztok.Game.GameActor import *
from kuposztok.Game.GameActor import *
import kuposztok
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.bg = BgActor()
        self.bg.width = 2400
        self.bg.height = 1400
        a = MyyActor()
        a.y = 0
        self.add_actor(self.bg)
        self.add_actor(a)
        self.button1 = Visszagomb()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = 0
        self.button1.x = 0

        self.joseph = Joseph()
        self.add_actor(self.joseph)
        self.joseph.width = 100
        self.joseph.height = 200
        self.joseph.x = 200
        self.joseph.y = 500

        self.enemy = Enemy()
        self.add_actor(self.enemy)
        self.enemy.width = 30
        self.enemy.height = 50

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.joseph.set_on_key_down_listener(self.on_key_down)
        self.joseph.set_on_key_press_listener(self.iranyitas)
        self.joseph.set_on_key_up_listener(self.on_key_up)

    def iranyitas(self, sender, event, a=50):
        if event.key == pygame.K_w:
            self.joseph.y -= a

    def iranyitas(self, sender, event, a=10):
        if event.key == pygame.K_s:
            self.joseph.y += a
        if event.key == pygame.K_SPACE:
            self.joseph.y -=a
            self.joseph.add_timer(self.t)
            self.joseph.y +=a
            self.joseph.y += a * 10
        if event.key == pygame.K_d:
            self.joseph.x += a * 10
        if event.key == pygame.K_a:
            self.joseph.x -= a * 10
        if event.key == pygame.K_w:
            self.joseph.y -= a * 10
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def on_key_down(self, sender: object, event: pygame.event.Event) -> bool:
        if event.key == pygame.K_SPACE:
            self.joseph.y -= 10

    def on_key_up(self, sender: object, event: pygame.event.Event) -> bool:
        if event.key == pygame.K_SPACE:
            self.joseph.y += 10

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())





