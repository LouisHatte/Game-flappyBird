from settings import XVELOCITY

import pygame

XSHIFT = -48

class Base:

    def __init__(self, sprite):
        self.sprite = sprite
        self.xShift = XSHIFT

    def drawInGame(self, window):
        window.blit(self.sprite.image, (self.sprite.x, self.sprite.y))

        if self.sprite.x > self.xShift:
            self.sprite.x -= XVELOCITY
        else:
            self.sprite.x = 0

    def drawInGameOver(self, window):
        window.blit(self.sprite.image, (self.sprite.x, self.sprite.y))
