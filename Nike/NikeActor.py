import game
import pygame
from game.simpleworld.ShapeType import ShapeType
from game.scene2d import MyBaseActor

class FatJordan(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/fatjordanact.png")
        self.y = 280
        self.x = 530


class MenuText(game.scene2d.MyLabel):

    def __init__(self, string: str = "Text") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")

class GameBg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/bgpic.jpg")
        self.y = -450



class GameBg2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/bgpic.jpg")
        self.y = -450
        self.x = 1900



class Sztrit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/streett.png")
        self.y = 600
        self.set_width(5000)
        self.hitbox_shape = ShapeType.Rectangle

class FatJordanact(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/fatjordanact.png")
        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.9
        self.y += 500
        self.set_on_key_press_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_w:
            self.y -= 4
        if event.key == pygame.K_s:
            self.y += 4



class LeBron(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/lebronjames.png")
        self.x += 800
        self.y += 500
        self.set_size(150,150)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x -= delta_time * 500
        if self.x > 1080:
            self.x = 1080



class stone(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/Stone.jpg")
        self.set_size(65, 65)

