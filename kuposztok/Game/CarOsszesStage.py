import game
import pygame
import random
from kuposztok.Game.GameActor import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
import kuposztok.CaraValt.CaraValtStage
from game.scene2d.MyGame import MyGame
from kuposztok.Lose.LoseScreen import LoseScreen


class CarOsszesStage(game.scene2d.MyStage):

    def __init__(self, carvalt: int, money: int, maxScore: int):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../kuposztok/music/gamemusica.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.bg = BgActor()
        self.bg.width = 2400
        self.bg.height = 1400
        self.bg.y = 0
        self.bg.z_index = 1
        self.add_actor(self.bg)
        self.bg2 = BgActor2()
        self.bg2.y = -1080
        self.bg2.z_index = 1
        self.bg2.width = 2400
        self.bg2.height = 1400
        self.add_actor(self.bg2)
        self.button1 = Visszagomb()
        self.button1.z_index = 101
        self.add_actor(self.button1)
        self.button1.width = 95
        self.button1.height = 45
        self.button1.y = 0
        self.button1.x = 0
        self.t = MyIntervalTimer(func=self.Timer, start_time=0, stop_time=9223372036854775807)
        self.add_timer(self.t)
        self.carvalt = carvalt

        self.maxScore = maxScore

        self.money = money

        # self.fpslabel = game.scene2d.MyLabel("FPS: " + str(self._frame_count))
        # self.add_actor(self.fpslabel)
        # self.fpslabel.x = self.width - 150
        # self.fpslabel.y = self.height / 30
        # self.fpslabel.set_color(0, 0, 0)
        # self.fpslabel.width = 50
        # self.fpslabel.height = 25
        # self.fpslabel.z_index = 80

        self.score = 0
        self.scorelabel = game.scene2d.MyLabel("Score:" + str(self.score))
        self.add_actor(self.scorelabel)
        self.scorelabel.x = 0
        self.scorelabel.y = self.height - self.scorelabel.get_height()
        self.scorelabel.set_color(0, 0, 0)


        if self.carvalt == 11:
            self.joseph = SnowBoard()
        if self.carvalt == 21:
            self.joseph = Sledge()
        if self.carvalt == 31:
            self.joseph = SnowMobile()
        if self.carvalt == 41:
            self.joseph = Ski()
        if self.carvalt == 12:
            self.joseph = SnowMobile()
            self.joseph2 = SnowMobile()
        if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
            print("bemegy")
            print(self.carvalt)
            if self.carvalt == 22:
                self.joseph = Sledge()
                self.joseph2 = Sledge()
            if self.carvalt == 32:
                self.joseph = SnowBoard()
                self.joseph2 = SnowBoard()
            if self.carvalt == 42:
                self.joseph = Ski()
                self.joseph2 = Ski()

        self.joseph.width = 100
        self.joseph.z_index = 5
        self.joseph.height = 200
        self.joseph.x = 200
        self.joseph.y = 500
        self.joseph.hitbox_scale_w = 0.4
        self.joseph.hitbox_scale_h = 0.4
        self.joseph.hitbox_shape = game.simpleworld.ShapeType.Circle
        self.joseph.debug = False
        self.add_actor(self.joseph)

        if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
            self.joseph2.width = 100
            self.joseph2.z_index = 5
            self.joseph2.height = 200
            self.joseph2.x = 700
            self.joseph2.y = self.joseph.get_y()
            self.joseph2.hitbox_scale_w = 0.4
            self.joseph2.hitbox_scale_h = 0.4
            self.joseph2.hitbox_shape = game.simpleworld.ShapeType.Circle
            self.joseph2.debug = False
            self.add_actor(self.joseph2)

        self.newgame = Newgame()
        self.newgame = Newgame()
        self.newgame.x = self.width - 300
        self.newgame.y = self.height - self.height + 250

        for i in range(10):
            self.enemy2 = Enemy()
            self.add_actor(self.enemy2)
            self.enemy2.width = 100
            self.enemy2.height = 100
            self.enemy2.z_index = 5
            self.enemy2.x = random.Random().randint(0, self.width - 200)
            self.enemy2.y = random.Random().randint(0 - self.height, 0)

        self.trap = Trap()
        self.add_actor(self.trap)
        self.trap.width = 100
        self.trap.height = 100
        self.trap.z_index = 5
        self.trap.x = random.Random().randint(0, self.width)
        self.trap.y = random.Random().randint(0 - self.height, 0)

        self.suport = SportDrink()
        self.add_actor(self.suport)
        self.suport.width = 100
        self.suport.height = 100
        self.suport.z_index = 5
        self.suport.x = random.Random().randint(0, self.width)
        self.suport.y = random.Random().randint(0 - self.height, 0)

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.joseph.set_on_key_press_listener(self.iranyitas)
        self.newgame.set_on_mouse_down_listener(self.NewG)
        self.set_on_key_down_listener(self.elfordul)
        self.set_on_key_up_listener(self.visszafordul)

    def filebaolvasas(self):
        with open('../kuposztok/Save/file.txt', 'r') as file:
            self.max_scoreno = int(file.readline())
            self.money = int(file.readline())
            file.close()

    def filebairas(self):
        with open('../kuposztok/Save/file.txt', 'w') as file:
            file.write(str(self.max_scoreno))
            if self.score < 100:
                self.money = self.money + 10
            if self.score > 100 and self.score < 500:
                self.money = self.money + 100
            if self.score > 500 and self.score < 1000:
                self.money = self.money + 500
            if self.score > 1000 and self.score < 5000:
                self.money = self.money + 1500
            if self.score > 5000 and self.score < 15000:
                self.money = self.money + 3000
            if self.score > 15000 and self.score < 50000:
                self.money = self.money + 10000
            if self.score > 50000 and self.score < 100000:
                self.money = self.money + 50000
            if self.score > 100000:
                self.money = self.money + 100000
            file.write("\n" + str(self.money))
            file.close()

    def Timer(self, sender):
        self.score = self.score + 1
        self.scorelabel.set_text("Score:" + str(self.score))
        self.vesztettellabel = game.scene2d.MyLabel("Sajnálom a játék végetért számodra, az elért pontszámod:" + str(self.score))
        self.vesztettellabel.x = self.width / 18
        self.vesztettellabel.y = 200
        self.vesztettellabel.set_font_size(55)
        self.vesztettellabel.z_index = 100

    def act(self, delta_time: float):
        super().act(delta_time)
        self.filebaolvasas()
        self.filebairas()
        if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
            if self.joseph.overlaps(self.joseph2):
                self.screen.game.set_screen(kuposztok.Lose.LoseScreen.LoseScreen(score=self.score, maxScore=self.maxScore))
        if self.joseph.y == self.height:
            self.screen.game.set_screen(kuposztok.Lose.LoseScreen.LoseScreen(score=self.score, maxScore=self.maxScore))
        if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
            if self.joseph2.y == self.height:
                self.screen.game.set_screen(kuposztok.Lose.LoseScreen.LoseScreen(score=self.score, maxScore=self.maxScore))
        for i in self.actors:
            if isinstance(i, Enemy):
                if self.joseph.overlaps(i):
                    self.screen.game.set_screen(kuposztok.Lose.LoseScreen.LoseScreen(score=self.score, maxScore=self.maxScore))
                if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
                    if self.joseph2.overlaps(i):
                        self.screen.game.set_screen(kuposztok.Lose.LoseScreen.LoseScreen(score=self.score, maxScore=self.maxScore))
        for k in self.actors:
            if isinstance(k, SportDrink):
                if self.joseph.overlaps(k):
                    if self.joseph.y > 0 and self.joseph.y < self.height:
                        self.score = self.score + 2000
                        self.joseph.y = self.joseph.y - 100
                if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
                    if self.joseph2.overlaps(k):
                        self.score = self.score + 500
                        self.joseph2.y = self.joseph2.y - 100
        for t in self.actors:
            if isinstance(t, Trap):
                if self.joseph.overlaps(t):
                    if self.joseph.y < self.height and self.joseph.y > 0:
                        self.joseph.y = self.joseph.y + 10
        for q in self.actors:
            if isinstance(q, Trap):
                if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
                    if self.joseph2.overlaps(q):
                        self.joseph2.y = self.joseph2.y + 10



    def iranyitas(self, sender, event, a=10):
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        if event.key == pygame.K_d:
            if self.joseph.x < self.width - 100:
                self.joseph.x += a
        if event.key == pygame.K_a:
            if self.joseph.x > 0:
                self.joseph.x -= a
        if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
            if event.key == pygame.K_RIGHT:
                if self.joseph2.x < self.width - 200:
                    self.joseph2.x += a
            if event.key == pygame.K_LEFT:
                if self.joseph2.x > 0:
                    self.joseph2.x -= a

        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def elfordul(self, sender, event):
        if event.key == pygame.K_d:
            self.joseph.rotate_with(+22)
        if event.key == pygame.K_a:
            self.joseph.rotate_with(-22)
        if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
            if event.key == pygame.K_RIGHT:
                self.joseph2.rotate_with(+22)
            if event.key == pygame.K_LEFT:
                self.joseph2.rotate_with(-22)

    def visszafordul(self, sender, event):
        if event.key == pygame.K_d:
            self.joseph.rotate_with(-22)
        if event.key == pygame.K_a:
            self.joseph.rotate_with(+22)
        if self.carvalt == 12 or self.carvalt == 22 or self.carvalt == 32 or self.carvalt == 42:
            if event.key == pygame.K_RIGHT:
                self.joseph2.rotate_with(-22)
            if event.key == pygame.K_LEFT:
                self.joseph2.rotate_with(+22)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def NewG(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(CarOsszesStage(carvalt=self.carvalt))