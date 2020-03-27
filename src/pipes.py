from settings import WINDOWWIDTH, XVELOCITY

from random import randint
import pygame

GAPBEFOREFIRSTPIPE = WINDOWWIDTH + (WINDOWWIDTH / 2)

PIPEGAPSPACE = 100
MINRANDOMPIPETOP = 90
MAXRANDOMPIPETOP = 210

class PairPipe:

    def __init__(self, sprite, x):
        self.sprite = sprite
        self.image = sprite.image
        self.reversedImage = pygame.transform.rotate(sprite.image, 180)

        self.x = x
        self.yUp = 0
        self.yDown = 0
        self.passed = False

        self._getRandomYPosition()

    def _getRandomYPosition(self):
        r = randint(MINRANDOMPIPETOP, MAXRANDOMPIPETOP)
        self.yDown = -self.sprite.height + r
        self.yUp = r + PIPEGAPSPACE

class Pipes:

    def __init__(self, sprite, hitBoxe):
        self.pipes = [
            PairPipe(sprite, GAPBEFOREFIRSTPIPE),
            PairPipe(sprite, GAPBEFOREFIRSTPIPE + WINDOWWIDTH / 2),
            PairPipe(sprite, GAPBEFOREFIRSTPIPE + WINDOWWIDTH),
            PairPipe(sprite, GAPBEFOREFIRSTPIPE + WINDOWWIDTH + WINDOWWIDTH / 2)
        ]
        self.upHitMask = hitBoxe.getHitMask(pygame.transform.rotate(sprite.image, 180), sprite.width, sprite.height)
        self.bottomHitMask = hitBoxe.getHitMask(sprite.image, sprite.width, sprite.height)

    def drawInGame(self, window):
        for pipe in self.pipes:
            window.blit(pipe.image, (pipe.x, pipe.yUp))
            window.blit(pipe.reversedImage, (pipe.x, pipe.yDown))

            if pipe.x > -pipe.sprite.width:
                pipe.x -= XVELOCITY
            else:
                pipe.x = WINDOWWIDTH * 2 - pipe.sprite.width
                pipe._getRandomYPosition()
                pipe.passed = False

    def drawInGameOver(self, window):
        for pipe in self.pipes:
            window.blit(pipe.image, (pipe.x, pipe.yUp))
            window.blit(pipe.reversedImage, (pipe.x, pipe.yDown))
