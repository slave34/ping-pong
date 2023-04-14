from pygame import *
from random import randint
import time as time_module

font.init()
window = display.set_mode((1000, 700))
display.set_caption('Пинг-понг')
window.fill((200,200,200))
clock = time.Clock()
mixer.init()


game = True


while game:
    for e in event.get():  # получить все события, происходящие в этот момент
        if e.type == QUIT:
            game = False

display.update()
clock.tick(60)
