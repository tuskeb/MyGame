import pygame
import time
from pygame.locals import *
from game.scene2d.MyTimers import *
from game.scene2d.MyKeyboardListeners import *
from game.scene2d.MyMouseListeners import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyGame(MyTimers, MyMouseListeners, MyKeyboardListeners):

    _screen_width: int
    _screen_height: int

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        MyTimers.__init__(self)
        MyMouseListeners.__init__(self)
        MyKeyboardListeners.__init__(self)
        pygame.init()
        MyGame._screen_width = width
        MyGame._screen_height = height
        self._p_et: float = 0
        self._elapsed_time: float = 0
        self._frame_limiter: float = 60
        self._frame_count: float = 0
        self._delta_time: float = 1.0 / self._frame_limiter
        self._ticks_from_last_frame: int = 0
        self._screen: 'MyScreen' = None
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        print(self.width)
        print(self.height)
        # https://stackoverflow.com/questions/6395923/any-way-to-speed-up-python-and-pygame
        flags = DOUBLEBUF | HWACCEL | HWSURFACE
        if autosize:
            self._surface: pygame.Surface = pygame.display.set_mode(size=(self.width, self.height), flags=flags)
        else:
            self._surface: pygame.Surface = pygame.display.set_mode(size=(width, height), flags=flags)
        self._running = True
        if autorun:
            self.loop()

    def run(self):
        self.loop()

    def act(self, delta_time: float):
        MyTimers.act(self, delta_time)
#        MyMouseListeners.act(self, delta_time)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                self.exit()
            if self._screen is not None:
                if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEWHEEL:
                    for st in self.screen.stages_reverse:
                        for ac in st.actors_reverse:
                            if ac.is_mouse_event_present():
                                if ac.overlaps_xy(event.pos[0], event.pos[1]):
                                    if ac.do_mouse_event(sender=ac, event=event):
                                        break
                        if st.is_mouse_event_present():
                            if st.do_mouse_event(sender=st, event=event):
                                break
                    if self.is_mouse_event_present():
                        if self.do_mouse_event(sender=st, event=event):
                            break
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    for st in self.screen.stages_reverse:
                        for ac in st.actors_reverse:
                            if ac.is_keyboard_event_present():
                                if ac.do_key_event(sender=ac, event=event):
                                    break
                        if st.is_keyboard_event_present():
                            if st.do_key_event(sender=st, event=event):
                                break
                    if self.is_keyboard_event_present():
                        if self.do_key_event(sender=st, event=event):
                            break
        self._elapsed_time += self.get_delta_time()
        if self._screen is not None:
            self._screen.act(delta_time)

    def draw(self):
        self._frame_count += 1
        if self._screen is not None:
            self._screen.draw()
        if int(self._elapsed_time) != int(self._p_et):
            print("FPS: " + str(self._frame_count))
            self._frame_count = 0
            self._p_et = self._elapsed_time
        pass

    def loop(self):
        # Folyamatosan fut, amíg be nem zárjuk a programot. Alapesetben itt kap helyet a képernyők megjelenítését kezelő
        # program is, azaz lehet vele a képernyőket cserélgetni. Itt érzékeli a felhasználói bemeneteket is.
        # Amennyiben az előre megírt algoritmusok megfelelők, ezt nem kell lecserélni az öröklődéskor.
        self.show()
        while self._running:
            t = pygame.time.get_ticks()
            self.act(self._delta_time)
            self.draw()
            pygame.display.update()
            sleep: float = 1.0 / self._frame_limiter - (pygame.time.get_ticks() - t) / 1000.0
            if sleep > 0:
                time.sleep(sleep)
            self._delta_time = (t - self._ticks_from_last_frame) / 1000.0
            self._ticks_from_last_frame = t
        self.hide()

    def set_screen(self, screen: 'MyScreen') -> 'MyGame':
        if self._screen is not None:
            self._screen.set_game(None)
        self._screen = screen
        self._screen.set_game(self)
        return self

    def exit(self) -> 'MyGame':
        self._running = False
        return self

    def get_screen(self) -> 'MyScreen':
        return self._screen

    def get_delta_time(self) -> float:
        return self._delta_time

    def get_elapsed_time(self) -> float:
        return self._elapsed_time

    @staticmethod
    def get_screen_width() -> int:
        return MyGame._screen_width

    @staticmethod
    def get_screen_height() -> int:
        return MyGame._screen_height

    def get_surface(self) -> pygame.Surface:
        return self._surface

    delta_time: float = property(get_delta_time)
    elapsed_time: float = property(get_elapsed_time)
    screen: 'MyScreen' = property(get_screen, set_screen)
    # screen_width: int = property(get_screen_width)
    # screen_height: int = property(get_screen_height)
    surface: pygame.Surface = property(get_surface)
