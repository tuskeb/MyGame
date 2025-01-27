import game
import pygame
from game.scene2d import MyTickTimer, MyIntervalTimer
import webbrowser
from Impostorsus.Game.WarioActor import *
from game.scene2d import MyBaseActor
import Impostorsus.Game.WarioScr
import random
import sys

class ASD(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        pygame.mouse.set_visible(0)
        # # for i in range(100):
        # #     h = HatterActor1()
        # #     h.x = i * h.w + -150
        # #     self.add_actor(h)
        # self.add_actor(HatterActor1())
        f = open("palya.txt", "r")

        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    a1: MyBaseActor = None
                    a2: MyBaseActor = None
                    a3: MyBaseActor = None
                    a4: MyBaseActor = None
                    if c == "y":
                        a = Kocka()
                    if c == "b":
                        self.a = BillActor()
                    if c == "o":
                        a = Kocka()
                        a1 = Lathatatlan()
                    if c == "p":
                        a = Kocka()
                        a2 = Lathatatlan2()
                    if c == "B":
                        a = CannonActor()
                    if c == "g":
                        a = GroundActor()
                    if c == "j":
                        a = GroundActor()
                        a3 = Lathatatlan3()
                    if c == "k":
                        a = GroundActor()
                        a4 = Lathatatlan4()
                    if c == "l":
                        a = Ground2Actor()
                    if c == "x":
                        a = InvisActor()
                    if c == "S":
                        a = Tabla()
                    if c == "z":
                        a = Zaszlo()
                    if c == "W":
                        self.wario = WarioActor()
                        a = self.wario
                        a1 = self.wario
                        a2 = self.wario
                        a3 = self.wario
                        a4 = self.wario
                    if a is not None:
                        a.x = x * 64
                        a.y = y * 64
                        self.add_actor(a)
                    if a1 is not None:
                        a1.x = x * 64
                        a1.y = y * 64
                        self.add_actor(a1)
                    if a2 is not None:
                        a2.x = x * 64
                        a2.y = y * 64
                        self.add_actor(a2)
                    if a3 is not None:
                        a3.x = x * 64
                        a3.y = y * 64
                        self.add_actor(a3)
                    if a4 is not None:
                        a4.x = x * 64
                        a4.y = y * 64
                        self.add_actor(a4)
                        print(c)
                    x += 1
            else:
                break
            y += 1

        f.close()

        # self.kocka = Kocka()
        # self.add_actor(self.kocka)
        # self.kocka.x = 250
        # self.kocka.y = 350
        # self.kerdo = Question()
        # self.gomba = Gemba()
        # self.add_actor(self.kerdo)
        # self.kerdo.x = 200
        # self.kerdo.y = 350
        # self.wario = WarioActor()
        self.camera.tracking = self.wario
        # self.add_actor(self.wario)
        self.wario.set_on_key_press_listener(self.press)
        self.wario.set_on_key_down_listener(self.key_down)
        #
        #
        # for i in range(100):
        #     g = GroundActor()
        #     g.y = 615
        #     g.x = i * g.w + -150
        #     self.add_actor(g)
        self.sz = MenuSzoveg()
        self.add_actor(self.sz)
        self.sz.set_text("Nyomj")
        self.sz.set_alpha(500)
        self.sz.set_width(25)
        self.sz.set_height(25)
        self.sz.x += 3410
        self.sz.y += 715
        self.sz2 = MenuSzoveg()
        self.add_actor(self.sz2)
        self.sz2.set_text("E-t")
        self.sz2.set_alpha(500)
        self.sz2.set_width(25)
        self.sz2.set_height(25)
        self.sz2.x += 3430
        self.sz2.y += 740
        self.t = MyTickTimer(interval=2.3, func=self.tikk)
        self.add_timer(self.t)
        self.t2 = MyTickTimer(interval=0.4, func=self.tikk2)
        self.add_timer(self.t2)
        self.t3 = MyTickTimer(interval=0.8, func=self.tikk3)
        self.add_timer(self.t3)
        self.q = Question()
        self.add_actor(self.q)
        self.q.y = 320
        self.q.x = 2900


    def tikk(self, sender):
        self.add_actor(self.a)
        self.a.x = +1100
        self.a.y = +700

    def tikk2(self, sender):
        self.wario.image_url = 'Kepek/actorsusus.png'

    def tikk3(self, sender):
        self.wario.image_url = 'Kepek/actorsusus2.png'



    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_d:
            sender.x += 10
            self.camera.set_tracking_window(0.2, 0.2, 0.7, -0.2)
        if event.key == pygame.K_a:
            sender.x -= 10
            self.wario.image_url = 'Kepek/actorsusus3.png'
            self.camera.set_tracking_window(0.4, 0.2, 0.2, -0.2)
        if event.key == pygame.K_RIGHT:
            sender.x += 10
            self.camera.set_tracking_window(0.2, 0.2, 0.7, -0.2)
        if event.key == pygame.K_LEFT:
            sender.x -= 10
            self.camera.set_tracking_window(0.4, 0.2, 0.2, -0.2)


    def interval(self, sender):
        self.wario.x += 100 * self.get_delta_time()
        self.gomba.x += 100 * self.get_delta_time()
        pass

    def key_down(self, sender, event):
        jump_fx = pygame.mixer.Sound("audio/jumpsound.mp3")
        jump_fx.set_volume(0.015)
        print(sender)
        print(event)
        if event.key == pygame.K_w:
            print("'hoppáré'")
            self.wario.ugras()
            jump_fx.play()
        if event.key == pygame.K_r:
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr())
        if event.key == pygame.K_SPACE:
            print("'hoppáré'")
            self.wario.ugras()
            jump_fx.play()
        if event.key == pygame.K_UP:
            print("'hoppáré'")
            self.wario.ugras()
            jump_fx.play()
        if event.key == pygame.K_e:
            pygame.mixer.music.load("audio/jebait.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.04)
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr())


    def act(self, delta_time: float):
        super().act(delta_time)
        overlapsASD: bool = False
        overASD: bool = False
        dead_fx = pygame.mixer.Sound("audio/battya.mp3")
        dead_fx.set_volume(0.04)
        win_fx = pygame.mixer.Sound("audio/winsound.mp3")
        win_fx.set_volume(0.04)

        g = None
        for actorASD in self.actors:
            if isinstance(actorASD, Gemba):
                if actorASD.elapsed_time > 0.5:
                    if self.wario.overlaps(actorASD):
                        # self.gomba = Gemba()
                        self.wario.set_height(200)
                        self.wario.set_width(200)
                        g = actorASD
            if isinstance(actorASD, Kocka):
                if actorASD.y - actorASD.h > self.wario.y:
                    if self.wario.overlaps(actorASD):
                        overlapsASD = True
                        break
            if isinstance(actorASD, GroundActor):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break
            if isinstance(actorASD, CannonActor):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break

            if isinstance(actorASD, InvisActor):
                if self.wario.overlaps(actorASD):
                    overASD = True
                    break
            if isinstance(actorASD, Kocka):
                if self.wario.overlaps(actorASD):
                    self.wario.y += 7.5
            if isinstance(actorASD, Lathatatlan):
                if self.wario.overlaps(actorASD):
                    self.wario.x -= 12
            if isinstance(actorASD, Lathatatlan2):
                if self.wario.overlaps(actorASD):
                    self.wario.x += 12
            if isinstance(actorASD, Lathatatlan3):
                if self.wario.overlaps(actorASD):
                    self.wario.x -= 12
            if isinstance(actorASD, Lathatatlan4):
                if self.wario.overlaps(actorASD):
                    self.wario.x += 12
            if isinstance(actorASD, BillActor):
                if self.wario.overlaps(actorASD):
                    dead_fx.play()
                    self.screen.game.set_screen(Impostorsus.Game.WarioScr.HalalScreen())
            if isinstance(actorASD, Zaszlo):
                if self.wario.overlaps(actorASD):
                    win_fx.play()
                    self.screen.game.set_screen(Impostorsus.Game.WarioScr.WinScreen())
            if isinstance(actorASD, Question):
                if self.wario.overlaps(actorASD):
                    self.remove_actor(self.q)
                    self.k = KunuM()
                    self.add_actor(self.k)
                    self.k.x = 2850
                    self.k.y = 900
            if isinstance(actorASD, KunuM):
                if self.wario.overlaps(actorASD):
                    self.remove_actor(self.k)



            if g is not None:
                g.remove_from_stage()
        #
        # for actorASD in self.actors:
        #     if isinstance(actorASD, GroundActor):
        #         if self.gomba.overlaps(actorASD):
        #             overlapsASD = True
        #             break
        # if overlapsASD:
        #     self.gomba.stop()
        # else:
        #     self.gomba.start()
        #
        # for actorASD in self.actors:
        #     if isinstance(actorASD, Question):
        #         if self.wario.overlaps(actorASD):
        #             overlapsASD = True
        #             break
        # if overlapsASD:
        #     self.wario.stop()
        #     self.add_actor(self.gomba)
        #     self.gomba.x += 200
        #     self.gomba.y += 400
        #     self.remove_actor(self.kerdo)
        #
        # else:
        #     self.wario.start()
        #
        # for actorASD in self.actors:
        #     if isinstance(actorASD, Kocka):
        #         if self.wario.overlaps(actorASD):
        #             overlapsASD = True
        #             break
        # if overlapsASD:
        #     self.wario.stop()
        # else:
        #     self.wario.start()
        #
        # for actorASD in self.actors:
        #     if isinstance(actorASD, GroundActor):
        #         if self.wario.overlaps(actorASD):
        #             overlapsASD = True
        #             break
        if overlapsASD:
            self.wario.stop()
        else:
            self.wario.start()

        if overASD:
            dead_fx.play()
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.HalalScreen())

class ASD2 (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.music.load('audio/rajosan.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.03)
        pygame.mouse.set_visible(10)
        self.b = BackGround()
        self.add_actor(self.b)
        self.b.x += 0
        self.b.y += 0
        self.p = Play()
        self.add_actor(self.p)
        self.p.x += 535
        self.p.y += 180
        self.s = SuperWario()
        self.add_actor(self.s)
        self.s.x += 350
        self.s.y += 75
        self.ex = Exit()
        self.add_actor(self.ex)
        self.ex.x += 535
        self.ex.y += 550
        self.fu = FullScreen()
        self.add_actor(self.fu)
        self.fu.x += 425
        self.fu.y += 475
        self.cr = Credit()
        self.add_actor(self.cr)
        self.cr.x += 500
        self.cr.y += 400
        self.bi = Bindings()
        self.add_actor(self.bi)
        self.bi.x += 475
        self.bi.y += 325
        self.w = Web()
        self.add_actor(self.w)
        self.w.x += 475
        self.w.y += 255
        self.stop = Pause()
        self.add_actor(self.stop)
        self.stop.x += 1030
        self.stop.y += 215
        self.start = Start()
        self.add_actor(self.start)
        self.start.x += 1030
        self.start.y += 215
        self.remove_actor(self.start)
        self.a = MenuSzoveg()
        self.add_actor(self.a)
        self.a.set_text("MARIO - Rajosan - OFFICIAL MUSIC VIDEO")
        self.a.set_alpha(1000)
        self.a.set_width(17)
        self.a.set_height(17)
        self.a.x += 900
        self.a.y += 190
        self.next = Next()
        self.add_actor(self.next)
        self.next.x += 1095
        self.next.y += 215
        self.b = MenuSzoveg()
        self.add_actor(self.b)
        self.b.set_text("Jonas Emil - Spártai Kemál Veretőgép")
        self.b.set_alpha(1000)
        self.b.set_width(18)
        self.b.set_height(18)
        self.b.x += 910
        self.b.y += 190
        self.remove_actor(self.b)
        self.stop1 = Pause()
        self.add_actor(self.stop1)
        self.stop1.x += 1030
        self.stop1.y += 215
        self.remove_actor(self.stop1)
        self.start1 = Start()
        self.add_actor(self.start1)
        self.start1.x += 1030
        self.start1.y += 215
        self.remove_actor(self.start1)
        self.last = Last()
        self.add_actor(self.last)
        self.last.x += 965
        self.last.y += 215
        self.remove_actor(self.last)
        self.c = MenuSzoveg()
        self.add_actor(self.c)
        self.c.set_text("25%")
        self.c.set_alpha(1000)
        self.c.set_width(18)
        self.c.set_height(18)
        self.c.x += 1200
        self.c.y += 220
        self.d = MenuSzoveg()
        self.add_actor(self.d)
        self.d.set_text("50%")
        self.d.set_alpha(1000)
        self.d.set_width(18)
        self.d.set_height(18)
        self.d.x += 1200
        self.d.y += 245
        self.e = MenuSzoveg()
        self.add_actor(self.e)
        self.e.set_text("25%")
        self.e.set_alpha(1000)
        self.e.set_width(18)
        self.e.set_height(18)
        self.e.x += 1200
        self.e.y += 220
        self.remove_actor(self.e)
        self.f = MenuSzoveg()
        self.add_actor(self.f)
        self.f.set_text("50%")
        self.f.set_alpha(1000)
        self.f.set_width(18)
        self.f.set_height(18)
        self.f.x += 1200
        self.f.y += 245
        self.remove_actor(self.f)
        self.p.set_on_mouse_down_listener(self.play)
        self.ex.set_on_mouse_down_listener(self.exit)
        self.fu.set_on_mouse_down_listener(self.fullscreen)
        self.bi.set_on_mouse_down_listener(self.bind)
        self.cr.set_on_mouse_down_listener(self.creator)
        self.w.set_on_mouse_down_listener(self.website)
        self.stop.set_on_mouse_down_listener(self.stopgomb)
        self.start.set_on_mouse_down_listener(self.startgomb)
        self.next.set_on_mouse_down_listener(self.nextgomb)
        self.stop1.set_on_mouse_down_listener(self.stopgomb1)
        self.start1.set_on_mouse_down_listener(self.startgomb1)
        self.last.set_on_mouse_down_listener(self.lastgomb)
        self.c.set_on_mouse_down_listener(self.volume)
        self.d.set_on_mouse_down_listener(self.volume1)
        self.e.set_on_mouse_down_listener(self.volume2)
        self.f.set_on_mouse_down_listener(self.volume3)

    def volume3(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.08)

    def volume2(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.04)

    def volume1(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.08)

    def volume(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.04)


    def nextgomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.stop()
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.play()
                self.remove_actor(self.a)
                self.add_actor(self.b)
                self.add_actor(self.stop1)
                self.remove_actor(self.stop)
                self.remove_actor(self.next)
                self.add_actor(self.last)
                self.remove_actor(self.c)
                self.remove_actor(self.d)
                self.add_actor(self.e)
                self.add_actor(self.f)

    def lastgomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.stop()
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.play()
                self.remove_actor(self.b)
                self.add_actor(self.a)
                self.remove_actor(self.stop1)
                self.add_actor(self.stop)
                self.add_actor(self.next)
                self.remove_actor(self.last)
                self.add_actor(self.c)
                self.add_actor(self.d)
                self.remove_actor(self.e)
                self.remove_actor(self.f)

    def stopgomb1(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.stop()
                self.remove_actor(self.stop1)
                self.add_actor(self.start1)
                self.remove_actor(self.last)
                self.remove_actor(self.e)
                self.remove_actor(self.f)

    def startgomb1(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.play()
                self.remove_actor(self.start1)
                self.add_actor(self.stop1)
                self.add_actor(self.last)
                self.add_actor(self.e)
                self.add_actor(self.f)


    def stopgomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.stop()
                self.remove_actor(self.stop)
                self.add_actor(self.start)
                self.remove_actor(self.next)
                self.remove_actor(self.c)
                self.remove_actor(self.d)

    def startgomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.play()
                self.remove_actor(self.start)
                self.add_actor(self.stop)
                self.add_actor(self.next)
                self.add_actor(self.c)
                self.add_actor(self.d)


    def creator(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScr.CreditScreen())

    def website(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                webbrowser.open('http://localhost:63342/MyGame/Impostorsus/kunoldal/kunweb.html?_ijt=cjm94dbrm2t5ma8c7htoogeun')

    def bind(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScr.BindingsScreen())

    def exit(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                quit()

    def play(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScr.PalyaScr())

    def fullscreen(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.display.toggle_fullscreen()


class BindingsStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mouse.set_visible(0)
        self.a = MenuSzoveg()
        self.add_actor(self.a)
        self.a.set_text("Gombok:")
        self.a.set_alpha(500)
        self.a.set_width(75)
        self.a.set_height(75)
        self.a.x += 250
        self.a.y += 50
        self.b = MenuSzoveg()
        self.add_actor(self.b)
        self.b.set_text("W,A,D,SPACE = Irányítás")
        self.b.set_alpha(500)
        self.b.set_width(50)
        self.b.set_height(50)
        self.b.x += 250
        self.b.y += 175
        self.c = MenuSzoveg()
        self.add_actor(self.c)
        self.c.set_text("F11 = FullScreen")
        self.c.set_alpha(500)
        self.c.set_width(50)
        self.c.set_height(50)
        self.c.x += 250
        self.c.y += 250
        self.d = MenuSzoveg()
        self.add_actor(self.d)
        self.d.set_text("BACKSPACE = Menü")
        self.d.set_alpha(500)
        self.d.set_width(50)
        self.d.set_height(50)
        self.d.x += 250
        self.d.y += 325
        self.e = MenuSzoveg()
        self.add_actor(self.e)
        self.e.set_text("ESC = Kilépés")
        self.e.set_alpha(500)
        self.e.set_width(50)
        self.e.set_height(50)
        self.e.x += 250
        self.e.y += 400
        self.f = MenuSzoveg()
        self.add_actor(self.f)
        self.f.set_text("CTRL= Zene megállítása")
        self.f.set_alpha(500)
        self.f.set_width(50)
        self.f.set_height(50)
        self.f.x += 250
        self.f.y += 475


class CreditStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.a = MenuSzoveg()
        self.add_actor(self.a)
        self.a.set_text("Készítők:")
        self.a.set_alpha(500)
        self.a.set_width(75)
        self.a.set_height(75)
        self.a.x += self.width /3 - self.a.get_width() / 2
        self.a.y += self.height /6 - self.a.get_height() / 2
        self.b = MenuSzoveg()
        self.add_actor(self.b)
        self.b.set_text("K.Bálint")
        self.b.set_alpha(500)
        self.b.set_width(50)
        self.b.set_height(50)
        self.b.x += 250
        self.b.y += 175
        self.c = MenuSzoveg()
        self.add_actor(self.c)
        self.c.set_text("Sz.Bálint")
        self.c.set_alpha(500)
        self.c.set_width(50)
        self.c.set_height(50)
        self.c.x += 250
        self.c.y += 250
        self.d = MenuSzoveg()
        self.add_actor(self.d)
        self.d.set_text("Márk")
        self.d.set_alpha(500)
        self.d.set_width(50)
        self.d.set_height(50)
        self.d.x += 250
        self.d.y += 325

class HalalStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.h = Halalkep()
        self.add_actor(self.h)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.h.x += self.width /2 - self.h.get_width() / 2
        self.h.y += self.height /2 - self.h.get_height() / 2
        self.set_on_key_down_listener(self.r)

    def r(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_r:
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr())

class HalalStage2 (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.pontbeolvasas()
        self.h = Halalkep()
        self.add_actor(self.h)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.h.x += self.width /2 - self.h.get_width() / 2
        self.h.y += self.height /2 - self.h.get_height() / 2
        self.set_on_key_down_listener(self.r)
        self.pontkiiras = game.scene2d.MyLabel("Elért idő: {ido}mp".format(ido=self.score))
        self.pontkiiras.x = 490
        self.pontkiiras.y = 200
        self.add_actor(self.pontkiiras)

    def pontbeolvasas(self):
        with open('Save/marioido', 'r') as file:
            self.score = int(file.readline())
            file.close()

    def r(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_r:
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr2())



class WinStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.pontbeolvasas()
        self.w = Winkep()
        self.add_actor(self.w)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.w.x += self.width /2 - self.w.get_width() / 2
        self.w.y += self.height /2 - self.w.get_height() / 2
        self.pontkiiras = game.scene2d.MyLabel("Elért idő: {ido}mp".format(ido=self.score))
        self.pontkiiras.x = 490
        self.pontkiiras.y = 200
        self.add_actor(self.pontkiiras)

    def pontbeolvasas(self):
        with open('Save/marioido', 'r') as file:
            self.score = int(file.readline())
            file.close()


class PalyaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.h1 = BackGround()
        self.add_actor(self.h1)
        self.h1.set_width(400)
        self.h1.x = 230
        self.h1.y = 275
        self.k1 = Keret()
        self.add_actor(self.k1)
        self.k1.x = 230
        self.k1.y = 260
        self.h2 = BackGround2()
        self.add_actor(self.h2)
        self.h2.set_height(360)
        self.h2.x = 730
        self.h2.y = 262
        self.m1 = Map1()
        self.add_actor(self.m1)
        self.m1.x = 270
        self.m1.y = 200
        self.m2 = Map2()
        self.add_actor(self.m2)
        self.m2.x = 730
        self.m2.y = 200
        self.m1.set_on_mouse_down_listener(self.palya1)
        self.h1.set_on_mouse_down_listener(self.palya1)
        self.k1.set_on_mouse_down_listener(self.palya1)
        self.m2.set_on_mouse_down_listener(self.palya2)
        self.h2.set_on_mouse_down_listener(self.palya2)

    def palya1(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr2())

    def palya2(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioKartScr())

class ASD3(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        pygame.mouse.set_visible(0)
        f = open("palya2.txt", "r")


        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    a1: MyBaseActor = None
                    a2: MyBaseActor = None
                    a3: MyBaseActor = None
                    a4: MyBaseActor = None
                    if c == "y":
                        a = Kocka()
                    if c == "L":
                        a = Ladder()
                    if c == "P":
                        a = Pipe()
                    if c == "M":
                        a = Pipe1()
                    if c == "h":
                        a = KockaHalf()
                    if c == "b":
                        self.a = BillActor()
                    if c == "o":
                        a = Kocka()
                        a1 = Lathatatlan()
                    if c == "p":
                        a = Kocka()
                        a2 = Lathatatlan2()
                    if c == "B":
                        a = CannonActor()
                    if c == "g":
                        a = GroundActor()
                    if c == "j":
                        a = GroundActor()
                        a3 = Lathatatlan3()
                    if c == "k":
                        a = GroundActor()
                        a4 = Lathatatlan4()
                    if c == "l":
                        a = Ground2Actor()
                    if c == "x":
                        a = InvisActor()
                    if c == "S":
                        a = Tabla()
                    if c == "z":
                        a = Zaszlo2()
                    if c == "W":
                        self.wario = WarioActor()
                        a = self.wario
                        a1 = self.wario
                        a2 = self.wario
                        a3 = self.wario
                        a4 = self.wario
                    if a is not None:
                        a.x = x * 64
                        a.y = y * 64
                        self.add_actor(a)
                    if a1 is not None:
                        a1.x = x * 64
                        a1.y = y * 64
                        self.add_actor(a1)
                    if a2 is not None:
                        a2.x = x * 64
                        a2.y = y * 64
                        self.add_actor(a2)
                    if a3 is not None:
                        a3.x = x * 64
                        a3.y = y * 64
                        self.add_actor(a3)
                    if a4 is not None:
                        a4.x = x * 64
                        a4.y = y * 64
                        self.add_actor(a4)
                        print(c)
                    x += 1
            else:
                break
            y += 1

        f.close()

        self.camera.tracking = self.wario
        # self.add_actor(self.wario)
        self.wario.set_on_key_press_listener(self.press)
        self.wario.set_on_key_down_listener(self.key_down)
        self.sz = MenuSzoveg()
        self.add_actor(self.sz)
        self.sz.set_text("Ugorj")
        self.sz.set_alpha(500)
        self.sz.set_width(25)
        self.sz.set_height(25)
        self.sz.x += 1810
        self.sz.y += 460
        self.sz2 = MenuSzoveg()
        self.add_actor(self.sz2)
        self.sz2.set_text("bele")
        self.sz2.set_alpha(500)
        self.sz2.set_width(25)
        self.sz2.set_height(25)
        self.sz2.x += 1815
        self.sz2.y += 485
        self.sz3 = MenuSzoveg()
        self.add_actor(self.sz3)
        self.sz3.set_text("--->")
        self.sz3.set_alpha(500)
        self.sz3.set_width(25)
        self.sz3.set_height(25)
        self.sz3.x += 1248
        self.sz3.y += 982
        self.t = MyTickTimer(interval=3, func=self.tikk)
        self.add_timer(self.t)
        self.t2 = MyTickTimer(interval=0.4, func=self.tikk2)
        self.add_timer(self.t2)
        self.t3 = MyTickTimer(interval=0.8, func=self.tikk3)
        self.add_timer(self.t3)
        self.q = Question()
        self.add_actor(self.q)
        self.q.x = 2150
        self.q.y = 880
        self.timer = MyTickTimer(interval=2.5, func=self.idocucc)
        self.add_timer(self.timer)
        self.camera.set_tracking_window(0.2, 0.2, 0.5, -0.3)
        self.pont = 0
        self.pontkiiras = game.scene2d.MyLabel("Idő: {ido}mp".format(ido=self.pont))
        self.add_actor(self.pontkiiras)
        self.pontkiiras.x = 10
        self.pontkiiras.y = 100
        self.ponttimer = MyTickTimer(func=self.ponttimerszamolo, interval=1)
        self.add_timer(self.ponttimer)

    def pontiras(self):
        self.pontkiiras.set_text("Idő: {ido}mp".format(ido=self.pont))
        f = open("Save/marioido", "w")
        f.write(str(self.pont))
        f.close()

    def ponttimerszamolo(self, sender):
        self.pont += 1
        self.pontkiiras.set_text("Idő: {point}mp".format(point=self.pont))
        self.pontiras()

    def idocucc(self, sender):
        self.c = Cloud()
        self.add_actor(self.c)
        self.c3 = Cloud3()
        self.add_actor(self.c3)
        self.c.y = random.Random().randint(300, 1500)
        self.c.x = random.Random().randint(100, 900)
        self.c3.y = random.Random().randint(300, 1500)
        self.c3.x = random.Random().randint(100, 900)

    def tikk(self, sender):
        self.add_actor(self.a)
        self.a.x = +1600
        self.a.y = +630

    def tikk2(self, sender):
        self.wario.image_url = 'Kepek/actorsusus.png'

    def tikk3(self, sender):
        self.wario.image_url = 'Kepek/actorsusus2.png'



    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_d:
            sender.x += 10
            self.camera.set_tracking_window(0.2, 0.2, 0.7, -0.2)
        if event.key == pygame.K_a:
            sender.x -= 10
            self.wario.image_url = 'Kepek/actorsusus3.png'
            self.camera.set_tracking_window(0.4, 0.2, 0.2, -0.2)
        if event.key == pygame.K_RIGHT:
            sender.x += 10
            self.camera.set_tracking_window(0.2, 0.2, 0.7, -0.2)
        if event.key == pygame.K_LEFT:
            sender.x -= 10
            self.camera.set_tracking_window(0.4, 0.2, 0.2, -0.2)


    def interval(self, sender):
        self.wario.x += 100 * self.get_delta_time()
        self.gomba.x += 100 * self.get_delta_time()
        pass

    def key_down(self, sender, event):
        jump_fx = pygame.mixer.Sound("audio/jumpsound.mp3")
        jump_fx.set_volume(0.015)
        print(sender)
        print(event)
        if event.key == pygame.K_w:
            print("'hoppáré'")
            self.wario.ugras()
            jump_fx.play()
        if event.key == pygame.K_r:
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr2())
        if event.key == pygame.K_SPACE:
            print("'hoppáré'")
            self.wario.ugras()
            jump_fx.play()
        if event.key == pygame.K_UP:
            print("'hoppáré'")
            self.wario.ugras()
            jump_fx.play()
        if event.key == pygame.K_e:
            pygame.mixer.music.load("audio/jebait.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.04)
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr2())


    def act(self, delta_time: float):
        super().act(delta_time)
        overlapsASD: bool = False
        overASD: bool = False
        dead_fx = pygame.mixer.Sound("audio/battya.mp3")
        dead_fx.set_volume(0.04)
        win_fx = pygame.mixer.Sound("audio/winsound.mp3")
        win_fx.set_volume(0.04)

        g = None
        for actorASD in self.actors:
            if isinstance(actorASD, Gemba):
                if actorASD.elapsed_time > 0.5:
                    if self.wario.overlaps(actorASD):
                        # self.gomba = Gemba()
                        self.wario.set_height(200)
                        self.wario.set_width(200)
                        g = actorASD
            if isinstance(actorASD, Kocka):
                if actorASD.y - actorASD.h > self.wario.y:
                    if self.wario.overlaps(actorASD):
                        overlapsASD = True
                        break
            if isinstance(actorASD, KockaHalf):
                if actorASD.y - actorASD.h > self.wario.y:
                    if self.wario.overlaps(actorASD):
                        overlapsASD = True
                        break
            if isinstance(actorASD, GroundActor):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break
            if isinstance(actorASD, CannonActor):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break

            if isinstance(actorASD, InvisActor):
                if self.wario.overlaps(actorASD):
                    overASD = True
                    break
            if isinstance(actorASD, Kocka):
                if self.wario.overlaps(actorASD):
                    self.wario.y += 7.5
            if isinstance(actorASD, Lathatatlan):
                if self.wario.overlaps(actorASD):
                    self.wario.x -= 12
            if isinstance(actorASD, Lathatatlan2):
                if self.wario.overlaps(actorASD):
                    self.wario.x += 12
            if isinstance(actorASD, Lathatatlan3):
                if self.wario.overlaps(actorASD):
                    self.wario.x -= 12
            if isinstance(actorASD, Lathatatlan4):
                if self.wario.overlaps(actorASD):
                    self.wario.x += 12
            if isinstance(actorASD, BillActor):
                if self.wario.overlaps(actorASD):
                    dead_fx.play()
                    self.ponttimer.stop()
                    self.screen.game.set_screen(Impostorsus.Game.WarioScr.HalalScreen2())
            if isinstance(actorASD, Zaszlo2):
                if self.wario.overlaps(actorASD):
                    win_fx.play()
                    self.ponttimer.stop()
                    self.screen.game.set_screen(Impostorsus.Game.WarioScr.WinScreen())
            if isinstance(actorASD, Question):
                if self.wario.overlaps(actorASD):
                    self.remove_actor(self.q)
                    self.k = KunuM()
                    self.add_actor(self.k)
                    self.k.x = 2035
                    self.k.y = 1220
            if isinstance(actorASD, KunuM):
                if self.wario.overlaps(actorASD):
                    self.remove_actor(self.k)
                    if self.elapsed_time > 0:
                        self.t = MyTickTimer(interval=0.2, func=self.tikktok)
                        self.add_timer(self.t)
            if isinstance(actorASD, Pipe):
                if self.wario.overlaps(actorASD):
                    self.wario.x += 2325
                    self.wario.y -= 50
            if isinstance(actorASD, Pipe1):
                if self.wario.overlaps(actorASD):
                    self.wario.x -= 2325
                    self.wario.y -= 50
            if isinstance(actorASD, Ladder):
                if self.wario.overlaps(actorASD):
                    self.wario.y -= 20

            if g is not None:
                g.remove_from_stage()

        if overlapsASD:
            self.wario.stop()
        else:
            self.wario.start()

        if overASD:
            dead_fx.play()
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.HalalScreen2())

    def tikktok(self, sender):
        self.screen.r = random.randint(0, 255)
        self.screen.g = random.randint(0, 255)
        self.screen.b = random.randint(0, 255)

class WarioKartStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        pygame.mixer.music.load('audio/rajosan.mp3')
        pygame.mixer.music.stop()
        pygame.mixer.music.load('audio/spartai.mp3')
        pygame.mixer.music.stop()
        pygame.mixer.music.load('audio/racemusic.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.03)
        pygame.mouse.set_visible(1)
        f = open("palya3", "r")

        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    if c == "r":
                        a = Road()
                    if c == "e":
                        a = KartEnemy()
                    if c == "b":
                        a = Barrel()
                    if c == "g":
                        a = BananKart()
                    if c == "o":
                        a = GombaKart()
                    if c == "p":
                        a = Ramp()
                    if c == "l":
                        a = LathatatlanKart3()
                    if c == "f":
                        a = Finish()
                    if a is not None:
                        a.x = x * 64
                        a.y = y * 64
                        self.add_actor(a)

                        print(c)
                    x += 1
            else:
                break
            y += 1

        f.close()
        self.l1 = LathatatlanKart()
        self.add_actor(self.l1)
        self.l1.x = 25
        self.l1.y = 150
        self.l2 = LathatatlanKart2()
        self.add_actor(self.l2)
        self.l2.x = 1170
        self.l2.y = 150
        self.wario = WarioKart()
        self.add_actor(self.wario)
        self.camera.tracking = self.wario
        self.wario.set_on_key_press_listener(self.press)
        self.set_on_key_down_listener(self.key_down)
        self.wario.x = 600
        self.wario.y = 150
        self.bl = Blue()
        self.add_actor(self.bl)
        self.mk = MarioKartSkin()
        self.add_actor(self.mk)
        self.mk.x = 350
        self.mk.y = 300
        self.wk = WarioKartSkin()
        self.add_actor(self.wk)
        self.wk.x = 485
        self.wk.y = 300
        self.sz = MenuSzoveg()
        self.add_actor(self.sz)
        self.sz.set_text("Válassz skint")
        self.sz.set_alpha(500)
        self.sz.set_width(50)
        self.sz.set_height(50)
        self.sz.x += 460
        self.sz.y += 175
        self.tk = TodKartSkin()
        self.add_actor(self.tk)
        self.tk.x = 570
        self.tk.y = 300
        self.dk = DonkeyKartSkin()
        self.add_actor(self.dk)
        self.dk.x = 680
        self.dk.y = 300
        self.lk = LuigiKartSkin()
        self.add_actor(self.lk)
        self.lk.x = 790
        self.lk.y = 300
        self.wk.set_on_mouse_down_listener(self.skin1)
        self.mk.set_on_mouse_down_listener(self.skin2)
        self.tk.set_on_mouse_down_listener(self.skin3)
        self.dk.set_on_mouse_down_listener(self.skin4)
        self.lk.set_on_mouse_down_listener(self.skin5)
        self.pont = 0
        self.pontkiiras = game.scene2d.MyLabel("Idő: {ido}mp".format(ido=self.pont))
        self.pontkiiras.x = 1075
        self.pontkiiras.y = 50
        self.add_actor(self.pontkiiras)
        self.camera.set_tracking_window(0, 0, 0, 0.7)
        self.ponttimer = MyTickTimer(func=self.ponttimerszamolo, interval=1)
        self.add_timer(self.ponttimer)

        self.hal = HalalKart()
        self.add_actor(self.hal)
        self.hal.x = 500
        self.hal.y = -200

    def pontiras(self):
        self.pontkiiras.set_text("Idő: {ido}mp".format(ido=self.pont))
        f = open("Save/kartido", "w")
        f.write(str(self.pont))
        f.close()

    def ponttimerszamolo(self, sender):
        if self.elapsed_time > 3:
            self.pont += 1
            self.pontkiiras.set_text("Idő: {point}mp".format(point=self.pont))
            self.pontiras()

    def skin1(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.wario.image_url = 'Kepek/wariokart.png'
    def skin2(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.wario.image_url = 'Kepek/mariokart.png'
                self.wario.hitbox_scale_w = 0.65
                self.wario.hitbox_scale_h = 0.85
    def skin3(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.wario.image_url = 'Kepek/todkart.png'
                self.wario.hitbox_scale_w = 0.65
                self.wario.hitbox_scale_h = 0.85
    def skin4(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.wario.image_url = 'Kepek/donkeykart.png'
                self.wario.hitbox_scale_w = 0.65
                self.wario.hitbox_scale_h = 0.85
    def skin5(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.wario.image_url = 'Kepek/luigikart.png'
                self.wario.hitbox_scale_w = 0.65
                self.wario.hitbox_scale_h = 0.85

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_r:
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioKartScr())


    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_d:
            sender.x += 3.5
            self.camera.set_tracking_window(0, 0, 0, 0.7)
        if event.key == pygame.K_a:
            sender.x -= 3.5
            self.camera.set_tracking_window(0, 0, 0, 0.7)
        if event.key == pygame.K_RIGHT:
            sender.x += 3.5
            self.camera.set_tracking_window(0, 0, 0, 0.7)
        if event.key == pygame.K_LEFT:
            sender.x -= 3.5
            self.camera.set_tracking_window(0, 0, 0, 0.7)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 4:
            self.pontkiiras.y += 200 * delta_time
        if self.elapsed_time > 3:
            self.mk.x = +3000
            self.bl.x = +3000
            self.wk.x = +3000
            self.sz.x = +3000
            self.tk.x = +3000
            self.dk.x = +3000
            self.lk.x = +3000
            pygame.mouse.set_visible(0)

        for i in self.actors:
            if isinstance(i, LathatatlanKart):
                if self.wario.overlaps(i):
                    self.wario.x += 3.5
            if isinstance(i, LathatatlanKart2):
                if self.wario.overlaps(i):
                    self.wario.x -= 3.5
            if isinstance(i, Finish):
                if self.wario.overlaps(i):
                    self.screen.game.set_screen(Impostorsus.Game.WarioScr.KartWinScr())
                    pygame.mixer.music.load('audio/winsound.mp3')
                    pygame.mixer.music.play()
                    self.ponttimer.stop()
            if isinstance(i, Barrel):
                if self.wario.overlaps(i):
                    self.wario.y -= 100
                    self.pontkiiras.y -= 100
                    self.l1.y -= 100
                    self.l2.y -= 100
            if isinstance(i, Ramp):
                if self.wario.overlaps(i):
                    self.wario.y += 100
                    self.pontkiiras.y += 100
                    self.l1.y += 100
                    self.l2.y += 100
                    self.hal.y += 100
            if isinstance(i, GombaKart):
                if self.wario.overlaps(i):
                    self.wario.image_url = 'Kepek/kunukart.png'
                    self.wario.hitbox_scale_w = 0.65
                    self.wario.hitbox_scale_h = 0.85
            if isinstance(i, BananKart):
                if self.wario.overlaps(i):
                    self.wario.y -= 120 * delta_time
                    self.l1.y -= 120 * delta_time
                    self.l2.y -= 120 * delta_time
                    self.pontkiiras.y -= 120 * delta_time
                    self.hal.y -= 120 * delta_time
            if isinstance(i, KartEnemy):
                if self.wario.overlaps(i):
                    self.screen.game.set_screen(Impostorsus.Game.WarioScr.KartHalalScr())
                    pygame.mixer.music.load('audio/battya.mp3')
                    pygame.mixer.music.play()
                    self.ponttimer.stop()
            if isinstance(i, HalalKart):
                if self.wario.overlaps(i):
                    self.screen.game.set_screen(Impostorsus.Game.WarioScr.KartHalalScr())
                    pygame.mixer.music.load('audio/battya.mp3')
                    pygame.mixer.music.play()
                    self.ponttimer.stop()



class KartHalalStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.pontbeolvasas()
        self.p = MarioDead()
        self.add_actor(self.p)
        self.p.x = 525
        self.p.y = 275
        self.h = Halalkep()
        self.add_actor(self.h)
        self.h.x = 405
        self.h.y = 100
        self.pontkiiras = game.scene2d.MyLabel("Elért idő: {ido}mp".format(ido=self.score))
        self.pontkiiras.x = 490
        self.pontkiiras.y = 200
        self.add_actor(self.pontkiiras)


    def r(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_r:
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioKartScr())

    def pontbeolvasas(self):
        with open('Save/kartido', 'r') as file:
            self.score = int(file.readline())
            file.close()

class KartWinStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.pontbeolvasas()
        self.p = KartPodium()
        self.add_actor(self.p)
        self.p.x = 375
        self.p.y = 350
        self.h = Winkep()
        self.add_actor(self.h)
        self.h.x = 405
        self.h.y = 50
        self.m = MarioKartWin1()
        self.add_actor(self.m)
        self.m.x = 540
        self.m.y = 200
        self.t2 = MyTickTimer(interval=0.3, func=self.tikk)
        self.add_timer(self.t2)
        self.t3 = MyTickTimer(interval=0.6, func=self.tikk2)
        self.add_timer(self.t3)
        self.pontkiiras = game.scene2d.MyLabel("Elért idő: {ido}mp".format(ido=self.score))
        self.pontkiiras.x = 490
        self.pontkiiras.y = 200
        self.add_actor(self.pontkiiras)

    def pontbeolvasas(self):
        with open('Save/kartido', 'r') as file:
            self.score = int(file.readline())
            file.close()

    def tikk(self, sender):
        self.m.image_url = 'Kepek/mariokartwin1.png'

    def tikk2(self, sender):
        self.m.image_url = 'Kepek/mariokartwin2.png'










