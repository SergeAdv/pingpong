from pygame import *
from random import randint

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y, size_x, size_y):
        super().__init__()
        self.player_image = player_image
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (self.size_x, self.size_y))
        self.speedx = player_speed_x
        self.speedy = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speedy
        if keys[K_s] and self.rect.y < win_height - 300:
            self.rect.y += self.speedy
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > 5:
            self.rect.y -= self.speedy
        if keys[K_l] and self.rect.y < win_height - 300:
            self.rect.y += self.speedy
    

back = (randint(1,255),randint(1,255),randint(1,255))
win_width = 2000
win_height = 1000
window = display.set_mode((win_width,win_height))
window.fill(back)
racket1 = Player('racket.png', 100, 500, 10, 10, 80, 300)
racket2 = Player('racket.png', 1900, 500, 10, 10, 80, 300)
ball = GameSprite('tenis_ball.png', 1000, 500, 10, 10, 80, 80)

game = True
clock = time.Clock()
FPS = 60
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.reset()
        racket1.update_l()
        racket2.reset()
        racket2.update_r()
        ball.reset()
        ball.rect.x+=ball.speedx
        ball.rect.y+=ball.speedy
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            ball.speedx*=-1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            ball.speedy*= -1
        if ball.rect.x < 0:
            window.blit(lose1, (1000,500))
            finish = True
        if ball.rect.x > win_width:
            window.blit(lose2, (1000,500))
            finish = True


    display.update()
    clock.tick(FPS)
    
    
