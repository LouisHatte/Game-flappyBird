import pygame
from random import randint

class Sprite:

    def __init__(self, sprite, x, y, width, height):
        self.image = sprite
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Sprites:

    def __init__(self):
        self.backgrounds = {
            'backgroundDay': Sprite(pygame.image.load('../assets/sprites/background-day.png'), 0, 0, 288, 512),
            'backgroundNight': Sprite(pygame.image.load('../assets/sprites/background-night.png'), 0, 0, 288, 512)
        }
        self.birds = {
            'yellowBird': [
                Sprite(pygame.image.load('../assets/sprites/yellowbird-midflap.png'), 65, 235, 34, 24),
                Sprite(pygame.image.load('../assets/sprites/yellowbird-downflap.png'), 65, 235, 34, 24),
                Sprite(pygame.image.load('../assets/sprites/yellowbird-midflap.png'), 65, 235, 34, 24),
                Sprite(pygame.image.load('../assets/sprites/yellowbird-upflap.png'), 65, 235, 34, 24)
            ],
            'redBird': [
                Sprite(pygame.image.load('../assets/sprites/redbird-midflap.png'), 65, 235, 34, 24),
                Sprite(pygame.image.load('../assets/sprites/redbird-downflap.png'), 65, 235, 34, 24),
                Sprite(pygame.image.load('../assets/sprites/redbird-midflap.png'), 65, 235, 34, 24),
                Sprite(pygame.image.load('../assets/sprites/redbird-upflap.png'), 65, 235, 34, 24)
            ],
            'blueBird': [
                Sprite(pygame.image.load('../assets/sprites/bluebird-midflap.png'), 65, 235, 34, 24),
                Sprite(pygame.image.load('../assets/sprites/bluebird-downflap.png'), 65, 235, 34, 24),
                Sprite(pygame.image.load('../assets/sprites/bluebird-midflap.png'), 65, 235, 34, 24),
                Sprite(pygame.image.load('../assets/sprites/bluebird-upflap.png'), 65, 235, 34, 24)
            ]
        }
        self.pipes = {
            'greenPipe': Sprite(pygame.image.load('../assets/sprites/pipe-green.png'), 0, 0, 52, 320),
            'redPipe': Sprite(pygame.image.load('../assets/sprites/pipe-red.png'), 0, 0, 52, 320)
        }
        self.numbers = [
            Sprite(pygame.image.load('../assets/sprites/0.png'), 0, 51, 24, 36),
            Sprite(pygame.image.load('../assets/sprites/1.png'), 0, 51, 16, 36),
            Sprite(pygame.image.load('../assets/sprites/2.png'), 0, 51, 24, 36),
            Sprite(pygame.image.load('../assets/sprites/3.png'), 0, 51, 24, 36),
            Sprite(pygame.image.load('../assets/sprites/4.png'), 0, 51, 24, 36),
            Sprite(pygame.image.load('../assets/sprites/5.png'), 0, 51, 24, 36),
            Sprite(pygame.image.load('../assets/sprites/6.png'), 0, 51, 24, 36),
            Sprite(pygame.image.load('../assets/sprites/7.png'), 0, 51, 24, 36),
            Sprite(pygame.image.load('../assets/sprites/8.png'), 0, 51, 24, 36),
            Sprite(pygame.image.load('../assets/sprites/9.png'), 0, 51, 24, 36)
        ]
        self.base = Sprite(pygame.image.load('../assets/sprites/base.png'), 0, 400, 336, 112)
        self.message = Sprite(pygame.image.load('../assets/sprites/message.png'), 52, 50, 184, 267)
        self.gameOver = Sprite(pygame.image.load('../assets/sprites/gameover.png'), 50, 180, 192, 42)

        self.background = self.setBackground()
        self.bird = self.setBird()
        self.pipe = self.setPipe()

    def setRandomSprites(self):
        self.background = self.setBackground()
        self.bird = self.setBird()
        self.pipe = self.setPipe()

    def setBackground(self):
        r = randint(0, 1)
        if r == 0:
            return self.backgrounds['backgroundDay']
        else:
            return self.backgrounds['backgroundNight']

    def setBird(self):
        r = randint(0, 2)
        if r == 0:
            return self.birds['yellowBird']
        elif r == 1:
            return self.birds['redBird']
        else:
            return self.birds['blueBird']

    def setPipe(self):
        r = randint(0, 1)
        if r == 0:
            return self.pipes['greenPipe']
        else:
            return self.pipes['redPipe']
