import pygame
import math
import random

# ALL OF THE CLASSES ARE DEFINED IN THIS FILE
# THE METHOD'S PURPOSE ARE DESCRIBED IN main.py AT THEIR POINT OF USE

# ENEMY # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('enemy.png')
        self.image = pygame.transform.scale(self.image, (40, 50))
        self.rect = self.image.get_rect()
        self.health = 80
        self.direction = 0
        self.counter = 0
        self.increment = random.randint(1,3)
        self.directionChoice = random.randint(1,4)

    def setdirectionChoice(self,direction):
        self.directionChoice = direction

    def getdirectionChoice(self):
        return self.directionChoice

    def counterReset(self):
        self.counter = 0

    def incrementReset(self):
        self.increment = random.randint(1, 3)

    def movementCounter(self):
        self.counter += self.increment

    def getcounter(self):
        return self.counter

    def healthDecrease(self):
        self.health -=1

    def getHealth(self):
        return self.health

    def moveUp(self):
        self.direction = 1
        self.rect.y -= 0.25
        self.rect.x += 3
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self):
        self.direction = 2
        self.rect.y += 1
        self.rect.x -= 2.5
        if self.rect.y > 420:
            self.rect.y = 420

    def moveLeft(self):
        self.direction = 3
        self.rect.x -= 3
        self.rect.y -= 1
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self):
        self.direction = 4
        self.rect.x += 3
        self.rect.y += 1
        if self.rect.x > 770:
            self.rect.x = 770

    def getDirection(self):
        return self.direction





# SWORD # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Sword(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.images = []

        self.images.append(pygame.image.load('swordswipe3.png'))
        #self.images.append(pygame.image.load('swordswipe2.png'))
        self.images.append(pygame.image.load('swordswipe3.png'))
        self.images.append(pygame.image.load('swordswipe4.png'))
        self.images.append(pygame.image.load('swordswipe5.png'))
        self.images.append(pygame.image.load('swordswipe5.png'))
        self.images.append(pygame.image.load('swordswipe6.png'))
        self.images.append(pygame.image.load('swordswipe6.png'))
        self.images.append(pygame.image.load('swordswipe7.png'))
        self.images.append(pygame.image.load('swordswipe8.png'))
        self.images.append(pygame.image.load('swordswipe3.png'))
        self.images.append(pygame.image.load('swordswipe3.png'))
        self.images.append(pygame.image.load('swordswipe3.png'))

        self.walkingimages = []

        self.walkingimages.append(pygame.image.load('swordswipe3.png'))
        self.walkingimages.append(pygame.image.load('swordswipe3.png'))
        self.walkingimages.append(pygame.image.load('swordswipe3.png'))
        self.walkingimages.append(pygame.image.load('swordswipe3.png'))
        self.walkingimages.append(pygame.image.load('swordswipe5.png'))
        self.walkingimages.append(pygame.image.load('swordswipe6.png'))
        self.walkingimages.append(pygame.image.load('swordswipe3.png'))
        self.walkingimages.append(pygame.image.load('swordswipe4.png'))
        self.walkingimages.append(pygame.image.load('swordswipe4.png'))
        self.walkingimages.append(pygame.image.load('swordswipe8.png'))
        self.walkingimages.append(pygame.image.load('swordswipe3.png'))
        self.walkingimages.append(pygame.image.load('swordswipe3.png'))
        self.walkingimages.append(pygame.image.load('swordswipe3.png'))


        self.isLeft = False
        self.index = 0
        self.index1 = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (60, 35))
        self.rect = self.image.get_rect()
        self.finished = False

    def reset(self):
        self.image = (pygame.image.load('swordswipe3.png'))
        self.image = pygame.transform.scale(self.image, (60, 35))
        if self.isLeft:
            self.image = pygame.transform.flip(self.image, True, False)
        self.index1 = 0

    def walking(self):
        self.index1 += 0.2

        if math.ceil(self.index1) >= len(self.walkingimages):
            self.index1 = 0

        self.image = self.walkingimages[math.ceil(self.index1)]
        self.image = pygame.transform.scale(self.image, (60, 35))
        if self.isLeft:
            self.image = pygame.transform.flip(self.image, True, False)

    def directionCheck(self):
        if self.isLeft:
            self.image = pygame.transform.flip(self.image, True, False)

    def swing(self):
        self.index += 0.5

        if math.ceil(self.index) >= len(self.images):
            self.index = 0
            self.finished = True

        self.image = self.images[math.ceil(self.index)]
        self.image = pygame.transform.scale(self.image, (60, 35))

        if self.finished:
            self.finished = False
            return True

    def Left(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.isLeft = True

    def Right(self):
        self.isLeft = False

# BIRD # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.images = []

        self.images.append(pygame.image.load('bird1.png'))
        self.images.append(pygame.image.load('bird2.png'))
        self.images.append(pygame.image.load('bird3.png'))

        self.option = [True,False]
        self.UorD = random.choice(self.option)
        self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (30, 20))
        self.rect = self.image.get_rect()

    def update(self):
        self.index += 0.1

        if math.ceil(self.index) >= len(self.images):
            self.index = 0

        self.image = self.images[math.ceil(self.index)]
        self.image = pygame.transform.scale(self.image, (30, 20))
        if self.UorD:
            self.rect.x -= 5
            option = [1,2,3,4]
            self.rect.y -= random.choice(option)
            self.image = pygame.transform.rotate(self.image, -10)
        else:
            self.rect.x -= 5
            option = [1, 2,3,4]
            self.rect.y += random.choice(option)
            self.image = pygame.transform.rotate(self.image,15)

# Ring # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Ring(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ring.png')
        self.image = pygame.transform.scale(self.image, (30,10))
        self.rect = self.image.get_rect()


# Block # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('art (28).png')
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_rect()


# Platform # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Platform(Block):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('platform.png')
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_rect()


# Background # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('art (32).png')
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 2


# Player # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []

        self.images.append(pygame.image.load('all walk4.png'))
        self.images.append(pygame.image.load('all walk12.png'))
        self.images.append(pygame.image.load('all walk11.png'))
        self.images.append(pygame.image.load('all walk10.png'))
        self.images.append(pygame.image.load('all walk9.png'))
        self.images.append(pygame.image.load('all walk8.png'))
        self.images.append(pygame.image.load('all walk7.png'))
        self.images.append(pygame.image.load('all walk6.png'))
        self.images.append(pygame.image.load('all walk5.png'))
        self.images.append(pygame.image.load('all walk1.png'))
        self.images.append(pygame.image.load('all walk2.png'))
        self.images.append(pygame.image.load('all walk3.png'))
        self.images.append(pygame.image.load('all walk4.png'))


        self.index = 0
        self.index1 = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (40, 50))
        self.rect = self.image.get_rect()
        self.isLeft = False


    def fall(self):
        self.rect.y += 7

    def idle(self):
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (40, 50))
        self.index = 0
        if self.isLeft:
            self.image = pygame.transform.flip(self.image, True, False)

    def moving(self):
        self.index += 0.2

        if math.ceil(self.index) >= len(self.images):
            self.index = 0

        self.image = self.images[math.ceil(self.index)]
        self.image = pygame.transform.scale(self.image, (40, 50))
        if self.isLeft:
            self.image = pygame.transform.flip(self.image, True, False)
        return True

    def moveUp(self, speed):
        self.rect.y -= 0.25
        self.rect.x += 3
        self.isLeft = False
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, speed):
        self.rect.y += 1
        self.rect.x -= 2.5
        self.isLeft = True
        if self.rect.y > 420:
            self.rect.y = 420

    def moveLeft(self, speed):
        self.rect.x -= speed
        self.rect.y -= 1
        self.isLeft = True
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, speed):
        self.rect.x += speed
        self.rect.y += 1
        self.isLeft = False
        if self.rect.x > 770:
            self.rect.x = 770


# GroundDetails # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class GroundDetails(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.grassImages = []
        self.grassImages.append(pygame.image.load('art (36).png'))
        self.grassImages.append(pygame.image.load('art (35).png'))
        self.grassImages.append(pygame.image.load('art (34).png'))

        self.pebbleImages = []
        self.pebbleImages.append(pygame.image.load('pebble1.png'))
        self.pebbleImages.append(pygame.image.load('pebble 2.png'))
        self.pebbleImages.append(pygame.image.load('pebble3.png'))

        self.flowerImages = []
        self.flowerImages.append(pygame.image.load('flower1.png'))
        self.flowerImages.append(pygame.image.load('flower1.png'))
        self.flowerImages.append(pygame.image.load('flower1.png'))
        self.flowerImages.append(pygame.image.load('flower1.png'))
        self.flowerImages.append(pygame.image.load('flower2.png'))
        self.flowerImages.append(pygame.image.load('flower3.png'))
        self.flowerImages.append(pygame.image.load('flower3.png'))

        self.image = self.grassImages[0]
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (10,20))

    def GrassImageSelect(self):
        self.image = self.grassImages[random.randrange(0,3)]
        self.image = pygame.transform.scale(self.image, (random.randrange(10,12), random.randrange(25,30)))

    def PebbleImageSelect(self):
        self.image = self.pebbleImages[random.randrange(0,3)]
        self.image = pygame.transform.scale(self.image, (random.randrange(3,6), random.randrange(2,4)))

    def FlowerImageSelect(self):
        self.image = self.flowerImages[random.randrange(0, 7)]
        self.image = pygame.transform.scale(self.image, (random.randrange(10, 12), random.randrange(15, 18)))




# Clouds # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []

        self.images.append(pygame.image.load('largeCloud.png'))
        self.images.append(pygame.image.load('medCloud.png'))
        self.images.append(pygame.image.load('smallCloud.png'))

        self.choice = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def selection(self):
        self.choice = random.randint(1, 3)
        if self.choice == 1:
            self.image = self.images[0]
        elif self.choice == 2:
            self.image = self.images[1]
        else:
            self.image = self.images[2]

    def update(self):
        self.rect.x -= 3














