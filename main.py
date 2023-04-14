from pygame import *
from random import randint
import time as time_module

font.init()
window = display.set_mode((1000, 700))
display.set_caption('Пинг-понг')
window.fill((200,200,200))
clock = time.Clock()
mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        pass

game = True
finish = False
platform1 = Player('platform.png', 10,200,5,50,250)
platform2 = Player('platform2.png', 940,200,5,50,250)


while game:
    for e in event.get():  # получить все события, происходящие в этот момент
        if e.type == QUIT:
            game = False

    platform1.reset()
    platform2.reset()

    display.update()
    clock.tick(60)

