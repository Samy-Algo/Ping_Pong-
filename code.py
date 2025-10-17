# type: ignore
from pygame import* 

class GameSprite(sprite.Sprite):
    def __init__(self, filename, width, height, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
                
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    

win_width, win_height = 700, 500
BACKGROUND = (200, 255, 255)
window = display.set_mode((win_width, win_height))
window.fill(BACKGROUND)
display.set_caption("Ping Pong")
clock = time.Clock()
FPS = 60

player_r = Player("racket.png", 40, 100, win_width - 50, 150, 3)
player_l = Player("racket.png", 40, 100, 10, 150, 3)

ball = GameSprite("tenis_ball.png", 40, 40, 300, 200, 0)

speed_x, speed_y = 3, 3

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(BACKGROUND)
    player_r.reset()
    player_l.reset()
    ball.reset()
    
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    
    if ball.rect.y > win_height - 40 or ball.rect.y < 0:
        speed_y *= -1
    

    if sprite.collide_rect(player_l, ball) or sprite.collide_rect(ball, player_r):
        speed_x *= -1

    player_r.update_r()
    player_l.update_l()

    
    display.update()
    clock.tick(FPS)
