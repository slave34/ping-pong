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
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 700 - 250 - 5:
            self.rect.y += self.speed
    def update_d(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 700 - 250 - 5:
            self.rect.y += self.speed

game = True
finish = False
platform1 = Player('platform.png', 10,200,5,50,250)
platform2 = Player('platform2.png', 940,200,5,50,250)
ball = GameSprite('ball.png', 400,400,10,50,50)
font = font.Font(None, 40)
speed_y = 3
speed_x = 3
win1 = font.render('Победил второй игрок', True, (255, 215,0))
win2= font.render('Победил первый игрок', True, (0, 215,0))
while game:
    if finish != True:
        window.fill((200,200,200))
        platform1.reset()
        platform2.reset()
        platform1.update_l()
        platform2.update_d()
        ball.rect.y += speed_y
        ball.rect.x += speed_x
        if ball.rect.y > 700 - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(platform1,ball):
            speed_x *= -1
        if sprite.collide_rect(platform2,ball):
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(win1,(500,400))
            finish = True
        if ball.rect.x > 1000 - 50:
            window.blit(win2,(400,300))
            finish = True

        ball.reset()

    for e in event.get():  # получить все события, происходящие в этот момент
        if e.type == QUIT:
            game = False






    display.update()
    clock.tick(60)


