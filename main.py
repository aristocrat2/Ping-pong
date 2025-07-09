import pygame
#大山豆根豆腐干
win = pygame.display.set_mode((700, 500))

clock = pygame.time.Clock()

win.fill((0, 220, 255))

is_game = True

class GameSprite(pygame.sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 415:
            self.rect.y += self.speed
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 620, 200, 4, 50, 150)
ball = Player('tenis_ball.png', 300, 200, 4, 50, 50)
while is_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False

    racket2.reset()
    racket1.reset()
    ball.reset()

    pygame.display.update()
    clock.tick(40)