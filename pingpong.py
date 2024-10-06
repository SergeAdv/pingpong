from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.player_image = player_image
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (self.size_x, self.size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 300:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < win_height - 300:
            self.rect.y += self.speed
    

back = (randint(1,255),randint(1,255),randint(1,255))
win_width = 2000
win_height = 1000
window = display.set_mode((win_width,win_height))
window.fill(back)
racket1 = Player('racket.png', 100, 500, 10, 80, 300)
racket2 = Player('racket.png', 1900, 500, 10, 80, 300)
ball = GameSprite('tenis_ball.png', 1000,500,30,80,80)

game = True
clock = time.Clock()
FPS = 60
while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket1.reset()
    racket1.update_l()
    racket2.reset()
    racket2.update_r()
    ball.reset()








    display.update()
    clock.tick(FPS)
    
