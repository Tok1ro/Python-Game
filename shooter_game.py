#improts
from operator import truediv
from pickletools import pystring
from time import time
from turtle import speed
import pygame
import random

#variables
FPS = 60
game=True
UfoArray = pygame.sprite.Group()
timer = 0
bullets = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
hp = 6
points = 0
healArray = pygame.sprite.Group()
pygame.font.init()

font = pygame.font.Font('font/a_FuturaRound Bold.ttf', 65)
hpLabel = font.render('HP ' + str(hp),True,(255,255,255))
pointLabel = font.render('KILLS ' + str(points),True,(255,255,255))

#class
class Sprite(pygame.sprite.Sprite):
    def __init__(self,x,y, w, h, imagefile,speed = 5):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,w,h)
        self.image = pygame.image.load(imagefile)
        self.image = pygame.transform.scale(self.image, (w,h))
        self.speed = speed
    def ShowSprite(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys = pygame.key.get_pressed() 
        if(keys[pygame.K_LEFT]):
            self.rect.x -=5
        if(keys[pygame.K_RIGHT]):
            self.rect.x +=5
            

class Ufo(Sprite):
    def update(self):
        self.rect.y += self.speed
        
class Bullet(Sprite):
    def update(self):
        self.rect.y -= self.speed
class Asteroid(Sprite):
    def update(self):
        self.rect.y += self.speed
class Heal(Sprite):
    def update(self):
        self.rect.y += self.speed

# creating objects
win=pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

HealthItem = Heal(320,440 , 60,60, 'images/HealItem.png')

player = Sprite(320,440 , 60,60, 'images/rocket.png')
for i in range(5):
    enemy = Ufo(random.randint(0,11) * 60, random.randint(-300,-150), 65,40, 'images/ufo.png', random.randint(1,5))
    UfoArray.add(enemy)

backgound = pygame.image.load('images/galaxy.jpg')
backgound = pygame.transform.scale(backgound, (700, 500))
GameOverSprite = pygame.image.load('images/game-over-screen.jpg')
GameOverSprite = pygame.transform.scale(GameOverSprite, (700, 500))
# update display
pygame.display.update()

# while 1
while game:
    win.blit(backgound, (0,0))
    # delay
    clock.tick(FPS)
    timer += 1
    if(timer % 60 == 0):
        enemy = Ufo(random.randint(0,11) * 60, random.randint(-300,-150), 65,40, 'images/ufo.png', random.randint(1,5))
        UfoArray.add(enemy)
    if(timer % 180 == 0):
        asteroid = Asteroid(random.randint(0,11) * 60, random.randint(-300,-150), 65,40, 'images/asteroid.png', random.randint(1,5))
        asteroidGroup.add(asteroid)
    if(timer % 200 == 0):
        healSpawn = Heal(random.randint(0,11) * 60, random.randint(-300,-150), 65,40, 'images/HealItem.png', random.randint(1,5))
        healArray.add(healSpawn)
        
    if(pygame.sprite.groupcollide(UfoArray,bullets, True, True)):
        points += 1
        pointLabel = font.render('KILLS ' + str(points),True,(255,255,255))
    pygame.sprite.groupcollide(asteroidGroup,bullets, False, True)
    
    # while 2
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game=False
        if(i.type == pygame.KEYDOWN):
            if(i.key == pygame.K_SPACE):
                bullets.add(Bullet(player.rect.centerx - 12, player.rect.top, 20,20, 'images/bullet.png', 4))
            
    for e in healArray:
        if(player.rect.colliderect(e.rect)):
            print('+hp')
            hp += 3
            hpLabel = font.render('HP' + str(hp),True,(255,255,255))
            healArray.remove(e)
            
    for e in asteroidGroup:
        if(player.rect.colliderect(e.rect)):
            print('oyyy')
            hp -= 2
            hpLabel = font.render('HP' + str(hp),True,(255,255,255))
            asteroidGroup.remove(e)
    for e in UfoArray:
        if(player.rect.colliderect(e.rect)):
            print('oyyy noo')
            hp -= 1
            hpLabel = font.render('HP' + str(hp),True,(255,255,255))
            UfoArray.remove(e)
    if(hp <= 0):
        game = False
            
    player.update()
    UfoArray.update()
    bullets.update()
    asteroidGroup.update()
    healArray.update()
    player.ShowSprite()
    win.blit(hpLabel, (40,20))
    win.blit(pointLabel, (40,80))
    
    for k in UfoArray:
        k.ShowSprite()
    for b in bullets:
        b.ShowSprite()
    for a in asteroidGroup:
        a.ShowSprite()
    for a in healArray:
        a.ShowSprite()
    # update display again
    pygame.display.update()
game = True
PointControll = font.render('YOU RESULT IS  ' + str(points),True,(150,0,0))
# while 3
while game:
    win.fill((125,125,125))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game=False
    win.blit(PointControll, (50,150))
    pygame.display.update()