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

win_width, win_height = 700, 500
BACKGROUND = (200, 255, 255)
window = display.set_mode((win_width, win_height))
window.fill(BACKGROUND)
display.set_caption("Ping Pong")
clock = time.Clock()
FPS = 60

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


  
    display.update()
    clock.tick(FPS)
